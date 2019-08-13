---
nav_title: Snowflake
alias: /partners/snowflake/
---

# Snowflake Secure Data Sharing

Snowflake is a purpose-built SQL cloud data warehouse for all of your data and all of your users. With Snowflake's unique and patented architecture it's easy to amass all of your data, enable rapid analytics, and derive data-driven insights for all of your users.

Braze leverages Snowflake’s Data Exchange to build a presence, find new customers, and expand reach through the ever-growing Snowflake customer base.

Learn more about this partnership [here](https://www.braze.com/perspectives/article/snowflake-partner-announcement)!

### What is Data Sharing?

Data Sharing allows Braze to allow you secure access to data on our Snowflake portal without worrying about workflow friction or slowdown, failure points, and unnecessary costs that come with typical data provider relationships.

## Integration

If you're interested in this integration, reach out to your Braze Account or Customer Success Manager and ask them to consult Braze Data Strategy Services on Secure Data Sharing with Snowflake. This will get the cogs going inside Braze and we'll have your views set up in no time!

{% alert important %}
You must have an account with Snowflake to use the Data Sharing Services.
{% endalert %}

## Usage & Visualization

Similar to Currents, you can use your Secure Snowflake Data Sharing to...

-   Create complex reports,
-   Perform attribution modeling,
-   Secure sharing within your own company,
-   Map raw event or user data to a CRM (like Salesforce)...

And so much more!

After Braze sets up your views on Snowflake and grants you the access you need, we will send you some views. This data is similar to what you'd see in [Currents]({{ site.baseurl }}/partners/braze_currents/about/).  

You'll have access to historical, current, and future data dating from the beginning of when that data was sent to Snowflake up until you choose not to utilize Snowflake anymore.

You can do whatever you want with the data, but we recommend using it in conjunction with our Looker Blocks.

### Query Samples

Below, you can see query samples for two possible use cases.

{% tabs %}
  {% tab Push Funnel %}

  You can use this Push Funnel query to aggregate push sends raw event data, through to deliveries raw event data, through to opens raw event data. This query shows how all the tables should be joined, since each raw event typically has a separate table.

```sql
SELECT
    COUNT(DISTINCT users_messages_pushnotification_send."ID" ) AS "users_messages_pushnotification_send.push_sent",
    COALESCE((COUNT(DISTINCT users_messages_pushnotification_send."ID" )),0)-COALESCE((COUNT(DISTINCT users_messages_pushnotification_bounce."ID" )),0) AS "users_messages_pushnotification_send.push_delivered",
    COUNT(DISTINCT users_messages_pushnotification_open."ID" ) AS "users_messages_pushnotification_open.push_opens"
FROM USERS_MESSAGES_PUSHNOTIFICATION_SEND  AS users_messages_pushnotification_send
LEFT JOIN USERS_MESSAGES_PUSHNOTIFICATION_OPEN  AS users_messages_pushnotification_open ON (users_messages_pushnotification_send."USER_ID")=(users_messages_pushnotification_open."USER_ID")
            AND
            (users_messages_pushnotification_send."DEVICE_ID")=(users_messages_pushnotification_open."DEVICE_ID")
            AND
            ((users_messages_pushnotification_send."MESSAGE_VARIATION_ID")=(users_messages_pushnotification_open."MESSAGE_VARIATION_ID")
            OR
            (users_messages_pushnotification_send."CANVAS_STEP_ID")=(users_messages_pushnotification_open."CANVAS_STEP_ID"))
LEFT JOIN USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE  AS users_messages_pushnotification_bounce ON (users_messages_pushnotification_send."USER_ID")=(users_messages_pushnotification_bounce."USER_ID")
            AND
            (users_messages_pushnotification_send."DEVICE_ID")=(users_messages_pushnotification_bounce."DEVICE_ID")
            AND
            ((users_messages_pushnotification_send."MESSAGE_VARIATION_ID")=(users_messages_pushnotification_bounce."MESSAGE_VARIATION_ID")
            OR
            (users_messages_pushnotification_send."CANVAS_STEP_ID")=(users_messages_pushnotification_bounce."CANVAS_STEP_ID"))

LIMIT 500
```

  {% endtab %}
  {% tab Email Cadence %}
You can use this daily Email Messaging Cadence query to analyze the time between emails that a user receives.

For example, if a user received two emails in one day, they would fall under `0 “days since last received”`. If they received one email on Monday and one on Tuesday, they would fall into the `1 “days since last received”` cohort.

```sql
WITH email_messaging_cadence AS (with deliveries as
      (select TO_TIMESTAMP(time) AS delivered_timestamp,
      email_address AS delivered_address,
      message_variation_id as d_message_variation_id,
      canvas_step_id as d_canvas_step_id,
      campaign_name as d_campaign_name,
      canvas_name as d_canvas_name,
      id as delivered_id,
      rank() over (partition by delivered_address order by delivered_timestamp asc) as delivery_event,
      min(delivered_timestamp) over (partition by delivered_address order by delivered_timestamp asc) as first_delivered,
      datediff(day, lag(delivered_timestamp) over (partition by delivered_address order by delivered_timestamp asc), delivered_timestamp) as diff_days,
      datediff(week, lag(delivered_timestamp) over (partition by delivered_address order by delivered_timestamp asc), delivered_timestamp) as diff_weeks
      from PUBLIC.USERS_MESSAGES_EMAIL_DELIVERY group by 1,2,3,4,5,6,7),

      opens as
      (select distinct email_address as open_address,
      message_variation_id as o_message_variation_id,
      canvas_step_id as o_canvas_step_id
      FROM PUBLIC.USERS_MESSAGES_EMAIL_OPEN),

      clicks as
      (select distinct email_address as click_address,
      message_variation_id as c_message_variation_id,
      canvas_step_id as c_canvas_step_id
      FROM PUBLIC.USERS_MESSAGES_EMAIL_CLICK)

      SELECT * FROM deliveries
      LEFT JOIN opens
      ON (deliveries.delivered_address)=(opens.open_address)
      AND ((deliveries.d_message_variation_id)=(opens.o_message_variation_id) OR (deliveries.d_canvas_step_id)=(opens.o_canvas_step_id))
      LEFT JOIN clicks
      ON (deliveries.delivered_address)=(clicks.click_address)
      AND ((deliveries.d_message_variation_id)=(clicks.c_message_variation_id) OR (deliveries.d_canvas_step_id)=(clicks.c_canvas_step_id))
      )
SELECT
    email_messaging_cadence."DIFF_DAYS"  AS "email_messaging_cadence.days_since_last_received",
    (count(distinct email_messaging_cadence."OPEN_ADDRESS", email_messaging_cadence."O_MESSAGE_VARIATION_ID")
      +count(distinct email_messaging_cadence."OPEN_ADDRESS", email_messaging_cadence."O_CANVAS_STEP_ID"))/(COUNT(DISTINCT email_messaging_cadence."DELIVERED_ID" ))  AS "email_messaging_cadence.unique_open_rate"
FROM email_messaging_cadence

GROUP BY 1
ORDER BY 1
LIMIT 500
```

{% endtab %}
{% tab Email Clicks %}

You can use this Email Clicks query to analyze the interactions with specific emails in your Braze Campaigns and Canvases.

**Set Up this Query**
Create a database for `BRAZE`, then create database if none exists for `BRAZE_CURRENTS;`:

```sql
use schema BRAZE_CURRENTS.public;

create or replace stage braze_currents.public.braze_data
url='s3://tl-braze/'
credentials = (AWS_KEY_ID = 'XXXXXXXXX' AWS_SECRET_KEY = 'YYYYYY' );

create file format braze_currents.public.currents_avro type = 'avro' compression = 'auto';

alter stage braze_currents.public.braze_data set file_format = braze_currents.public.currents_avro;

show stages;
```

_Use the following command to create your table:_

```sql
CREATE TABLE
  braze_currents.public.users_messages_email_click (
    id STRING,
    user_id STRING,
    external_user_id STRING,
    time INT,
    timezone STRING,
    campaign_id STRING,
    campaign_name STRING,
    message_variation_id STRING,
    canvas_id STRING,
    canvas_name STRING,
    canvas_variation_id STRING,
    canvas_step_id STRING,
    send_id STRING,
    dispatch_id STRING,
    email_address STRING,
    url STRING,
    sending_ip STRING,
    user_agent STRING
  );
```

_Use the following command to create or replace your pipe:_

```sql
CREATE OR REPLACE PIPE
  pipe_users_messages_email_click
    auto_ingest=true AS

COPY INTO
  braze_currents.public.users_messages_email_click
  FROM
  (select
    $1:id::STRING,
    $1:user_id::STRING,
    $1:external_user_id::STRING,
    $1:time::INT,
    $1:timezone::STRING,
    $1:campaign_id::STRING,
    $1:campaign_name::STRING,
    $1:message_variation_id::STRING,
    $1:canvas_id::STRING,
    $1:canvas_name::STRING,
    $1:canvas_variation_id::STRING,
    $1:canvas_step_id::STRING,
    $1:send_id::STRING,
    $1:dispatch_id::STRING,
    $1:email_address::STRING,
    $1:url::STRING,
    $1:sending_ip::STRING,
    $1:user_agent::STRING

    FROM
    @braze_currents.public.braze_data/currents/dataexport.prod-03.S3.integration.YOUR_INTEGRATION_ID_HERE/event_type=users.messages.email.click/);

show pipes;
```

**Do More with this Query Example**

Copy the `notification_channel` from the output of the command above and use that when configuring S3 bucket notifications.

Manually sync from S3 to Snowflake for the pipe name given below:

```sql
ALTER PIPE
  pipe_users_messages_email_click
  refresh ;
```

Check the pipe status, which will show when the message was forwarded from S3 into Snowflake.

```sql
SELECT
  SYSTEM$PIPE_STATUS(
    'pipe_users_messages_email_click'
  )
```

Finally, show the copy history for the table by selecting `*` from

```sql
table(braze_currents.information_schema.copy_history(table_name=>'users_messages_email_click', start_time=> dateadd(hours, -1, current_timestamp())));
```

{% endtab %}
{% endtabs %}

## Braze Benchmarks

Braze Benchmarks will allow Braze prospects and  customers alike to see how they compare to top players in their industry by comparing their metrics against Braze's industry benchmarks.

We created a [Data Tool for Braze Benchmarks](https://www.braze.com/perspectives/benchmarks) so you can view a selection of the data, outside the Snowflake interface.

The initial industries are: Delivery Services, Ecommerce, Education, Entertainment, Finance, Gaming, Health, Lifestyle, Restaurants, Retail, Technology, Transportation, and Travel.

Our benchmarking data will also be available directly in the Snowflake Data Exchange.
