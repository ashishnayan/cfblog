from django.dispatch import Signal

"""
    pre_publish_signal should return list of tuples with two elements.
    Frist element of the tuple should be boolean and the second one should be
    string.
    e.g. [(True, "Tag name: Success",), (False, "Tag Name: Error Message",)...]
"""
pre_publish_signal = Signal(providing_args=["cms_page"])
post_publish_signal = Signal()
