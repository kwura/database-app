-- Add the primary keys
ALTER TABLE Contract ADD PRIMARY KEY(property_id, tenant_id, move_in_date);
ALTER TABLE Tenant ADD PRIMARY KEY(id);
ALTER TABLE Property ADD PRIMARY KEY(id);
ALTER TABLE Property_summary ADD PRIMARY KEY(property_id);

-- Add foreign keys
ALTER TABLE Contract ADD FOREIGN KEY(property_id) REFERENCES Property(id);
ALTER TABLE Contract ADD FOREIGN KEY(tenant_id) REFERENCES Tenant(id);
ALTER TABLE Property_summary ADD FOREIGN KEY(property_id) REFERENCES Property(id);