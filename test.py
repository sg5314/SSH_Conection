# -*- coding: utf-8 -*-

from sshtunnel import SSHTunnelForwarder
import mysql.connector

from sshtunnel import SSHTunnelForwarder
import mysql.connector
import pymysql.cursors

port_num = 22
with SSHTunnelForwarder(
    ('', port_num),
    ssh_username='username',
    ssh_password='password',
    ssh_pkey='',
    remote_bind_address=('', 3306)
) as server:
    print(server.local_bind_port)
    conn = pymysql.connect(
            host = 'localhost',
            port = server.local_bind_port,
            user = '',
            password = '',
            database = '',
            charset = 'utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
    
    #server='yourserver.database.windows.net', user='yourusername@yourserver', password='yourpassword', database='AdventureWorks'

    cur = conn.cursor()

    print('クエリを実行')
    # クエリを記述
    cur.execute("""
        SELECT * FROM user
    """)

    for row in cur:
        print(row)

    cur.close()
    conn.close()
