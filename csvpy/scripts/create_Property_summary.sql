create table Property_Summary(
   property_id int,
   property_type varchar(10),
   year_built int,
   date_of_ownership date,
   sale_price NUMERIC(15,2),
   initial_mortgage numeric(15,2),
   remaining_mortgage numeric(15,2),
   interest NUMERIC(3,2),
   yearly_hoa NUMERIC(15,2),
   property_tax NUMERIC(15,2),
   num_beds int,
   num_bath int,
   area_sqft NUMERIC(15,2)
);