#SELECT count(*) FROM customers where id IS NULL;
tables = ['customers', 'orders', 'products', 'prices']
columns = ['id', 'create_date']
for t in tables:
    for c in columns:
        print(f"SELECT count(*) FROM {t} where {c} IS NULL;")