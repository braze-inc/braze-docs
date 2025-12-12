---
nav_title: メッセージエクストラタグ
article_title: メッセージエクストラタグ
page_order: 1
description: "この記事では、メッセージエクストラLiquidタグの使用方法と構文の確認方法について説明します。"
alias: "/message_extras_tag/"
---

# メッセージエクストラ Liquid タグ

> `message_extras` Liquidタグを使用して、コネクテッドコンテンツ、カタログ、カスタム属性（言語、国など）、キャンバスエントリープロパティ、またはその他のデータソースからのダイナミックなデータで送信イベントに注釈を付ける。

Liquid タグ `message_extras` は、Currents や Snowflake Data Sharing の対応する送信イベントにキーと値のペアを追加します。 

ダイナミックなデータまたは追加のデータをCurrents またはSnowflake Data Sharing の送信イベントに送信するには、適切な Liquid タグをメッセージ本文に挿入します。 

以下は `message_extras` の標準 Liquid タグ形式の例です。

{% raw %}
```liquid
{% message_extras :key test :value 123 %}
```
{% endraw %}

メッセージ本文のキーと値のペアに必要に応じてこれらのタグを追加できます。ただし、すべてのキーと値の長さは1KBを超えてはならない。Currents および Snowflake Data Sharing で、送信イベント用に `message_extras` という新しいイベントフィールドが表示されます。これにより、1つのフィールドにJSONシリアライズされた文字列が生成されます。

## サポートされているチャンネル

`message_extras` タグは、アプリ内メッセージのインプレッションイベントとともに、送信イベントを含むすべてのメッセージタイプでサポートされています。インアプリメッセージで`message_extras`を使用するには、特定の[最低SDKバージョン](#iam-sdk)を満たす必要があります。

## `message_extras` タグの使い方

1. チャネルのメッセージ本文に、`message_extras` Liquidタグを入力する。または、**パーソナライゼーションを追加**モーダルを使用して、パーソナライゼーションタイプとして**メッセージエクストラ**を選択できます。 

![メッセージエクストラを含む追加パーソナライゼーション モーダルがパーソナライゼーションの種類として選択されました。]({% image_buster /assets/img_archive/message_extras1.png %}){: style="max-width:35%;"}

{: start="2"}

2. 各`message_extras`タグの[キーと値のペア]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/)を入力してください。 

![メッセージエクストラタグのキーと値のペアの例。[タイトル] フィールドには「あなたの新しいお気に入り」と表示されています。メッセージはメッセージエクストラのタグのキーと値のペアと、次の文を読み取ります。「当社は、あなたの新しいお気に入りになること間違いなしの新鮮で心躍る製品のサイドセレクションをお知らせできることを嬉しく思います」]({% image_buster /assets/img_archive/message_extras2.png %}){: style="max-width:70%;"}

{: start="3"}

3. キャンペーンまたはキャンバスが送信された後、Brazeは送信時にダイナミックなデータをCurrentsまたはSnowflake Data Sharingの送信イベントを介して`message_extras`フィールドに添付します。

## 構文の確認

前述したタグ標準に一致しないその他の入力はすべて、Currents または Snowflake に渡されないことがあります。次のいずれかが含まれていないことを確認してください: あなたの構文または書式設定

- 存在しない、空の、または誤って入力された区切り文字
- 重複キー（Brazeは最初に見つかったキーと値のペアをデフォルトで送信します）
- キーや値が定義される前の余分なテキスト
- 順序の一致しないキーと値 
  - {% raw %}例えば、```{% message_extras :value 123 :key test %}```{% endraw %}

## Currentsへのプロモーションコード発信

{% multi_lang_include shopify.md section='Liquid promotion codes with Currents' %}

## 考慮事項

- キーの値が 1 KB を超える場合、切り詰められます。 
- 空白は文字数にカウントされます。Brazeは前後の空白を省略します。
- 結果のJSONは文字列値のみを出力します。
- Liquid の変数をキーまたは値として含めることはできますが、`message_extras` 内で他の Liquid タグを使用することはできません。
  - 例えば、次の Liquid を使用できます： {% raw %}```{% assign value = '123' %} {% assign key = 'test' %} {% message_extras :key {{key}} :value {{value}} %}```{% endraw %}

## よくある質問

#### 送信イベントのmessage_extras フィールドを開封 s やクリックなどのエンゲージメントイベントに関連付けるにはどうすればよいですか? 

`dispatch_id` が生成され、送信イベントで提供されます。これは、特定のクリック、開封、または配信されたイベントに関連付けるための一意の識別子として使用できます。Currents または Snowflake でこのフィールドを使用およびクエリできます。[`dispatch_id` 行動]({{site.baseurl}}/help/help_articles/data/dispatch_id/) について詳しく学びます。

#### アプリ内メッセージ s でmessage_extras を使用できますか? {#iam-sdk}

はい、ユーザーのデバイスが次の最小SDKバージョンにある限り、`message_extras`をアプリ内メッセージで使用できます。

{% sdk_min_versions web:5.2.0 android:30.4.0 swift:8.4.0 %}

