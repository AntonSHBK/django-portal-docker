from django.shortcuts import render
from django.conf import settings


def page_not_found_view_404(request, exception):
    return render(request, f'{settings.ERRORS_TAMPLATES_PATH}/404.html', status=404)

def page_internal_server_error_500(request):
    return render(request, f'{settings.ERRORS_TAMPLATES_PATH}/500.html', status=500)