---
nav_title: "Cas d’utilisation"
article_title: "Cas d'utilisation des extensions de segments SQL"
page_order: 2
page_type: glossary
layout: sql_segment_extensions_glossary
alias: "/sql_segments_use_cases/"
description: "Cet article contient des requêtes testées et éprouvées pour les extensions de segments SQL."
tool: Segments
---

{% api %}
## Sélectionner les utilisateurs en fonction du nombre de fois qu'un événement s'est produit
{% apitags %}
Événement
{% endapitags %}

Sélectionnez les utilisateurs qui ont ouvert une certaine campagne d'e-mail plus d'une fois dans le passé.

Cela fonctionne également pour le plafonnement des messages in-app en fonction du nombre d'impressions, par exemple en sélectionnant les utilisateurs ayant plus de trois impressions comme segment d'exclusion sur la même campagne. 

```sql
SELECT user_id FROM "USERS_MESSAGES_EMAIL_OPEN_SHARED"
WHERE campaign_api_id='8f7026dc-e9b7-40e6-bdc7-96cf58e80faa'
GROUP BY user_id
HAVING count(*) > 1
```
{% endapi %}

{% api %}
## Sélectionnez les utilisateurs qui ont effectué une action et additionnez la valeur d'une propriété.
{% apitags %}
Propriété
{% endapitags %}

Sélectionnez les utilisateurs qui ont fait un pari sur le sport et dont la somme de tous les paris est supérieure à un certain montant.

```sql
select user_id from "USERS_BEHAVIORS_CUSTOMEVENT_SHARED"
where name='Bet On Sports'
group by 1 having sum(get_path(parse_json(properties), 'amount')) > 150
```
{% endapi %}

{% api %}
## Sélectionnez les utilisateurs en fonction du nombre de fois qu'un événement s'est produit dans une période donnée.
{% apitags %}
Événement, Période
{% endapitags %}

Sélectionnez les utilisateurs ayant ouvert plus de trois e-mails au cours des 30 derniers jours.

Cela permet également de déterminer les niveaux d'engagement des utilisateurs, par exemple les utilisateurs très réactifs sur différents canaux.

```sql
SELECT user_id, COUNT(DISTINCT id) AS num_emails_opened
FROM USERS_MESSAGES_EMAIL_OPEN_SHARED
WHERE to_timestamp_ntz(time) >= DATEADD(day, -30, CURRENT_TIMESTAMP()) AND to_timestamp_ntz(time) <= CURRENT_TIMESTAMP()
GROUP BY user_id;
HAVING COUNT(DISTINCT id) > 3
```
{% endapi %}

{% api %}
## Sélectionnez les utilisateurs qui ont enregistré au moins un événement sur plusieurs périodes.
{% apitags %}
Événement, Période
{% endapitags %}

Sélectionnez les utilisateurs qui ont effectué un achat au cours de chacun des quatre derniers trimestres. Ce segment d'utilisateurs peut être utilisé avec la [synchronisation d'audience]({{site.baseurl}}/partners/canvas_audience_sync/) pour identifier des clients similaires de grande valeur pour l'acquisition.

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
## Sélectionnez tout achat présentant certaines propriétés
{% apitags %}
Achat, propriété
{% endapitags %}

Sélectionnez les clients qui ont effectué un achat contenant la propriété `“type = shops”` dans les 14 jours. 

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
## Sélectionnez les utilisateurs auxquels un message a été envoyé mais n'a pas été délivré.
{% apitags %}
Message, réception/distribution
{% endapitags %}

Sélectionnez les utilisateurs qui ont reçu une campagne de communication par SMS ou Canvas, mais dont le message n'est pas parvenu à l'opérateur. Par exemple, le message peut avoir été arrêté en raison d’un débordement de la file d'attente. 

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
## Retrouvez tous les messages SMS qui ont été envoyés mais qui ne sont pas parvenus à l'opérateur en raison d'un dépassement de la file d'attente.
{% apitags %}
Message, opérateur
{% endapitags %}

Cela peut être réutilisé pour d'autres types de messages envoyés à partir d'un Canvas particulier et qui n'ont pas été délivrés.

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
`CANVAS_ID` est le numéro qui suit `/canvas/` dans l'URL de votre Canvas.
{% endapi %}

{% api %}
## Sélectionnez les utilisateurs qui ont effectué un achat avec un tableau de propriétés contenant une valeur spécifique.
{% apitags %}
Achat, propriété
{% endapitags %}

```sql
SELECT DISTINCT EXTERNAL_USER_ID
FROM "USERS_BEHAVIORS_PURCHASE_SHARED",
LATERAL FLATTEN(input=>parse_json(properties):modifiers) as f
WHERE f.VALUE::STRING = 'Bacon'
```
{% endapi %}

{% api %}
## Trouvez tous les utilisateurs qui ont eu plusieurs erreurs 30003 et 0 réception/distribution.
{% apitags %}
Erreur, réception/distribution
{% endapitags %}

Ceci est utile pour résoudre les situations où vous voulez arrêter l'envoi aux utilisateurs qui ne reçoivent pas de messages mais qui ne sont pas marqués comme invalides parce qu'ils n'ont pas le code d'erreur requis. Vous pouvez soit recibler ces utilisateurs pour qu'ils mettent à jour leur numéro de téléphone, soit les désabonner. 

Cette requête utilise l'éditeur incrémental et recherche les utilisateurs dont trois envois ou plus ont été rejetés au cours des 90 derniers jours et dont aucune réception/distribution n'a été effectuée.

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
## Recherchez des utilisateurs ayant des propriétés d'événement spécifiques et un nombre d'événements dans une période donnée.
{% apitags %}
Événement, Propriété, Plage de temps
{% endapitags %}

Trouvez les utilisateurs qui remplissent simultanément les conditions suivantes :

- Transaction d'une valeur totale supérieure à 500 $ (somme de plusieurs événements `Transact`)
- Transactions au centre commercial `Funan`
- Transactions effectuées plus de trois fois au cours des 90 derniers jours

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
## Sélectionnez les utilisateurs dont la dernière session s'est déroulée sur un modèle d'appareil spécifique.
{% apitags %}
Session, appareil
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
## Trouvez les utilisateurs qui ont sélectionné le deuxième bouton d'un message in-app dans une plage de temps spécifique.
{% apitags %}
Intervalle de temps
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
## Recherchez les utilisateurs qui ont acheté au cours de chacun des trois derniers mois calendaires.
{% apitags %}
Achat, Période
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
## Sélectionner les utilisateurs qui ont participé à un événement personnalisé avec une propriété spécifique lorsque la propriété est un nombre entier.
{% apitags %}
Evénement, Propriété
{% endapitags %}

Envoi d'un message aux utilisateurs qui ont regardé une série au cours des six derniers mois et qui s'apprêtent à quitter la plateforme. 

La propriété est l'ID du titre. Sinon, vous auriez dû inclure plus de 100 ID de titres dans un filtre. L’extension de segment incrémentielle peut être optimisée en termes de coûts et vous pouvez spécifier la plage de dates dans l'en-tête.

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
## Déterminez le nombre moyen d'e-mails qu'un utilisateur reçoit chaque jour.
{% apitags %}
Message
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
Pour les messages SMS, remplacez `USERS_MESSAGES_EMAIL_SEND_SHARED` par `USERS_MESSAGES_SMS_SEND_SHARED` dans la requête. Pour les notifications push, remplacez `USERS_MESSAGES_EMAIL_SEND_SHARED` par `USERS_MESSAGES_SMS_SEND_SHARED` dans la requête
{% endalert %}
{% endapi %}

{% api %}
## Déterminez le nombre moyen d'e-mails qu'un utilisateur reçoit chaque semaine.
{% apitags %}
Message
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
Pour les messages SMS, remplacez `USERS_MESSAGES_EMAIL_SEND_SHARED` par `USERS_MESSAGES_SMS_SEND_SHARED` dans la requête. Pour les notifications push, remplacez `USERS_MESSAGES_EMAIL_SEND_SHARED` par `USERS_MESSAGES_SMS_SEND_SHARED` dans la requête
{% endalert %}
{% endapi %}