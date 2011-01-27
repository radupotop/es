#!/usr/bin/python2

import web
import db
import core

urls = ('/', 'index')
app = web.application(urls, globals())

class index:
    def GET(self):
        tpl = web.template.render('tpl/')
        es_form = self.form()
        return tpl.form(es_form)

    def form(self):
        symp = db.get_symptoms_list()
        es_form = DynamicForm()
        for row in symp:
            es_form.add_input(web.form.Checkbox(web.utils.utf8(row.name), value=row.id_symptom))
        return es_form



class DynamicForm(web.form.Form):
    def add_input(self, new_input):
        list_inputs = list(self.inputs)
        list_inputs.append(new_input)
        self.inputs = tuple(list_inputs)


if __name__ == '__main__':
    app.run()
else:
    application = app.wsgifunc()
