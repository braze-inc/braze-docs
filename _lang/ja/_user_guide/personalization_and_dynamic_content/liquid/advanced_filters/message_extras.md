---
nav_title: メッセージエクストラタグ
article_title: メッセージエクストラタグ
page_order: 1
description: "この記事では、メッセージエクストラLiquidタグの使用方法と構文の確認方法について説明します。"
alias: "/message_extras_tag/"
---

# メッセージエクストラ Liquid タグ

> `message_extras` Liquid タグを使用すると、コネクテッドコンテンツ、カタログ、カスタム属性（言語、国など）、キャンバスエントリプロパティ、その他のデータソースからのダイナミックなデータで送信イベントに注釈を付けることができます。

`message_extras` Liquid タグはキーと値のペアを対応する送信イベントに追加し、Currents および Snowflake データ共有に送信します。 

動的または追加のデータをCurrentsまたはSnowflake Data Sharing送信イベントに送信するには、適切なLiquidタグをメッセージ本文に挿入します。 

以下は`message_extras`の標準Liquidタグ形式の例です:

{% raw %}
```liquid
{% message_extras :key test :value 123 %}
```
{% endraw %}

メッセージ本文のキーと値のペアに必要に応じてこれらのタグを追加できます。ただし、すべてのキーと値の長さは1KBを超えてはなりません。CurrentsとSnowflakeデータ共有では、送信イベント用の新しいイベントフィールド`message_extras`が表示されます。これにより、1つのフィールドにJSONシリアライズされた文字列が生成されます。

## サポートされているチャンネル

`message_extras`タグは、送信イベントを伴うすべてのメッセージタイプ、およびアプリ内メッセージインプレッションイベントに対応しています。インアプリメッセージで`message_extras`を使用するには、特定の[最低SDKバージョン](#iam-sdk)を満たす必要があります。

## 使い方

1. チャネルのメッセージ本文に`message_extras` Liquidタグを入力します。または、**パーソナライゼーションを追加**モーダルを使用して、パーソナライゼーションタイプとして**メッセージエクストラ**を選択できます。<br>![メッセージエクストラをパーソナライゼーションタイプとして選択したパーソナライゼーションの追加モーダル。][1]{: style="max-width:70%;"}
2. 各`message_extras`タグの[キーと値のペア]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/)を入力してください。<br>![メッセージエクストラタグのキーと値のペアの例。タイトルフィールドには「あなたの新しいお気に入り」と書かれています。メッセージはメッセージの追加情報タグのキーと値のペアを読み取り、次の文を読み取ります:私たちは、あなたの新しいお気に入りになること間違いなしの新鮮でエキサイティングな製品のサイドセレクションをお届けできることを楽しみにしています][2]{: style="max-width:70%;"}
3. キャンペーンまたはキャンバスが送信された後、Brazeは送信時にダイナミックなデータをCurrentsまたはSnowflake Data Sharingの送信イベントを介して`message_extras`フィールドに添付します。

## 構文の確認

それ以外の入力は、Currents または Snowflake に渡されない可能性があります。次のいずれかが含まれていないことを確認してください: あなたの構文または書式設定

- 存在しない、空の、または誤って入力された区切り文字
- 重複キー（Brazeは最初に見つかったキーと値のペアをデフォルトで送信します）
- キーや値が定義される前の余分なテキスト
- 順不同のキーと値 
  - {% raw %}例えば、```{% message_extras :value 123 :key test %}```{% endraw %}

## 考慮事項

- キー値が1KBを超える場合、切り捨てられます。 
- 空白は文字数にカウントされます。Brazeは前後の空白を省略します。
- 結果のJSONは文字列値のみを出力します。
- Liquid変数はキーまたは値として含めることができますが、Liquidタグは直接サポートされていません。 
  - 例えば、{% raw %}```{% assign value = '123' %} {% assign key = 'test' %} {% message_extras :key {{key}} :value {{value}} %}```{% endraw %}

## よくある質問

#### 送信イベントのmessage_extrasフィールドを、開封やクリックのようなエンゲージメントイベントにどのように関連付けることができますか？ 

`dispatch_id` が生成され、送信イベントに提供されます。これを使用して、特定のクリック、開封、または配信イベントに結び付けるための一意の識別子として使用できます。CurrentsまたはSnowflakeでこのフィールドを利用およびクエリできます。[`dispatch_id` 行動]({{site.baseurl}}/help/help_articles/data/dispatch_id/) について詳しく学びます。

#### メッセージエクストラをアプリ内メッセージで使用できますか？ {#iam-sdk}

はい、ユーザーのデバイスが次の最小SDKバージョンにある限り、`message_extras`をアプリ内メッセージで使用できます。

{% sdk_min_versions web:5.2.0 android:30.4.0 swift:8.4.0 %}

[1]: {% image_buster /assets/img_archive/message_extras1.png %}
[2]: {% image_buster /assets/img_archive/message_extras2.png %}
