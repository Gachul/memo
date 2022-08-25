# import pymysql as conn_db

# def runsql(user_id: str, user_pass: str) -> tuple:
    
#     my_db = conn_db.connect(host = "localhost", port = 3306, user = "manager01", password = "password01", db = 'user_info')
#     cur = my_db.cursor()
    
#     sql = f'select count(*) from jo_user where uid = {user_id} and upw = {user_pass}'
    
#     cur.execute(sql)
    
#     content = cur.fetchall()[0]
    
#     return content[0]