import sqlite3 as lite
import sys

# python2.7 Ref: http://zetcode.com/db/sqlitepythontutorial/

def read_tb(db_file, tb_name):
    con = None

    try:
        #con = lite.connect('xxProvider.db')
        con = lite.connect(db_file)
        cur = con.cursor()
        cur.execute('SELECT * FROM %s' % tb_name)

        # print(cur.description)

        # get table column names.
        col_name_list = [tuple[0] for tuple in cur.description]
        print(col_name_list)
        
        rows = cur.fetchall()
        for row in rows:
            print(row)

    except lite.Error as e:
        print('Error %s:' % e.args[0])
        sys.exit(1)
    finally:
        if con:
            con.close()

def update_tb(db_file, tb_name):
    con = None

    try:
        #con = lite.connect('xxProvider.db')
        con = lite.connect(db_file)
        cur = con.cursor()
        
        key1 = 18
        key2 = 20
        # select ref : http://database.51cto.com/art/201107/277317.htm

        prim_column_name = '_id'
        
        cur.execute(' SELECT * from %s WHERE %s IN (%d, %d)' % (tb_name, prim_column_name, key1, key2))
        res = cur.fetchall()
        print(res)
        if len(res) == 0:
            cur.execute("INSERT INTO %s VALUES(%d, 'renyafei', '12')" % (tb_name, key1))
            cur.execute("INSERT INTO %s VALUES(%d, 'renyafei', '12')" % (tb_name, key2))
            print('insert to table')
        
        con.commit()
        
        # SELECT * FROM Cars WHERE Cost BETWEEN 20000 AND 55000;
        cur.execute( 'SELECT * FROM %s WHERE %s BETWEEN 1 AND 15' % (tb_name, prim_column_name))
        res = cur.fetchall()
        print('------------------')
        print(res)
        print('------------------')
                            
    except lite.Error as e:
        print('Error %s:' % e.args[0])
        sys.exit(1)
    finally:
        if con:
            con.close()
    
if __name__ == "__main__":
    db_file = 'xxProvider.db'
    tb_name = 'users'
    
    read_tb(db_file, tb_name)
    update_tb(db_file, tb_name)
    read_tb(db_file, tb_name)
    
