-- Show current top 15 highest monthly paying properties. Return property id, tenant name, neighborhood, address, and monthly rent
SELECT p.id, t.first_name, t.last_name, p.neighborhood, p.address, c.monthly_rent
FROM Property as p 
JOIN Contract AS c ON p.id = c.property_id
JOIN Tenant AS t ON t.id = c.tenant_id
WHERE c.move_out_date > '2012/1/1'
ORDER BY 6 DESC
LIMIT 15; 


-- Show the properties with the 5 lowest HOA fees. Return Property id, neighborhood, address, yearly_hoa and prop_tax.
SELECT p.id, p.neighborhood, p.address, ps.yearly_hoa, ps.property_tax
FROM Property as p
JOIN Property_summary as ps ON p.id = ps.property_id
ORDER BY 4 DESC
LIMIT 5;

-- Show the tenants who moved out from 2006 to 2011 and return deposit and refund amounts.
SELECT t.first_name, t.last_name, t.email, t.phone_number, c.deposit, c.refund, c.move_out_date
FROM Tenant as t 
JOIN Contract as c ON t.id = c.tenant_id
WHERE EXTRACT(year FROM c.move_out_date) >= '2006' AND EXTRACT(year FROM c.move_out_date) <= '2011'
ORDER BY c.deposit DESC;

-- Show the number of properties without a mortgage
SELECT Count(*) AS Number_of_properties_without_mortgage FROM 
Property_summary WHERE initial_mortgage IS NULL; 

-- Show the 10 lowest current mortgages.
SELECT p.neighborhood, p.address, ps.property_type, ps.year_built, ps.sale_price, ps.initial_mortgage, ps.remaining_mortgage, ps.interest
FROM Property_summary AS ps
JOIN Property AS p ON p.id = ps.property_id
ORDER BY 7 ASC
LIMIT 10;

-- Show tenants who are living in properties with greater than 4 bathrooms
SELECT t.first_name, t.last_name, p.neighborhood, ps.property_type, p.address, ps.num_beds, ps.num_bath
FROM Property_summary AS ps
JOIN Property AS p ON p.id = ps.property_id
JOIN Contract AS c ON c.property_id = p.id
JOIN Tenant AS t ON t.id = c.tenant_id
WHERE num_bath > 4
ORDER BY 7 DESC;
