---
nav_title: "Data Retention"
article_title: Snowflake Data Retention
page_order: 3
description: "This page covers how to retain full events data when the Braze retention policy is applied."
page_type: partner
search_tag: Partner
---

# Snowflake data retention

> Braze anonymizes (removes personally identifiable information (PII)) from all events data that is older than two years old. If you use Snowflake data sharing, you may choose to retain the full events data in your environment by storing a copy in your Snowflake account before the retention policy is applied.

This page presents two ways you can retain non-anonymized data: 

- Copy your data to another Snowflake database
- Unload your data to a stage

{% alert warning %}
Braze automatically anonymizes events data for users that are deleted from Braze, as described in [Data Protection Technical Assistance]({{site.baseurl}}/dp-technical-assistance/). Any data copied outside of the shared database will not be included in this process, as it’s no longer managed by Braze. 
{% endalert %}

## Copy all data to another Snowflake database

You can retain non-anonymized data by copying your data from the shared `BRAZE_RAW_EVENTS` schema to another database and schema in Snowflake. To do so, follow these steps:

1. Create the procedure `COPY_BRAZE_SHARE`, which will be used to copy all the data shared by Braze to another database and schema within Snowflake. 

{% raw %}
```json
-- 
-- @param string SOURCE_DATABASE - database name of the braze data share
-- @param string SOURCE_SCHEMA - schema name of the braze data share
-- @param string DESTINATION_DATABASE - 
-- @param string DESTINATION_SCHEMA - 
-- @param string MAX_DATE - copy data on / before the max date default DATEADD(year, -2, CURRENT_DATE())
-- @param string TABLE_NAME_FILTER - filter to select table that will be unloaded, default to 'USER_%'
-- 

CREATE PROCEDURE COPY_BRAZE_SHARE(
    SOURCE_DATABASE STRING,
    SOURCE_SCHEMA STRING,
    DESTINATION_DATABASE STRING,
    DESTINATION_SCHEMA STRING,
    MAX_DATE DATE default DATEADD(year, -2, CURRENT_DATE()),
    TABLE_NAME_FILTER STRING default 'USERS_%'
)
RETURNS TABLE (TABLE_NAME STRING, SUCCESS BOOLEAN, INFO STRING)
LANGUAGE PYTHON
RUNTIME_VERSION = '3.8'
PACKAGES = ('snowflake-snowpark-python')
HANDLER = 'run'
AS
$$
import snowflake.snowpark as snowpark
from snowflake.snowpark.exceptions import SnowparkSQLException

def run(session: snowpark.Session, SOURCE_DATABASE: str, SOURCE_SCHEMA: str, DESTINATION_DATABASE: str, DESTINATION_SCHEMA: str, MAX_DATE: str, TABLE_NAME_FILTER: str):
    result = []
    
    # Get the list of filtered table names
    table_query = f"""
        SELECT table_name 
        FROM {SOURCE_DATABASE}.INFORMATION_SCHEMA.TABLES
        WHERE TABLE_SCHEMA = '{SOURCE_SCHEMA}' AND table_name LIKE '{TABLE_NAME_FILTER}'
    """
    
    tables = session.sql(table_query).collect()
    
    # Iterate through each table and copy data
    for row in tables:
        table_name = row['TABLE_NAME']

	 # skip archive tables
        if table_name.endswith('_ARCHIVED'):
            continue

        # Check if the destination table exists
        check_table_query = f"""
            SELECT COUNT(*) as count
            FROM {DESTINATION_DATABASE}.INFORMATION_SCHEMA.TABLES
            WHERE TABLE_SCHEMA = '{DESTINATION_SCHEMA}' AND TABLE_NAME = '{table_name}'
        """
        table_exists = session.sql(check_table_query).collect()[0]['COUNT'] > 0

        if table_exists:
            # find the current max SF_CREATED_AT in the existing table
            cur_max_date = None
            
            date_query = f"""
                SELECT MAX(SF_CREATED_AT) as CUR_MAX_DATE
                FROM {DESTINATION_DATABASE}.{DESTINATION_SCHEMA}.{table_name}
            """
            date_result = session.sql(date_query).collect()
            
            if date_result:
                cur_max_date = date_result[0]['CUR_MAX_DATE']
                
            if cur_max_date:
                # If the destination table is not empty, only add data that is newer than cur_max_date and older than MAX_DATE
                copy_query = f"""
                    INSERT INTO {DESTINATION_DATABASE}.{DESTINATION_SCHEMA}.{table_name}
                    SELECT * FROM {SOURCE_DATABASE}.{SOURCE_SCHEMA}.{table_name}
                    WHERE SF_CREATED_AT <= '{MAX_DATE}'
                        AND SF_CREATED_AT > '{cur_max_date}'
                """
            else:
                # If the destination table is empty, copy all data before MAX_DATE
                copy_query = f"""
                    INSERT INTO {DESTINATION_DATABASE}.{DESTINATION_SCHEMA}.{table_name}
                    SELECT * FROM {SOURCE_DATABASE}.{SOURCE_SCHEMA}.{table_name}
                    WHERE SF_CREATED_AT <= '{MAX_DATE}'
                """
        else:
            # If table doesn't exist, create it and copy data
            copy_query = f"""
                CREATE TABLE {DESTINATION_DATABASE}.{DESTINATION_SCHEMA}.{table_name} AS
                SELECT * FROM {SOURCE_DATABASE}.{SOURCE_SCHEMA}.{table_name}
                WHERE SF_CREATED_AT <= '{MAX_DATE}'
            """
        
        try:
            session.sql(copy_query).collect()
            result.append([table_name, True, ""])
        except SnowparkSQLException as e:
            result.append([table_name, False, str(e)])
    
    # Return the results
    return session.create_dataframe(result, schema=['TABLE_NAME', 'SUCCESS', 'INFO'])
$$;
```
{% endraw %}

{: start="2"}
2. Run the below command to execute the procedure. By default, the procedure will back up data older than two years for all `USERS_*` event types. 

{% raw %}
```json
-- this will copy all the rows that are 2 years or older in all the 'USERS_*' tables 
-- from 'SOURCE_DB'.'SOURCE_SCHEMA' to 'DEST_DB'.'DEST_SCHEMA'

CALL COPY_BRAZE_SHARE('SOURCE_DB', 'SOURCE_SCHEMA', 'DEST_DB', 'DEST_SCHEMA')
```
{% endraw %}

{: start="3"}
3. (Optional) Specify a filter to choose what age data to back up, and specify a table name filter to back up only selected events tables. 

{% raw %}
```json
-- this will copy all the rows that are 1 year or older in all the 'USERS_BEHAVIORS_*' tables
-- from 'SOURCE_DB'.'SOURCE_SCHEMA' to 'DEST_DB'.'DEST_SCHEMA'

CALL COPY_BRAZE_SHARE('SOURCE_DB', 'SOURCE_SCHEMA', 'DEST_DB', 'DEST_SCHEMA', DATEADD(year, -1, CURRENT_DATE()), 'USERS_BEHAVIORS_%')
```
{% endraw %}

{% alert note %}
Repeat running of the procedure shouldn't create duplicate records, as it will check the max (`SF_CREATED_AT`) and only back up data newer than that. 
{% endalert %}

## Unload data to stage

You can retain non-anonymized data by unloading data from the shared `BRAZE_RAW_EVENTS` schema to a stage. To do so, follow these steps:

1. Create the procedure `UNLOAD_BRAZE_SHARE`, which will be used to copy all the data shared by Braze to the specified stage.

{% raw %}
```json
-- 
-- @param string DATABASE_NAME - database name of the braze data share
-- @param string SCHEMA_NAME - schema name of the braze data share
-- @param string STAGE_NAME - Snowflake stage where the data will be unloaded
-- @param int MIN_DATE - copy data from this date (inclusive)
-- @param int MAX_DATE - copy data till this date (exclusive)
-- @param string TABLE_NAME_FILTER - filter to select table that will be unloaded, default to 'USER_%'
-- 
CREATE PROCEDURE UNLOAD_BRAZE_SHARE(
    SOURCE_DATABASE STRING,
    SOURCE_SCHEMA STRING,
    STAGE_NAME STRING,
    MIN_DATE DATE,
    MAX_DATE DATE,
    TABLE_NAME_FILTER STRING default 'USERS_%'
)
RETURNS TABLE (TABLE_NAME STRING, SUCCESS BOOLEAN, INFO STRING)
LANGUAGE PYTHON
RUNTIME_VERSION = '3.8'
PACKAGES = ('snowflake-snowpark-python')
HANDLER = 'run'
AS
$$
import snowflake.snowpark as snowpark
from snowflake.snowpark.exceptions import SnowparkSQLException

def run(session: snowpark.Session, DATABASE_NAME: str, SCHEMA_NAME: str, STAGE_NAME: str, MIN_DATE: str, MAX_DATE: str, TABLE_NAME_FILTER: str):
    result = []

    if MIN_DATE >= MAX_DATE:
        result.append(["MIN_DATE cannot be more recent than MAX_DATE", False, ""])
        return session.create_dataframe(result, schema=['TABLE_NAME', 'SUCCESS', 'INFO'])
        
    # Get list of tables
    table_query = f"""
    SELECT TABLE_NAME 
    FROM {DATABASE_NAME}.INFORMATION_SCHEMA.TABLES 
    WHERE TABLE_SCHEMA = '{SCHEMA_NAME}' AND TABLE_NAME LIKE '{TABLE_NAME_FILTER}'
    """
    tables = session.sql(table_query).collect()
    
    for table in tables:
        table_name = table['TABLE_NAME']

	 # skip archive tables
        if table_name.endswith('_ARCHIVED'):
            continue
        
        # Create CSV file name
        csv_file_name = f"{table_name}_{MIN_DATE}_{MAX_DATE}.csv"
        
        # Construct COPY INTO command with date filter
        copy_cmd = f"""
        COPY INTO @{STAGE_NAME}/{csv_file_name}
        FROM (
            SELECT *
            FROM {DATABASE_NAME}.{SCHEMA_NAME}.{table_name}
            WHERE SF_CREATED_AT >= TO_DATE('{MIN_DATE}') and SF_CREATED_AT < TO_DATE('{MAX_DATE}')
        )
        FILE_FORMAT = (TYPE = CSV FIELD_OPTIONALLY_ENCLOSED_BY = '"')
        HEADER = TRUE
        OVERWRITE = FALSE
        """
        
        # Execute COPY INTO command
        try:
            session.sql(copy_cmd).collect()
            result.append([table_name, True, csv_file_name])
        except SnowparkSQLException as e:
            result.append([table_name, False, str(e)])
    
    return session.create_dataframe(result, schema=['TABLE_NAME', 'SUCCESS', 'INFO'])
$$;
```
{% endraw %}

{: start="2"}
2. Run the below commands to execute the procedure. If you don’t specify a table name filter, the default behavior will copy all tables with `USERS_` prefix.

{% raw %}
```json
-- create a Snowflake stage to store the file
create stage MY_EXPORT_STAGE;

-- call the procedure 
-- this will unload date between '2020-01-01' and '2021-01-01'
-- from tables with 'USERS_' prefix in 'DATABASE_NAME'.'SCHEMA'
CALL UNLOAD_BRAZE_SHARE('DATABASE_NAME', 'SCHEMA', 'MY_EXPORT_STAGE', '2020-01-01', 2021-01-01');

-- should list the files that's unloaded 
LIST @MY_EXPORT_STAGE;
```
{% endraw %}

{: start="3"}
3. (Optional) Specify a filter in the procedure to unload only specified tables.

{% raw %}
```json
-- create a Snowflake stage to store the file
create stage MY_EXPORT_STAGE;

-- this will unload date between '2020-01-01' and '2021-01-01'
-- from tables with 'USERS_BEHAVIORS_' prefix in 'DATABASE_NAME'.'SCHEMA'
CALL EXPORT_BRAZE_SHARE_TO_STAGE('DATABASE_NAME', 'SCHEMA', 'MY_EXPORT_STAGE', '2020-01-01', 2021-01-01', 'USERS_BEHAVIORS_%');

-- should list the files that's unloaded 
LIST @MY_EXPORT_STAGE;
```
{% endraw %}
