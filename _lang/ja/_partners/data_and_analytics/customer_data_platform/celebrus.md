---
nav_title: Celebrus
article_title: Celebrus 統合
description: "Braze と Celebrus の統合。"
---

# Celebrus

> Celebrus は Web アプリチャネルとモバイルアプリチャネルで Braze SDK とシームレスに統合され、チャネルアクティビティデータを Braze に取り込みやすくなります。これには、特定期間におけるデジタル資産全体のビジター・トラフィックに関する包括的な洞察も含まれる。<br><br>さらに Celebrus は、個々の顧客の豊富なプロファイルデータを取得し、Braze と同期できます。これにより、包括的で正確かつ詳細なファーストパーティデータに基づき、効果的なBrazeアナリティクスとコミュニケーション戦略を策定することができる。この機能は Celebrus の機械学習を活用したシグナルによりさらに強化されます。これにより、大規模なタグ付け作業を必要とせずに、簡単にデータを取り込むことができます。堅牢なファーストパーティの ID グラフを導入することで、すべてのデータに即座にアクセスしてすぐに使用できるようになります。 

_この統合は Celebrus によって管理されます。_

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Celebrus アカウント | このパートナーシップを活用するには、Celebrus アカウントが必要です。 |
| データウェアハウス（オプション） | Celebrus コネクターを Braze のカスタム属性に使用する場合は、Braze クラウドデータ取り込み (CDI) 統合でサポートされるデータウェアハウスが必要です。また、Braze ダッシュボードで CDI を設定する必要があります。 |
| Braze SDKの構成設定（オプション） | Braze SDK に Celebrus コネクターを使用する場合は、SDK エンドポイントと SDK API キーを渡す必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 実装
Celebrusの実装をインストールした後、Braze用のCelebrusコネクタを使用してCelebrusデータをBrazeに統合する。Braze の Celebrus 統合には、Braze SDK とBraze のカスタム属性という2つの要素があります。Braze の使い方と必要なユースケースに応じて、いずれかまたは両方をデプロイできます。

Web チャネルに Braze SDK がまだ実装されていない場合は、Celebrus を使用して Braze SDK をデプロイできます。Celebrusは、WebページにBraze SDKを追加し、Celebrusアイデンティティグラフを使用してWeb訪問者にBrazeアイデンティティを設定する。顧客の属性は、クラウドデータ取り込み (CDI) を使用して Braze と同期できます。このためには、Braze CDI によってサポートされるデータウェアハウスと、Braze での CDI の設定が必要です。

### Braze SDK用Celebrusコネクタ

BrazeSDK用Celebrusコネクタは、Brazeのハイレベルなウェブおよびモバイルアプリのチャネルデータを提供する。Braze SDK では、Celebrus ID グラフの Celebrus `System Identity` が Braze 統合の識別子として使用されます。その他の識別子は、Braze Custom Attributes Celebrus コネクターを介してカスタム属性を同期するためにサポートされています。

このコネクターによりチャネルに Braze SDK がデプロイされ、設定されます。このため、Braze SDK データストリームでいくつかの設定を行い、次の3つの設定の値を指定する必要があります。

```
    response.addParameter("sdk_endpoint", "sdk.xxxxxx.braze.com");
    response.addParameter("api_key", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
    response.addParameter("app_id", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
```

{% alert important %}
Braze SDK 用の Celebrus コネクターは、ユーザーを識別し、識別子を Celebrus の ID グラフに追加するために Braze SDK を挿入および初期化します。このコネクタは、ユーザープロファイルにデータを記録したり、他のBraze SDKメソッドをトリガーしたりしない。<br><br>[Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)経由でデータを記録したり、Braze SDKがサポートする他の機能を利用したりするために、コードベース内で必要なメソッドを直接呼び出すことができる。
{% endalert%}

### Brazeカスタム属性用Celebrusコネクター

#### ステップ1:Celebrus で接続の詳細を設定する 

Braze カスタム属性用の Celebrus コネクターは、カスタム属性を中間データベースに送信します。このときカスタム属性は、Braze での受け取り形式で事前に形式設定されています。Celebrusでは、使用しているデータベースの種類（SnowflakeやRedshiftなど）によって異なるデータベースの接続詳細を設定する。 

#### ステップ2:Braze ダッシュボードでクラウドデータ取り込みを設定する

この統合では、Braze のクラウドデータ取り込みを使用します。「[データウェアハウスの統合]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/)」の手順に従って、使用するウェアハウスのタイプに応じて[クラウドデータ取り込みの設定]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/)を行います。 

#### ステップ3:Celebrus から Braze にデータを同期する

Celebrus は、メール、電話、`external_id` またはユーザーエイリアスなどの一意の識別子をキャプチャし、個別に割り当て、CDI を使用して Braze に送信します。これにより、同一の個人に関するデータを Braze と同期できます。

Celebrus は、属性値が変更された場合にのみ、定義されている識別子を使用して、Celebrus プロファイルビルダーで定義された顧客属性を送信します。なお、Celebrus プロファイルビルダーで定義された属性名は、デフォルトで Braze で使用されます。そのため、[Braze の命名規則に準拠するように]({{site.baseurl}}/api/objects_filters/user_attributes_object/)、これらの名前を更新してください。

{% alert important %}
現時点では、このリリースではイベントと購入はサポートされていません。<br><br> この統合では、属性を文字列値として送信するため、一部の属性はリストになる（シグナルなど）。今のところ、リストを配列に変換することはできない。ネストされた属性はない。
{% endalert%}

