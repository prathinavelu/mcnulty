import pymysql
import scp
import glob
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())
ssh.connect("104.131.123.231", username='root', password='a9124032')

client = scp.SCPClient(ssh.get_transport())
client.put('bysleepdata.csv', '~/WebApp')
client.put('index.html', '~/WebApp')
client.put('d3.legend.js', '~/WebApp')
#client.get('/tmp/main_attributes.csv','dumb_sample.csv')
import sys
sys.exit()

#my_file_list = glob.glob('/Users/Praveen/Metis/Projects/heart-disease-data/*.csv')

# for name in ['switzerland','long-beach-va','hungarian']:
#     switzerland = open(name+'.data').read().split('name')
#     switzerlanddata = []
#     for i in switzerland[:-1]:
#         s = ' '.join(i.split('\n'))
#         switzerlanddata.append(s.strip())
#     s = open(name+'.csv', 'w')   
#     for item in switzerlanddata:
#         s.write("%s\n" % item)


# db = pymysql.connect(host="104.131.117.224",  #your cloud ip 
#                      user='root',
#                      passwd='hd_adepr',
#                      db='mcnulty_hd_adepr')
                     
db = pymysql.connect(host="104.131.123.231",  #your cloud ip 
                     user='root',
                     passwd='a9124032',
                     db='heart_disease')


cursor = db.cursor()


# Copy file over
client = scp.Client(host='mcnulty_praveen', user='praveen', password='pwd')


# for file in my_file_list:
#     with closing(Write(ssh.get_transport(), '.')) as scp:
#         scp.send_file(file, True)
#     #client.transfer(file, '~/heart_disease/data/')

for name in ['switzerland','long-beach-va','hungarian']:
    csvfile = name +'.csv'
    sql = "LOAD DATA INFILE '"+csvfile+"' INTO TABLE all_data FIELDS TERMINATED BY ' '"

    cursor.execute(sql)
    
cursor.close()
db.close()