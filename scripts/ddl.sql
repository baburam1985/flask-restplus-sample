create table customer
(
	id integer not null
		constraint customer_pkey
			primary key,
	name varchar,
	age integer,
	salary integer
)
;

