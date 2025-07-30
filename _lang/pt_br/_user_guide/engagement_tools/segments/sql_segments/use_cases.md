---
nav_title: "Casos de uso"
article_title: Casos de Uso de Extensões de Segmento SQL
page_order: 2
page_type: glossary
layout: sql_segment_extensions_glossary
alias: "/sql_segments_use_cases/"
description: "Este artigo contém consultas testadas e comprovadas para extensões de segmento SQL."
tool: Segments
---

{% api %}
## Selecione os usuários pela quantidade de vezes que um evento ocorreu
{% apitags %}
Evento
{% endapitags %}

Selecione os usuários que abriram uma certa campanha de e-mail mais de uma vez no passado.

Isso também funciona para o limite de mensagens no app pelo número de impressões, como selecionar usuários com mais de três impressões como uma exclusão de segmento na mesma campanha. 

```sql
SELECT user_id FROM "USERS_MESSAGES_EMAIL_OPEN_SHARED"
WHERE campaign_api_id='8f7026dc-e9b7-40e6-bdc7-96cf58e80faa'
GROUP BY user_id
HAVING count(*) > 1
```
{% endapi %}

{% api %}
## Selecione os usuários que realizaram uma ação e some um valor de propriedade
{% apitags %}
Propriedade
{% endapitags %}

Selecione usuários que fizeram uma aposta em esportes com a soma de todas as suas apostas sendo maior que um certo valor.

```sql
select user_id from "USERS_BEHAVIORS_CUSTOMEVENT_SHARED"
where name='Bet On Sports'
group by 1 having sum(get_path(parse_json(properties), 'amount')) > 150
```
{% endapi %}

{% api %}
## Selecione usuários com base em quantas vezes um evento ocorreu em um intervalo de tempo
{% apitags %}
Evento, Intervalo de tempo
{% endapitags %}

Selecione usuários com mais de três aberturas de e-mail nos últimos 30 dias.

Isso também funciona para determinar os níveis de engajamento dos usuários, como usuários altamente responsivos em diferentes canais.

```sql
SELECT user_id, COUNT(DISTINCT id) AS num_emails_opened
FROM USERS_MESSAGES_EMAIL_OPEN_SHARED
WHERE to_timestamp_ntz(time) >= DATEADD(day, -30, CURRENT_TIMESTAMP()) AND to_timestamp_ntz(time) <= CURRENT_TIMESTAMP()
GROUP BY user_id;
HAVING COUNT(DISTINCT id) > 3
```
{% endapi %}

{% api %}
## Selecione usuários que registraram pelo menos um evento em vários intervalos de tempo
{% apitags %}
Evento, Intervalo de tempo
{% endapitags %}

Selecione os usuários que fizeram uma compra em cada um dos últimos quatro trimestres. Este segmento de usuário pode ser usado com [público sincronizado]({{site.baseurl}}/partners/canvas_audience_sync/) para identificar clientes semelhantes de alto valor para aquisição.

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
## Selecione qualquer compra com certas propriedades
{% apitags %}
Compra, Propriedade
{% endapitags %}

Selecione clientes que fizeram qualquer compra que contenha a propriedade `“type = shops”` em 14 dias. 

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
## Selecione usuários que receberam uma mensagem que não foi entregue
{% apitags %}
Mensagem, Entrega
{% endapitags %}

Selecione os usuários que receberam uma campanha de SMS ou canva, mas a mensagem não chegou à operadora. Por exemplo, a mensagem pode ter sido interrompida por um estouro de fila. 

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
## Encontre todas as mensagens SMS que foram enviadas, mas não chegaram à operadora devido ao estouro da fila
{% apitags %}
Mensagem, operadora
{% endapitags %}

Isso pode ser reutilizado para outros tipos de mensagens enviadas de uma canva específica que não foram entregues.

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
`CANVAS_ID` é o número após `/canvas/` na sua URL do canva.
{% endapi %}

{% api %}
## Selecione usuários que fizeram qualquer compra com uma matriz de propriedades contendo um valor específico
{% apitags %}
Compra, Propriedade
{% endapitags %}

```sql
SELECT DISTINCT EXTERNAL_USER_ID
FROM "USERS_BEHAVIORS_PURCHASE_SHARED",
LATERAL FLATTEN(input=>parse_json(properties):modifiers) as f
WHERE f.VALUE::STRING = 'Bacon'
```
{% endapi %}

{% api %}
## Encontre todos os usuários que tiveram vários erros 30003 e 0 entregas
{% apitags %}
Erro, Entrega
{% endapitags %}

Isso é útil para resolver situações em que você deseja parar de enviar para usuários que não estão recebendo mensagens, mas não estão sendo marcados como inválidos porque não possuem o código de erro necessário. Você pode redirecionar esses usuários para atualizar o número de telefone deles ou cancelar inscrição. 

Esta consulta usa o editor incremental e procura usuários com três ou mais envios rejeitados nos últimos 90 dias e zero entregas.

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
## Encontre usuários com propriedades de eventos específicas e contagens de eventos em um intervalo de tempo
{% apitags %}
Evento, Propriedade, Intervalo de tempo
{% endapitags %}

Encontre usuários que atendam às seguintes condições simultaneamente:

- Transacionou um valor total superior a $500 (a soma de vários `Transact` eventos)
- Transação no shopping `Funan`
- Transacionado mais de três vezes nos últimos 90 dias

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
## Selecione usuários cuja sessão mais recente foi em um modelo de dispositivo específico
{% apitags %}
Sessão, dispositivo
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
## Encontre usuários que selecionaram o segundo botão de uma mensagem no app em um intervalo de tempo específico
{% apitags %}
Período
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
## Encontre usuários que compraram em cada um dos últimos três meses do calendário
{% apitags %}
Compra, Intervalo de tempo
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
## Selecione usuários que completaram um evento personalizado com uma propriedade específica quando a propriedade é um número inteiro
{% apitags %}
Evento, Propriedade
{% endapitags %}

Enviando uma mensagem para usuários que assistiram a uma série nos últimos seis meses e estão prestes a deixar a plataforma. 

A propriedade é o ID do título; caso contrário, você precisaria incluir mais de 100 IDs de título em um filtro. A extensão de segmento incremental pode ser otimizada para custo e você pode especificar o intervalo de datas no cabeçalho.

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
## Encontre o número médio de e-mails que um usuário recebe diariamente
{% apitags %}
Mensagem
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
Para mensagens SMS, substitua `USERS_MESSAGES_EMAIL_SEND_SHARED` por `USERS_MESSAGES_SMS_SEND_SHARED` na consulta. Para notificações por push, substitua `USERS_MESSAGES_EMAIL_SEND_SHARED` por `USERS_MESSAGES_SMS_SEND_SHARED` na consulta
{% endalert %}
{% endapi %}

{% api %}
## Encontre o número médio de e-mails que um usuário recebe semanalmente
{% apitags %}
Mensagem
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
Para mensagens SMS, substitua `USERS_MESSAGES_EMAIL_SEND_SHARED` por `USERS_MESSAGES_SMS_SEND_SHARED` na consulta. Para notificações por push, substitua `USERS_MESSAGES_EMAIL_SEND_SHARED` por `USERS_MESSAGES_SMS_SEND_SHARED` na consulta
{% endalert %}
{% endapi %}