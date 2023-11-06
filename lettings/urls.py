from django.urls import path
from . import views


# def trigger_error(request):
#   division_by_zero = 1 / 0


urlpatterns = [
    path('lettings/', views.lettings_index, name='lettings'),
    # Détails d'une location par son ID
    path('lettings/<int:letting_id>/', views.letting, name='letting'),

]
