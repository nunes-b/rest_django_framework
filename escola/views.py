from django.http import JsonResponse


def get_student(request):
    if request.method == 'GET':
        student = {'id': 1, 'name': 'João'}
        return JsonResponse(student)
