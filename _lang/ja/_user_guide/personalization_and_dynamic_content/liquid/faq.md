---
nav_title: よくある質問
article_title: よくある質問
page_order: 11
description: "この記事では、Liquidに関するよくある質問への回答を提供します。"

---

# よくある質問

> このページでは、Liquidに関するよくある質問への回答をご覧いただけます。<br><br>Brazeは現在、Shopifyのリキッドを100％サポートしているわけではなく、ドキュメントで概説しようとした特定の部分のみをサポートしています。エラーやサポートされていないLiquidの使用のリスクを減らすために、送信前にすべてのメッセージをLiquidでテストすることを強くお勧めします。

### Braze でリキッドスニペットを使用するにはどうすればよいですか？

多くの場合、キャンペーンやキャンバスに移動し、メールメッセージ本文やセグメントなどのパーソナライゼーションモーダルにLiquidを挿入することで、Liquidスニペットを組み込むことができます。 

#### 詳細はどこで確認できますか?

Liquidの詳細については、Liquid [Brazeによるダイナミックパーソナライゼーションのガイド付きラーニングパスをご覧ください](https://learning.braze.com/path/dynamic-personalization-with-liquid)！また、[Liquidのユースケースライブラリを参照してインスピレーションを得たり]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/)、Liquidを使ったさまざまなパーソナライゼーションの例を確認したりすることもできます。

### パーソナライゼーションにLiquidとコネクテッドコンテンツを使用する場合の違いは何ですか？

ブレイズコネクテッドコンテンツはリキッドタグの一例です。パーソナライゼーションにも使用されますが、このデータは Braze 内に保存されているデータではなく、外部のエンドポイントから取得されます。メッセージをパーソナライズする方法の拡張について詳しくは、専用の「[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content)」セクションをご覧ください。

### Liquid テンプレートとは何ですか?

これは Braze でリキッドを使用する最も一般的な方法です。Liquid テンプレートでは、ユーザーのプロファイルからメッセージにデータを取り込みます。このデータは、ユーザーの名前からイベントトリガーメッセージからのカスタムイベントまでさまざまです。

[サポートされているLiquidタグの完全なリストについては、「サポートされているパーソナライゼーションタグ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)」を参照してください。

### Liquidで変数を割り当てるにはどうすればいいですか？

`assign`タグを使用して変数を作成して割り当てることができます。これにより、メッセージコンポーザーに変数が作成され、メッセージ全体で参照することもできます。

### Liquidを使用するとデータポイントが消費されますか？

いいえ。

### Liquidを使ってパーソナライズされたグリーティングを送るにはどうすればいいですか？

ユーザーのファーストネームを使用してパーソナライズされたグリーティングの場合は、{% raw %}`{{${first_name}}}`、`{{${last_name}}}`などの標準ユーザープロファイル属性を取得できます。

Liquid `{% if X %}` {% endraw %} ステートメントを使用して、曜日やカスタム属性など、あらゆる条件に基づいて条件付きレンダリングを行うこともできます。[条件文で使用できるサポート対象のLiquid演算子の詳細については]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/operators/)、「演算子」を参照してください。

### 顧客の位置情報に基づいてメッセージをパーソナライズする方法を教えてください。

{% raw %}
ユーザーの場所にはデフォルト属性があります:`{{${most_recent_location}}}`.

### What's the difference between {{campaign.${name}}} and {{campaign.${message\_name}}}?

`{{campaign.${name}}}``{{campaign.${message_name}}}`との両方が Liquid パーソナライゼーションタグに対応しています。どちらのタグもキャンペーン属性を参照しています。`{{campaign.${name}}}`キャンペーンの名前を表し、`{{campaign.${message_name}}}`はメッセージバリアントの名前です。
{% endraw %}

### ネストされたオブジェクトでLiquidを使用するにはどうすればよいですか?

Braze には、メッセージで使用できるセグメントの Liquid コードを生成する機能が組み込まれています。具体的には、オブジェクト内の複数の条件に一致するセグメントを作成できます。

詳しくは、「[複数条件セグメンテーション]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#multi-criteria-segmentation)」をご覧ください。

### イベント属性を使用して、イベントがトリガーされているメッセージをパーソナライズする方法を教えてください。

{% raw %}
API でトリガーされたイベントのプロパティには、:`api_triggered_property`というタグでアクセスできます`{{api_trigger_properties.${attribute_key}}}`。  
{% endraw %}

### アボートロジックとは何ですか? また、どのように使用できますか?

中止ロジックを使用すると、条件が満たされた場合にメッセージの送信を停止できます。これは、不完全なメッセージがユーザーに送信されるのを防ぐのに特に役立ちます。マーケティングキャンペーンの中止ロジックの例については、「[メッセージを中止する]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/)」で詳細をご覧ください。

### forループロジックとは何ですか? また、どのように使用できますか?

for [ループは反復タグとも呼ばれます](https://shopify.github.io/liquid/tags/iteration/)。Liquidスニペットでforループロジックを使用すると、条件が満たされるまでLiquidのブロックを循環させることができます。 

Brazeでは、これを配列のカスタム属性内の項目や、[カタログやConnected]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs) [Contentの呼び出し応答によって返された値とオブジェクトのリストを確認するために使用できます]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content)。具体的には、for ループロジックをメッセージの一部として使用して、商品の在庫があるかどうか、または商品に最低評価があるかどうかを確認できます。 

例えば、Get Going という名前の靴会社の全画像を含めて 100 行のカタログを検索したい場合、次の Liquid スニペットを使用できます。

{% raw %}

```liquid
{% for item in catalog %}
{% if {{item.brand}} = "GetGoing %}
{{item.image}}
{% endif %}
{% endfor %}
```

{% endraw %}

設定した条件が満たされると、メッセージを続行できます。このロジックを使用すると、さまざまな条件でLiquidブロックを繰り返す代わりに、時間を節約できるので便利です。
