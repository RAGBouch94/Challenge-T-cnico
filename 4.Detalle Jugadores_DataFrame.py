#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Importar librerias necesarias para el funcionamiento de Python
import sqlite3
import pandas as pd

# Crear conexion SQL desde python a la BD del ejercicio
con = sqlite3.connect("database.sqlite")
cur = con.cursor()

# Cargar resultados de la SQL Query al Data Frame best_player en python, la query esta generada en base a un JOIN ON.
con = sqlite3.connect("database.sqlite")
df_best_player = pd.read_sql_query("SELECT player_name, birthday, height, weight, overall_rating, potential, preferred_foot, attacking_work_rate, defensive_work_rate, ball_control, positioning, stamina, strength, dribbling, vision, aggression FROM player INNER JOIN Player_Attributes on player.player_api_id = player_attributes.player_api_id", con)
#Formatear Cabeceras de listado
df_best_player.columns = ['PLAYER NAME','BIRTHDAY','HEIGHT','WEIGHT','OVERALL_RATING',
                                 'POTENTIAL','PREFERRED_FOOT','ATTACKING_WORK_RATE','DEFENSIVE_WORK_RATE','BALL_CONTROL','POSITIONING','STAMINA','STRENGTH','DRIBBLING','VISION','AGGRESSION']
                                 
df_best_player.info()
df_best_player.head()


# In[ ]:




