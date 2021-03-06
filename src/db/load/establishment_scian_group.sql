-- `psql -U postgres --host 127.0.0.1 --port 5432 -f db/load/establishment_scian_group.sql`
-- this script doesn't need to be executed if we populate database with `dump.sql` in `data` repo

update map_establishment set scian_group_id = 1;
update map_establishment set scian_group_id = 2 where codigo_act in ('931110',
'931310',
'931510',
'931810',
'931610',
'931410',
'931210');
update map_establishment set scian_group_id = 4 where codigo_act in ('813230',
'813210');
update map_establishment set scian_group_id = 5 where codigo_act in ('623312',
'622212',
'621422',
'621332',
'621399',
'541942',
'622112',
'621492',
'621112',
'623222',
'621114',
'622311',
'621116',
'621421',
'624122',
'622312',
'622111');
update map_establishment set scian_group_id = 6 where codigo_act in ('237993',
'237994',
'236113',
'237991',
'562112',
'434221',
'237132',
'237312',
'434311',
'222112',
'237313',
'237992',
'237133',
'434219',
'237311',
'222111',
'237212',
'434313',
'562111',
'237999',
'434319',
'238910',
'237121',
'435110',
'236212',
'236222',
'434225',
'238340',
'435210',
'435419',
'237123',
'237111',
'434226',
'237112',
'221110',
'236111',
'541310',
'434227',
'221120',
'541330',
'237131',
'434224',
'237113',
'222210',
'238121',
'238311',
'238210',
'434229',
'236211',
'236221',
'541360',
'237213',
'434211',
'238330',
'434314',
'236112',
'238110',
'541350',
'541320');
update map_establishment set scian_group_id = 7 where codigo_act in ('611122',
'611151',
'611182',
'611212',
'611162',
'611121',
'611612',
'611152',
'611171',
'611142',
'611111',
'611312',
'611131',
'611211',
'611141',
'611172',
'611611',
'611112',
'611161',
'611132',
'611311',
'611622');
update map_establishment set scian_group_id = 8 where codigo_act in ('713112',
'712112',
'712190',
'713114',
'713944');
update map_establishment set scian_group_id = 10 where codigo_act in ('484231',
'484121',
'484234',
'484221',
'484224',
'484233',
'484111',
'484222',
'484223',
'488320');
