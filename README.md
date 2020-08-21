# Try-Django, add new app precedure


1. Create a New App named Blog
    1. python manage.py startapp blog

2. Add ‘Blog’ to Django project
    1. trydjango-setting.py-INSTALLED-APP. add ‘blog

3. Create a Model named Article
    1. blog-modles-new class

4. Run Migrations
    1. python manage.py makemigrations
    2. python manage.py migrate

5. Create a ModelForm for Article
    1. modify blog/model.py
    2. modify blog/admin.py

6. Create ‘article-list.html’ & ‘article_detail.html’  etc. Template

7. Add Article Model to the admin
    1. edit blog/admin.py, import .models from Article

8. Save a new Article object in the admin
