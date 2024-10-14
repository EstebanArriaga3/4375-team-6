import hashlib
import flask
from flask import jsonify
import hashlib
import flask
from flask import jsonify
from flask import request, make_response
import SQL
from SQL import create_connection
from SQL import execute_read_query
from SQL import execute_query
import Credentials

app = flask.Flask(__name__)
app.config["DEBUG"] = True

creds = Credentials.Creds()
conn = create_connection(creds.address, creds.username, creds.password, creds.db)
cursor = conn.cursor(dictionary=True)

'''
masterPassword = "password"
masterUsername = 'username'

#basic http authentication, prompts username and password:
@app.route('/login', methods=['GET'])
def auth_example():
    if request.authorization:
        if request.authorization.username == masterUsername and request.authorization.password == masterPassword:
            return '<h1> We are allowed to be here </h1>'
    return make_response('COULD NOT VERIFY!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})
'''

'''
AppointmentDetails = AppDetailID, AppID, ServiceID, SubTotal
Appointments = AppID, CustomerID, AppDetailID
Customers = CustomerID, FirstName, LastName, Email, Address
Employees = EmployeeID, FirstName, LastName, PhoneNumber, Email, Position
Invoices = InvoiceID, AppDetailID, AppDate, Status, SubTotal
Reviews = ReviewID, ServiceID, Rating, Comments, ReviewDate
Schedule = ScheduleID, EmployeeID, ServiceID, Date, StartTime, EndTime
Services = ServiceID, ServiceName, Description, Price
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
    return jsonify(execute_read_query(conn, 'SELECT * FROM Reviews'))

@app.route('/api/Schedule', methods=['GET'])
def vSchedule():
    return jsonify(execute_read_query(conn, 'SELECT * FROM Schedule'))

@app.route('/api/Services', methods=['GET'])
def vServices():
    return jsonify(execute_read_query(conn, 'SELECT * FROM Services'))










@app.route('/api/AppointmentDetails/add', methods=['POST'])
def aAppointmentDetails():
    request_data = request.get_json()
    addAppID = request_data['AppID']
    addServiceID = request_data['ServiceID']
    addSubTotal = request_data['SubTotal']

    cursor.execute("INSERT INTO AppointmentDetails (AppID, ServiceID, SubTotal) VALUES (%s, %s, %s)", (addAppID, addServiceID, addSubTotal))
    conn.commit()
    return 'Appointment Details added successfully!'

@app.route('/api/Appointments/add', methods=['POST'])
def aAppointments():
    request_data = request.get_json()
    addCustomerID = request_data['CustomerID']
    addAppDetailID = request_data['AppDetailID']

    cursor.execute("INSERT INTO Appointments (CustomerID, AppDetailID) VALUES (%s, %s)", (addCustomerID, addAppDetailID))
    conn.commit()
    return 'Appointment added successfully!'

@app.route('/api/Customers/add', methods=['POST'])
def aCustomers():
    request_data = request.get_json()
    addFirstName = request_data['FirstName']
    addLastName = request_data['LastName']
    addEmail = request_data['Email']
    addAddress = request_data['Address']

    cursor.execute("INSERT INTO Customers (FirstName, LastName, Email, Address) VALUES (%s, %s, %s, %s)", 
                   (addFirstName, addLastName, addEmail, addAddress))
    conn.commit()
    return 'Customer added successfully!'

@app.route('/api/Employees/add', methods=['POST'])
def aEmployees():
    request_data = request.get_json()
    addFirstName = request_data['FirstName']
    addLastName = request_data['LastName']
    addPhoneNumber = request_data['PhoneNumber']
    addEmail = request_data['Email']
    addPosition = request_data['Position']

    cursor.execute("INSERT INTO Employees (FirstName, LastName, PhoneNumber, Email, Position) VALUES (%s, %s, %s, %s, %s)", 
                   (addFirstName, addLastName, addPhoneNumber, addEmail, addPosition))
    conn.commit()
    return 'Employee added successfully!'

@app.route('/api/Invoices/add', methods=['POST'])
def aInvoices():
    request_data = request.get_json()
    addAppDetailID = request_data['AppDetailID']
    addAppDate = request_data['AppDate']
    addStatus = request_data['Status']
    addSubTotal = request_data['SubTotal']

    cursor.execute("INSERT INTO Invoices (AppDetailID, AppDate, Status, SubTotal) VALUES (%s, %s, %s, %s)", 
                   (addAppDetailID, addAppDate, addStatus, addSubTotal))
    conn.commit()
    return 'Invoice added successfully!'

@app.route('/api/Reviews/add', methods=['POST'])
def aReviews():
    request_data = request.get_json()
    addServiceID = request_data['ServiceID']
    addRating = request_data['Rating']
    addComments = request_data['Comments']
    addReviewDate = request_data['ReviewDate']

    cursor.execute("INSERT INTO Reviews (ServiceID, Rating, Comments, ReviewDate) VALUES (%s, %s, %s, %s)", 
                   (addServiceID, addRating, addComments, addReviewDate))
    conn.commit()
    return 'Review added successfully!'

@app.route('/api/Schedule/add', methods=['POST'])
def aSchedule():
    request_data = request.get_json()
    addEmployeeID = request_data['EmployeeID']
    addServiceID = request_data['ServiceID']
    addDate = request_data['Date']
    addStartTime = request_data['StartTime']
    addEndTime = request_data['EndTime']

    cursor.execute("INSERT INTO Schedule (EmployeeID, ServiceID, Date, StartTime, EndTime) VALUES (%s, %s, %s, %s, %s)", 
                   (addEmployeeID, addServiceID, addDate, addStartTime, addEndTime))
    conn.commit()
    return 'Schedule entry added successfully!'

@app.route('/api/Services/add', methods=['POST'])
def aServices():
    request_data = request.get_json()
    addServiceName = request_data['ServiceName']
    addDescription = request_data['Description']
    addPrice = request_data['Price']

    cursor.execute("INSERT INTO Services (ServiceName, Description, Price) VALUES (%s, %s, %s)", 
                   (addServiceName, addDescription, addPrice))
    conn.commit()
    return 'Service added successfully!'










# Update methods

@app.route('/api/AppointmentDetails/update', methods=['PUT'])
def uAppointmentDetails():
    request_data = request.get_json()
    updateAppDetailID = request_data['AppDetailID']
    updateAppID = request_data['AppID']
    updateServiceID = request_data['ServiceID']
    updateSubTotal = request_data['SubTotal']

    cursor.execute("UPDATE AppointmentDetails SET AppID = %s, ServiceID = %s, SubTotal = %s WHERE AppDetailID = %s", 
                   (updateAppID, updateServiceID, updateSubTotal, updateAppDetailID))
    conn.commit()
    return 'Appointment Details updated successfully!'

@app.route('/api/Appointments/update', methods=['PUT'])
def uAppointments():
    request_data = request.get_json()
    updateAppID = request_data['AppID']
    updateCustomerID = request_data['CustomerID']
    updateAppDetailID = request_data['AppDetailID']

    cursor.execute("UPDATE Appointments SET CustomerID = %s, AppDetailID = %s WHERE AppID = %s", 
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

    cursor.execute("UPDATE Customers SET FirstName = %s, LastName = %s, Email = %s, Address = %s WHERE CustomerID = %s", 
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

    cursor.execute("UPDATE Employees SET FirstName = %s, LastName = %s, PhoneNumber = %s, Email = %s, Position = %s WHERE EmployeeID = %s", 
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

    cursor.execute("UPDATE Invoices SET AppDetailID = %s, AppDate = %s, Status = %s, SubTotal = %s WHERE InvoiceID = %s", 
                   (updateAppDetailID, updateAppDate, updateStatus, updateSubTotal, updateInvoiceID))
    conn.commit()
    return 'Invoice updated successfully!'

@app.route('/api/Reviews/update', methods=['PUT'])
def uReviews():
    request_data = request.get_json()
    updateReviewID = request_data['ReviewID']
    updateServiceID = request_data['ServiceID']
    updateRating = request_data['Rating']
    updateComments = request_data['Comments']
    updateReviewDate = request_data['ReviewDate']

    cursor.execute("UPDATE Reviews SET ServiceID = %s, Rating = %s, Comments = %s, ReviewDate = %s WHERE ReviewID = %s", 
                   (updateServiceID, updateRating, updateComments, updateReviewDate, updateReviewID))
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

    cursor.execute("UPDATE Schedule SET EmployeeID = %s, ServiceID = %s, Date = %s, StartTime = %s, EndTime = %s WHERE ScheduleID = %s", 
                   (updateEmployeeID, updateServiceID, updateDate, updateStartTime, updateEndTime, updateScheduleID))
    conn.commit()
    return 'Schedule entry updated successfully!'

@app.route('/api/Services/update', methods=['PUT'])
def uServices():
    request_data = request.get_json()
    updateServiceID = request_data['ServiceID']
    updateServiceName = request_data['ServiceName']
    updateDescription = request_data['Description']
    updatePrice = request_data['Price']

    cursor.execute("UPDATE Services SET ServiceName = %s, Description = %s, Price = %s WHERE ServiceID = %s", 
                   (updateServiceName, updateDescription, updatePrice, updateServiceID))
    conn.commit()
    return 'Service updated successfully!'














# Delete methods

@app.route('/api/AppointmentDetails/delete', methods=['DELETE'])
def dAppointmentDetails():
    request_data = request.get_json()
    deleteAppDetailID = request_data['AppDetailID']

    cursor.execute("DELETE FROM AppointmentDetails WHERE AppDetailID = %s", [deleteAppDetailID])
    conn.commit()
    return 'Appointment Details deleted successfully!'

@app.route('/api/Appointments/delete', methods=['DELETE'])
def dAppointments():
    request_data = request.get_json()
    deleteAppID = request_data['AppID']

    cursor.execute("DELETE FROM Appointments WHERE AppID = %s", [deleteAppID])
    conn.commit()
    return 'Appointment deleted successfully!'

@app.route('/api/Customers/delete', methods=['DELETE'])
def dCustomers():
    request_data = request.get_json()
    deleteCustomerID = request_data['CustomerID']

    cursor.execute("DELETE FROM Customers WHERE CustomerID = %s", [deleteCustomerID])
    conn.commit()
    return 'Customer deleted successfully!'

@app.route('/api/Employees/delete', methods=['DELETE'])
def dEmployees():
    request_data = request.get_json()
    deleteEmployeeID = request_data['EmployeeID']

    cursor.execute("DELETE FROM Employees WHERE EmployeeID = %s", [deleteEmployeeID])
    conn.commit()
    return 'Employee deleted successfully!'

@app.route('/api/Invoices/delete', methods=['DELETE'])
def dInvoices():
    request_data = request.get_json()
    deleteInvoiceID = request_data['InvoiceID']

    cursor.execute("DELETE FROM Invoices WHERE InvoiceID = %s", [deleteInvoiceID])
    conn.commit()
    return 'Invoice deleted successfully!'

@app.route('/api/Reviews/delete', methods=['DELETE'])
def dReviews():
    request_data = request.get_json()
    deleteReviewID = request_data['ReviewID']

    cursor.execute("DELETE FROM Reviews WHERE ReviewID = %s", [deleteReviewID])
    conn.commit()
    return 'Review deleted successfully!'

@app.route('/api/Schedule/delete', methods=['DELETE'])
def dSchedule():
    request_data = request.get_json()
    deleteScheduleID = request_data['ScheduleID']

    cursor.execute("DELETE FROM Schedule WHERE ScheduleID = %s", [deleteScheduleID])
    conn.commit()
    return 'Schedule entry deleted successfully!'

@app.route('/api/Services/delete', methods=['DELETE'])
def dServices():
    request_data = request.get_json()
    deleteServiceID = request_data['ServiceID']

    cursor.execute("DELETE FROM Services WHERE ServiceID = %s", [deleteServiceID])
    conn.commit()
    return 'Service deleted successfully!'

# Update database
@app.route('/api/Facilities/update', methods=['PUT'])
def uFacilities():
    request_data = request.get_json()
    updateID = request_data['id']
    updateName = request_data['Name']

    # ... rest of the code remains the same


app.run()