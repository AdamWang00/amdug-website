from flask import flash, render_template, redirect, url_for, request, Blueprint
from website.main.forms import ContactForm
from website.main.utils import send_contact_email
from website.models import Post


main = Blueprint('main', __name__)


@main.route("/")
def home():
	return render_template('home.html', title='Home')


@main.route("/about")
def about():
	return render_template('about.html', title='About Us')


@main.route("/events")
def events():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=10)
    return render_template('events.html', title='Upcoming Events', posts=posts)


@main.route("/opportunities")
def opportunities():
    return render_template('opportunities.html', title='Opportunities 2020-2021')


@main.route("/resources")
def resources():
    return render_template('resources.html', title='Resources')


@main.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        send_contact_email(form.name.data, form.email.data, form.message.data)
        flash('Your message has been sent. We will get back to you soon!', 'success')
        return redirect(url_for('main.contact'))
    return render_template('contact.html', title='Contact', form=form)
