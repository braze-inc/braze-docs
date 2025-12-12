---
nav_title: "ユースケース"
article_title: SQL セグメントエクステンションのユースケース
page_order: 2
page_type: glossary
layout: sql_segment_extensions_glossary
alias: "/sql_segments_use_cases/"
description: "この記事には、SQL セグメントエクステンションのテスト済みおよび実証済みのクエリが含まれています。"
tool: Segments
---

{% api %}
## イベントが発生した回数に基づいてユーザーを選択する
{% apitags %}
イベント
{% endapitags %}

過去に特定のメールキャンペーンを複数回開いたユーザーを選択します。

これは、同じキャンペーンでセグメント排除として3つ以上のインプレッションを持つユーザーを選択するなど、インプレッション数によるアプリ内メッセージキャップにも役立ちます。 

```sql
SELECT user_id FROM "USERS_MESSAGES_EMAIL_OPEN_SHARED"
WHERE campaign_api_id='8f7026dc-e9b7-40e6-bdc7-96cf58e80faa'
GROUP BY user_id
HAVING count(*) > 1
```
{% endapi %}

{% api %}
## アクションを実行したユーザーを選択し、プロパティ値を合計する
{% apitags %}
プロパティ
{% endapitags %}

スポーツに賭けたユーザーのうち、賭け金の合計が一定額以上のユーザーを選択します。

```sql
select user_id from "USERS_BEHAVIORS_CUSTOMEVENT_SHARED"
where name='Bet On Sports'
group by 1 having sum(get_path(parse_json(properties), 'amount')) > 150
```
{% endapi %}

{% api %}
## 時間範囲内でイベントが発生した回数に基づいてユーザーを選択する
{% apitags %}
イベント、時間範囲
{% endapitags %}

過去30日間に開いたメールが3件以上あるユーザーを選択します。

これは、さまざまなチャネルで応答性の高いユーザーなど、ユーザのエンゲージメントレベルを決定するためにも機能します。

```sql
SELECT user_id, COUNT(DISTINCT id) AS num_emails_opened
FROM USERS_MESSAGES_EMAIL_OPEN_SHARED
WHERE to_timestamp_ntz(time) >= DATEADD(day, -30, CURRENT_TIMESTAMP()) AND to_timestamp_ntz(time) <= CURRENT_TIMESTAMP()
GROUP BY user_id;
HAVING COUNT(DISTINCT id) > 3
```
{% endapi %}

{% api %}
## 複数の時間範囲にわたって少なくとも1つのイベントを記録したユーザーを選択する
{% apitags %}
イベント、時間範囲
{% endapitags %}

過去4四半期ごとに購入したユーザーを選択します。このユーザーセグメントは、[audience sync]({{site.baseurl}}/partners/canvas_audience_sync/) で使用して、獲得する価値の高い類似顧客を識別できます。

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
## 特定のプロパティを持つ購入を選択する
{% apitags %}
購入プロパティ
{% endapitags %}

14 日以内にプロパティ `“type = shops”` を含む購入を行った顧客を選択します。 

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
## 配信されなかったメッセージが送信されたユーザーを選択する
{% apitags %}
メッセージ、配信
{% endapitags %}

SMSキャンペーンまたはCanvasが送信されたが、メッセージが通信事業者に到達しなかったユーザーを選択します。たとえば、メッセージがキューオーバーフローによって停止した可能性があります。 

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
## 送信されたが、キューオーバーフローのために通信事業者に到達しなかったすべての SMS メッセージを検索する
{% apitags %}
メッセージ、通信事業者
{% endapitags %}

これは、配信されていない特定のキャンバスから送信された他のタイプのメッセージに対して再利用できます。

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
`CANVAS_ID` は、キャンバス URL の`/canvas/` の後の番号です。
{% endapi %}

{% api %}
## 特定の値を含むプロパティ配列を含む購入を行ったユーザーを選択する
{% apitags %}
購入プロパティ
{% endapitags %}

```sql
SELECT DISTINCT EXTERNAL_USER_ID
FROM "USERS_BEHAVIORS_PURCHASE_SHARED",
LATERAL FLATTEN(input=>parse_json(properties):modifiers) as f
WHERE f.VALUE::STRING = 'Bacon'
```
{% endapi %}

{% api %}
## 30003エラーが複数回発生し、配信数が0のすべてのユーザーを検索する
{% apitags %}
エラー、配信
{% endapitags %}

これは、メッセージの受信に失敗したが、必要なエラーコードがないために無効としてマークされていないユーザーへの送信を停止する場合に役立ちます。これらのユーザーをリターゲティングして電話番号を更新するか、配信停止することができます。 

このクエリはインクリメンタルエディタを使用し、過去90日間に送信が3回以上拒否され、配信が0回のユーザーを検索します。

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
## 特定のイベントプロパティと時間範囲内のイベント数を持つユーザーを検索する
{% apitags %}
イベント、プロパティ、時間範囲
{% endapitags %}

次の条件を同時に満たすユーザーを検索します。

- 合計金額が$500 (複数の `Transact` イベントの合計) を超える取引を行いました
- モール `Funan` での取引
- 過去90日間で3回以上取引

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
## 特定のデバイスモデルで最後のセッションを行ったユーザーを選択する
{% apitags %}
セッション、デバイス
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
## 特定の時間範囲でアプリ内メッセージの2番目のボタンを選択したユーザーを検索する
{% apitags %}
期間
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
## 過去3か月の各月に購入したユーザーの検索
{% apitags %}
購入、時間範囲
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
## プロパティが整数の場合、特定のプロパティを持つカスタムイベントを完了したユーザーを選択する
{% apitags %}
イベント、プロパティ
{% endapitags %}

過去6カ月間にシリーズを視聴し、プラットフォームを離れようとしているユーザーにメッセージを送信する。 

このプロパティはタイトルID です。それ以外の場合は、フィルターに100以上のタイトル ID を含める必要があります。増分セグメントエクステンションはコストに合わせて最適化でき、ヘッダーで日付範囲を指定できます。

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
## ユーザーが1日に受信するメールの平均数を調べる
{% apitags %}
メッセージ
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
SMS メッセージの場合は、クエリの `USERS_MESSAGES_EMAIL_SEND_SHARED` を `USERS_MESSAGES_SMS_SEND_SHARED` に置き換えます。プッシュ通知の場合は、クエリの `USERS_MESSAGES_EMAIL_SEND_SHARED` を`USERS_MESSAGES_SMS_SEND_SHARED` に置き換えます
{% endalert %}
{% endapi %}

{% api %}
## ユーザーが毎週受信する平均メール数を調べる
{% apitags %}
メッセージ
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
SMS メッセージの場合は、クエリの `USERS_MESSAGES_EMAIL_SEND_SHARED` を `USERS_MESSAGES_SMS_SEND_SHARED` に置き換えます。プッシュ通知の場合は、クエリの `USERS_MESSAGES_EMAIL_SEND_SHARED` を`USERS_MESSAGES_SMS_SEND_SHARED` に置き換えます
{% endalert %}
{% endapi %}