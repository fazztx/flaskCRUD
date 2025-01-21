# Import libraries
from flask import Flask, request, render_template, redirect, url_for

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route('/', methods=['GET'])
def get_transactions():
    if request.method == 'GET':
        return render_template('transactions.html', transactions=transactions) #Passes data from python to html

# Create operation
@app.route('/add', methods=['GET', 'POST'])
def add_transaction(): #If button is pressed from transaction... if <a> then, method == GET
    if request.method == 'GET':
        return render_template('form.html')
    
    if request.method == 'POST': #If button is pressed from from... if <form>, then == POST
        transactions.append(
            {
                'id': len(transactions) + 1, 
                'date': str(request.form['date']), 
                'amount': float(request.form['amount'])
            }
        )
        return redirect(url_for('get_transactions')) #Runs the GET defined above 



# Update operation
@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST', 'PUT'])
def edit_transaction(transaction_id):
    if request.method == 'GET':
        for eachTransaction in transactions:
            if eachTransaction['id'] == transaction_id:
                return render_template('edit.html', transaction = eachTransaction, total_balance = total_balance())
    
    if request.method == 'POST' or  request.method == 'PUT':
        # transactions[transaction_id-1] = {
        #     'id' : transaction_id,
        #     'date': str(request.form['date']), 
        #     'amount': float(request.form['amount'])
        # }
        for eachTransaction in transactions:
            if eachTransaction['id'] == transaction_id:
                eachTransaction['date'] = str(request.form['date'])
                eachTransaction['amount'] = float(request.form['amount'])
                break

    return redirect(url_for('get_transactions')) #Runs the GET defined above 

# Delete operation
@app.route('/delete/<int:transaction_id>', methods=['GET', 'DELETE'])
def delete_transaction(transaction_id):
    if request.method == 'GET' or  request.method == 'DELETE':
        # del(transactions[transaction_id-1])
        for eachTransaction in transactions:
            if eachTransaction['id'] == transaction_id:
                transactions.remove(eachTransaction)
                break
        return redirect(url_for('get_transactions')) #Runs the GET defined above 
    
# Exercise 1: Search Transactions
@app.route('/search', methods=['GET', 'POST'])
def search_transactions():
    if request.method == 'GET':
        return render_template('search.html')
    if request.method == 'POST':
        min = int(request.form['min_amount'])
        max = int(request.form['max_amount'])
        print('Min: ',min)
        print('Max: ', max)

        specificTransactions = []

        for eachTransaction in transactions:
            if min <= eachTransaction['amount'] and eachTransaction['amount'] <= max:
                specificTransactions.append(eachTransaction)
        
        print(specificTransactions)
        return render_template('transactions.html', transactions=specificTransactions)

# Exercise 2: Total Balance
@app.route('/balance', methods=['GET'])
def total_balance():
    total = 0
    for eachTransaction in transactions:
        total = total+ eachTransaction['amount']
    return f"Total balance: {total}"

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080)