import web

db = web.database(dbn='mysql', db='es', user='root', pw='')

print db.select('symptoms')
