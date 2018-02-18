set client_encoding to 'utf8';
\copy Contract FROM C:/Career/LCN/database-app/csvpy/Contract.csv (FORMAT csv, HEADER True)
\copy Property FROM C:/Career/LCN/database-app/csvpy/Property.csv (FORMAT csv, HEADER True)
\copy Property_summary FROM C:/Career/LCN/database-app/csvpy/Property_summary.csv (FORMAT csv, HEADER True)
\copy Tenant FROM C:/Career/LCN/database-app/csvpy/Tenant.csv (FORMAT csv, HEADER True)