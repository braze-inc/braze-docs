---
nav_title: "Sample Queries"
page_order: 1
description: "This partner page offers some sample queries of possible use cases to reference when setting up your queries."
page_type: partner
---

# Sample Queries

>  This partner page offers some sample queries of possible use cases to reference when setting up your queries.

{% tabs %}
  {% tab Filter By Time%}
  
  A common query might be to filter events by time.
  
  You can filter them by the time of occurrence. Event tables are clustered by `time` which makes filtering by `time` performant.

```sql
-- find custom events that occurred after 04/15/2019 @ 7:02pm (UTC) i.e. timestamp=1555354920
SELECT *
FROM users_behaviors_customevent_shared
WHERE time > 1555354920
LIMIT 10;
```
  Or you can filter events by the time at which they were persisted in the Snowflake data warehouse by using `sf_created_at`. `sf_created_at` and `time` are not the same but are usually close, so this query should have similar performance characteristics

```sql
-- find custom events that arrived in Snowflake after time 04/15/2019 @ 7:02pm (UTC)
SELECT *
FROM users_behaviors_customevent_shared
WHERE sf_created_at > to_timestamp_ntz('2019-04-15 19:02:00')
LIMIT 10;
```
  {% endtab %}
  {% tab Querying Changelogs%}
  
Campaign names and Canvas names are not present in the events themselves. Instead, they are published in a changelog table. 

You can see campaign names for events related to a campaign by joining with the campaign changelog table using a query like

```sql
SELECT e.id, e.time, ccs.time, ccs.name, ccs.conversion_behaviors[e.conversion_behavior_index]
FROM USERS_CAMPAIGNS_CONVERSION_SHARED e
LEFT JOIN CHANGELOGS_CAMPAIGN_SHARED ccs
ON ccs.id = e.campaign_id
AND ccs.time < e.time
qualify row_number() over (partition by e.id ORDER BY ccs.time DESC) = 1;
```
Note:
- We are using Snowflake's [window](https://docs.snowflake.com/en/sql-reference/functions-analytic.html) functions here.
- The left join will ensure that events that were not related to a campaign will also be included.
- If you see events with `campaign_id`s but no campaign names then there is a possibility that the campaign was created with a name before Data Sharing existed as a product.
- You can see canvas names using a similar query, joining with the `CHANGELOGS_CANVAS_SHARED` table instead.

If you want to see both campaign and canvas names, you may have to use a sub-query as shown below.

```sql
SELECT campaign_join.*, canvas.name AS canvas_name
FROM 
(SELECT e.id AS event_id, e.external_user_id, e.time, e.user_id, e.device_id, e.sf_created_at,
    e.campaign_api_id, e.canvas_api_id, e.canvas_step_api_id, 
    campaign.name AS campaign_name
  FROM USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED AS e
  LEFT JOIN CHANGELOGS_CAMPAIGN_SHARED AS campaign ON campaign.id = e.campaign_id
  WHERE e.time >= 1574830800 AND e.time <= 1575176399
  qualify row_number() over (partition by e.id ORDER BY campaign.time DESC) = 1) AS campaign_join
LEFT JOIN CHANGELOGS_CANVAS_SHARED AS canvas ON canvas.id = campaign_join.canvas_id
qualify row_number() over (partition by campaign_join.event_id ORDER BY canvas.time DESC) = 1;
```
  {% endtab %}
  {% tab Push Funnel %}

  You can use this Push Funnel query to aggregate push sends raw event data, through to deliveries raw event data, through to opens raw event data. This query shows how all the tables should be joined since each raw event typically has a separate table.

```sql

SELECT
    COUNT(DISTINCT s."ID" ) AS "users_messages_pushnotification_send.push_sent",
    COALESCE((COUNT(DISTINCT s."ID" )),0)-COALESCE((COUNT(DISTINCT b."ID" )),0) AS "users_messages_pushnotification_send.push_delivered",
    COUNT(DISTINCT o."ID" ) AS "users_messages_pushnotification_open.push_opens"
FROM users_messages_pushnotification_send_shared AS s
LEFT JOIN USERS_MESSAGES_PUSHNOTIFICATION_OPEN_shared AS o ON (s."USER_ID")=(o."USER_ID")
    AND
    (s."DEVICE_ID")=(o."DEVICE_ID")
    AND
    ((s."MESSAGE_VARIATION_API_ID")=(o."MESSAGE_VARIATION_API_ID")
    OR
    (s."CANVAS_STEP_API_ID")=(o."CANVAS_STEP_API_ID"))
LEFT JOIN users_messages_pushnotification_bounce_shared AS b ON (s."USER_ID")=(b."USER_ID")
    AND
    (s."DEVICE_ID")=(b."DEVICE_ID")
    AND
    ((s."MESSAGE_VARIATION_API_ID")=(b."MESSAGE_VARIATION_API_ID")
    OR
    (s."CANVAS_STEP_API_ID")=(b."CANVAS_STEP_API_ID"))
LIMIT 500;
```

  {% endtab %}
  {% tab Email Cadence %}
You can use this daily Email Messaging Cadence query to analyze the time between emails that a user receives.

For example, if a user received two emails in one day, they would fall under `0 “days since last received”`. If they received one email on Monday and one on Tuesday, they would fall into the `1 “days since last received”` cohort.

```sql
WITH email_messaging_cadence AS (WITH deliveries AS
      (SELECT TO_TIMESTAMP(time) AS delivered_timestamp,
      email_address AS delivered_address,
      message_variation_api_id AS d_message_variation_api_id,
      canvas_step_api_id AS d_canvas_step_api_id,
      campaign_api_id AS d_campaign_api_id,
      canvas_api_id AS d_canvas_api_id,
      id AS delivered_id,
      rank() over (partition by delivered_address ORDER BY delivered_timestamp ASC) AS delivery_event,
      min(delivered_timestamp) over (partition by delivered_address ORDER BY delivered_timestamp ASC) AS first_delivered,
      datediff(day, lag(delivered_timestamp) over (partition by delivered_address ORDER BY delivered_timestamp ASC), delivered_timestamp) AS diff_days,
      datediff(week, lag(delivered_timestamp) over (partition by delivered_address ORDER BY delivered_timestamp ASC), delivered_timestamp) AS diff_weeks
      from USERS_MESSAGES_EMAIL_DELIVERY_SHARED GROUP BY 1,2,3,4,5,6,7),      opens AS
      (SELECT DISTINCT email_address AS open_address,
      message_variation_api_id AS o_message_variation_api_id,
      canvas_step_api_id AS o_canvas_step_api_id
      FROM USERS_MESSAGES_EMAIL_OPEN_SHARED),      clicks AS
      (SELECT DISTINCT email_address AS click_address,
      message_variation_api_id AS c_message_variation_api_id,
      canvas_step_api_id AS c_canvas_step_api_id
      FROM USERS_MESSAGES_EMAIL_CLICK_SHARED)      SELECT * FROM deliveries
      LEFT JOIN opens
      ON (deliveries.delivered_address)=(opens.open_address)
      AND ((deliveries.d_message_variation_api_id)=(opens.o_message_variation_api_id) OR (deliveries.d_canvas_step_api_id)=(opens.o_canvas_step_api_id))
      LEFT JOIN clicks
      ON (deliveries.delivered_address)=(clicks.click_address)
      AND ((deliveries.d_message_variation_api_id)=(clicks.c_message_variation_api_id) OR (deliveries.d_canvas_step_api_id)=(clicks.c_canvas_step_api_id))
      )
SELECT
    email_messaging_cadence."DIFF_DAYS"  AS "email_messaging_cadence.days_since_last_received",
    (count(distinct email_messaging_cadence."OPEN_ADDRESS", email_messaging_cadence."O_MESSAGE_VARIATION_API_ID")
      +count(distinct email_messaging_cadence."OPEN_ADDRESS", email_messaging_cadence."O_CANVAS_STEP_API_ID"))/(COUNT(DISTINCT email_messaging_cadence."DELIVERED_ID" ))  AS "email_messaging_cadence.unique_open_rate"
FROM email_messaging_cadenceGROUP BY 1
ORDER BY 1
LIMIT 500;
```

{% endtab %}
{% endtabs %}
