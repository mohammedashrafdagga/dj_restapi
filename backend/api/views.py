from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):
    print(request.body)
    body = request.body
    # convert body to dict
    data = {}
    try:
        data = json.loads(body)
    except:
        pass

    print(data)
    print(request.GET)
    print(request.POST)
    # prams
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    return JsonResponse(data)
