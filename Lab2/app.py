from flask import Flask, render_template, redirect, url_for, flash
from models import db, Company
from forms import CompanyForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///companies.db'

db.init_app(app)

@app.route('/')
def home():
    companies = Company.query.all()
    return render_template('company_list.html', companies=companies)

@app.route('/add', methods=['GET', 'POST'])
def add_company():
    form = CompanyForm()
    if form.validate_on_submit():
        new_company = Company(
            name=form.name.data,
            description=form.description.data,
            employees_count=form.employees_count.data,
            location=form.location.data
        )
        db.session.add(new_company)
        db.session.commit()
        flash('Company added successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('add_company.html', form=form)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)