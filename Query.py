import pandas as pd

# Load the Excel file with multiple sheets
file_path = "data.xlsx"
sheets = pd.read_excel(file_path, sheet_name=None)

# Read the main table (Sheet1) - Only first row
df_main = sheets["Sheet1"].iloc[:1]  # Process only the first row

# Read location table (Sheet2) and create a mapping {location_name: location_code}
df_location = sheets["Sheet2"]
location_map = dict(zip(df_location["location_name"], df_location["location_code"]))

# Read user table (Sheet3) and create a mapping {name: user_id}
df_user = sheets["Sheet3"]
user_map = dict(zip(df_user["name"], df_user["user_id"]))

# Define the table name
TABLE_NAME = "employees"

# Process only the first row
for _, row in df_main.iterrows():
    location_name = row.get("location", "").strip()
    emp_name = row.get("name", "").strip()

    # Get corresponding location_code
    location_code = location_map.get(location_name, "NULL")

    # Get user_id based on employee name
    user_id = user_map.get(emp_name, "NULL")

    # Define workgroup value
    workgroup = 5  # Fixed value or extract from data if needed

    # Generate the UPDATE SQL statement for row 1
    sql_stmt = f"""
    UPDATE {TABLE_NAME} 
    SET userinfo = '{user_id}', workgroup = {workgroup} 
    WHERE location = '{location_code}';
    """
    
    print(sql_stmt.strip())  # Print the generated statement for row 1
