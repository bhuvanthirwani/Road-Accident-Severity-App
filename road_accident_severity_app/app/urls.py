from django.urls import path
from .views import register_user, login_user, logout_user, home, add_data
from .views import update_entry,list_data,list_data_api, modify_specific_data, guidelines, get_current_data 
from .views import get_variables, predict, visualization_page, generate_chart, eda, model_results, delete_data

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    # path('/', login_user, name='login'),
    # path('', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('home/', home, name='home'),
    path('add-data/', add_data, name='add_data'),
    # path('data-modification/', modify_data, name='modify_data'),
    path('modify-page/<str:entry_id>/', modify_specific_data, name='modify_specific_data'),
    path('delete-data/', delete_data, name='delete_data'),
    path('update-entry/', update_entry, name='update_entry'),
    path('list-data/', list_data, name='list_user_data'),
    path('list-data-api/', list_data_api, name='list_data_api'),
    path('get-current-data/<str:entry_id>/', get_current_data, name='get_current_data'),
    path('prediction/', predict, name='road_accident_prediction_page'),
    path("get-variables/", get_variables, name="get_variables"),
    path("predict/", predict, name="predict"),
    path("visualization-page/", visualization_page, name="visualization_page"),
    path('generate-chart/', generate_chart, name='generate_chart'),
    path('eda/', eda, name='eda'),
    path('model-results/', model_results, name='model_results'),
    path('guidelines/', guidelines, name='guidelines'),
    
]