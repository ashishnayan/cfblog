cfblog ChangeLog
================
0.2.3 - 12-Apr-2016
-------------------
* added pre and post publish signals

* added can_publish permission

* added validation on out of date data stored in localstorage and restricted it from being published.

0.2.2 - 26-Nov-2015
-------------------

* changed datetime.now to timezone.now in publish field

* fixed issue where editing page fails if cms_data contains script tag

* fixed issue where base and snippet templates load different csrf_token

0.2.1 - 29-Oct-2015
-------------------

* Content instance is available inside the templates as `cms_content`. This is only available to those which are rendered using Content model.

0.2.0 - 28-Oct-2015
-------------------

* `*` is added to fields that are markdown supported.

* lazy importing 'cms_page_index` inside middleware.

* major rework to the structure of cfblog

* removed html caching

* caching the validated templates using lru_cache

* split single render function to three functions

* added template context support for the templates being rendered by cfblog

* modified dum_request to be able to get passed to view

0.1.9 - 20-Oct-2015
-------------------

* fixed issues #12, #13 and #14

* scripts and templates install in package folder.

* replaced `request.path` usage with `request.path_info`.

* added catchall url to fix the `csrf_token` being loaded as `NOTPROVIDED`.

* `process_response` now catches all the exceptions similar to flatpage middleware and return the original response.

* rewrote ContentManager to support chaining custom methods.

* added proper post notification on post failure.

0.1.8 - 15-Oct-2015
-------------------

* bug fix for `__getitem__` on CacheObject

0.1.7 - 14-Oct-2015
-------------------

* added view on site option at admin list_display.
* added MANIFEST template to include static and templates in the package.
* pre loading localStorage value in the editor if exists.
* bug fixes while publishing content.

0.1.6 - 9-Oct-2015
------------------

* not escaping html elements while parsing through markdown
* added tests for this change

0.1.5 - 9-Oct-2015
------------------

* changed requirement from `django-jsonfield` to `jsonfield`

0.1.4 - 9-Oct-2015
------------------

* restricted static page category deletion from admin page instead of `AssertionError`

0.1.3 - 9-Oct-2015
------------------

* middleware is now called `cfblog.Middleware` [Backward Incompatible]

0.1.2 - 8-Oct-2015
------------------

* added `blank=True` for auth_data and public_data fields

0.1.1 - 8-Oct-2015
------------------

* fixed a typo in readme

0.1.0 - 8-Oct-2015
------------------

* first release

