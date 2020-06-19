from flask import render_template, request, Blueprint
from website.models import Post


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
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
    return render_template('opportunities.html', title='Opportunities Fall 2020')


@main.route("/resources")
def resources():
    return render_template('resources.html', title='Resources')

