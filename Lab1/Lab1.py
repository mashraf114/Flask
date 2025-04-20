
# LAB 1
'''
create a company route that display all companies
- company name
- company location
- company description
- company employees count
'''

from flask import Flask, render_template

app = Flask(__name__)

# Sample data: List of companies
companies = [
    {
        "name": "bank masr",
        "location": "zag",
        "description": "A bank.",
        "employees_count": 50
    },
    {
        "name": "bosta",
        "location": "giza",
        "description": "Providing transportation services.",
        "employees_count": 1200
    },
    {
        "name": "giza systems",
        "location": "giza",
        "description": "A technology solutions provider.",
        "employees_count": 500
    },
]

# Route to display all companies
@app.route('/companies')
def display_companies():
    return render_template('companies.html', companies=companies)

if __name__ == '__main__':
    app.run(debug=True)