from django.test import TestCase
from .models import UserProfile, Post, Poll, PostComment, PollComment, Rating, Vote
from datetime import date
from datetime import datetime

# Create your tests here.
class UserProfileModelTests(TestCase):

	def test_userprofile_has_profile_picture(self):
		for u in UserProfile.objects.all():
			self.assertIsNotNone(u.picture)

	def test_userprofile_dob_makes_sense(self):
		for u in UserProfile.objects.all():
			self.assertLess(u.dateOfBirth, date.today())

class PostTest(TestCase):
	def test_there_is_photo(self):
		for p in Post.objects.all():
			self.assertIsNotNone(p.photo)

class PollTest(TestCase):
	def test_there_is_photo(self):
		for p in Poll.objects.all():
			self.assertIsNotNone(p.picture1)
			self.assertIsNotNone(p.picture2)


class PostCommentTests(TestCase):
	def test_user_in_comment(self):
		for c in PostComment.objects.all():
			self.assertIsNotNone(c.userPofile)

	def test_post_in_comment(self):
		for c in PostComment.objects.all():
			self.assertIsNotNone(c.post)

	def comment(self):
		for c in PostComment.objects.all():
			self.assertIsNotNone(c.comment)


class PollCommentTests(TestCase):
	def test_user_in_comment(self):
		for c in PollComment.objects.all():
			self.assertIsNotNone(c.userPofile)

	def test_post_in_comment(self):
		for c in PollComment.objects.all():
			self.assertIsNotNone(c.post)

	def test_comment(self):
		for c in PollComment.objects.all():
			self.assertIsNotNone(c.comment)


class RatingTests(TestCase):
	def test_user_in_rating(self):
		for r in Rating.objects.all():
			self.assertIsNotNone(r.userPofile)

	def test_post_in_rating(self):
		for r in Rating.objects.all():
			self.assertIsNotNone(r.post)

	def test_rating(self):
		for r in Rating.objects.all():
			self.assertIsNotNone(r.rating)


class VoteTests(TestCase):
	def test_user_in_rating(self):
		for v in Vote.objects.all():
			self.assertIsNotNone(v.userPofile)

	def test_poll_in_vote(self):
		for v in Vote.objects.all():
			self.assertIsNotNone(v.post)

	def test_vote(self):
		for v in Vote.objects.all():
			self.assertIsNotNone(v.rating)

