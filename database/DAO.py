from database.DB_connect import DBConnect


class DAO:

    @staticmethod
    def getAllAnni():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)
        result = []
        query = """ SELECT s.year
                    FROM seasons s
                    group by s.year
                    order by s.year asc"""
        cursor.execute(query)
        for row in cursor:
            result.append(row["year"])
        cursor.close()
        conn.close()
        return result
