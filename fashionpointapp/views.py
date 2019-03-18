from django.shortcuts import render
from django.http import HttpResponse
from fashionpointapp.models import Category , Post ,PostComment ,Poll ,PollComment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from fashionpointapp.forms import PostForm,EditForm
from fashionpointapp.models import UserProfile,Post, Rating, Poll, Category
from datetime import datetime


from fashionpointapp.forms import UserForm,UserProfileForm,PollForm
def updatePosts(request):
	context_dict = {}
	ind = int(request.GET['inc'])
	post = Post.objects.all()[ind:ind+3]
	length = len(Post.objects.all())
	state2 = 0
	state1 = 0
	if (ind+3 >= length):
		state2 = 1
	if (ind == 0):
		state1 = 1
	context_dict['state1'] = state1
	context_dict['state2'] = state2
	context_dict['post1'] = post[0]
	context_dict['post2'] = post[1]
	context_dict['post3'] = post[2]
	arp1 = round(post[0].avgRating * 2)
	onp1 = int(arp1 / 2)
	offp1 = int((10 - arp1) / 2)
	hp1 = 0
	if (arp1 % 2 == 1):
		hp1 = 1;
	arp2 = round(post[1].avgRating * 2)
	onp2 = int(arp2 / 2)
	offp2 = int((10 - arp2) / 2)
	hp2 = 0
	if (arp2 % 2 == 1):
		hp2 = 1;
	arp3 = round(post[2].avgRating * 2)
	onp3 = int(arp3 / 2)
	offp3 = int((10 - arp3) / 2)
	hp3 = 0
	if (arp3 % 2 == 1):
		hp3 = 1;
	context_dict['onp1'] = startate(onp1)
	context_dict['offp1'] = startate(offp1)
	context_dict['hp1'] = hp1
	context_dict['onp2'] = startate(onp2)
	context_dict['offp2'] = startate(offp2)
	context_dict['hp2'] = hp2
	context_dict['onp3'] = startate(onp3)
	context_dict['offp3'] = startate(offp3)
	context_dict['hp3'] = hp3
	return render(request, 'fashionpointapp/newPosts.html',context_dict)

def updatePolls(request):
	context_dict = {}
	ind = int(request.GET['inc'])
	poll = Poll.objects.all()[ind:ind+2]
	length = len(Poll.objects.all())
	state3 = 0
	state4 = 0
	if (ind + 2 >= length):
		state4 = 1
	if (ind == 0):
		state3 = 1
	context_dict['state3'] = state3
	context_dict['state4'] = state4
	context_dict['poll1'] = poll[0]
	context_dict['poll2'] = poll[1]
	return render(request, 'fashionpointapp/newPolls.html',context_dict)

def index(request):
	context_dict = {}
	post = Post.objects.all()
	poll = Poll.objects.all()
	state2 = 0
	state4=0
	if (len(post)<=3):
		state2 = 1
	if (len(poll) <= 3):
		state4 = 1
	context_dict['state1'] = 1
	context_dict['state2'] = state2
	context_dict['state3'] = 1
	context_dict['state4'] = state2
	context_dict['post1'] = post[0]
	context_dict['post2'] = post[1]
	context_dict['post3'] = post[2]
	context_dict['poll1'] = poll[0]
	context_dict['poll2'] = poll[1]
	arp1 = round(post[0].avgRating * 2)
	onp1= int(arp1/2)
	offp1 = int((10 - arp1)/2)
	hp1 = 0
	if(arp1 %2 == 1):
		hp1 = 1;
	arp2 = round(post[1].avgRating * 2)
	onp2 = int(arp2 / 2)
	offp2 = int((10 - arp2) / 2)
	hp2 = 0
	if (arp2 % 2 == 1):
		hp2 = 1;
	arp3 = round(post[2].avgRating * 2)
	onp3 = int(arp3 / 2)
	offp3 = int((10 - arp3) / 2)
	hp3 = 0
	if (arp3 % 2 == 1):
		hp3 = 1;
	context_dict['onp1'] = startate(onp1)
	context_dict['offp1'] = startate(offp1)
	context_dict['hp1'] = hp1
	context_dict['onp2'] = startate(onp2)
	context_dict['offp2'] = startate(offp2)
	context_dict['hp2'] = hp2
	context_dict['onp3'] = startate(onp3)
	context_dict['offp3'] = startate(offp3)
	context_dict['hp3'] = hp3
	if request.user.is_authenticated:
		userProfile = UserProfile.objects.get(user=request.user)
		context_dict['userProfile'] = userProfile
		length = len(request.user.first_name)
		context_dict['length']= 87 - length
	context_dict['pos']=1
	return render(request, 'fashionpointapp/index.html',context_dict)

def categories(request):
	context_dict = {}
	if request.user.is_authenticated:
		userProfile = UserProfile.objects.get(user=request.user)
		context_dict['userProfile'] = userProfile
		length = len(request.user.first_name)
		context_dict['length']= 87 - length
	context_dict['pos']=2
	context_dict['categories'] = Category.objects.all()
	return render(request, 'fashionpointapp/categories.html',context_dict)

def show_category(request, category_name_slug):
	context_dict = {}
	if request.user.is_authenticated:
		userProfile = UserProfile.objects.get(user=request.user)
		context_dict['userProfile'] = userProfile
		length = len(request.user.first_name)
		context_dict['length']= 87 - length
	try:
 		category = Category.objects.get(slug=category_name_slug)
 		context_dict['category'] = category
 		context_dict['posts'] = Post.objects.filter(category=category)
 		context_dict['polls'] = Poll.objects.filter(category=category)
	except Category.DoesNotExist:
 		context_dict['category'] = None
	return render(request, 'fashionpointapp/category.html', context_dict)

def contact_us(request):
	context_dict = {}
	if request.user.is_authenticated:
		userProfile = UserProfile.objects.get(user=request.user)
		context_dict['userProfile'] = userProfile
		length = len(request.user.first_name)
		context_dict['length']= 87 - length
	return render(request, 'fashionpointapp/contact_us.html',context_dict)

def about_us(request):
	context_dict = {}
	if request.user.is_authenticated:
		userProfile = UserProfile.objects.get(user=request.user)
		context_dict['userProfile'] = userProfile
		length = len(request.user.first_name)
		context_dict['length']= 87 - length
	return render(request, 'fashionpointapp/about.html',context_dict)

def sitemap(request):
	context_dict = {}
	if request.user.is_authenticated:
		userProfile = UserProfile.objects.get(user=request.user)
		context_dict['userProfile'] = userProfile
		length = len(request.user.first_name)
		context_dict['length']= 87 - length
	return render(request, 'fashionpointapp/sitemap.html',context_dict)

def register(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			else:
				profile.picture = Image.open("/static/images/default.jpg")
			profile.save()
			registered = True
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(username=username, password=password)
			login(request, user)
			return HttpResponseRedirect(reverse('index'))
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render(request,
				'fashionpointapp/signup.html',
				{'user_form': user_form,
				'profile_form': profile_form,
				'registered': registered,
				'pos': 5})

@login_required
def PostaPost(request):
	form = PostForm()
	context_dict = {'form': form}
	if request.user.is_authenticated:
		userProfile = UserProfile.objects.get(user=request.user)
		context_dict['userProfile'] = userProfile
		length = len(request.user.first_name)
		context_dict['length']= 87 - length
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES )
		if form.is_valid():
			candidate = form.save(commit=False)
			candidate.userPofile = UserProfile.objects.get(user=request.user)
			candidate.save()
			form.save_m2m()
			return index(request)
		else:
			print(form.errors)

	context_dict['pos']=3
	return render(request, 'fashionpointapp/PostaPost.html', context_dict)

@login_required
def PollaPoll(request):
	form = PollForm()
	context_dict = {'form': form}
	if request.user.is_authenticated:
		userProfile = UserProfile.objects.get(user=request.user)
		context_dict['userProfile'] = userProfile
		length = len(request.user.first_name)
		context_dict['length']= 87 - length
	if request.method == 'POST':
		form = PollForm(request.POST, request.FILES )
		if form.is_valid():
			candidate = form.save(commit=False)
			candidate.userPofile = UserProfile.objects.get(user=request.user)
			candidate.save()
			form.save_m2m()
			return index(request)
		else:
			print(form.errors)

	context_dict['pos']=6
	return render(request, 'fashionpointapp/PollaPoll.html', context_dict)


def user_login(request):
	context_dict = {}
	context_dict['pos'] = 4
	context_dict['type'] = "";
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				context_dict['type'] = "Account is Disabled";
				return render(request, 'Fashionpointapp/login.html', context_dict)
		else:
			context_dict['type'] = "Invalid login details";
			print("Invalid login details: {0}, {1}".format(username, password))
			return render(request, 'Fashionpointapp/login.html', context_dict)
	else:
		return render(request, 'Fashionpointapp/login.html', context_dict)
@login_required
def view_profile(request):
	context_dict = {}
	user = request.user
	userProfile = UserProfile.objects.get(user=user)
	context_dict['userProfile'] = userProfile
	logged_in_user_posts = Post.objects.filter(userPofile=userProfile)	
	context_dict['posts'] =logged_in_user_posts
	context_dict['polls'] = Poll.objects.filter(userPofile=userProfile)
	return render(request, 'fashionpointapp/myaccount.html', context_dict)


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

def visitor_cookie_handler(request):
	visits = int(get_server_side_cookie(request, 'visits', '1'))
	last_visit_cookie = get_server_side_cookie(request,'last_visit',str(datetime.now()))
	last_visit_time = datetime.strptime(last_visit_cookie[:-7],'%Y-%m-%d %H:%M:%S')
	if (datetime.now() - last_visit_time).days > 0:
		visits = visits + 1
		request.session['last_visit'] = str(datetime.now())
	else:
		request.session['last_visit'] = last_visit_cookie
	request.session['visits'] = visits

def get_server_side_cookie(request, cookie, default_val=None):
	val = request.session.get(cookie)
	if not val:
		val = default_val
	return val


def startate(x):
	text=""
	for i in  range(0,x):
		text = text + "*"
	return text


@login_required	
def edit_profile(request):
    if request.method == 'POST':
        form = EditForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return  HttpResponseRedirect(reverse('view_profile'))
    else:
        form = EditForm(instance=request.user)
        args = {'form': form}
        return render(request, 'fashionpointapp/edit_profile.html', args)
def edit_pic(request):
    if request.method == 'POST':
        form = EditPic(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return  HttpResponseRedirect(reverse('view_profile'))
    else:
        form = EditForm(instance=request.user)
        args = {'form': form}
        return render(request, 'fashionpointapp/pic.html', args)

def show_post(request , post_id):
	context_dict = {}
	if request.user.is_authenticated:
		userProfile = UserProfile.objects.get(user=request.user)
		context_dict['userProfile'] = userProfile
		length = len(request.user.first_name)
		context_dict['length']= 87 - length
	context_dict['post'] = Post.objects.get(id=int(post_id))
	comments = PostComment.objects.filter(post=int(post_id))
	context_dict['Comments'] = comments
	return render(request,'Fashionpointapp/post.html',context_dict)


def show_poll(request , poll_id):
	context_dict = {}
	if request.user.is_authenticated:
		userProfile = UserProfile.objects.get(user=request.user)
		context_dict['userProfile'] = userProfile
		length = len(request.user.first_name)
		context_dict['length']= 87 - length
	context_dict['poll'] = Poll.objects.get(id=int(poll_id))
	comments = PollComment.objects.filter(poll=int(poll_id))
	context_dict['Comments'] = comments
	return render(request,'Fashionpointapp/poll.html',context_dict)




def update_avg(request , post_id ):
	if request.method == 'POST' and request.is_ajax():
		userProfile = UserProfile.objects.get(user=request.user)
		try:
			id = post_id
			value = request.POST.get('value')
			obj = Post.objects.get(id=post_id)

			rating = Rating()
			rating.userPofile = userProfile
			rating.post = obj
			rating.rating = value
			rating.save()

			ratings = len(Rating.objects.filter(post=obj))
			obj.avgRating = (obj.avgRating * (len(Rating.objects.filter(post=obj))-1) + int(value)) / len(Rating.objects.filter(post=obj))

			obj.save()
			return HttpResponse(value)
		except Post.DoesNotExist:
			return HttpResponse('did not work')
	else: return HttpResponse('did not work 2')


def makeacomment(request , post_id ):

	if request.method == 'POST' and request.is_ajax():
		userProfile = UserProfile.objects.get(user=request.user)
		try:
			id = post_id
			comment = PostComment()
			comment.comment = request.POST.get('comment')
			comment.post = Post.objects.get(id=int(post_id))
			comment.userPofile = userProfile
			comment.save()
			return HttpResponse("It did work")
		except Post.DoesNotExist:
			return HttpResponse('did not work')
	else :

		return HttpResponse('did not work')


def makeapollcomment(request, poll_id):
    if request.method == 'POST' and request.is_ajax():
        userProfile = UserProfile.objects.get(user=request.user)
        try:
            comment = PollComment()
            comment.comment = request.POST.get('comment')
            comment.poll = Poll.objects.get(id= int(poll_id))
            comment.userPofile = userProfile
            comment.save()
            return HttpResponse("It did work")
        except Post.DoesNotExist:
            return HttpResponse('did not work')
    else:
        return HttpResponse('did not work')

def update_comments(request, post_id):
	context_dict={}
	context_dict['Comments'] = PostComment.objects.filter(post=int(post_id))
	return render(request, 'Fashionpointapp/newComments.html', context_dict)



def update_pollcomments(request , poll_id):
    context_dict={}
    context_dict['Comments'] = PollComment.objects.filter(poll=int(poll_id))
    return render(request, 'Fashionpointapp/newpollComments.html', context_dict)


def click(request, poll_id):
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = Poll.objects.get(id=int(poll_id))
            if (int(request.POST.get('picture') )== 1 ):
                obj.picture1Clicks=obj.picture1Clicks+1
                obj.save()
                return HttpResponse("worked")
            else :
                obj.picture2Clicks=obj.picture2Clicks+1
                obj.save()
                return HttpResponse("worked")

        except Poll.DoesNotExist:
            return HttpResponse('did not work')

def account_page(request):


	return render(request, 'fashionpointapp/myaccount.html', {'posts': logged_in_user_posts})



