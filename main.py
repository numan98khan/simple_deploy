

# az postgres up --resource-group rg-data-dev --location southeastasia --sku-name B_Gen5_1 --server-name postdbtest --database-name maindb --admin-user numan98khan --admin-password NAUman!@#123 --ssl-enforcement Enabled

database_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser='numan98khan@postdbtest',
    dbpass='NAUman!@#123',
    dbhost='postdbtest.postgres.database.azure.com',
    dbname='maindb'
)

print(database_uri)