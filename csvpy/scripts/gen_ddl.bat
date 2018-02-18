rem running this .bat file will run the gen_ddl.py script for each .csv file, generating tables
@py C:\Career\LCN\database-app\csvpy\scripts\gen_ddl.py %* C:\Career\LCN\database-app\csvpy\Contract.csv
@py C:\Career\LCN\database-app\csvpy\scripts\gen_ddl.py %* C:\Career\LCN\database-app\csvpy\Property.csv
@py C:\Career\LCN\database-app\csvpy\scripts\gen_ddl.py %* C:\Career\LCN\database-app\csvpy\Property_summary.csv
@py C:\Career\LCN\database-app\csvpy\scripts\gen_ddl.py %* C:\Career\LCN\database-app\csvpy\Tenant.csv
@pause