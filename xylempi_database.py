#xylempi_database.py
# handles database operations

import psycopg2

class XylemPiDatabase:
    def __init__(self, dbname, user, password, host='localhost'):
        self.conn = psycopg2.connect(dbname=dbname,
                                     user=user,
                                     password=password,
                                     host=host)
        self.cur = self.conn.cursor()
        
    def insert_sensor_readings(self,
                               moisture_status,
                               temperature,
                               humidity,
                               pressure,
                               luminosity,
                               irrig_score,
                               timestamp):
        
        #need to extract the last 3 chars of the returns from moisture_status
        moisture_status_abbr = moisture_status[-3:]
        
        #also need to abbreiviate light message
        def light_abbr(luminosity):
            return "Light" if luminosity == "Light Detected" else "Dark"
        lum_abbr = light_abbr(luminosity)
        
        sql = "INSERT INTO sensor_readings (moisture, temperature, humidity, pressure, luminosity, irrig_score, timestamp) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (moisture_status_abbr, temperature, humidity, pressure, lum_abbr, irrig_score, timestamp)
        self.cur.execute(sql, data)
        self.conn.commit();
        
    def fetch_sensor_data(self):
        sql = "SELECT * FROM sensor_readings ORDER BY timestamp DESC"
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def fetch_recent_data(self):
        sql = "SELECT * FROM sensor_readings ORDER BY timestamp DESC LIMIT 10"
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def fetch_latest_irrig_score_30(self):
        sql = "SELECT * FROM sensor_readings WHERE irrig_score > 29 ORDER BY timestamp DESC LIMIT 1"
        self.cur.execute(sql)
        self.conn.commit()
        data = self.cur.fetchone()
        return data
        
    def close_connection(self):
        self.cur.close()
        self.conn.close()