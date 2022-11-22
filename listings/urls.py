from django.urls import path
from .import views

app_name = 'listings'

urlpatterns = [
    #Homepage
    path('', views.index, name='index'),

    # Listing page
    path('all_listings/', views.all_listings, name='all_listings'),

    # New listing
    path('new_listing/', views.new_listing, name='new_listing'),
    
    # Detail listing page
    path('all_listings/<detail_id>/', views.detail, name='detail'),

    # My listing
    path('my_listings/', views.my_listings, name='my_listings'),

    # Edit listing
    path('edit_listing/<edit_id>/', views.edit_listing, name='edit_listing'),

    # Delete listing
    path('delete_listing/<delete_id>/', views.delete_listing, name="delete_listing"),
]
