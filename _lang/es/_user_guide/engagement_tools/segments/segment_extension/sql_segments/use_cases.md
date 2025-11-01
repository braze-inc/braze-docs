---
nav_title: "Casos de uso"
article_title: Casos de uso de las extensiones de segmento SQL
page_order: 2
page_type: glossary
layout: sql_segment_extensions_glossary
alias: "/sql_segments_use_cases/"
description: "Este artículo contiene consultas probadas y demostradas para las extensiones de segmento SQL."
tool: Segments
---

{% api %}
## Seleccionar usuarios por el número de veces que se ha producido un suceso
{% apitags %}
Evento
{% endapitags %}

Selecciona los usuarios que abrieron una determinada campaña de correo electrónico más de una vez en el pasado.

Esto también funciona para la limitación de mensajes dentro de la aplicación por el número de impresiones, como la selección de usuarios con más de tres impresiones como exclusión de segmento en la misma campaña. 

```sql
SELECT user_id FROM "USERS_MESSAGES_EMAIL_OPEN_SHARED"
WHERE campaign_api_id='8f7026dc-e9b7-40e6-bdc7-96cf58e80faa'
GROUP BY user_id
HAVING count(*) > 1
```
{% endapi %}

{% api %}
## Selecciona los usuarios que realizaron una acción y suma un valor de propiedad
{% apitags %}
Propiedad
{% endapitags %}

Selecciona usuarios que hayan realizado una apuesta deportiva cuya suma de todas sus apuestas sea superior a una cantidad determinada.

```sql
select user_id from "USERS_BEHAVIORS_CUSTOMEVENT_SHARED"
where name='Bet On Sports'
group by 1 having sum(get_path(parse_json(properties), 'amount')) > 150
```
{% endapi %}

{% api %}
## Seleccionar usuarios en función de cuántas veces se ha producido un evento en un intervalo de tiempo
{% apitags %}
Suceso, intervalo de tiempo
{% endapitags %}

Selecciona usuarios con más de tres aperturas de correo electrónico en los últimos 30 días.

Esto también sirve para determinar los niveles de interacción de los usuarios, como los usuarios muy receptivos en distintos canales.

```sql
SELECT user_id, COUNT(DISTINCT id) AS num_emails_opened
FROM USERS_MESSAGES_EMAIL_OPEN_SHARED
WHERE to_timestamp_ntz(time) >= DATEADD(day, -30, CURRENT_TIMESTAMP()) AND to_timestamp_ntz(time) <= CURRENT_TIMESTAMP()
GROUP BY user_id;
HAVING COUNT(DISTINCT id) > 3
```
{% endapi %}

{% api %}
## Seleccionar usuarios que registraron al menos un evento en varios intervalos de tiempo
{% apitags %}
Suceso, intervalo de tiempo
{% endapitags %}

Selecciona los usuarios que realizaron una compra en cada uno de los últimos cuatro trimestres. Este segmento de usuarios puede utilizarse con la [sincronización de audiencias]({{site.baseurl}}/partners/canvas_audience_sync/) para identificar clientes similares de alto valor para la adquisición.

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
## Selecciona cualquier compra con determinadas propiedades
{% apitags %}
Compra, Propiedad
{% endapitags %}

Selecciona clientes que hayan realizado alguna compra que contenga la propiedad `“type = shops”` en 14 días. 

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
## Seleccionar usuarios a los que se envió un mensaje que no se entregó
{% apitags %}
Mensaje, entrega
{% endapitags %}

Selecciona los usuarios a los que se ha enviado una campaña SMS o Canvas, pero el mensaje no ha llegado al operador. Por ejemplo, el mensaje podría haberse detenido por un desbordamiento de la cola. 

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
## Encuentra todos los mensajes SMS que se enviaron pero no llegaron al operador por desbordamiento de la cola.
{% apitags %}
Mensaje, Operador
{% endapitags %}

Esto puede reutilizarse para otros tipos de mensajes enviados desde un Canvas concreto que no se hayan entregado.

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
`CANVAS_ID` es el número que aparece después de `/canvas/` en tu URL de Canvas.
{% endapi %}

{% api %}
## Selecciona usuarios que hayan realizado alguna compra con una matriz de propiedades que contenga un valor específico
{% apitags %}
Compra, Propiedad
{% endapitags %}

```sql
SELECT DISTINCT EXTERNAL_USER_ID
FROM "USERS_BEHAVIORS_PURCHASE_SHARED",
LATERAL FLATTEN(input=>parse_json(properties):modifiers) as f
WHERE f.VALUE::STRING = 'Bacon'
```
{% endapi %}

{% api %}
## Buscar todos los usuarios que tuvieron varios errores 30003 y 0 entregas
{% apitags %}
Error, entrega
{% endapitags %}

Esto es útil para resolver situaciones en las que quieres dejar de enviar a usuarios que no reciben mensajes, pero que no se marcan como no válidos porque no tienen el código de error requerido. Puedes reorientar a estos usuarios para que actualicen su número de teléfono o cancelar suscripción. 

Esta consulta utiliza el editor incremental y busca usuarios con tres o más envíos rechazados en los últimos 90 días y cero entregas.

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
## Buscar usuarios con propiedades del evento específicas y recuentos de eventos en un intervalo de tiempo
{% apitags %}
Suceso, propiedad, intervalo de tiempo
{% endapitags %}

Busca usuarios que cumplan simultáneamente las siguientes condiciones:

- Has realizado una transacción por un valor total superior a 500 $ (la suma de varios eventos `Transact` )
- Transacción en el centro comercial `Funan`
- Has realizado más de tres transacciones en los últimos 90 días

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
## Selecciona usuarios cuya sesión más reciente se haya realizado en un modelo de dispositivo concreto
{% apitags %}
Sesión, Dispositivo
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
## Encontrar usuarios que seleccionaron el segundo botón de un mensaje dentro de la aplicación en un intervalo de tiempo específico
{% apitags %}
Rango temporal
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
## Busca usuarios que hayan comprado en cada uno de los tres últimos meses naturales
{% apitags %}
Compra, intervalo de tiempo
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
## Seleccionar usuarios que completaron un evento personalizado con una propiedad específica cuando la propiedad es un número entero
{% apitags %}
Evento, Propiedad
{% endapitags %}

Enviar un mensaje a los usuarios que vieron una serie en los últimos seis meses y están a punto de abandonar la plataforma. 

La propiedad es el ID del título; de lo contrario, tendrías que incluir más de 100 ID de títulos en un filtro. La extensión incremental de segmento puede optimizarse en función del coste y puedes especificar el intervalo de fechas en la cabecera.

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
## Averigua el número medio de correos electrónicos que recibe un usuario al día
{% apitags %}
Mensaje
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
Para los mensajes SMS, sustituye `USERS_MESSAGES_EMAIL_SEND_SHARED` por `USERS_MESSAGES_SMS_SEND_SHARED` en la consulta. Para las notificaciones push, sustituye `USERS_MESSAGES_EMAIL_SEND_SHARED` por `USERS_MESSAGES_SMS_SEND_SHARED` en la consulta
{% endalert %}
{% endapi %}

{% api %}
## Averigua el número medio de correos electrónicos que recibe un usuario semanalmente
{% apitags %}
Mensaje
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
Para los mensajes SMS, sustituye `USERS_MESSAGES_EMAIL_SEND_SHARED` por `USERS_MESSAGES_SMS_SEND_SHARED` en la consulta. Para las notificaciones push, sustituye `USERS_MESSAGES_EMAIL_SEND_SHARED` por `USERS_MESSAGES_SMS_SEND_SHARED` en la consulta
{% endalert %}
{% endapi %}