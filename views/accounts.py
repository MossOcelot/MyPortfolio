from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, login_user, logout_user

from werkzeug.security import generate_password_hash, check_password_hash

from forms import accounts,createprofile

import models
from models import users,folios

bp = Blueprint("accounts", __name__, url_prefix="/accounts")


@bp.route("/login")
def login():
    logo_status = True
    form = accounts.LoginForm()
    return render_template("/accounts/login.html", form = form, logo_show = logo_status)


@bp.route("/do-login", methods=["POST"])
def do_login():
    form = accounts.LoginForm()

    if not form.validate_on_submit():
        return redirect(url_for("accounts.login", **form.errors))

    user = (
        models.db.session.query(users.User)
        .filter_by(
            email=form.email.data,
        )
        .first()
    )

    if not user:
        return redirect(url_for("accounts.login", message="invalid login"))

    if not check_password_hash(user.password, form.password.data):
        return redirect(url_for("accounts.login", message="invalid password"))

    login_user(user)

    return redirect(url_for("accounts.dashboard"))


@bp.route("/register", methods=["GET", "POST"])
def register():
    register_status = True
    form = accounts.RegisterForm()
    if not form.validate_on_submit():
        return render_template("/accounts/register.html", form=form,  logo_show = register_status)

    user = users.User()
    form.populate_obj(user)

    print(form.data)
    user.password = generate_password_hash(form.password.data, method="sha256")

    # db management
    models.db.session.add(user)
    models.db.session.commit()

    return redirect(url_for("accounts.login"))


@bp.route("/logout")
def logout():
    logout_user()
    return redirect("/")

@bp.route("/dashboard", methods=['GET','POST'])
@login_required
def dashboard():
    page_index = int(request.args.get('page_index', "1"))
    profile_form = createprofile.ProfileDetailFrom()
    template_cards = ['template_1', 'template_2','template_3', 'template_4','template_5', 'template_6']
    folio_data = models.db.session.query(folios.Folio).all()

    if page_index == 2:
        
        if not profile_form.validate_on_submit():
          
            return render_template('/accounts/dashboard.html', page = page_index, form = profile_form, template_cards = template_cards, folio_data = folio_data)
  
        folio = folios.Folio()
        profile_form.populate_obj(folio)
        models.db.session.add(folio)
        models.db.session.commit()

        return redirect(url_for("accounts.dashboard"))
        
    if page_index == 3:
        return render_template("/accounts/dashboard.html", page = page_index , form = profile_form, template_cards = template_cards, folio_data = folio_data)
    
    return render_template("/accounts/dashboard.html", page = page_index , form = profile_form, template_cards = template_cards, folio_data = folio_data)

@bp.route("/<folio_id>")
@login_required
def view(folio_id):
    folio = (
        models.db.session.query(folios.Folio)
        .filter_by(
            id=folio_id,
        )
        .first()
    )

    return render_template("/myprofile.html", folio=folio)

@bp.route("/<folio_id>/update", methods=["GET", "POST"])
def update(folio_id):
    folio = (
        models.db.session.query(folios.Folio)
        .filter_by(
            id=folio_id,
        )
        .first()
    )
    template_cards = ['template_1', 'template_2','template_3', 'template_4','template_5', 'template_6']
    folio_data = models.db.session.query(folios.Folio).all()
    
    profile_form = createprofile.ProfileDetailFrom(obj=folio)
    if not profile_form.validate_on_submit():
         return render_template("/accounts/dashboard.html", page = 2 , form = profile_form, template_cards = template_cards, folio_data = folio_data)

    profile_form.populate_obj(folio)

    # models.db.session.update(folio)
    models.db.session.commit()

    return redirect(url_for("accounts.dashboard"))


@bp.route("/<folio_id>/delete")
@login_required
def delete(folio_id):
    folio = (
        models.db.session.query(folios.Folio)
        .filter_by(
            id=folio_id,
        )
        .first()
    )

    models.db.session.delete(folio)
    models.db.session.commit()

    return redirect(url_for("accounts.dashboard"))

