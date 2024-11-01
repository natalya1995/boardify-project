from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.paginator import Paginator
from .models import Category, Location, Board,UserProfile
from django.contrib import messages
from .forms import UserRegistrationForm,UserLoginForm,BoardForm,UserProfileForm


def home_page(request):
    categories=Category.objects.all()
    last_board=Board.objects.filter(is_active_board=True).order_by('-created_at')[:8]
    context={
        'categories':categories,
        'last_board':last_board
    }
    return render(request, "./client/home.html",context)

def all_boards_page(request):
    board_list=Board.objects.filter(is_active_board=True).order_by('-created_at')
    paginator=Paginator(board_list,12)
    page_number=request.GET.get('page')
    boards=paginator.get_page(page_number)
    context={
        'boards':boards,
        'page_number':page_number
    }
    return render(request,"./client/all-boards.html",context)

def categories_page(request):
    categories=Category.objects.all()
    lacations=Location.objects.all()
    context={
        'categories':categories,
        'lacations':lacations
    }
    return render(request,"./client/categories.html",context)

def search_results_page(request):
    query=request.GET.get('q')
    boards=Board.objects.filter(title__icontains=query,is_active_board=True)
    paginator=Paginator(boards,12)
    page_number=request.GET.get('page')
    search_boards=paginator.get_page(page_number)
    context={
        'search_boards':search_boards,
        'query':query
    }
    return render(request,"./client/search-results.html",context)

def boards_by_category_page(request,slug):
    category=get_object_or_404(Category,slug=slug)
    board_list=Board.objects.filter(category=category,is_avtive_board=True).order_by('-created_at')
    paginator=Paginator(board_list,12)
    page_number=request.GET.get('page')
    boards=paginator.get_page(page_number)
    context={
        'boards':boards,
        'category':category
    }
    return render(request,"./client/boards-by-category.html",context)

def boards_by_location_page(request,slug):
    location=get_object_or_404(Location,slug=slug)
    board_list=Board.objects.filter(location=location,is_avtive_board=True).order_by('-created_at')
    paginator=Paginator(board_list,12)
    page_number=request.GET.get('page')
    boards=paginator.get_page(page_number)
    context={
        'boards':boards,
        'location':location
    }
    return render(request,"./client/boards-by-location.html",context)
def board_detail_page(request,pk):
    board=get_object_or_404(Board,pk=pk)
    author=board.userprofile
    context={
        'board':board,
        'author':author
    }
    return render(request,"./client/board-detail.html",context)
def login_page(request):
    if request.method=="POST":
        form=UserLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,"Добро пожаловать в BOARDIFY!")
                return redirect(profile_page)
            else:
                messages.error(request,"Неверный логин или пароль")
    else:
        form=UserLoginForm()
    context={
        'form':form
    }
    return render(request,"./user/login.html",context)

def sign_up_page(request):
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid:
           form.save()
           messages.success(request,"")
           return redirect('login_page')
    else:
        form=UserRegistrationForm()
    context={
        'form':form
    }
    return render(request,"./user/sign-up.html",context)
def logout_action(request):
    logout(request)
    return redirect('home_page')