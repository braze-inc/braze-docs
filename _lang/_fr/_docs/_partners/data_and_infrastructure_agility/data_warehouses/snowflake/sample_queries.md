---
nav_title: "Exemples de Requêtes"
article_title: Échantillons d'échantillons de flocon de neige
page_order: 1
description: "Cette page partenaire offre quelques exemples de cas d'utilisation possibles à référencer lors de la configuration de vos requêtes."
page_type: partenaire
search_tag: Partenaire
---

# Exemples de requêtes

> Cette page partenaire offre quelques exemples de cas d'utilisation possibles à référencer lors de la configuration de vos requêtes.

{% tabs %}
  {% tab Filter By Time%}

  Une requête courante peut être de filtrer les événements par temps.

  Vous pouvez les filtrer au moment de l'occurrence. Les tables d'événements sont regroupées par `temps` qui rend le filtrage par `temps` performant.

```sql
-- trouver les événements personnalisés qui se sont produits après le 15/04/2019 @ 7:02pm (UTC) i.e. timestamp=1555354920
SELECT *
FROM users_behaviors_customevent_shared
WHERE time > 1555354920
LIMIT 10;
```
  Ou vous pouvez filtrer les événements au moment où ils ont été maintenus dans l'entrepôt de données Snowflake en utilisant `sf_created_at`. `sf_created_at` et `instant` ne sont pas les męmes mais sont généralement proches, donc cette requête doit avoir des caractéristiques de performances similaires

```sql
-- trouver les événements personnalisés qui sont arrivés dans Snowflake après le 04/15/2019 @ 7:02pm (UTC)
SELECT *
FROM users_behaviors_customevent_shared
WHERE sf_created_at > to_timestamp_ntz('2019-04-15 19:02:00')
LIMIT 10;
```

Remarque : La valeur de `sf_created_at` n'est fiable que pour les événements qui ont été persistés après `15 Nov 21 :31 pm UTC`.
  {% endtab %}
  {% tab Querying Changelogs%}

Les noms de campagne et de Canvas ne sont pas présents dans les événements eux-mêmes. Au lieu de cela, ils sont publiés dans un tableau du changelog.

Vous pouvez voir les noms des campagnes pour les événements liés à une campagne en rejoignant la table de changelog de campagne en utilisant une requête comme

```sql
SELECT event.id, event.time, ccs.time, ccs.time, ccs.name, ccs.conversion_behaviors[event.conversion_behavior_index]
FROM USERS_CAMPAIGNS_CONVERSION_SHARED event
LEFT JOINDRE CHANGELOGS_CAMPAIGN_SHARED ccs
ON ccs. d = event.campaign_id
AND ccs.time < event.time
qualifier row_number() plus (partition par event.id ORDER BY ccs.time DESC) = 1;
```
Note :
- Nous utilisons les fonctions [window](https://docs.snowflake.com/en/sql-reference/functions-analytic.html) de Snowflake ici.
- La participation de gauche fera en sorte que les événements qui n'étaient pas liés à une campagne seront également inclus.
- Si vous voyez des événements avec `campaign_id`s mais aucun nom de campagne, il est possible que la campagne ait été créée avec un nom avant que le partage de données n'existe.
- Vous pouvez voir les noms de Canvas en utilisant une requête similaire, en rejoignant la table `CHANGELOGS_CANVAS_SHARED` à la place.

Si vous voulez voir les noms de campagne et de Canvas vous devrez utiliser une sous-requête comme indiqué ci-dessous.

```sql
SELECT campaign_join.*, canvas.name AS canvas_name
FROM 
(SELECT e.id AS event_id, e.external_user_id, e.time, e.user_id, e.device_id, e.sf_created_at,
    e.campaign_api_id, e. anvas_id, e.canvas_step_api_id, 
    campagne. Identique comme campaign_name
  FROM USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED AS e
  LEFT JOIN CHANGELOGS_CAMPAIGN_SHARED AS campaign ON campaign. d = e.campaign_id
  OÙ e.time >= 1574830800 ET e. ime <= 1575176399
  qualifie la fonction row_number() (partition par campagne ORDER BY e.id. ime DESC) = 1) AS campaign_join
GAUCHE JOINDRE CHANGELOGS_CANVAS_SHARED AS Canvas ON canvas.id = campaign_join. anvas_id
qualifie row_number() au dessus (partition par campaign_join.event_id ORDER BY canvas.time DESC) = 1;
```
  {% endtab %}
  {% tab Push Funnel %}

  Vous pouvez utiliser cette requête Push Funnel pour agréger l'envoi de données d'événements bruts, jusqu'à la livraison de données d'événements bruts, à travers pour ouvrir les données de l'événement brut. Cette requête montre comment toutes les tables doivent être jointes car chaque événement brut a généralement une table séparée.

```sql

SELECTIONNEZ
    COUNT(DISTINCT send."ID" ) AS "users_messages_pushnotification_send.push_sent",
    COALESCE((COUNT(DISTINCT envoyer). ID" ),0)-COALESCE((COUNT(DISTINCT bounce."ID" ),0) AS "users_messages_pushnotification_send.push_delivered",
    COUNT(DISTINCT ouvert. ID" ) AS "users_messages_pushnotification_open.push_opens"
FROM users_messages_pushnotification_send_shared AS send
LEFT JOIN USERS_MESSAGES_PUSHNOTIFICATION_OPEN_shared AS open ON (send. USER_ID")=(open."USER_ID")
    ET
    (send."DEVICE_ID")=(ouvert. DEVICE_ID")
    ET
    ((send."MESSAGE_VARIATION_API_ID")=(open."MESSAGE_VARIATION_API_ID")
    OU
    (send. CANVAS_STEP_API_ID")=(open."CANVAS_STEP_API_ID"))
LEFT JOIN users_messages_pushnotification_bounce_shared AS bounce ON (send."USER_ID")=(bounce. USER_ID")
    ET
    (Send."DEVICE_ID")=(bounce."DEVICE_ID")
    ET
    (Send."MESSAGE_VARIATION_API_ID")=(bounce. MESSAGE_VARIATION_API_ID")
    OU
    (send."CANVAS_STEP_API_ID")=(bounce."CANVAS_STEP_API_ID"))
LIMIT 500;
```

  {% endtab %}
  {% tab Email Cadence %}
Vous pouvez utiliser cette requête quotidienne de Cadence de messagerie pour analyser le temps entre les emails qu'un utilisateur reçoit.

Par exemple, si un utilisateur a reçu deux e-mails en un jour, il tomberait sous `0 « jours depuis la dernière réception»`. S'ils ont reçu un email le lundi et un mardi, ils tomberaient dans la cohorte `1 « jours depuis la dernière réception»`.

```sql
WITH email_messaging_cadence AS (WITH deliveries AS
      (SELECT TO_TIMESTAMP(time) AS delivered_timestamp,
      email_address AS delivered_address,
      message_variation_api_id AS d_message_variation_api_id,
      canvas_step_api_id AS d_canvas_step_api_id,
      campaign_api_id AS d_campaign_api_id,
      canvas_api_id AS d_canvas_api_id,
      id AS delivered_id,
      rank() over (partition par delivered_address ORDER BY delivered_timestamp ASC) AS delivery_event,
      min(delivered_timestamp) over (partition par delivered_address ORDER BY delivered_timestamp ASC) AS first_delivered,
      datdiff(day, lag(delivered_timestamp) over (partition par delivered_address ORDER BY delivered_timestamp ASC), delivered_timestamp) AS diff_days,
      datediff(week, lag(delivered_timestamp) over (partition par delivered_address ORDER BY delivered_timestamp ASC), delivered_timestamp) AS diff_weeks
      from USERS_MESSAGES_EMAIL_DELIVERY_SHARED GROUP BY 1,2,3,4,5,6,7), ouvre AS
      (SELECT DISTINCT email_address AS open_address,
      message_variation_api_id AS o_message_variation_api_id,
      canvas_step_api_id AS o_canvas_step_api_id
      FROM USERS_MESSAGES_EMAIL_OPEN_SHARED), clique sur
      (SELECT DISTINCT email_address AS click_address,
      message_variation_api_id AS c_message_variation_api_id,
      canvas_step_api_id AS c_canvas_step_api_id
      FROM USERS_MESSAGES_EMAIL_CLICK_SHARED) SELECT * FROM livraison
      GAUCHE JOIN ouvre
      ON (livraisons. elivered_address)=(opens.open_address)
      AND ((deliveries.d_message_variation_api_id)=(opens.o_message_variation_api_id) OU (livraisons. _canvas_step_api_id)=(opens.o_canvas_step_api_id))
      clics GAUCHE REJOINT clics
      ON (livraisons. elivered_address)=(clicks.click_address)
      ET ((deliveries.d_message_variation_api_id)=(clicks.c_message_variation_api_id) OU (livraisons. _canvas_step_api_id)=(clicks.c_canvas_step_api_id))
      )
SELECT
    email_messaging_cadence. DIFF_DAYS" AS "email_messaging_cadence.days_since_last_received",
    (count(distinct email_messaging_cadence."OPEN_ADDRESS", email_messaging_cadence."O_MESSAGE_VARIATION_API_ID")
      +count(distinct email_messaging_cadence. OPEN_ADDRESS", email_messaging_cadence."O_CANVAS_STEP_API_ID"))/(COUNT(DISTINCT email_messaging_cadence."DELIVERED_ID" )) AS "email_messaging_cadence.unique_open_rate"
FROM email_messaging_cadence GROUP BY 1
ORDER BY 1
LIMIT 500;
```
  {% endtab %}
  {% tab Unique Email Clicks %}

L'algorithme pour calculer les clics uniques d'email dans une fenêtre de temps donnée est comme suit.
  1. Partitionner les événements par la clé (app_group_id, message_variation_id, dispatch_id, email_address).
  2. Dans chaque partition, ordonner les événements par temps et le premier événement est toujours un événement unique.
  3. Pour chaque événement subséquent, s'il s'est produit plus de 7 jours après son prédécesseur, est considéré comme un événement unique.

Nous pouvons utiliser les fonctions de fenêtrage de Snowflake pour nous aider à y parvenir. La requête ci-dessous nous donne tous les clics de courriel au cours des 365 derniers jours et indique quels événements sont uniques dans la colonne `is_unique` </code>.

```sql
SELECT id, app_group_id, message_variation_api_id, dispatch_id, email_address, heure,
  ROW_NUMBER() OVER (PARTITION BY app_group_id, message_variation_api_id, dispatch_id, dispatch_id, email_address order by time) row_number,
  LAG(time, 1, time) OVER (PARTITION BY app_group_id, message_variation_api_id, dispatch_id, email_address order by time) previous_time,
  temps - previous_time AS diff,
  IFF(row_number = 1, true, IFF(diff >= 7*24*3600, true, false)) AS is_unique
DE USERS_MESSAGES_EMAIL_CLICK_SHARED
OÙ
  heure < DATE_PART('EPOCH_SECOND', À TIMESTAMP(CURRENT_TIMESTAMP())) 
  ET heure > DATE_PART('EPOCH_SECOND', TO_TIMESTAMP(CURRENT_TIMESTAMP())) - 365*24*3600; 
```
Si vous voulez juste voir les événements uniques, utilisez la clause `QUALIFY`.
```sql
SELECT id, app_group_id, message_variation_api_id, dispatch_id, email_adresse, heure,
  ROW_NUMBER() OUVRIR (PARTITION BY app_group_id, message_variation_api_id, dispatch_id, email_address order by time) row_number,
  LAG(temps, 1, temps) OVRIR (PARTITION BY app_group_id, message_variation_api_id, dispatch_id, email_address order by time) previous_time,
  time - previous_time AS diff,
  IFF(row_number = 1, true, IFF(diff >= 7*24*3600, true, false)) AS is_unique
DE USERS_MESSAGES_EMAIL_CLICK_SHARED
OÙ
  heure < DATE_PART('EPOCH_SECOND', À TIMESTAMP(CURRENT_TIMESTAMP())) 
  ET heure > DATE_PART('EPOCH_SECOND', TO_TIMESTAMP(CURRENT_TIMESTAMP())) - 365*24*3600
QUALIFY est_unique = true;
```
Pour voir plus loin le nombre d'événements uniques regroupés par adresse e-mail
```sql
WITH unique_events AS(
  SELECT id, app_group_id, message_variation_api_id, dispatch_id, email_address, heure,
  ROW_NUMBER() OUVRIR (PARTITION PAR app_group_id, message_variation_api_id, dispatch_id, email_address order par temps) row_number,
  LAG(temps, 1, temps) NIVEAU (PARTITION PAR app_group_id, message_variation_api_id, dispatch_id, email_address order by time) previous_time,
  time - previous_time AS diff,
  IFF(row_number = 1, true, iff(diff >= 7*24*3600, true, false)) AS is_unique
FROM USERS_MESSAGES_EMAIL_CLICK_SHARED
WHERE
  time < DATE_PART('EPOCH_SECOND', À TIMESTAMP(CURRENT_TIMESTAMP())) 
  ET heure > DATE_PART('EPOCH_SECOND', TO_TIMESTAMP(CURRENT_TIMESTAMP())) - 365*24*3600
QUALIFY est_unique = true) 
SELECT email_address, count(*) AS count
FROM unique_events
GROUP BY email_address;
```
  {% endtab %}
{% endtabs %}
