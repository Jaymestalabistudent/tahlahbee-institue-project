flask_blog/
├── flaskblog/
│   ├── __init__.py
│   ├── models.py
│   ├── config.py
│   ├── posts/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── forms.py
│   ├── main/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── users/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── utils.py
│   │   └── forms.py
│   ├── templates/
│   │   ├── errors/
│   │   │   ├── 403.html
│   │   │   ├── 404.html
│   │   │   └── 500.html
│   │   ├── post.html
│   │   ├── reset_password.html
│   │   ├── post.html
│   │   ├── login.html
│   │   └── register.html
│   │   └── (more templates)
│   └── static/
│       ├── css/
│       │   └── mainpage.css
│       │   └── misc.css
│       │   └── preloader.css
│       ├── img/
│       │   └── logo/
│       │   └── profile_pics/
│       └── js/
│           └── mainpage.js
│           └── misc.js
│           └── preloader.js
├── migrations/
├── .gitignore (remove .env from git so secure environment variables are not exposed)
├── config.py
├── requirements.txt
├── .env (your for local testing )
└── run.py
