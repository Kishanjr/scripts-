import pandas as pd

# Load the Excel file with multiple sheets
file_path = "data.xlsx"
sheets = pd.read_excel(file_path, sheet_name=None)

# Read the main table (Sheet1)
df_main = sheets["Sheet1"]

# Read location table (Sheet2) and create a mapping {location_name: location_code}
df_location = sheets["Sheet2"]
location_map = dict(zip(df_location["location_name"], df_location["location_code"]))

# Read user table (Sheet3) and create a mapping {name: user_id}
df_user = sheets["Sheet3"]
user_map = dict(zip(df_user["name"], df_user["user_id"]))

# Map X (new names) to their respective IDs
x_name_to_id = dict(zip(df_main["X"], df_main["id"]))

# Define the table name
TABLE_NAME = "employees"

# Initialize a list for SQL statements
sql_statements = []

for _, row in df_main.iterrows():
    v_name = row.get("V", "").strip()  # Existing name
    x_name = row.get("X", "").strip()  # New name
    location_name = row.get("location", "").strip()
    emp_name = row.get("name", "").strip()

    # Get corresponding location_code
    location_code = location_map.get(location_name, "NULL")

    # Get user_id based on employee name
    user_id = user_map.get(emp_name, "NULL")

    if v_name:  # If V exists, generate UPDATE
        sql_stmt = f"""
        UPDATE {TABLE_NAME} 
        SET name = '{row['name']}', age = {row['age']}, salary = {row['salary']}, 
            location_code = {location_code}, user_id = {user_id} 
        WHERE id = (SELECT id FROM {TABLE_NAME} WHERE name = '{v_name}');
        """
    elif x_name in x_name_to_id:  # If X exists but V is empty, generate INSERT
        id_value = x_name_to_id[x_name]
        sql_stmt = f"""
        INSERT INTO {TABLE_NAME} (id, name, age, salary, location_code, user_id) 
        VALUES ({id_value}, '{row['name']}', {row['age']}, {row['salary']}, {location_code}, {user_id});
        """
    else:
        continue  # Skip rows where both V and X are empty

    sql_statements.append(sql_stmt.strip())

# Print the generated SQL statements
for stmt in sql_statements:
    print(stmt)
