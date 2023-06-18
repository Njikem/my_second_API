import mariadb
import dbcreds


def run_procedure(sql, args):
    try:
        results = None
        conn = mariadb.connect(**dbcreds.conn_params)
        cursor = conn.cursor()
        cursor.execute(sql, args)
        results = cursor.fetchall()
    except mariadb.programmingError as error:
        print("There is an issue with the bd code:", error)
    except mariadb.operationalError:
        print("There is an issue connect to the db:", error)
    except Exception as error:
        print("There was an unknown error:", error)
    finally:
        if(cursor !=None):
            cursor.close()
        if(conn !=None):
            conn.close()
        return results                    