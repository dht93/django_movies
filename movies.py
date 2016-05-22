import os
import sqlite3
# d='/media/dht93/Seagate Backup Plus Drive/Movies'
# f_name='lst.txt'
# path = '/home/dht93'
# full_path=os.path.join(path, f_name)
# f=open(full_path, 'a')
# for root, dirs, files in os.walk(d):
# 	for name in dirs:
# 		if not name.startswith('.'):
# 			print name
# 			f.write(name+'\n')
# 	break
# f.close()

#------------------------------------

# conn=sqlite3.connect('movies.sqlite')
# cur = conn.cursor()
# cur.execute('CREATE TABLE IF NOT EXISTS movies (name TEXT)')
# conn.commit()
# l=[]
# f=open('/home/dht93/lst.txt')
# for line in f:
# 	# print line.strip()
# 	l.append(line.strip())
# print len(l)
# l=list(set(l))
# l.sort()
# for el in l:
# 	if l.count(el)==1:
# 	cur.execute('INSERT INTO movies VALUES (?)',(el,))
# conn.commit()
# cur.close()
# conn.close()
# f.close()
