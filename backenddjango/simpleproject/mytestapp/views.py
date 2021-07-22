from django.http import HttpResponse
from prometheus_client import Summary, Gauge, Counter
import random
import time
gauge = Gauge('request_fake_workload_seconds', 'A silly gauge', ['mylabel'])

def get_fake_workload_seconds():

    if 'fake_workload_values' not in get_fake_workload_seconds.__dict__:
        get_fake_workload_seconds.fake_workload_values = [int(random.random() * 10), int(random.random() * 10), int(random.random() * 10)]
        get_fake_workload_seconds.last_time = time.time()

    if (time.time() - get_fake_workload_seconds.last_time) > 300:
        get_fake_workload_seconds.fake_workload_values = [int(random.random() * 10), int(random.random() * 10), int(random.random() * 10)]
        get_fake_workload_seconds.last_time = time.time()

    return get_fake_workload_seconds.fake_workload_values
    

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@REQUEST_TIME.time()
def index(request):
    labels = ['PC01', 'PC02', 'PC03']
    values = get_fake_workload_seconds()
    for label, value in zip(labels, values):
        time.sleep(value)
        gauge.labels(mylabel = label).set(value)   

    return HttpResponse("Hello, world. This is just a simple response.")

