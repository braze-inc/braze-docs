---
nav_title: "Musterabfragen"
article_title: Snowflake Musterabfragen
page_order: 1
description: "Auf dieser Partnerseite finden Sie einige Beispielabfragen für mögliche Anwendungsfälle, auf die Sie beim Einrichten Ihrer Snowflake-Abfragen referenzieren können."
page_type: partner
search_tag: Partner

---

# Musterabfragen

> Auf dieser Partnerseite finden Sie einige Beispielabfragen für mögliche Anwendungsfälle, auf die Sie beim Einrichten Ihrer Abfragen referenzieren können.

{% tabs %}
{% tab Nach Zeit filtern%}

Eine gängige Abfrage könnte sein, Ereignisse nach Zeit zu filtern.

Sie können sie nach dem Zeitpunkt des Vorkommens filtern. Die Ereignistabellen sind nach `time` geclustert, so dass die Filterung nach `time` optimal ist:
```sql
-- find custom events that occurred after 04/15/2019 @ 7:02pm (UTC) i.e., timestamp=1555354920
SELECT *
FROM users_behaviors_customevent_shared
WHERE time > 1555354920
LIMIT 10;
```
Sie können Ereignisse auch nach dem Zeitpunkt filtern, zu dem sie im Snowflake Data Warehouse persistiert wurden, indem Sie `sf_created_at` verwenden. `sf_created_at` und `time` sind nicht dasselbe, liegen aber in der Regel nahe beieinander, so dass diese Abfrage ähnliche Performance-Eigenschaften haben sollte:
```sql
-- find custom events that arrived in Snowflake after time 04/15/2019 @ 7:02pm (UTC)
SELECT *
FROM users_behaviors_customevent_shared
WHERE sf_created_at > to_timestamp_ntz('2019-04-15 19:02:00')
LIMIT 10;
```
{% alert note %}
Der Wert von `sf_created_at` ist nur für Ereignisse zuverlässig, die nach `Nov 15th, 2019 9:31 pm UTC` persistent waren.
{% endalert %}
{% endtab %}

{% tab Changelogs abfragen%}
  
Die Namen der Kampagnen und Canvas sind nicht in den Ereignissen selbst enthalten. Stattdessen werden sie in einer Changelog-Tabelle veröffentlicht. 

Sie können die Namen von Kampagnen für Ereignisse im Zusammenhang mit einer Kampagne sehen, indem Sie eine Abfrage wie diese mit der Tabelle der Kampagnen-Änderungsprotokolle verbinden:

```sql
SELECT event.id, event.time, ccs.time, ccs.name, ccs.conversion_behaviors[event.conversion_behavior_index]
FROM USERS_CAMPAIGNS_CONVERSION_SHARED event
LEFT JOIN CHANGELOGS_CAMPAIGN_SHARED ccs
ON ccs.id = event.campaign_id
AND ccs.time < event.time
qualify row_number() over (partition by event.id ORDER BY ccs.time DESC) = 1;
```
Einige wichtige Dinge sind zu beachten:
- Hier werden die [Fensterfunktionen](https://docs.snowflake.com/en/sql-reference/functions-analytic.html) von Snowflake verwendet.
- Die linke Verknüpfung sorgt dafür, dass auch Ereignisse, die nicht mit einer Kampagne in Verbindung stehen, berücksichtigt werden.
- Wenn Sie Ereignisse mit `campaign_id`sehen, aber keine Namen von Kampagnen, besteht die Möglichkeit, dass die Kampagne mit einem Namen erstellt wurde, bevor es Data Sharing als Produkt gab.
- Sie können die Canvas-Namen mit einer ähnlichen Abfrage anzeigen, die Sie stattdessen mit der Tabelle `CHANGELOGS_CANVAS_SHARED` verknüpfen.

Wenn Sie sowohl die Namen von Kampagnen als auch von Canvas sehen möchten, müssen Sie möglicherweise die folgende Unterabfrage verwenden:
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
{% tab Push Funnel %}

Sie können diese Push Funnel-Abfrage verwenden, um Push-Sende-Rohdaten, Zustellungs-Rohdaten und Öffnungs-Rohdaten zu aggregieren. Diese Abfrage zeigt, wie alle Tabellen miteinander verbunden werden sollten, da jedes Raw Event in der Regel eine eigene Tabelle hat:

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
{% tab E-Mail Kadenz %}
Mit dieser Abfrage für das tägliche Messaging von E-Mails können Sie die Zeitspanne zwischen den Nachrichten analysieren, die ein Nutzer:innen erhält.

Wenn ein Nutzer:innen zum Beispiel zwei E-Mails an einem Tag erhalten hat, fallen diese unter `0 "days since last received"`. Wenn sie eine E-Mail am Montag und eine am Dienstag erhalten haben, würden sie in die Kohorte `1 "days since last received"` fallen.

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
{% tab Eindeutige Klicks auf E-Mails %}

Sie können diese Abfrage für eindeutige E-Mail-Klicks verwenden, um die eindeutigen E-Mail-Klicks in einem bestimmten Zeitfenster zu analysieren. Der Algorithmus zur Berechnung lautet wie folgt:
  1. Unterteilen Sie die Ereignisse nach dem Schlüssel (`app_group_id`, `message_variation_id`, `dispatch_id`, `email_address`).
  2. Ordnen Sie die Ereignisse in jeder Partition nach Zeit, wobei das erste Ereignis immer ein eindeutiges Ereignis ist.
  3. Denn jedes nachfolgende Ereignis, das mehr als sieben Tage nach seinem Vorgänger eintritt, wird als eindeutiges Ereignis betrachtet.
  
Dazu können wir die [Windowing-Funktionen](https://docs.snowflake.com/en/sql-reference/functions-analytic.html) von Snowflake verwenden. Die folgende Abfrage liefert uns alle E-Mail Klicks der letzten 365 Tage und zeigt in der Spalte `is_unique` an, welche Ereignisse eindeutig sind:
  
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

Wenn Sie nur die eindeutigen Ereignisse sehen möchten, verwenden Sie die `QUALIFY` Klausel:
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
Um die Anzahl eindeutiger Ereignisse gruppiert nach E-Mail-Adressen anzuzeigen:
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
