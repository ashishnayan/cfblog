import json
import traceback
from django.utils.dateparse import parse_datetime

from django.core.cache import cache
from django.http.response import HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST

from .models import Content
from .response import render, render_content
from .utils import user_passes_test
from .signals import pre_publish_signal, post_publish_signal

__author__ = 'vinay'


def cms_page_index(request):
    return render(request)


@require_POST
@csrf_protect
@user_passes_test()
def save(request, save_type):
    if not request.is_ajax():
        return HttpResponseForbidden()

    post_data = request.POST

    if any(_ not in post_data for _ in ('auth_data', 'cms_page_id')):
        return JsonResponse({'success': False}, status=400)

    if save_type not in ('draft', 'publish'):
        return JsonResponse({'success': False}, status=400)

    cms_page = get_object_or_404(Content, id=post_data['cms_page_id'])
    draft_date = parse_datetime(post_data['draft_modified'])

    if draft_date < cms_page.modified_on:
        return JsonResponse(
            {
                'success': False,
                'draft_error': True,
                'message': 'Draft data was out of date'
            },
            status=200
        )

    try:
        content = json.loads(post_data['auth_data'])
    except:
        return JsonResponse(
            {
                'success': False,
                'message': 'Invalid JSON object'
            },
            status=400
         )
    else:
        cms_page.auth_data.update(content)
        try:
            template_context = cache.get(
                'template_context_{}'.format(cms_page.id)
            )
            render_content(cms_page, request=request,
                           template_context=template_context)
        except Exception as e:
            return JsonResponse(
                {'success': False,
                 'message': 'Unable to parse the new content.\n'
                 'Please check the console for issues.',
                 'exception': unicode(e),
                 'traceback': traceback.format_exc()}
            )
        else:
            if save_type == 'draft':
                cms_page.save()
            else:
                pre_signal_response = pre_publish_signal.send(
                    sender=cms_page._meta.model,
                    cms_page=cms_page
                )
                for v1, v2 in pre_signal_response:
                    if not v1:
                        return JsonResponse(
                            {
                                'success': False,
                                'meta_tag_error': True,
                                'message': v2
                            },
                            status=200
                        )

                cms_page.publish_cms_content()
                post_publish_signal.send(
                    sender=cms_page._meta.model,
                    cms_page=cms_page
                )

            return JsonResponse({'success': True})
