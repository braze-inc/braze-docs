---
nav_title: FAQ
article_title: よくある質問
page_order: 12
description: "この記事では、Liquid に関してよくある質問にお答えします。"

---

# よくある質問

> このページでは、Liquidに関するよくある質問への回答を見つけることができます。<br><br>Brazeは現在、ShopifyのLiquidの100%をサポートしているわけではなく、ドキュメントで概説しようとした特定の部分のみをサポートしています。すべてのメッセージを送信する前にLiquidを使用してテストすることを強くお勧めします。これにより、エラーのリスクやサポートされていないLiquidの使用を減らすことができます。

### Braze で Liquid スニペットを使用するにはどうすればよいですか?

多くの場合、キャンペーンやキャンバスに移動し、パーソナライゼーションモーダルのメールメッセージ本文やセグメントなどの領域にLiquidを挿入することで、Liquidスニペットを組み込むことができます。 

#### もっと詳しく知るにはどこで学べますか？

Liquid の詳細については、Braze ラーニングのガイド付きパス「[Liquid を使用したダイナミックなパーソナライゼーション](https://learning.braze.com/path/dynamic-personalization-with-liquid)」を参照してください。また、インスピレーションやLiquidを使用したさまざまなパーソナライゼーションの例については、[Liquidユースケースライブラリー]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/)を参照することもできます。

### Liquid とコネクテッドコンテンツをパーソナライゼーションに使用する場合の違いは何ですか?

Braze コネクテッドコンテンツは Liquid タグの一例です。これはパーソナライゼーションにも使用されますが、このデータは Braze 内の保存データではなく、外部のエンドポイントから取得されます。専用の[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content)セクションをご覧になり、メッセージのパーソナライズ方法を拡張する方法について詳しく学んでください。

### Liquid テンプレートとは何ですか?

これは、Braze で Liquid を使用する最も一般的な方法です。Liquid テンプレートでは、ユーザーのプロファイルからデータをメッセージに引き出します。このデータは、ユーザーの名からイベントトリガーメッセージのカスタムイベントまで多岐にわたっています。

[サポートされているパーソナライゼーションタグ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)の完全なリストについては、サポートされているLiquidタグを参照してください。

### Liquidで変数をどのように割り当てますか？

`assign`タグを使用して変数を作成および割り当てることができます。これにより、メッセージ作成画面で変数が作成され、メッセージ全体で参照できるようになります。

### リキッドログデータポイントs を使用していますか?

いいえ。

### Liquid を使用してパーソナライズされた挨拶を送信するにはどうすればよいですか?

パーソナライズされた挨拶にユーザーの名を使用する場合、標準的なユーザープロファイル属性を {% raw %} `{{${first_name}}}`、`{{${last_name}}}`のように取得することができます。

Liquidを使用して、曜日やカスタム属性などに基づいて条件付きレンダリングを行う`{% if X %}` {% endraw %}ステートメントを使用することもできます。サポートされているLiquid演算子の条件文で使用できる演算子の詳細については、[演算子]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/operators/)をチェックしてください。

### 顧客の所在地に基づいてメッセージをパーソナライズするにはどうすればよいですか？

{% raw %}
ユーザーの位置情報にはデフォルトの属性があります: `{{${most_recent_location}}}`。

### {{campaign.${name}}}と{{campaign.${message_name}}}の違いは何ですか？

両方`{{campaign.${name}}}`と`{{campaign.${message_name}}}`はサポートされているLiquidパーソナライゼーションタグです。両方のタグはキャンペーン属性を参照しています。`{{campaign.${name}}}`はキャンペーンの名前を示し、`{{campaign.${message_name}}}`はメッセージバリアントの名前を示します。
{% endraw %}

### Liquidをネストされたオブジェクトでどのように使用しますか？

Brazeには、メッセージで使用できるセグメントのLiquidコードを生成する組み込み機能があります。具体的には、オブジェクト内の複数の基準に一致するSegmentを作成できます。

詳細については、[マルチ基準セグメンテーション]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#multi-criteria-segmentation)をご覧ください。

### イベント属性を使用して、イベントがトリガーしているメッセージをどのようにパーソナライズしますか？

{% raw %}
API トリガーイベントのプロパティにアクセスするには、`api_triggered_property` タグ: `{{api_trigger_properties.${attribute_key}}}` を使用できます。  
{% endraw %}

### 中止ロジックとは何ですか、それをどのように使用できますか？

中止ロジックにより、条件が満たされている場合、メッセージの送信を停止できます。これは、未完成のメッセージがユーザーに送信されるのを防ぐのに特に役立ちます。マーケティングキャンペーンにおける中止ロジックの例については、[メッセージの中止]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/)をお読みください。

### ループロジックとは何ですか、それはどのように使用できますか?

For loops are also known as [反復タグ](https://shopify.github.io/liquid/tags/iteration/).Liquid スニペットで for ループロジックを使用すると、条件が満たされるまで Liquid のブロックを反復実行できます。 

Braze では、これは配列のカスタム属性、または[カタログ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs)、[セレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/)、または[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content)の呼び出し応答によって返される値やオブジェクトのリストをチェックするために使用できます。具体的には、メッセージングの一環としてforループロジックを使用して、製品が在庫にあるかどうか、または製品が最低評価を持っているかどうかを確認できます。 

たとえば、"Games"という名前のカタログがあり、"cheap_games". という名前の選択肢があるとします。"cheap_games", でゲームのタイトルをプルするには、次のリキッドスニペットを使用できます。

{% raw %}
```liquid
{% catalog_selection_items Games cheap_games %}
{% for item in items %}
 Get this game: {{ item.title }}
{% endfor %}
```
{% endraw %}

設定された条件が満たされると、メッセージを進めることができます。さまざまな条件で Liquid ブロックを繰り返す代わりに、このロジックを使用すると、時間を節約できて便利です。
