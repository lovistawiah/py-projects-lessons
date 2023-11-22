import shelve
from initdata import bob, sue
db = shelve.open('people-shelve')
db['sue'] = sue
db['bob'] = bob
db.close()
