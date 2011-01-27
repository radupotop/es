import web

db = web.database(dbn='mysql', db='es', user='root')

def join():
    results = db.query(
        'select diseases.name as dis, symptoms.name as symp from rules \
        join diseases on rules.id_disease = diseases.id_disease \
        join symptoms on rules.id_symptom = symptoms.id_symptom'
    )
    return results.list()
    
#~ x = join()
#~ 
#~ for row in x:
    #~ print row


def get_symptoms():
    result = db.select('symptoms')
    return result.list()

def get_rules(symp):
    result = db.select('rules', where='id_symptom=%s' % symp)
    return result.list()
