import json
import os
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import uuid
from db.connect import get_db
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import pickle
import numpy as np
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.http import JsonResponse
from db.connect import get_db
# from middleware.auth import is_logged_in
from utils.auth import hash_password, verify_password
from bson import ObjectId
from django.views.decorators.csrf import csrf_exempt
from django.templatetags.static import static
y_map = {'Accident_severity': {
        'slight injury': 2, 'serious injury': 1, 'fatal injury': 0,
        }}

# features = [
#     'Time_of_day', 'Sex_of_driver_male', 'Sex_of_driver_unknown', 'Vehicle_driver_relation_other',
#     'Vehicle_driver_relation_owner', 'Vehicle_driver_relation_unknown', 'Type_of_vehicle_bajaj',
#     'Type_of_vehicle_bicycle', 'Type_of_vehicle_long lorry', 'Type_of_vehicle_lorry (11 - 40 q)',
#     'Type_of_vehicle_lorry (41 - 100 q)', 'Type_of_vehicle_motorcycle', 'Type_of_vehicle_other',
#     'Type_of_vehicle_pick up upto 10q', 'Type_of_vehicle_public (12 seats)',
#     'Type_of_vehicle_public (13 - 45 seats)', 'Type_of_vehicle_public (> 45 seats)',
#     'Type_of_vehicle_ridden horse', 'Type_of_vehicle_special vehicle', 'Type_of_vehicle_stationwagen',
#     'Type_of_vehicle_taxi', 'Type_of_vehicle_turbo', 'Type_of_vehicle_unknown', 'Defect_of_vehicle_7',
#     'Defect_of_vehicle_no defect', 'Area_accident_occured_hospital areas',
#     'Area_accident_occured_industrial areas', 'Area_accident_occured_market areas',
#     'Area_accident_occured_office areas', 'Area_accident_occured_other',
#     'Area_accident_occured_outside rural areas', 'Area_accident_occured_recreational areas',
#     'Area_accident_occured_residential areas', 'Area_accident_occured_rural office areas',
#     'Area_accident_occured_rural village areas', 'Area_accident_occured_school areas',
#     'Area_accident_occured_unknown', 'Lanes_or_Medians_one way', 'Lanes_or_Medians_other',
#     'Lanes_or_Medians_two-way (divided with broken lines road marking)',
#     'Lanes_or_Medians_two-way (divided with solid lines road marking)', 'Lanes_or_Medians_undivided two way',
#     'Lanes_or_Medians_unknown', 'Road_allignment_gentle horizontal curve',
#     'Road_allignment_sharp reverse curve', 'Road_allignment_steep grade downward with mountainous terrain',
#     'Road_allignment_steep grade upward with mountainous terrain', 'Road_allignment_tangent road with flat terrain',
#     'Road_allignment_tangent road with mild grade and flat terrain', 'Road_allignment_tangent road with mountainous terrain',
#     'Road_allignment_tangent road with rolling terrain', 'Road_allignment_unknown', 'Types_of_Junction_no junction',
#     'Types_of_Junction_o shape', 'Types_of_Junction_other', 'Types_of_Junction_t shape',
#     'Types_of_Junction_unknown', 'Types_of_Junction_x shape', 'Types_of_Junction_y shape',
#     'Road_surface_type_asphalt roads with some distress', 'Road_surface_type_earth roads',
#     'Road_surface_type_gravel roads', 'Road_surface_type_other', 'Road_surface_type_unknown',
#     'Light_conditions_darkness - lights unlit', 'Light_conditions_darkness - no lighting',
#     'Light_conditions_daylight', 'Weather_conditions_fog or mist', 'Weather_conditions_normal',
#     'Weather_conditions_other', 'Weather_conditions_raining', 'Weather_conditions_raining and windy',
#     'Weather_conditions_snow', 'Weather_conditions_unknown', 'Weather_conditions_windy',
#     'Type_of_collision_collision with pedestrians', 'Type_of_collision_collision with roadside objects',
#     'Type_of_collision_collision with roadside-parked vehicles', 'Type_of_collision_fall from vehicles',
#     'Type_of_collision_other', 'Type_of_collision_rollover', 'Type_of_collision_unknown',
#     'Type_of_collision_vehicle with vehicle collision', 'Type_of_collision_with train', 'Vehicle_movement_getting off',
#     'Vehicle_movement_going straight', 'Vehicle_movement_moving backward', 'Vehicle_movement_other',
#     'Vehicle_movement_overtaking', 'Vehicle_movement_parked', 'Vehicle_movement_reversing',
#     'Vehicle_movement_stopping', 'Vehicle_movement_turnover', 'Vehicle_movement_u-turn',
#     'Vehicle_movement_unknown', 'Vehicle_movement_waiting to go', 'Casualty_class_na',
#     'Casualty_class_passenger', 'Casualty_class_pedestrian', 'Sex_of_casualty_male',
#     'Sex_of_casualty_na', 'Work_of_casuality_employee', 'Work_of_casuality_other',
#     'Work_of_casuality_self-employed', 'Work_of_casuality_student', 'Work_of_casuality_unemployed',
#     'Work_of_casuality_unknown', 'Fitness_of_casuality_deaf', 'Fitness_of_casuality_normal',
#     'Fitness_of_casuality_other', 'Fitness_of_casuality_unknown', 'Cause_of_accident_changing lane to the right',
#     'Cause_of_accident_driving at high speed', 'Cause_of_accident_driving carelessly',
#     'Cause_of_accident_driving to the left', 'Cause_of_accident_driving under the influence of drugs',
#     'Cause_of_accident_drunk driving', 'Cause_of_accident_getting off the vehicle improperly',
#     'Cause_of_accident_improper parking', 'Cause_of_accident_moving backward',
#     'Cause_of_accident_no distancing', 'Cause_of_accident_no priority to pedestrian',
#     'Cause_of_accident_no priority to vehicle', 'Cause_of_accident_other', 'Cause_of_accident_overloading',
#     'Cause_of_accident_overspeed', 'Cause_of_accident_overtaking', 'Cause_of_accident_overturning',
#     'Cause_of_accident_turnover', 'Cause_of_accident_unknown', 'Day_of_week_ordinal',
#     'Age_band_of_driver_ordinal', 'Educational_level_ordinal', 'Driving_experience_ordinal',
#     'Service_year_of_vehicle_ordinal', 'Road_surface_conditions_ordinal', 'Age_band_of_casualty_ordinal',
#     'Casualty_severity_ordinal'
# ]
features = [
    'Time_of_day', 'Sex_of_driver_male', 'Sex_of_driver_unknown', 'Vehicle_driver_relation_other',
    'Vehicle_driver_relation_owner', 'Vehicle_driver_relation_unknown', 'Type_of_vehicle_bajaj',
    'Type_of_vehicle_bicycle', 'Type_of_vehicle_long lorry', 'Type_of_vehicle_lorry (11 - 40 q)',
    'Type_of_vehicle_lorry (41 - 100 q)', 'Type_of_vehicle_motorcycle', 'Type_of_vehicle_other',
    'Type_of_vehicle_pick up upto 10q', 'Type_of_vehicle_public (12 seats)',
    'Type_of_vehicle_public (13 - 45 seats)', 'Type_of_vehicle_public (> 45 seats)',
    'Type_of_vehicle_ridden horse', 'Type_of_vehicle_special vehicle', 'Type_of_vehicle_stationwagen',
    'Type_of_vehicle_taxi', 'Type_of_vehicle_turbo', 'Type_of_vehicle_unknown', 'Defect_of_vehicle_7',
    'Defect_of_vehicle_no defect', 'Area_accident_occured_hospital areas',
    'Area_accident_occured_industrial areas', 'Area_accident_occured_market areas',
    'Area_accident_occured_office areas', 'Area_accident_occured_other',
    'Area_accident_occured_outside rural areas', 'Area_accident_occured_recreational areas',
    'Area_accident_occured_residential areas', 'Area_accident_occured_rural office areas',
    'Area_accident_occured_rural village areas', 'Area_accident_occured_school areas',
    'Area_accident_occured_unknown', 'Lanes_or_Medians_one way', 'Lanes_or_Medians_other',
    'Lanes_or_Medians_two-way (divided with broken lines road marking)',
    'Lanes_or_Medians_two-way (divided with solid lines road marking)', 'Lanes_or_Medians_undivided two way',
    'Lanes_or_Medians_unknown', 'Road_allignment_gentle horizontal curve',
    'Road_allignment_sharp reverse curve', 'Road_allignment_steep grade downward with mountainous terrain',
    'Road_allignment_steep grade upward with mountainous terrain', 'Road_allignment_tangent road with flat terrain',
    'Road_allignment_tangent road with mild grade and flat terrain', 'Road_allignment_tangent road with mountainous terrain',
    'Road_allignment_tangent road with rolling terrain', 'Road_allignment_unknown', 'Types_of_Junction_no junction',
    'Types_of_Junction_o shape', 'Types_of_Junction_other', 'Types_of_Junction_t shape',
    'Types_of_Junction_unknown', 'Types_of_Junction_x shape', 'Types_of_Junction_y shape',
    'Road_surface_type_asphalt roads with some distress', 'Road_surface_type_earth roads',
    'Road_surface_type_gravel roads', 'Road_surface_type_other', 'Road_surface_type_unknown',
    'Light_conditions_darkness - lights unlit', 'Light_conditions_darkness - no lighting',
    'Light_conditions_daylight', 'Weather_conditions_fog or mist', 'Weather_conditions_normal',
    'Weather_conditions_other', 'Weather_conditions_raining', 'Weather_conditions_raining and windy',
    'Weather_conditions_snow', 'Weather_conditions_unknown', 'Weather_conditions_windy',
    'Type_of_collision_collision with pedestrians', 'Type_of_collision_collision with roadside objects',
    'Type_of_collision_collision with roadside-parked vehicles', 'Type_of_collision_fall from vehicles',
    'Type_of_collision_other', 'Type_of_collision_rollover', 'Type_of_collision_unknown',
    'Type_of_collision_vehicle with vehicle collision', 'Type_of_collision_with train', 'Vehicle_movement_getting off',
    'Vehicle_movement_going straight', 'Vehicle_movement_moving backward', 'Vehicle_movement_other',
    'Vehicle_movement_overtaking', 'Vehicle_movement_parked', 'Vehicle_movement_reversing',
    'Vehicle_movement_stopping', 'Vehicle_movement_turnover', 'Vehicle_movement_u-turn',
    'Vehicle_movement_unknown', 'Vehicle_movement_waiting to go', 'Casualty_class_na',
    'Casualty_class_passenger', 'Casualty_class_pedestrian', 'Sex_of_casualty_male',
    'Sex_of_casualty_na', 'Work_of_casuality_employee', 'Work_of_casuality_other',
    'Work_of_casuality_self-employed', 'Work_of_casuality_student', 'Work_of_casuality_unemployed',
    'Work_of_casuality_unknown', 'Fitness_of_casuality_deaf', 'Fitness_of_casuality_normal',
    'Fitness_of_casuality_other', 'Fitness_of_casuality_unknown', 'Cause_of_accident_changing lane to the right',
    'Cause_of_accident_driving at high speed', 'Cause_of_accident_driving carelessly',
    'Cause_of_accident_driving to the left', 'Cause_of_accident_driving under the influence of drugs',
    'Cause_of_accident_drunk driving', 'Cause_of_accident_getting off the vehicle improperly',
    'Cause_of_accident_improper parking', 'Cause_of_accident_moving backward',
    'Cause_of_accident_no distancing', 'Cause_of_accident_no priority to pedestrian',
    'Cause_of_accident_no priority to vehicle', 'Cause_of_accident_other', 'Cause_of_accident_overloading',
    'Cause_of_accident_overspeed', 'Cause_of_accident_overtaking', 'Cause_of_accident_overturning',
    'Cause_of_accident_turnover', 'Cause_of_accident_unknown', 'Driving_experience_ordinal',
    'Service_year_of_vehicle_ordinal', 'Road_surface_conditions_ordinal', 'Age_band_of_casualty_ordinal',
    'Casualty_severity_ordinal'
]
def register_user(request):
    if request.method == 'POST':
        db = get_db()
        username = request.POST['username']
        password = request.POST['password']
        users_collection = db['users']

        # Check if username already exists
        if users_collection.find_one({'username': username}):
            return render(request, 'register.html', {'error': 'Username already exists'})

        # Register new user
        user = {
            'id': str(uuid.uuid4()),
            'username': username,
            'hashed_password': hash_password(password),
        }
        users_collection.insert_one(user)
        return redirect('login')

    return render(request, 'register.html')

# @login_required
def home(request):
    # Example home view to check if user is logged in
    print("HOME...")
    return render(request, 'home.html')

def login_user(request):
    if request.method == 'POST':
        db = get_db()
        username = request.POST['username']
        password = request.POST['password']
        users_collection = db['users']

        # Fetch user from MongoDB
        user = users_collection.find_one({'username': username})

        # Validate credentials
        if user and verify_password(password, user['hashed_password']):
            # Log the user in by storing their ID in the session
            request.session['user_id'] = user['id']
            return render(request, 'home.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def logout_user(request):
    auth_logout(request)
    request.session['user_id'] = None  # Clears session
    return redirect('login')


# @login_required
def add_data(request):
    db = get_db()
    variables_collection = db['data_variables_collection']
    dataset_collection = db['additional_dataset_collection']

    # Fetch the document with "type": "variables"
    data_variables = variables_collection.find_one({'type': 'variables'})
    variables = data_variables.get('variables', []) if data_variables else []

    if request.method == 'POST':
        # Collect and append form data to the collection
        data = {key: request.POST[key] for key in request.POST if key != 'csrfmiddlewaretoken'}
        data['user_id'] = request.session['user_id']
        data['id'] = str(uuid.uuid4())  # Attach the user ID
        dataset_collection.insert_one(data)
        return redirect('home')  # Redirect to the home page after submission
    # print("variables: ", variables)
    return render(request, 'add_data.html', {'variables': variables})

def list_data_api(request):
    db = get_db()
    dataset_collection = db['additional_dataset_collection']
    variables_collection = db['data_variables_collection']

    # Fetch all entries for the current user
    user_id = request.session.get('user_id')
    if not user_id:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

    # Fetch the data entries for the user
    user_entries = list(dataset_collection.find({'user_id': user_id}, {"_id": 0}))

    # Fetch the schema for dynamic table headers
    data_variables = variables_collection.find_one({'type': 'variables'})
    variables = data_variables.get('variables', []) if data_variables else []

    # Preprocess entries to replace dropdown values with display names
    for entry in user_entries:
        for variable in variables:
            if variable['type'] == 'dropdown':
                dropdown_key = variable['key']
                dropdown_values = {item['value']: item['displayName'] for item in variable.get('dropdownValues', [])}
                entry[dropdown_key] = dropdown_values.get(entry.get(dropdown_key), 'N/A')

    # Return JSON response with user entries and variables
    return JsonResponse({'entries': user_entries, 'variables': variables})

def list_data(request):
    # Fetch data as before
    db = get_db()
    dataset_collection = db['additional_dataset_collection']
    variables_collection = db['data_variables_collection']

    # Fetch all entries for the current user
    user_id = request.session['user_id']
    user_entries = list(dataset_collection.find({'user_id': user_id}, {"_id": 0}))

    # Fetch the schema for dynamic table headers
    data_variables = variables_collection.find_one({'type': 'variables'}, {"_id": 0})
    variables = data_variables.get('variables', []) if data_variables else []

    # Pass the template without actual data (we will fill it via JS)
    return render(request, 'list_data.html', {
        'variables': variables,  # Pass the variables for rendering in the template (if needed)
    })

def modify_data(request):
    db = get_db()
    dataset_collection = db['additional_dataset_collection']
    variables_collection = db['data_variables_collection']

    # Fetch the variables for dynamic form rendering
    data_variables = variables_collection.find_one({'type': 'variables'})
    variables = data_variables.get('variables', []) if data_variables else []

    # Fetch user-specific data (e.g., by session user ID)
    user_id = request.session['user_id']
    user_data = dataset_collection.find_one({'user_id': user_id})

    if request.method == 'POST':
        # Update the user’s data in the collection
        updated_data = {key: request.POST[key] for key in request.POST if key != 'csrfmiddlewaretoken'}
        dataset_collection.update_one(
            {'id': user_data['id']},  # Use the user's specific record ID
            {'$set': updated_data}
        )
        return redirect('home')  # Redirect to the home page after saving changes
    print("variables: ", variables, "current_data: ", user_data)
    return render(request, 'modify_data.html', {
        'variables': variables,
        'current_data': user_data or {}
    })

def modify_specific_data(request, entry_id):
    db = get_db()
    dataset_collection = db['additional_dataset_collection']
    variables_collection = db['data_variables_collection']

    # Fetch the variables for dynamic form rendering
    data_variables = variables_collection.find_one({'type': 'variables'})
    variables = data_variables.get('variables', []) if data_variables else []

    # Fetch the specific entry to edit
    entry = dataset_collection.find_one({'id': entry_id})

    
    print(variables, entry)
    return render(request, 'modify_data.html', {
        'entry_id': entry_id,
        'variables': variables,
        'current_data': entry
    })

@csrf_exempt 
def update_entry(request):
    if request.method == 'POST':
        # Get the entry_id and the updated data from the POST request
        entry_id = request.POST.get('entry_id')
        updated_data = {key: value for key, value in request.POST.items() if key != 'csrfmiddlewaretoken' and key != 'entry_id'}
        
        # Validate entry_id
        if not entry_id:
            return JsonResponse({'status': 'failure', 'message': 'Entry ID is missing'})

        db = get_db()
        dataset_collection = db['additional_dataset_collection']
        
        # Update the data in the database
        result = dataset_collection.update_one(
            {'id': entry_id},
            {'$set': updated_data}
        )

        if result.modified_count > 0:
            return JsonResponse({'status': 'success', 'message': 'Data updated successfully'})
        else:
            return JsonResponse({'status': 'failure', 'message': 'No data was updated'})

    return JsonResponse({'status': 'failure', 'message': 'Invalid request method'})

def get_current_data(request, entry_id):
    # Connect to your database collections
    db = get_db()
    dataset_collection = db['additional_dataset_collection']
    variables_collection = db['data_variables_collection']

    # Fetch the variables for dynamic form rendering
    data_variables = variables_collection.find_one({'type': 'variables'})
    variables = data_variables.get('variables', []) if data_variables else []

    # Fetch the specific entry to edit
    entry = dataset_collection.find_one({'id': entry_id})

    return JsonResponse({
        'variables': variables,
        'current_data': entry
    })

# @login_required
def road_accident_prediction(request):
    if request.method == 'POST':
        with open('ml_models/road_accident_model.pkl', 'rb') as model_file:
            model = pickle.load(model_file)
        inputs = np.array([float(request.POST.get(key)) for key in request.POST.keys()]).reshape(1, -1)
        prediction = model.predict(inputs)
        return JsonResponse({'severity': prediction[0]})
    return render(request, 'prediction.html')

def get_variables(request):
    db = get_db()
    variables_collection = db['data_variables_collection']
    variables_doc = variables_collection.find_one({"type": "variables"}, {"_id": 0})
    return JsonResponse({"variables": variables_doc.get("variables", [])})

def one_hot_encode(input_data):
    db = get_db()
    one_hot_collection = db['data_variables_collection']
    one_hot_doc = one_hot_collection.find_one({"type": "variables"}, {"_id": 0})
    one_hot_variables = one_hot_doc.get("variables", [])

    one_hot_encoded = {}
    for variable in one_hot_variables:
        key = variable["key"]
        # print("variable", variable)
        if variable["encoding"] == "one_hot":
            # print("JJ")
            dropdown_values = variable.get("dropdownValues", [])
            for option in dropdown_values:
                column_name = option["col_name"]
                value = input_data.get(key)
                one_hot_encoded[column_name] = 1 if option["value"] == value else 0

    return one_hot_encoded

def ordinal(input_data):
    db = get_db()
    one_hot_collection = db['data_variables_collection']
    one_hot_doc = one_hot_collection.find_one({"type": "variables"}, {"_id": 0})
    one_hot_variables = one_hot_doc.get("variables", [])

    one_hot_encoded = {}
    for variable in one_hot_variables:
        key = variable["key"]
        if variable["encoding"] == "ordinal":
            dropdown_values = variable.get("dropdownValues", [])
            for option in dropdown_values:
                value = input_data.get(key)
                one_hot_encoded[key] = option["value"]

    return one_hot_encoded
@csrf_exempt
def predict(request):
    if request.method == "POST":
        input_data = json.loads(request.body)

        # One-hot encode the input
        one_hot_data = one_hot_encode(input_data)
        # print("one_hot_data: ", one_hot_data)

        ordinal_data = ordinal(input_data)
        # print("ordinal: ", ordinal_data)
        # Prepare data for model prediction
        # Combine one-hot and ordinal data
        combined_data = {**one_hot_data, **ordinal_data}
        # for key in features:
        print("features: ", len(features))
        # input_vector = np.array([combined_data[key] for key in sorted(combined_data.keys())]).reshape(1, -1)
        input_vector = np.array([
            combined_data.get(feature, 0)  # Use 0 if the feature is missing from the combined data
            for feature in features
        ]).reshape(1, -1)
        # print("input_vector: ", input_vector)
        result = {
            'SVM': '',
            'Naive_Bayes': '',
            'ETC': '',
            'KNN': ''
        }
        with open('ml_models/SVM_Oversampled_without_weights.pkl', 'rb') as model_file:
            model = pickle.load(model_file)
        prediction = model.predict(input_vector)
        print("prediction: ", prediction)
        
        
        # prediction = ["Hurrah"]
        for value in y_map['Accident_severity']:
            if y_map['Accident_severity'][value] == int(prediction[0]):
                result['SVM'] = value
                break


        with open('ml_models/Naive_Bayes_Oversampled_without_weights.pkl', 'rb') as model_file:
            model = pickle.load(model_file)
        prediction = model.predict(input_vector)
        print("prediction: ", prediction)
        
        
        # prediction = ["Hurrah"]
        for value in y_map['Accident_severity']:
            if y_map['Accident_severity'][value] == int(prediction[0]):
                result['Naive_Bayes'] = value
                break

        with open('ml_models/KNN_Oversampled_without_weights.pkl', 'rb') as model_file:
            model = pickle.load(model_file)
        prediction = model.predict(input_vector)
        print("prediction: ", prediction)
        
        
        # prediction = ["Hurrah"]
        for value in y_map['Accident_severity']:
            if y_map['Accident_severity'][value] == int(prediction[0]):
                result['KNN'] = value
                break

        with open('ml_models/ETC_Oversampled_without_weights.pkl', 'rb') as model_file:
            model = pickle.load(model_file)
        prediction = model.predict(input_vector)
        print("prediction: ", prediction)
        
        
        # prediction = ["Hurrah"]
        for value in y_map['Accident_severity']:
            if y_map['Accident_severity'][value] == int(prediction[0]):
                result['ETC'] = value
                break
        return JsonResponse({"prediction": result})
    return render(request, 'prediction.html') 

@csrf_exempt
def generate_chart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        x_variable = data.get('xVariable')
        y_variable = data.get('yVariable')
        filter_value = data.get('filterValue')
        print("Filter Value: ", x_variable, y_variable, filter_value)
        # Connect to MongoDB
        db = get_db()
        collection = db['dataset_collection']
        for value in y_map['Accident_severity']:
            if y_map['Accident_severity'][value] == int(filter_value):
                filter_value = value
                break
        
        # Filter data by the provided Y variable value
        filtered_data = list(collection.find({y_variable: filter_value}))
        # print("filtered_data", filtered_data)
        # Count occurrences of each X variable value
        total_count = len(filtered_data)
        x_counts = {}
        for entry in filtered_data:
            x_val = entry.get(x_variable)
            if x_val not in x_counts:
                x_counts[x_val] = 0
            x_counts[x_val] += 1

        # Calculate percentage for each X variable value
        labels = []
        values = []
        for x_val, count in x_counts.items():
            labels.append(x_val)
            values.append((count / total_count) * 100)

        return JsonResponse({"labels": labels, "values": values})
    return JsonResponse({"error": "Invalid request method"}, status=400)


def visualization_page(request):
    return render(request, "visualization.html")

def eda(request):
    print(os.getcwd())
    # Path to your image directory inside the static folder
    image_dir = 'images/eda'  # Relative path from the static folder
    
    # List the image files (without the full path)
    image_list = [
        os.path.join(image_dir, img) for img in os.listdir(os.path.join(os.getcwd(), 'static', image_dir)) if img.endswith(('png', 'jpg', 'jpeg'))
    ]
    
    # Create a list of dictionaries with the static file URLs
    images = [
        {'url': img, 'filename': img.replace(os.sep, '/').split('/')[-1]} for img in image_list
    ]
    
    print("images: ", images)
    return render(request, 'eda.html', {'images': images})

def model_results(request):
    print(os.getcwd())
    # Path to your image directory inside the static folder
    image_dir = 'images/model_results'  # Relative path from the static folder
    
    # List the image files (without the full path)
    image_list = [
        os.path.join(image_dir, img) for img in os.listdir(os.path.join(os.getcwd(), 'static', image_dir)) if img.endswith(('png', 'jpg', 'jpeg'))
    ]
    
    # Create a list of dictionaries with the static file URLs
    images = [
        {'url': img, 'filename': img.replace(os.sep, '/').split('/')[-1]} for img in image_list
    ]
    
    print("images: ", images)
    return render(request, 'model_results.html', {'images': images})

def guidelines(request):
    return render(request, "guidelines.html")

