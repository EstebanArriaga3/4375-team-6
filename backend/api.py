import flask
from flask import jsonify, request, session
from flask_cors import CORS, cross_origin
from functools import wraps
import Credentials
from SQL import create_connection, execute_read_query, execute_query
from flask_bcrypt import Bcrypt

# Initialize Flask app
app = flask.Flask(__name__)
app.secret_key = 'your_secret_key'
app.config["DEBUG"] = True

# Initialize bcrypt for hashing passwords and CORS for frontend communication
bcrypt = Bcrypt(app)
CORS(app, origins="http://localhost:5173", supports_credentials=True)

# Set up database connection
creds = Credentials.Creds()
conn = create_connection(creds.address, creds.username, creds.password, creds.db)
cursor = conn.cursor(dictionary=True)

# Authentication function with bcrypt hash check

def authenticate(email, password):
    query = "SELECT PasswordHash, Role FROM OwnerLogin WHERE Email = %s"
    user = execute_read_query(conn, query, (email,))
    
    if user and user[0]['PasswordHash'] == password:
        # Return user data instead of True
        return {'role': user[0]['Role']}
    return None  # Return None if authentication fails



# Decorator for routes that require authentication
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session or not session['logged_in']:
            return jsonify({'message': 'Unauthorized access!'}), 401
        return f(*args, **kwargs)
    return decorated_function

# Login route for authentication
@app.route('/api/login', methods=['POST'])
@cross_origin(origin='http://localhost:5173', supports_credentials=True)
def login():
    data = request.get_json()
    email = data.get('username')
    password = data.get('password')
    
    user = authenticate(email, password)
    if user:  # If user is not None, authentication was successful
        session['logged_in'] = True
        session['username'] = email
        session['role'] = user['role']  # Store the user's role in the session
        return jsonify({'success': True, 'role': user['role']}), 200
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

# View all data routes (GET requests for all tables)
@app.route('/api/AppointmentDetails', methods=['GET'])
def vAppointmentDetails():
    return jsonify(execute_read_query(conn, 'SELECT * FROM AppointmentDetails'))

@app.route('/api/Appointments', methods=['GET'])
def vAppointments():
    return jsonify(execute_read_query(conn, 'SELECT * FROM Appointments'))

@app.route('/api/Customers', methods=['GET'])
def vCustomers():
    return jsonify(execute_read_query(conn, 'SELECT * FROM Customers'))

@app.route('/api/Employees', methods=['GET'])
def vEmployees():
    return jsonify(execute_read_query(conn, 'SELECT * FROM Employees'))

@app.route('/api/Invoices', methods=['GET'])
def vInvoices():
    return jsonify(execute_read_query(conn, 'SELECT * FROM Invoices'))

@app.route('/api/Reviews', methods=['GET'])
def vReviews():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT ReviewID, ServiceID, Rating, Comment, ReviewDate, CustomerName FROM Reviews")
    reviews = cursor.fetchall()
    return jsonify(reviews)

@app.route('/api/Schedule', methods=['GET'])
def vSchedule():
    return jsonify(execute_read_query(conn, 'SELECT * FROM Schedule'))

@app.route('/api/Services', methods=['GET'])
def vServices():
    return jsonify(execute_read_query(conn, 'SELECT * FROM Services'))

@app.route('/api/Quotes', methods=['GET'])
def vQuotes():
    return jsonify(execute_read_query(conn, 'SELECT * FROM Quotes'))

# Add routes (POST requests for inserting new entries)
@app.route('/api/AppointmentDetails/add', methods=['POST'])
def aAppointmentDetails():
    data = request.get_json()
    query = """
    INSERT INTO AppointmentDetails (AppDetailID, AppID, ServiceID, SubTotal)
    VALUES (%s, %s, %s, %s)
    """
    execute_query(conn, query, (data['AppDetailID'], data['AppID'], data['ServiceID'], data['SubTotal']))
    return jsonify({'message': 'Appointment Details added successfully!'})

@app.route('/api/Appointments/add', methods=['POST'])
def aAppointments():
    data = request.get_json()
    query = """
    INSERT INTO Appointments (AppID, CustomerID, AppDetailID)
    VALUES (%s, %s, %s)
    """
    execute_query(conn, query, (data['AppID'], data['CustomerID'], data['AppDetailID']))
    return jsonify({'message': 'Appointment added successfully!'})

@app.route('/api/Customers/add', methods=['POST'])
def aCustomers():
    data = request.get_json()
    query = """
    INSERT INTO Customers (CustomerID, FirstName, LastName, Email, Address)
    VALUES (%s, %s, %s, %s, %s)
    """
    execute_query(conn, query, (data['CustomerID'], data['FirstName'], data['LastName'], data['Email'], data['Address']))
    return jsonify({'message': 'Customer added successfully!'})

# Update routes (PUT requests for modifying existing entries)
@app.route('/api/AppointmentDetails/update', methods=['PUT'])
def uAppointmentDetails():
    data = request.get_json()
    query = """
    UPDATE AppointmentDetails
    SET AppID = %s, ServiceID = %s, SubTotal = %s
    WHERE AppDetailID = %s
    """
    execute_query(conn, query, (data['AppID'], data['ServiceID'], data['SubTotal'], data['AppDetailID']))
    return jsonify({'message': 'Appointment Details updated successfully!'})

@app.route('/api/Appointments/update', methods=['PUT'])
def uAppointments():
    data = request.get_json()
    query = """
    UPDATE Appointments
    SET CustomerID = %s, AppDetailID = %s
    WHERE AppID = %s
    """
    execute_query(conn, query, (data['CustomerID'], data['AppDetailID'], data['AppID']))
    return jsonify({'message': 'Appointment updated successfully!'})

# Delete routes (DELETE requests for removing records)
@app.route('/api/AppointmentDetails/delete', methods=['DELETE'])
def dAppointmentDetails():
    data = request.get_json()
    query = "DELETE FROM AppointmentDetails WHERE AppDetailID = %s"
    execute_query(conn, query, (data['AppDetailID'],))
    return jsonify({'message': 'Appointment Details deleted successfully!'})

@app.route('/api/Appointments/delete', methods=['DELETE'])
def dAppointments():
    data = request.get_json()
    query = "DELETE FROM Appointments WHERE AppID = %s"
    execute_query(conn, query, (data['AppID'],))
    return jsonify({'message': 'Appointment deleted successfully!'})

# Run the app
if __name__ == '__main__':
    app.run()
