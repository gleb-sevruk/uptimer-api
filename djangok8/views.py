import datetime
from time import perf_counter

from django.http import HttpResponse
from rest_framework import mixins, viewsets

from .models import Job
from .serializers import JobSerializer

import logging
my_logger = logging.getLogger(__name__)


class JobViewSet(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):
    """
    API endpoint that allows jobs to be viewed or created.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer


def test_func(request):
    ts = perf_counter()

    my_logger.info('Hello Graylog2. ' + str(datetime.datetime.now().isoformat()), extra={'extra_1': 'ti che???'} )
    my_logger.info('Hello a?.' + str(datetime.datetime.now().isoformat()), extra={'extra_2': 'nu net'}  )
    my_logger.info('Hello b?.' + str(datetime.datetime.now().isoformat()) )

    print('aaa')
    te = perf_counter()
    diff = te - ts
    ms_elapsed = round(diff * 1000, 2)
    my_logger.info('test_func timings', extra={
        'execution_time': ms_elapsed,
    })


    return HttpResponse('шутки шутишь?')