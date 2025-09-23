---
nav_title: "Exemples de requêtes"
article_title: "Snowflake Requêtes d'échantillon"
page_order: 1
description: "Cette page partenaire propose quelques exemples de requêtes de cas d'utilisation possibles à consulter lors de la configuration de vos requêtes Snowflake."
page_type: partner
search_tag: Partner

---

# Exemples de requêtes

> Cette page partenaire propose quelques exemples de requêtes de cas d'utilisation possibles à consulter lors de la configuration de vos requêtes.

{% tabs %}
{% tab Filtrer par temps%}

Une requête courante pourrait être de filtrer les événements par heure.

Vous pouvez les filtrer par le moment de l'occurrence. Les tables d'événements sont regroupées par `time`, ce qui rend le filtrage par `time` optimal :
```sql
-- find custom events that occurred after 04/15/2019 @ 7:02pm (UTC) i.e., timestamp=1555354920
SELECT *
FROM users_behaviors_customevent_shared
WHERE time > 1555354920
LIMIT 10;
```
Vous pouvez également filtrer les événements selon l'heure à laquelle ils ont été enregistrés dans l'entrepôt de données Snowflake à l’aide du paramètre `sf_created_at`. `sf_created_at` et `time` ne sont pas identiques mais fonctionnent généralement de manière semblable, donc cette requête devrait avoir des caractéristiques de performance similaires :
```sql
-- find custom events that arrived in Snowflake after time 04/15/2019 @ 7:02pm (UTC)
SELECT *
FROM users_behaviors_customevent_shared
WHERE sf_created_at > to_timestamp_ntz('2019-04-15 19:02:00')
LIMIT 10;
```
{% alert note %}
La valeur de `sf_created_at` n'est fiable que pour les événements qui ont été enregistrés après `Nov 15th, 2019 9:31 pm UTC`.
{% endalert %}
{% endtab %}

{% tab Interroger les journaux des modifications%}
  
Les noms de campagne et les noms de canvas ne sont pas présents dans les événements eux-mêmes. Au lieu de cela, ils sont publiés dans un journal des modifications. 

Vous pouvez voir les noms des campagnes des événements liés à une campagne en joignant la table du journal des modifications de la campagne en utilisant une requête comme :

```sql
SELECT event.id, event.time, ccs.time, ccs.name, ccs.conversion_behaviors[event.conversion_behavior_index]
FROM USERS_CAMPAIGNS_CONVERSION_SHARED event
LEFT JOIN CHANGELOGS_CAMPAIGN_SHARED ccs
ON ccs.id = event.campaign_id
AND ccs.time < event.time
qualify row_number() over (partition by event.id ORDER BY ccs.time DESC) = 1;
```
Quelques points importants à noter :
- Les fonctions de [fenêtre](https://docs.snowflake.com/en/sql-reference/functions-analytic.html) de Snowflake sont utilisées ici.
- La jointure gauche garantira que les événements non liés à une campagne seront également inclus.
- Si vous voyez des événements avec `campaign_id`s mais sans noms de campagne, il est possible que la campagne ait été créée avec un nom avant que le partage de données n'existe en tant que produit.
- Vous pouvez voir les noms de canvas en utilisant une requête similaire, en joignant la table `CHANGELOGS_CANVAS_SHARED` à la place.

Si vous souhaitez voir à la fois les noms de campagne et de canvas, vous pouvez utiliser la sous-requête suivante :
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
{% tab Entonnoir des notifications push %}

Vous pouvez utiliser cette requête d'entonnoir de notifications push pour agréger les données brutes des événements d'envoi de notifications push, jusqu'aux données brutes des événements de livraison, et jusqu'aux données brutes des événements d'ouverture. Cette requête montre comment toutes les tables doivent être jointes car chaque événement brut a généralement une table séparée :

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
{% tab Fréquence des e-mails %}
Vous pouvez utiliser cette requête de cadence d'envoi de messages par e-mail quotidienne pour analyser le temps entre les e-mails qu'un utilisateur reçoit.

Par exemple, si un utilisateur recevait deux e-mails en une journée, ils tomberaient sous `0 "days since last received"`. S'ils recevaient un e-mail lundi et un autre mardi, ils tomberaient dans la cohorte `1 "days since last received"`.

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
{% tab Clics d'e-mail uniques %}

Vous pouvez utiliser cette requête de clics d'e-mail unique pour analyser le clic d'e-mail unique dans une fenêtre de temps donnée. L'algorithme pour calculer cela est le suivant :
  1. Partitionner les événements par la clé (`app_group_id`, `message_variation_id`, `dispatch_id`, `email_address`).
  2. Dans chaque partition, ordonnez les événements par temps, et le premier événement est toujours un événement unique.
  3. Pour chaque événement ultérieur, s'il s'est produit plus de sept jours après son prédécesseur, il est considéré comme un événement unique.
  
Nous pouvons utiliser les [fonctions de fenêtrage](https://docs.snowflake.com/en/sql-reference/functions-analytic.html) de Snowflake pour nous aider à atteindre cet objectif. La requête suivante nous donne tous les clics d'e-mail des 365 derniers jours et indique quels événements sont uniques dans la colonne `is_unique` :
  
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

Si vous voulez simplement voir les événements uniques, utilisez la clause `QUALIFY` :
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
Pour afficher les comptes d'événements uniques regroupés par adresse e-mail :
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
