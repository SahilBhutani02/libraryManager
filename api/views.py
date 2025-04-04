from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    urls = {
        "books": "/api/v1/books/",
        "students": "/api/v1/students/",
    }

    content = f"""
    <html>
        <body>
            <h2>Select a Page to Visit:</h2>
            <ul>
                <li><a href="{urls['books']}">Books API</a></li>
                <li><a href="{urls['students']}">Students API</a></li>
            </ul>
        </body>
    </html>
    """
    
    return HttpResponse(content)