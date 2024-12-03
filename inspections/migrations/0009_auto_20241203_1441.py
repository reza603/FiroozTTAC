from django.db import migrations

class Migration(migrations.Migration):

   dependencies = [
   ('inspections', '0008_alter_inspection_options'),
     ]

operations = [
migrations.RunSQL(
sql=[
   "ALTER TABLE YourTableName DROP CONSTRAINT inspections_inspection_company_id_f2621d37;",
   "DROP INDEX inspections_inspection_company_id_f2621d37 ON YourTableName;",
   "ALTER TABLE YourTableName ALTER COLUMN NationalId new_data_type;",
   "CREATE INDEX inspections_inspection_company_id_f2621d37 ON YourTableName (NationalId);",
    "ALTER TABLE YourTableName ADD CONSTRAINT inspections_inspection_company_id_f2621d37 FOREIGN KEY (NationalId) REFERENCES OtherTable(OtherColumn);"
],
reverse_sql=[
  "ALTER TABLE YourTableName DROP CONSTRAINT inspections_inspection_company_id_f2621d37;",
  "DROP INDEX inspections_inspection_company_id_f2621d37 ON YourTableName;",
  "ALTER TABLE YourTableName ALTER COLUMN NationalId old_data_type;",
  "CREATE INDEX inspections_inspection_company_id_f2621d37 ON YourTableName (NationalId);",
  "ALTER TABLE YourTableName ADD CONSTRAINT inspections_inspection_company_id_f2621d37 FOREIGN KEY (NationalId) REFERENCES OtherTable(OtherColumn);"
]
),
]