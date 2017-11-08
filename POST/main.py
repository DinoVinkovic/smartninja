#!/usr/bin/env python
import os
import jinja2
import webapp2


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
        return self.render_template("hello.html")

class GameHandler(BaseHandler):
    def get(self):
        return self.render_template("game.html")

    def post(self):
        secret_number = 37
        user_guess = int(self.request.get("user_guess"))

        if user_guess == secret_number:
            result = "Correct!"
        elif user_guess > secret_number:
            result = "Nope. Try lower."
        elif user_guess < secret_number:
            result = "Nope. Try higher."

        params = {"result" : result, "user_guess" : user_guess}
        return self.render_template("game-result.html", params=params)

class ConverterHandler(BaseHandler):
    def get(self):
        return self.render_template("converter.html")

    def post(self):
        user_input = float(self.request.get("user_input"))
        selected_unit = self.request.get("unit")

        if selected_unit == "mi":
            result = user_input * 1.61
        elif selected_unit == "km":
            result = user_input * 0.62

        params = {"result" : result, "user_input" : user_input, "selected_unit" : selected_unit}

        return self.render_template("converter-result.html", params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/game', GameHandler),
    webapp2.Route('/converter', ConverterHandler)
], debug=True)
