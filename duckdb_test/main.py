import duckdb

# Testing duckdb
# Surprised
data = duckdb.query("SELECT 1 + 1").fetchall()

print(data)

# querying from a csv file
another = duckdb.query("SELECT * from propuestas_mabe_visual.csv")
print(another)
output = another.fetchdf()
print(output)
output.to_csv("output.csv")

output = duckdb.query("SELECT * from propuestas_mabe_visual.csv").fetchdf()
# Great! I can query from a csv file
#
