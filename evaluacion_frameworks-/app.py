import web

urls = (
    '/', 'mvc.controllers.login.Login',
)

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'))

if __name__ == "__main__":
    web.config.debug = True
    app.run()