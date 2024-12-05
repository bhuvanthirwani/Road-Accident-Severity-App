from django.urls import path
from .views import register_user, login_user, logout_user, home, add_data, update_entry,list_data,list_data_api, modify_specific_data, road_accident_prediction, get_current_data

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('home/', home, name='home'),
    path('add-data/', add_data, name='add_data'),
    # path('data-modification/', modify_data, name='modify_data'),
    path('modify-page/<str:entry_id>/', modify_specific_data, name='modify_specific_data'),
    path('update-entry/', update_entry, name='update_entry'),
    path('list-data/', list_data, name='list_user_data'),
    path('list-data-api/', list_data_api, name='list_data_api'),
    path('get-current-data/<str:entry_id>/', get_current_data, name='get_current_data'),
    path('prediction/', road_accident_prediction, name='road_accident_prediction'),
]