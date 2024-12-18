---
nav_title: "샘플 쿼리"
article_title: Snowflake 샘플 쿼리
page_order: 1
description: "이 파트너 페이지에서는 Snowflake 쿼리를 설정할 때 참조할 수 있는 몇 가지 사용 사례의 샘플 쿼리를 제공합니다."
page_type: partner
search_tag: Partner

---

# 샘플 쿼리

> 이 파트너 페이지에서는 쿼리를 설정할 때 참조할 수 있는 몇 가지 사용 사례의 샘플 쿼리를 제공합니다.

{% tabs %}
{% tab 시간으로 필터링%}

일반적인 쿼리는 시간별로 이벤트를 필터링하는 것일 수 있습니다.

발생 시간별로 필터링할 수 있습니다. 이벤트 테이블은 `time`에 의해 클러스터링되므로 `time`으로 필터링하는 것이 적합합니다.
```sql
-- find custom events that occurred after 04/15/2019 @ 7:02pm (UTC) i.e., timestamp=1555354920
SELECT *
FROM users_behaviors_customevent_shared
WHERE time > 1555354920
LIMIT 10;
```
`sf_created_at`을 사용하여 Snowflake 데이터 웨어하우스에서 지속되는 시간을 기준으로 이벤트를 필터링할 수도 있습니다. `sf_created_at` 및 `time`은 동일하지는 않지만 일반적으로 비슷하므로 이 쿼리의 성능 특성도 비슷합니다.
```sql
-- find custom events that arrived in Snowflake after time 04/15/2019 @ 7:02pm (UTC)
SELECT *
FROM users_behaviors_customevent_shared
WHERE sf_created_at > to_timestamp_ntz('2019-04-15 19:02:00')
LIMIT 10;
```
{% alert note %}
`sf_created_at`의 값은 `Nov 15th, 2019 9:31 pm UTC` 이후에 지속되는 이벤트에 대해서만 신뢰할 수 있습니다.
{% endalert %}
{% endtab %}

{% tab 변경 로그 쿼리%}
  
캠페인 이름과 캔버스 이름은 이벤트 자체에 표시되지 않습니다. 대신 변경 로그 테이블에 게시됩니다. 

다음과 같은 쿼리를 사용하여 캠페인 변경 로그 테이블에 조인하면 캠페인과 관련된 이벤트의 캠페인 이름을 확인할 수 있습니다:

```sql
SELECT event.id, event.time, ccs.time, ccs.name, ccs.conversion_behaviors[event.conversion_behavior_index]
FROM USERS_CAMPAIGNS_CONVERSION_SHARED event
LEFT JOIN CHANGELOGS_CAMPAIGN_SHARED ccs
ON ccs.id = event.campaign_id
AND ccs.time < event.time
qualify row_number() over (partition by event.id ORDER BY ccs.time DESC) = 1;
```
주의해야 할 몇 가지 중요한 사항은 다음과 같습니다:
- 여기서는 눈송이의 [창](https://docs.snowflake.com/en/sql-reference/functions-analytic.html) 기능이 사용됩니다.
- 왼쪽으로 조인하면 캠페인과 관련이 없는 이벤트도 포함될 수 있습니다.
- `campaign_id`는 있지만 캠페인 이름은 없는 이벤트가 표시되는 경우 데이터 공유가 제품으로 존재하기 전에 이름과 함께 캠페인을 생성했을 수 있습니다.
- 대신 `CHANGELOGS_CANVAS_SHARED` 테이블과 조인하여 유사한 쿼리를 사용하여 캔버스 이름을 확인할 수 있습니다.

캠페인과 캔버스 이름을 모두 보려면 다음 하위 쿼리를 사용해야 할 수 있습니다:
```sql
SELECT campaign_join.*, canvas.name AS canvas_name
FROM 
(SELECT e.id AS event_id, e.external_user_id, e.time, e.user_id, e.device_id, e.sf_created_at,
    e.campaign_api_id, e.canvas_id, e.canvas_step_api_id, 
    campaign.name AS campaign_name
  FROM USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED AS e
  LEFT JOIN CHANGELOGS_CAMPAIGN_SHARED AS campaign ON campaign.id = e.campaign_id
  WHERE e.time >= 1574830800 AND e.time <= 1575176399
  qualify row_number() over (partition by e.id ORDER BY campaign.time DESC) = 1) AS campaign_join
LEFT JOIN CHANGELOGS_CANVAS_SHARED AS Canvas ON canvas.id = campaign_join.canvas_id
qualify row_number() over (partition by campaign_join.event_id ORDER BY canvas.time DESC) = 1;
```
{% endtab %}
{% tab 푸시 퍼널 %}

이 푸시 퍼널 쿼리를 사용하여 푸시 전송 원시 이벤트 데이터부터 전달 원시 이벤트 데이터, 열람 원시 이벤트 데이터까지 집계할 수 있습니다. 일반적으로 각 원시 이벤트에 별도의 테이블이 있으므로 이 쿼리는 모든 테이블을 조인하는 방법을 보여줍니다.

```sql

SELECT
    COUNT(DISTINCT send."ID" ) AS "users_messages_pushnotification_send.push_sent",
    COALESCE((COUNT(DISTINCT send."ID" )),0)-COALESCE((COUNT(DISTINCT bounce."ID" )),0) AS "users_messages_pushnotification_send.push_delivered",
    COUNT(DISTINCT open."ID" ) AS "users_messages_pushnotification_open.push_opens"
FROM users_messages_pushnotification_send_shared AS send
LEFT JOIN USERS_MESSAGES_PUSHNOTIFICATION_OPEN_shared AS open ON (send."USER_ID")=(open."USER_ID")
    AND
    (send."DEVICE_ID")=(open."DEVICE_ID")
    AND
    ((send."MESSAGE_VARIATION_API_ID")=(open."MESSAGE_VARIATION_API_ID")
    OR
    (send."CANVAS_STEP_API_ID")=(open."CANVAS_STEP_API_ID"))
LEFT JOIN users_messages_pushnotification_bounce_shared AS bounce ON (send."USER_ID")=(bounce."USER_ID")
    AND
    (send."DEVICE_ID")=(bounce."DEVICE_ID")
    AND
    ((send."MESSAGE_VARIATION_API_ID")=(bounce."MESSAGE_VARIATION_API_ID")
    OR
    (send."CANVAS_STEP_API_ID")=(bounce."CANVAS_STEP_API_ID"))
LIMIT 500;
```

{% endtab %}
{% tab 이메일 주기 %}
이 일일 이메일 메시징 주기 쿼리를 사용하여 사용자가 수신하는 이메일 사이의 시간을 분석할 수 있습니다.

예를 들어 사용자가 하루에 두 개의 이메일을 받았다면 `0 "days since last received"`에 해당됩니다. 월요일에 한 번, 화요일에 한 번 이메일을 받았다면 `1 "days since last received"` 코호트에 속합니다.

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
FROM email_messaging_cadence GROUP BY 1
ORDER BY 1
LIMIT 500;
```
{% endtab %}
{% tab 고유 이메일 클릭 수 %}

이 고유 이메일 클릭 수 쿼리를 사용하여 주어진 기간 고유 이메일 클릭 수를 분석할 수 있습니다. 이를 계산하는 알고리즘은 다음과 같습니다:
  1. 키별로 이벤트를 분할합니다(`app_group_id`, `message_variation_id`, `dispatch_id`, `email_address`).
  2. 각 파티션에서 시간별로 이벤트를 정렬합니다. 첫 번째 이벤트는 항상 고유한 이벤트입니다.
  3. 모든 후속 이벤트는 이전 이벤트가 발생한 후 7일 넘게 경과한 경우 고유 이벤트로 간주합니다.
  
이를 위해 Snowflake의 [윈도우 함수](https://docs.snowflake.com/en/sql-reference/functions-analytic.html)를 사용할 수 있습니다. 다음 쿼리는 지난 365일 동안 모든 이메일 클릭 수를 제공하며 `is_unique` 열에 고유한 이벤트를 표시합니다.
  
```sql
SELECT id, app_group_id, message_variation_api_id, dispatch_id, email_address, time,
  ROW_NUMBER()       OVER (PARTITION BY app_group_id, message_variation_api_id, dispatch_id, email_address order by time) row_number,
  LAG(time, 1, time) OVER (PARTITION BY app_group_id, message_variation_api_id, dispatch_id, email_address order by time) previous_time,
  time - previous_time AS diff,
  IFF(row_number = 1, true, IFF(diff >= 7*24*3600, true, false)) AS is_unique
FROM USERS_MESSAGES_EMAIL_CLICK_SHARED
WHERE
  time < DATE_PART('EPOCH_SECOND', TO_TIMESTAMP(CURRENT_TIMESTAMP())) 
  AND time > DATE_PART('EPOCH_SECOND', TO_TIMESTAMP(CURRENT_TIMESTAMP())) - 365*24*3600; 
```

고유 이벤트만 보려면 `QUALIFY` 절을 사용하세요:
```sql
SELECT id, app_group_id, message_variation_api_id, dispatch_id, email_address, time,
  ROW_NUMBER()       OVER (PARTITION BY app_group_id, message_variation_api_id, dispatch_id, email_address order by time) row_number,
  LAG(time, 1, time) OVER (PARTITION BY app_group_id, message_variation_api_id, dispatch_id, email_address order by time) previous_time,
  time - previous_time AS diff,
  IFF(row_number = 1, true, IFF(diff >= 7*24*3600, true, false)) AS is_unique
FROM USERS_MESSAGES_EMAIL_CLICK_SHARED
WHERE
  time < DATE_PART('EPOCH_SECOND', TO_TIMESTAMP(CURRENT_TIMESTAMP())) 
  AND time > DATE_PART('EPOCH_SECOND', TO_TIMESTAMP(CURRENT_TIMESTAMP())) - 365*24*3600
QUALIFY is_unique = true;
```
이메일 주소별로 그룹화된 고유 이벤트 수를 자세히 보려면 다음을 수행합니다.
```sql
WITH unique_events AS(
  SELECT id, app_group_id, message_variation_api_id, dispatch_id, email_address, time,
  ROW_NUMBER()       OVER (PARTITION BY app_group_id, message_variation_api_id, dispatch_id, email_address order by time) row_number,
  LAG(time, 1, time) OVER (PARTITION BY app_group_id, message_variation_api_id, dispatch_id, email_address order by time) previous_time,
  time - previous_time AS diff,
  IFF(row_number = 1, true, iff(diff >= 7*24*3600, true, false)) AS is_unique
FROM USERS_MESSAGES_EMAIL_CLICK_SHARED
WHERE
  time < DATE_PART('EPOCH_SECOND', TO_TIMESTAMP(CURRENT_TIMESTAMP())) 
  AND time > DATE_PART('EPOCH_SECOND', TO_TIMESTAMP(CURRENT_TIMESTAMP())) - 365*24*3600
QUALIFY is_unique = true) 
SELECT email_address, count(*) AS count
FROM unique_events
GROUP BY email_address;
```
{% endtab %}
{% endtabs %}
