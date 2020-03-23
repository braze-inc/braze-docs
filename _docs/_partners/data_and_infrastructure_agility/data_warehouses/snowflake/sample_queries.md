---
nav_title: "Sample Queries"
page_order: 1
description: "This partner page offers some sample queries of possible use cases to reference when setting up your queries."
page_type: partner
---

# Sample Queries

>  This partner page offers some sample queries of possible use cases to reference when setting up your queries.

{% tabs %}
  {% tab Push Funnel %}

  You can use this Push Funnel query to aggregate push sends raw event data, through to deliveries raw event data, through to opens raw event data. This query shows how all the tables should be joined, since each raw event typically has a separate table.

```sql

SELECT
    COUNT(DISTINCT users_messages_pushnotification_send_non_pii_shared."ID" ) AS "users_messages_pushnotification_send.push_sent",
    COALESCE((COUNT(DISTINCT users_messages_pushnotification_send_non_pii_shared."ID" )),0)-COALESCE((COUNT(DISTINCT users_messages_pushnotification_bounce_non_pii_shared."ID" )),0) AS "users_messages_pushnotification_send.push_delivered",
    COUNT(DISTINCT users_messages_pushnotification_open_non_pii_shared."ID" ) AS "users_messages_pushnotification_open.push_opens"
FROM USERS_MESSAGES_PUSHNOTIFICATION_SEND_NON_pii_shared AS users_messages_pushnotification_send_non_pii_shared
LEFT JOIN USERS_MESSAGES_PUSHNOTIFICATION_OPEN_NON_pii_shared AS users_messages_pushnotification_open_non_pii_shared ON (users_messages_pushnotification_send_non_pii_shared."USER_ID")=(users_messages_pushnotification_open_non_pii_shared."USER_ID")
    AND
    (users_messages_pushnotification_send_non_pii_shared."DEVICE_ID")=(users_messages_pushnotification_open_non_pii_shared."DEVICE_ID")
    AND
    ((users_messages_pushnotification_send_non_pii_shared."MESSAGE_VARIATION_API_ID")=(users_messages_pushnotification_open_non_pii_shared."MESSAGE_VARIATION_API_ID")
    OR
    (users_messages_pushnotification_send_non_pii_shared."CANVAS_STEP_API_ID")=(users_messages_pushnotification_open_non_pii_shared."CANVAS_STEP_API_ID"))
LEFT JOIN USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_NON_pii_shared AS users_messages_pushnotification_bounce_NON_pii_shared ON (users_messages_pushnotification_send_NON_pii_shared."USER_ID")=(users_messages_pushnotification_bounce_NON_pii_shared."USER_ID")
    AND
    (users_messages_pushnotification_send_non_pii_shared."DEVICE_ID")=(users_messages_pushnotification_bounce_non_pii_shared."DEVICE_ID")
    AND
    ((users_messages_pushnotification_send_non_pii_shared."MESSAGE_VARIATION_API_ID")=(users_messages_pushnotification_bounce_non_pii_shared."MESSAGE_VARIATION_API_ID")
    OR
    (users_messages_pushnotification_send_non_pii_shared."CANVAS_STEP_API_ID")=(users_messages_pushnotification_bounce_non_pii_shared."CANVAS_STEP_API_ID"))
LIMIT 500;
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
{% endtabs %}
