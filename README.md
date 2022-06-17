# Flask_Blog_API
Creating a simple JSON API utilizing the Flask framework that retrieves blog posts from a 3rd party API using inputed tags, sorts and stores them without duplications and displays them to the user. 


GET STARTED HERE:

If you want this application to run locally, clone this repo, and do the following:

    cd into the cloned repo flask_blog_api

Create a Python virtual env:

    python -m venv <name_of_your_env>

Activate Python virtual env AND set Flask ENV variables in terminal/CMD:

  Mac

    source <name_of_your_env>/bin/activate
    export FLASK_APP=hatch_api
    export FLASK_ENV=development

  Windows

    <name_of_your_env>\Scripts\activate.bat
    set FLASK_APP=hatch_api
    set FLASK_ENV=development

Install dependencies:

    pip install -r requirements.txt

Start dev server:

    flask run
