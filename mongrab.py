import pymongo
import sys
import json

def mongo_db_connect(clientIP):
    
    try:
        conn=pymongo.MongoClient(clientIP,27017, maxPoolSize=50, waitQueueTimeoutMs=100)
	print conn
        conn.server_info()
        print "Connected!!!!"
        d = dict((db, [collection for collection in conn[db].collection_names()])
        for db in conn.database_names())
        print json.dumps((d), indent=6)
        conn.database_names()	

    except pymongo.errors.ConnectionFailure, e:
        print "Could not connect to MongoDB: %s" % e 

def main(argv):

    ipfile = sys.argv[1]

    # Open the file
    with open(ipfile, 'r') as infile:
        data = infile.read()  

    # Read Lines
    my_list = data.splitlines()

    # Scans
    for line in my_list:
        print 'Target: '
        print line
        print '----------------------------------------'
	
        try:
            mongo_db_connect(line)
        except:
            print 'Connexion Terminated'

        print '----------------------------------------'


if __name__ == "__main__":
   main(sys.argv[1:])
