from django.urls import path
from . import views

urlpatterns = [
    path('add_review/', views.add_review, name='add_review'),
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('reviews/json/', views.show_json, name='show_json'),
    path('reviews/json/<int:id>/', views.show_json_by_id, name='show_json_by_id'),
]
