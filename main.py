from flask import Flask, render_template
from forms import accounts,createprofile
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/accounts/login', methods=['GET','POST'])
def loginpage():
    logo_status = True
    login_form = accounts.LoginForm()
    return render_template('login.html', form = login_form, logo_show = logo_status)

@app.route('/accounts/register', methods=['GET','POST'])
def registerpage():
    register_status = True 
    register_form = accounts.RegisterForm()
    return render_template('register.html', form = register_form, logo_show = register_status)

@app.route('/dashboard')
def dashboardpage():
    page_index = 1
    profile_form = createprofile.ProfileDetailFrom()
    
    template_cards = ['template_1', 'template_2','template_3', 'template_4','template_5', 'template_6']
    
    return render_template('dashboard.html', page = page_index , form = profile_form, template_cards = template_cards)

@app.route('/myprofile')
def myprofilepage():
    return render_template('myprofile.html')

if __name__ == "__main__":
    app.secret_key = '12345'
    app.run(debug=True)

