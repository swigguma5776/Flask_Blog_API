from flask import Blueprint, render_template, request, url_for, redirect 
import requests
from blog_inventory.models import Blogs


site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        tags = request.form['tag']   #need to add if statements to call upon object based on what the user inputs
        sortBy = request.form['sortby']
        direction = request.form['direction']
        
        if not tags:
            return {"error: Tags parameter is required"}, 400

        tags = tags.split(',')
        print(tags, sortBy, direction)

        if not sortBy and not direction:
            blogs = Blogs(tags)
            if blogs.fetch_posts == False:
                return {"error: Tags parameter is required"}, 400

        elif not direction:
            blogs = Blogs(tags, sortBy, 'asc')
            if blogs.fetch_posts == False:
                return {"error: Tags parameter is required"}, 400
            if blogs.check_sortby() == False:
                return {'error':'sortBy parameter is invalid'}, 400

        else:
            blogs = Blogs(tags, sortBy, direction)
            if blogs.fetch_posts == False:
                return {"error: Tags parameter is required"}, 400
            if blogs.check_sortby() == False:
                return {'error':'sortBy parameter is invalid'}, 400
            if blogs.check_dir() == False:
                return {'error':'direction parameter is invalid'}, 400

        #checking tag verification 
        blogs.fetch_posts()
        return blogs.get_posts()
        
        
    else:
        return render_template('index.html')


@site.route('/ping')
def ping():
    ping = requests.get(f'https://api.hatchways.io/assessment/blog/posts?tag=tech').status_code
    if ping == 200:
        print({'success':True}, 200)

    return {'failure': False}, 400


@site.route('/posts', methods = ['GET']) 
def post():
    #Grabbing the parameters 
    tags = request.args.get('tags')
    sortBy = request.args.get('sortBy')
    direction = request.args.get('direction')

    if not tags:
        return {"error: Tags parameter is required"}, 400

    tags = tags.split(',')
    print(tags, sortBy, direction)

    if not sortBy and not direction:
        blogs = Blogs(tags)
        if blogs.fetch_posts == False:
            return {"error: Tags parameter is required"}, 400

    elif not direction:
        blogs = Blogs(tags, sortBy, 'asc')
        if blogs.fetch_posts == False:
            return {"error: Tags parameter is required"}, 400
        if blogs.check_sortby() == False:
            return {'error':'sortBy parameter is invalid'}, 400

    else:
        blogs = Blogs(tags, sortBy, direction)
        if blogs.fetch_posts == False:
            return {"error: Tags parameter is required"}, 400
        if blogs.check_sortby() == False:
            return {'error':'sortBy parameter is invalid'}, 400
        if blogs.check_dir() == False:
            return {'error':'direction parameter is invalid'}, 400

    #checking tag verification 
    blogs.fetch_posts()
    return blogs.get_posts()  
