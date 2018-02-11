-- List me all tenants from property 501 West 26th
SELECT Property.address, fname, lname, monthly_rent FROM Property, Property_tenant, Tenant 
WHERE Property.address LIKE '%501 West 26%' AND Property.id = Property_tenant.property_id AND Tenant.id = Property_tenant.tenant_id
;

-- 