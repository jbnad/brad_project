
queries={
    'delete_row':
        "Update real_estate set deleted=1 where mls_number in (%s);",
    'delete_unwatch_row':
        "Update real_estate set deleted=1, hotlist=0 where mls_number in (%s);",
    'undelete_row':
        "Update real_estate set deleted=0 where mls_number in (%s);",
    'add_watch_list':
        "Update real_estate set hotlist=1 where mls_number in (%s);",
    'remove_watch_list':
        "Update real_estate set hotlist=0 where mls_number in (%s);",
    'update_note':
        "Update real_estate set note='%s' where mls_number=%s",
    'get_not_deleted_not_hotlist':
        "Select * from real_estate where deleted != 1 and hotlist != 1;",
    'get_watchlist':
        "Select * from real_estate where hotlist = 1;",
    'get_deleted':
        "Select * from real_estate where deleted = 1;",
    'insert_into_update_time':
        'Insert into update_time values(`id`, now());',
    'get_latest_timestamp':
        'select max(update_time) from update_time;',
    'create_table':
        'Create table real_estate (`id` BIGINT NOT NULL AUTO_INCREMENT Primary Key,mls_number int UNIQUE,class varchar(40),building_type varchar(40), area varchar(40),price int,address varchar(40), city varchar(40),state varchar(10),status varchar(40),zoning varchar(20),days_on_market int, date_added DATETIME, last_updated DATETIME, deleted SMALLINT, hotlist SMALLINT, note text) ENGINE=MyISAM;',
    'create_table_update_time':
        'Create table update_time (`id` Int NOT NULL AUTO_INCREMENT Primary Key, update_time DATETIME) ENGINE=MyISAM;',
    'insert_update':
    "(`id`,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s', '%s', now(), now(), '0', '0', '')"
} 
   




"""    
    'create_table2':
        'CREATE TABLE `homes` (`id` int(11) NOT NULL AUTO_INCREMENT Primary Key,`mls_id` int(11) UNIQUE, `price` int(11),last_update Datetime);',
    'delete_table':
        'Drop table `homes`;',
    'add_row':
        'Insert into homes values(`id`,%s,%s,now());',
    'add_row_dup':
        'Insert into homes values(`id`,2,100000,now()) on Duplicate Key Update price=200000;',
    'add_row_dup2':
            "Insert into real_estate values(`id`,%s,'%s','%s','%s',%s,'%s','%s','%s','%s','%s', '%s', now(), now(), 0, 0, '') on Duplicate Key Update price=%s, last_updated=now(), days_on_market=%s",
    'testing':
    "Insert into real_estate VALUES(`id`,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s', '%s', '', '', '0', '0', '') on Duplicate Key Update price='%s', last_updated='', days_on_market='%s'",
    'add_row_dup3':
        "Insert into real_estate on Duplicate Key Update price=%s;",
    
    
    'testyo1':
                "Insert into real_estate values(`id`,%s,'%s','%s','%s',%s,'%s','%s','%s','%s','%s', '%s', now(), now(), 0, 0, '') on Duplicate Key Update price=%s, last_updated=now(), days_on_market=%s",
}
"""
