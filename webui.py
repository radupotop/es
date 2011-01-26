#!/usr/bin/python2

import web
import db
import core

urls = ('/', 'index')
app = web.application(urls, globals())

class index:
    def GET(self):
        tpl = web.template.render('tpl/')
        return tpl.form('world', 'page')



















if __name__ == '__main__':
    app.run()
else:
    application = app.wsgifunc()
