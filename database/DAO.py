from database.DB_connect import DBConnect


class DAO():

    @staticmethod
    def get_id_map_countires(anno):
        from model.country import Country
        conn = DBConnect.get_connection()
        result = {}
        cursor = conn.cursor(dictionary=True)
        query = ("SELECT co.StateAbb, co.CCode, co.StateNme "
                 "from contiguity c, country co "
                 "where c.`year` <= %s and c.state1no = co.CCode "
                 "group by c.state1no "
                 "ORDER BY StateAbb")
        cursor.execute(query, (anno,))
        for row in cursor:
            result[row['CCode']] = Country(**row)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_tuple(anno):
       conn = DBConnect.get_connection()
       result = []
       cursor = conn.cursor(dictionary=True)
       query = ("select  c.state1no as stato1, c.state2no as stato2 "
                "from contiguity c "
                "where c.`year`<=%s and c.conttype=1")
       cursor.execute(query, (anno,))
       for row in cursor:
           tupla = (
               row["stato1"],
               row["stato2"],)
           result.append(tupla)
       cursor.close()
       conn.close()
       return result
