import web

db = web.database(dbn='mysql', db='es', user='root')



def get_symptoms():
    result = db.select('symptoms').list()
    return mk_dict('id_symptom', 'name', result)

def get_diseases():
    result = db.select('diseases').list()
    return mk_dict('id_disease', 'name', result)

def get_rules(symp):
    result = db.select('rules', where='id_symptom=%s' % symp).list()
    rules = dict()
    for rule in result:
        rules[rule.id_disease] = rule.cf
    return rules

def get_diseases_init_cf():
    result = db.select('diseases').list()
    diseases = dict()
    for dis in result:
        diseases[dis.id_disease] = 0
    return diseases

def mk_dict(k, v, result):
    """Make dict() from db result"""
    d = dict()
    for row in result:
        d[row[k]] = row[v].encode('utf-8')
    return d
