Looking at the error and the file content, the issue is that the file is truncated mid-Liquid code block. The last section "カスタム属性から配列内の値を複数の組み合わせでクエリする" has an incomplete `{% raw %}` code block that's never closed. I need to complete the remaining content based on the English source pattern.

---
nav_title: Liquid ユースケースライブラリー
article_title: Liquid ユースケースライブラリ
page_order: 10
search_rank: 2
excerpt_separator: ""
page_type: glossary
layout: liquid_use_case_glossary
description: "このランディングページには、記念日、アプリの使用状況、カウントダウンなど、カテゴリー別に整理された Liquid のユースケースのサンプルが掲載されています。"

---

{% api %}

## 記念日と祝日

{% apitags %}
記念日と祝日
{% endapitags %}

- [ユーザーの記念年に基づいてメッセージをパーソナライズする](#anniversary-year)
- [ユーザーの誕生週に基づいてメッセージをパーソナライズする](#birthday-week)
- [ユーザーの誕生月にキャンペーンを送信する](#birthday-month)
- [大型連休にメッセージを送信しないようにする](#holiday-avoid)

### ユーザーの記念年に基づいてメッセージをパーソナライズする {#anniversary-year}

このユースケースでは、ユーザーの最初の登録日に基づいてアプリ記念日を計算し、何周年を祝うかによって異なるメッセージを表示する方法を説明します。

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

**説明:** ここでは予約変数 `now` を使用して、[ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) 形式で現在の日付と時刻をテンプレート化します。フィルター `%B`（「May」などの月）および `%d`（「18」などの日）は、現在の月と日をフォーマットします。次に、`signup_date` の値に同じ日付と時間のフィルターを使い、条件タグとロジックを使って2つの値を比較できるようにします。

そして、さらに3つの変数ステートメントを繰り返して、`signup_date` の `%B` と `%d` を取得し、`%Y`（「2021」などの年）も追加します。これにより、`signup_date` の日付と時刻が年だけになります。日と月が分かると、そのユーザーの記念日が今日かどうかを確認することができ、年が分かると、何年経ったかが分かります。したがって、何周年を祝うかを知ることができます。

{% alert tip %}登録日を収集した年数を上限に、その数の条件を作成できます。{% endalert %}  

### ユーザーの誕生週に基づいてメッセージをパーソナライズする {#birthday-week}

このユースケースは、ユーザーの誕生日を見つけ、現在の日付と比較し、誕生日の週の前、中、後に特別な誕生日メッセージを表示する方法を示しています。

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

**説明:** [記念年](#anniversary-year)のユースケースと同様に、ここでは予約変数 `now` と `%W` フィルター（1年52週のうち12週目など）を使用して、ユーザーの誕生日が含まれる年の週番号を取得します。ユーザーの誕生週が現在の週と一致すれば、お祝いのメッセージを送ります！ 

メッセージングをさらにパーソナライズするために、`last_week` および `next_week` のステートメントも含めています。

### ユーザーの誕生月にキャンペーンを送る {#birthday-month}

このユースケースは、ユーザーの誕生月を計算し、誕生月が当月かどうかをチェックし、当月であれば特別なメッセージを送信する方法を示しています。

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

**説明:** [誕生週](#birthday-week)のユースケースと似ていますが、ここでは `%B` フィルター（「May」などの月）を使用して、今月誕生日を迎えるユーザーを計算します。毎月のメールに誕生日のユーザーを登場させるといった応用が考えられます。

### 大型連休にメッセージを送信しないようにする {#holiday-avoid}

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

**説明:** ここでは、フィルター `%Y`（「2023」などの年）、`%m`（「12」などの月）、および `%d`（「25」などの日）を使用して、`today` という用語に予約変数 `now`（現在の日時）を代入し、日付をフォーマットします。次に条件付きステートメントを実行し、変数 `today` が選択した休日と一致した場合はメッセージを中止します。 

この例では、クリスマス・イブ、クリスマス・デー、ボクシング・デー（クリスマスの翌日）を使用しています。

{% endapi %}

{% api %}

## アプリの利用状況

{% apitags %}
アプリの利用状況
{% endapitags %}

- [ユーザーがセッションを記録していない場合、そのユーザーの言語でメッセージを送信する](#app-session-language)
- [ユーザーが最後にアプリを開いた日に基づいてメッセージをパーソナライズする](#app-last-opened)
- [ユーザーが最後にアプリを使用したのが3日以内の場合、別のメッセージを表示する](#app-last-opened-less-than)

### ユーザーがセッションを記録していない場合、そのユーザーの言語でメッセージを送信する {#app-session-language}

このユースケースは、ユーザーがセッションを記録したかどうかをチェックし、もし記録していなければ、カスタム属性を介して手動で収集した言語に基づいてメッセージを表示するロジックを含みます。アカウントに言語情報がない場合は、デフォルトの言語でメッセージが表示されます。もしユーザーがセッションを記録していれば、そのユーザーに結びついた言語情報を引き出し、適切なメッセージを表示します。 

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
**説明:** ここでは、2つのグループ化された `if` ステートメントを入れ子にして使っています。最初の `if` ステートメントは、`last_used_app_date` が `nil` かどうかをチェックすることによって、ユーザーがセッションを開始したかどうかを確認します。これは、ユーザーがセッションを記録するときに、`{{${language}}}` が SDK によって自動的に収集されるためです。ユーザーのセッションがログに記録されていない場合、ユーザーの言語はまだ不明です。そのため、言語関連のカスタム属性が保存されているかどうかをチェックして、可能であればその情報に基づいて、その言語でメッセージを表示します。
{% endraw %}

2番目の `if` ステートメントは、標準（デフォルト）の属性をチェックするだけです。ユーザーの `last_used_app_date` が `nil` ではなく（つまり、ユーザーがセッションを記録済み）、ユーザーの言語が分かっているためです。

{% alert note %}
[`Nil`](https://shopify.github.io/liquid/basics/types/#nil) は予約変数で、Liquid コードの結果がないときに返されます。`Nil` は、`if` ブロックの中では `false` として扱われます。
{% endalert %}

### ユーザーが最後にアプリを開いた日に基づいてメッセージをパーソナライズする {#app-last-opened}

このユースケースは、ユーザーが最後にアプリを開いた時間を計算し、時間の長さに応じて異なるパーソナライズされたメッセージを表示します。

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Happy to see you again!
{% else %}
It's been a while; here are some of our latest updates.
{% endif %}
```
{% endraw %}

### ユーザーが最後にアプリを使用したのが3日以内の場合、別のメッセージを表示する {#app-last-opened-less-than}

このユースケースでは、ユーザーがアプリを最後に使用してからの経過時間を計算し、その長さに応じてパーソナライズされた異なるメッセージを表示します。

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}}} | date: "%s" %}
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
- [設定した時点からカウントダウンを計算する](#countdown-difference-days)
- [特定の配送日と優先順位に関するカウントダウンを作成する](#countdown-shipping-options)
- [日単位でカウントダウンを作成する](#countdown-days)
- [日、時間、分のカウントダウンを作成する](#countdown-dynamic)
- [特定の日付までの残り日数を表示する](#countdown-future-date)
- [カスタム日付属性が到着するまでの残り日数を表示する](#countdown-custom-date-attribute)
- [残り時間を表示し、残り時間がX時間しかない場合はメッセージを中断する](#countdown-abort-window)
- [ユーザーのメンバーシップが終了するX日前に送信するアプリ内メッセージ](#countdown-membership-expiry)
- [ユーザーの日付と言語に基づいてアプリ内メッセージをパーソナライズする](#countdown-personalize-language)
- [今から30日後の日付を月と日の形式でテンプレート化する](#countdown-template-date)

### 今日の日付にx日を加える {#countdown-add-x-days}

このユースケースは、現在の日付に特定の日数を追加して参照し、メッセージに追加します。例えば、週の半ばに週末のイベントを紹介するメッセージを送りたい場合があります。

{% raw %}
```liquid
Here are the movies we're showing on {{ "now" | date:'%s' | plus:259200 | date:"%F" }}!
```
{% endraw %}

`plus` の値は常に秒単位であるため、最終的にフィルター `%F` を使用して秒数を日数に変換します。

{% alert important %}
メッセージにイベントのリストへのURLやディープリンクを含めると、ユーザーを将来のアクションのリストに誘導できます。
{% endalert %}

### 設定した時点からカウントダウンを計算する {#countdown-difference-days}

このユースケースは、特定の日付と現在の日付の日数の差を計算します。この差を利用して、ユーザーにカウントダウンを表示することができます。

{% raw %}
```liquid
{% assign event_date = '2023-12-31' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
you have {{ difference_days }} days left!
```
{% endraw %}

### 特定の配送日と優先順位に関するカウントダウンを作成する {#countdown-shipping-options}

このユースケースでは、さまざまな配送オプションを取得し、受け取りにかかる時間を計算し、特定の日付までに荷物を受け取れるよう、ユーザーに購入を促すメッセージを表示します。

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

このユースケースは、特定のイベントから現在の日付までの残り時間を計算し、イベントまであと何日かを表示します。

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
`date` の値を持つカスタム属性フィールドが必要です。
{% endalert %}

### 日、時間、分のカウントダウンを作成する {#countdown-dynamic}

このユースケースは、特定のイベントから現在の日付までの残り時間を計算します。イベントまでの残り時間に応じて、時間値（日、時間、分）が変更され、パーソナライズされたさまざまなメッセージが表示されます。

例えば、顧客の注文が届くまで2日かかる場合、「ご注文は2日後に届きます」と表示できます。一方、1日未満の場合は、「ご注文は17時間以内に届きます」と変更できます。

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
`date` の値を持つカスタム属性フィールドが必要です。また、日数、時間数、分数で表示する時間のしきい値を設定する必要もあります。
{% endalert %}

### 特定の日付までの残り日数を表示する {#countdown-future-date}

このユースケースは、現在の日付と将来のイベントの日付の差を計算し、イベントまであと何日かを示すメッセージを表示します。

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

このユースケースは、現在の日付と将来の日付の日数の差を計算し、その差が設定された数値と一致した場合にメッセージを表示します。

この例では、ユーザーはカスタム日付属性から2日以内にメッセージを受け取ります。そうでなければ、メッセージは送信されません。

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

### 残り時間を表示し、残り時間がx時間しかない場合はメッセージを中断する {#countdown-abort-window}

このユースケースは、ある日付までの時間を計算し、その長さに応じて（日付が近すぎる場合はメッセージをスキップする）、パーソナライズされたさまざまなメッセージを表示します。 

例えば、「ロンドン行きの航空券を買うのにあとx時間残っています」といったメッセージですが、ロンドン行きのフライト時間まで2時間以内であれば送信しません。

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

### ユーザーのメンバーシップが終了するx日前に送信するアプリ内メッセージ {#countdown-membership-expiry}

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

このユースケースは、イベントまでのカウントダウンを計算し、ユーザーの言語設定に基づいて、その言語でカウントダウンを表示します。

例えば、月に一度、4回のアプリ内メッセージでオファーの有効期限を知らせるアップセルメッセージをユーザーに送ることができます：

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
指定した日付が日付範囲外の場合は、`date` の値を代入し、中止ロジックを含める必要があります。正確な日数を計算するには、代入する最終日に23時59分59秒を含める必要があります。
{% endalert %}

### 今から30日後の日付を月と日の形式でテンプレート化する {#countdown-template-date}

このユースケースでは、今から30日後の日付をメッセージングに表示します。

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
- [フルネームがfirst_nameフィールドに保存されている場合、ユーザーの名を参照する](#attribute-first-name)

### 一致するカスタム属性に基づいてメッセージをパーソナライズする {#attribute-matching}

このユースケースは、ユーザーが特定のカスタム属性を持っているかどうかをチェックし、もし持っていれば、異なるパーソナライズされたメッセージを表示します。 

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

このユースケースは、2つの金銭的なカスタム属性をキャプチャし、その差額を計算して表示することで、ユーザーにゴールまでの道のりを知らせます。

{% raw %}
```liquid
{% assign event_goal = {{custom_attribute.${last_selected_event_personal_goal}}} %}
{% assign current_raised =  {{custom_attribute.${last_selected_event_personal_amount_raised}}} %}
{% assign difference =  event_goal | minus: current_raised %}
You only have ${{ difference | round: 0 | number_with_delimiter }} left to raise!
```
{% endraw %}

### フルネームがfirst_nameフィールドに保存されている場合、ユーザーの名を参照する {#attribute-first-name}

このユースケースでは、ユーザーの名を取得し（姓と名の両方が単一のフィールドに格納されている場合）、その名を使用してウェルカムメッセージを表示します。

{% raw %}
```liquid
{{${first_name} | truncatewords: 1, "" | default: 'hi'}}
{% assign name = {{${first_name}}} | split: ' ' %}
Hi {{name[0]}}, here's your message!
```

**説明:** `split` フィルタは、`{{${first_name}}}` に保持されている文字列を配列に変換します。`{{name[0]}}` を使用することで、配列の最初の項目（ユーザーの名）のみを参照します。 

{% endraw %}
{% endapi %}

{% api %}

## カスタムイベント

{% apitags %}
カスタムイベント
{% endapitags %}

- [カスタムイベントが現在から2時間以内の場合、プッシュ通知を中止する](#event-abort-push)
- [ユーザーがカスタムイベントを3回実行するたびにキャンペーンを送信する](#event-three-times)
- [1つのカテゴリーからのみ購入したユーザーにメッセージを送信する](#event-purchased-one-category)
- [過去1か月間にカスタムイベントが発生した回数を追跡する](#track)


### カスタムイベントが現在から2時間以内の場合、プッシュ通知を中止する {#event-abort-push}

このユースケースは、イベントまでの時間を計算し、残り時間に応じて、パーソナライズされたさまざまなメッセージを表示します。

例えば、あるカスタムイベントプロパティが今後2時間以内に期限切れになるときに、プッシュ通知の送信を止めたい場合があります。この例では、電車の切符の放棄カートのシナリオを使っています。

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

このユースケースでは、あるユーザーがカスタムイベントを3回実行したかどうかをチェックし、実行した場合はメッセージを表示するか、キャンペーンを送信します。 

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

{% alert important %} カスタムイベント数のイベントプロパティを設定しているか、Braze エンドポイントへの Webhook を使用する必要があります。これは、ユーザーがイベントを実行するたびに、カスタム属性（`example_event_count`）をインクリメントするためです。この例では、3ずつ増える一連の数（1、4、7、10など）を使用しています。この一連の数をゼロから始める（0、3、6、9などにする）には、`minus: 1` を削除します。
{% endalert %}

### 1つのカテゴリーからのみ購入したユーザーにメッセージを送信する {#event-purchased-one-category}

このユースケースは、ユーザーが購入したカテゴリーのリストを取得し、購入カテゴリーが1つしか存在しない場合は、メッセージを表示します。

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

### 過去1か月間にカスタムイベントが発生した回数を追跡する {#track}

このユースケースは、当月1日と前月の間にカスタムイベントが記録された回数を計算します。その後、users/track 呼び出しを実行して、この値をカスタム属性として更新し保存できます。なお、このキャンペーンは、月次データを使用する前に、2か月連続で実施する必要があります。

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

このユースケースでは、現在の日、月、年を表示し、月には別の言語を使用します。この例ではスウェーデン語を使用しています。

{% raw %}
```liquid
{% assign day = 'now' | date: "%e" %}
{% assign year =  'now' | date: "%Y" %}
{% assign month =  'now' | date: "%B" %}

{% if {{month}} == 'January' %}
{{day}} Januari {{year}}
{% elsif {{month}} == 'February' %}
{{day}} Februari {{year}}
{% elsif {{month}} == 'March' %}
{{day}} Mars {{year}}
{% elsif {{month}} == 'April' %}
{{day}} April {{year}}
{% elsif {{month}} == 'May' %}
{{day}} Maj {{year}}
{% elsif {{month}} == 'June' %}
{{day}} Juni {{year}}
{% elsif {{month}} == 'July' %}
{{day}} Juli {{year}}
{% elsif {{month}} == 'August' %}
{{day}} Augusti {{year}}
{% elsif {{month}} == 'September' %}
{{day}} September {{year}}
{% elsif {{month}} == 'October' %}
{{day}} Oktober {{year}}
{% elsif {{month}} == 'November' %}
{{day}} November {{year}}
{% elsif {{month}} == 'December' %}
{{day}} December {{year}}
{% endif %}
```
{% endraw %}

### ユーザーの言語に基づいて画像を表示する {#language-image-display}

このユースケースは、ユーザーの言語に基づいて画像を表示します。なお、このユースケースは、Braze メディアライブラリにアップロードされた画像でのみテストされています。

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

このユースケースは、現在の曜日をチェックし、その曜日に基づいて、ユーザーの言語が提供された言語オプションのひとつに設定されていれば、その言語で特定のメッセージを表示します。

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
- [文字列の末尾をクエリする](#misc-query-end-of-string)
- [カスタム属性から配列内の値を複数の組み合わせでクエリする](#misc-query-array-values)
- [文字列を電話番号にフォーマットする](#phone-number)

### マーケティングメールをブロックしている顧客にメールを送信しない {#misc-avoid-blocked-emails}

このユースケースでは、コンテンツブロックに保存されたブロック済みユーザーのリストを取得し、それらのブロック済みユーザーが今後のキャンペーンやキャンバスでの通信やターゲット設定の対象外であることを確認します。

{% alert important %}
この Liquid を使用するには、まずコンテンツブロック内にブロックされたメールのリストを保存してください。このリストのメールアドレスの間に、追加のスペースや文字を挿入しないでください（例：`test@braze.com,abc@braze.com`）。
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

**説明:** ここでは、ブロックされたメールのコンテンツブロックを参照することで、潜在的な受信者のメールがこのリストにあるかどうかをチェックします。メールが見つかった場合、メッセージは送信されません。

{% alert note %}
コンテンツブロックのサイズ制限は5 MBです。
{% endalert %}

### 顧客のサブスクリプション状態を利用して、メッセージの内容をパーソナライズする {#misc-personalize-content}

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

このユースケースは、単語の文字列を受け取り、配列に分割し、各単語の最初の文字を大文字にします。

{% raw %}
```liquid
{% assign words_array = {{custom_attribute.${address}}} | split: ' ' %}
{% for words in {{words_array}} %}
{{ words | capitalize | append: ' ' }}
{% endfor %} 
```
{% endraw %}

**説明:** ここでは、選んだ文字列属性に変数を代入し、`split` フィルタを使って文字列を配列に分割しています。次に、`for` タグを使用して、新規作成した配列の各項目に変数 `words` を割り当て、`capitalize` フィルターと `append` フィルターを使用してそれぞれの語の間にスペースを追加してから表示します。

### カスタム属性の値を配列と比較する {#misc-compare-array}

このユースケースでは、お気に入りストアのリストを取得し、あるユーザーのお気に入りストアがそのリストにあるかどうかをチェックします。ある場合は、それらのストアからの特別オファーを表示します。

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

{% alert important %} このシーケンスの最初の条件付きステートメントには `break` タグがあります。これにより、マッチが見つかった時点でループが停止します。多くの、あるいはすべてのマッチを表示したい場合は、`break` タグを削除してください。{% endalert %}

### 次回イベントのリマインダーを作成する {#misc-event-reminder}

このユースケースは、ユーザーがカスタムイベントに基づいて今後のリマインダーを設定することを可能にします。このシナリオ例で、ユーザーは26日以上先のポリシー更新日に関するリマインダーを設定できます。リマインダーはポリシー更新日の26日前、13日前、7日前、2日前に送信されます。

このユースケースでは、[Webhook キャンペーン]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)またはキャンバスステップの本文に次のように記述します。

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

{% elsif {{time_to_reminder}} < 604799 and {{time_to_reminder}} > 172860 %}
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

カスタムイベント `reminder_capture` が必要で、カスタムイベントプロパティには少なくとも以下のものが含まれていなければなりません：

- `reminder-id`：カスタムイベントの識別子
- `reminder_date`：ユーザーが指定したリマインダーの期日
- `message_personalisation_X`：送信時にメッセージをパーソナライズするために必要なすべてのプロパティ

{% endalert %}

### 配列内の文字列を検索する {#misc-string-in-array}

このユースケースは、カスタム属性配列に特定の文字列が含まれているかどうかをチェックし、存在すれば特定のメッセージを表示します。

{% raw %}
```liquid
{% if custom_attribute.${PartnershipProgramsNotLinked} contains 'Hertz' %}
Link your Hertz account to use Hertz Fast Lane.
{% endif %}
```
{% endraw %}

### 配列の中で最大の値を見つける {#misc-largest-value}

このユースケースは、ユーザーメッセージングで使用するために、与えられたカスタム属性配列の中で最も高い値を計算します。

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
使用するカスタム属性は、整数値を持ち、配列（リスト）の一部を構成するものでなければなりません。{% endalert %}

### 配列の中で最小の値を見つける {#misc-smallest-value}

このユースケースは、ユーザーメッセージングで使用するために、与えられたカスタム属性配列の中で最も低い値を計算します。

例えば、ユーザーに最低得点や最安値を表示したい場合があります。

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

{% alert important %} 使用するカスタム属性は、整数値を持ち、配列（リスト）の一部を構成するものでなければなりません。{% endalert %}

### 文字列の末尾をクエリする {#misc-query-end-of-string}

このユースケースは、メッセージングで使用する文字列の末尾をクエリします。

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

### カスタム属性から配列内の値を複数の組み合わせでクエリする {#misc-query-array-values}

このユースケースは、もうすぐ期限切れになる番組のリストを受け取り、ユーザーのお気に入りの番組がそのリストにあるかどうかをチェックし、もしあれば、ユーザーに