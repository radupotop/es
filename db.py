import web

db = web.database(dbn='mysql', db='es', user='root')

def select(table):
    result = db.select(table)
    return result.list()


#~ symptoms = select('symptoms')
#~ 
#~ 
#~ for row in symptoms:
    #~ print row.name


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
