---
nav_title: フィルター
article_title: 液体フィルター
page_order: 3
description: "このリファレンス・ページでは、静的または動的コンテンツを再フォーマットするために使用できるフィルタをリストアップしている。"

---

# フィルター

> この参考記事では、Liquidにおけるフィルターの概要と、Brazeでサポートされているフィルターを取り上げている。これらのフィルターの使い方のアイデアをお探しですか？[リキッドのユースケースライブラリーを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/)チェックしよう。

{% raw %}

フィルターは、Liquid の数値、文字列、変数、オブジェクトの出力を変更する方法だ。フィルターを使用して、文字列の小文字から大文字への変更など、静的テキストまたは動的テキストを再フォーマットしたり、加算や除算などの数学演算を実行したりできます。

フィルターは出力タグ`{{ }}` 内に置かなければならず、パイプ文字`|` で示される。

{% endraw %}

{% tabs local %}
{% tab インプット %}
{% raw %}
```liquid
{{"Big Sale" | upcase}}
```
{% endraw %}
{% endtab %}
{% tab 出力 %}
{% raw %}
```liquid
BIG SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

この例では、`Big Sale` が文字列で、`upcase` が適用されるフィルターである。

1つの出力に複数のフィルターを使うことができる。左から右に適用される。

{% tabs local %}
{% tab インプット %}
{% raw %}
```liquid
 {{ "Big Sale" | upcase | remove: "BIG" }}
```
{% endraw %}
{% endtab %}
{% tab 出力 %}
{% raw %}
```liquid
SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert important %}
BrazeはShopifyのすべてのリキッドフィルターをサポートしているわけではない。このページでは、Brazeがテストしたリキッドフィルターの概要を試みているが、完全なリストではない可能性がある。メッセージを送る前に必ずリキッドをテストすること。
<br><br>ここに掲載されていないフィルターについてご質問がある場合は、カスタマー・サクセス・マネージャーまでお問い合わせください。
{% endalert %}

## アレイ・フィルター

アレイ・フィルターは、アレイの出力を変更するために使われる。

| フィルター               | 定義                                                                                                         | サポート |
| :------------------- | :----------------------------------------------------------------------------------------------------------------- | :-------- |
| [参加する][1.1]          | 配列の要素を、パラメータとして渡された文字で結合する。結果は単一の文字列である。          | はい   |
| [第一][1.2]         | 配列の最初の要素を返す。カスタム属性配列では、これは最も古く追加された値である。                | はい   |
| [最後][1.3]          | 配列の最後の要素を返す。カスタム属性配列では、これは最近追加された値である。          | はい   |
| [コンパクト][1.4]       | 配列から`nil` の項目を削除する。                                                                             | はい   |
| [コンカット][1.5]        | 配列を別の配列と結合する。                                                                              | はい   |
| [インデックス][1.6]         | 配列の指定されたインデックスの位置にある項目を返す。配列の最初の項目は`[0]` で参照される。 | はい   |
| [地図][1.7]           | 配列要素の属性をパラメーターとして受け取り、各配列要素の値から配列を作成する。        | はい   |
| [リバース][1.8]       | 配列の項目の順序を逆にする。                                                                       | はい   |
| [サイズ][1.9]          | 文字列のサイズ（文字数）または配列のサイズ（要素数）を返す。                      | はい   |
| [ソート][1.10]         | 配列の要素を、その配列の要素の指定された属性でソートする。                                    | はい   |
| [sort_natural][1.11] | 大文字小文字を区別せずにアルファベット順に配列の項目をソートする。                                                | はい   |
| [ユニック][1.12]         | 配列中の要素の重複を削除する。                                                           | はい   |
| [どこだ][1.13]        | 特定のプロパティ値を持つ項目のみを含むように配列をフィルタリングする。                                             | はい   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## カラーフィルター

[カラーフィルターは][2.1]Brazeではサポートされていない。

## フォントフィルター

Brazeでは[フォントフィルターは][3.1]サポートされていない。

## 数学フィルター

数学フィルターでは、数学的な演算を行うことができる。覚えておいてほしいのは、1つの出力に複数のフィルターを使った場合、それらは左から右に適用されるということだ。

| フィルター  | 定義      | サポート |
| :------ |:----------------| :-------- |
| [腹筋][4.1]        | 絶対値関数は、数値の絶対値を返す。     | はい   |
| [at_most][4.2]    | 数値を最大値に制限する。   | はい   |
| [at_least][4.3]   | 数値を最小値に制限する。   | はい   |
| [天井][4.4]       | 出力を最も近い整数に丸める。  | はい   |
| [divided_by][4.5] | 出力を数値で割る。出力は最も近い整数に切り捨てられる。四捨五入を防ぐために、以下のヒントをチェックしよう。 | はい   |
| [フロア][4.6]      | 出力を最も近い整数に丸める。        | はい   |
| [マイナス][4.7]      | 出力から数値を引く。          | はい   |
| [プラス][4.8]       | 出力に数値を追加する。     | はい   |
| [ラウンド][4.9]      | 出力を最も近い整数または指定した小数点以下の桁数に丸める。  | はい   |
| [回][4.10]     | 出力に数値を掛ける。       | はい   |
| [モジュロ][4.11]    | 出力を数値で割り、余りを返す。   | はい   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert tip %}
Liquid で整数(整数)を整数で割るとき、答えが浮動小数点(小数を含む数値)の場合、Liquid は自動的に最も近い整数に切り捨てられる。しかし、整数を浮動小数点数で割ると、常に浮動小数点数になる。つまり、整数をfloat（1.0、2.0、3.0）に変換してfloatを返すことができる。
{% raw %}
<br><br>例えば、`{{15 | divided_by: 2}}` は`7` を出力し、`{{15 | divided_by: 2.0}}` は`7.5` を出力する。
{% endraw %}
{% endalert %}

### カスタム属性を使った数学演算

2つのカスタム属性の間で数学的演算を実行することはできないことを覚えておいてほしい。

{% raw %}

```liquid
{{custom_attribute.${current_rewards_balance} | plus: {{custom_attribute.${giftcard_balance}}}}}
```

リキッドの1行で複数のカスタム属性を参照することはできないので、この例はうまくいかないだろう。その代わりに、数学関数が実行される前に、これらの値の少なくとも1つに変数を代入する必要がある。つのカスタム属性を一緒に追加するには、2行のリキッドが必要になる：

1. カスタム属性を変数に割り当てる、
2. ひとつは追加を行う。

例えば、ギフトカードの残高とリワードの残高を足して、ユーザーの現在の残高を計算したいとしよう。まず、`assign` タグを使って、`current_rewards_balance` のカスタム属性を "balance "という言葉に置き換える。つまり、`balance` という変数ができたことになる。

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

次に、`plus` フィルタを使って、各ユーザーのギフトカード残高と、`{{balance}}` オブジェクトで示されるリワード残高を結合する。
{% endraw %}
{% tabs local %}
{% tab インプット %}
{% raw %}
```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}
{% endtab %}
{% tab 出力 %}
{% raw %}
```liquid
You have $35 to spend!
```
{% endraw %}
{% endtab %}
{% endtabs %}

## マネーフィルター

ユーザーの購入品や口座残高など、お金に関することを更新する場合は、マネーフィルターを使うべきだ。マネーフィルターは、小数が適切な位置にあり、更新の一部が失われないようにする（最後にある厄介な`0` ）。

| フィルター         | 定義          | サポート |
| :--------------- | :--------------- | :-------- |
| [マネー][5.1]      | 小数が適切な位置にあり、数字の末尾からゼロが抜けていないことを確認するために、数字を整形する。   | はい   |
| [money_with_currency][5.2]    | 数字を通貨記号で表示する。     | いいえ    |
| [money_without_currency][5.4]     | 通貨記号を除いた数値をフォーマットする。      | いいえ    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert important %}
`money` フィルタで数値を適切にフォーマットするには、数値のカンマをすべて削除し、`money` フィルタの前に`plus: 0` フィルタを追加する。例えば、次のリキッドを見てほしい：<br><br>
{% raw %}
```liquid
{% assign my_int = "350000.25" | plus: 0 %}
{{ my_int | money }}
```
{% endraw %}
{% endalert %}

### ShopifyマネーフィルターとBrazeマネーフィルターの比較

{% alert warning %}
Shopify`money` フィルタの動作は、Brazeでの使い方とは異なる。期待される動作の正確な描写については、以下の例を参照のこと。
{% endalert %}

{% raw %}
カスタム属性（`account_balance` など）を入力する場合は、常に`money` フィルタを使用して、小数点が適切な位置にあり、数字の末尾からゼロが抜けていないことを確認する必要がある：

```liquid
${{custom_attribute.${account_balance} | money}}
```
{% endraw %}

| マネーフィルター付き                       | マネーフィルターなし                    |
| :------------------------------------------ | :------------------------------------------ |
| ![マネーフィルター付き][1]                     | ![マネーフィルターなし][2]                  |
| ここで、`account_balance` は`17.8` で入力される。 | ここで、`account_balance` は`17.8` で入力される。 |
{: .reset-td-br-1 .reset-td-br-2}

Brazeの`money` フィルタは、Shopifyとは異なり、プリセット設定に従って自動的に小数点を適用するわけではない。例えば、`rewards_redeemed` に`145` という値が含まれている場合を考えてみよう：

{% tabs local %}
{% tab インプット %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | money }}
```
{% endraw %}
{% endtab %}
{% tab 出力 %}
{% raw %}
```liquid
$145.00
```
{% endraw %}
{% endtab %}
{% endtabs %}

Shopifyの[マネー][5.1]フィルターによると、これは`$1.45` の出力となるはずだが、Brazeでは`$145.00` の出力となる。回避策として、`divided_by` フィルタを使って数値を10進数に変換してから、マネーフィルタを適用することができる：

{% tabs local %}
{% tab インプット %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | divided_by: 100.00 | money }}
```
{% endraw %}
{% endtab %}
{% tab 出力 %}
{% raw %}
```liquid
$1.45
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 文字列フィルター

文字列フィルターは、文字列の出力や変数を操作するために使われる。文字列は英数字の組み合わせであり、ストレート引用符で囲む必要がある。

{% alert note %}
Liquidでは、ストレートクォートとカーリークォートは異なる。テキストエディタからBrazeにLiquidをコピー＆ペーストするときは注意しよう。リキッドを直接Brazeに書き込む場合、直線引用符は自動的に適用される。
{% endalert %}

| フィルター          | 説明     | サポート |
| :--------------- | ------------- | --------- |
| [アペンド][6.1]     | 文字列に文字を追加する。           | はい   |
| [キャメルケース][6.2]     | 文字列をキャメルケースに変換する。             | いいえ    |
| [資本を投下する][6.3]     | 文字列の最初の単語を大文字にし、残りの文字を小文字にする。         | はい   |
| [ダウンケース][6.4]      | 文字列を小文字に変換する。         | はい   |
| [エスケープ][6.5]    | 文字列をエスケープする。             | はい   |
| [ハンドル/ハンドルライズ][6.6]        | 文字列をハンドルにフォーマットする。        | いいえ    |
| [MD5][6.7]    | 文字列をMD5ハッシュに変換する。詳しくは\[エンコード・フィルター][3] ] を参照のこと。   | はい   |
| [シャ1][6.8]    | 文字列をSHA-1ハッシュに変換する。詳しくは\[エンコード・フィルター][3] ] を参照のこと。  | はい   |
| hmac_sha1_hex<br>(previously [hmac_sha_1][6.10]) | ハッシュメッセージ認証コード（HMAC）を使って文字列をSHA-1ハッシュに変換する。メッセージの秘密鍵をフィルターにパラメータとして渡す。詳しくは\[エンコード・フィルター][3] ] を参照のこと。 | はい   |
| [hmac_sha256][6.11]    | ハッシュメッセージ認証コード（HMAC）を使用して、文字列をSHA-256ハッシュに変換する。メッセージの秘密鍵をフィルターにパラメータとして渡す。       | はい   |
| hmac_sha512 | ハッシュメッセージ認証コード（HMAC）を使って文字列をSHA-512ハッシュに変換する。メッセージの秘密鍵をフィルターにパラメータとして渡す。 | はい  |
| [newline_to_br][6.12]     | 文字列の各改行の前に`<br>` 改行 HTML タグを挿入する。        | はい   |
| [複数化する][6.13]   | 数字の値に基づいて、英語の文字列の単数形または複数形を出力する。      | いいえ    |
| [プリペンド][6.14]     | 文字列の先頭に文字を追加する。      | はい   |
| [取り除く][6.15]      | 文字列から部分文字列をすべて削除する。       | はい   |
| [remove_first][6.16]    | 文字列から、最初に出現した部分文字列のみを削除する。      | はい   |
| [置き換える][6.17]        | 文字列のすべての出現回数を部分文字列で置き換える。   | はい   |
| [replace_first][6.18]        | 文字列の最初に現れる部分を部分文字列で置き換える。      | はい   |
| [スライス][6.19]       | スライスフィルターは、指定されたインデックスから始まる部分文字列を返す。       | はい   |
| [スプリット][6.20]  | スプリット・フィルターは部分文字列をパラメーターとして受け取る。部分文字列は、文字列を配列に分割する際の区切り文字として使われる。            | はい   |
| [ストリップ][6.21]   | 文字列の左右からタブ、スペース、改行（すべての空白）を取り除く。                                                                                                    | はい   |
| [ストリップ][6.22]     | 文字列の左側からタブ、スペース、改行（すべての空白）を取り除く。    | いいえ    |
| [ストリップ][6.23]             | 文字列の右側からタブ、スペース、改行（すべての空白）を取り除く。          | いいえ    |
| [strip_html][6.24]         | 文字列からすべてのHTMLタグを取り除く。        | はい   |
| [strip_newlines][6.25]  | 文字列から改行/改段を削除する。        | はい   |
| [切り捨てる][6.26]    | 文字列を、最初のパラメータとして渡された文字数まで切り詰める。省略記号（...）は切り捨てられた文字列に付加され、文字数に含まれる。    | はい   |
| [トランケートワード][6.27]   | 文字列を、最初のパラメータとして渡された語数まで切り詰める。切り捨てられた文字列には省略記号（...）が付加される。    | はい   |
| [アップケース][6.28]   | 文字列を大文字に変換する。      | はい   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 追加フィルター

以下の一般的なフィルターは、コンテンツのフォーマットや変換など、さまざまな目的を果たす。

| フィルター                | 説明                                                                                                                      | サポート |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| [日付][7.1]           | タイムスタンプを別の日付フォーマットに変換する。詳しくは[日付フィルタを](#date-filter)参照のこと。         | はい   |
| [デフォルト][7.2]        | 値が割り当てられていない変数にデフォルト値を設定する。文字列、配列、ハッシュで使用できる。      | はい   |
| [format_address][7.3] | アドレスをフォーマットし、そのロケールに従ってアドレスの要素を順番に表示する。        | いいえ    |
| [ハイライト][7.4]      | 送信された検索キーワードにマッチする場合、検索結果内の単語をHTMLの`<strong>` タグで囲む。 | いいえ    |
| `time_zone`             | 詳しくは[タイムゾーンフィルターを](#time-zone-filter)参照のこと。     | はい   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

エンコーディングやURLフィルターなど、サポートされているフィルターについては、[アドバンス・フィルターの]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/)ページで確認できる。

### 日付フィルター {#date-filter}

`date` フィルタは、タイムスタンプを別の日付フォーマットに変換するのに使える。タイムスタンプを再フォーマットするために、`date` フィルタにパラメータを渡すことができる。これらのパラメータの例については、以下を参照のこと。 [strfti.me](http://www.strfti.me/).

例えば、`date_attribute` の値がタイムスタンプ`2021-06-03 17:13:41 UTC` だとしよう。

{% tabs local %}
{% tab インプット %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%b %d'}}
```
{% endraw %}
{% endtab %}
{% tab 出力 %}
{% raw %}
```liquid
03 June
```
{% endraw %}
{% endtab %}
{% endtabs %}

`strftime` フォーマットオプションに加えて、Brazeは`%s` 日付フィルタを使ったタイムスタンプのUnix時間への変換もサポートしている。例えば、`date_attribute` をUnix時間で取得する：

{% tabs local %}
{% tab インプット %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%s' }}
```
{% endraw %}
{% endtab %}
{% tab 出力 %}
{% raw %}
```liquid
1433351621
```
{% endraw %}
{% endtab %}
{% endtabs %}

### タイムゾーンフィルター {#time-zone-filter}

{% raw %}
Shopifyのドキュメントに記載されているフィルターに加えて、Brazeは`time_zone` フィルターもサポートしている。

`time_zone` フィルタは、時刻、タイムゾーン、日付フォーマットを受け取り、そのタイムゾーンの時刻を指定された日付フォーマットで返す。例えば、`{{custom_attribute.$date_attribute}}}` の値が`2021-08-04 9:00:00 UTC` だとしよう：
{% endraw %}

{% tabs local %}
{% tab インプット %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | time_zone: 'America/Los_Angeles' | date: '%a %b %e %T' }}
```
{% endraw %}
{% endtab %}
{% tab 出力 %}
{% raw %}
```liquid
Wed August 4 2:00:00
```
{% endraw %}
{% endtab %}
{% endtabs %}

予約変数`now` を使って、現在の日付と時刻にアクセスして操作することもできる。

{% tabs local %}
{% tab インプット %}
{% raw %}
```liquid
{{ 'now' | date: '%Y-%m-%d %H:%M:%S' }}
```
{% endraw %}
{% endtab %}
{% tab 出力 %}
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
