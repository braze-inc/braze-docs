---
nav_title: "데이터 보존"
article_title: Snowflake 데이터 보존
page_order: 3
description: "이 페이지에서는 Braze 유지 정책이 적용될 때 전체 이벤트 데이터를 유지하는 방법을 다룹니다."
page_type: partner
search_tag: Partner
---

# Snowflake 데이터 유지

> Braze anonymizes—removes personally identifiable information (PII)—from all events data stored in Snowflake that is older than two years old. Snowflake 데이터 공유를 사용하는 경우 유지 정책이 적용되기 전에 Snowflake 계정에 사본을 저장하여 환경의 전체 이벤트 데이터를 유지하도록 선택할 수 있습니다.

이 페이지에서는 익명화되지 않은 데이터를 유지할 수 있는 두 가지 방법을 제공합니다. 

- 데이터를 다른 Snowflake 데이터베이스에 복사하십시오
- 스테이지로 데이터 언로드

{% alert warning %}
Braze는 [데이터 보호 기술 지원]({{site.baseurl}}/dp-technical-assistance/)에 설명된 대로 Braze에서 삭제된 사용자의 이벤트 데이터를 자동으로 익명화합니다. 공유 데이터베이스 외부로 복사된 모든 데이터는 Braze가 더 이상 관리하지 않기 때문에 이 프로세스에 포함되지 않습니다.
{% endalert %}

## Copying all data to another Snowflake database

공유된 `BRAZE_RAW_EVENTS` 스키마에서 Snowflake의 다른 데이터베이스 및 스키마로 데이터를 복사하여 익명화되지 않은 데이터를 유지할 수 있습니다. 이렇게 하려면 다음 단계를 따르세요:

1. Snowflake 계정에서 `COPY_BRAZE_SHARE` 프로시저를 생성합니다. 이를 사용하여 Braze가 공유한 모든 데이터를 Snowflake 내 다른 데이터베이스 및 스키마로 복사합니다. 

{% raw %}
```sql
CREATE PROCEDURE COPY_BRAZE_SHARE(
    SOURCE_DATABASE STRING, -- Database name of the braze data share
    SOURCE_SCHEMA STRING, -- Schema name of the braze data share
    DESTINATION_DATABASE STRING, -- Name of the database to which you want to copy shared the data
    DESTINATION_SCHEMA STRING, -- Name of the schema to which you want to copy shared the data
    MAX_DATE DATE default DATEADD(year, -2, CURRENT_DATE()), -- Copy data on or before the maximum date default DATEADD(year, -2, CURRENT_DATE())
    TABLE_NAME_FILTER STRING default 'USERS_%' -- Filter to select table that will be unloaded, default to 'USER_%'
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
    
    -- Get the list of filtered table names
    table_query = f"""
        SELECT table_name 
        FROM {SOURCE_DATABASE}.INFORMATION_SCHEMA.TABLES
        WHERE TABLE_SCHEMA = '{SOURCE_SCHEMA}' AND table_name LIKE '{TABLE_NAME_FILTER}'
    """
    
    tables = session.sql(table_query).collect()
    
    -- Iterate through each table and copy data
    for row in tables:
        table_name = row['TABLE_NAME']

	 -- Skip archive tables
        if table_name.endswith('_ARCHIVED'):
            continue

        -- Check if the destination table exists
        check_table_query = f"""
            SELECT COUNT(*) as count
            FROM {DESTINATION_DATABASE}.INFORMATION_SCHEMA.TABLES
            WHERE TABLE_SCHEMA = '{DESTINATION_SCHEMA}' AND TABLE_NAME = '{table_name}'
        """
        table_exists = session.sql(check_table_query).collect()[0]['COUNT'] > 0

        if table_exists:
            -- Find the current, most recent `SF_CREATED_AT` in the existing table
            cur_max_date = None
            
            date_query = f"""
                SELECT MAX(SF_CREATED_AT) as CUR_MAX_DATE
                FROM {DESTINATION_DATABASE}.{DESTINATION_SCHEMA}.{table_name}
            """
            date_result = session.sql(date_query).collect()
            
            if date_result:
                cur_max_date = date_result[0]['CUR_MAX_DATE']
                
            if cur_max_date:
                -- If the destination table is not empty, only add data that is newer than `cur_max_date` and older than`MAX_DATE`
                copy_query = f"""
                    INSERT INTO {DESTINATION_DATABASE}.{DESTINATION_SCHEMA}.{table_name}
                    SELECT * FROM {SOURCE_DATABASE}.{SOURCE_SCHEMA}.{table_name}
                    WHERE SF_CREATED_AT <= '{MAX_DATE}'
                        AND SF_CREATED_AT > '{cur_max_date}'
                """
            else:
                -- If the destination table is empty, copy all data before `MAX_DATE`
                copy_query = f"""
                    INSERT INTO {DESTINATION_DATABASE}.{DESTINATION_SCHEMA}.{table_name}
                    SELECT * FROM {SOURCE_DATABASE}.{SOURCE_SCHEMA}.{table_name}
                    WHERE SF_CREATED_AT <= '{MAX_DATE}'
                """
        else:
            -- If the table doesn't exist, create it and copy data
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
    
    -- Return the results
    return session.create_dataframe(result, schema=['TABLE_NAME', 'SUCCESS', 'INFO'])
$$;
```
{% endraw %}

{: start="2"}
2\. 아래 명령 중 하나를 Snowflake 계정에서 실행하여 프로시저를 수행합니다.

{% tabs %}
{% tab 기본값 %}

기본적으로, 프로시저는 모든 `USERS_*` 이벤트 유형에 대해 2년 넘게 경과한 데이터를 백업합니다. 

{% raw %}
```sql
-- Copy all the rows that are two years or older in all the 'USERS_*' tables 
-- from 'SOURCE_DB'.'SOURCE_SCHEMA' to 'DEST_DB'.'DEST_SCHEMA'

CALL COPY_BRAZE_SHARE('SOURCE_DB', 'SOURCE_SCHEMA', 'DEST_DB', 'DEST_SCHEMA')
```
{% endraw %}
{% endtab %}
{% tab 필터링된 항목 %}

백업할 오래된 데이터를 선택하려면 필터를 지정하고, 선택한 이벤트 테이블만 백업하도록 테이블 이름 필터를 지정합니다. 

{% raw %}
```sql
-- Copy all the rows that are one year or older in all the 'USERS_BEHAVIORS_*' tables
-- from 'SOURCE_DB'.'SOURCE_SCHEMA' to 'DEST_DB'.'DEST_SCHEMA'

CALL COPY_BRAZE_SHARE('SOURCE_DB', 'SOURCE_SCHEMA', 'DEST_DB', 'DEST_SCHEMA', DATEADD(year, -1, CURRENT_DATE()), 'USERS_BEHAVIORS_%')
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
프로시저를 반복 실행해도 중복 레코드가 생성되지 않습니다. 이 프로시저는 최신 `SF_CREATED_AT`을 확인하고 그 이후의 데이터만 백업하기 때문입니다.
{% endalert %}

## Unloading data to stage

공유된 `BRAZE_RAW_EVENTS` 스키마에서 스테이지로 데이터를 언로드하여 익명화되지 않은 데이터를 유지할 수 있습니다. 이렇게 하려면 다음 단계를 따르세요:

1. `UNLOAD_BRAZE_SHARE` 프로시저를 생성합니다. 이를 사용하여 Braze에서 지정된 스테이지로 공유된 모든 데이터를 복사합니다.

{% raw %}
```sql
CREATE PROCEDURE UNLOAD_BRAZE_SHARE(
    SOURCE_DATABASE STRING, -- Database name of the braze data share
    SOURCE_SCHEMA STRING, -- Schema name of the braze data share
    STAGE_NAME STRING, -- Snowflake stage where the data will be unloaded
    MIN_DATE DATE, -- Copy data from this date (inclusive)
    MAX_DATE DATE, -- Copy data till this date (exclusive)
    TABLE_NAME_FILTER STRING default 'USERS_%' -- Filter to select table that will be unloaded, default to 'USER_%'
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
        
    -- Get list of tables
    table_query = f"""
    SELECT TABLE_NAME 
    FROM {DATABASE_NAME}.INFORMATION_SCHEMA.TABLES 
    WHERE TABLE_SCHEMA = '{SCHEMA_NAME}' AND TABLE_NAME LIKE '{TABLE_NAME_FILTER}'
    """
    tables = session.sql(table_query).collect()
    
    for table in tables:
        table_name = table['TABLE_NAME']

	 -- Skip archive tables
        if table_name.endswith('_ARCHIVED'):
            continue
        
        -- Create CSV file name
        csv_file_name = f"{table_name}_{MIN_DATE}_{MAX_DATE}.csv"
        
        -- Construct `COPY INTO` command with date filter
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
        
        -- Execute COPY INTO command
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
2\. 다음 명령어 중 하나를 실행하여 절차를 수행하십시오. 

{% tabs %}
{% tab 기본값 %}

기본적으로, 프로시저는 `USERS_` 접두사의 모든 테이블을 복사합니다.

{% raw %}
```sql
-- Create a Snowflake stage to store the file
create stage MY_EXPORT_STAGE;

-- Call the procedure 
-- to unload date between '2020-01-01' and '2021-01-01'
-- from tables with 'USERS_' prefix in 'DATABASE_NAME'.'SCHEMA'
CALL UNLOAD_BRAZE_SHARE('DATABASE_NAME', 'SCHEMA', 'MY_EXPORT_STAGE', '2020-01-01', 2021-01-01');

-- List the files that are unloaded
LIST @MY_EXPORT_STAGE;
```
{% endraw %}
{% endtab %}
{% tab 필터링된 항목 %}

절차에서 지정된 테이블만 언로드하도록 필터를 지정하십시오.

{% raw %}
```sql
-- Create a Snowflake stage to store the file
create stage MY_EXPORT_STAGE;

-- Unload date between '2020-01-01' and '2021-01-01'
-- from tables with 'USERS_BEHAVIORS_' prefix in 'DATABASE_NAME'.'SCHEMA'
CALL EXPORT_BRAZE_SHARE_TO_STAGE('DATABASE_NAME', 'SCHEMA', 'MY_EXPORT_STAGE', '2020-01-01', 2021-01-01', 'USERS_BEHAVIORS_%');

-- List the files that are unloaded 
LIST @MY_EXPORT_STAGE;
```
{% endraw %}
{% endtab %}
{% endtabs %}
