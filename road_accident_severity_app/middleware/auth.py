from django.shortcuts import redirect

from db.connect import get_db

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Allow unauthenticated access to these paths
        allowed_paths = ['/login', '/register', '/static']
        if any(request.path.startswith(path) for path in allowed_paths):
            return self.get_response(request)

        # Check session for user_id
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('login')

        # Verify user exists in MongoDB
        db = get_db()
        users_collection = db['users']
        user = users_collection.find_one({'id': user_id})
        if not user:
            # Invalid session, clear it and redirect to login
            request.session.flush()
            return redirect('login')

        # Proceed with request
        return self.get_response(request)
    

# def is_logged_in():
#     return redirect('login')
