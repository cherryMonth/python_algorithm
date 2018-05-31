# 三维温度变化图的SQL语句:

"select store_temp_layer, store_temp_breadth, store_temp_width, store_length, store_breadth ,entry_time , entry_data "
    "from grm_production2.entry_temperature, grm_production2.store where entry_temperature.store_id = store.store_id "
    "and entry_temperature.store_id = 14 and entry_time = '2018-01-01 01:05:04';"


# 历史温度变化图语句:
SELECT * FROM grm_production2.entry_temperature where 
entry_temperature.store_id = 1 and entry_temperature.entry_time >= '2017-03-01 00:00:00' and
 entry_temperature.entry_time <= '2017-04-01 00:00:00' and entry_temperature.entry_time like '2017-%-% 09:00:05';
