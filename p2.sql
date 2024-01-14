use kc1_26dec23;

delimiter $$
drop procedure if exists p2 $$
create procedure p2(num int)
begin
	declare i int default 1;
	declare sum int default 0;
	if num is null then
		select "null value not allowed" as ERR_MSG;
	elseif num >0 then
		repeat 
			set sum = sum +i;
			set i = i +1;

		until i > num end repeat;
		select concat("sum = ", sum) as Result;

	else 
		select "invalid input" as ERR;
	end if;
		
	
end $$
delimiter ;