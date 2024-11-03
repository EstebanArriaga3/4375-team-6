import flask
from flask import jsonify, request, session, make_response
from flask_cors import CORS
from functools import wraps
import Credentials
from SQL import create_connection, execute_read_query, execute_query

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)  # Enable CORS for all routes

# Set up credentials
creds = Credentials.Creds()
conn = create_connection(creds.address, creds.username, creds.password, creds.db)
cursor = conn.cursor(dictionary=True)

# Master credentials for basic auth
masterUsername = 'username'
masterPassword = 'password'

# Basic HTTP authentication function
def authenticate(username, password):
    return username == masterUsername and password == masterPassword

# Decorator for routes requiring authentication
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session or not session['logged_in']:
            return jsonify({'message': 'Unauthorized access!'}), 401
        return f(*args, **kwargs)
    return decorated_function

app.secret_key = 'your_secret_key'

# Login API
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Check authentication
    if authenticate(username, password):
        session['logged_in'] = True
        session['username'] = username
        return jsonify({'success': True, 'role': 'admin'}), 200  # Include role or other data if needed
    else:
        return jsonify({'success': False}), 401

@app.route('/api/protected', methods=['GET'])
@login_required
def protected():
    return jsonify({'message': f'Hello, {session["username"]}!'})

'''
AppointmentDetails = AppDetailID, AppID, ServiceID, SubTotal
Appointments = AppID, CustomerID, AppDetailID
Customers = CustomerID, FirstName, LastName, Email, Address
Employees = EmployeeID, FirstName, LastName, PhoneNumber, Email, Position
Invoices = InvoiceID, AppDetailID, AppDate, Status, SubTotal
Reviews = ReviewID, ServiceID, Rating, Comment, ReviewDate
Schedule = ScheduleID, EmployeeID, ServiceID, Date, StartTime, EndTime
Services = ServiceID, ServiceName, Description, Price
Quote = email_address, description, fence_gates_service, landscaping_service, raised_beds_service,
gutters_roofing_service, created_at, status, last_updated
'''

# View all data based on specifications, No id included
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
    # Create a cursor object
    cursor = conn.cursor()
    
    # Execute the SQL query to fetch reviews including CustomerName
    cursor.execute("SELECT ReviewID, ServiceID, Rating, Comment, ReviewDate, CustomerName FROM TexasLawns.Reviews")
    
    # Fetch all results from the executed query
    reviews = cursor.fetchall()
    
    # Prepare a list to hold formatted review data
    reviews_list = []
    for review in reviews:
        reviews_list.append({
            'ReviewID': review[0],
            'ServiceID': review[1],
            'Rating': review[2],
            'Comment': review[3],
            'ReviewDate': review[4],
            'name': review[5]  # Ensure CustomerName is included
        })
        
    # Return the reviews as a JSON response
    return jsonify(reviews_list)


@app.route('/api/Schedule', methods=['GET'])
def vSchedule():
    return jsonify(execute_read_query(conn, 'SELECT * FROM Schedule'))

@app.route('/api/Services', methods=['GET'])
def vServices():
    return jsonify(execute_read_query(conn, 'SELECT * FROM Services'))

@app.route('/api/Quotes', methods=['GET'])
def vQuotes():
    return jsonify(execute_read_query(conn, 'SELECT * FROM Quotes'))








@app.route('/api/AppointmentDetails/add', methods=['POST'])
def aAppointmentDetails():
    request_data = request.get_json()
    addAppDetailID = request_data['AppDetailID']
    addAppID = request_data['AppID']
    addServiceID = request_data['ServiceID']
    addSubTotal = request_data['SubTotal']

    cursor.execute("INSERT INTO TexasLawns.AppointmentDetails (AppDetailID, AppID, ServiceID, SubTotal) VALUES (%s, %s, %s, %s)", (addAppDetailID, addAppID, addServiceID, addSubTotal))
    conn.commit()
    return 'Appointment Details added successfully!'

@app.route('/api/Appointments/add', methods=['POST'])
def aAppointments():
    request_data = request.get_json()
    addAppID = request_data['AppID']
    addCustomerID = request_data['CustomerID']
    addAppDetailID = request_data['AppDetailID']

    cursor.execute("INSERT INTO TexasLawns.Appointments (AppID, CustomerID, AppDetailID) VALUES (%s, %s, %s)", 
                   (addAppID, addCustomerID, addAppDetailID))
    conn.commit()
    return 'Appointment added successfully!'

@app.route('/api/Customers/add', methods=['POST'])
def aCustomers():
    request_data = request.get_json()
    addCustomerID = request_data['CustomerID']
    addFirstName = request_data['FirstName']
    addLastName = request_data['LastName']
    addEmail = request_data['Email']
    addAddress = request_data['Address']

    cursor.execute("INSERT INTO TexasLawns.Customers (CustomerID, FirstName, LastName, Email, Address) VALUES (%s, %s, %s, %s, %s)",
                     (addCustomerID, addFirstName, addLastName, addEmail, addAddress))
    conn.commit()
    return 'Customer added successfully!'

@app.route('/api/Employees/add', methods=['POST'])
def aEmployees():
    request_data = request.get_json()
    addEmployeeID = request_data['EmployeeID']
    addFirstName = request_data['FirstName']
    addLastName = request_data['LastName']
    addPhoneNumber = request_data['PhoneNumber']
    addEmail = request_data['Email']
    addPosition = request_data['Position']

    cursor.execute("INSERT INTO TexasLawns.Employees (EmployeeID, FirstName, LastName, PhoneNumber, Email, Position) VALUES (%s, %s, %s, %s, %s, %s)",
                        (addEmployeeID, addFirstName, addLastName, addPhoneNumber, addEmail, addPosition))
    conn.commit()
    return 'Employee added successfully!'

@app.route('/api/Invoices/add', methods=['POST'])
def aInvoices():
    request_data = request.get_json()
    addInvoiceID = request_data['InvoiceID']
    addAppDetailID = request_data['AppDetailID']
    addAppDate = request_data['AppDate']
    addStatus = request_data['Status']
    addSubTotal = request_data['SubTotal']

    cursor.execute("INSERT INTO TexasLawns.Invoices (InvoiceID, AppDetailID, AppDate, Status, SubTotal) VALUES (%s, %s, %s, %s, %s)",
                     (addInvoiceID, addAppDetailID, addAppDate, addStatus, addSubTotal))
    conn.commit()
    return 'Invoice added successfully!'

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




@app.route('/api/Schedule/add', methods=['POST'])
def aSchedule():
    request_data = request.get_json()
    addScheduleID = request_data['ScheduleID']
    addEmployeeID = request_data['EmployeeID']
    addServiceID = request_data['ServiceID']
    addDate = request_data['Date']
    addStartTime = request_data['StartTime']
    addEndTime = request_data['EndTime']

    cursor.execute("INSERT INTO TexasLawns.Schedule (ScheduleID, EmployeeID, ServiceID, Date, StartTime, EndTime) VALUES (%s, %s, %s, %s, %s, %s)",
                        (addScheduleID, addEmployeeID, addServiceID, addDate, addStartTime, addEndTime))
    conn.commit()
    return 'Schedule entry added successfully!'

@app.route('/api/Services/add', methods=['POST'])
def aServices():
    request_data = request.get_json()
    addServiceID = request_data['ServiceID']
    addServiceName = request_data['ServiceName']
    addDescription = request_data['Description']
    addPrice = request_data['Price']

    cursor.execute("INSERT INTO TexasLawns.Services (ServiceID, ServiceName, Description, Price) VALUES (%s, %s, %s, %s)",
                        (addServiceID, addServiceName, addDescription, addPrice))
    conn.commit()
    return 'Service added successfully!'

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







# Update methods

@app.route('/api/AppointmentDetails/update', methods=['PUT'])
def uAppointmentDetails():
    request_data = request.get_json()
    updateAppDetailID = request_data['AppDetailID']
    updateAppID = request_data['AppID']
    updateServiceID = request_data['ServiceID']
    updateSubTotal = request_data['SubTotal']

    cursor.execute("UPDATE TexasLawns.AppointmentDetails SET AppID = %s, ServiceID = %s, SubTotal = %s WHERE AppDetailID = %s", 
                   (updateAppID, updateServiceID, updateSubTotal, updateAppDetailID))
    conn.commit()
    return 'Appointment Details updated successfully!'

@app.route('/api/Appointments/update', methods=['PUT'])
def uAppointments():
    request_data = request.get_json()
    updateAppID = request_data['AppID']
    updateCustomerID = request_data['CustomerID']
    updateAppDetailID = request_data['AppDetailID']

    cursor.execute("UPDATE TexasLawns.Appointments SET CustomerID = %s, AppDetailID = %s WHERE AppID = %s", 
                   (updateCustomerID, updateAppDetailID, updateAppID))
    conn.commit()
    return 'Appointment updated successfully!'

@app.route('/api/Customers/update', methods=['PUT'])
def uCustomers():
    request_data = request.get_json()
    updateCustomerID = request_data['CustomerID']
    updateFirstName = request_data['FirstName']
    updateLastName = request_data['LastName']
    updateEmail = request_data['Email']
    updateAddress = request_data['Address']

    cursor.execute("UPDATE TexasLawns.Customers SET FirstName = %s, LastName = %s, Email = %s, Address = %s WHERE CustomerID = %s", 
                   (updateFirstName, updateLastName, updateEmail, updateAddress, updateCustomerID))
    conn.commit()
    return 'Customer updated successfully!'

@app.route('/api/Employees/update', methods=['PUT'])
def uEmployees():
    request_data = request.get_json()
    updateEmployeeID = request_data['EmployeeID']
    updateFirstName = request_data['FirstName']
    updateLastName = request_data['LastName']
    updatePhoneNumber = request_data['PhoneNumber']
    updateEmail = request_data['Email']
    updatePosition = request_data['Position']

    cursor.execute("UPDATE TexasLawns.Employees SET FirstName = %s, LastName = %s, PhoneNumber = %s, Email = %s, Position = %s WHERE EmployeeID = %s", 
                   (updateFirstName, updateLastName, updatePhoneNumber, updateEmail, updatePosition, updateEmployeeID))
    conn.commit()
    return 'Employee updated successfully!'

@app.route('/api/Invoices/update', methods=['PUT'])
def uInvoices():
    request_data = request.get_json()
    updateInvoiceID = request_data['InvoiceID']
    updateAppDetailID = request_data['AppDetailID']
    updateAppDate = request_data['AppDate']
    updateStatus = request_data['Status']
    updateSubTotal = request_data['SubTotal']

    cursor.execute("UPDATE TexasLawns.Invoices SET AppDetailID = %s, AppDate = %s, Status = %s, SubTotal = %s WHERE InvoiceID = %s", 
                   (updateAppDetailID, updateAppDate, updateStatus, updateSubTotal, updateInvoiceID))
    conn.commit()
    return 'Invoice updated successfully!'

@app.route('/api/Reviews/update', methods=['PUT'])
#@login_required
def uReviews():
    request_data = request.get_json()
    updateReviewID = request_data['ReviewID']
    updateServiceID = request_data['ServiceID']
    updateRating = request_data['Rating']
    updateComment = request_data['Comment']
    updateReviewDate = request_data['ReviewDate']

    cursor.execute("UPDATE TexasLawns.Reviews SET ServiceID = %s, Rating = %s, Comment = %s, ReviewDate = %s WHERE ReviewID = %s", 
                   (updateServiceID, updateRating, updateComment, updateReviewDate, updateReviewID))
    conn.commit()
    return 'Review updated successfully!'

@app.route('/api/Schedule/update', methods=['PUT'])
def uSchedule():
    request_data = request.get_json()
    updateScheduleID = request_data['ScheduleID']
    updateEmployeeID = request_data['EmployeeID']
    updateServiceID = request_data['ServiceID']
    updateDate = request_data['Date']
    updateStartTime = request_data['StartTime']
    updateEndTime = request_data['EndTime']

    cursor.execute("UPDATE TexasLawns.Schedule SET EmployeeID = %s, ServiceID = %s, Date = %s, StartTime = %s, EndTime = %s WHERE ScheduleID = %s", 
                   (updateEmployeeID, updateServiceID, updateDate, updateStartTime, updateEndTime, updateScheduleID))
    conn.commit()
    return 'Schedule entry updated successfully!'

@app.route('/api/Services/update', methods=['PUT'])
#@login_required
def uServices():
    request_data = request.get_json()
    updateServiceID = request_data['ServiceID']
    updateServiceName = request_data['ServiceName']
    updateDescription = request_data['Description']
    updatePrice = request_data['Price']

    cursor.execute("UPDATE TexasLawns.Services SET ServiceName = %s, Description = %s, Price = %s WHERE ServiceID = %s", 
                   (updateServiceName, updateDescription, updatePrice, updateServiceID))
    conn.commit()
    return 'Service updated successfully!'














# Delete methods

@app.route('/api/AppointmentDetails/delete', methods=['DELETE'])
def dAppointmentDetails():
    request_data = request.get_json()
    deleteAppDetailID = request_data['AppDetailID']

    cursor.execute("DELETE FROM TexasLawns.AppointmentDetails WHERE AppDetailID = %s", [deleteAppDetailID])
    conn.commit()
    return 'Appointment Details deleted successfully!'

@app.route('/api/Appointments/delete', methods=['DELETE'])
def dAppointments():
    request_data = request.get_json()
    deleteAppID = request_data['AppID']

    cursor.execute("DELETE FROM TexasLawns.Appointments WHERE AppID = %s", [deleteAppID])
    conn.commit()
    return 'Appointment deleted successfully!'

@app.route('/api/Customers/delete', methods=['DELETE'])
def dCustomers():
    request_data = request.get_json()
    deleteCustomerID = request_data['CustomerID']

    cursor.execute("DELETE FROM TexasLawns.Customers WHERE CustomerID = %s", [deleteCustomerID])
    conn.commit()
    return 'Customer deleted successfully!'

@app.route('/api/Employees/delete', methods=['DELETE'])
def dEmployees():
    request_data = request.get_json()
    deleteEmployeeID = request_data['EmployeeID']

    cursor.execute("DELETE FROM TexasLawns.Employees WHERE EmployeeID = %s", [deleteEmployeeID])
    conn.commit()
    return 'Employee deleted successfully!'

@app.route('/api/Invoices/delete', methods=['DELETE'])
def dInvoices():
    request_data = request.get_json()
    deleteInvoiceID = request_data['InvoiceID']

    cursor.execute("DELETE FROM TexasLawns.Invoices WHERE InvoiceID = %s", [deleteInvoiceID])
    conn.commit()
    return 'Invoice deleted successfully!'

@app.route('/api/Reviews/delete', methods=['DELETE'])
#@login_required
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


@app.route('/api/Schedule/delete', methods=['DELETE'])
def dSchedule():
    request_data = request.get_json()
    deleteScheduleID = request_data['ScheduleID']

    cursor.execute("DELETE FROM TexasLawns.Schedule WHERE ScheduleID = %s", [deleteScheduleID])
    conn.commit()
    return 'Schedule entry deleted successfully!'

@app.route('/api/Services/delete', methods=['DELETE'])
#@login_required
def dServices():
    request_data = request.get_json()
    deleteServiceID = request_data['ServiceID']

    cursor.execute("DELETE FROM TexasLawns.Services WHERE ServiceID = %s", [deleteServiceID])
    conn.commit()
    return 'Service deleted successfully!'

app.run()
