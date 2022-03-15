#import mysql.connector
import yaml, os
'''
db_name = [
    ['inspiral_1000',1],
    ['inspiral_100',2],
    ['inspiral_50',3],
    ['inspiral_30',4],
    ['montage_1000',10],
    ['montage_100',11],
    ['montage_50',12],
    ['montage_25',13],
    ['sipht_1000',20],
    ['sipht_100',21],
    ['sipht_60',22],
    ['sipht_30',23],
    ['epigenomics_997',30],
    ['epigenomics_100',31],
    ['epigenomics_46',32],
    ['epigenomics_24',33],
    ['cybershake_1000',40],
    ['cybershake_100',41],
    ['cybershake_50',42],
    ['cybershake_30',43],
]
'''
db_name =[
    ['cybershake_1000',40],
]
costs = [
1.575,
1.8,
2.7,
3.6,
4.5,
6.075,
6.975,
7.65,
9,
10.35,
11.7,
13.5,
14.4,
15.3,
16.71,
18,
18.93,
19.83,
21.405,
23.01,



]

def query_cost():
    '''
    mydb = mysql.connector.connect(
            host="172.16.137.120",
            user="root",
            passwd="123456",
            database=database
          )
    mycursor = mydb.cursor()
    '''
    for item in db_name:
        #mycursor.execute("SELECT cost FROM "+ item[0])
        #myresult = mycursor.fetchall()
        for x in costs:

            with open("./resources/config/config.yml", 'r') as stream:
                try:
                    myyaml = yaml.load(stream)
                except yaml.YAMLError as exc:
                    print(exc)
                #        for iteration in iteration_number:
                myyaml['global']['workflow_id'] = item[1]
                myyaml['global']['workflow_name'] = item[0]
                myyaml['global']['budget'] = x

                # myyaml['pacsa_algorithm']['iteration_number'] = iteration
                # line = "workflow_id:" + workflow + ", start_temprature:" + temprature + ", iteration_number:"+ iteration
                with open('./resources/config/config.yml', 'w') as outfile:
                    yaml.dump(myyaml, outfile, default_flow_style=False)
                os.system('java -jar optframework.jar')
                print(item)
                print(item)
                print(item)
                print(item)
                print(item)
                print(item)
                print(item)
                print(item)
                print(item)
                print(item)
                print(item)
                print(item)
                print(item)
                print(item)
                print(item)
                print(item)
                print(item)
                print(item)
                print(item)
                print(item)
                print(item)

query_cost()

