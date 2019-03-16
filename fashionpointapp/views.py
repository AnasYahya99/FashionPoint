from django.shortcuts import render
from django.http import HttpResponse
from fashionpointapp.models import Category , Post ,PostComment ,Poll ,PollComment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from fashionpointapp.forms import PostForm
from fashionpointapp.models import UserProfile,Post
from datetime import datetime


from fashionpointapp.forms import UserForm,UserProfileForm,PollForm


from django.http import JsonResponse

from django.shortcuts import get_object_or_404

from fashionpointapp.forms import UserForm,UserProfileForm,PollForm,EditForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import update_session_auth_hash
ind = 0

def index(request):
	context_dict = {}
	post = Post.objects.all()
	state1 = 0
	state2 = 0
	if (ind == 0):
		state1 = 1
	if (ind * 3 + 3 >= len(post)):
		state2 = 1
	context_dict['state1'] = state1
	context_dict['state2'] = state2
	context_dict['post1'] = post[ind*3]
	context_dict['post2'] = post[ind*3+1]
	context_dict['post3'] = post[ind*3+2]
	context_dict['arp1'] = int(round(post[ind*3].avgRating*2))
	context_dict['arp2'] = int(round(post[ind*3+1].avgRating*2))
	context_dict['arp3'] = int(round(post[ind*3+2].avgRating*2))
	if request.user.is_authenticated:
		userProfile = UserProfile.objects.get(user=request.user)
		context_dict['userProfile'] = userProfile
		length = len(request.user.first_name)
		context_dict['length']= 87 - length
	context_dict['pos']=1
	return render(request, 'fashionpointapp/index.html',context_dict)
def indexReset(request):
	global ind
	ind = 0
	return index(request)
def indexNext(request):
	post = Post.objects.all()
	global ind
	if (ind * 3 + 3 < len(post)):
		ind = ind + 1
	return index(request)
def indexPrev(request):
	global ind
	if (ind != 0):
		ind = ind - 1
	return index(request)
def categories(request):
	context_dict = {}
	if request.user.is_authenticated:
		userProfile = UserProfile.objects.get(user=request.user)
		context_dict['userProfile'] = userProfile
		length = len(request.user.first_name)
		context_dict['length']= 87 - length
	context_dict['pos']=2
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
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}

    return render(request, 'fashionpointapp/myaccount.html', args)


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
@login_required	
def edit_profile(request):
    if request.method == 'POST':
        form = EditForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('fashionpointapp:view_profile'))
    else:
        form = EditForm(instance=request.user)
        args = {'form': form}
        return render(request, 'fashionpointapp/edit_profile.html', args)



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
		try:
			id = post_id
			value = request.POST.get('value')
			obj = Post.objects.get(id=post_id)
			obj.avgRating = value
			obj.save()
			return HttpResponse(value)
		except Post.DoesNotExist:
			return HttpResponse('did not work')


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
    return render(request, 'Fashionpointapp/bewpollComments.html', context_dict)


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









