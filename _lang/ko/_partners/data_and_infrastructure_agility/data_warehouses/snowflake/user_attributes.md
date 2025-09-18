---
nav_title: "사용자 프로필 속성"
article_title: User Attribute Views in Snowflake 
page_order: 10
page_type: partner
search_tag: Partner
---

# Default user profile attributes

> This page serves as a reference for the default attribute views in Snowflake. There are three views, each designed for a specific use case with its own performance considerations.

{% alert important %}
User profile attributes are currently in beta for Snowflake Data Sharing customers. If you're using Snowflake Data Sharing and would like access to this beta, contact your customer success manager or Braze Support.
{% endalert %}

## Available views

- `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`  
- `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` 
- `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` 

### `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`

This view provides a periodic snapshot of user profile default attributes. The data is delayed by up to 8 hours, making it useful for queries that don't require real-time updates.

#### 스키마

| Column name     | 데이터 유형     |
|-----------------|---------------|
| `APP_GROUP_ID`  | VARCHAR       |
| `USER_ID`       | VARCHAR       |
| `TIME`          | 번호        |
| `UPDATE_SOURCE` | VARCHAR       |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID`   | VARCHAR       |
| `FIRST_NAME`    | VARCHAR       |
| `LAST_NAME`     | VARCHAR       |
| `EMAIL`         | VARCHAR       |
| `GENDER`        | VARCHAR       |
| `PHONE`         | VARCHAR       |
| `DOB`           | VARCHAR       |
| `TIME_ZONE`     | VARCHAR       |
| `HOME_CITY`     | VARCHAR       |
| `COUNTRY`       | VARCHAR       |
| `LANGUAGE`      | VARCHAR       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

#### Usage notes

* Provides a snapshot of user attributes with up to an **8-hour delay**.
* Performs well for queries that don't require real-time accuracy.
* Faster query execution, particularly when filtering on attributes other than `USER_ID`.
* **Limitation:** Data is not up to date in real time.

### `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`

This view provides near real-time updates on user profile attributes, with data delayed by up to 10 minutes after an update occurs in Braze.

#### 스키마

| Column name     | 데이터 유형     |
|-----------------|---------------|
| `APP_GROUP_ID`  | VARCHAR       |
| `USER_ID`       | VARCHAR       |
| `TIME`          | 번호        |
| `UPDATE_SOURCE` | VARCHAR       |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID`   | VARCHAR       |
| `FIRST_NAME`    | VARCHAR       |
| `LAST_NAME`     | VARCHAR       |
| `EMAIL`         | VARCHAR       |
| `GENDER`        | VARCHAR       |
| `PHONE`         | VARCHAR       |
| `DOB`           | VARCHAR       |
| `TIME_ZONE`     | VARCHAR       |
| `HOME_CITY`     | VARCHAR       |
| `COUNTRY`       | VARCHAR       |
| `LANGUAGE`      | VARCHAR       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

#### Usage notes

* Provides up-to-date user attributes with minimal delay (~10 minutes).
* Useful for real-time analysis and scenarios where recent data is required.
* **Performance considerations:**
    * Queries on individual users are faster (under a minute using a large warehouse).
    * Queries without USER_ID filters require aggregation across all users, leading to significantly longer execution times.
    * Queries on a large dataset (such as over 100 million users) may take many minutes.

### `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`

This view stores historical change logs of user attributes, capturing changes with an 8-hour granularity.

#### 스키마

| Column name     | 데이터 유형     |
|-----------------|---------------|
| `APP_GROUP_ID`  | VARCHAR       |
| `USER_ID`       | VARCHAR       |
| `TIME`          | 번호        |
| `UPDATE_SOURCE` | VARCHAR       |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID`   | VARCHAR       |
| `FIRST_NAME`    | VARCHAR       |
| `LAST_NAME`     | VARCHAR       |
| `EMAIL`         | VARCHAR       |
| `GENDER`        | VARCHAR       |
| `PHONE`         | VARCHAR       |
| `DOB`           | VARCHAR       |
| `TIME_ZONE`     | VARCHAR       |
| `HOME_CITY`     | VARCHAR       |
| `COUNTRY`       | VARCHAR       |
| `LANGUAGE`      | VARCHAR       |
| `EFF_DT`        | TIMESTAMP_NTZ |
| `END_DT`        | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

#### Usage notes

* Provides a record of historical changes to user attributes.
* Data is snapshotted every eight hours, meaning multiple updates in this window are combined into a single record. Individual changes within this period are not separately retained.
* `EFF_DT` and `END_DT` mark the start and end of a user’s attribute state.

## Best practices

### Recommended query usage

| 사용 사례                                               | Recommended view                                   | 참고                                                                 |
|--------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|
| **General queries** that do not require recent updates | `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`              | Fast execution, with data up to 8 hours old.                          |
| Queries requiring the **latest user attributes**       | `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` | Provides near real-time updates but can be slower for large datasets. |
| **Historical tracking** of attribute changes           | `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`      | Stores attribute changes with 8-hour granularity.                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation}

### Performance considerations

* Queries on `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` should return in under 10 seconds for large datasets (~1 billion users) on a large warehouse.
* Queries on `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` for a single user return in under a minute but scale poorly without `USER_ID` filtering.
* Queries on over 100 million users in `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` may take several minutes due to per-user aggregation.


