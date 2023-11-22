from initdata import db
import pickle
#? using pickle module to write db in bytes
dbfile = open('people-pickle','wb')
pickle.dump(db,dbfile)
dbfile.close()

