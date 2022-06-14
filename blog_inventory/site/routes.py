from flask import Blueprint, render_template, request, url_for, redirect 
import requests
from blog_inventory.models import Blogs


site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        tag = request.form['tag']
        sortby = request.form['sortby']
        dir = request.form['direction']
        redirect(url_for('site.ping'))
        return redirect(url_for('site.post', tag=tag, sortby=sortby, dir=dir))
        
    else:
        return render_template('index.html')


@site.route('/ping')
def ping():
    ping = requests.get(f'https://api.hatchways.io/assessment/blog/posts?tag=tech').status_code
    if ping == 200:
        print({'success':True}, 200)
        # return (f"<h1>{ping}</h1>")
    return {'failure': False}, 400


@site.route('/<tag>,<sortby>,<dir>')
def post(tag, sortby, dir):
    blogs = Blogs([tag], sortby, dir)
    print(blogs)
    return render_template('index.html', blogs = blogs)
