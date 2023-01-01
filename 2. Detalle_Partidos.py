#!/usr/bin/env python
# coding: utf-8

# In[137]:


#Importar librerias necesarias para el funcionamiento de Python
import sqlite3
import pandas as pd

# Crear conexion SQL desde python a la BD del ejercicio
con = sqlite3.connect("database.sqlite")
cur = con.cursor()

# Cargar resultados de la SQL Query al Data Frame best_player en python, la query esta generada en base a un JOIN ON.
con = sqlite3.connect("database.sqlite")
df_best_player = pd.read_sql_query("SELECT country.name AS COUNTRY, league.name AS LEAGUE, season AS SEASON, date AS DATE, Equipo_visita.team_long_name AS AWAY_TEAM, Equipo_Local.team_long_name AS LOCAL_TEAM, home_team_goal AS LOCAL_GOAL, away_team_goal AS AWAY_GOAL FROM Match INNER JOIN Country ON match.country_id = country.id INNER JOIN League ON match.country_id = league.country_id INNER JOIN Team AS Equipo_Visita ON match.away_team_api_id = Equipo_Visita.team_api_id  INNER JOIN Team AS Equipo_Local ON match.home_team_api_id = Equipo_Local.team_api_id", con)
df_best_player.info()
df_best_player.head()


# In[ ]:




