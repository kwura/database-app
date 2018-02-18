set client_encoding to 'utf8';

\copy People FROM C:/Career/LCN/database-app/csvpy/names.csv (FORMAT csv, HEADER True)