from mk_db_file import loadDbase,storeDbase

db =loadDbase()
db['tom']['job'] ='Software Developer'
db['tom']['pay'] =9000
db['tom']['last name'] ='Tawiah'
storeDbase(db)

for keys,values in db.items():
   for key,value in values.items():
    if key !='last name':
        db[keys]['last name'] ='Skido'

print(db)