---
nav_title: Celebrus
article_title:セレブラスの統合
description:"BrazeとCelebrusの統合"
---

# セレブラス

> Celebrusは、WebおよびモバイルアプリのチャネルでBraze SDKとシームレスに統合し、チャネルのアクティビティデータとBrazeの人口を促進する。これには、特定期間におけるデジタル資産全体のビジター・トラフィックに関する包括的なインサイトが含まれる。<br><br>さらに、セレブラスは顧客一人ひとりの豊富なプロファイルデータを取得し、Brazeと同期させることができる。これにより、包括的で正確かつ詳細なファーストパーティデータに基づいた、効果的なBraze分析とコミュニケーション戦略を策定することができる。この機能は、セレブラスの機械学習型のシグナルによってさらに強化され、大掛かりなタグ付けを必要とせず、手間をかけずにデータを取り込むことができる。堅牢なファーストパーティ・アイデンティティ・グラフがあれば、すべてのデータに即座にアクセスでき、すぐに利用できるようになる。 

## 前提条件

| 必要条件 | 説明 |
|---|---|
| セレブルスアカウント | このパートナーシップを利用するには、セレブラスのアカウントが必要である。 |
| データウェアハウス（オプション） | Brazeカスタム属性用のCelebrusコネクタを使用する場合は、Braze Cloud Data Ingestion（CDI）統合がサポートするデータウェアハウスを用意し、BrazeダッシュボードでCDIを設定する必要がある。 |
| Braze SDKの設定（オプション） | Braze SDK用のCelebrusコネクタを使用する場合は、SDKエンドポイントとSDK APIキーを渡す必要がある。 |
{: .reset-td-br-1 .reset-td-br-2}

## 実装
Celebrusの実装をインストールした後、Braze用のCelebrusコネクタを使用してCelebrusデータをBrazeに統合する。BrazeのCelebrus統合には、Braze SDKとBrazeカスタム属性の2つの要素がある。Brazeの使い方や必要なユースケースに応じて、どちらか一方を導入することも、両方を導入することもできる。

まだWebチャネルにBraze SDKを実装していない場合は、Celebrusを使用してBraze SDKをデプロイすることができる。Celebrusは、WebページにBraze SDKを追加し、Celebrus IDグラフを使用してWeb訪問者にBraze IDを設定する。顧客属性は、CDI（Cloud Data Ingestion）を介してBrazeと同期することができる。これには、Braze CDIがサポートするデータウェアハウスと、BrazeでのCDIの設定が必要である。

### Braze SDK用Celebrusコネクタ

Braze SDK用Celebrusコネクターは、BrazeのハイレベルWebおよびモバイルアプリチャネルデータを提供する。Braze SDKでは、Celebrus IDグラフのCelebrus`System Identity` がBraze統合の識別子として使用される。Braze Custom Attributes Celebrusコネクタを介したカスタム属性の同期には、他の識別子もサポートされている。

コネクターはチャネルにBraze SDKをデプロイして設定するので、Braze SDKデータストリームでいくつかの設定を行い、これら3つの設定の値を提供する必要がある：

```
    response.addParameter("sdk_endpoint", "sdk.xxxxxx.braze.com");
    response.addParameter("api_key", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
    response.addParameter("app_id", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
```

{% alert important %}
Braze SDK用Celebrusコネクタは、ユーザーを識別するためにBraze SDKを挿入して初期化し、CelebrusのIdentity Graphに識別子を追加する。このコネクターは、ユーザープロファイルにデータを記録したり、他のBraze SDKメソッドをトリガーしたりしない。<br><br>コードベース内で必要なメソッドを直接呼び出して、[SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/)経由でデータを記録したり、SDKがサポートする他の機能を利用したりすることができる。
{% endalert%}

### Brazeカスタム属性用Celebrusコネクター

#### ステップ1:Celebrusで接続の詳細を設定する 

Brazeカスタム属性用のCelebrusコネクターは、Brazeが期待する方法で事前にフォーマットされたカスタム属性を中間データベースに送信する。Celebrusでは、使用しているデータベースの種類（SnowflakeやRedshiftなど）によって異なるデータベースの接続詳細を設定する。 

#### ステップ2:BrazeダッシュボードでCloud Data Ingestionを設定する。

この統合はBraze Cloud Data Ingestionを使用している。[データウェアハウスの統合の]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/)説明に従って、使用しているウェアハウスの種類に応じて[クラウドデータインジェストレーションの]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/overview/)設定を行う。 

#### ステップ3:CelebrusからBrazeにデータを同期する

Celebrusは、メール、電話、`external_id`、ユーザーエイリアスなどの一意の識別子を取得し、個人に割り当て、CDIを介してBrazeに送信する。これにより、同じ個人のBrazeにデータを同期させることができる。

セレブラスは、定義された識別子を使用して、セレブラス・プロファイル・ビルダーで定義された顧客属性を送信するが、属性値が変更された場合にのみ送信する。属性名はCelebrusプロファイルビルダーで定義されたものになるので、Brazeの属性はCelebrusプロファイルの属性と同じになる。これらは、Brazeの命名規則に合わせて調整する必要があるかもしれない。例えば、Brazeの[標準属性項目命名規則に]({{site.baseurl}}/api/objects_filters/user_attributes_object/)準拠する。  

{% alert important %}
今のところ、このリリースはイベントと購入には対応していない。<br><br> この統合では、属性を文字列値として送信するため、一部の属性はリストになる（シグナルなど）。今のところ、リストを配列に変換することはできない。ネストされた属性はない。
{% endalert%}

