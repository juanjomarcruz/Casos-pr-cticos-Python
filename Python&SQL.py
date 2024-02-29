import psycopg2
conn = psycopg2.connect(host="localhost", database="demo",
user = "postgres", password="13211321Jj-bbc")
sql_query_1="SELECT * FROM airports"
sql_query_2="SELECT COUNT(flight_id) as Total_vuelos FROM flights"
sql_query_3="SELECT DISTINCT(aircraft_code) FROM flights"
sql_query_4="SELECT departure_airport, AVG(actual_departure - scheduled_departure) as Average_Departure_Delay FROM flights GROUP BY departure_airport"
sql_query_5="SELECT aircraft_code, COUNT(flight_id) as Total_Delayed_flights FROM flights WHERE Status='Delayed' GROUP BY aircraft_code"
sql_query_6="SELECT arrival_airport, MAX(actual_arrival - scheduled_arrival) as Maximum_arrival_delay FROM flights GROUP BY arrival_airport"
sql_query_7="SELECT aircraft_code, departure_airport, COUNT(flight_id) as Total_flights_plus30min_delay FROM flights WHERE (actual_departure - scheduled_departure) > '00:30:00' GROUP BY aircraft_code,departure_airport"
sql_query_8="SELECT aircraft_code FROM flights WHERE (actual_departure-scheduled_departure)=(SELECT MAX(actual_departure-scheduled_departure) FROM flights)"
sql_query_9="SELECT departure_airport, arrival_airport, COUNT(flight_id) FROM flights GROUP BY departure_airport, arrival_airport HAVING COUNT(flight_id)>100"
sql_query_10="SELECT aircraft_code, AVG(actual_departure-scheduled_departure) as average_departure_delay FROM flights WHERE aircraft_code IN (SELECT aircraft_code FROM flights WHERE Status='Cancelled' GROUP BY aircraft_code) GROUP BY aircraft_code"
sql_query_11="SELECT aircraft_code, MAX(actual_arrival-scheduled_arrival) as Max_Arrival_Delay FROM flights GROUP BY aircraft_code"
sql_query_12="SELECT aircraft_code, MAX(actual_departure-scheduled_departure) as Max_Departure_Delay FROM flights GROUP BY aircraft_code"
sql_query_13="SELECT aircraft_code, COUNT(flight_id) as Total_flights FROM flights WHERE aircraft_code IN (SELECT aircraft_code FROM flights WHERE Status='Cancelled' GROUP BY aircraft_code) GROUP BY aircraft_code"
sql_query_14="SELECT aircraft_code, AVG(actual_departure-scheduled_departure) as average_departure_delay FROM flights WHERE aircraft_code IN (SELECT aircraft_code FROM flights GROUP BY aircraft_code HAVING COUNT(flight_id)>100) GROUP BY aircraft_code"
sql_query_15="SELECT aircraft_code, AVG(actual_departure-scheduled_departure) as average_departure_delay FROM flights WHERE aircraft_code IN (SELECT aircraft_code FROM flights WHERE Status='Cancelled' GROUP BY aircraft_code) GROUP BY aircraft_code"
cursor=conn.cursor()
cursor.execute(sql_query_15)
title=[i[0] for i in cursor.description]
print(title)
rows=cursor.fetchall()
for row in rows:
  print(*row)
