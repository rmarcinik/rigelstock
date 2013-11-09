from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
import os

import prog

class MainPage(webapp.RequestHandler):
    generator = prog.prog_gen()
    program_output = generator.next()
    
    def get(self):
        cmd = self.request.get('content', None)
        if cmd != None:
            self.program_output = self.generator.send(cmd)
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, {'text':self.program_output}))

application = webapp.WSGIApplication([('/', MainPage)], debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()