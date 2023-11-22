import pickle
#open the byte file using rb mode
dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)
for key, value in db.items():
    print(key, '=>', value)
dbfile.close()

#updating the object
db['tom']['name'] = 'Lovis Tawiah'
db['tom']['job'] = 'Software Engineer'

#open file to write in byte mode
dbfile = open('people-pickle', 'wb')
#dump() accept two arguments the object and the file to write to
db = pickle.dump(db, dbfile)
dbfile.close()
print(db)
