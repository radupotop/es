#!/usr/bin/python2

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
        symp = db.get_symptoms()
        es_form = DynamicForm()
        for k,v in symp.items():
            es_form.add_input(web.form.Checkbox(v, value=k))
        return es_form
        
    def POST(self):
        i = web.input()
        symptoms = i.values()
        diseases = db.get_diseases_init_cf()
        
        for symp in symptoms:
            rules = db.get_rules(symp)
            for k,v in rules.items():
                diseases[k] += v
        
        max_cf = max(diseases.values())
        for k,v in diseases.items():
            if v == max_cf:
                winner_k = k
                break
        
        winner_name = db.get_diseases()[winner_k]
        
        tpl = web.template.render('tpl/')
        return tpl.result(winner_name, max_cf, diseases)



class DynamicForm(web.form.Form):
    def add_input(self, new_input):
        list_inputs = list(self.inputs)
        list_inputs.append(new_input)
        self.inputs = tuple(list_inputs)


if __name__ == '__main__':
    app.run()
else:
    application = app.wsgifunc()
