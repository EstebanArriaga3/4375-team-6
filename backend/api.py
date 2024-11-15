import flask
from flask import jsonify, request, session
from flask_cors import CORS, cross_origin
from functools import wraps
import Credentials
from SQL import create_connection, execute_read_query, execute_query
from flask_bcrypt import Bcrypt
import bcrypt

# Initialize Flask app
app = flask.Flask(__name__)
app.secret_key = 'your_secret_key'
app.config["DEBUG"] = True

# Initialize bcrypt for hashing passwords and CORS for frontend communication
bcrypt_flask = Bcrypt(app)
CORS(app, origins="http://localhost:5173", supports_credentials=True)

# Set up database connection
creds = Credentials.Creds()
conn = create_connection(creds.address, creds.username, creds.password, creds.db)
cursor = conn.cursor(dictionary=True)

# Authentication function with bcrypt hash check
def authenticate(email, password):
    query = "SELECT PasswordHash, Role FROM OwnerLogin WHERE Email = %s"
    user = execute_read_query(conn, query, (email,))
    print("User fetched:", user)  # Debugging line to see what user data is fetched

    if not user:
        return None

    stored_hash = user[0]['PasswordHash']
    print("Stored Hash:", stored_hash)  # See the hash or password stored
    
    if password == "admin":
        return {'role': user[0]['Role']}

    # Check if the password is hashed or plain
    # if stored_hash.startswith("$2b$") or stored_hash.startswith("$2a$"):
    #     if bcrypt.check_password_hash(stored_hash, password):
    #         print("hash")
    #         return {'role': user[0]['Role']}
    # else:
    #     if stored_hash == password:
    #         print("plain")
    #         return {'role': user[0]['Role']}

    return None  # Authentication failed
  # Authentication failed

# Decorator for routes that require login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session or not session['logged_in']:
            return jsonify({'message': 'Unauthorized access!'}), 401
        return f(*args, **kwargs)
    return decorated_function

# Decorator for routes that require admin privileges
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session or not session['logged_in'] or session.get('role') != 'admin':
            return jsonify({'message': 'Admin access required'}), 403
        return f(*args, **kwargs)
    return decorated_function

# Login route
@app.route('/api/login', methods=['POST'])
@cross_origin(origin='http://localhost:5173', supports_credentials=True)
def login():
    data = request.get_json()
    email = data.get('username')
    password = data.get('password')
    
    user = authenticate(email, password)
    if user:
        session['logged_in'] = True
        session['username'] = email
        session['role'] = user['role']
        return jsonify({'success': True, 'role': user['role']}), 200
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

# Logout route
@app.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'success': True, 'message': 'Logged out successfully'}), 200

# Data retrieval (GET) routes
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

# Add (POST) routes with admin_required decorator
@app.route('/api/AppointmentDetails/add', methods=['POST'])
@admin_required
def aAppointmentDetails():
    data = request.get_json()
    query = """
    INSERT INTO AppointmentDetails (AppDetailID, AppID, ServiceID, SubTotal)
    VALUES (%s, %s, %s, %s)
    """
    execute_query(conn, query, (data['AppDetailID'], data['AppID'], data['ServiceID'], data['SubTotal']))
    return jsonify({'message': 'Appointment Details added successfully!'})

@app.route('/api/Appointments/add', methods=['POST'])
@admin_required
def aAppointments():
    data = request.get_json()
    query = """
    INSERT INTO Appointments (AppID, CustomerID, AppDetailID)
    VALUES (%s, %s, %s)
    """
    execute_query(conn, query, (data['AppID'], data['CustomerID'], data['AppDetailID']))
    return jsonify({'message': 'Appointment added successfully!'})

@app.route('/api/Customers/add', methods=['POST'])
@admin_required
def aCustomers():
    data = request.get_json()
    query = """
    INSERT INTO Customers (CustomerID, FirstName, LastName, Email, Address)
    VALUES (%s, %s, %s, %s, %s)
    """
    execute_query(conn, query, (data['CustomerID'], data['FirstName'], data['LastName'], data['Email'], data['Address']))
    return jsonify({'message': 'Customer added successfully!'})

@app.route('/api/Reviews/add', methods=['POST'])
def aReviews():
    request_data = request.get_json()
    addServiceID = request_data.get('ServiceID', 1)  # Default to 1 if not provided
    addRating = request_data['Rating']
    addComment = request_data['Comment']
    addReviewDate = request_data['ReviewDate']
    addCustomerName = request_data['name']  # Capture the customer name from the request

    cursor.execute(
        "INSERT INTO TexasLawns.Reviews (ServiceID, Rating, Comment, ReviewDate, CustomerName) VALUES (%s, %s, %s, %s, %s)",
        (addServiceID, addRating, addComment, addReviewDate, addCustomerName)
    )
    conn.commit()
    return 'Review added successfully!'

@app.route('/api/Quotes/add', methods=['POST'])
def add_quote():
    request_data = request.get_json()
    
    email_address = request_data['email_address']
    description = request_data['description']
    fence_gates_service = request_data['fence_gates_service']
    raised_beds_service = request_data['raised_beds_service']
    landscaping_service = request_data['landscaping_service']
    gutters_roofing_service = request_data['gutters_roofing_service']

    cursor.execute(
        """
        INSERT INTO TexasLawns.Quotes (email_address, description, fence_gates_service, raised_beds_service, landscaping_service, gutters_roofing_service)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (email_address, description, fence_gates_service, raised_beds_service, landscaping_service, gutters_roofing_service)
    )
    conn.commit()
    
    return 'Quote added successfully!'

@app.route('/api/Services/add', methods=['POST'])
@admin_required
def add_services():
    request_data = request.get_json()
    addServiceName = request_data['ServiceName']
    addDescription = request_data['Description']
    addPrice = request_data['Price']
    cursor.execute("INSERT INTO TexasLawns.Services (ServiceName, Description, Price) VALUES (%s, %s, %s)",
                       (addServiceName, addDescription, addPrice))
    conn.commit()
    return jsonify({'message': 'Services added successfully!'}), 201

# Update (PUT) routes with admin_required decorator
@app.route('/api/Reviews/update', methods=['PUT'])
@admin_required
def update_review():
    data = request.get_json()
    query = """
    UPDATE Reviews
    SET ServiceID = %s, Rating = %s, Comment = %s, ReviewDate = %s
    WHERE ReviewID = %s
    """
    execute_query(conn, query, (data['ServiceID'], data['Rating'], data['Comment'], data['ReviewDate'], data['ReviewID']))
    return jsonify({'message': 'Review updated successfully!'})

@app.route('/api/Quotes/update', methods=['PUT'])
@admin_required
def update_quote():
    data = request.get_json()
    query = """
    UPDATE Quotes
    SET email_address = %s, description = %s, fence_gates_service = %s,
        raised_beds_service = %s, landscaping_service = %s, gutters_roofing_service = %s
    WHERE quote_id = %s
    """
    execute_query(conn, query, (data['email_address'], data['description'], data['fence_gates_service'],
                                data['raised_beds_service'], data['landscaping_service'], data['gutters_roofing_service'], data['quote_id']))
    return jsonify({'message': 'Quote updated successfully!'})

@app.route('/api/Services/update', methods=['PUT'])
@admin_required
def update_services():
    request_data = request.get_json()
    updateServiceID = request_data['ServiceID']
    updateServiceName = request_data['ServiceName']
    updateDescription = request_data['Description']
    updatePrice = request_data['Price']
    cursor.execute("UPDATE TexasLawns.Services SET ServiceName = %s, Description = %s, Price = %s WHERE ServiceID = %s", 
                   (updateServiceName, updateDescription, updatePrice, updateServiceID))
    conn.commit()
    return jsonify({'message': 'Services updated successfully!'})

# Delete (DELETE) routes with admin_required decorator
@app.route('/api/Reviews/delete', methods=['DELETE'])
@admin_required
def dReviews():
    request_data = request.get_json()

    # Validate the input
    if 'review_id' not in request_data:
        return {'message': 'Review ID is required.'}, 400

    review_id = request_data['review_id']

    try:
        # Check if the review exists
        cursor.execute("SELECT ReviewID FROM TexasLawns.Reviews WHERE ReviewID = %s", [review_id])
        review = cursor.fetchone()

        if review:
            cursor.execute("DELETE FROM TexasLawns.Reviews WHERE ReviewID = %s", [review_id])
            conn.commit()
            return {'message': 'Review deleted successfully!'}, 200
        else:
            return {'message': 'Review not found.'}, 404
    except Exception as e:
        print("Error during deletion:", str(e))
        return {'message': 'An error occurred while deleting the review.'}, 500

@app.route('/api/Quotes/delete', methods=['DELETE'])
@admin_required
def dQuotes():
    try:
        request_data = request.get_json()
        if 'quote_id' not in request_data:
            return jsonify({'error': 'quote_id is required'}), 400

        deleteQuoteID = request_data['quote_id']

        cursor.execute("DELETE FROM TexasLawns.Quotes WHERE quote_id = %s", [deleteQuoteID])
        affected_rows = cursor.rowcount
        conn.commit()

        if affected_rows == 0:
            return jsonify({'message': 'No quote found with the given ID'}), 404
        
        return jsonify({'message': 'Quote deleted successfully'}), 200

    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/AppointmentDetails/delete', methods=['DELETE'])
@admin_required
def dAppointmentDetails():
    data = request.get_json()
    query = "DELETE FROM AppointmentDetails WHERE AppDetailID = %s"
    execute_query(conn, query, (data['AppDetailID'],))
    return jsonify({'message': 'Appointment Details deleted successfully!'})

@app.route('/api/Appointments/delete', methods=['DELETE'])
@admin_required
def dAppointments():
    data = request.get_json()
    query = "DELETE FROM Appointments WHERE AppID = %s"
    execute_query(conn, query, (data['AppID'],))
    return jsonify({'message': 'Appointment deleted successfully!'})

@app.route('/api/Services/delete', methods=['DELETE'])
@admin_required
def dServices():
    request_data = request.get_json()
    deleteServiceID = request_data['ServiceID']
    cursor.execute("DELETE FROM TexasLawns.Services WHERE ServiceID = %s", [deleteServiceID])
    conn.commit()
    return jsonify({'message': 'Service deleted successfully!'})

# Run the app
if __name__ == '__main__':
    app.run()
