SELECT   country.name AS COUNTRY, league.name AS LEAGUE, season AS SEASON, date AS DATE, Equipo_visita.team_long_name AS AWAY_TEAM, Equipo_Local.team_long_name AS LOCAL_TEAM, home_team_goal AS LOCAL_GOAL, away_team_goal AS AWAY_GOAL
FROM Match 
INNER JOIN Country ON match.country_id = country.id
INNER JOIN League ON match.country_id = league.country_id
INNER JOIN Team AS Equipo_Visita ON match.away_team_api_id = Equipo_Visita.team_api_id 
INNER JOIN Team AS Equipo_Local ON match.home_team_api_id = Equipo_Local.team_api_id

