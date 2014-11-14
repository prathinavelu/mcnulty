import pymysql

db = pymysql.connect(host="104.131.117.224",  #your cloud ip
                     user='root',
                     passwd='hd_adepr',
                     db='mcnulty_hd_adepr')
                     
                     
cursor = db.cursor()
cursor.execute('SHOW TABLES')