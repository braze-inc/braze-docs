---
nav_title: "사용 사례"
article_title: SQL 세그먼트 확장 사용 사례
page_order: 2
page_type: glossary
layout: sql_segment_extensions_glossary
alias: "/sql_segments_use_cases/"
description: "이 문서에는 SQL 세그먼트 확장을 위해 테스트되고 검증된 쿼리가 포함되어 있습니다."
tool: Segments
---

{% api %}
## 이벤트가 발생한 횟수별로 사용자를 선택합니다.
{% apitags %}
이벤트
{% endapitags %}

과거에 특정 이메일 캠페인을 한 번 이상 열어본 사용자를 선택합니다.

이는 동일한 캠페인에서 노출 횟수가 3회를 초과하는 사용자를 세그먼트 제외 대상으로 선정하는 등 노출 횟수에 따른 인앱 메시지 제한에도 적용됩니다. 

```sql
SELECT user_id FROM "USERS_MESSAGES_EMAIL_OPEN_SHARED"
WHERE campaign_api_id='8f7026dc-e9b7-40e6-bdc7-96cf58e80faa'
GROUP BY user_id
HAVING count(*) > 1
```
{% endapi %}

{% api %}
## 작업을 수행한 사용자를 선택하고 속성 값을 합산합니다.
{% apitags %}
속성
{% endapitags %}

스포츠에 베팅한 모든 베팅의 합계가 일정 금액 이상인 사용자를 선택합니다.

```sql
select user_id from "USERS_BEHAVIORS_CUSTOMEVENT_SHARED"
where name='Bet On Sports'
group by 1 having sum(get_path(parse_json(properties), 'amount')) > 150
```
{% endapi %}

{% api %}
## 시간 범위에서 이벤트가 발생한 횟수를 기준으로 사용자를 선택합니다.
{% apitags %}
이벤트, 시간 범위
{% endapitags %}

지난 30일 동안 이메일을 세 번 이상 열어본 사용자를 선택합니다.

이는 여러 채널에서 반응이 높은 사용자 등 사용자의 참여 수준을 파악하는 데도 유용합니다.

```sql
SELECT user_id, COUNT(DISTINCT id) AS num_emails_opened
FROM USERS_MESSAGES_EMAIL_OPEN_SHARED
WHERE to_timestamp_ntz(time) >= DATEADD(day, -30, CURRENT_TIMESTAMP()) AND to_timestamp_ntz(time) <= CURRENT_TIMESTAMP()
GROUP BY user_id;
HAVING COUNT(DISTINCT id) > 3
```
{% endapi %}

{% api %}
## 여러 시간 범위에 걸쳐 하나 이상의 이벤트를 기록한 사용자를 선택합니다.
{% apitags %}
이벤트, 시간 범위
{% endapitags %}

지난 4분기 각각에 구매를 한 사용자를 선택합니다. 이 사용자 세그먼트는 [오디언스 동기화와]({{site.baseurl}}/partners/canvas_audience_sync/) 함께 사용하여 가치가 높은 유사 고객을 식별하여 고객 확보에 활용할 수 있습니다.

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
## 특정 속성을 가진 구매를 선택합니다.
{% apitags %}
구매, 속성정보
{% endapitags %}

14일 이내에 `“type = shops”` 속성이 포함된 구매를 한 고객을 선택합니다. 

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
## 전달되지 않은 메시지를 받은 사용자를 선택합니다.
{% apitags %}
메시지, 전달
{% endapitags %}

SMS 캠페인 또는 캔버스를 전송했지만 메시지가 이동 통신사에 전달되지 않은 사용자를 선택합니다. 예를 들어 대기줄이 넘쳐서 메시징이 중지되었을 수 있습니다. 

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
## 전송되었지만 대기줄 초과로 인해 이동 통신사에 도달하지 못한 모든 SMS 메시지 찾기
{% apitags %}
메시지, 캐리어
{% endapitags %}

특정 캔버스에서 전송되었지만 전달되지 않은 다른 유형의 메시징을 위해 용도를 변경할 수 있습니다.

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
`CANVAS_ID` 는 캔버스 URL의 `/canvas/` 뒤에 오는 숫자입니다.
{% endapi %}

{% api %}
## 특정 값이 포함된 속성 배열로 구매를 한 사용자를 선택합니다.
{% apitags %}
구매, 속성정보
{% endapitags %}

```sql
SELECT DISTINCT EXTERNAL_USER_ID
FROM "USERS_BEHAVIORS_PURCHASE_SHARED",
LATERAL FLATTEN(input=>parse_json(properties):modifiers) as f
WHERE f.VALUE::STRING = 'Bacon'
```
{% endapi %}

{% api %}
## 30003 오류가 여러 번 발생하고 전달이 0건인 모든 사용자 찾기
{% apitags %}
오류, 전달
{% endapitags %}

이는 메시지를 받지 못했지만 필요한 오류 코드가 없어 무효로 표시되지 않는 사용자에게 더 이상 메시지를 보내지 않으려는 상황을 해결하는 데 유용합니다. 이러한 사용자를 리타겟팅하여 휴대폰 번호를 업데이트하거나 탈퇴할 수 있습니다. 

이 쿼리는 증분 편집기를 사용하여 지난 90일 동안 전송이 거부된 횟수가 3회 이상이고 전달 건수가 0건인 사용자를 찾습니다.

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
## 특정 이벤트 속성정보 및 이벤트 횟수가 있는 사용자를 시간 범위에서 찾기
{% apitags %}
이벤트, 속성, 시간 범위
{% endapitags %}

다음 조건을 동시에 충족하는 사용자를 찾습니다:

- 총 금액이 $500(여러 `Transact` 이벤트의 합계)보다 큰 트랜잭션이 발생한 경우
- 쇼핑몰에서 트랜잭션 발생 `Funan`
- 지난 90일 동안 3회 이상 트랜잭션이 발생한 경우

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
## 특정 기기 모델에서 가장 최근 세션이 있었던 사용자를 선택합니다.
{% apitags %}
세션, 기기
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
## 특정 시간 범위에서 인앱 메시지의 두 번째 버튼을 선택한 사용자 찾기
{% apitags %}
시간 범위
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
## 지난 3개월 동안 각각 캘린더에서 구매한 사용자 찾기
{% apitags %}
구매, 시간 범위
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
## 속성이 정수인 경우 특정 속성으로 커스텀 이벤트를 완료한 사용자를 선택합니다.
{% apitags %}
이벤트, 속성정보
{% endapitags %}

지난 6개월 동안 시리즈를 시청하고 플랫폼을 떠나려고 하는 사용자에게 메시지를 보냅니다. 

속성은 제목 ID이며, 그렇지 않으면 필터에 100개 이상의 제목 ID를 포함해야 합니다. 증분 세그먼트 확장은 비용에 맞게 최적화할 수 있으며 헤더에 날짜 범위를 지정할 수 있습니다.

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
## 사용자가 매일 수신하는 평균 이메일 수 찾기
{% apitags %}
메시지
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
SMS 메시징의 경우 쿼리에서 `USERS_MESSAGES_EMAIL_SEND_SHARED` 을 `USERS_MESSAGES_SMS_SEND_SHARED` 으로 바꿉니다. 푸시 알림의 경우 쿼리에서 `USERS_MESSAGES_EMAIL_SEND_SHARED` 을 `USERS_MESSAGES_SMS_SEND_SHARED` 으로 바꿉니다.
{% endalert %}
{% endapi %}

{% api %}
## 사용자가 매주 받는 평균 이메일 수 찾기
{% apitags %}
메시지
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
SMS 메시징의 경우 쿼리에서 `USERS_MESSAGES_EMAIL_SEND_SHARED` 을 `USERS_MESSAGES_SMS_SEND_SHARED` 으로 바꿉니다. 푸시 알림의 경우 쿼리에서 `USERS_MESSAGES_EMAIL_SEND_SHARED` 을 `USERS_MESSAGES_SMS_SEND_SHARED` 으로 바꿉니다.
{% endalert %}
{% endapi %}