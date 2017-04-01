from django.http import HttpResponse

from dummyapp import tasks


def foo(request):
    r = tasks.add.delay(1,2)
    return HttpResponse(r.task_id)
