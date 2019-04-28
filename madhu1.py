import pymysql
from madhu2 import paswd

class backend:
    
    GUIDB='natural_calamity'
    
    def connect(self):
        conn=pymysql.connect(**paswd)
        cursor=conn.cursor()
        return conn,cursor
    
    def close(self,cursor,conn):
        cursor.close()
        conn.close()
    
    def usedb(self,cursor):
        cursor.execute("USE natural_calamity")

    def add_earthquake(self,e_id,seismic_wave,p_wave,s_wave,ground_motion):
        conn,cursor=self.connect()
        self.usedb(cursor)
        cursor.execute("INSERT INTO earthquake(e_id,seismic_wave,p_wave,s_wave,ground_motion) VALUES (%s,%s,%s,%s,%s)",(e_id,seismic_wave,p_wave,s_wave,ground_motion))
        conn.commit()
        self.close(cursor,conn)

    def add_floods(self,f_id,water_surface_elevation,water_level_measurement,soil_moisture_content,rainfall_measurement):
        conn,cursor=self.connect()
        self.usedb(cursor)
        cursor.execute("INSERT INTO flood(f_id,water_surface_elevation,water_level_measurement,soil_moisture_content,rainfall_measurement) VALUES (%s,%s,%s,%s,%s)",(f_id,water_surface_elevation,water_level_measurement,soil_moisture_content,rainfall_measurement))
        conn.commit()
        self.close(cursor,conn)

    def add_wildfire(self,w_id,temperature,humidity,smoke_density,light_intensity):
        conn,cursor=self.connect()
        self.usedb(cursor)
        cursor.execute("INSERT INTO wildfire(w_id,temperature,humidity,smoke_density,light_intensity) VALUES (%s,%s,%s,%s,%s)",(w_id,temperature,humidity,smoke_density,light_intensity))
        conn.commit()
        self.close(cursor,conn)

    def add_storms(self,s_id,equilibrium_level,lapse_rate,convective_inhibition,storm_relative_helicity):
        conn,cursor=self.connect()
        self.usedb(cursor)
        cursor.execute("INSERT INTO storm(s_id,equilibrium_level,lapse_rate,convective_inhibition,storm_relative_helicity) VALUES (%s,%s,%s,%s,%s)",(s_id,equilibrium_level,lapse_rate,convective_inhibition,storm_relative_helicity))
        conn.commit()
        self.close(cursor,conn)

    def add_alert(self,val,cn,pn):
        conn,cursor=self.connect()
        self.usedb(cursor)
        cursor.execute("insert into alert (value,calamity_name,parameter_name) VALUES (%s,%s,%s)",(val,cn,pn))
        conn.commit()
        self.close(cursor,conn)

    def update_doc_password(self,usr,new_password,old_password):
        conn,cursor=self.connect()
        self.usedb(cursor)
        cursor.execute("UPDATE users SET password=%s WHERE password=%s AND Name=%s ",(new_password,old_password,usr))
        conn.commit()
        self.close(cursor,conn)

ob=backend()
