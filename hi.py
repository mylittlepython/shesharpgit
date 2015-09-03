#http://webpy.org/
import web

render= web.template.render('templates/')

#regex explanation: parenthesis -> create a capture group
#and indicate precedence
#dot star -> match 0 or more characters
urls = ('/(.*)', 'index')

#request the webpage context
class index:
    def GET(self, name):
        return render.index(name)

#let the web library know (in this case web.py
#how to serve web pages according to the defined urls
#start the webapp
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

#for this simple hello_name app
#python hi.py
#localhost:8080/name
