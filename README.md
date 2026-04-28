# DjangoCRUD

An example CRUD app using Django and MySQL.

## Install

1. git clone this repo: `git clone https://github.com/AAA-Friends-CS383/DjangoCRUD.git`

2. It's good practice to create a python virtual environment for each new project so as to not dirty your global pip installs. You can do this using python's built-in `venv`

```bash
# use this command to create a venv in the .venv folder.
# This folder will house all your installed pip packages for this project and is not
# tracked by git (we put it in .gitignore)
# use python3 or whatever your python executable is from the command line
python3 -m venv .venv
# alternatively if you use VSC, you can do ctrl+shift+p Python: Create Environment
# this will create an environment, and set it as your workspace's default venv

# activate the venv in your current terminal 
source .venv/bin/activate
# or use this on windows cmd prompt
.venv\Scripts\activate
# or use this on windows powershell
.\.venv\Scripts\Activate.ps1

# if you use VSC but didn't create this with VSC's command 
# but want to set your venv as the default workspace venv
# do ctrl+shift+p Python: Select Interpreter and choose the one from .venv
```

3. install the required packages. It is common practice to include a `REQUIREMENTS.txt` file along with all python projects that require installed packages. You can use `pip freeze > REQUIREMENTS.txt` to save a list of the packages installed and their installed versions into a `REQUIREMENTS.txt` file. Use the following command to install those listed requirements.

```bash
# this pip installs all the packages specified in the REQUIREMENTS.txt
pip install -r REQUIREMENTS.txt
```

You can inspect the `REQUIREMENTS.txt` file to see what packages will be installed but it also includes all the dependencies as well. If you were to start working on this project from scratch, you would instead `pip install` the main packages manually like so

```bash
# install Django
pip install django
# install PyMySQL
pip install pymysql
# install dotenv
pip install python-dotenv
# once you're happy with the packages you've installed for this feature, 
# pip freeze it and git commit the resulting REQUIREMENTS.txt if this is your project
```

## Running

`python manage.py runserver`

## Following along

Simply follow along the git changes by doing `git checkout <step>` where `<step>` is the current step you're at in the walkthrough. ex. `git checkout 1` is the 1st step. You can check what the changes were by doing `git show`.

## Additional steps

### Step 1.
1. Django expects a db to already be created, so open a terminal, log into mysql, and `CREATE DATABASE your_db`
2. If doing this from a blank project, do `django-admin startproject my_project_name` to create the project folder structure
3. If doing this from a blank project, edit the project folder's `__init__.py` to match this repo's 
4. If doing this from a blank project, edit the project folder's `settings.py` to match this repo's taking note of the `SECRET_KEY` value first
5. make a `.env` file at root with the following
```bash
SECRET_KEY=key_from_settings.py
DB_NAME=your_db
DB_USER=django_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
DEBUG=True
```
6. Run `python manage.py migrate` to create the initial tables for Django’s built-in systems

### Step 2.
1. The django project you created is for the whole website. If doing this from a blank project, you will need to create an app as well with `django-admin startapp name_of_app`
2. If doing this from a blank project, register the app by editing `settings.py` again with this repo's at this commit (do `git show`) and editing the `urls.py` file in the same path with this repo's at this commit

### Step 3.
1. You will need to create the `todo` table in the database by running `python manage.py makemigrations name_of_app` followed by `python manage.py migrate`
2. If you would like to be able to edit the app's data through Django's admin panel, do `python manage.py createsuperuser` and follow the prompts. The admin url is at http://localhost:8000/admin/
