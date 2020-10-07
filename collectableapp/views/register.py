import json
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login_user(request):
    '''Handles the authentication of a user
    Method arguments:
      request -- The full HTTP request object
    '''

    req_body = json.loads(request.body.decode())

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        # Use the built-in authenticate method to verify
        username = req_body['username']
        password = req_body['password']
        authenticated_user = None
        authenticated_user = authenticate(username=username, password=password)

        # get the user by their username and password if they don't have a token yet
        user = User.objects.get(username=username)


        # If the user was made using a fixture, auth will be unsuccessful and will need a token first
        if user is not None and authenticated_user is None:
            user.set_password(user.password)
            user.save()

            # gotta get the user again because we just updated it?
            user = User.objects.get(username=username)

            token = Token.objects.create(user=user)
            authenticated_user = authenticate(
                username=user.username, password=user.password)
            print("auth'd user", authenticated_user)
            data = json.dumps({"valid": True, "token": token.key})
            return HttpResponse(data, content_type='application/json')

        # If authentication was successful, respond with their token
        elif authenticated_user is not None:
            token = Token.objects.get(user=authenticated_user)
            data = json.dumps({"valid": True, "token": token.key})
            return HttpResponse(data, content_type='application/json')
        else:
            # Bad login details were provided. So we can't log the user in.
            data = json.dumps({"valid": False})
            return HttpResponse(data, content_type='application/json')


@csrf_exempt
def register_user(request):
    '''Handles the creation of a new user for authentication
    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    new_user = User.objects.create_user(
        username=req_body['email'],
        email=req_body['email'],
        password=req_body['password'],
        first_name=req_body['first_name'],
        last_name=req_body['last_name']
    )

    # Use the REST Framework's token generator on the new user account
    token = Token.objects.create(user=new_user)

    # Return the token to the client
    # The json. dumps() method encodes any Python object into JSON formatted String.
    data = json.dumps({"token": token.key})

    return HttpResponse(data, content_type='application/json')
