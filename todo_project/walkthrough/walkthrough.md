# Django Todolist
## Walkthrough

This walkthrough is a first introduction to Django and follows roughly the [djangoproject.com](
https://docs.djangoproject.com/en/2.1/intro/tutorial01/) tutorial with screenshots and terminal output for the complete beginner.

I have broken the walkthrough up into very small bits to

## 1. Project Setup

### 1.1 Setup
> Create a virtual environment, activate it, install Django, and start a new project called todo_project .

Create a virtual environment
```
python3 -m venv env
```
Activate the virtual environment
```
source env/bin/activate
```
Install Django in the virtual environment
```
pip install django
```
Terminal output
```
Collecting django
  Using cached https://files.pythonhosted.org/packages/32/ab/22530cc1b2114e6067eece94a333d6c749fa1c56a009f0721e51c181ea53/Django-2.1.2-py3-none-any.whl
Collecting pytz (from django)
  Using cached https://files.pythonhosted.org/packages/30/4e/27c34b62430286c6d59177a0842ed90dc789ce5d1ed740887653b898779a/pytz-2018.5-py2.py3-none-any.whl
Installing collected packages: pytz, django
Successfully installed django-2.1.2 pytz-2018.5
You are using pip version 10.0.1, however version 18.0 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(env) ➜  todo
```
Start a new project called todoapp
```
django-admin startproject todo_project
```
Verify the project works
```
cd todo_project
python manage.py runserver
```
Terminal output
```
Performing system checks...

System check identified no issues (0 silenced).

You have 15 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

October 05, 2018 - 08:10:20
Django version 2.1.2, using settings 'todo_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Apply migrations as suggested
```
python manage.py migrate
```
Terminal output
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying sessions.0001_initial... OK
  ```
### 1.2. Create App
> Create an app named todolist

```
python manage.py startapp todo_list
```
### 1.3 Register the app
Insert a reference to the `todo_list` app using dot notation to describe the path with this structure:

```
project folder
    app folder
        apps.py file
            App config class
```
Open `todo_project/todo_list/apps.py` and find the `TodoListConfig` class
```py
...
class TodoListConfig(AppConfig):
    name = 'todo_list'
```
Copy the name of the class, open `todo_project/todo_project/settings.py` and find the `INSTALLED_APPS` section

```py
...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
...
```

Specifically: `todo_project/todo_list/apps.py > TodoListConfig`

```py
...
INSTALLED_APPS = [
    'todo_list.apps.TodoListConfig',
    'django.contrib.admin',
    'django.contrib.auth',
...
```
Let's see if everything is working by running the server in terminal and checking `http://127.0.0.1:8000/`
```
python manage.py runserver
```
Open a browser and enter `http://127.0.0.1:8000/` in the address bar. Should look like this:

![](https://www.dropbox.com/s/hx9ecysqg2rde6o/Screenshot%202018-10-05%2010.46.51.png?raw=1)


### 1.4 Create a view
> Create a view that returns a simple text to the `/todo` endpoint URL

This requires us to set up some routing in Django - ie tell Django where stuff is, what it is called etc.

First step is to create the view. Open up the `todo_project/todo_list/views.py`. Looks like this for me:

```py
from django.shortcuts import render

# Create your views here.
```
Not much here - we need to create the first view (ie page). Change it to:

```py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")
```
If you try going to `127.0.0.1:8000/todo` you will not get the "Hello World!" page because we haven't told Django that we made this page.

Let's fix that.

### 1.5 URL Routing
> Register the URL routes using both the app-level as well as the project-level urls.py file

Next step is to **create** a file called `urls.py` inside the `todo_project/todo_list` folder.

In terminal go to your app folder `/todo_project/todo_list` and create the urls.py file

```
touch urls.py
```
Then open the empty file (`todo_project/todo_list/urls.py`) in your editor of choice and edit it to look like this:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
```
Now open the project urls.py file located in `/todo_project/todo_project/urls.py`. It should look like this:
```py
...
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```
Change it to
```py
...
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('todo/', include('todo_list.urls')),
    path('admin/', admin.site.urls),
]
```
Ok, awesome. Now let's try to run the server from terminal
```terminal
python manage.py runserver
```
And then go to `http://127.0.0.1:8000/todo/` in your browser:
![](https://www.dropbox.com/s/zhv6xdaf2ksy96l/Screenshot%202018-10-05%2011.42.47.png?raw=1)
# 🙌

Ok - let's break this down...

```
"Hello World!"
    > HttpResponse
        > index()
            > todo_project/todo_list/urls.py
                > todo_project/urls.py
                    > django.urls
                        > Http response
                            > browser
```

1. we created what is called a "view" in Django. Our view is the simplest possible view that just returns a HttpResponse with the string "Hello World!"

2. In the file `todo_project/todo_list/urls.py` (app urls) we imported the views.py file and referenced `views.index` to the path `''`

3. In the file `todo_project/todo_project/urls.py` (project urls) we told Django that the `todo/` endpoint should reference the `todo_project/todo_list/urls.py` for paths local to the `todo_list` app.

Journey from the browser down to the "Hello World":

1. we hit the `todo/` endpoint (for now `127.0.0.1:8000/todo/` on our local server) in the browser
2. Django catches the HTTP request via it's `django.urls` library
3. The request is returned to the path() method we called in the `todo_project/urls.py`
4. And passed to the path() method we called in the `todo_list/urls.py` file
5. And passed to the index() method in the `todo_project/todo_list/views.py`
6. And passed to the HttpResponse() method inside the index() function.
7. Which returns "Hello World!"

Journey from "Hello World!" to the browser

1. we call the `index()` method in the `todo_project/todo_list/views.py`
2. which returns "Hello world!" to the `HttpResponse()`` method
3. which is returned to the `path()` method we called in the `todo_list/urls.py` file
4. which returns the `HttpResponse` to the path() method we called in the `todo_project/urls.py`
5. which then returns it to the `django.urls`
6. which then returns it to the browser.

---

## 2. Models

### 2.1 TodoList class
> Create a TodoList class that contains a title and a completed attribute. completed will be a count of items associated with this list that have been completed

Open up the `todo_project/todo_list/models.py` file. Mine looks like this:

```py
from django.db import models

# Create your models here.
```
Change it to
```py
from django.db import models

class TodoList(models.Model):
    title = models.Charfield(max_length=50)
    completed = models.IntegerField(default=0)
```

### 2.2. TodoItem class
> Create a TodoItem class that contains a reference to the TodoList that it is part of, as well as a name, a description, a date_created and a due_date attribute

```py
from django.db import models

class TodoList(models.Model):
    title = models.Charfield(max_length=50)
    completed = models.IntegerField(default=0)

class TodoItem(models.Model):
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    name = models.Charfield(max_length=50)
    Description = models.Charfield(max_length=200)
    date_created = models.DateTimeField('date created')
    due_date = models.DateTimeField('date due')
```
### 2.3 Custom function
> Add a custom function to your TodoItem class that allows querying how many days are left before a TodoItem is due

```py
from django.db import models
from django.utils import timezone

class TodoList(models.Model):
    title = models.Charfield(max_length=50)
    completed = models.IntegerField(default=0)

class TodoItem(models.Model):
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    name = models.Charfield(max_length=50)
    Description = models.Charfield(max_length=200)
    date_created = models.DateTimeField('date created')
    due_date = models.DateTimeField('date due')

    def days_left(self):
        return self.due_date() - timeszone.now()
```

### 2.4 `__str__()` function
> Add descriptive `__str__()` methods to create a readable string representation of your objects

```py
from django.db import models
from django.utils import timezone

class TodoList(models.Model):
    title = models.Charfield(max_length=50)
    completed = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class TodoItem(models.Model):
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    name = models.Charfield(max_length=50)
    Description = models.Charfield(max_length=200)
    date_created = models.DateTimeField('date created')
    due_date = models.DateTimeField('date due')

    def __str__(self):
        return self.name

    def days_left(self):
        return self.due_date() - timeszone.now()
```
### 2.5 Migrations
> Complete the necessary migrations to create the tables and make your db functional

#### Commit migrations
Use `makemigrations` to create a snapshot of the model state - a bit like `commit` in git.
```sh
python manage.py makemigrations todo_list
```
Terminal output
```
Migrations for 'todo_list':
  todo_list/migrations/0001_initial.py
    - Create model TodoItem
    - Create model TodoList
    - Add field todolist to todoitem
```
#### Push migrations
Use `migrate` to migrate the models to the database - a bit like `push` in git

Register the `todo_list` app in

```sh
python manage.py migrate
```
Terminal output
```
Applying todo_list.0001_initial... OK
```
### 2.6 Register models
> Register both models in your admin panel

Open `todo_list/admin.py`. Mine looks like this:
```py
from django.contrib import admin

# Register your models here.
```
Change it to:
```py
from django.contrib import admin
from .models import TodoList, TodoItem

admin.site.register((TodoList, TodoItem))
```
What this means call the `register` method inside the `site` module inside the `admin` module inside the `contrib` module inside the `django` module

```
(TodoList, TodoItem)
    > register
        > site
            > admin
                > contrib
                    > django
```    

Notice I passed a tuple to the register function to avoid repeating the same line of code.

### 2.7 Admin
> Validate the db's functionality by adding two TodoLists and a couple of TodoItems each through the admin panel

First we need to create a user so we can log in to the admin panel
```
python manage.py createsuperuser
```
Input information when prompted
```
Username (leave blank to use 'my_user'):
Email address:  
Password:
Password (again):
```
Output
```
Superuser created successfully.
```
Cool - lets try the admin panel. In the browser, navigate to `http://127.0.0.1:8000/admin/`

<img src="https://www.dropbox.com/s/6f8kqxifxgarx1b/Screenshot%202018-10-05%2015.52.28.png?raw=1" alt="" width="300"/>

Type in your username and password and click log in

<img src="https://www.dropbox.com/s/vieu46ben6mv0sh/Screenshot%202018-10-05%2015.53.47.png?raw=1" width="300"/>

# ✌️
Alright! You have a Django server running with an admin panel and a database!

Try making lists and items and explore the admin panel.

That concludes the second step of this walkthrough. You now have a project, app, database and access to the admin panel.

## 3. Views and Tables

### 3.1 Todolists overview page

#### 3.1.1 Upgrade the view
> Edit the view that points to the /todo endpoint so that it lists all available TodoLists

```py
from django.http import HttpResponse
from .models import TodoList

def index(request):
    lists = TodoList.objects.all()
    output = ', </br>'.join(l.title for l  in lists)
    return HttpResponse(output)
```

#### 3.1.2 Templates folder
> Create a /template folder for your app (make sure you closely follow the suggestions in regards to that on the Django tutorial!)

First we need to create a `todo_project/todo_list/templates/todo_list` folder. First navigate to `todo_project/todo_list`. Then:

```
mkdir templates
mkdir templates/todo_list
touch templates/todo_list/index.html
```
 #### 3.1.3 Upgraded index.html
> Create a template for the previously mentioned function, so that it lists all available TodoLists as clickable items in a bullet-point list

Ok, first I am going to revise the `views.py` file to use the render method instead of the HttpResponse() method so that I can use the templates further down:

```py
from django.shortcuts import render
from .models import TodoList #, TodoItem

def index(request):
    lists = TodoList.objects.all()
    return render(request, 'todo_list/index.html', {'lists':lists})
```
I am returning a tuple consisting of the request, the template name and a dictionary.

I can then use this tuple in the `template/todo_list/index.html` - like this:
```py
{% if lists %}
    <ul>
        {% for a_list in lists %}
            <li> <a href="/todo/{{ a_list.id }}/"> {{ a_list.title }} </a> </li>
        {% endfor %}
    </ul>
{% else %}
    <p>No lists on file</p>
{% endif %}
```
#### 3.1.4 Redirect to TODO list
> The links should redirect to a new URL that is specific to the clicked TodoList (hint: use the TodoList object's ID)

We already have what we need in the `todo_list/models.py` file, so let's move to the routing in the `todo_list/urls.py` file and include the path to the lists
```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # /todo/
    path('<int:todolist_id>/', views.lists, name='lists'),  # /todo/5/
]
```
What is going on here is that whenever someone hits the endpoint `/todo/` followed by an integer, I will send them to the lists view with the integer.

#### 3.1.5 Render the page
> Use Django's render() shortcut to pass the necessary information from the db to your template

Next we need to make sure our controller - the `/todo_list/views.py` file has a corresponding lists view.
```py
from django.shortcuts import get_object_or_404, render
from .models import TodoList #, TodoItem

def index(request):
    lists = TodoList.objects.all()
    return render(request, 'todo_list/index.html', {'lists':lists})
```

---

### 3.2 Todolist items page

#### 3.2.1 Fetch todo items

> Create another function in views.py that takes as an input a TodoList s ID and fetches all associated TodoItems from the database.

```py
from django.shortcuts import get_object_or_404, render
from .models import TodoList #, TodoItem

def index(request):
    lists = TodoList.objects.all()
    return render(request, 'todo_list/index.html', {'lists':lists})

def lists(request, todolist_id):
    my_list = get_object_or_404(TodoList, pk=todolist_id)
    return render(request, 'todo_list/lists.html', {'my_list':my_list})
```
In the first line of the lists function, we are querying the TodoList object/table using the todolist_id we got passed from the  urls.py as a primary key lookup. In the second line we are passing the infomation in the exact same way we did in the index method.

Now we need to make a template for the `lists` view to show all the items on the list. Inside the `templates/todo_list` folder I create a file called `lists.html`
```
touch lists.html
```
And edit it to have the following content

```py
{{ todolists }}
<h1>{{ my_list.title}}</h1>
<ul>
    {% for item in my_list.todoitem_set.all %}
        <li>{{item.name}}</li>
    {% endfor %}
</ul>
```
Here we iterate through the items related with a foreign key in the TodoList-TodoItem classes in the models.py file using the django attribute todoitem_set.all. It took me a while to understand that this attribute that has the same name as its model but in lowecase is just something that is available to me on all models with a foreign key relationship.


#### 3.2.2 Display items

> Create a template that displays all TodoItems of that TodoList as checkboxes
Remember to register the URLs to allow for correct URL routing
