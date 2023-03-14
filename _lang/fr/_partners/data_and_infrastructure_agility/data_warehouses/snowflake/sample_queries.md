---
nav_title: "Exemples de requêtes"
article_title: Exemples de requêtes Snowflake
page_order: 1
description: "Cette page partenaire propose des exemples de requêtes de cas d’utilisation qui peuvent vous être utiles lorsque vous configurez vos requêtes."
page_type: partner
search_tag: Partenaire

---

# Exemples de requêtes Snowflake

>  Cette page partenaire propose des exemples de requêtes de cas d’utilisation qui peuvent vous être utiles lorsque vous configurez vos requêtes.

{% tabs %}
{% tab Filter By Time%}

Un exemple de requête courante peut être de filtrer les événements par heure.

Vous pouvez les filtrer au moment où ils se produisent. Les tableaux d’événements sont regroupés par `time`, pour optimiser le filtrage par `time` :
```sql
-- find custom events that occurred after 04/15/2019 @ 7:02pm (UTC) i.e., timestamp=1555354920
SELECT *
FROM users_behaviors_customevent_shared
WHERE time > 1555354920
LIMIT 10;
```
Vous pouvez également filtrer les événements en fonction de l’heure à laquelle ils ont été conservés dans l’entrepôt de données Snowflake en utilisant `sf_created_at`. `sf_created_at` et `time` ne sont pas identiques, mais sont généralement proches, cette requête devrait donc avoir des caractéristiques de performance similaires :
```sql
-- find custom events that arrived in Snowflake after time 04/15/2019 @ 7:02pm (UTC)
SELECT *
FROM users_behaviors_customevent_shared
WHERE sf_created_at > to_timestamp_ntz('2019-04-15 19:02:00')
LIMIT 10;
```
{% alert note %}
La valeur `sf_created_at` n’est fiable que pour les événements qui ont persisté après le `15 novembre 2019 à 21 h 31 UTC`.
{% endalert %}
{% endtab %}

{% tab Querying Changelogs%}
  
Les noms des campagnes et Canvas ne sont pas inclus dans les événements eux-mêmes. Ils sont publiés dans un journal de modifications. 

Vous pouvez voir les noms de campagne des événements liés à une campagne en interrogeant le journal de modifications de la campagne à l’aide d’une requête telle que :

```sql
SELECT event.id, event.time, ccs.time, ccs.name, ccs.conversion_behaviors[event.conversion_behavior_index]
FROM USERS_CAMPAIGNS_CONVERSION_SHARED event
LEFT JOIN CHANGELOGS_CAMPAIGN_SHARED ccs
ON ccs.id = event.campaign_id
AND ccs.time < event.time
qualify row_number() over (partition by event.id ORDER BY ccs.time DESC) = 1;
```
Voici quelques éléments importants à noter :
- Les fonctions de la [fenêtre](https://docs.snowflake.com/en/sql-reference/functions-analytic.html) Snowflake sont utilisées ici.
- La jointure à gauche permet de vous assurer que les événements non liés à une campagne seront également inclus.
- Si vous voyez des événements avec des `campaign_id`, mais pas de noms de campagne, il se peut que la campagne ait été créée avec un nom alors que Data Sharing n’existait pas encore.
- Vous pouvez voir les noms de Canvas en utilisant une requête similaire, mais en interrogeant le tableau `CHANGELOGS_CANVAS_SHARED`.

Si vous souhaitez voir les noms des campagnes et Canvas, vous devrez peut-être utiliser la sous-requête suivante :
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

Vous pouvez utiliser cette requête d’entonnoir de notification push pour regrouper les données brutes d’événements d’envoi de notifications push, les données brutes d’événements de livraison et les données brutes d’événements d’ouverture. Cette requête montre comment tous les tableaux doivent être joints, car chaque événement brut dispose généralement d’un tableau séparé :

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
{% tab Email Cadence %}
Vous pouvez utiliser cette requête de fréquence quotidienne des envois d’e-mail pour analyser le temps écoulé entre les e-mails reçus par un utilisateur.

Par exemple, si un utilisateur a reçu deux e-mails en un jour, ils seraient catégorisés comme `0 « jours depuis la dernière réception »`. S’ils ont reçu un e-mail le lundi et un autre mardi, ils seraient catégorisés dans la cohorte `1 « jours depuis la dernière réception »`.

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
{% tab Unique Email Clicks %}

Vous pouvez utiliser cette requête pour analyser le nombre de clics sur cet e-mail unique par rapport à une période donnée. L’algorithme utilisé pour ce calcul est le suivant :
  1. Partitionner les événements en fonction de la clé (`app_group_id`, `message_variation_id`, `dispatch_id`, `email_address`).
  2. Dans chaque partition, organisez les événements par heure, le premier événement étant toujours un événement unique.
  3. Pour chaque événement ultérieur, si l’événement se produit plus de sept jours après le dernier, il sera alors considéré comme un événement unique.
  
Pour vous aider, vous pouvez utiliser les [fonctions de fenêtrage](https://docs.snowflake.com/en/sql-reference/functions-analytic.html) de Snowflake. La requête suivante indique tous les clics effectués sur l’e-mail au cours des 365 derniers jours et quels événements sont uniques dans la colonne `is_unique` :
  
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

Si vous souhaitez simplement voir les événements uniques, utilisez la clause `QUALIFY` :
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
Pour voir plus en détail les nombres d’événements uniques regroupés par e-mail :
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
