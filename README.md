## Dushanbe Work Submission APIs (Backend)

#### Developed by Django REST Framework (Windows 10 x64)

##### Test Servers

* Backend: https://dushanbe-backend-apis.herokuapp.com/
* Frontend: https://dushanbe-frontend-vuejs.herokuapp.com/

##### Local Servers

* Backend: http://localhost:8000/
* Frontend: http://localhost:5000/

##### Deployment Commands (Heroku & Git)

```
heroku login
```
```
heroku create dushanbe-backend-apis
```
```
heroku addons:create heroku-postgresql:hobby-dev
```
```
git add .
```
```
git commit -m "first commit"
```
```
git remote -v
```
```
git push origin main
```
```
git push heroku main
```
```
git log
```

##### Collecting Static Assets 

* From Local
```
python manage.py collectstatic
```
* From Heroku (No need if collected from locally)
```
heroku run python manage.py collectstatic
```

##### Access Heroku Bash

```
heroku run bash
```
```
ls
```
```
cd /
```
```
ls
```
```
exit
```
