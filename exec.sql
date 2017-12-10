CREATE DEFINER=`root`@`localhost` PROCEDURE `exec_sql`(IN `sql_str` VARCHAR(255))
    NO SQL
BEGIN
SELECT sql_str INTO sql;
select sql;
prepare stmt from sql;
execute stmt;
deallocate prepare stmt;
END