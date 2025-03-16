# Arbitration Case Lookup

This is a Django-based web application for looking up arbitration case details.

## Features
- Enter a case name to fetch case details.
- View case description and timeline.
- Uses Tailwind CSS for styling.

## Installation & Setup

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Django
- Git

### Clone the Repository
```sh
git@github.com:maheshwari-nitin/django-arbitration-app.git
cd django-arbitration-app
```

### Create a Virtual Environment (Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Apply Migrations
```sh
python manage.py migrate
```

### Run the Development Server
```sh
python manage.py runserver
```
Visit `http://127.0.0.1:8000/cases/` in your browser.

## Deployment
To deploy, configure a production database and set up a web server like Gunicorn or uWSGI with Nginx.

## Contributing
Feel free to fork the repository and submit pull requests!

## License
This project is licensed under the MIT License.

## Contact
For issues, open a GitHub issue or contact the maintainer.

