
# Creating a Basic HTML Template with Bootstrap

create a basic HTML template using Bootstrap. This template will include a header, content section, and footer.

To get started, open a new HTML file and copy the following code:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    {% block head %}
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
        <title>{% block title %}{% endblock %} - My Webpage</title>
    {% endblock %}
</head>
<body>
    <div id="content">{% block content %}{% endblock %}</div>
    <div id="footer">
        {% block footer %}
            &copy; 2024 by <a href="https://hackerwasii.com/">Waseem Akram💙</a>.
        {% endblock %}
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@1.16.1/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
```

This code sets up the basic structure of an HTML document and includes the necessary CSS and JavaScript files from Bootstrap. It also defines three blocks: `head`, `content`, and `footer`, which can be customized.

