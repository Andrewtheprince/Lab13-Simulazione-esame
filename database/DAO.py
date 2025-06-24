from database.DB_connect import DBConnect
from model.driver import Driver


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

    @staticmethod
    def getNodi(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)
        result = []
        query = """ select distinctrow d.*
                    from drivers d, results r , races r2 
                    where r2.`year` = %s and r2.raceId =r.raceId and r.`position` is not null and r.driverId = d.driverId"""
        cursor.execute(query, (anno,))
        for row in cursor:
            result.append(Driver(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """ select r1.driverId as driver1, r3.driverId as driver2, count(*) as tot
                    from results r1 , races r2, results r3
                    where r2.`year` = %s and r1.raceId = r2.raceId and r3.raceId =r2.raceId and r1.driverId != r3.driverId 
                    and r1.`position` < r3.`position`
                    group by r1.driverId, r3.driverId """
        cursor.execute(query, (anno,))
        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result