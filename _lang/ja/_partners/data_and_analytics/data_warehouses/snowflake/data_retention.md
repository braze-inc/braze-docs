---
nav_title: "データリテンション"
article_title: Snowflake データリテンション
page_order: 3
description: "このページでは、Brazeのリテンションポリシーが適用されている場合に、フルイベントデータを保持する方法について説明する。"
page_type: partner
search_tag: Partner
---

# Snowflake データリテンション

> Braze は、Snowflake に保存されている 2 年以上経過したすべてのイベントデータから個人識別情報 (PII) を匿名化して削除します。Snowflake データシェアリングを使用する場合、完全なイベントデータをご使用の環境に保持するには、リテンションポリシーが適用される前に Snowflake アカウントにコピーを保存します。

このページでは、匿名化されていないデータを保持する2つの方法を紹介する： 

- データを別のSnowflakeデータベースにコピーする
- ステージにデータをアンロードする

{% alert warning %}
「[データ保護技術支援]({{site.baseurl}}/dp-technical-assistance/)」で説明されているように、Braze は、Braze から削除されたユーザーのイベントデータを自動的に匿名化します。共有データベースの外部にコピーされたデータは、Brazeがもはや管理していないため、このプロセスには含まれない。
{% endalert %}

## すべてのデータを別のSnowflakeデータベースにコピーする

共有`BRAZE_RAW_EVENTS` スキーマから Snowflake の別のデータベースとスキーマにデータをコピーすることで、匿名化されていないデータを保持することができる。そのためには、以下の手順に従ってほしい：

1. Snowflakeアカウントで、プロシージャ`COPY_BRAZE_SHARE` を作成する。このプロシージャは、Brazeが共有するすべてのデータをSnowflake内の別のデータベースとスキーマにコピーするために使用される。 

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
2\.Snowflake アカウントで以下のコマンドのいずれかを実行して、プロシージャーを実行します。

{% tabs %}
{% tab デフォルト %}

デフォルトでは、すべての `USERS_*` イベントタイプについて、2年以上経過しているデータがバックアップされます。 

{% raw %}
```sql
-- Copy all the rows that are two years or older in all the 'USERS_*' tables 
-- from 'SOURCE_DB'.'SOURCE_SCHEMA' to 'DEST_DB'.'DEST_SCHEMA'

CALL COPY_BRAZE_SHARE('SOURCE_DB', 'SOURCE_SCHEMA', 'DEST_DB', 'DEST_SCHEMA')
```
{% endraw %}
{% endtab %}
{% tab フィルター付き %}

バックアップ対象の古いデータを選択するフィルターを指定し、選択されるイベントテーブルのみをバックアップするためのテーブル名フィルターを指定します。 

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
このプロシージャーは最新の `SF_CREATED_AT` をチェックし、それより新しいデータのみをバックアップするので、このプロシージャーを繰り返し実行しても、重複するレコードは作成されません。
{% endalert %}

## ステージへのデータのアンロード

共有`BRAZE_RAW_EVENTS` スキーマからステージにデータをアンロードすることで、匿名化されていないデータを保持することができる。そのためには、以下の手順に従ってほしい：

1. プロシージャー `UNLOAD_BRAZE_SHARE` を作成します。これは、Braze が共有するすべてのデータを、指定したステージにコピーする場合に使用されるプロシージャーです。

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
2\.以下のコマンドのいずれかを実行して、プロシージャーを実行します。 

{% tabs %}
{% tab デフォルト %}

デフォルトでは、`USERS_` 接頭辞を持つすべてのテーブルがコピーされます。

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
{% tab フィルター付き %}

プロシージャにフィルターを指定し、指定したテーブルのみをアンロードする。

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
