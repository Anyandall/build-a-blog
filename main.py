#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import string

from google.appengine.ext import db



form = """
<!DOCTYPE HTML>

<html>

<head>

	<title> The NOOB Blog! </title>
	<div class="accepted">%(accepted)s</div>
</head>

<body>

	<h2> The NOOB Blog! </h2>

	<form method="post">

		<label>
			<div> Blog Title </div>
			<input type="text" name="blog_title" value="%(blog_title)s">
		</label>

		<label>
			<div>Blog Body</div>
			<textarea name="blog_body">%(blog_body)s</textarea>
		</label>

		<div class="error" style="color: red">%(error)s</div>

		<input type="submit"/>

	</form>

<hr>

	<div><h3>%(previous)s</h3></div>

</body>

</html>

"""

def user_has_blog_title(blog_title):
	if len(str(blog_title)) != 0:
		return True
	return False

def user_has_blog_body(blog_body):
	if len(str(blog_body)) != 0:
		return True
	return False


class Submission(db.Model):
	blog_title = db.StringProperty(required = True)
	blog_body = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)


class MainHandler(webapp2.RequestHandler):

	def write_new_form(self, accepted="", blog_title="", blog_body="", error=""):
		pass

	def write_form(self, accepted="", blog_title="", blog_body="", error="", previous=""):
	#	all_posts = db.GqlQuery("SELECT * FROM Submission ORDER BY created DESC")
	#	samus_post = db.GqlQuery("SELECT * FROM Submission WHERE sub_title = 'samus'")

		self.response.write(form % {
									"accepted" : accepted,
									"blog_title" : blog_title,
									"blog_body" : blog_body,
									"error" : error,
									"previous" : "previous"
									})

#	def write_home(self):
#		accepted = "Thanks for submitting! Your post can be viewed below the form."

#		self.response.write(accepted)
#		self.write_form("", "", "", all_posts)



	def get(self):
		self.redirect("/newpost")
	#	self.write_form()
#		self.query = Submission.all()
	#	for self.submission in self.query:
		#	self.response.write("<p>%s</p><p>%s</p>" % (self.submission.blog_title, self.submission.blog_body))


	def post(self):
		blog_title = self.request.get("blog_title")
		blog_body = self.request.get("blog_body")

		has_title = user_has_blog_title(blog_title)
		has_body = user_user_has_blog_body(blog_body)

		accepted = "Thanks for submitting! Your post can be viewed below the form."
	#	all_posts = db.GqlQuery("SELECT * FROM Submission")

		if has_title and has_body:
			#self.response.write("Thanks for submitting! Your comment has been posted below.")
			submission = Submission(blog_title = blog_title, blog_body = blog_body)
			submission.put()

			#self.write_form(accepted)
			self.redirect('/')
			self.query = Submission.all()
			for self.submission in self.query:
				self.response.write("<p>%s</p><p>%s</p>" % (self.submission.blog_title, self.submission.blog_body))


			#self.response.write(all_posts)
			#self.redirect("/")

			#self.response.write(submission)

		elif has_title and not has_body:
			self.write_form("", blog_title, "", "Submission has a title but no body!")
		elif has_body and not has_title:
			self.write_form("", "", blog_body, "Submission has a body but no title!")
		else:
			self.write_form("", "", "", "Submission requires a title and body!")

class NewPostHandler(MainHandler):

	def write_newpost(self, accepted="", blog_title="", blog_body="", error="", previous=""):
		self.response.write(form % {
									"accepted" : accepted,
									"blog_title" : blog_title,
									"blog_body" : blog_body,
									"error" : error,
									"previous" : previous
									})

	def get(self):
		previous = "<h3> Previous Posts </h3>"
		self.write_newpost()

	def post(self):
		blog_title = self.request.get("blog_title")
		blog_body = self.request.get("blog_body")
		has_title = user_has_blog_title(blog_title)
		has_body = user_has_blog_body(blog_body)

		accepted = "Thanks for submitting! Your post can be viewed below the form."
		#	all_posts = db.GqlQuery("SELECT * FROM Submission")

		if has_title and has_body:
				#self.response.write("Thanks for submitting! Your comment has been posted below.")
			submission = Submission(blog_title = blog_title, blog_body = blog_body)
			submission.put()

				#self.write_form(accepted)
				#self.redirect('/')
				#self.query = Submission.all()
				#for self.submission in self.query:
				#	self.response.write("<p>%s</p><p>%s</p>" % (self.submission.blog_title, self.submission.blog_body))


			self.redirect("/blog")
		elif has_title and not has_body:
			self.write_newpost("", blog_title, "", "Submission has a title but no body!")
		elif has_body and not has_title:
			self.write_newpost("", "", blog_body, "Submission has a body but no title!")
		else:
			self.write_newpost("", "", "", "Submission requires a title and body!")

class BlogHandler(NewPostHandler):

	def write_blog(self, accepted="", blog_title="", blog_body="", error="", previous=""):
#		submissions = str(db.GqlQuery("SELECT * FROM Submission "
#								  "ORDER BY created DESC "))
#		accepted = "Thanks for submitting! Your post can be viewed below the form."

		self.response.write(form % {
									"accepted" : accepted,
									"blog_title" : blog_title,
									"blog_body" : blog_body,
									"error" : error,
									"previous" : previous
									})

	def get(self):
		accepted = "Thanks for submitting! Please refresh the page to view your submission below."

		blog_title = self.request.get("blog_title")
		blog_body = self.request.get("blog_body")
		#has_title = user_has_blog_title(blog_title)
		#has_body = user_has_blog_body(blog_body)


		#if has_title and has_body:
		self.response.write(accepted + "<hr><br>")
			#self.write_blog()
		#else:
			#self.write_blog()

#		self.write_blog()
	#	all_posts = Submission.gql("ORDER BY created DESC LIMIT 5")
		all_posts = db.GqlQuery("SELECT * FROM Submission ORDER BY created DESC LIMIT 5")
		for submission in all_posts:
			self.response.write("<a href='/blog?post_id=%s'>%s</a><p>%s</p>" % (submission.key().id(), submission.blog_title, submission.blog_body))

class ViewPostHandler(webapp2.RequestHandler):
	def get(self, id):
		post_id = self.request.get(submission.key().id())
		self.response.write(post_id)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
	('/blog', BlogHandler),
	('/newpost', NewPostHandler),
	webapp2.Route('/blog/<id>:\d+>', ViewPostHandler)
], debug=True)
