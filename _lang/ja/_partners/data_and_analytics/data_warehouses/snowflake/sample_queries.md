---
nav_title: "サンプルクエリ"
article_title: Snowflake サンプルクエリ
page_order: 1
description: "このパートナーページでは、Snowflakeクエリを設定する際に参照する可能性のあるユースケースのサンプルクエリをいくつか提供しています。"
page_type: partner
search_tag: Partner

---

# サンプルクエリ

> このパートナーページでは、クエリを設定する際に参照するための考えられるユースケースのサンプルクエリを紹介します。

{% tabs %}
{% tab 時間でのフィルタリング%}

一般的なクエリは、時間でイベントをフィルターすることです。

発生時刻でイベントをフィルタリングできます。イベントテーブルは`time`によってクラスタリングされるため、`time`によるフィルタリングが最適です:
```sql
-- find custom events that occurred after 04/15/2019 @ 7:02pm (UTC) i.e., timestamp=1555354920
SELECT *
FROM users_behaviors_customevent_shared
WHERE time > 1555354920
LIMIT 10;
```
また、`sf_created_at` を使用して、イベントが Snowflake データウェアハウスで永続化された時刻に基づいてイベントをフィルタリングすることもできます。`sf_created_at` と `time` は同じではありませんが通常は類似しているため、このクエリは同様のパフォーマンス特性を持ちます。
```sql
-- find custom events that arrived in Snowflake after time 04/15/2019 @ 7:02pm (UTC)
SELECT *
FROM users_behaviors_customevent_shared
WHERE sf_created_at > to_timestamp_ntz('2019-04-15 19:02:00')
LIMIT 10;
```
{% alert note %}
`sf_created_at`の値は、`Nov 15th, 2019 9:31 pm UTC`以降に永続化されたイベントに対してのみ信頼できます。
{% endalert %}
{% endtab %}

{% tab 変更ログのクエリ%}
  
キャンペーン名とキャンバス名はイベント自体には存在しません。代わりに、それらは変更ログテーブルに公開されます。 

クエリのようなものを使用して、キャンペーンの変更履歴テーブルと結合することにより、キャンペーンに関連するイベントのキャンペーン名を確認できます。

```sql
SELECT event.id, event.time, ccs.time, ccs.name, ccs.conversion_behaviors[event.conversion_behavior_index]
FROM USERS_CAMPAIGNS_CONVERSION_SHARED event
LEFT JOIN CHANGELOGS_CAMPAIGN_SHARED ccs
ON ccs.id = event.campaign_id
AND ccs.time < event.time
qualify row_number() over (partition by event.id ORDER BY ccs.time DESC) = 1;
```
いくつかの重要な点には次のようなものがあります:
- Snowflakeの[window](https://docs.snowflake.com/en/sql-reference/functions-analytic.html)機能がここで使用されています。
- 左結合により、キャンペーンに関連しないイベントも含まれるようになります。
- イベントに`campaign_id`が表示されるがキャンペーン名が表示されない場合、キャンペーンがデータ共有が製品として存在する前の名前で作成された可能性があります。
- 代わりに `CHANGELOGS_CANVAS_SHARED` テーブルと結合することで、同様のクエリを使用してキャンバス名を確認できます。

キャンペーンとキャンバスの両方の名前を表示したい場合は、次のサブクエリを使用する必要があるかもしれません:
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
{% tab プッシュファネル %}

このプッシュファネルクエリを使用して、プッシュ送信の生イベントデータ、配信の生イベントデータ、開封の生イベントデータの順に集約できます。通常、生イベントごとに個別のテーブルがあるため、このクエリはすべてのテーブルを結合する方法を示します。

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
{% tab メールケイデンス %}
日次メールメッセージングケイデンスクエリを使用して、ユーザーのメール受信間隔の時間を分析できます。

例えば、ユーザーが1日に2通のメールを受信した場合、それは`0 "days since last received"`に該当します。月曜日と火曜日にそれぞれメールを1通ずつ受信したユーザーは、`1 "days since last received"` コホートに分類されます。

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
{% tab ユニークなメールクリック数 %}

このユニークなメールクリック数のクエリを使用して、指定された時間枠内でのユニークなメールクリックを分析できます。これを計算するアルゴリズムは次のとおりです:
  1. キー (`app_group_id`、`message_variation_id`、`dispatch_id`、`email_address`) でイベントを分割します。
  2. 各パーティション内で、イベントを時間順に並べ、最初のイベントは常に一意のイベントです。
  3. 後続のすべてのイベントでは、前のイベントから7日以上経過して発生したイベントは、ユニークなイベントと見なされます。
  
これを達成するために、Snowflake の[ウィンドウ関数](https://docs.snowflake.com/en/sql-reference/functions-analytic.html)を使用できます。次のクエリは、過去365日間のすべてのメールクリックを示し、`is_unique` 列にどのイベントがユニークであるかを示します。
  
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

一意のイベントだけを見たい場合は、`QUALIFY`句を使用します。
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
メールアドレスごとにグループ化されたユニークイベントの数をさらに表示するには、:次のようにします。
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
