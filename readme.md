`Getting started with Blog Application`

``Installation``
 Create a virtual environment: python -m venv env
 Activate the virtual environment:
 On Windows: .\env\Scripts\activate
 On Linux/Mac: source env/bin/activate
 Install the dependencies: pip install -r requirements.txt
 Run the migrations: python manage.py migrate
 Create a superuser: python manage.py createsuperuser
 Start the development server: python manage.py runserver
 Access the app at http://localhost:8000/ in your web browser.
 
``API Endpoints``
GET /blogs/ `List all blog posts.`
POST /blogs/ `Create a new blog post.`
GET /blog/id/ `Retrieve a single blog post by ID.`
PUT /blog/id/ `Update a blog post by ID.`
DELETE /blog/id/ `Delete a blog post by ID.`

``Authentication``
Add `JWT <access_token> while making request`
POST /user/register/ To register a user with username and password
POST /user/login/ Obtain an access token by providing valid credentials (username and password)
POST /user/token/refresh/ Refresh an access token by providing a valid refresh token in the body




