---
nav_title: "User profile attributes"
article_title: User Attribute Views in Snowflake 
page_order: 10
page_type: partner
search_tag: Partner
---

# User profile attributes

> This page serves as a reference for the default and custom attribute views in Snowflake. There are three views for default attributes and three views for custom attributes, each designed for a specific use case with its own performance considerations.

{% alert important %} 
User profile attributes are currently in beta for Snowflake Data Sharing customers. If you're using Snowflake Data Sharing and would like access to this beta, contact your customer success manager or Braze Support.
{% endalert %}

# Available views

<table>
  <thead>
    <tr>
      <th>Type</th>
      <th>View</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Default attribute</td>
      <td><code>USER_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>User profile snapshots</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Real time user profiles</td>
    </tr>
    <tr>
      <td><code>USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>Historical change logs</td>
    </tr>
    <tr>
      <td rowspan="3">Custom attribute</td>
      <td><code>USER_CUSTOM_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>User profile snapshots</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED</code></td>
      <td>Real time user profiles</td>
    </tr>
    <tr>
      <td><code>USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>Historical change logs</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## User profile snapshots

These views provide periodic snapshots of user profile attributes. The data is delayed by up to 12 hours, making it useful for queries that don't require real-time updates. 

 - `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`
 - `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`  

### `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`

#### Schema

| Column name     | Data type     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE` | VARCHAR |
| `DOB` | VARCHAR |
| `TIME_ZONE` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}


### `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`

#### Schema

| Column name     | Data type     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `CUSTOM_ATTRIBUTES` | VARIANT |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}  

### User profile snapshots - usage notes

* Provides a snapshot of user attributes with up to a **12-hour delay**.
* Performs well for queries that don't require real-time accuracy.
* Faster query execution, particularly when filtering on attributes other than `USER_ID`.
* **Limitation:** Data is not up to date in real time.

## Real time user profile views

These views provides near real-time updates on user profile attributes, with data delayed by up to 10 minutes after an update occurs in Braze.

  - `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` 
  - `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` 

### `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`
#### Schema

| Column name     | Data type     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_LTZ |
| `EXTERNAL_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE` | VARCHAR |
| `DOB` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `TIME_ZONE` | VARCHAR |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

### `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`
#### Schema

| Column name     | Data type     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `APP_ID` | VARCHAR |
| `CUSTOM_ATTRIBUTES` | OBJECT |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}


### Real time user profile views - usage notes

* Provides up-to-date user attributes with minimal delay (~10 minutes).
* Useful for real-time analysis and scenarios where recent data is required.
* **Performance considerations:**
    * Queries on individual users are faster (under a minute using a large warehouse).
    * Queries without USER_ID filters require aggregation across all users, leading to significantly longer execution times.
    * Queries on a large dataset (such as over 100 million users) may take many minutes.

## Historical change logs

These views store historical change logs of user attributes, capturing changes with a 12-hour granularity.

- `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` 
- `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED` 

### `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`
#### Schema

| Column name     | Data type     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `TIME` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE` | VARCHAR |
| `DOB` | VARCHAR |
| `TIME_ZONE` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `EFF_DT` | TIMESTAMP_NTZ |
| `END_DT` | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

### `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`
#### Schema

| Column name     | Data type     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `TIME` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `CUSTOM_ATTRIBUTES` | VARIANT |
| `EFF_DT` | TIMESTAMP_NTZ |
| `END_DT` | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

### Historical change logs - usage notes

* Provides a record of historical changes to user attributes.
* Data is snapshotted every 12 hours, meaning multiple updates in this window are combined into a single record. Individual changes within this period are not separately retained.
* `EFF_DT` and `END_DT` mark the start and end of a user’s attribute state.

# Best practices

## Recommended query usage

| Use case                                               | Recommended views                                   | Notes                                                                 |
|--------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|
| **General queries** that do not require recent updates | `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` and `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`               | Fast execution, with data up to 12 hours old.                          |
| Queries requiring the **latest user attributes**       | `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` and `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` | Provides near real-time updates but can be slower for large datasets. |
| **Historical tracking** of attribute changes           | `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` and `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`      | Stores attribute changes with 12-hour granularity.                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation}

## Performance considerations

* Queries on `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` or `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` should return in under 10 seconds for large datasets (~1 billion users) on a large warehouse.
* Queries on `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` or `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED ` for a single user return in under a minute but scale poorly without `USER_ID` filtering.
* Queries on over 100 million users in `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` or `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` may take several minutes due to per-user aggregation.


