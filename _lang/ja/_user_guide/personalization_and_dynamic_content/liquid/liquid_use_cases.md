---
nav_title: Liquid ユースケースライブラリ
article_title: Liquid ユースケースライブラリ
page_order: 10
search_rank: 2
excerpt_separator: ""
page_type: glossary
layout: liquid_use_case_glossary
description: "このランディングページには、記念日、アプリの使用状況、カウントダウンなど、カテゴリ別に整理されたLiquidのユースケースのサンプルが掲載されています。"

---

{% api %}

## 記念日・祝日

{% apitags %}
記念日・祝日
{% endapitags %}

- [ユーザーの記念日に基づいてメッセージをパーソナライズする](#anniversary-year)
- [ユーザーの誕生日に基づいてメッセージをパーソナライズする](#birthday-week)
- [ユーザーの誕生月にキャンペーンを送信する](#birthday-month)
- [主要な休日にメッセージを送信しないようにする](#holiday-avoid)

### ユーザーの記念日に基づいてメッセージをパーソナライズする {#anniversary-year}

このユースケースでは、最初のサインアップ日に基づいてユーザーのアプリの記念日を計算し、何年を祝うかに基づいてさまざまなメッセージを表示する方法を示します。

{% raw %}
\`\`\`liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign this_day = 'now' | date: "%d" %}
{% assign anniversary\_month = custom\_attribute.${registration\_date}}} | date: "%B" %}
{% assign anniversary\_day = custom\_attribute.${registration\_date}}} | date: "%d" %}
{% assign anniversary\_year = custom\_attribute.${registration\_date}}} | date: "%Y" %}

{% if this_month == anniversary_month %}
{% if this_day == anniversary_day %}
{% if anniversary_year == '2021' %}
ちょうど1年前の今日、初めてお会いしました!

{% elsif anniversary_year == '2020' %}
ちょうど2年前の今日、初めてお会いしました!

{% elsif anniversary_year == '2019' %}
ちょうど3年前の今日、私たちは初めて会いました!

{% else %}
{% abort_message("Not same year") %}
{% endif %}

{% else %}
{% abort_message("Not same day") %}
{% endif %}

{% else %}
{% abort_message("Not same month") %}
{% endif %}
\`\`\`
{% endraw %}

**Explanation:**ここでは、予約変数 `now` を使用して、現在の日付と時刻を [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601 "ISO 8601 Time Code Wiki") 形式でテンプレート化します。フィルター `%B` ("May" のような月) と ("18" のような日) は `%d` 、現在の月と日をフォーマットします。次に、値に対して `signup_date` 同じ日付と時刻のフィルターを使用して、コンディショナルタグとロジックを使用して 2 つの値を比較できるようにします。

次に、さらに 3 つの変数ステートメントを繰り返して、 の and `%d` `signup_date`を取得します`%B`が、(year like "2021") も追加`%Y`します。これにより、の `signup_date` 日付と時刻が年だけになります。曜日と月がわかれば、ユーザーの記念日が今日かどうかを確認でき、年がわかれば、何年経ったかがわかるので、何年おめでとうかがわかります。

{% alert tip %} 条件は、サインアップ日を収集している年数だけ作成できます。 {% endalert %}  

### ユーザーの誕生日に基づいてメッセージをパーソナライズする {#birthday-week}

このユースケースでは、ユーザーの誕生日を検索し、現在の日付と比較し、誕生日の週の前、最中、後に特別な誕生日メッセージを表示する方法を示します。

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

**Explanation:**[アニバーサリーイヤー](#anniversary-year)のユースケースと同様に、ここでは予約変数`now`を取得し、フィルター(1年で52週中12週目など)を使用して`%W`、ユーザーの誕生日が属する年の週数を取得します。ユーザーの誕生日の週が現在の週と一致する場合は、お祝いのメッセージを送信します。 

また、メッセージをさらにパーソナライズするためのステートメント`last_week``next_week`も含まれています。

### ユーザーの誕生月にキャンペーンを送信する {#birthday-month}

このユースケースでは、ユーザーの誕生日月を計算し、誕生日が当月にあるかどうかを確認し、該当する場合は特別なメッセージを送信する方法を示します。

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

**Explanation:**[誕生日の週](#birthday-week)のユースケースと似ていますが、ここではフィルター(「5月」などの月)を使用して`%B`、今月誕生日を迎えるユーザーを計算します。たとえば、誕生日のユーザーに毎月のメールで宛てることが考えられます。

### 主要な休日にメッセージを送信しないようにする {#holiday-avoid}

このユースケースでは、エンゲージメントが低い可能性が高い主要な休日を避けながら、休暇期間中にメッセージを送信する方法を示します。

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

**Explanation:**ここでは、フィルター `%Y` ("2023" のような年)、("12" のような月)、`%d` `%m` および ("25" のような日) を使用して、予約変数 `now` (現在の日付と時刻) に用語`today`を割り当てて日付を書式設定します。次に、条件ステートメントを実行して、変数 `today` が選択した休日の曜日と一致する場合、メッセージは中止されます。 

この例では、クリスマス イブ、クリスマス デー、ボクシング デー (クリスマスの翌日) を使用しています。

{% endapi %}

{% api %}

## アプリの利用状況

{% apitags %}
アプリの利用状況
{% endapitags %}

- [ユーザーがセッションを記録した場合にユーザーの言語でメッセージを送信する](#app-session-language)
- [ユーザーが最後にアプリを開いた日時に基づいてメッセージをパーソナライズする](#app-last-opened)
- [ユーザーが最後にアプリを使用してから 3 日以内の場合は、別のメッセージを表示する](#app-last-opened-less-than)

### ユーザーがセッションを記録していない場合にユーザーの言語でメッセージを送信する {#app-session-language}

このユースケースでは、ユーザーがセッションを記録しているかどうかをチェックし、そうでない場合は、カスタム属性(存在する場合)を介して手動で収集された言語に基づいてメッセージを表示するロジックを含めます。アカウントに言語情報が関連付けられていない場合は、デフォルトの言語でメッセージが表示されます。ユーザーがセッションをログに記録すると、ユーザーに関連付けられている言語情報が取得され、適切なメッセージが表示されます。 

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
**Explanation:**ここでは、入れ子になった 2 つのグループ化された `if` ステートメントを使用しています。最初の`if`ステートメントは、ユーザーが`last_used_app_date``nil`セッションを開始したかどうかをチェックするために、 が .これは、ユーザーがセッションをログに記録したときに SDK によって自動収集されるため `{{${language}}}` です。ユーザーがセッションを記録していない場合、そのユーザーの言語はまだ取得されていないため、言語関連のカスタム属性が保存されているかどうかがチェックされ、その情報に基づいて、可能であればその言語でメッセージが表示されます。
{% endraw %}

2 番目の`if`ステートメントは、ユーザーが の を持っていない`nil``last_used_app_date`ため、標準 (デフォルト) 属性をチェックするだけです。これは、ユーザーがセッションをログに記録し、その言語があることを意味します。

{% alert note %}
[`Nil`](https://shopify.github.io/liquid/basics/types/#nil) は、Liquidコードに結果がない場合に返される予約変数です。 `Nil` はブロック内と同様に `false` 扱われます `if` 。
{% endalert %}

### ユーザーが最後にアプリを開いた日時に基づいてメッセージをパーソナライズする {#app-last-opened}

このユースケースでは、ユーザーが最後にアプリを開いた時刻が計算され、時間の長さに応じて異なるパーソナライズされたメッセージが表示されます。

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

### ユーザーが最後にアプリを使用してから 3 日以内の場合は、別のメッセージを表示する {#app-last-opened-less-than}

このユースケースでは、ユーザーがアプリを使用した時間が計算され、時間の長さに応じて、異なるパーソナライズされたメッセージが表示されます。

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

## カウント ダウン

{% apitags %}
カウント ダウン
{% endapitags %}

- [今日の日付に X 日を加算します](#countdown-add-x-days)
- [設定した時点からのカウントダウンを計算する](#countdown-difference-days)
- [特定の出荷日と優先順位のカウントダウンを作成する](#countdown-shipping-options)
- [カウントダウンを日数で作成する](#countdown-days)
- [数日から数時間、数分のカウントダウンを作成](#countdown-dynamic)
- [特定の日付までの残り日数を表示する](#countdown-future-date)
- [カスタム日付属性が到着するまでの残り日数を表示する](#countdown-custom-date-attribute)
- [残り時間を表示し、残り時間が X 時間しかない場合はメッセージを中止します](#countdown-abort-window)
- [ユーザーのメンバーシップが終了する X 日前に送信するアプリ内メッセージ](#countdown-membership-expiry)
- [ユーザーの日付と言語に基づいてアプリ内メッセージをパーソナライズする](#countdown-personalize-language)
- [今から 30 日後の日付のテンプレート (月と日として書式設定)](#countdown-template-date)

### 今日の日付に x 日を加算します {#countdown-add-x-days}

このユースケースでは、現在の日付に特定の日数を追加して、メッセージを参照および追加します。たとえば、週末のエリア内のイベントを示す週の半ばのメッセージを送信できます。

{% raw %}
```liquid
Here are the movies we're showing on {{ "now" | date:'%s' | plus:259200 | date:"%F" }}!
```
{% endraw %}

`plus`値は常に秒単位であるため、秒を日に変換するフィルター`%F`で終了します。

{% alert important %}
メッセージにイベントのリストへの URL またはディープリンクを含めると、今後発生するアクションのリストにユーザーを誘導できます。
{% endalert %}

### 設定した時点からのカウントダウンを計算する {#countdown-difference-days}

このユースケースでは、特定の日付と現在の日付の日差を計算します。この違いを使用して、ユーザーにカウントダウンを表示できます。

{% raw %}
```liquid
{% assign event_date = '2023-12-31' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
you have {{ difference_days }} days left!
```
{% endraw %}

### 特定の出荷日と優先順位のカウントダウンを作成する {#countdown-shipping-options}

このユースケースでは、さまざまな配送オプションをキャプチャし、受信にかかる時間を計算し、特定の日付までにパッケージを受け取るのに間に合うように購入するようユーザーに促すメッセージを表示します。

{% raw %}
\`\`\`liquid
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
これは標準配送で注文する最終日なので、注文はクリスマスイブに間に合います!
{% elsif difference_s_days == 1 %}
通常配送で注文できる日が{{difference\_s\_days}}日残っているので、クリスマスイブに間に合うように注文が届きます!

{% else %}
通常配送で注文できる期間は{{difference\_s\_days}}日残っているので、クリスマスイブに間に合うようにご注文ください!
{% endif %}
{% elsif today > standard_shipping_end and today < express_shipping_end %}
{% if difference_e_days == 1 %}
速達便で注文できる{{difference\_e\_days}}日が残っているので、クリスマスイブに間に合うように注文してください!
{% else %}
速達便で注文できる期間は{{difference\_e\_days}}日残っているので、クリスマスイブに間に合うように注文してください!
{% endif %}
{% elsif today >= express_shipping_end and today < overnight_shipping_end %}
これは翌日発送の最終日なので、ご注文はクリスマスイブに間に合います!
{% else %}
{% abort_message("Unable to order and ship in time") %}
{% endif %}
\`\`\`
{% endraw %}

### カウントダウンを日数で作成する {#countdown-days}

このユースケースでは、特定のイベントと現在の日付の間の残り時間を計算し、イベントまでの残り日数を表示します。

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
値を持つ `date` カスタム属性フィールドが必要になります。
{% endalert %}

### 数日から数時間、数分のカウントダウンを作成 {#countdown-dynamic}

このユースケースでは、特定のイベントから現在の日付までの残り時間を計算します。イベントまでの残り時間に応じて、時間値(日、時間、分)を変更して、さまざまなパーソナライズされたメッセージを表示します。

たとえば、顧客の注文が届くまで 2 日ある場合、「注文は 2 日後に届きます」と言うことができます。 一方、1日未満の場合は、「注文は17時間以内に到着します」に変更できます。

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
値を持つ `date` カスタム属性フィールドが必要になります。また、時刻を表示する時間しきい値を日、時間、分で設定する必要があります。
{% endalert %}

### 特定の日付までの残り日数を表示する {#countdown-future-date}

このユースケースでは、現在の日付と将来のイベント日付の差を計算し、イベントまでの日数を示すメッセージを表示します。

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

このユースケースでは、現在の日付と将来の日付の日数の差を計算し、その差が設定された数値と一致する場合にメッセージを表示します。

この例では、ユーザーはカスタム日付属性から 2 日以内にメッセージを受信します。それ以外の場合、メッセージは送信されません。

{% raw %}
\`\`\`liquid
{% assign today = 'now' | date: '%j' | plus: 0 %}
{% assign surgery\_date = {{custom\_attribute.${surgery\_date}}} | date: '%j' | plus:0 %}

{% assign difference\_days = {{surgery\_date}} | minus: {{today}} %}
{% if difference_days == 2 %}
手術は2日後です{{custom\_attribute.${surgery\_date}}}
{% else %}
{% abort_message %}
{% endif %}
\`\`\`
{% endraw %}

### 残り時間を表示し、残り時間が x 時間しかない場合はメッセージを中止します {#countdown-abort-window}

このユースケースでは、特定の日付までの期間を計算し、長さに応じて(日付が早すぎる場合はメッセージをスキップします)、さまざまなパーソナライズされたメッセージを表示します。 

たとえば、「ロンドン行きの航空券の購入まであと x 時間あります」と表示されますが、ロンドンのフライト時刻まで 2 時間以内の場合は送信しないでください。

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

{% alert important %} カスタムイベントプロパティが必要になります。 {% endalert %}

### ユーザーのメンバーシップが終了する x 日前に送信するアプリ内メッセージ {#countdown-membership-expiry}

このユースケースでは、メンバーシップの有効期限をキャプチャし、有効期限までの期間を計算し、メンバーシップの有効期限が切れるまでの期間に基づいてさまざまなメッセージを表示します。

{% raw %}
\`\`\`liquid
{% assign membership\_expiry = {{custom\_attribute.${membership\_expiry\_date}}} | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = membership_expiry | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}

{% if difference_days > 4 and difference_days <= 7 %}
試用期間が{{difference\_days}}日残っていますので、必ずアップグレードしてください!

{% elsif difference_days > 2 and difference_days <= 4 %}
急ぐ！試用期間が{{difference\_days}}日残っていますので、必ずアップグレードしてください!

{% elsif difference_days == 2 %}
ラストチャンス!試用期間は{{difference\_days}}日残っています。必ずアップグレードしてください!

{% else %}
試用期間は残りわずかです。必ずアップグレードしてください!
{% endif %}
\`\`\`
{% endraw %}

### ユーザーの日付と言語に基づいてアプリ内メッセージをパーソナライズ {#countdown-personalize-language}

このユースケースでは、イベントまでのカウントダウンを計算し、ユーザーの言語設定に基づいて、その言語でカウントダウンを表示します。

たとえば、月に一度、ユーザーに一連のアップセルメッセージを送信して、オファーの有効期間を 4 つのアプリ内メッセージで知らせることができます。

- イニシャル
- 残り 2 日
- 残り 1 日
- 最終日

{% raw %}
\`\`\`liquid
{% assign today = 'now' | date: "%s" %}
{% assign end_date = "2021-04-16T23:59:59" | date: "%s" %}
{% assign difference = end_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
{% if {{difference\_days}} >= 3 %}
{% if ${language} == 'de' %}

Hallo, das Angebot gilt bis zum 16.04.

{% elsif ${language} == 'ch' %}
Grüezi, das Angebot gilt bis zum 16.04.

{% elsif ${language} == 'en' %}
オファーは4月16日まで有効です。

{% else %}
オファーは4月16日まで有効です。

{% endif %}
{% elsif {{difference\_days}} == 2 %}
{% if ${language} == 'de' %}
メッセージの挿入

{% elsif ${language} == 'ch' %}
メッセージの挿入

{% elsif ${language} == 'en' %}
メッセージの挿入

{% else %}
メッセージの挿入
{% endif %}

{% elsif {{difference\_days}} == 1 %}
{% if ${language} == 'de' %}
メッセージの挿入

{% elsif ${language} == 'ch' %}
メッセージの挿入

{% elsif ${language} == 'en' %}
メッセージの挿入

{% else %}
メッセージの挿入
{% endif %}

{% elsif {{difference\_days}} == 0 %}
{% if ${language} == 'de' %}
Hallo, das Angebot gilt noch heute.

{% elsif ${language} == 'ch' %}
Hallo, das Angebot gilt noch heute.

{% elsif ${language} == 'en' %}
Grüezi, das Angebot gilt noch heute.

{% else %}
こんにちは、オファーは今日のみ有効です。
{% endif %}

{% else %}
{% abort_message("Calculation failed") %}
{% endif %}
\`\`\`
{% endraw %}

{% alert important %}
値を割り当て `date` 、指定された日付が日付範囲外にある場合は中止ロジックを含める必要があります。正確な日の計算の場合、割り当てられた終了日には 23:59:59 が含まれている必要があります。
{% endalert %}

### 今から 30 日後の日付のテンプレート (月と日として書式設定) {#countdown-template-date}

このユースケースでは、メッセージングで使用する日付を今から30日後に表示します。

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
- [2 つのカスタム属性を減算して、その差を金額として表示する](#attribute-monetary-difference)
- [ユーザーのフルネームが [first\_name] フィールドに格納されている場合は、ユーザーの名を参照します](#attribute-first-name)

### 一致するカスタム属性に基づいてメッセージをパーソナライズする {#attribute-matching}

このユースケースでは、ユーザーが特定のカスタム属性を持っているかどうかをチェックし、持っている場合は、さまざまなパーソナライズされたメッセージを表示します。 

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

### 2 つのカスタム属性を減算して、その差を金額として表示する {#attribute-monetary-difference}

このユースケースでは、2つの金銭的カスタム属性をキャプチャし、その差を計算して表示し、目標達成までの距離をユーザーに知らせます。

{% raw %}
```liquid
{% assign event_goal = {{custom_attribute.${last_selected_event_personal_goal}}} %}
{% assign current_raised =  {{custom_attribute.${last_selected_event_personal_amount_raised}}} %}
{% assign difference =  event_goal | minus: current_raised %}
You only have ${{ difference | round: 0 | number_with_delimiter }} left to raise!
{% endif %}
```
{% endraw %}

### ユーザーのフルネームが [first\_name] フィールドに格納されている場合は、ユーザーの名を参照します {#attribute-first-name}

このユースケースでは、ユーザーの名を取得し (姓と名の両方が 1 つのフィールドに格納されている場合)、この名を使用してウェルカム メッセージを表示します。

{% raw %}
```liquid
{{${first_name} | truncatewords: 1, "" | default: 'hi'}}
{% assign name = {{${first_name}}} | split: ' ' %}
Hi {{name[0]}}, here's your message!
```

**Explanation:**フィルターは `split` 、保持されている `{{${first_name}}}` 文字列を配列に変換します。`{{name[0]}}`を使用すると、配列の最初の項目 (ユーザーの名) のみを参照します。 

{% endraw %}
{% endapi %}

{% api %}

## カスタムイベント

{% apitags %}
カスタムイベント
{% endapitags %}

- [Abort push notification if a custom event is within two hours of now (カスタムイベントが 2 時間以内の場合にプッシュ通知を中止する)](#event-abort-push)
- [ユーザーがカスタムイベントを 3 回実行するたびにキャンペーンを送信する](#event-three-times)
- [1 つのカテゴリからのみ購入したユーザーにメッセージを送信する](#event-purchased-one-category)
- [過去 1 か月間にカスタム イベントが発生した回数を追跡する](#track)


### Abort push notification if a custom event is within two hours of now (カスタムイベントが 2 時間以内の場合にプッシュ通知を中止する) {#event-abort-push}

このユースケースでは、イベントまでの時間を計算し、残り時間に応じて、さまざまなパーソナライズされたメッセージを表示します。

たとえば、カスタム イベント プロパティが今後 2 時間以内に渡される場合にプッシュが送信されないようにすることができます。この例では、列車の切符の放棄されたカートのシナリオを使用します。

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

### ユーザーがカスタムイベントを 3 回実行するたびにキャンペーンを送信する {#event-three-times}

このユースケースでは、ユーザーがカスタムイベントを3回実行したかどうかを確認し、実行した場合はメッセージを表示するか、キャンペーンを送信します。 

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

{% alert important %} カスタムイベント数のイベントプロパティを持っているか、BrazeエンドポイントへのWebhookを使用する必要があります。これは、ユーザーがイベントを実行するたびにカスタム属性(`example_event_count`)をインクリメントするためです。この例では、3 つのケイデンス (1、4、7、10 など) を使用します。ケイデンスをゼロ(0、3、6、9など)から開始するには、 `minus: 1`を削除します。
{% endalert %}

### 1 つのカテゴリからのみ購入したユーザーにメッセージを送信する {#event-purchased-one-category}

このユースケースでは、ユーザーが購入したカテゴリのリストをキャプチャし、購入カテゴリが 1 つしか存在しない場合は、メッセージが表示されます。

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

### 過去 1 か月間にカスタム イベントが発生した回数を追跡する {#track}

このユースケースでは、当月の1日から前月までの間にカスタムイベントが記録された回数を計算します。その後、users/track 呼び出しを実行して、この値をカスタム属性として更新保存できます。このキャンペーンは、月次データを使用する前に 2 か月連続で実施する必要があります。

{% raw %}
\`\`\`liquid

{% capture body %}
{
"braze_id": "{{${braze_id}}}",
 "fields\_to\_export": ["custom\_events"]
 }

{% endcapture %}

{% connected_content YOUR_BRAZE_ENDPOINT/users/export/ids
:method post
:headers { "Authorization": "Bearer YOUR_API_KEY" }
 :body {{body}}
  :content\_type application/json
  :save 応答
 :retry %}

{% for custom_event in response.users[0].custom_events %}
{% assign ce_name = custom_event.name %}
{% comment %} 次のカスタムイベント名は、ターゲットのカスタムイベント用に修正する必要があります。 {% endcomment %}

{% if ce_name == "Project Exported" %}
{% comment %}{{custom\_event.name}}: {{custom\_event.count}}{% endcomment %}
{% assign current_count = custom_event.count %}
{% endif %}
{% endfor %}

{% assign prev\_month\_count = {{custom\_attribute.${projects\_exported\_prev\_month}}} %}
{% assign latest_count = current_count | minus: prev_month_count %}
{% assign now = "now" | date: "%s" %}
{% assign yesterday = {{now}} | minus:86400 %}
{% assign previous\_month = {{yesterday}} | date: "%B" %}
{% assign previous\_year = {{yesterday}} | date: "%y" %}
{% assign formatted_month = previous_month | downcase %}
{% comment %}追跡されているカスタムイベント名は、以下の属性名でターゲットのカスタムイベント用に修正する必要があります。 {% endcomment %}
\`\`\`

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

- [月の名前を別の言語で表示する](#language-display-month)
- [ユーザーの言語に基づいて画像を表示する](#language-image-display)
- [曜日とユーザーの言語に基づいてメッセージをパーソナライズします](#language-personalize-message)

### 月の名前を別の言語で表示する {#language-display-month}

このユースケースでは、現在の日付、月、年が別の言語で表示されます。この例では、スウェーデン語を使用します。

{% raw %}
\`\`\`liquid
{% assign day = 'now' | date: "%e" %}
{% assign year =  'now' | date: "%Y" %}
{% assign month =  'now' | date: "%B" %}

{% if {{month}} == '1月' %}
{{day}}1月{{year}}
{% elsif {{month)) == 'February' %}
{{day}}2月{{year}}
{% elsif {{month)) == 'March' %}
{{day}}火星 {{year}}
{% elsif {{month)) == 'April' %}
{{day}}4月 {{year}}
{% elsif {{month)) == 'May' %}
{{day}}5月 {{year}}
{% elsif {{month)) == 'June' %}
{{day}}六月{{year}}
{% elsif {{month)) == 'July' %}
{{day}}7月 {{year}}
{% elsif {{month)) == 'August' %}
{{day}}8月 {{year}}
{% elsif {{month)) == 'September' %}
{{day}}9月{{year}}
{% elsif {{month)) == 'October' %}
{{day}}10月 {{year}}
{% elsif {{month)) == 'November' %}
{{day}}11月 {{year}}
{% elsif {{month)) == 'December' %}
{{day}}12月{{year}}
{% endif %}
\`\`\`
{% endraw %}

### ユーザーの言語に基づいて画像を表示する {#language-image-display}

このユースケースでは、ユーザーの言語に基づいて画像を表示します。このユースケースは、Braze Media Libraryにアップロードされた画像でのみテストされています。

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

### 曜日とユーザーの言語に基づいてメッセージをパーソナライズします {#language-personalize-message}

このユースケースでは、現在の曜日をチェックし、その日に基づいて、ユーザーの言語が指定された言語オプションの1つに設定されている場合は、その言語で特定のメッセージが表示されます。

この例では火曜日に停止しますが、曜日ごとに繰り返すことができます。

{% raw %}
\`\`\`liquid
{% assign today  = 'now' | date: '%A' %}

{% if today == 'Monday' %}
{% if ${language} == 'es' %}
Compra hoy y lleva tu aprendizaje de idiomas a niveles más altos.🚀

{% elsif ${language} == 'en' %}
今すぐ購入して、語学学習を次のレベルに引き上げましょう。🚀

{% elsif ${language} == 'zh' %}
今天就购买并将您的语言提高到一个新水平吧。🚀

{% else %}
月曜日なのに言語が合わない
{% endif %}

{% elsif today == 'Tuesday' %}

{% if ${language} == 'zh' %}
不要忘记解锁以获取完整版本哦。🔓

{% elsif ${language} == 'en' %}
あなたの言語のフルバージョンのロックを解除することを忘れないでください。🔓

{% elsif ${language} == 'ja' %}
すべての機能を使ってみませんか 🔓

{% elsif ${language} == 'es' %}
No te olivides de desbloquear la versión completa del programa de idiomas.🔓

{% else %}
火曜日のデフォルト
{% endif %}
{% endif %}
\`\`\`
{% endraw %}

{% endapi %}

{% api %}

## その他

{% apitags %}
その他
{% endapitags %}

- [マーケティングメールをブロックしている顧客へのメール送信は避ける](#misc-avoid-blocked-emails)
- [顧客のサブスクリプション状態を使用してメッセージ内のコンテンツをパーソナライズする](#misc-personalize-content)
- [文字列内のすべての単語の最初の文字を大文字にする](#misc-capitalize-words-string)
- [カスタム属性値を配列と比較する](#misc-compare-array)
- [近日開催予定のイベントリマインダーを作成する](#misc-event-reminder)
- [配列内の文字列を検索する](#misc-string-in-array)
- [配列内の最大値を見つける](#misc-largest-value)
- [配列の最小値を求める](#misc-smallest-value)
- [文字列の末尾を照会する](#misc-query-end-of-string)
- [複数の組み合わせを持つカスタム属性からの配列内のクエリ値](#misc-query-array-values)
- [文字列を電話番号に書式設定する](#phone-number)

### マーケティングメールをブロックしている顧客へのメール送信は避ける {#misc-avoid-blocked-emails}

このユースケースでは、コンテンツブロックに保存されたブロックされたユーザーのリストを取得し、ブロックされたユーザーが今後のキャンペーンやキャンバスに伝達されたり、ターゲットにされたりしていないことを確認します。

{% alert important %}
このLiquidを使用するには、まずブロックされたメールのリストをコンテンツブロック内に保存します。リストには、メールアドレスの間に余分なスペースや文字を挿入しないでください(例: `test@braze.com,abc@braze.com`)。
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

**Explanation:**ここでは、ブロックされたメールのコンテンツブロックを参照して、潜在的な受信者のメールがこのリストに含まれているかどうかを確認します。メールが見つかった場合、メッセージは送信されません。

{% alert note %}
コンテンツブロックのサイズ制限は 5 MB です。
{% endalert %}

### 顧客のサブスクリプション状態を使用してメッセージ内のコンテンツをパーソナライズする {#misc-personalize-content}

このユースケースでは、顧客のサブスクリプション状態を取得して、パーソナライズされたコンテンツを送信します。特定のサブスクリプション グループをサブスクライブしている顧客は、電子メール サブスクリプション グループ専用のメッセージを受信します。

{% raw %}
```liquid
{% if {{subscribed_state.${subscription_group_id}}}} == 'subscribed' %}
This is an exclusive message for subscribed users!
{% else %} This is the default message for other users.
{% endif %}
```
{% endraw %}

### 文字列内のすべての単語の最初の文字を大文字にする {#misc-capitalize-words-string}

このユースケースでは、単語の文字列を受け取り、それらを配列に分割し、各単語の最初の文字を大文字にします。

{% raw %}
```liquid
{% assign words_array = {{custom_attribute.${address}}} | split: ' ' %}
{% for words in {{words_array}} %}
{{ words | capitalize | append: ' ' }}
{% endfor %} 
```
{% endraw %}

**Explanation:**ここでは、選択した文字列属性に変数を割り当て、フィルターを使用して `split` 文字列を配列に分割しました。次に、タグを使用して`for`、新しく作成した配列の各項目に変数`words`を割り当ててから、それらの単語をフィルターと`append`フィルターで`capitalize`表示し、各用語の間にスペースを追加しました。

### カスタム属性値を配列と比較する {#misc-compare-array}

このユースケースでは、お気に入りの店舗のリストを取得し、ユーザーのお気に入りの店舗のいずれかがそのリストにあるかどうかを確認し、含まれている場合は、それらの店舗からの特別オファーを表示します。

{% raw %}
\`\`\`liquid
{% assign favorite_stores = 'Target,Walmart,Costco' | split: ',' %}
{% for store in favorite_stores %}
{% if {{custom\_attribute.${favorited\_stores}}} contains {{store}} %}
本日のお知らせは{{store}}さんから

{% break %}

{% else %}
{% abort_message("No attribute found") %}
{% endif %}
{% endfor %}
\`\`\`
{% endraw %}

{% alert important %} このシーケンスには、 `break` プライマリ条件ステートメントにタグがあります。これにより、一致が見つかったときにループが停止します。一致したものを多数またはすべて表示する場合は、タグを削除します `break` 。 {% endalert %}

### 近日開催予定のイベントリマインダーを作成する {#misc-event-reminder}

このユースケースでは、ユーザーはカスタムイベントに基づいて今後のリマインダーを設定できます。このシナリオ例では、ユーザーは 26 日以上先のポリシー更新日のリマインダーを設定し、ポリシー更新日の 26 日前、13 日前、7 日前、または 2 日前にリマインダーが送信されます。

このユースケースでは、 [Webhookキャンペーン]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) またはキャンバスステップの本文に以下を含める必要があります。

{% raw %}
\`\`\`liquid
{% comment %}
reminder\_captureプロパティがBrazeに渡される方法に応じて、/without a timestamp, the number of days could impact whether a user falls on either side of the 26/13/7/2-day windows.
ユーザーがリマインダージャーニー/フローに割り当てられると、後続のキャンバスに入るようにスケジュールされます。
この「イベントリスナー」は、Brazeに送信されたカスタムイベントプロパティに基づいて、ユーザーを異なるジャーニーに分割するために使用できます。
{% endcomment %}

{% comment %}
テストの際は、キャンペーン ID、キャンペーン API エンドポイント、キャンバス ID、キャンバス API エンドポイントが正しく入力されていることを確認してください。この例では、Canvas ID と Canvas API エンドポイントがクライアントと共有するように設定されています。実際には、キャンペーン ID と Campaign API エンドポイントを使用してテストできます。
{% endcomment %}

{% comment %}
次の手順では、今日の日付とリマインダー日付の間の差を「time\_to\_reminder」として計算します。
{% endcomment %}

{% assign today = "now" | date: '%s' %}
{% assign reminder\_start\_date = {{event\_properties.${reminder\_date}}} | date: '%s' %}
{% assign time_to_reminder = reminder_start_date | minus: today %}

{% comment %}
次の手順では、time\_to\_reminderが 26 日以上先にあるかどうかを確認します。これが true の場合、ユーザーはreminder\_dateの 26 日前に後続の Canvas に入るようにスケジュールされます。
時刻は「1970 年からの秒数」から、必要な ISO 8601 形式の適切なリマインダー日付に変換されます。
注意追加のタイムゾーンは、"in\_local\_time" の API スケジュール プロパティを追加することで対応する必要があります
{% endcomment %}

{% if {{time\_to\_reminder}} > 2246400 %}
{% assign time_to_first_message = reminder_start_date | plus: 2246400 %}
{{ time_to_first_message | date: '%Y-%m-%dT%H:%M' }}
{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger\_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder\_date" : "{{event\_properties.${reminder\_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message\_personalisation\_X" : "{{event\_properties.${property\_x}}}",
"message\_personalisation\_Y" : "{{event\_properties.${property\_y}}}",
"message\_personalisation\_Z" : "{{event\_properties.${property\_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
次の手順では、time\_to\_reminderが 26 日未満で 13 日以上先かどうかを確認します。
ユーザーは 13 日目にジャーニーを入力するようにスケジュールされています。
{% endcomment %}

{% elsif 1123200 > {{time\_to\_reminder}} と {{time\_to\_reminder}} < 2246399 %}
{% assign time_to_first_message = reminder_start_date | plus: 1123200 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger\_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder\_date" : "{{event\_properties.${reminder\_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message\_personalisation\_X" : "{{event\_properties.${property\_x}}}",
"message\_personalisation\_Y" : "{{event\_properties.${property\_y}}}",
"message\_personalisation\_Z" : "{{event\_properties.${property\_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
次の手順では、time\_to\_reminderが 13 日未満で 7 日以上先にあるかどうかを確認します。
ユーザーは 7 日目にジャーニーに入るようにスケジュールされています。
{% endcomment %}

{% elsif 604800 > {{time\_to\_reminder}} と {{time\_to\_reminder}} < 1123199 %}
{% assign time_to_first_message = reminder_start_date | plus: 604800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger\_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder\_date" : "{{event\_properties.${reminder\_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message\_personalisation\_X" : "{{event\_properties.${property\_x}}}",
"message\_personalisation\_Y" : "{{event\_properties.${property\_y}}}",
"message\_personalisation\_Z" : "{{event\_properties.${property\_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
次の手順では、time\_to\_reminderが 7 日未満で 2 日以上先かどうかを確認します。
ユーザーは 2 日目にジャーニーに入るようにスケジュールされています。
{% endcomment %}

{% else {{time\_to\_reminder}} < 604799 and {{time\_to\_reminder}} > 172860 %}
{% assign time_to_first_message = reminder_start_date | plus: 172800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger\_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder\_date" : "{{event\_properties.${reminder\_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message\_personalisation\_X" : "{{event\_properties.${property\_x}}}",
"message\_personalisation\_Y" : "{{event\_properties.${property\_y}}}",
"message\_personalisation\_Z" : "{{event\_properties.${property\_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}
{% endif %}
\`\`\`
{% endraw %}

{% alert important %} 

カスタムイベント `reminder_capture`が必要であり、カスタムイベントのプロパティには少なくとも次のものが含まれている必要があります。

- `reminder-id`:カスタムイベントの識別子
- `reminder_date`:ユーザーが送信したリマインダーの期限日
- `message_personalisation_X`:送信時にメッセージをパーソナライズするために必要なプロパティ

{% endalert %}

### 配列内の文字列を検索する {#misc-string-in-array}

このユースケースでは、カスタム属性配列に特定の文字列が含まれているかどうかをチェックし、存在する場合は特定のメッセージを表示します。

{% raw %}
```liquid
{% if custom_attribute.${PartnershipProgramsNotLinked} contains 'Hertz' %}
Link your Hertz account to use Hertz Fast Lane.
{% endif %}
```
{% endraw %}

### 配列内の最大値を見つける {#misc-largest-value}

このユースケースでは、ユーザーメッセージングで使用する特定のカスタム属性配列の最大値を計算します。

たとえば、現在の最高スコアやアイテムの最高入札単価をユーザーに表示できます。

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
整数値を持ち、配列 (リスト) の一部であるカスタム属性を使用する必要があります。 {% endalert %}

### 配列の最小値を求める {#misc-smallest-value}

このユースケースでは、ユーザーメッセージングで使用する特定のカスタム属性配列の最小値を計算します。

たとえば、最低スコアや最も安いアイテムをユーザーに表示できます。

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

{% alert important %} 整数値を持ち、配列 (リスト) の一部であるカスタム属性を使用する必要があります。 {% endalert %}

### 文字列の末尾を照会する {#misc-query-end-of-string}

このユースケースでは、メッセージングで使用する文字列の末尾を照会します。

{% raw %}
\`\`\`liquid
{% assign interest = {{custom\_attribute.${買い手の利息}} | first } %}
{% assign marketplace = {{{{interest}} | split: "" | reverse | join: "" | 切り捨てる：4, ""}} %}
{% if {{marketplace}} == '3243' %}

前回のマーケットプレイス検索は{{custom\_attribute.${Last marketplace buyer interest} | date: '%d.%m.%Y'}}でした。すべての新しいオファーをチェックしてください。

{% else %}
{% abort_message() %}
{% endif %}
\`\`\`
{% endraw %}

### 複数の組み合わせを持つカスタム属性からの配列内のクエリ値 {#misc-query-array-values}

このユースケースでは、有効期限が近づいている番組のリストを取得し、ユーザーのお気に入りの番組のいずれかがそのリストにあるかどうかを確認し、存在する場合は、まもなく期限切れになることをユーザーに通知するメッセージを表示します。

{% raw %}
\`\`\`liquid
{% assign expired_shows = 'Modern Family,The Rookie,Body of Proof,Felicity' | split: ',' %}
{% for show in expired_shows %}
{% if {{custom\_attribute.${Favorite Shows}}} contains {{show}} %}
{% assign new_shows = new_shows | append: {{show}} |追加: '*' %}
{% endif %}
{% endfor %}
{% assign new\_shows\_clean = new\_shows | split: '*' %}
{% if new_shows_clean.size != 0 %}

} の全 {{new_shows_clean | join: ', ' }エピソードは 9/8 で期限切れになります - なくなる前に今すぐ見てください!

{% else %}
{% abort_message("Not found") %}
{% endif %}
\`\`\`
{% endraw %}

{% alert important %} 最初に配列間の一致を見つけてから、最後に一致を分割するロジックを構築する必要があります。 {% endalert %}

### 文字列を電話番号に書式設定する {#phone-number}

このユースケースでは、ユーザープロファイルフィールド(デフォルトでは整数の文字列としてフォーマット)に `phone_number` インデックスを付け、ローカルの電話番号標準に基づいて再フォーマットする方法を示します。たとえば、(123)-456-7890 に1234567890します。

{% raw %}
\`\`\`liquid
{% assign phone = {{${phone\_number}}} | remove: "-" | split: '' %}

({{ phone[0] }}{{ phone[1] }}{{ phone[2] }})-{{ phone[3] }}{{ phone[4] }}{{ phone[5] }}-{{ phone[6] }}{{ phone[7] }}{{ phone[8] }}{{ phone[9] }}
\`\`\`
{% endraw %}

{% endapi %}

{% api %}

## プラットフォーム ターゲティング

{% apitags %}
プラットフォーム ターゲティング
{% endapitags %}

- [デバイスのOSでコピーを区別する](#platform-device-os)
- [特定のプラットフォームのみをターゲットにする](#platform-target)
- [特定の OS バージョンの iOS デバイスのみをターゲットにする](#platform-target-ios-version)
- [Web ブラウザーのみを対象とする](#platform-target-web)
- [特定の携帯通信会社をターゲットに設定する](#platform-target-carrier)

### デバイスのOSでコピーを区別する {#platform-device-os}

このユースケースでは、ユーザーがどのプラットフォームを使用しているかを確認し、プラットフォームに応じて特定のメッセージを表示します。

たとえば、モバイル ユーザーには短いバージョンのメッセージ コピーを表示し、他のユーザーには通常の長いバージョンのコピーを表示することができます。また、モバイル ユーザーには、Web ユーザーには関係ない特定のメッセージを表示することもできます。たとえば、iOS のメッセージでは Apple Pay について説明できますが、Android のメッセージでは Google Pay について言及する必要があります。

{% raw %}
\`\`\`liquid
{% if targeted\_device.${platform} == "ios" or targeted\_device.${platform} == "android" %}
これは短いコピーです。

{% else %}
これは通常のコピーであり、短いバージョンよりもはるかに長いです。
{% endif %}
\`\`\`
{% endraw %}

{% alert note %}
Liquid では大文字と小文字が区別され、 `targeted_device.${platform}` すべて小文字で値を返します。
{% endalert %}

### 特定のプラットフォームのみをターゲットにする {#platform-target}

このユースケースでは、ユーザーのデバイスプラットフォームがキャプチャされ、プラットフォームに応じてメッセージが表示されます。

たとえば、Android ユーザーにのみメッセージを送信することができます。これは、セグメンテーション ツール内でアプリを選択する代わりに使用できます。

{% raw %}
\`\`\`liquid
{% if {{targeted\_device.${platform}}} == 'android' %} 

Androidユーザーへのメッセージです! 

{% else %}  
{% abort_message %}
{% endif %}
\`\`\`
{% endraw %}

### 特定の OS バージョンのデバイスのみをターゲットにする {#platform-target-ios-version}

このユースケースでは、ユーザーのOSバージョンが特定のバージョンのセットに該当するかどうかをチェックし、該当する場合は特定のメッセージを表示します。

この例では、OS バージョン 10.0 以前のユーザーに、ユーザーのデバイス OS のサポートを段階的に廃止するという警告を送信します。

{% raw %}
\`\`\`liquid
{% if {{targeted\_device.${os}}} == "10.0" or {{targeted\_device.${os}}} == "10.0.1" or {{targeted\_device.${os}}} == "10.0.2" or {{targeted\_device.${os}}} == "10.0.3" or {{targeted\_device.${os}}} == "10.1" or {{targeted\_device.${os}}} == "10.2" or {{targeted\_device.${os}}} == "10.2.1" or {{targeted\_device.${os}}} == "10.3" or {{targeted\_device.${os}}} == "10.3.1" or {{targeted\_device.${os}}} == "10.3.2" or {{targeted\_device.${os}}} == "10.3.3" or {{targeted\_device.${os}}} == "10.3.4" or {{targeted\_device.${os}}} == "9.3.1" or {{targeted\_device.${os}}} == "9.3.2" or {{targeted\_device.${os}}} == "9.3.3" or {{targeted\_device.${os}}} == "9.3.4" or {{targeted\_device.${os}}} == "9.3.5" %}

デバイスのオペレーティング システムのサポートを段階的に廃止しています。最高のアプリエクスペリエンスを得るには、必ず最新のソフトウェアに更新してください。

{% else %}
{% abort_message %}
{% endif %}
\`\`\`
{% endraw %}

### Web ブラウザのみをターゲットにする {#platform-target-web}

このユースケースでは、ユーザーのターゲットデバイスがMacまたはWindowsで実行されているかどうかを確認し、実行されている場合は特定のメッセージを表示します。

{% raw %}
\`\`\`liquid
{% if {{targeted\_device.${os}}} == 'Mac' or {{targeted\_device.${os}}} == 'Windows' %}

このメッセージは、デスクトップのWebブラウザに表示されます。

{% else %}
{% abort_message %}
{% endif %}
\`\`\`
{% endraw %}

次のユースケースでは、WebユーザーがiOSまたはAndroidを使用しているかどうかを確認し、使用している場合は特定のメッセージを表示します。

{% raw %}
\`\`\`liquid
{% if {{targeted\_device.${os}}} == 'iOS' and {{targeted\_device.${platform}}} == 'web' %}

iOS用のコンテンツ。

{% elsif {{targeted\_device.${os}}} == 'android' and {{targeted\_device.${platform}}} == 'web' %}

Android向けのコンテンツ。

{% else %}
{% abort_message %}
{% endif %}
\`\`\`
{% endraw %}

### 特定の携帯通信会社をターゲットに設定する {#platform-target-carrier}

このユースケースでは、ユーザーのデバイスキャリアがVerizonであるかどうかを確認し、Verizonの場合は特定のメッセージを表示します。

プッシュ通知とアプリ内メッセージチャネルの場合、Liquidを使用してメッセージ本文でデバイスキャリアを指定できます。受信者の携帯通信会社が一致しない場合、メッセージは送信されません。

{% raw %}
\`\`\`liquid
{% if {targeted\_device.${carrier}} contains "verizon" or {targeted\_device.${carrier}} contains "Verizon" %}

これはVerizonユーザーへのメッセージです!

{% else %}
{% abort_message %}
{% endif %}
\`\`\`
{% endraw %}

{% endapi %}

{% api %}

## タイムゾーン

{% apitags %}
タイムゾーン
{% endapitags %}

- [ユーザーのタイムゾーンに応じてメッセージをパーソナライズする](#personalize-timezone)
- [CST タイムゾーンをカスタム属性に追加する](#time-append-cst)
- [タイムスタンプの挿入](#time-insert-timestamp)
- [ユーザーのローカルタイムゾーンの時間帯にのみCanvasプッシュを送信する](#time-canvas-window)
- [ユーザーのローカルタイムゾーンの時間帯の間に繰り返しアプリ内メッセージキャンペーンを送信する](#time-reocurring-iam-window)
- [ユーザーのローカル タイム ゾーンで平日と週末に異なるメッセージを送信する](#time-weekdays-vs-weekends)
- [ユーザーのローカルタイムゾーンの時刻に基づいて異なるメッセージを送信する](#time-of-day)

### ユーザーのタイムゾーンに応じてメッセージをパーソナライズする {#personalize-timezone}

このユースケースでは、ユーザーのタイムゾーンに基づいて異なるメッセージが表示されます。

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

### CST タイムゾーンをカスタム属性に追加する {#time-append-cst}

このユースケースでは、特定のタイムゾーンでカスタム日付属性を表示します。

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

### タイムスタンプの挿入 {#time-insert-timestamp}

このユースケースでは、現在のタイムゾーンのタイムスタンプを含むメッセージが表示されます。

次の例では、日付を YYYY-mm-dd HH:MM:SS として表示します (2021-05-03 10:41:04 など)。

{% raw %}
```liquid
{{${user_id} | default: 'You'}} received a campaign, rendered at ({{ "now" | time_zone: ${time_zone} | date: "%Y-%m-%d %H:%M:%S" }})
```
{% endraw %}

### ユーザーのローカルタイムゾーンの時間帯にのみCanvasプッシュを送信する {#time-canvas-window}

このユースケースでは、ユーザーのローカルタイムゾーンでの時刻をチェックし、設定された時間内であれば、特定のメッセージが表示されます。

{% raw %}
\`\`\`liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}

これは、午前8時から午後8時の間に送信されるメッセージです。
\`\`\`
{% endraw %}

### ユーザーのローカルタイムゾーンの時間帯の間に繰り返しアプリ内メッセージキャンペーンを送信する {#time-reoccurring-iam-window}

このユースケースでは、ユーザーの現在の時刻が設定されたウィンドウ内にある場合にメッセージが表示されます。

たとえば、次のシナリオでは、店舗が閉店していることをユーザーに知らせます。

{% raw %}
\`\`\`liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 21 or hour < 10 %}

閉店しました。午前11時から午後9時の間に戻ってきてください!

{% else %}
{% abort_message("Not sent because the store is open") %}
{% endif %}
\`\`\`
{% endraw %}

### ユーザーのローカル タイム ゾーンで平日と週末に異なるメッセージを送信する {#time-weekdays-vs-weekends}

このユースケースでは、ユーザーの現在の曜日が土曜日か日曜日かを確認し、曜日に応じて異なるメッセージを表示します。

{% raw %}
\`\`\`liquid
{% assign today = 'now' | time_zone: ${time_zone} | date: "%A" %}
{% if {{today}} == 'Saturday' or {{today}} == 'Sunday' %}
{{today}}ですが、取引のためにアプリを開いてみませんか?

{% else %}
{{today}}ですが、ぜひお店に足を運んでみませんか?
{% endif %}
\`\`\`
{% endraw %}

### ユーザーのローカルタイムゾーンの時刻に基づいて異なるメッセージを送信する {#time-of-day}

このユースケースでは、ユーザーの現在時刻が設定されたウィンドウ外にある場合にメッセージが表示されます。

たとえば、時間帯によって異なる時間的制約のある営業案件についてユーザーに伝えることができます。

{% raw %}
\`\`\`liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}

今日の仕事の後にこの新しいバーをチェックしてください。HHスペシャル!
\`\`\`
{% endraw %}

{% alert note %} これは [クワイエットアワー]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/time_based_campaign/#time-based-functionalities-for-campaigns)の反対です。 {% endalert %}

{% endapi %}

{% api %}

## 週/Day/Month

{% apitags %}
週/Day/Month
{% endapitags %}

- [前月の名前をメッセージに取り込む](#month-name)
- [毎月末にキャンペーンを送信する](#month-end)
- [月の最終日(平日)にキャンペーンを送信する](#day-of-month-last)
- [毎月異なるメッセージを送信する](#day-of-month)
- [曜日ごとに異なるメッセージを送信する](#day-of-week)

### 前月の名前をメッセージに取り込む {#month-name}

このユースケースでは、現在の月を取得し、メッセージングで使用する前月を表示します。

{% raw %}
\`\`\`liquid
{% assign today = 'now' | date: "%m" %}
{% assign last\_month = {{today}} | minus:1 %}
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
{% elsif last_month == 12 %}
{% assign month = "December" %}
{% endif %}

以下は、{{month}}での支出の概要です。
\`\`\`
{% endraw %}

### 毎月末にキャンペーンを送信する {#month-end}

このユースケースでは、現在の日付が日付のリストに含まれているかどうかをチェックし、日付に応じて特定のメッセージを表示します。

{% alert note %} これにはうるう年(2月29日)は含まれていません。 {% endalert %}

{% raw %}
\`\`\`liquid
{% assign current_date = 'now' | date: '%b %d' %}

{% if current_date == "Jan 31" or current_date == "Feb 28" or current_date == "Mar 31" or current_date == "Apr 30" or current_date == "May 31" or current_date == "Jun 30" or current_date == "Jul 31" or current_date == "Aug 31" or current_date == "Sep 30" or current_date == "Oct 31" or current_date == "Nov 30" or current_date == "Dec 31" %}

日付が正しい

{% else %}
{% abort_message("Date is not listed") %}
{% endif %}
\`\`\`
{% endraw %}

### 月の最終日(平日)にキャンペーンを送信する {#day-of-month-last}

このユースケースでは、現在の月と日をキャプチャし、現在の日が月の最後の平日内にあるかどうかを計算します。

たとえば、月の最終水曜日にユーザーにアンケートを送信して、製品に関するフィードバックを求めることができます。

{% raw %}
\`\`\`liquid
{% comment %}今日の日付から日、曜日名、月、年を取得します。{% endcomment %}
{% assign current_day = "now" | date: "%d" %}
{% assign current_day_name = "now" | date: "%a" %}
{% assign current_month = "now" | date: "%b" %}
{% assign current_year = "now" | date: "%Y" %}

{% comment %}当月に正しい日数を割り当てます。{% endcomment %}

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

{% comment %}現在の月が 2 月の場合は、うるう年を考慮して正しい日数を割り当てます。{% endcomment %}

{% assign leap_year_remainder = {{current_year | modulo: 4 }} != "0" %}
{% if leap_year_remainder == 0 and current_month == "Feb" %}
{% assign last_day_of_month = 29 %}
{% elsif leap_year_remainder != "0" and current_month == "Feb" %}
{% assign last_day_of_month = 28 %}
{% endif %}

{% comment %}今日の日付が月の最終日から 1 週間以内であることを確認します。そうでない場合は、メッセージを中止します。その場合は、今日が水曜日であることを確認してください。そうでない場合は、メッセージを中止します。{% endcomment %}

{% assign diff_in_days = last_day_of_month | minus: current_day | plus: 1%}
{% if diff_in_days <= 7 %}
{% unless current_day_name == "Wed" %}
{% abort_message("Wrong day of the week") %}
{% endunless %}
{% else %}
{% abort_message("Not the last week of the month") %}
{% endif %}
\`\`\`
{% endraw %}

### 毎月異なるメッセージを送信する {#day-of-month}

このユースケースでは、現在の日付がリスト上の日付と一致するかどうかをチェックし、日に応じて個別のメッセージを表示します。

{% raw %}
\`\`\`liquid
{% assign today = 'now' | time_zone: {{${time_zone}}} |日付: "%Y-%m-%d" %}
{% assign day_1 = "2019-12-01" | time_zone: {{${time_zone}}} |日付: "%Y-%m-%d" %}
{% assign day_2 = "2019-12-02" | time_zone: {{${time_zone}}} |日付: "%Y-%m-%d" %}
{% assign day_3 = "2019-12-03" | time_zone: {{${time_zone}}} |日付: "%Y-%m-%d" %}

{% if today == day_1 %}
2019-12-01のご挨拶

{% elsif today == day_2 %}
2019-12-02 のご挨拶

{% elsif today == day_3%}
2019-12-03 のメッセージ

{% else %}
{% abort_message("Date not listed") %}
{% endif %}
\`\`\`
{% endraw %}

### 曜日ごとに異なるメッセージを送信する {#day-of-week}

このユースケースでは、現在の曜日をチェックし、曜日に応じて個別のメッセージを表示します。

{% raw %}
\`\`\`liquid
{% assign today = 'now' | date: "%A" %}
{% case today %}
{% when 'Monday' %}
月曜日のコピー

{% when 'Tuesday' %}
火曜日のコピー

{% when 'Wednesday' %}
水曜日のコピー

{% when  'Thursday' %}
木曜日のコピー

{% when  'Friday' %}
金曜日のコピー

{% when 'Saturday' %}
土曜日のコピー

{% when 'Sunday' %}
日曜日のコピー

{% else %}
デフォルトコピー
{% endcase %}
\`\`\`
{% endraw %}

{% alert note %}
「default copy」という行を に置き換え {% raw %}`{% abort_message() %}`{% endraw %} て、曜日が不明な場合にメッセージが送信されないようにすることができます。
{% endalert %}

{% endapi %}
