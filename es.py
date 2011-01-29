#!/usr/bin/python2

import os, sys
abspath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(abspath)

import web
import db

urls = ('/', 'index')
app = web.application(urls, globals())

class index:
    def GET(self):
        tpl = web.template.render('tpl/')
        es_form = self.form()
        diseases = db.get_diseases().values()
        return tpl.form(es_form, diseases)

    def form(self):
        symptoms = db.get_symptoms()
        es_form = DynamicForm()
        for k,v in symptoms.items():
            es_form.add_input(web.form.Checkbox(v, value=k))
        return es_form
        
    def POST(self):
        symptoms_iv = web.input().values()
        diseases_cf = db.get_diseases_init_cf()

        # Determine CF for each disease
        for symp in symptoms_iv:
            rules = db.get_rules(symp)
            for k,v in rules.items():
                diseases_cf[k] += v

        # Determine winning disease
        max_cf = max(diseases_cf.values())
        for k,v in diseases_cf.items():
            if v == max_cf:
                winner_k = k
                break
        winner_name = db.get_diseases()[winner_k]
        
        symptoms_ik = web.input().keys()
        
        tpl = web.template.render('tpl/')
        return tpl.result(winner_name, max_cf, diseases_cf, symptoms_ik)


class DynamicForm(web.form.Form):
    def add_input(self, new_input):
        list_inputs = list(self.inputs)
        list_inputs.append(new_input)
        self.inputs = tuple(list_inputs)


if __name__ == '__main__':
    app.run()
else:
    application = app.wsgifunc()
