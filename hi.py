import web

urls = ('/(.*)/', 'redirect',
        "/.*", "hi")

app = web.application(urls, globals())

class redirect:
    def GET(self, path):
        web.seeother('/' + path)

class hi:
    def GET(self):
        return 'Hi all'

if __name__ == "__main__":
    app.run()
