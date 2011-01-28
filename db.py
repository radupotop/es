import web

db = web.database(dbn='mysql', db='es', user='root')



def get_symptoms():
    result = db.select('symptoms').list()
    return result

def get_rules(symp):
    result = db.select('rules', where='id_symptom=%s' % symp).list()
    return result

def get_diseases_cf():
    result = db.select('diseases').list()
    diseases = dict()
    for dis in result:
        diseases[dis.id_disease] = 0
    return diseases

def get_disease_name(id_disease):
    result = db.select('diseases', where='id_disease=%s' % id_disease).list()
    return result[0].name

def get_diseases_name_list():
    result = db.select('diseases').list()
    diseases = list()
    for dis in result:
        diseases.append(dis.name)
    return diseases
