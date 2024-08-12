---
nav_title: フィルター
article_title: 液体フィルター
page_order: 3
description: "この参照ページには、静的または動的コンテンツの再フォーマットに使用できるフィルタがリストされています。"

---

# フィルター

> このリファレンス記事では、液体中のフィルターの概要と、ろう付けでサポートされているフィルターのカバーについて説明します。これらのフィルタをどのように使用できるかについてのアイデアを探していますか?[液体ユースケースライブラリ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/)をチェックしてください。

{% raw %}

フィルタは、液体内の数値、文字列、変数、およびオブジェクトの出力を変更する方法です。フィルタを使用して、文字列を小文字から大文字に変更したり、加算や除算などの数学的演算を実行したりするなど、静的テキストまたは動的テキストを再フォーマットできます。

フィルタは、出力タグ`{{ }}` 内に配置する必要があり、パイプ文字`|` で示されます。

{% endraw %}

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{"Big Sale" | upcase}}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
BIG SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

この例では、`Big Sale` は文字列で、`upcase` は適用されているフィルタです。

1つの出力に複数のフィルタを使用できます。それらは左から右に適用されます。

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
 {{ "Big Sale" | upcase | remove: "BIG" }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert important %}
ろう付けは、Shopifyのすべての液体フィルターをサポートしているわけではありません。このページでは、ろう付けがテストした液体フィルターのアウトラインを作成しますが、完全なリストではない場合があります。メッセージを送信する前に必ず液体をテストしてください。
<br><br>ここにリストされていないフィルタに関する質問がある場合は、カスタマーサクセスマネージャーに連絡してください。
{% endalert %}

## 配列フィルタ

配列フィルタは、配列の出力を変更するために使用されます。

| フィルタ| 定義| サポートされる|
| :------------------- | :----------------------------------------------------------------------------------------------------------------- | :-------- |
| [join][1.1] | パラメータとして渡された文字で配列の要素を結合します。結果は単一の文字列になります。| ✅ Yes |
| [最初の][1.2] | 配列の最初の要素を返します。カスタム属性配列では、これが最も古い付加価値です。| ✅ Yes |
| [last][1.3] | 配列の最後の要素を返します。カスタム属性配列では、これは最後に追加された値です。| ✅ Yes |
| [compact][1.4] | 配列から任意の`nil`項目を削除します。| ✅ Yes |
| [concat][1.5] | 配列を別の配列と結合します。| ✅ Yes |
| [index][1.6] | 配列内の指定されたインデックス位置の項目を返します。配列の最初の要素は`[0]`で参照されます。| ✅ Yes |
| [map][1.7] | 配列要素の属性をパラメータとして受け入れ、配列要素の値から配列を作成します。| ✅ Yes |
| [reverse][1.8] | 配列内の項目の順序を逆にします。| ✅ Yes |
| [size][1.9] | 文字列の大きさ(文字数)または配列(要素数)を返します。| ✅ Yes |
| [sort][1.10] | 配列内の要素の属性によって配列の要素を並べ替えます。| ✅ Yes |
| [sort\_natural][1.11] | 大文字小文字を区別しないアルファベット順に配列内の項目を並べ替えます。| ✅ Yes |
| [uniq][1.12] | 配列内の要素の重複したインスタンスを削除します。| ✅ Yes |
| [ここで][1.13] | 特定のプロパティ値を持つ項目のみを含めるように配列をフィルタリングします。| ✅ Yes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## カラーフィルター

[カラーフィルタ][2.1]はブレーズではサポートされていません。

## フォントフィルタ

[フォントフィルタ][3.1]はブレーズではサポートされていません。

## 演算フィルタ

演算フィルタを使用すると、数学演算を実行できます。1 つの出力で複数のフィルタを使用する場合、フィルタは左から右に適用されます。

| フィルタ| 定義| サポートされる|
| :------ |:----------------| :-------- |
| [abs][4.1] | 数値の絶対値を返します。| ✅ Yes |
| [at\_most][4.2] | 数値を最大値に制限します。| ✅ Yes |
| [少なくとも][4.3] | 数値を最小値に制限します。| ✅ Yes |
| [ceil][4.4] | 最も近い整数まで丸めます。| ✅ Yes |
| [divided\_by][4.5] | 出力を数値で除算します。出力は、最も近い整数に切り捨てられます。丸みを避けるために、次のヒントを確認してください。| ✅ Yes |
| [floor][4.6] | 出力を最も近い整数に丸めます。| ✅ Yes |
| [マイナス][4.7] | 出力から数値を減算します。| ✅ Yes |
| [plus][4.8] | 出力に数値を追加します。| ✅ Yes |
| [round][4.9] | 最も近い整数または指定した小数点以下の桁数に丸めます。| ✅ Yes |
| [回][4.10] | 出力に数値を乗算します。| ✅ Yes |
| [modulo][4.11] | 出力を数値で除算し、剰余を返します。| ✅ Yes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert tip %}
整数(整数) を液体の整数で除算する場合、答えが浮動小数点数(10 進数) の場合、Liquid は自動的に最も近い整数に切り捨てます。ただし、整数を浮動小数点で除算すると、常に浮動小数点が得られます。つまり、整数をfloat (1.0, 2.0, 3.0) に変換してfloat を返すことができます。
{% raw %}
<br><br>たとえば、`{{15 | divided_by: 2}}` は`7` を出力し、`{{15 | divided_by: 2.0}}` は`7.5` を出力します。
{% endraw %}
{% endalert %}

### カスタム属性を使用した数学演算

2 つのカスタム属性間で数学演算を実行することはできないことに注意してください。

{% raw %}

```liquid
{{custom_attribute.${current_rewards_balance} | plus: {{custom_attribute.${giftcard_balance}}}}}
```

この例は、Liquid の1 行で複数のカスタム属性を参照できないため、機能しません。代わりに、数学関数を実行する前に、これらの値の少なくとも1つに変数を割り当てる必要があります。2 つのカスタム属性を一緒に追加するには、2 行のLiquid が必要です。

1. カスタム属性を変数に割り当てるには、
2. 1 つは加算を実行します。

たとえば、ギフトカード残高と報酬残高を加算して、ユーザーの現在の残高を計算するとします。まず、`assign` タグを使用して、`current_rewards_balance` のカスタム属性を"balance" という用語で置き換えます。これは、`balance` という名前の変数があり、これを操作できることを意味します。

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

次に、`plus` フィルタを使用して、各ユーザーのギフトカード残高と、`{{balance}}` オブジェクトで示される報酬残高を組み合わせます。
{% endraw %}
{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
You have $35 to spend!
```
{% endraw %}
{% endtab %}
{% endtabs %}

## マネーフィルター

購入時のユーザー、口座残高、またはお金に関するものを更新する場合は、マネーフィルターを使用する必要があります。マネーフィルタは、小数点以下の桁数が適切な位置にあること、および更新の一部が失われないことを確認します(末尾のペスキー`0` など)。

| フィルタ| 定義| サポートされる|
| :--------------- | :--------------- | :-------- |
| [money][5.1] | 小数点以下の桁数が正しい位置にあることを保証するための数値の書式、および任意の数値の末尾からゼロが削除されないようにする| ✅ Yes |
| [money\_with\_currency][5.2] | 通貨記号付きの数値を書式設定します。| ⛔ No |
| [money\_without\_currency][5.4] | 通貨記号のない数値を書式設定します。| ⛔ No |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### ShopifyのマネーフィルターとBrazeのマネーフィルター

{% alert warning %}
Shopify `money` フィルタの動作は、ブレーズでの使用方法とは異なります。予想される動作を正確に示すには、次の例を参照してください。
{% endalert %}

{% raw %}
カスタム属性(`account_balance` など) を入力する場合は、常に`money` フィルタを使用して、小数点以下の桁数が適切な位置にあること、およびゼロが数字の末尾から削除されないことを確認する必要があります。

```liquid
${{custom_attribute.${account_balance} | money}}
```
{% endraw %}

| MONEY FILTER | でMONEY FILTER |
| :------------------------------------------ | :------------------------------------------ |
| ![マネーフィルタあり][1] | ![マネーフィルタなし][2] |
| ここで、`account_balance` は`17.8` で入力されます。| `account_balance` は`17.8` で入力されます。|
{: .reset-td-br-1 .reset-td-br-2}

Brazeの`money`フィルタは、プリセット設定に応じて自動的に小数点を適用しない点でShopifyと異なります。たとえば、`rewards_redeemed` に`145` の値が含まれる次のシナリオを考えます。

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | money }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
$145.00
```
{% endraw %}
{% endtab %}
{% endtabs %}

Shopify の[money][5.1] フィルタによれば、これは`$1.45` の出力を持つはずですが、Braze では`$145.00` の出力を持ちます。回避策として、`divided_by` フィルタを使用して、マネーフィルタを適用する前に数値を10 進数に操作できます。

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | divided_by: 100.00 | money }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
$1.45
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 文字列フィルタ

文字列フィルタは、文字列の出力と変数を操作するために使用されます。文字列は英数字の組み合わせであり、引用符で囲む必要があります。

{% alert note %}
直線引用符は、Liquidの中括弧引用符とは異なります。テキストエディタからBraze にLiquid をコピー&ペーストするときは注意してください。中抜きの引用符があると、Liquid にエラーが発生します。液体を直接ろうそくに書き込む場合は、直線引用符が自動的に適用されます。
{% endalert %}

| フィルタ| 説明| サポート対象|
| :--------------- | ------------- | --------- |
| [append][6.1] | 文字列に文字を追加します。| ✅ Yes |
| [camelcase][6.2] | 文字列をCamelCase に変換します。| ⛔ No |
| [capitalize][6.3] | 文字列の最初の単語を大文字にします。| ✅ Yes |
| [小文字][6.4] | 文字列を小文字に変換します。| ✅ Yes |
| [escape][6.5] | 文字列をエスケープします。| ✅ Yes |
| [handle/handleize][6.6] | 文字列をハンドルにフォーマットします。| ⛔ No |
| [md5][6.7] | 文字列をMD5ハッシュに変換します。詳細は[エンコードフィルタ][3] を参照してください。| ✅ Yes |
| [sha1][6.8] | 文字列をSHA-1 ハッシュに変換します。詳細は[エンコードフィルタ][3] を参照してください。| ✅ Yes |
| hmac\_sha1\_hex<br>(以前は[hmac\_sha\_1][6.10])|ハッシュメッセージ認証コード(HMAC)を使用して、文字列をSHA-1ハッシュに変換します。メッセージの秘密鍵をパラメータとしてフィルタに渡します。詳細は[エンコードフィルタ][3] を参照してください。| ✅ Yes |
| [hmac\_sha256][6.11] | ハッシュメッセージ認証コード(HMAC)を使用して、文字列をSHA-256 ハッシュに変換します。パラメータとしてメッセージのシークレットキーをフィルタに渡します。| ✅ Yes |
| hmac\_sha512 | ハッシュメッセージ認証コード(HMAC)を使用して、文字列をSHA-512ハッシュに変換します。パラメータとしてメッセージのシークレットキーをフィルタに渡します。| ✅ Yes |
| [newline\_to\_br][6.12] | `<br>`改行HTMLタグを文字列の改行ごとに挿入します。| ✅ Yes |
| [pluralize][6.13] | 英語文字列の単数形または複数形を数値に基づいて出力します。| ⛔ No |
| [prepend][6.14] | 文字列の先頭に文字を付加します。| ✅ Yes |
| [remove][6.15] | 文字列から部分文字列の出現をすべて削除します。| ✅ Yes |
| [remove\_first][6.16] | 文字列から部分文字列の最初の出現のみを削除します。| ✅ Yes |
| [replace][6.17] | 文字列のすべての出現箇所を部分文字列で置き換えます。| ✅ Yes |
| [replace\_first][6.18] | 文字列の最初の出現を部分文字列で置き換えます。| ✅ Yes |
| [slice][6.19] | スライスフィルタは、指定したインデックスから始まる部分文字列を返します。| ✅ Yes |
| [split][6.20] | 分割フィルタは、部分文字列をパラメータとして受け取ります。部分文字列は、文字列を配列に分割するための区切り文字として使用されます。| ✅ Yes |
| [strip][6.21] | 文字列の左右からタブ、空白、改行(すべての空白)を取り除きます。| ✅ Yes |
| [lstrip][6.22] | 文字列の左側からタブ、空白、および改行(すべての空白) を取り除きます。| ⛔ いいえ |
| [rstrip][6.23] | 文字列の右側からタブ、空白、および改行(すべての空白) を取り除きます。| ⛔ いいえ |
| [strip\_html][6.24] | 文字列からすべてのHTML タグを削除します。| ✅ Yes |
| [strip\_newlines][6.25] | 文字列から改行/改行を削除します。| ✅ Yes |
| [truncate][6.26] | 文字列を最初のパラメータとして渡された文字数まで切り捨てます。省略記号(...) が切り捨てられた文字列に追加され、文字数に含まれます。| ✅ Yes |
| [truncatewords][6.27] | 最初のパラメータとして渡された単語の数まで文字列を切り捨てます。省略記号(...) が切り捨てられた文字列に追加されます。| ✅ Yes |
| [upcase][6.28] | 文字列を大文字に変換します。| ✅ Yes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 追加のフィルター

以下の一般的なフィルタは、コンテンツのフォーマットや変換など、さまざまな目的に役立ちます。

| フィルタ| 説明| サポート対象|
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| [日付][7.1] | タイムスタンプを別の日付形式に変換します。詳細については、[日付フィルタ](#date-filter)を参照してください。| ✅ Yes |
| [default][7.2] | 値が割り当てられていない変数のデフォルト値を設定します。文字列、配列、ハッシュで使用できます。| ✅ Yes |
| [format\_address][7.3] | アドレスのロケールに従って、アドレスの要素を順番に出力するアドレスをフォーマットします。| ⛔ No |
| [highlight][7.4] | HTML `<strong>` タグで検索結果内の単語をラップし、サブミットされた検索用語と一致する場合はクラスhighlight を付けます。| ⛔ No |
| `time_zone`| [タイムゾーンフィルタ](#time-zone-filter)を参照してください。| ✅ はい|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

[詳細フィルタ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/) ページでは、エンコーディングやURL フィルタなど、サポートされているフィルタを見つけることができます。

### 日付フィルター {#date-filter}

`date` フィルタを使用して、タイムスタンプを別の日付形式に変換できます。パラメータを`date`フィルタに渡して、タイムスタンプを再フォーマットできます。これらのパラメータの例については、[strfti.me](http://www.strfti.me/)を参照してください。

たとえば、`date_attribute` の値がタイムスタンプ`2021-06-03 17:13:41 UTC` であるとします。

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%b %d'}}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
03 June
```
{% endraw %}
{% endtab %}
{% endtabs %}

`strftime` フォーマットオプションに加えて、Braze は`%s` 日付フィルタを使用してタイムスタンプをUnix 時刻に変換することもサポートしています。例えば、Unix 時刻で`date_attribute` を取得するには、次のようにします。

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%s' }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
1433351621
```
{% endraw %}
{% endtab %}
{% endtabs %}

### タイムゾーンフィルタ {#time-zone-filter}

{% raw %}
Shopifyのドキュメントに記載されているフィルタに加えて、Brazeは`time_zone`フィルタもサポートしています。

`time_zone`フィルタは、時刻、タイムゾーン、日付の形式を取り、指定された日付形式でそのタイムゾーンの時刻を返します。たとえば、`{{custom_attribute.$date_attribute}}}` の値が`2021-08-04 9:00:00 UTC` であるとします。
{% endraw %}

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | time_zone: 'America/Los_Angeles' | date: '%a %b %e %T' }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
Wed August 4 2:00:00
```
{% endraw %}
{% endtab %}
{% endtabs %}

また、予約変数`now` を使用して、現在の日付と時刻にアクセスして操作することもできます。

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{ 'now' | date: '%Y-%m-%d %H:%M:%S' }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
2021-08-04 18:13:13
```
{% endraw %}
{% endtab %}
{% endtabs %}


[1.1]: https://shopify.dev/api/liquid/filters/array-filters#join
[1.2]: https://shopify.dev/api/liquid/filters/array-filters#first
[1.3]: https://shopify.dev/api/liquid/filters/array-filters#last
[1.4]: https://shopify.dev/api/liquid/filters#compact
[1.5]: https://shopify.dev/api/liquid/filters/array-filters#concat
[1.6]: https://shopify.dev/api/liquid/filters/array-filters#index
[1.7]: https://shopify.dev/api/liquid/filters/array-filters#map
[1.8]: https://shopify.dev/api/liquid/filters/array-filters#reverse
[1.9]: https://shopify.dev/api/liquid/filters/array-filters#size
[1.10]: https://shopify.dev/api/liquid/filters/array-filters#sort
[1.11]: https://shopify.dev/api/liquid/filters#sort_natural
[1.12]: https://shopify.dev/api/liquid/filters/array-filters#uniq
[1.13]: https://shopify.dev/api/liquid/filters#where

[2.1]: https://shopify.dev/api/liquid/filters/color-filters
[3.1]: https://shopify.dev/api/liquid/filters/font-filters

[4.1]: https://shopify.dev/api/liquid/filters/math-filters#abs
[4.2]: https://shopify.dev/api/liquid/filters/math-filters#at_most
[4.3]: https://shopify.dev/api/liquid/filters/math-filters#at_least
[4.4]: https://shopify.dev/api/liquid/filters/math-filters#ceil
[4.5]: https://shopify.dev/api/liquid/filters/math-filters#divided_by
[4.6]: https://shopify.dev/api/liquid/filters/math-filters#floor
[4.7]: https://shopify.dev/api/liquid/filters/math-filters#minus
[4.8]: https://shopify.dev/api/liquid/filters/math-filters#plus
[4.9]: https://shopify.dev/api/liquid/filters/math-filters#round
[4.10]: https://shopify.dev/api/liquid/filters/math-filters#times
[4.11]: https://shopify.dev/api/liquid/filters/math-filters#modulo

[5.1]: https://shopify.dev/api/liquid/filters/money-filters#money
[5.2]: https://shopify.dev/api/liquid/filters/money-filters#money_with_currency
[5.3]: https://shopify.dev/api/liquid/filters/money-filters#money_without_trailing_zeros
[5.4]: https://shopify.dev/api/liquid/filters/money-filters#money_without_currency

[6.1]: https://shopify.dev/api/liquid/filters/string-filters#append
[6.2]: https://shopify.dev/api/liquid/filters/string-filters#camelcase
[6.3]: https://shopify.dev/api/liquid/filters/string-filters#capitalize
[6.4]: https://shopify.dev/api/liquid/filters/string-filters#downcase
[6.5]: https://shopify.dev/api/liquid/filters/string-filters#escape
[6.6]: https://shopify.dev/api/liquid/filters/string-filters#handle-handleize
[6.7]: https://shopify.dev/api/liquid/filters/string-filters#md5
[6.8]: https://shopify.dev/api/liquid/filters/string-filters#sha1
[6.10]: https://shopify.dev/api/liquid/filters/string-filters#hmac_sha1
[6.11]: https://shopify.dev/api/liquid/filters/string-filters#hmac_sha256
[6.12]: https://shopify.dev/api/liquid/filters/string-filters#newline_to_br
[6.13]: https://shopify.dev/api/liquid/filters/string-filters#pluralize
[6.14]: https://shopify.dev/api/liquid/filters/string-filters#prepend
[6.15]: https://shopify.dev/api/liquid/filters/string-filters#remove
[6.16]: https://shopify.dev/api/liquid/filters/string-filters#remove_first
[6.17]: https://shopify.dev/api/liquid/filters/string-filters#replace
[6.18]: https://shopify.dev/api/liquid/filters/string-filters#replace_first
[6.19]: https://shopify.dev/api/liquid/filters/string-filters#slice
[6.20]: https://shopify.dev/api/liquid/filters/string-filters#split
[6.21]: https://shopify.dev/api/liquid/filters/string-filters#strip
[6.22]: https://shopify.dev/api/liquid/filters/string-filters#lstrip
[6.23]: https://shopify.dev/api/liquid/filters/string-filters#rstrip
[6.24]: https://shopify.dev/api/liquid/filters/string-filters#strip_html
[6.25]: https://shopify.dev/api/liquid/filters/string-filters#strip_newlines
[6.26]: https://shopify.dev/api/liquid/filters/string-filters#truncate
[6.27]: https://shopify.dev/api/liquid/filters/string-filters#truncatewords
[6.28]: https://shopify.dev/api/liquid/filters/string-filters#upcase

[7.1]: https://shopify.dev/api/liquid/filters/additional-filters#date
[7.2]: https://shopify.dev/api/liquid/filters/additional-filters#default
[7.3]: https://shopify.dev/api/liquid/filters/additional-filters#format_address
[7.4]: https://shopify.dev/api/liquid/filters/additional-filters#highlight


[1]: {% image_buster /assets/img/with_money_filter.png %}
[2]: {% image_buster /assets/img/without_money_filter.png %}
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters
