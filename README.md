# Flask JWT Demo

This Flask application serves as a demonstration of how to implement JSON Web Tokens (JWT) for authentication.

## Features

This application currently supports the following features:

* **User Registration:** Users can register by sending a POST request with their username, password, and name.
* **User Login:** Users can log in by sending a POST request with their username and password. Upon successful login, they receive an authentication token which must be included in subsequent API requests.
* **Get User Name:** Authenticated users can retrieve their name by sending a GET request with their JWT authentication token included in the header.

These features are accessible through a RESTful API, facilitating integration with various clients, such as web interfaces or mobile applications.

## Running the Application

To run the application, ensure you have the necessary requirements installed:

```bash
pip3 install -r requirements.txt
```

Then, execute the following command from the root directory of the project:

```bash
python main.py
```

This command starts a Flask web server, making the API accessible at http://localhost:5000.

### Making Requests with cURL

#### User Registration

```bash
curl --location 'http://localhost:5000/register' \
--header 'Content-Type: application/json' \
--data '{
    "username": "admin",
    "password": "pass",
    "name": "Om"
}'
```

#### User Login

```bash
curl --location 'http://localhost:5000/login' \
--header 'Content-Type: application/json' \
--data '{
    "username": "admin",
    "password": "pass"
}'
```

#### Get User Name

```bash
curl --location 'http://localhost:5000/get_name' \
--header 'Content-Type: application/json' \
--header 'JWT_HEADER_NAME: <JWT_TOKEN>'
```

Replace `<JWT_TOKEN>` with the actual JWT token received after login.

## Contributing

Contributions to the Flask JWT Demo are welcome! We're particularly interested in new features or enhancements related to JWT token handling and API security.

Your contributions help improve the Flask JWT Demo for everyone!

### Development Environment

To set up the development environment, install the development requirements:

```bash
pip3 install -r requirements-dev.txt
```

You can run unit tests by executing:

```bash
python -m unittest discover -s tests/unit_tests -t tests
```

An example usage of the application in Python can be found in the `tests/manual_tests/test_api_flow.py` file.

---

Feel free to further customize the README to match your project's specific requirements and conventions. Let me know if you need any further assistance! 

### For more tutorials visit https://dhirajpatra.blogspot.com
