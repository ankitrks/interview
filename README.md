# interview
Interview Projct - Ankit Rastogi

Steps to setup:
1. Clone the repo
2. Go to repo and configure python environment
   virtualenv -p python3.7 pyenv
3. Activate python environment
   source pyenv/bin/activate
4. Install dependencies
   pip install -r req.txt
5. Run migrations
   python manage.py migrate
6. Run django server
   python manage.py runserver
7. It will be available on http://localhost:8000
8. Postman collection is also committed along with the code:
   postman_collection.json
