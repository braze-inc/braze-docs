---
nav_title: "Anwendungsfälle"
article_title: SQL Segment Extensions Anwendungsfälle
page_order: 2
page_type: glossary
layout: sql_segment_extensions_glossary
alias: "/sql_segments_use_cases/"
description: "Dieser Artikel enthält getestete und bewährte Abfragen für SQL Segment Extensions."
tool: Segments
---

{% api %}
## Benutzer danach auswählen, wie oft ein Ereignis aufgetreten ist
{% apitags %}
Event
{% endapitags %}

Wählen Sie Benutzer aus, die eine bestimmte E-Mail-Kampagne in der Vergangenheit mehr als einmal geöffnet haben.

Dies funktioniert auch für die Begrenzung von In-App-Nachrichten nach der Anzahl der Impressionen, z. B. durch Auswahl von Nutzer:innen mit mehr als drei Impressionen als Segmentausschluss für dieselbe Kampagne. 

```sql
SELECT user_id FROM "USERS_MESSAGES_EMAIL_OPEN_SHARED"
WHERE campaign_api_id='8f7026dc-e9b7-40e6-bdc7-96cf58e80faa'
GROUP BY user_id
HAVING count(*) > 1
```
{% endapi %}

{% api %}
## Wählen Sie Nutzer:innen aus, die eine Aktion durchgeführt haben, und summieren Sie den Wert einer Eigenschaft.
{% apitags %}
Eigenschaft
{% endapitags %}

Wählen Sie Benutzer aus, die eine Sportwette abgeschlossen haben, bei der die Summe aller ihrer Wetten einen bestimmten Betrag übersteigt.

```sql
select user_id from "USERS_BEHAVIORS_CUSTOMEVENT_SHARED"
where name='Bet On Sports'
group by 1 having sum(get_path(parse_json(properties), 'amount')) > 150
```
{% endapi %}

{% api %}
## Wählen Sie Nutzer:innen danach aus, wie oft ein Event in einer bestimmten Zeitspanne aufgetreten ist
{% apitags %}
Event, Zeitbereich
{% endapitags %}

Wählen Sie Nutzer:innen mit mehr als drei geöffneten E-Mails in den letzten 30 Tagen aus.

Auf diese Weise lässt sich auch das Engagement von Nutzer:innen ermitteln, z. B. von Nutzer:innen, die über verschiedene Kanäle hinweg besonders schnell reagieren.

```sql
SELECT user_id, COUNT(DISTINCT id) AS num_emails_opened
FROM USERS_MESSAGES_EMAIL_OPEN_SHARED
WHERE to_timestamp_ntz(time) >= DATEADD(day, -30, CURRENT_TIMESTAMP()) AND to_timestamp_ntz(time) <= CURRENT_TIMESTAMP()
GROUP BY user_id;
HAVING COUNT(DISTINCT id) > 3
```
{% endapi %}

{% api %}
## Wählen Sie Nutzer:innen aus, die mindestens ein Ereignis über mehrere Zeiträume hinweg aufgezeichnet haben
{% apitags %}
Event, Zeitbereich
{% endapitags %}

Wählen Sie Nutzer aus, die in jedem der letzten vier Quartale einen Kauf getätigt haben. Dieses Nutzersegment kann mit [Zielgruppen-Synchronisierung]({{site.baseurl}}/partners/canvas_audience_sync/) verwendet werden, um hochwertige ähnliche Kund:innen für die Akquisition zu identifizieren.

```sql
ELECT DISTINCT user_id
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_timestamp_ntz(time) >= DATEADD(day, -90, CURRENT_TIMESTAMP()) AND to_timestamp_ntz(time) <= CURRENT_TIMESTAMP()
INTERSECT
SELECT DISTINCT user_id
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_timestamp_ntz(time) >= DATEADD(day, -180, CURRENT_TIMESTAMP()) AND to_timestamp_ntz(time) <= DATEADD(day, -91, CURRENT_TIMESTAMP())
INTERSECT
SELECT DISTINCT user_id
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_timestamp_ntz(time) >= DATEADD(day, -270, CURRENT_TIMESTAMP()) AND to_timestamp_ntz(time) <= DATEADD(day, -181, CURRENT_TIMESTAMP())
INTERSECT
SELECT DISTINCT user_id
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_timestamp_ntz(time) >= DATEADD(day, -365, CURRENT_TIMESTAMP()) AND to_timestamp_ntz(time) <= DATEADD(day, -271, CURRENT_TIMESTAMP());
```
{% endapi %}

{% api %}
## Wählen Sie einen Kauf mit bestimmten Eigenschaften
{% apitags %}
Kauf, Eigenschaft
{% endapitags %}

Wählen Sie Kunden aus, die innerhalb von 14 Tagen einen Kauf getätigt haben, der die Eigenschaft `“type = shops”` enthält. 

```sql
SELECT
user_id
FROM
USERS_BEHAVIORS_PURCHASE_SHARED
WHERE
product_id IS NOT NULL
AND
get_path(
parse_json(properties),
'propertyname'
) = 'propertyvalue'
AND
to_timestamp_ntz(time) >= DATEADD(day, -14, CURRENT_TIMESTAMP())
AND
to_timestamp_ntz(time) <= CURRENT_TIMESTAMP()
GROUP BY 1
HAVING COUNT(id) > 0;
```
{% endapi %}

{% api %}
## Wählen Sie Nutzer:innen aus, die eine nicht zugestellte Nachricht erhalten haben
{% apitags %}
Nachricht, Lieferung
{% endapitags %}

Wählen Sie Benutzer aus, denen eine SMS-Kampagne oder Canvas gesendet wurde, die Nachricht aber nicht an den Betreiber weitergeleitet wurde. Die Nachricht könnte zum Beispiel durch einen Überlauf der Warteschlange gestoppt worden sein. 

```sql
SELECT
user_id
FROM
USERS_MESSAGES_SMS_SEND_SHARED
WHERE
CANVAS_ID='63067c50740cc3377f8200d5'
AND TO_PHONE_NUMBER NOT IN (SELECT TO_PHONE_NUMBER FROM USERS_MESSAGES_SMS_CARRIERSEND_SHARED WHERE CANVAS_ID='63067c50740cc3377f8200d5')
GROUP BY 1
HAVING COUNT(id) > 0;
```
{% endapi %}

{% api %}
## Finden Sie alle SMS-Nachrichten, die versendet wurden, aber aufgrund eines Überlaufs in der Warteschlange den Betreiber nicht erreicht haben
{% apitags %}
Nachricht, Netzbetreiber
{% endapitags %}

Dies kann für andere Arten von Nachrichten, die von einem bestimmten Canvas gesendet wurden und nicht zugestellt wurden, wiederverwendet werden.

```sql
SELECT
user_id
FROM
USERS_MESSAGES_SMS_SEND_SHARED
WHERE
CANVAS_ID='id pulled from URL'
AND TO_PHONE_NUMBER NOT IN (SELECT TO_PHONE_NUMBER FROM USERS_MESSAGES_SMS_CARRIERSEND_SHARED WHERE CANVAS_ID='id pulled from URL')
GROUP BY 1
HAVING COUNT(id) > 0;
```
`CANVAS_ID` ist die Zahl nach `/canvas/` in Ihrer Canvas-URL.
{% endapi %}

{% api %}
## Wählen Sie Benutzer aus, die einen Kauf mit einem Eigenschaftsfeld getätigt haben, das einen bestimmten Wert enthält
{% apitags %}
Kauf, Eigenschaft
{% endapitags %}

```sql
SELECT DISTINCT EXTERNAL_USER_ID
FROM "USERS_BEHAVIORS_PURCHASE_SHARED",
LATERAL FLATTEN(input=>parse_json(properties):modifiers) as f
WHERE f.VALUE::STRING = 'Bacon'
```
{% endapi %}

{% api %}
## Finden Sie alle Benutzer, die mehrere 30003-Fehler und 0 Lieferungen hatten
{% apitags %}
Fehler, Lieferung
{% endapitags %}

Das ist hilfreich, wenn Sie den Versand an Nutzer:innen einstellen möchten, die keine Nachrichten erhalten, aber nicht als ungültig markiert werden, weil sie nicht den erforderlichen Fehlercode haben. Sie können diese Nutzer entweder erneut ansprechen, um ihre Telefonnummer zu aktualisieren, oder sie abmelden. 

Diese Abfrage verwendet den inkrementellen Editor und sucht nach Benutzern mit drei oder mehr abgelehnten Sendungen in den letzten 90 Tagen und null Lieferungen.

```sql
SELECT
  $date(time), user_id, COUNT(id)
FROM
  USERS_MESSAGES_SMS_REJECTION_SHARED
WHERE
  provider_error_code = '30003' 
  AND
  time > $start_date
    AND TO_PHONE_NUMBER NOT IN (SELECT TO_PHONE_NUMBER FROM USERS_MESSAGES_SMS_DELIVERY_SHARED)
GROUP BY 1, 2;
```
{% endapi %}

{% api %}
## Nutzer:innen mit bestimmten Event-Eigenschaften und einer bestimmten Anzahl von Events in einem bestimmten Zeitraum finden
{% apitags %}
Ereignis, Eigenschaft, Zeitbereich
{% endapitags %}

Finden Sie Benutzer, die die folgenden Bedingungen gleichzeitig erfüllen:

- Transaktionen mit einem Gesamtwert von mehr als 500 $ (die Summe mehrerer `Transact`-Events))
- Transaktionen im Einkaufszentrum `Funan`
- In den letzten 90 Tagen mehr als drei Transaktionen getätigt

```sql
SELECT
USER_ID
FROM
USERS_BEHAVIORS_CUSTOMEVENT_SHARED
WHERE
TIME > $start_date
AND NAME = 'Transact'
AND get_path(parse_json(properties), 'mall') = 'Funan'
GROUP BY
USER_ID
HAVING
SUM(get_path(parse_json(properties), 'total_value')) > 500
AND COUNT(*) > 3
```
{% endapi %}

{% api %}
## Benutzer auswählen, deren letzte Sitzung auf einem bestimmten Gerätemodell stattfand
{% apitags %}
Sitzung, Gerät
{% endapitags %}

```sql
select user_id, external_user_id, device_id, platform, os_version, device_model, to_timestamp(max(time)) last_session
from users_behaviors_app_sessionstart
where app_group_id = ''
and date_trunc(day, to_timestamp(time)) <= to_timestamp('2023-08-07')
and device_model = ''
group by user_id, external_user_id, device_id, platform, os_version, device_model
```
{% endapi %}

{% api %}
## Finden Sie Nutzer:innen, die in einem bestimmten Zeitraum den zweite Button einer In-App-Nachricht ausgewählt haben.
{% apitags %}
Zeitspanne
{% endapitags %}

```sql
SELECT DISTINCT USER_ID, to_timestamp_ntz(time)
FROM USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED
WHERE to_timestamp_ntz(time) >= '2023-08-03'::timestamp_ntz
AND to_timestamp_ntz(time) <= '2023-08-09'::timestamp_ntz
AND BUTTON_ID = '1'
AND CAMPAIGN_ID = '64c8cd9c4d38d13091957b1c'
```
{% endapi %}

{% api %}
## Finden Sie Benutzer, die in jedem der letzten drei Kalendermonate gekauft haben
{% apitags %}
Kauf, Zeitspanne
{% endapitags %}

```sql
SELECT DISTINCT user_id
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_timestamp_ntz(time) >= '2023-09-01'::timestamp_ntz
AND to_timestamp_ntz(time) <= '2023-09-30'::timestamp_ntz
INTERSECT
SELECT DISTINCT user_id
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_timestamp_ntz(time) >= '2023-10-01'::timestamp_ntz
AND to_timestamp_ntz(time) <= '2023-10-31'::timestamp_ntz
INTERSECT
SELECT DISTINCT user_id
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_timestamp_ntz(time) >= '2023-11-01'::timestamp_ntz
AND to_timestamp_ntz(time) <= '2023-11-30'::timestamp_ntz;
```
{% endapi %}

{% api %}
## Benutzer auswählen, die ein benutzerdefiniertes Ereignis mit einer bestimmten Eigenschaft abgeschlossen haben, wenn die Eigenschaft eine ganze Zahl ist
{% apitags %}
Event, Eigenschaft
{% endapitags %}

Senden Sie eine Nachricht an Nutzer, die in den letzten sechs Monaten eine Serie gesehen haben und die Plattform verlassen wollen. 

Die Eigenschaft ist die Titel-ID; andernfalls müssten Sie über 100 Titel-IDs in einen Filter aufnehmen. Die inkrementelle Segmenterweiterung kann kostenoptimiert werden und Sie können den Datumsbereich in der Kopfzeile angeben.

```sql
SELECT 
  $date(time), 
  USER_ID, 
  COUNT(*)
FROM 
  USERS_BEHAVIORS_CUSTOMEVENT_SHARED
WHERE 
  TIME > $start_date
  AND NAME = 'event name'
  AND (PARSE_JSON(PROPERTIES):property_name::INT) IN (1, 2)
GROUP BY 
  1, 2;
```
{% endapi %}

{% api %}
## Ermitteln Sie die durchschnittliche Anzahl von E-Mails, die ein Benutzer täglich erhält
{% apitags %}
Nachricht
{% endapitags %}

```sql
WITH user_email_counts AS (
  SELECT 
    USER_ID,
    COUNT(*) AS total_emails,
    DATEDIFF(day, MIN(TO_DATE(DATE_TRUNC('day', TO_TIMESTAMP_NTZ(TIME)))), MAX(TO_DATE(DATE_TRUNC('day', TO_TIMESTAMP_NTZ(TIME))))) AS days
  FROM USERS_MESSAGES_EMAIL_SEND_SHARED
  GROUP BY USER_ID
  HAVING COUNT(USER_ID) > 1
),

-- Then, calculate the average number of emails received by each user daily
user_daily_average AS (
  SELECT 
    USER_ID,
    days,
    CASE 
      WHEN days = 0 THEN total_emails  -- If the user received all emails in one day, the average for that user is the total number of emails
      ELSE total_emails / days  -- Otherwise, it's the total number of emails divided by the number of days
    END AS daily_average
  FROM user_email_counts
)

-- The total daily average is the average of all users
SELECT 
  AVG(daily_average)
FROM user_daily_average;
```

{% alert tip %}
Für SMS-Nachrichten ersetzen Sie `USERS_MESSAGES_EMAIL_SEND_SHARED` durch `USERS_MESSAGES_SMS_SEND_SHARED` in der Abfrage. Für Push-Benachrichtigungen ersetzen Sie `USERS_MESSAGES_EMAIL_SEND_SHARED` durch `USERS_MESSAGES_SMS_SEND_SHARED` in der Abfrage
{% endalert %}
{% endapi %}

{% api %}
## Ermitteln Sie die durchschnittliche Anzahl von E-Mails, die ein Benutzer wöchentlich erhält
{% apitags %}
Nachricht
{% endapitags %}

```sql
WITH user_email_counts AS (
  SELECT 
    USER_ID,
    COUNT(*) AS total_emails,
    DATEDIFF(week, MIN(TO_DATE(DATE_TRUNC('week', TO_TIMESTAMP_NTZ(TIME)))), MAX(TO_DATE(DATE_TRUNC('week', TO_TIMESTAMP_NTZ(TIME))))) AS weeks
  FROM USERS_MESSAGES_EMAIL_SEND_SHARED
  GROUP BY USER_ID
  HAVING COUNT(USER_ID) > 1
),

-- Then, calculate the average number of emails received by each user weekly
user_weekly_average AS (
  SELECT 
    USER_ID,
    CASE 
      WHEN weeks = 0 THEN total_emails  -- If the user received all emails in the same week, the average is the total number of emails
      ELSE total_emails / weeks  -- Otherwise, it's the total number of emails divided by the number of weeks
    END AS weekly_average
  FROM user_email_counts
)

-- The total weekly average is the average of all users
SELECT 
  AVG(weekly_average) AS average_weekly_emails
FROM user_weekly_average;
```
{% alert tip %}
Für SMS-Nachrichten ersetzen Sie `USERS_MESSAGES_EMAIL_SEND_SHARED` durch `USERS_MESSAGES_SMS_SEND_SHARED` in der Abfrage. Für Push-Benachrichtigungen ersetzen Sie `USERS_MESSAGES_EMAIL_SEND_SHARED` durch `USERS_MESSAGES_SMS_SEND_SHARED` in der Abfrage
{% endalert %}
{% endapi %}