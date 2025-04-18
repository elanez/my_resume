# Personal Resume Website

A modern, dynamic personal resume website built with Django that allows you to showcase your professional experience, skills, and blog posts. This a passion project created with the use of AI agents for personal improvement and development.

## Features

- Professional resume display with sections for experience, education, and skills
- Blog functionality to share your thoughts and insights
- Responsive design that works on all devices
- Easy-to-use admin interface for content management

## Technologies Used

- **Django**: A high-level Python web framework for rapid development
- **Python**: The core programming language
- **HTML/CSS**: For responsive and modern design
- **JavaScript**: For interactive features and dynamic content
- **PostgreSQL**: Database for storing content and user data

## Getting Started

1. Clone the repository
2. Install the required dependencies
3. Set up your environment variables
4. Run migrations
5. Start the development server

### Environment Variables Setup

Create a `.env` file in the root directory with the following variables:

```env
SECRET_KEY=your-secret-key-from-django
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=
DATABASE_PORT=
```

## Project Structure

```
my_resume/
├── manage.py
├── requirements.txt
├── .env
├── resume/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
└── blog/
    ├── models.py
    ├── views.py
    ├── urls.py
    └── templates/
        └── blog/
            ├── base.html
            ├── post_list.html
            └── post_detail.html
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
