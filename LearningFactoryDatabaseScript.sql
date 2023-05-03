/*HAAS table*/
drop table haas

create table haas
(	timestamp TIMESTAMP,
	coolant_level numeric(10,2),
	spindle_rpm numeric(10,2),
	lower_spindle_cl numeric(10,2),
	upper_spindle_cl numeric(10,2),
	x_coordinate numeric(10,2),
	y_coordinate numeric(10,2),
	z_coordinate numeric(10,2),
	a_coordinate numeric(10,2),
	b_coordinate numeric(10,2),
	x_work numeric(10,2),
	y_work numeric(10,2),
	z_work numeric(10,2),
	a_work numeric(10,2),
	b_work numeric(10,2));

select * from haas 

/*UR5 table*/
drop table ur5

create table ur5
(	timestamp TIMESTAMP,
	x_coordinate numeric(10,2),
	y_coordinate numeric(10,2),
	z_coordinate numeric(10,2),
	rx_coordinate numeric(10,2),
	ry_coordinate numeric(10,2),
	rz_coordinate numeric(10,2));

select * from ur5

/*Stratasys 1 table*/
drop table strata1 

create table strata1
(	timestamp TIMESTAMP,
	status varchar(100),
	material_type varchar(100),
	temperature numeric(10,2),
	lower_temp_cl numeric(10,2),
	upper_temp_cl numeric(10,2),
	job_progress numeric(10,2));	
	
select * from strata1 






