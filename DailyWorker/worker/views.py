from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json


from .models import *


# Create your views here.
def index(request):
	return render(request, "worker/index.html")

def search(request):
	req = request.POST.get("search")
	tool = tools.objects.all()
	users = User.objects.all()
	for i in tool:
		if req in i.tool.lower():
			return render(request,"worker/find.html",{
				"tool" :tools.objects.filter(tool=i)
				})

	
		# if i.tool == req:
		# 	print(i.tool, req)
		# 	error = "you are in "
		# 	return render(request, "worker/404.html",{
		# 		"error":error
		# 		})
		# else:
		# 	print(i.tool, req)

		# 	error = "we dont have your request"
		# 	return render(request, "worker/404.html",{
		# 		"error":error
		# 		})


@login_required
def worker(request):
	
	if request.method == "POST":
		job = request.POST.get("job")
		gender = request.POST.get("gender")
		country = request.POST.get("country")
		fname = request.POST.get("fname")
		lname = request.POST.get("lname")
		email = request.POST.get("email")
		nat = request.POST.get("nat")
		phone = request.POST.get("phone")
		title = request.POST.get("title")
		avater = request.POST.get("avater")
		user = User.objects.filter(id=request.user.id)
		if job != "":
			user.update(job=job)
			print(job)
		if gender != "":
			user.update(gender=gender)
			print(gender)
		if country != "":
			user.update(country=country)
			print(country)
		if fname != "":
			user.update(first_name=fname)
			print(fname)
		if lname != "":
			user.update(last_name=lname)
			print(lname)
		if email != "":
			user.update(email=email)
			print(email)
		if nat != "":
			user.update(nat=nat)
			print(nat)
		if phone != "":
			user.update(phone=phone)
			print(phone)
		if title != "":
			user.update(title=title)
			print(title)
		if avater != "":
			user.update(picture=avater)
			print(avater)
		return HttpResponseRedirect(reverse("worker"))
	return render(request, "worker/worker.html")
@login_required
def seeker(request):
	workers = User.objects.all()
	return render(request, "worker/seeker.html",{
		"workers":workers
		})

@login_required
def rent(request):
	rent_tools = tools.objects.all()
	if request.method == "POST":
		tool = request.POST.get("tool")
		owner = request.POST.get("owner")
		image = request.POST.get("image")
		desc= request.POST.get("desc")
		price = request.POST.get("price")
		country = request.POST.get("country")
		try:
			tool = tools(tool=tool, owner=owner, image=image, desc=desc, price=price, country=country)
			tool.save()
			return HttpResponseRedirect(reverse("rent"))
		except:
			return HttpResponse("error in rent")
	
	return render(request, "worker/rent.html",{
		"tools":rent_tools
		})

def borrow(request, toolid):
	tool = tools.objects.get(id=toolid)
	
	renter = Reserve.objects.filter(tool=tool.tool)
	print(renter)
	
	return render(request, "worker/borrow.html", {
		"tool":tool,
		"renter":renter
		})


def reserve(request, toolid):
	tool = tools.objects.filter(id=toolid)
	print(tool)
	if request.method == "POST":
		renter = request.POST.get("renter")
		place =  request.POST.get("place")
		days = request.POST.get("days")
		for t in tool:
			toolname = t.tool
			print(toolname)
		try:
			reserved = Reserve(tool=toolname, renter=renter, place=place, days=days)
			reserved.save()
			tool.update(is_rented="true")
			return HttpResponseRedirect(reverse("rent"))
		except:
			print("some error")
			# return render(request, "worker/404.html",{
			# 	"error":"there is some issues with rent tool"
			# 	})

	

@login_required
def profile(request):
	username = request.user.username
	user = User.objects.filter(username=username)

	return render(request, "worker/profile.html",{
		# "username":username,
		"user":user
		})



def login_view(request):
	if request.method == "POST":

		# Attempt to sign user in
		username = request.POST["username"].capitalize()
		password = request.POST["password"]
		user = authenticate(request, username=username, password=password)

		# Check if authentication successful
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse("index"))
		else:
			return render(request, "worker/login.html", {
				"message": "Invalid username and/or password."
			})
	else:
		return render(request, "worker/login.html")


def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse("index"))


def register(request):
	if request.method == "POST":
		username = request.POST["username"].capitalize()
		email = request.POST["email"]

		# Ensure password matches confirmation
		password = request.POST["password"]
		confirmation = request.POST["confirmation"]
		if password != confirmation:
			return render(request, "worker/register.html", {
				"message": "Passwords must match."
			})

		# Attempt to create new user
		try:
			user = User.objects.create_user(username, email, password)
			user.save()
		except IntegrityError:
			return render(request, "worker/register.html", {
				"message": "Username already taken."
			})
		login(request, user)
		return HttpResponseRedirect(reverse("index"))
	else:
		return render(request, "worker/register.html")






###########################################################

def randomuser():
	# construction industry
	# "Labourers are responsible for doing manual work requiring high physical fitness and strength to construct structures or buildings."
	# "bricklayer"
	res = requests.get("https://randomuser.me/api/")
	users = res.json()
	user = users["results"][0]
	gender = user["gender"]
	title = user["name"]["title"]
	first = user["name"]["first"]
	last = user["name"]["last"]
	email = user["email"]
	phone = user["phone"]
	picture = user["picture"]["thumbnail"]
	country = user["location"]["country"]
	nat = user["nat"]
	username = user["login"]["username"]
	password = user["login"]["sha256"]
	worker = User(gender=gender, password=password, title=title, first_name=first, last_name=last, email=email, phone=phone, picture=picture, country=country, nat=nat, username=username)
	worker.save()
	print(f"Name: {title}.{last}{first}, gender: {gender}")

