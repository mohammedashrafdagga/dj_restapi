from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    return JsonResponse({'message': 'Hello There, Welcome in First Api View'})
