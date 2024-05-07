import requests

# The base URL for the API
BASE_URL = "http://127.0.0.1:5000"


def register(username, password, name):
    """
    Creates a user using the web API.
    """
    response = requests.post(
        f"{BASE_URL}/users", json={"username": username, "password": password, "name": name}
    )
    return response


def login(username, password):      
   """
   Logs in a user using the web API
   """
   response = requests.post(
       f"{BASE_URL}/login", json={"username": username, "password": password}
   )
   return response


def get_name():
    """
    Gets the name of the user using the web API
    """
    response = requests.get(f"{BASE_URL}/get_name")
    return response

if __name__ == "__main__":
    # Register a new user
    register_response = register("testuser", "password123", "Test User")
    print(register_response.text)

    # Login as the new user
    login_response = login("testuser", "password123")
    print(login_response.text)

    # Get the name of the user
    name_response = get_name()
    print(name_response.text)
    