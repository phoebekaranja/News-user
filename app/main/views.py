from flask import render_template
from app import app

# Views
@app.route('/')
def index():
    '''
    my index page
    :return:
    '''
    sources=  get sources()
    print(Sources)
    message= "Test Dynamic message"
    return render_template('index.html' sources =sources, message = message)
@main.route('/articles/<id>')
def articles(id):
    '''
    View  page function that returns the  details page and its data
    '''
    Name = "Phoebe"
    articles=get_articles(id)
    return render_template('articles.html', articles = articles, name=name,name_source=id )
print(articles)
    title=f'{articles.title}'


@main.route('/categories/<category_name>')
def categories(category_name):

    '''
    View  page function that returns the details page and its data
    '''
    category="phoebe"
    category=get_category(category_name)
    print(category_name)
    category_name1=category_name

    return render_template('categories.html', category=category,name_source=id,category_name1=category_name1)
