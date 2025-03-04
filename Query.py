import pandas as pd

# Load the Excel file with multiple sheets
file_path = "data.xlsx"
sheets = pd.read_excel(file_path, sheet_name=None)

# Read the main table (Sheet1) - Only first row
df_main = sheets["Sheet1"].iloc[:1]  # Process only row 1

# Read location table (Sheet2) and create a mapping {location_name: location_code}
df_location = sheets["Sheet2"]
location_map = dict(zip(df_location["location_name"], df_location["location_code"]))

# Read user table (Sheet3) and create a mapping {name: user_id}
df_user = sheets["Sheet3"]
user_map = dict(zip(df_user["name"], df_user["user_id"]))

# Map X (new names) to their respective IDs (assumed present in Sheet1)
x_name_to_id = dict(zip(df_main["X"], df_main["id"]))

# Define the table name
TABLE_NAME = "employees"

# Process only the first row
for _, row in df_main.iterrows():
    v_name = row.get("V", "").strip()  # Existing name
    x_name = row.get("X", "").strip()  # New name
    location_name = row.get("location", "").strip()
    emp_name = row.get("name", "").strip()

    # Get corresponding location_code
    location_code = location_map.get(location_name, "NULL")

    # Get user_id based on employee name
    user_id = user_map.get(emp_name, "NULL")

    # Define workgroup value
    workgroup = 5  # Fixed value or extract from data if needed

    if v_name:  # If V exists, generate UPDATE
        sql_stmt = f"""
        UPDATE {TABLE_NAME} 
        SET userinfo = '{user_id}', workgroup = {workgroup} 
        WHERE id = (SELECT id FROM {TABLE_NAME} WHERE name = '{v_name}');
        """
    elif x_name in x_name_to_id:  # If X exists but V is empty, generate INSERT
        id_value = x_name_to_id[x_name]
        sql_stmt = f"""
        INSERT INTO {TABLE_NAME} (id, name, age, salary, location_code, user_id, workgroup) 
        VALUES ({id_value}, '{row['name']}', {row['age']}, {row['salary']}, {location_code}, {user_id}, {workgroup});
        """
    else:
        sql_stmt = "-- No valid V or X found for row 1, skipping."

    print(sql_stmt.strip())  # Print the generated statement for row 1
