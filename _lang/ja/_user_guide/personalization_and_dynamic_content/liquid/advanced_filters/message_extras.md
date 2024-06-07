---
nav_title: メッセージエクストラタグ
article_title: メッセージエクストラタグ
page_order: 1
description: "この記事では、メッセージエクストラLiquidタグの使用方法と、構文を確認する方法について説明します。"
alias: "/message_extras_tag/"
---

# メッセージエクストラ Liquid タグ

> `message_extras` Liquidタグを使用すると、接続コンテンツ、カタログ、カスタム属性(言語、国など)、キャンバスエントリのプロパティ、またはその他のデータソースからの動的データで送信イベントに注釈を付けることができます。 

Liquidタグは `message_extras` 、CurrentsおよびSnowflakeデータ共有の対応する送信イベントにキーと値のペアを追加します。これは、送信イベントを持つすべてのメッセージの種類でサポートされています。

動的データまたは追加データを Currents または Snowflake Data Sharing 送信イベントに送り返すには、適切な Liquid タグをメッセージ本文に挿入します。以下は、 の `message_extras`標準の Liquid タグ形式の例です。 

{% raw %}
```
{% message_extras :key test :value 123 %}
```
{% endraw %}

これらのタグは、必要に応じてメッセージ本文のキーと値のペアに追加できます。ただし、すべてのキーと値の長さは 1 KB を超えてはなりません。Currents と Snowflake Data Sharing では、送信イベント用に呼び出され `message_extras` る新しいイベントフィールドが表示されます。これにより、1 つのフィールドに JSON シリアル化された文字列が生成されます。 

## 使用方法

1. チャネルのメッセージ本文に、Liquidタグを入力します `message_extras` 。または、「 **パーソナライゼーションを追加** 」モーダルを使用して、パーソナライゼーションタイプとして **「メッセージエクストラ** 」を選択することもできます。<br>![パーソナライゼーションタイプとして Message Extras が選択された Add Personalization モーダル。[1]{: style="max-width:70%;"}
2. 各`message_extras`タグの[キーと値のペア]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/)を入力します。<br>![message extras タグのキーと値のペアの例。タイトルフィールドには「新しいお気に入り」と表示されます。 このメッセージでは、message extras タグのキーと値のペアと、次の文が読み上げられます。「私たちは、あなたの新しい頼りになるお気に入りになること間違いなしの新鮮でエキサイティングな製品のサイドセレクションをお届けできることを嬉しく思います」][2]{: style="max-width:70%;"}
3. キャンペーンまたはキャンバスが送信されると、Brazeは送信時にCurrentsまたはSnowflakeデータ共有送信イベント `message_extras` を介して動的データをフィールドに添付します。

## 構文のチェック

前述のタグ標準に一致しないその他の入力は、Currents または Snowflake に渡されない可能性があります。構文または書式設定に次のものが含まれていないことを確認します。

- 存在しない区切り文字、空の区切り文字、または入力ミスのある区切り文字
- 重複キー(Brazeはデフォルトで、最初に検出されたキーと値のペアを送信します)
- キーまたは値が定義される前の追加のテキスト
- キーと値が順不同です 
  - {% raw %}例えば ```{% message_extras :value 123 :key test %}```{% endraw %}

## 考慮 事項

- Key-Value が 1 KB を超えると、切り捨てられます。 
- 空白は文字数にカウントされます。Brazeは先頭と末尾の空白を省略することに注意してください。
- 結果の JSON は、文字列値のみを出力します。
- Liquid変数はキーまたは値として含めることができますが、Liquidタグは直接サポートされていません。 
  - 例えば {% raw %}```{% assign value = '123' %} {% assign key = 'test' %} {% message_extras :key {{key}} :value {{value}} %}```{% endraw %}

## よくある質問

#### 送信イベントのmessage\_extrasフィールドをエンゲージメントイベント(開封数やクリック数など)に関連付けるにはどうすればよいですか? 

送信 `dispatch_id` イベントで生成および提供され、特定のクリックイベント、開封イベント、配信イベントに結び付けるための一意の識別子として使用できます。このフィールドは、CurrentsまたはSnowflakeで利用およびクエリできます。詳しくは、動作について[`dispatch_id`]({{site.baseurl}}/help/help_articles/data/dispatch_id/)の記事をご覧ください。

#### アプリ内メッセージでmessage\_extrasを使用できますか?

アプリ内メッセージチャネルでの使用`message_extras` は、現時点ではサポートされていません。

[1]: {% image_buster /assets/img_archive/message_extras1.png %}
[2]: {% image_buster /assets/img_archive/message_extras2.png %}
