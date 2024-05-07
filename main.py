# main.py
from flask import Flask, jsonify, request, redirect, url_for
from entities.user import User, db
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os


# load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')  # Database URI
# Configure a strong secret key for JWT (replace with your actual secret)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_TOKEN_LOCATION'] = ['headers']

db.init_app(app)  # Initialize db with Flask app
cors = CORS(app)  # Enable CORS

# JWT initialize
jwt = JWTManager(app)

# Initialize the database
with app.app_context():
    db.create_all()


# Endpoint to get user name to test JWT
@app.route('/get_name', methods=['GET'])
@jwt_required()
def get_name():
    # Extract the user ID from the JWT
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()

    # Check if user exists
    if user:
        return jsonify({'message': 'User found', 'name': user.name})
    else:
        return jsonify({'message': 'User not found'}), 404
    
# user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    print('Received data:', username , password)

    user = User.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify({'message': 'Login Success', 'access_token': access_token})
    else:
        return jsonify({'message': 'Login Failed'}), 401
    

# user register
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    name = data['name']
    print('Received data:', username, password, name)

    # Check if user already exists
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'message': 'User already exists'}), 400

    # # Generate a salt
    # salt = bcrypt.gensalt()  # Recommended way

    # # Hash the password with the salt
    # hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Create a new user
    new_user = User(username=username, password=hashed_password, name=name)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201


# Entry point to run the Flask web application
if __name__ == "__main__":
    app.run(debug=True)
