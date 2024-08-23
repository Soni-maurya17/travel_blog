from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# def blog_list_view(request):
#     return render(
#         request,
#         'blog_list.html',
#         context={
#             'articles' : Article.objects.all()
#         }
#     )
    
# def article_view(request,id):
#     return render(
#         request,
#         'article.html',
#         context={
#             'article':Article.objects.get(id=id)
#         }
#     )
# def edit_article_view(request,id):
#     return render(
#         request,
#         'article.html',
#         context={
#             'article':Article.objects.get(id)
#         }
#     )


# Create your views here.
def index(request):
    return render(request,'index.html')


def login_view(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user =authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('index')
        print("welcome",username)
    return render(request,'login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password == cpassword:
            user= User(username=username, email=email)
            user.set_password(password)
            user.save()
            return redirect('login')
    return render(request,'register.html')

def logout_view(request):
    logout(request)
    return redirect('index.html')

