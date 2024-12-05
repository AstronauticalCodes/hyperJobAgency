from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('''<h2>Welcome to HyperJob!</h2>
<p><a href="/login">Login</a></p>
<p><a href="/logout">Logout</a></p>
<p></p><a href="/signup">Signup</a></p>
<p><a href="/vacancies">Vacancies</a></p>
<p><a href="/resumes">Resume</a></p>
<p><a href="/home">Personal Profile</a></p>''')