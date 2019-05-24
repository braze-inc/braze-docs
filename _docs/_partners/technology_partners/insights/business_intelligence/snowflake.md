---
nav_title: Snowflake
alias: /partners/snowflake/
---

# Snowflake

Summary of what Snowflake is and how we work together. Data-sharing!

## Use Cases
Similar to Currents, you can use your Snowflake
- Complex File Reports
- Attribution modeling
- Mapping raw event or user data to a CRM like Salesforce

## Requirements

|Requirement | Description |
|---|---|
| Snowflake Account |
| Braze App Group ID |

## Integration

If you're interested in this integration, reach out to your Braze Account or Customer Success Manager and ask to consult the Braze Business Intelligence Team on data-sharing with Snowflake. This will get the cogs going inside Braze. It will involve and update to your MSA.


## Usage/Visualization

Braze will send you some views.

You'll have access to historical, current, and future data dating from the beginning of when data was sent to Snowflake up until you choose not to utilize Snowflake anymore.

You can do whatever you want with it, but we recommend using it in conjunction with our Looker Blocks.

```json
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

Or this example, for Raw Events Data for open rate based on the spacing between emails that a user is sent.

```json
```WITH email_messaging_cadence AS (with deliveries as
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
LIMIT 500```
```


## Benchmarks

Braze also offers data sharing for our Benchmark data.

We will create a corresponding Looker Block so you can use Snowflake or Looker to join that data to their own data, perform what-if analysis, and other more flexible analytics.

“Sample_query”: <query_string> }],  //at least one required. Recommend 3-4

The initial set of top-level categories are: Financial, Health, Weather, Media, Transportation, Business, Cyber, Sports, Government, Lookup Tables, Demographics, Advertising, Local
For customer specific shares:

Email address to contact when a customer requests a share

In addition, please also provide us a high-res image of your logo. (Is this for benchmarks or for snowflake in general?)


## Data

The data you'll see in Snowflake is similar to what you'd see in currents.  
