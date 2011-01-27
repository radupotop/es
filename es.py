#!/usr/bin/python2

import web
import db

urls = ('/', 'index')
app = web.application(urls, globals())

class index:
    def GET(self):
        tpl = web.template.render('tpl/')
        es_form = self.form()
        return tpl.form(es_form)

    def form(self):
        symp = db.get_symptoms()
        es_form = DynamicForm()
        for row in symp:
            es_form.add_input(web.form.Checkbox(row.name.encode('utf-8'), value=row.id_symptom))
        return es_form
        
    def POST(self):
        i = web.input()
        symptoms = i.values()
        diseases = db.get_diseases()
        
        for symp in symptoms:
            rules = db.get_rules(symp)
            for rule in rules:
                diseases[rule.id_disease] += rule.cf
        
        max_cf = max(diseases.values())
        for k,v in diseases.items():
            if v == max_cf:
                winner = k
                break
        
        winner_name = db.get_disease_name(winner)
        
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
