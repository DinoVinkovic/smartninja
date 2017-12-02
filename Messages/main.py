#!/usr/bin/env python
import os
import jinja2
import webapp2
import datetime
from models import Message


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        params = {"date" : datetime.datetime.now().strftime("%d/%m/%Y"), "time" : datetime.datetime.now().strftime("%H:%M")}
        return self.render_template("home.html", params=params)

class AboutHandler(BaseHandler):
    def get(self):
        return self.render_template("about.html")

class ProjectsHandler(BaseHandler):
    def get(self):
        return self.render_template("projects.html")

class BlogHandler(BaseHandler):
    def get(self):
        return self.render_template("blog.html")

class ResultHandler(BaseHandler):
    def post(self):
        result = self.request.get("some_text")

        msg = Message(message_text = result)
        msg.put()

        return self.write(result)

class MessageListHandler(BaseHandler):
    def get(self):
        messages = Message.query(Message.deleted == False).fetch()
        params = {"messages" : messages}
        return self.render_template("message_list.html", params=params)

class MessageDetailsHandler(BaseHandler):
    def get(self, message_id):
        message = Message.get_by_id(int(message_id))
        params = {"message" : message}
        return self.render_template("message_details.html", params=params)

class EditMessageHandler(BaseHandler):
    def get(self, message_id):
        message = Message.get_by_id(int(message_id))
        params = {"message": message}
        return self.render_template("message_edit.html", params=params)

    def post(self, message_id):
        new_text = self.request.get("some_text")
        message = Message.get_by_id(int(message_id))
        message.message_text = new_text
        message.put()
        return self.redirect_to("msg-list")

class DeleteMessageHandler(BaseHandler):
    def get(self, message_id):
        message = Message.get_by_id(int(message_id))
        params = {"message" : message}
        return self.render_template("message_delete.html", params=params)

    def post(self, message_id):
        message = Message.get_by_id(int(message_id))
        message.deleted = True
        message.put()
        return self.redirect_to("msg-list")

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/about', AboutHandler),
    webapp2.Route('/projects', ProjectsHandler),
    webapp2.Route('/blog', BlogHandler),
    webapp2.Route('/result', ResultHandler),
    webapp2.Route('/message_list', MessageListHandler, name="msg-list"),
    webapp2.Route('/message/<message_id:\d+>', MessageDetailsHandler),
    webapp2.Route('/message/<message_id:\d+>/edit', EditMessageHandler),
    webapp2.Route('/message/<message_id:\d+>/delete', DeleteMessageHandler)
], debug=True)
