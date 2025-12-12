---
nav_title: 流動ユースケース ライブラリー
article_title: リキッド ユースケース ライブラリ
page_order: 10
search_rank: 2
excerpt_separator: ""
page_type: glossary
layout: liquid_use_case_glossary
description: "このランディングページには、記念日、アプリの使用状況、カウントダウンなど、カテゴリー別に整理されたリキッドのユースケースのサンプルが掲載されている。"

---

{% api %}

## 記念日と祝日

{% apitags %}
記念日と祝日
{% endapitags %}

- [ユーザーの記念年に基づいてメッセージをパーソナライズする](#anniversary-year)
- [ユーザーの誕生週に基づいてメッセージをパーソナライズする。](#birthday-week)
- [ユーザーの誕生月にキャンペーンを送信する](#birthday-month)
- [大型連休にメッセージを送るのは避ける](#holiday-avoid)

### ユーザーの記念年に基づいてメッセージをパーソナライズする {#anniversary-year}

このユースケースでは、ユーザーの最初の登録日に基づいてユーザーのアプリ記念日を計算し、何周年を祝うかによって異なるメッセージを表示する方法を説明します。

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %} 
{% assign this_day = 'now' | date: "%d" %}
{% assign anniversary_month = {{custom_attribute.${registration_date}}} | date: "%B" %}
{% assign anniversary_day = {{custom_attribute.${registration_date}}} | date: "%d" %}
{% assign anniversary_year = {{custom_attribute.${registration_date}}} | date: "%Y" %}

{% if this_month == anniversary_month %} 
{% if this_day == anniversary_day %} 
{% if anniversary_year == '2021' %}
Exactly one year ago today we met for the first time!

{% elsif anniversary_year == '2020' %}
Exactly two years ago today we met for the first time!

{% elsif anniversary_year == '2019' %}
Exactly three years ago today we met for the first time!

{% else %}
{% abort_message("Not same year") %}
{% endif %}

{% else %} 
{% abort_message("Not same day") %} 
{% endif %}

{% else %}
{% abort_message("Not same month") %}
{% endif %}
```
{% endraw %}

**説明:**ここでは予約変数 `now` を使用して、[ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) 形式で現在の日付と時刻をテンプレート化します。フィルター `%B` (「5 月」などの月) および `%d` (「18」などの日) は、現在の月と日の形式を設定します。次に、`signup_date` の値に同じ日付と時間のフィルターを使い、条件タグとロジックを使って2つの値を比較できるようにする。

そして、さらに 3 つの変数ステートメントを繰り返して、`signup_date` の `%B` と `%d` を取得し、`%Y` (「2021」などの年) も追加します。これにより、`signup_date` の日付と時刻が年号だけになる。日と月が分かると、そのユーザーの記念日が今日かどうかを確認することができ、年が分かると、何年経ったかが分かります。したがって、何周年を祝うかを知ることができます。

{% alert tip %}登録日を収集した年数を上限に、その数の条件を作成できます。{% endalert %}  

### ユーザーの誕生週に基づいてメッセージをパーソナライズする。 {#birthday-week}

このユースケースは、ユーザーの誕生日を見つけ、現在の日付と比較し、誕生日の週の前、中、後に特別な誕生日メッセージを表示する方法を示している。

{% raw %}
```liquid
{% assign this_week = 'now' | date: '%W' %}
{% assign birthday_week = ${date_of_birth}  | date: '%W' %}
{% assign last_week = {{this_week}} | minus: 1 %}
{% assign next_week = {{this_week}} | plus: 1 %}
{% assign birthday_week_conversion = {{birthday_week}} | plus: 0 %}
{% if {{last_week}} == {{birthday_week_conversion}} %}
Happy birthday for last week!
{% elsif {{birthday_week}} == {{this_week}} %}
Happy birthday for this week!
{% elsif {{next_week}} == {{birthday_week_conversion}} %}
Happy birthday for next week!
{% else %}
No birthday for you!
{% endif %}
```
{% endraw %}

**説明:**[周年記念日](#anniversary-year)のユースケースと同様に、ここでは予約変数 `now` と `%W` フィルター (1 年 52週のうち 12 週目など) を使用して、ユーザーの誕生日を含む年の週番号を取得します。ユーザーの誕生週が現在の週と一致すれば、お祝いのメッセージを送る！ 

メッセージングをさらにパーソナライズするために、`last_week` および `next_week` のステートメントも含めています。

### ユーザーの誕生月にキャンペーンを送る {#birthday-month}

このユースケースは、ユーザーの誕生月を計算し、誕生月が当月かどうかをチェックし、当月であれば特別なメッセージを送信する方法を示している。

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
{% if {{this_month}} == {{birth_month}} %}
Message body 
{% else %} 
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}

**説明:**[誕生週](#birthday-week)のユースケースと似ていますが、ここでは `%B` フィルター (「5 月」などの月) を使用して、今月誕生日を迎えるユーザーを計算します。毎月のEメールに誕生日のユーザーを登場させるといった応用が考えられる。

### 大型連休にメッセージを送るのは避ける {#holiday-avoid}

このユースケースでは、エンゲージメントが低い傾向のある大型連休の日を避けつつ、連休中にメッセージを送信する方法を説明します。

{% raw %}
```liquid
{% assign today = 'now' | date: '%Y-%m-%d' %}
{% if today == "2023-12-24" or today == "2023-12-25" or today == "2023-12-26" %}
{% abort_message %}
{% else %}
Message if today isn't one of the provided holidays.
{% endif %}
```
{% endraw %}

**説明:**ここでは、フィルター `%Y` (「2023」などの年)、フィルター `%m` (「12」などの月)、およびフィルター `%d` (「25」などの日) を使用して、用語 `today` に予約変数 `now` (現在の日時) を代入し、日付の形式を設定します。次に条件付きステートメントを実行し、選択した休日と変数 `today` が一致した場合はメッセージを中止します。 

この例では、クリスマス・イブ、クリスマス・デー、ボクシング・デー（クリスマスの翌日）を使用している。

{% endapi %}

{% api %}

## アプリの利用状況

{% apitags %}
アプリの利用状況
{% endapitags %}

- [ユーザーがセッションを記録した場合、そのユーザーの言語でメッセージを送信する。](#app-session-language)
- [ユーザーが最後にアプリを開いた日に基づいてメッセージをパーソナライズする。](#app-last-opened)
- [ユーザーが最後にアプリを使用したのが3日以内の場合、別のメッセージを表示する。](#app-last-opened-less-than)

### ユーザーがセッションを記録していない場合、そのユーザーの言語でメッセージを送信する。 {#app-session-language}

このユースケースは、ユーザがセッションを記録したかどうかをチェックし、もし記録していなければ、カスタム属性を介して手動で収集した言語に基づいてメッセージを表示するロジックを含む。アカウントに言語情報がない場合は、デフォルトの言語でメッセージが表示される。もしユーザーがセッションを記録していれば、そのユーザーに結びついた言語情報を引き出し、適切なメッセージを表示する。 

{% raw %}
```liquid
{% if {{${last_used_app_date}}} == nil %}
{% if {{custom_attribute.${user_language}}} == 'en' %}
Message in English based on custom attribute
{% elsif {{custom_attribute.${user_language}}} == 'fr' %}
Message in French based on custom attribute
{% else %}
Does not have language - Default language
{% endif %}
{% else %}
{% if ${language} == 'en' %}
Message in English based on Language
{% elsif ${language} == 'fr' %}
Message in French based on Language
{% else %}
Has language - Default language
{% endif %}
{% endif %}
```
{% endraw %}

{% raw %}
**説明:**ここでは、2つのグループ化された`if` ステートメントを入れ子にして使っている。最初の `if` ステートメントは、`last_used_app_date` が `nil` かどうかをチェックすることによって、ユーザーがセッションを開始したかどうかを確認します。これは、ユーザーがセッションを記録するときに、`{{${language}}}` がSDKによって自動的に収集されるためです。ユーザーのセッションがログに記録されていない場合、ユーザーの言語はまだ不明です。そのため、言語関連のカスタム属性が保存されているかどうかをチェックして、可能であればその情報に基づいて、その言語でメッセージを表示します。
{% endraw %}

2 番目の`if` ステートメントは、標準 (デフォルト) の属性をチェックするだけです。ユーザーの `last_used_app_date` が `nil` ではなく (つまり、ユーザーがセッションを記録済み)、ユーザーの言語が分かっているためです。

{% alert note %}
[`Nil`](https://shopify.github.io/liquid/basics/types/#nil) は予約変数で、リキッドコードの結果がないときに返される。`Nil` は、`if` ブロックの中では、`false` として扱われる。
{% endalert %}

### ユーザーが最後にアプリを開いた日に基づいてメッセージをパーソナライズする。 {#app-last-opened}

このユースケースは、ユーザーが最後にアプリを開いた時間を計算し、時間の長さに応じて異なるパーソナライズされたメッセージを表示する。

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Happy to see you again!
{% else %}
It's been a while; here are some of our latest updates.
{% endif %}
```
{% endraw %}

### ユーザーが最後にアプリを使用したのが3日以内の場合、別のメッセージを表示する。 {#app-last-opened-less-than}

このユースケースでは、ユーザーがアプリを最後に使用してからの経過時間を計算し、その長さに応じてパーソナライズされた異なるメッセージを表示します。

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Message for a recently active user
{% else %}
Message for a less active user
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## カウントダウン

{% apitags %}
カウントダウン
{% endapitags %}

- [今日の日付にX日を加える](#countdown-add-x-days)
- [設定した時間からカウントダウンを計算する](#countdown-difference-days)
- [特定の出荷日と優先順位に関するカウントダウンを作成する](#countdown-shipping-options)
- [日単位でカウントダウンを作成する](#countdown-days)
- [日、時間、分のカウントダウンを作成する](#countdown-dynamic)
- [特定の日付までの残り日数を表示する](#countdown-future-date)
- [カスタム日付属性が到着するまでの残り日数を表示する](#countdown-custom-date-attribute)
- [残り時間を表示し、X時間しかない場合はメッセージを中断する。](#countdown-abort-window)
- [ユーザーのメンバーシップが終了する X 日前に送信するアプリ内メッセージ](#countdown-membership-expiry)
- [ユーザーの日付と言語に基づいて、アプリ内メッセージをパーソナライズする。](#countdown-personalize-language)
- [今から 30 日後の日付を月と日の形式でテンプレート化する](#countdown-template-date)

### 今日の日付にx日を加える {#countdown-add-x-days}

このユースケースは、現在の日付に特定の日数を追加して参照し、メッセージに追加する。例えば、週の半ばに週末のイベントを紹介するメッセージを送りたい場合がある。

{% raw %}
```liquid
Here are the movies we're showing on {{ "now" | date:'%s' | plus:259200 | date:"%F" }}!
```
{% endraw %}

`plus` の値は常に秒単位であるため、最終的にフィルター `%F` を使用して秒数を日数に変換します。

{% alert important %}
メッセージにイベントのリストへのURLやディープリンクを含めると、ユーザーを将来起こるアクションのリストに送ることができる。
{% endalert %}

### 設定した時間からカウントダウンを計算する {#countdown-difference-days}

このユースケースは、特定の日付と現在の日付の日数の差を計算する。この違いを利用して、ユーザーにカウントダウンを表示することができる。

{% raw %}
```liquid
{% assign event_date = '2023-12-31' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
you have {{ difference_days }} days left!
```
{% endraw %}

### 特定の出荷日と優先順位に関するカウントダウンの作成{#countdown-shipping-options}

この使用例では、さまざまな配送オプションを取得し、受け取りにかかる時間を計算し、特定の日付までに荷物を受け取れるよう、ユーザーに購入を促すメッセージを表示する。

{% raw %}
```liquid
{% assign standard_shipping_start = "2023-12-10T00:00-05:00" | date: "%s" %}
{% assign standard_shipping_end = "2023-12-20T13:00-05:00" | date: "%s" %}
{% assign express_shipping_end = "2023-12-22T24:00-05:00" | date: "%s" %}
{% assign overnight_shipping_end = "2023-12-23T24:00-05:00" | date: "%s" %}
{% assign today = 'now' | date: "%s" %}

{% assign difference_s = standard_shipping_end | minus: today %}
{% assign difference_s_days = difference_s | divided_by: 86400.00 | round %}
{% assign difference_e = express_shipping_end | minus: today %}
{% assign difference_e_days = difference_e | divided_by: 86400.00 | round %}
{% assign difference_o = overnight_shipping_end | minus: today %}
{% assign difference_o_days = difference | divided_by: 86400.00 | round %}

{% if today >= standard_shipping_start and today <= standard_shipping_end %}
{% if difference_s_days == 0 %}
This is the last day to order with standard shipping, so your order gets here on time for Christmas Eve!
{% elsif difference_s_days == 1 %}
There is {{difference_s_days}} day left to order with standard shipping, so your order gets here on time for Christmas Eve!

{% else %}
There are {{difference_s_days}} days left to order with standard shipping so your order gets here on time for Christmas Eve!
{% endif %}
{% elsif today > standard_shipping_end and today < express_shipping_end %}
{% if difference_e_days == 1 %}
There is {{difference_e_days}} day left to order with express shipping, so your order gets here on time for Christmas Eve!
{% else %}
There are {{difference_e_days}} days left to order with express shipping so your order gets here on time for Christmas Eve!
{% endif %}
{% elsif today >= express_shipping_end and today < overnight_shipping_end %}
This is the last day for overnight shipping so your order gets here on time for Christmas Eve!
{% else %}
{% abort_message("Unable to order and ship in time") %}
{% endif %}
```
{% endraw %}

### 日単位でカウントダウンを作成する {#countdown-days}

このユースケースは、特定のイベントから現在の日付までの残り時間を計算し、イベントまであと何日かを表示する。

{% raw %}
```liquid
{% assign event_date = {{custom_attribute.${last_selected_event_date}}} | date: "%s" %}
{% assign today =  'now' | date: "%s"  %}
{% assign difference =  event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Your order will arrive in {{ difference_days }} days!
```
{% endraw %}

{% alert important %}
`date` の値を持つカスタム属性 フィールドが必要です。
{% endalert %}

### 日、時間、分のカウントダウンを作成する {#countdown-dynamic}

このユースケースは、特定のイベントから現在の日付までの残り時間を計算する。イベントまでの残り時間に応じて、時間値（日、時間、分）が変更され、パーソナライズされたさまざまなメッセージが表示される。

例えば、顧客の注文が届くまで 2 日かかる場合、「ご注文は 2 日後に届きます」と表示できます。一方、1 日未満の場合は、「ご注文は 17 時間以内に到着します」と変更できます。

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign scheme_finish = "2017-10-13T10:30:30" | date: "%s" %}
{% assign difference_seconds =  scheme_finish | minus: today %}
{% assign difference_minutes = difference_seconds | divided_by: 60 %}
{% assign difference_hours = difference_seconds | divided_by: 3600 %}
{% assign difference_days = difference_seconds | divided_by: 86400 %}
{% if {{difference_minutes}} > 59 and {{difference_minutes}} < 1440 %}
You have {{difference_hours}} hours left till your order arrives!
{% elsif {{difference_minutes}} < 59 %}
You have {{difference_minutes}} minutes left till your order arrives!
{% else %}
You have {{difference_days}} days left till your order arrives!
{% endif %}
```
{% endraw %}

{% alert important %}
`date` の値を持つカスタム属性 フィールドが必要です。また、日数、時間数、分数で表示する時間のしきい値を設定する必要もあります。
{% endalert %}

### 特定の日付までの残り日数を表示する {#countdown-future-date}

このユースケースは、現在の日付と将来のイベントの日付の差を計算し、イベントまであと何日かを示すメッセージを表示する。

{% raw %}
```liquid
{% assign event_date = '2024-01-15' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
There are {{difference_days}} days until your birthday!
```
{% endraw %}

### カスタム日付属性が到着するまでの残り日数を表示する {#countdown-custom-date-attribute}

このユースケースは、現在の日付と将来の日付の日数の差を計算し、その差が設定された数値と一致した場合にメッセージを表示する。

この例では、ユーザーはカスタム日付属性から2日以内にメッセージを受け取る。そうでなければ、メッセージは送信されない。

{% raw %}
```liquid
{% assign today = 'now' | date: '%j' | plus: 0 %}
{% assign surgery_date = {{custom_attribute.${surgery_date}}} | date: '%j' | plus: 0 %}

{% assign difference_days = {{surgery_date}} | minus: {{today}} %}
{% if difference_days == 2 %}
Your surgery is in 2 days on {{custom_attribute.${surgery_date}}}
{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### 残り時間を表示し、残り時間がx時間しかない場合はメッセージを中断する。 {#countdown-abort-window}

このユースケースは、ある日付までの時間を計算し、その長さに応じて（日付が近すぎる場合はメッセージをスキップする）、パーソナライズされたさまざまなメッセージを表示する。 

例えば、"ロンドン行きの航空券を買うのにあと○時間残っています "といったメッセージだが、ロンドン行きのフライト時間まで2時間以内であれば送信しない。

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign dep_time = {{event_properties.${outboundDate}}} | date: "%s" %}
{% assign time_to_dep = dep_time | minus: today %}
{% if {{time_to_dep}} < 7200 %}
{% abort_message("OutboundDate less than 2 hours") %}
{% elsif {{time_to_dep}} > 7200 and {{time_to_dep}} < 86400 %}
Don't forget to buy your ticket to {{event_properties.${toStation}}} within next 24 hours!
{% else %}
Still traveling to {{event_properties.${toStation}}} in more than 24 hours? Book now!
{% endif %}
```
{% endraw %}

{% alert important %} カスタムイベントプロパティが必要です。 {% endalert %}

### ユーザーのメンバーシップが終了する x 日前に送信するアプリ内メッセージ{#countdown-membership-expiry}

このユースケースでは、メンバーシップの有効期限を取得し、それまでの期間を計算して、有効期限までの期間に応じて異なるメッセージを表示します。

{% raw %}
```liquid
{% assign membership_expiry = {{custom_attribute.${membership_expiry_date}}} | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = membership_expiry | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}

{% if difference_days > 4 and difference_days <= 7 %}
You have {{difference_days}} days left in your trial, make sure you upgrade!

{% elsif difference_days > 2 and difference_days <= 4 %}
HURRY! You have {{difference_days}} days left in your trial, make sure you upgrade!

{% elsif difference_days == 2 %}
LAST CHANCE! You have {{difference_days}} days left in your trial. Make sure you upgrade!

{% else %}
You have few days left in your trial. Make sure to upgrade!
{% endif %}
```
{% endraw %}

### ユーザーの日付と言語に基づいてアプリ内メッセージをパーソナライズする {#countdown-personalize-language}

このユースケースは、イベントまでのカウントダウンを計算し、ユーザーの言語設定に基づいて、その言語でカウントダウンを表示する。

例えば、月に一度、4回のアプリ内メッセージでオファーの有効期限を知らせるアップセルメッセージをユーザーに送ることができる：

- 初回
- 残り2日
- 残り1日
- 最終日

{% raw %}
```liquid
{% assign today = 'now' | date: "%s" %}
{% assign end_date = "2021-04-16T23:59:59" | date: "%s" %}
{% assign difference = end_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
{% if {{difference_days}} >= 3 %}
{% if ${language} == 'de' %}

Hallo, das Angebot gilt bis zum 16.04.

{% elsif ${language} == 'ch' %}
Grüezi, das Angebot gilt bis zum 16.04.

{% elsif ${language} == 'en' %}
The offer is valid until 16.04.

{% else %}
The offer is valid until 16.04.

{% endif %}
{% elsif {{difference_days}} == 2 %}
{% if ${language} == 'de' %}
INSERT MESSAGE

{% elsif ${language} == 'ch' %}
INSERT MESSAGE

{% elsif ${language} == 'en' %}
INSERT MESSAGE

{% else %}
INSERT MESSAGE
{% endif %}

{% elsif {{difference_days}} == 1 %}
{% if ${language} == 'de' %}
INSERT MESSAGE

{% elsif ${language} == 'ch' %}
INSERT MESSAGE

{% elsif ${language} == 'en' %}
INSERT MESSAGE

{% else %}
INSERT MESSAGE
{% endif %}

{% elsif {{difference_days}} == 0 %}
{% if ${language} == 'de' %}
Hallo, das Angebot gilt noch heute.

{% elsif ${language} == 'ch' %}
Hallo, das Angebot gilt noch heute.

{% elsif ${language} == 'en' %}
Grüezi, das Angebot gilt noch heute.

{% else %}
Hi, the offer is only valid today.
{% endif %}

{% else %}
{% abort_message("Calculation failed") %}
{% endif %}
```
{% endraw %}

{% alert important %}
指定した日付が日付範囲外の場合は、`date` の値を代入し、中止トロジックを含める必要があります。正確な日数を計算するには、代入する最終日に 23 時 59 分 59秒を含める必要があります。
{% endalert %}

### 今から 30 日後の日付を月と日の形式でテンプレート化{#countdown-template-date}

このユースケースでは、今から 30 日後の日付をメッセージングに表示します。

{% raw %}
```liquid
{% assign today = 'now' | date: "%s" %}
{% assign thirty_days = today | plus: 2592000 | date: "%B %d" %}
```
{% endraw %}

{% endapi %}

{% api %}

## カスタム属性

{% apitags %}
カスタム属性
{% endapitags %}

- [一致するカスタム属性に基づいてメッセージをパーソナライズする](#attribute-matching)
- [2つのカスタム属性を引いて、その差を金額で表示する](#attribute-monetary-difference)
- [ユーザーのフルネームがfirst_name フィールドに保存されている場合、そのユーザーの名を参照する。](#attribute-first-name)

### 一致するカスタム属性に基づいてメッセージをパーソナライズする {#attribute-matching}

このユースケースは、ユーザーが特定のカスタム属性を持っているかどうかをチェックし、もし持っていれば、異なるパーソナライズされたメッセージを表示する。 

{% raw %}
```liquid
{% if custom_attribute.${hasShovel} == true and custom_attribute.${VisitToGroundTooTough} > 0 %}
The ground is very hard. The dirt road goes East.
{% elsif custom_attribute.${hasShovel} == true %}
The dirt road goes East.
{% elsif custom_attribute.${VisitToStart} > 0 %}
The dirt road goes East.
The shovel here.
{% else %}
You are at a dead-end of a dirt road. The road goes to the east. In the distance, you can see that it will eventually fork off. The trees here are very tall royal palms, and they are spaced equidistant from each other.
There is a shovel here.
{% endif %}
```
{% endraw %}

### 2つのカスタム属性を引いて、その差を金額で表示する {#attribute-monetary-difference}

このユースケースは、2つの金銭的なカスタム属性をキャプチャし、その差額を計算して表示することで、ユーザーにゴールまでの道のりを知らせる。

{% raw %}
```liquid
{% assign event_goal = {{custom_attribute.${last_selected_event_personal_goal}}} %}
{% assign current_raised =  {{custom_attribute.${last_selected_event_personal_amount_raised}}} %}
{% assign difference =  event_goal | minus: current_raised %}
You only have ${{ difference | round: 0 | number_with_delimiter }} left to raise!
```
{% endraw %}

### ユーザーのフルネームがfirst_name フィールドに保存されている場合、そのユーザーの名を参照する。 {#attribute-first-name}

このユースケースでは、ユーザーの名を取得し (姓と名の両方が単一のフィールドに格納されている場合)、ユーザーの名を使用してウェルカムメッセージを表示します。

{% raw %}
```liquid
{{${first_name} | truncatewords: 1, "" | default: 'hi'}}
{% assign name = {{${first_name}}} | split: ' ' %}
Hi {{name[0]}}, here's your message!
```

**説明:**`split` フィルタは、`{{${first_name}}}` に保持されている文字列を配列に変換する。`{{name[0]}}` を使用することで、配列の最初の項目 (ユーザーの名) のみを参照します。 

{% endraw %}
{% endapi %}

{% api %}

## カスタムイベント

{% apitags %}
カスタムイベント
{% endapitags %}

- [カスタムイベントが現在から2時間以内の場合、プッシュ通知を中止する](#event-abort-push)
- [ユーザーがカスタムイベントを3回実行するたびにキャンペーンを送信する](#event-three-times)
- [1 つのカテゴリーからのみ購入したユーザーにメッセージを送信する](#event-purchased-one-category)
- [過去 1 か月間にカスタムイベントが発生した回数を追跡する](#track)


### カスタムイベントが現在から2時間以内の場合、プッシュ通知を中止する {#event-abort-push}

このユースケースは、イベントまでの時間を計算し、残り時間に応じて、パーソナライズされたさまざまなメッセージを表示する。

例えば、あるカスタムイベントプロパティが今後 2 時間以内に無効になるときに、あるプッシュ通知の送信を止める場合があります。この例では、電車の切符を買うためのカートが捨てられているというシナリオを使っている。

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign dep_time = {{event_properties.${outboundDate_Time}}} | date: "%s" %}
{% assign time_to_dep = dep_time | minus: today %}
{% if {{time_to_dep}} <= 7200 %}
{% abort_message("OutboundDate less than 2 hours") %}
{% elsif {{time_to_dep}} > 7200 and {{time_to_dep}} < 86400 %}
Don't forget to buy your ticket to {{event_properties.${toStation}}} within next 24 hours
{% else %}
Still traveling to {{event_properties.${toStation}}} in more than 24 hours? Book now
{% endif %}
```
{% endraw %}

### ユーザーがカスタムイベントを3回実行するたびにキャンペーンを送信する {#event-three-times}

このユースケースでは、あるユーザーがカスタムイベントを 3 回実行したかどうかをチェックし、実行した場合はメッセージを表示するか、キャンペーンを送信します。 

{% raw %}
```liquid
{% assign cadence = custom_attribute.${example} | minus: 1 | modulo: 3 %}
{% if custom_attribute.${example} == blank %}
{% abort_message("Error calculating cadence") %}
{% elsif cadence != 0 %}
{% abort_message("Skip message") %}
{% endif %}
Did you forget something in your shopping cart?
```
{% endraw %}

{% alert important %}カスタムイベント数のイベントプロパティを設定しているか、Braze エンドポイントに Webhook を使用する必要があります。これは、ユーザーがイベントを実行するたびに、カスタム属性 (`example_event_count`） をインクリメントするためです。この例では、3 ずつ増える一連の数 (1、4、7、10 など) を使用しています。この一連の数をゼロから始める (0、3、6、9 などにする） には、`minus: 1` を削除します。
{% endalert %}

### 1 つのカテゴリーからのみ購入したユーザーにメッセージを送信する{#event-purchased-one-category}

このユースケースは、ユーザーが購入したカテゴリーのリストを取得し、購入カテゴリーが1つしか存在しない場合は、メッセージを表示する。

{% raw %}
```liquid
{% assign category = {{custom_attribute.${categories_purchased}}} %}
{% assign uniq_cat = {{category | uniq }} %}
{% if {{uniq_cat | size}} == 1%}
{{uniq_cat}}
{% else %}
{% abort_message("Purchase category doesn't exist") %}
{% endif %}
```
{% endraw %}

### 過去 1 か月間にカスタムイベントが発生した回数を追跡する{#track}

このユースケースは、当月1日と前月の間にカスタムイベントが記録された回数を計算する。その後、users/track 呼び出しを実行して、この値をカスタム属性として更新し保存できます。なお、このキャンペーンは、月次データを使用する前に、2ヶ月連続で実施する必要がある。

{% raw %}
```liquid

{% capture body %}
{
 "braze_id": "{{${braze_id}}}",
 "fields_to_export": ["custom_events"]
}

{% endcapture %}

{% connected_content YOUR_BRAZE_ENDPOINT/users/export/ids
 :method post
  :headers { "Authorization": "Bearer YOUR_API_KEY" }
  :body {{body}}
 :content_type application/json
 :save response
  :retry %}

{% for custom_event in response.users[0].custom_events %}
{% assign ce_name = custom_event.name %}
{% comment %} The following custom event name will need to be amended for the target custom event. {% endcomment %}

{% if ce_name == "Project Exported" %}
{% comment %}{{custom_event.name}}: {{custom_event.count}}{% endcomment %}
{% assign current_count = custom_event.count %}
{% endif %}
{% endfor %}

{% assign prev_month_count = {{custom_attribute.${projects_exported_prev_month}}} %}
{% assign latest_count = current_count | minus: prev_month_count %}
{% assign now = "now" | date: "%s" %}
{% assign yesterday = {{now}} | minus: 86400 %}
{% assign previous_month = {{yesterday}} | date: "%B" %}
{% assign previous_year = {{yesterday}} | date: "%y" %}
{% assign formatted_month = previous_month | downcase %}
{% comment %}The Custom Event name that is being tracked will be needed to be amended for the target Custom Event in the Attribute Name below. {% endcomment %}
```

```json
"attributes": [
  {
    "external_id":"{{${user_id}}}",
       "projects_exported_{{formatted_month}}_{{previous_year}}": "{{latest_count}}"
  }
]
```

{% endraw %}

{% endapi %}

{% api %}

## 言語

{% apitags %}
言語
{% endapitags %}

- [月名を別の言語で表示する](#language-display-month)
- [ユーザーの言語に基づいて画像を表示する](#language-image-display)
- [曜日とユーザーの言語に基づいてメッセージをパーソナライズする](#language-personalize-message)

### 月名を異なる言語で表示する {#language-display-month}

このユースケースでは、現在の日、月、年を表示し、月には別の言語を使用します。この例ではスウェーデン語を使用している。

{% raw %}
```liquid
{% assign day = 'now' | date: "%e" %}
{% assign year =  'now' | date: "%Y" %}
{% assign month =  'now' | date: "%B" %}

{% if {{month}} == 'January' %}
{{day}} Januari {{year}}
{% elsif {{month)) == 'February' %}
{{day}} Februari {{year}}
{% elsif {{month)) == 'March' %}
{{day}} Mars {{year}}
{% elsif {{month)) == 'April' %}
{{day}} April {{year}}
{% elsif {{month)) == 'May' %}
{{day}} Maj {{year}}
{% elsif {{month)) == 'June' %}
{{day}} Juni {{year}}
{% elsif {{month)) == 'July' %}
{{day}} Juli {{year}}
{% elsif {{month)) == 'August' %}
{{day}} Augusti {{year}}
{% elsif {{month)) == 'September' %}
{{day}} September {{year}}
{% elsif {{month)) == 'October' %}
{{day}} Oktober {{year}}
{% elsif {{month)) == 'November' %}
{{day}} November {{year}}
{% elsif {{month)) == 'December' %}
{{day}} December {{year}}
{% endif %}
```
{% endraw %}

### ユーザーの言語に基づいて画像を表示する {#language-image-display}

このユースケースは、ユーザーの言語に基づいて画像を表示する。なお、このユースケースは、Brazeメディアライブラリにアップロードされた画像でのみテストされている。

{% raw %}
```liquid
{% if ${language} == 'en' %}
English image URL (for example, https://cdn-staging.braze.com/appboy/communication/assets/image_assets/images/60aecba96a93150c749b4d57/original.png?1622068137)
{% elsif ${language} == 'ru' %}
Russian image URL
{% elsif ${language} == 'es' %}
Spanish image URL
{% else %}
Fallback image URL
{% endif %}
```
{% endraw %}

### 曜日とユーザーの言語に基づいてメッセージをパーソナライズする {#language-personalize-message}

このユースケースは、現在の曜日をチェックし、その曜日に基づいて、ユーザーの言語が提供された言語オプションのひとつに設定されていれば、その言語で特定のメッセージを表示する。

この例は火曜日までですが、各曜日について繰り返すことができます。

{% raw %}
```liquid
{% assign today  = 'now' | date: '%A' %}

{% if today == 'Monday' %}
{% if ${language} == 'es' %}
Compra hoy y lleva tu aprendizaje de idiomas a niveles más altos. 🚀

{% elsif ${language} == 'en' %}
Purchase today and take your language learning to the next level. 🚀

{% elsif ${language} == 'zh' %}
今天就购买并将您的语言提高到一个新水平吧。🚀

{% else %}
It's Monday, but the language doesn't match 
{% endif %}

{% elsif today == 'Tuesday' %}

{% if ${language} == 'zh' %}
不要忘记解锁以获取完整版本哦。🔓

{% elsif ${language} == 'en' %}
Don't forget to unlock the full version of your language. 🔓

{% elsif ${language} == 'ja' %}
すべての機能を使ってみませんか 🔓

{% elsif ${language} == 'es' %}
No te olivides de desbloquear la versión completa del programa de idiomas. 🔓

{% else %}
tuesday default
{% endif %}
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## その他

{% apitags %}
その他
{% endapitags %}

- [マーケティングメールをブロックしている顧客にメールを送信しない](#misc-avoid-blocked-emails)
- [顧客のサブスクリプション状態を利用して、メッセージの内容をパーソナライズする](#misc-personalize-content)
- [文字列内のすべての単語の最初の文字を大文字にする](#misc-capitalize-words-string)
- [カスタム属性の値を配列と比較する](#misc-compare-array)
- [今後のイベントのリマインダーを作成する](#misc-event-reminder)
- [配列内の文字列を検索する](#misc-string-in-array)
- [配列の中で最大の値を見つける](#misc-largest-value)
- [配列の中で最小の値を見つける](#misc-smallest-value)
- [文字列の終わりを問い合わせる](#misc-query-end-of-string)
- [カスタム属性から配列内の値を複数の組み合わせで問い合わせる](#misc-query-array-values)
- [文字列を電話番号にフォーマットする](#phone-number)

### マーケティングメールをブロックしている顧客にメールを送信しない{#misc-avoid-blocked-emails}

このユースケースでは、コンテンツブロックに保存されたブロック済みユーザーのリストを取得し、それらのブロック済みユーザーが今後のキャンペーンやキャンバスでの通信やターゲット設定の対象外であることをチェックします。

{% alert important %}
このリキッドを使用するには、まずコンテンツブロック内にブロックされたメールのリストを保存する。このリストのメールアドレスの間に、追加のスペースや文字を挿入しないでください (例: `test@braze.com,abc@braze.com`)。
{% endalert %}

{% raw %}
```liquid
{% assign blocked_emails = {{content_blocks.${BlockedEmailList}}} | split: ',' %}
{% for email in blocked_emails %}
    {% if {{${email_address}}} == email %}
    {% abort_message("Email is blocked") %}
    {% break %}
    {% endif %}
{% endfor %} 
Your message here!
```
{% endraw %}

**説明:**ここでは、ブロックされたメールのコンテンツブロックを参照することで、潜在的な受信者のメールがこのリストにあるかどうかをチェックする。メールが見つかった場合、メッセージは送信されない。

{% alert note %}
コンテンツブロックのサイズ制限は 5 MB です。
{% endalert %}

### 顧客のサブスクリプション状態を利用して、メッセージの内容をパーソナライズする{#misc-personalize-content}

このユースケースでは、顧客のサブスクリプション状態を取得して、パーソナライズされた内容を送信します。特定のサブスクリプショングループに登録した顧客は、メールサブスクリプショングループ専用のメッセージを受け取ります。

{% raw %}
```liquid
{% if {{subscribed_state.${subscription_group_id}}} == 'subscribed' %}
This is an exclusive message for subscribed users!
{% else %} This is the default message for other users.
{% endif %}
```
{% endraw %}

### 文字列内のすべての単語の最初の文字を大文字にする {#misc-capitalize-words-string}

このユースケースは、単語の文字列を受け取り、配列に分割し、各単語の最初の文字を大文字にする。

{% raw %}
```liquid
{% assign words_array = {{custom_attribute.${address}}} | split: ' ' %}
{% for words in {{words_array}} %}
{{ words | capitalize | append: ' ' }}
{% endfor %} 
```
{% endraw %}

**説明:**ここでは、選んだ文字列属性に変数を代入し、`split` フィルタを使って文字列を配列に分割している。次に、`for` タグを使用して、新規作成した配列の各項目に変数 `words` を割り当て、`capitalize` フィルターと `append` フィルターを使用してそれぞれの語の間にスペースを追加してから表示します。

### カスタム属性の値を配列と比較する {#misc-compare-array}

このユースケースでは、お気に入りストアのリストを取得し、あるユーザーについてお気に入りストアがそのリストにあるかどうかをチェックします。ある場合は、それらのストアからの特別オファーを表示します。

{% raw %}
```liquid
{% assign favorite_stores = 'Target,Walmart,Costco' | split: ',' %}
{% for store in favorite_stores %}
{% if {{custom_attribute.${favorited_stores}}} contains {{store}} %}
Today's offer from {{store}}

{% break %}

{% else %}
{% abort_message("No attribute found") %}
{% endif %}
{% endfor %}
```
{% endraw %}

{% alert important %} このシーケンスの最初の条件付きステートメントには `break` タグがあります。これにより、マッチが見つかった時点でループが停止する。多くの、あるいはすべてのマッチを表示したい場合は、`break` タグを削除する。 {% endalert %}

### 次回イベントのリマインダーを作成する {#misc-event-reminder}

このユースケースは、ユーザーがカスタムイベントに基づいて今後のリマインダーを設定することを可能にする。このシナリオ例で、ユーザーは 26 日以上先のポリシー更新日に関するリマインダーを設定できます。リマインダーはポリシー更新日の 26 日前、13 日前、7 日前、2 日前に送信されます。

この使用例では、[ウェブフック・キャンペーン]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)またはキャンバス・ステップの本文に次のように記述する。

{% raw %}
```liquid
{% comment %}
Depending on how the reminder_capture property is passed to Braze, with/without a timestamp, the number of days could impact whether a user falls on either side of the 26/13/7/2-day windows.
Once users have been assigned to a Reminder journey/flow, they are then scheduled to enter a subsequent Canvas.
This 'Event Listener' can be used to split out users into different journeys based on the Custom Event properties sent to Braze.
{% endcomment %}

{% comment %}
When testing, make sure the campaign ID, campaign API endpoint, Canvas ID, Canvas API endpoint are entered correctly. In this example, the Canvas ID and Canvas API endpoint have been set up for sharing with the client. In practice, this can be testing using a campaign ID and Campaign API endpoint.
{% endcomment %}

{% comment %}
The following step calculates how much there is between today's date and the Reminder Date as 'time_to_reminder'.
{% endcomment %}

{% assign today = "now" | date: '%s' %}
{% assign reminder_start_date = {{event_properties.${reminder_date}}} | date: '%s' %}
{% assign time_to_reminder = reminder_start_date | minus: today %}

{% comment %}
The following step checks if the time_to_reminder is more than 26 days away; if this is true, then the user is scheduled to enter the subsequent Canvas 26 days before the reminder_date.
The time is converted from 'seconds from 1970' to the appropriate Reminder Date in the required ISO 8601 format.
N.B. Additional time zones would need to be catered for by adding an additional API Schedule property of "in_local_time"
{% endcomment %}

{% if {{time_to_reminder}} > 2246400 %}
{% assign time_to_first_message = reminder_start_date | plus: 2246400 %}
{{ time_to_first_message | date: '%Y-%m-%dT%H:%M' }}
{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than 26 days away but more than 13 days away.
Users are scheduled to enter the journey on day 13.
{% endcomment %}

{% elsif 1123200 > {{time_to_reminder}} and {{time_to_reminder}} < 2246399 %}
{% assign time_to_first_message = reminder_start_date | plus: 1123200 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than 13 days away but more than seven days away.
Users are scheduled to enter the journey on day 7.
{% endcomment %}

{% elsif 604800 > {{time_to_reminder}} and {{time_to_reminder}} < 1123199 %}
{% assign time_to_first_message = reminder_start_date | plus: 604800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than seven days away but more than two days away.
Users are scheduled to enter the journey on day 2.
{% endcomment %}

{% else {{time_to_reminder}} < 604799 and {{time_to_reminder}} > 172860 %}
{% assign time_to_first_message = reminder_start_date | plus: 172800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}
{% endif %}
```
{% endraw %}

{% alert important %} 

カスタムイベント`reminder_capture` が必要で、カスタムイベントプロパティには少なくとも以下のものが含まれていなければならない：

- `reminder-id`:カスタムイベントの識別子
- `reminder_date`:ユーザーが指定したリマインダーの期日
- `message_personalisation_X`:送信時にメッセージをパーソナライズするために必要なすべてのプロパティ

{% endalert %}

### 配列内の文字列を検索する {#misc-string-in-array}

このユースケースは、カスタム属性配列に特定の文字列が含まれているかどうかをチェックし、存在すれば特定のメッセージを表示する。

{% raw %}
```liquid
{% if custom_attribute.${PartnershipProgramsNotLinked} contains 'Hertz' %}
Link your Hertz account to use Hertz Fast Lane.
{% endif %}
```
{% endraw %}

### 配列の中で最大の値を見つける{#misc-largest-value}

このユースケースは、ユーザーメッセージングで使用するために、与えられたカスタム属性配列の中で最も高い値を計算する。

例えば、現在のハイスコアや、あるアイテムの最高入札額をユーザーに表示できます。

{% raw %}
```liquid
{% assign maxValue = 0 %}
{% for attribute in {{custom_attribute.${array_attribute}}} %}
{% assign compareValue = {{attribute | plus: 0}} %}
{% if compareValue > maxValue %}
{% assign maxValue = compareValue %}
{% endif %}
{% endfor %}
{{maxValue}}
```
{% endraw %}

{% alert important %}
使用するカスタム属性は、整数値を持ち、配列 (リスト) の一部を構成するものでなければなりません。{% endalert %}

### 配列の中で最小の値を見つける {#misc-smallest-value}

このユースケースは、ユーザーメッセージングで使用するために、与えられたカスタム属性配列の中で最も低い値を計算する。

例えば、ユーザーに最低得点や最安値を表示したい場合がある。

{% raw %}
```liquid
{% assign minValue = custom_attribute.${array_attribute}[0] | plus: 0 %}
{% for attribute in {{custom_attribute.${array_attribute}}} %}
{% assign compareValue = {{attribute | plus: 0}} %}
{% if compareValue < minValue %}
{% assign minValue = compareValue %}
{% endif %}
{% endfor %}
{{minValue}}
```
{% endraw %}

{% alert important %}使用するカスタム属性は、整数値を持ち、配列 (リスト) の一部を構成するものでなければなりません。{% endalert %}

### 文字列の末尾をクエリする{#misc-query-end-of-string}

このユースケースは、メッセージングで使用する文字列の末尾を問い合わせる。

{% raw %}
```liquid
{% assign interest = {{custom_attribute.${Buyer Interest}} | first } %}
{% assign marketplace = {{{{interest}} | split: "" | reverse | join: "" |  truncate: 4, ""}} %}
{% if {{marketplace}} == '3243' %}

Your last marketplace search was on {{custom_attribute.${Last marketplace buyer interest} | date: '%d.%m.%Y'}}. Check out all of our new offers.

{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

### カスタム属性から配列内の値を複数の組み合わせで問い合わせる {#misc-query-array-values}

このユースケースは、もうすぐ期限切れになる番組のリストを受け取り、ユーザーのお気に入りの番組がそのリストにあるかどうかをチェックし、もしあれば、ユーザーにもうすぐ期限切れになることを知らせるメッセージを表示する。

{% raw %} 
```liquid
{% assign expired_shows = 'Modern Family,The Rookie,Body of Proof,Felicity' | split: ',' %}
{% for show in expired_shows %}
{% if {{custom_attribute.${Favorite Shows}}} contains {{show}} %}
{% assign new_shows = new_shows | append: {{show}} | append: '*' %}
{% endif %}
{% endfor %}
{% assign new_shows_clean = new_shows | split: '*' %}
{% if new_shows_clean.size != 0 %}

All episodes of {{new_shows_clean | join: ', ' }} expire on 9/8 - watch them now before they're gone!

{% else %}
{% abort_message("Not found") %}
{% endif %}
```
{% endraw %}

{% alert important %} 最初に配列間のマッチを見つけ、最後にマッチを分割するロジックを構築する必要がある。 {% endalert %}

### 文字列を電話番号にフォーマットする {#phone-number}

この使用例では、`phone_number` ユーザープロファイルフィールド（デフォルトでは、整数の文字列としてフォーマットされている）にインデックスを付け、ローカルの電話番号標準に基づいて再フォーマットする方法を示す。例えば、1234567890 を (123)-456-7890 にします。.

{% raw %} 
```liquid
{% assign phone = {{${phone_number}}} | remove: "-" | split: '' %}

({{ phone[0] }}{{ phone[1] }}{{ phone[2] }})-{{ phone[3] }}{{ phone[4] }}{{ phone[5] }}-{{ phone[6] }}{{ phone[7] }}{{ phone[8] }}{{ phone[9] }}
```
{% endraw %}

{% endapi %}

{% api %}

## プラットフォーム・ターゲティング

{% apitags %}
プラットフォーム・ターゲティング
{% endapitags %}

- [デバイス OS別に異なる文章を使用する](#platform-device-os)
- [指定プラットフォームのみをターゲットにする](#platform-target)
- [特定のOSバージョンを持つiOSデバイスのみを対象とする](#platform-target-ios-version)
- [ウェブブラウザだけをターゲットにする](#platform-target-web)
- [特定のモバイル通信事業者をターゲットにする](#platform-target-carrier)

### デバイス OS別に異なる文章を使用する{#platform-device-os}

このユースケースは、ユーザーがどのプラットフォームを利用しているかをチェックし、プラットフォームに応じて特定のメッセージを表示する。

例えば、モバイルユーザーには短いバージョンのメッセージコピーを表示し、その他のユーザーには通常の長いバージョンのコピーを表示したい場合がある。また、モバイルユーザーに、関連性の高い (Web ユーザーには関係しない） 特定のメッセージングを表示することもできます。例えば、iOSのメッセージングではApple Payについて話すかもしれないが、AndroidのメッセージングではGoogle Payについて話すべきだ。

{% raw %}
```liquid
{% if targeted_device.${platform} == "ios" or targeted_device.${platform} == "android" %}
This is a shorter copy.

{% else %}
This is the regular copy and much longer than the short version. 
{% endif %}
```
{% endraw %}

{% alert note %}
Liquidは大文字と小文字を区別し、`targeted_device.${platform}` はすべて小文字で値を返す。
{% endalert %}

### 指定プラットフォームのみをターゲットにする{#platform-target}

このユースケースは、ユーザーのデバイス・プラットフォームをキャプチャし、プラットフォームに応じてメッセージを表示する。

例えば、Androidユーザーにだけメッセージを送りたい場合がある。これは、セグメンテーションツールでアプリを選択する方法の代替方法として使用できます。

{% raw %}
```liquid
{% if {{targeted_device.${platform}}} == 'android' %} 

This is a message for an Android user! 

{% else %}  
{% abort_message %} 
{% endif %}
```
{% endraw %}

### 特定のOSバージョンを持つデバイスのみを対象とする {#platform-target-ios-version}

このユースケースは、ユーザーのOSバージョンが特定のバージョン・セットに含まれるかどうかをチェックし、含まれる場合は特定のメッセージを表示する。

この例では、OS のバージョンが 10.0 またはそれ以前のユーザーに、そのユーザーのデバイス OS のサポートが段階的に終了するという警告を送信します。

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == "10.0" or {{targeted_device.${os}}} == "10.0.1" or {{targeted_device.${os}}} == "10.0.2" or {{targeted_device.${os}}} == "10.0.3" or {{targeted_device.${os}}} == "10.1" or {{targeted_device.${os}}} == "10.2" or {{targeted_device.${os}}} == "10.2.1" or {{targeted_device.${os}}} == "10.3" or {{targeted_device.${os}}} == "10.3.1" or {{targeted_device.${os}}} == "10.3.2" or {{targeted_device.${os}}} == "10.3.3" or {{targeted_device.${os}}} == "10.3.4" or {{targeted_device.${os}}} == "9.3.1" or {{targeted_device.${os}}} == "9.3.2" or {{targeted_device.${os}}} == "9.3.3" or {{targeted_device.${os}}} == "9.3.4" or {{targeted_device.${os}}} == "9.3.5" %}

We are phasing out support for your device's operating system. Be sure to update to the latest software for the best app experience.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### ウェブブラウザだけをターゲットにする {#platform-target-web}

このユースケースは、ユーザーのターゲット・デバイスがマックまたはウィンドウズで動作しているかどうかをチェックし、動作していれば特定のメッセージを表示する。

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == 'Mac' or {{targeted_device.${os}}} == 'Windows' %}

This message will display on your desktop web browser.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

次のユースケースでは、Web ユーザーが iOS か Android のいずれを使用しているかをチェックし、それに応じて特定のメッセージを表示します。

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == 'iOS' and {{targeted_device.${platform}}} == 'web' %}

Content for iOS.

{% elsif {{targeted_device.${os}}} == 'android' and {{targeted_device.${platform}}} == 'web' %}

Content for Android.

{% else %}
{% abort_message %} 
{% endif %}
```
{% endraw %}

### 特定のモバイル通信事業者をターゲットにする{#platform-target-carrier}

このユースケースは、ユーザーのデバイスのキャリアがVerizonかどうかをチェックし、もしそうであれば、特定のメッセージを表示する。

プッシュ通知やアプリ内メッセージのチャネルでは、Liquid を使用してメッセージ本文内でデバイスの通信事業者を指定できます。受信者のデバイスの通信事業者が一致しない場合、メッセージは送信されません。

{% raw %}
```liquid
{% if {targeted_device.${carrier}} contains "verizon" or {targeted_device.${carrier}} contains "Verizon" %}

This is a message for Verizon users!

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## タイムゾーン

{% apitags %}
タイムゾーン
{% endapitags %}

- [ユーザーのタイムゾーンに応じてメッセージをパーソナライズする。](#personalize-timezone)
- [CSTタイムゾーンをカスタム属性に追加する](#time-append-cst)
- [タイムスタンプを挿入する](#time-insert-timestamp)
- [ユーザーのローカルタイムゾーンの特定時間帯にのみキャンバスのプッシュ通知を送信する](#time-canvas-window)
- [ユーザーのローカルタイムゾーンの特定時間帯に定期のアプリ内メッセージのキャンペーンを送信する](#time-reocurring-iam-window)
- [ユーザーのローカルタイムゾーンの平日と週末で異なるメッセージを送信する](#time-weekdays-vs-weekends)
- [ユーザーのローカルタイムゾーンの時間帯に応じて異なるメッセージを送信する](#time-of-day)

### ユーザーのタイムゾーンに応じてメッセージをパーソナライズする。 {#personalize-timezone}

このユースケースは、ユーザーのタイムゾーンに応じて異なるメッセージを表示する。

{% raw %}
```liquid
{% if {{${time_zone}}} == 'xx' %}
Message for time zone xx.
{% elsif {{$time_zone}}} == 'yy' %}
Message for time zone yy.
{% else %}
{% abort_message("Invalid time zone") %}
{% endif %}
```
{% endraw %}

### CSTタイムゾーンをカスタム属性に追加する {#time-append-cst}

このユースケースは、指定されたタイムゾーンのカスタム日付属性を表示する。

オプション 1: 
{% raw %}
```liquid
{{custom_attribute.${application_expires_date} | time_zone: -0005 | date: '%B, %d %Y' }}
```
{% endraw %}

オプション 2: 
{% raw %}
```liquid
{{custom_attribute.${application_expires_date} | time_zone: 'America/Chicago' | date: '%B %d %Y %z' }}
```
{% endraw %}

### タイムスタンプを挿入する{#time-insert-timestamp}

このユースケースは、現在のタイムゾーンのタイムスタンプを含むメッセージを表示する。

次の例では、2021-05-03 10:41:04 のように、YYYY-mm-dd HH:MM:SS の形式で日付を表示します。

{% raw %}
```liquid
{{${user_id} | default: 'You'}} received a campaign, rendered at ({{ "now" | time_zone: ${time_zone} | date: "%Y-%m-%d %H:%M:%S" }})
```
{% endraw %}

### ユーザーのローカルタイムゾーンの特定時間帯にのみキャンバスのプッシュ通知を送信する{#time-canvas-window}

このユースケースは、ユーザーのローカルタイムゾーンの時刻をチェックし、それが設定された時間内であれば、特定のメッセージを表示する。

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}

Here's a message that will send between 8 am and 8 pm!
```
{% endraw %}

### ユーザーのローカルタイムゾーンの特定時間帯に定期のアプリ内メッセージのキャンペーンを送信する{#time-reoccurring-iam-window}

このユースケースは、ユーザーの現在時刻が設定されたウィンドウ内にある場合にメッセージを表示する。

例えば、次のシナリオでは、ある店舗が閉店したことをユーザーに知らせる。

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %} 
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 21 or hour < 10 %}

Store's closed. Come back between 11 am and 9 pm!

{% else %} 
{% abort_message("Not sent because the store is open") %}
{% endif %}
```
{% endraw %}

### ユーザーのローカルタイムゾーンの平日と週末で異なるメッセージを送信する{#time-weekdays-vs-weekends}

このユースケースは、ユーザーの現在の曜日が土曜日か日曜日かをチェックし、曜日によって異なるメッセージを表示する。

{% raw %}
```liquid
{% assign today = 'now' | time_zone: ${time_zone} | date: "%A" %}
{% if {{today}} == 'Saturday' or {{today}} == 'Sunday' %}
It's {{today}}, why don't you open the app for your transactions?

{% else %}
It's {{today}}, why don't you visit the store?
{% endif %}
```
{% endraw %}

### ユーザーのローカルタイムゾーンの時間帯に応じて異なるメッセージを送信する{#time-of-day}

このユースケースは、ユーザーの現在時刻が設定されたウィンドウの外に出た場合にメッセージを表示する。

例えば、時間帯に左右されるような、一刻を争うチャンスについてユーザーに伝えたい場合がある。

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}

Check out this new bar after work today. HH specials!
```
{% endraw %}

{% alert note %} これは[サイレント時間]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/time_based_campaign/#time-based-functionalities-for-campaigns)とは対照的なものです。{% endalert %}

{% endapi %}

{% api %}

## 週/日/月

{% apitags %}
週/日/月
{% endapitags %}

- [前月の名前をメッセージに入れる](#month-name)
- [毎月末にキャンペーンを送信する](#month-end)
- [月末（平日）にキャンペーンを送信する](#day-of-month-last)
- [ある月に毎日異なるメッセージを送信する](#day-of-month)
- [曜日ごとに異なるメッセージを送信する](#day-of-week)

### 前月の名前をメッセージに入れる {#month-name}

このユースケースは、メッセージングで使用するために、現在の月を取得し、前の月を表示する。

{% raw %}
```liquid
{% assign today = 'now' | date: "%m" %}
{% assign last_month = {{today}} | minus: 1 %}
{% if last_month == 1 %}
{% assign month = "January" %}
{% elsif last_month == 2 %}
{% assign month = "February" %}
{% elsif last_month == 3 %}
{% assign month = "March" %}
{% elsif last_month == 4 %}
{% assign month = "April" %}
{% elsif last_month == 5 %}
{% assign month = "May" %}
{% elsif last_month == 6 %}
{% assign month = "June" %}
{% elsif last_month == 7 %}
{% assign month = "July" %}
{% elsif last_month == 8 %}
{% assign month = "August" %}
{% elsif last_month == 9 %}
{% assign month = "September" %}
{% elsif last_month == 10 %}
{% assign month = "October" %}
{% elsif last_month == 11 %}
{% assign month = "November" %}
{% elsif last_month == 0 %}
{% assign month = "December" %}
{% endif %}

Here's an overview of what your spending looked like in {{month}}.
```
{% endraw %}

同じ結果を得るために、次のような方法もある。

{% raw %}
```liquid
{% assign last_month_name = 'now' | date: "%Y-%m-01" | date: '%s' | minus: 1 | date: "%B" %}

Here's an overview of what your spending looked like in {{month}}.
```
{% endraw %}

### 毎月末にキャンペーンを送る {#month-end}

このユースケースは、現在の日付が日付のリスト内にあるかどうかをチェックし、日付に応じて特定のメッセージを表示する。

{% alert note %}これはうるう年 (2 月 29 日) を考慮していません。 {% endalert %}

{% raw %}
```liquid
{% assign current_date = 'now' | date: '%b %d' %}

{% if current_date == "Jan 31" or current_date == "Feb 28" or current_date == "Mar 31" or current_date == "Apr 30" or current_date == "May 31" or current_date == "Jun 30" or current_date == "Jul 31" or current_date == "Aug 31" or current_date == "Sep 30" or current_date == "Oct 31" or current_date == "Nov 30" or current_date == "Dec 31" %}

The date is correct

{% else %}
{% abort_message("Date is not listed") %}
{% endif %}
```
{% endraw %}

### 月末（平日）にキャンペーンを送信する {#day-of-month-last}

このユースケースは、現在の月と日をキャプチャし、現在の日がその月の最後の平日に当たるかどうかを計算する。

例えば、毎月最終水曜日にユーザーにアンケートを送り、製品へのフィードバックを求めることができる。

{% raw %}
```liquid
{% comment %}Pull the day, day name, month, and year from today's date.{% endcomment %}
{% assign current_day = "now" | date: "%d" %}
{% assign current_day_name = "now" | date: "%a" %}
{% assign current_month = "now" | date: "%b" %}
{% assign current_year = "now" | date: "%Y" %}

{% comment %}Assign the correct number of days for the current month.{% endcomment %}

{% if current_month == "Jan" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Mar" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Apr" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "May" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Jun" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Jul" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Aug" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Sep" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Oct" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Nov" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Dec" %}
{% assign last_day_of_month = 31 %}
{% endif %}

{% comment %}Assign the correct number of days if the current month is February, taking into account leap years.{% endcomment %}

{% assign leap_year_remainder = {{current_year | modulo: 4 }} != "0" %}
{% if leap_year_remainder == 0 and current_month == "Feb" %}
{% assign last_day_of_month = 29 %}
{% elsif leap_year_remainder != "0" and current_month == "Feb" %}
{% assign last_day_of_month = 28 %}
{% endif %}

{% comment %}Check that today's date is within a week of the last day of the month. If not, abort the message. If so, check that today is Wednesday. If not, abort the message.{% endcomment %}

{% assign diff_in_days = last_day_of_month | minus: current_day | plus: 1%} 
{% if diff_in_days <= 7 %} 
{% unless current_day_name == "Wed" %} 
{% abort_message("Wrong day of the week") %} 
{% endunless %} 
{% else %} 
{% abort_message("Not the last week of the month") %} 
{% endif %}
```
{% endraw %}

### ある月に毎日異なるメッセージを送信する{#day-of-month}

このユースケースは、現在の日付がリストにある日付と一致するかどうかをチェックし、日によっては明確なメッセージを表示する。

{% raw %}
```liquid
{% assign today = 'now' | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_1 = "2019-12-01" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_2 = "2019-12-02" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_3 = "2019-12-03" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}

{% if today == day_1 %}
Message for 2019-12-01

{% elsif today == day_2 %}
Message for 2019-12-02

{% elsif today == day_3%}
Message for 2019-12-03

{% else %}
{% abort_message("Date not listed") %}
{% endif %}
```
{% endraw %}

### 曜日ごとに異なるメッセージを送信する{#day-of-week}

このユースケースは、現在の曜日をチェックし、曜日によって異なるメッセージを表示する。

{% raw %}
```liquid
{% assign today = 'now' | date: "%A" %}
{% case today %}
{% when 'Monday' %}
Monday copy

{% when 'Tuesday' %}
Tuesday copy

{% when 'Wednesday' %}
Wednesday copy

{% when  'Thursday' %}
Thursday copy

{% when  'Friday' %}
Friday copy

{% when 'Saturday' %}
Saturday copy

{% when 'Sunday' %}
Sunday copy

{% else %}
Default copy
{% endcase %}
```
{% endraw %}

{% alert note %}
"Default copy"の行を {% raw %}`{% abort_message() %}`{% endraw %} に置き換えることで、曜日が不明な場合にメッセージの送信を停止できます。
{% endalert %}

{% endapi %}
