A sample library management application that aims to simulate the borrowing and renewal of library books via a Django web application.

###Requirements
* Oracle 11g (MySQL, PostGRE SQL or any other database that you prefer)
* Django 1.9 
* Python 2.4
* cx_Oracle 5.0.2 (For those using Oracle database)


###Setup
1. To establish the connection to your database, go to the settings.py file located at miniproj/miniproj/settings.py and make appropriate changes in the DATABASES section. For more details on how to do this, check [https://docs.djangoproject.com/en/1.9/ref/databases/]

2. Run 
```python manage.py migrate ```. 
  This command looks into the INSTALLED_APPS directory and createas any tables required as per the settings specified in settings.py file.
3. If you decide to play around with the models.py file, make sure that you run the following **three commands after each and every change** you make to the file.
  * Change your models (in models.py).
  * Run ```python manage.py makemigrations``` to create migrations for those changes
  * Run ```python manage.py migrate``` to apply those changes to the database.

4. To run the development server, run  ```python manage.py runserver ```


