---
nav_title: セレブラス
article_title: セレブラスの統合
description: "ブレイズとセレブラスの統合"
---

# セレブラス

> Celebrusは、WebおよびモバイルアプリのチャネルでBraze SDKとシームレスに統合し、チャネルのアクティビティデータをBrazeに取り込むことを容易にする。これには、特定期間におけるデジタル資産全体のビジター・トラフィックに関する包括的な洞察も含まれる。<br><br>さらに、セレブラスは顧客一人ひとりの豊富なプロフィールデータを取得し、Brazeと同期させることができる。これにより、包括的で正確かつ詳細なファーストパーティデータに基づき、効果的なBrazeアナリティクスとコミュニケーション戦略を策定することができる。この能力は、セレブラスの機械学習主導型シグナルによってさらに強化され、大掛かりなタグ付けをすることなく、手間をかけずにデータを取り込むことができる。堅牢なファーストパーティ・アイデンティティ・グラフがあれば、すべてのデータに即座にアクセスでき、すぐに利用できるようになる。 

## 前提条件

| 必要条件 | 説明 |
|---|---|
| セレブルスアカウント | このパートナーシップを利用するには、セレブラスのアカウントが必要である。 |
| データウェアハウス（オプション） | Brazeカスタム属性用のCelebrusコネクタを使用する場合は、Braze Cloud Data Ingestion (CDI)統合がサポートするデータウェアハウスを用意し、BrazeダッシュボードでCDIを設定する必要がある。 |
| Braze SDKの構成設定（オプション） | Braze SDK用のCelebrusコネクタを使用する場合は、SDKエンドポイントとSDK API Keyを渡す必要がある。 |
{: .reset-td-br-1 .reset-td-br-2}

## 実装
Celebrusの実装をインストールした後、Braze用のCelebrusコネクタを使用してCelebrusデータをBrazeに統合する。BrazeのCelebrus統合には、Braze SDKとBrazeカスタム属性の2つの要素がある。Brazeの使い方や必要なユースケースに応じて、どちらか一方を導入することも、両方を導入することもできる。

WebチャンネルにBraze SDKがまだ実装されていない場合は、Celebrusを使用してBraze SDKをデプロイすることができる。Celebrusは、WebページにBraze SDKを追加し、Celebrusアイデンティティグラフを使用してWeb訪問者にBrazeアイデンティティを設定する。顧客属性は、CDI（Cloud Data Ingestion）経由でBrazeと同期できる。これには、Braze CDIがサポートするデータウェアハウスと、BrazeでのCDIの設定が必要である。

### Braze SDK用Celebrusコネクタ

BrazeSDK用Celebrusコネクタは、Brazeのハイレベルなウェブおよびモバイルアプリのチャネルデータを提供する。Braze SDKでは、Celebrus IDグラフのCelebrus`System Identity` がBraze統合の識別子として使用される。その他の識別子は、Braze Custom Attributes Celebrusコネクタを介してカスタム属性を同期するためにサポートされている。

コネクターは、あなたのチャンネルにBraze SDKをデプロイして構成するので、Braze SDKデータストリームでいくつかの設定を構成し、これら3つの設定の値を提供する必要がある：

```
    response.addParameter("sdk_endpoint", "sdk.xxxxxx.braze.com");
    response.addParameter("api_key", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
    response.addParameter("app_id", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
```

{% alert important %}
Braze SDK用のCelebrusコネクタは、ユーザーを識別するためにBraze SDKを挿入して初期化し、CelebrusのIdentity Graphに識別子を追加する。このコネクタは、ユーザープロファイルにデータを記録したり、他のBraze SDKメソッドをトリガーしたりしない。<br><br>[Braze SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/)経由でデータを記録したり、Braze SDKがサポートする他の機能を利用したりするために、コードベース内で必要なメソッドを直接呼び出すことができる。
{% endalert%}

### Brazeカスタム属性用Celebrusコネクター

#### ステップ1:Celebrusで接続の詳細を設定する 

Brazeカスタム属性用のCelebrusコネクタは、Brazeが期待する方法で事前にフォーマットされたカスタム属性を中間データベースに送信する。Celebrusでは、使用しているデータベースの種類（SnowflakeやRedshiftなど）によって異なるデータベースの接続詳細を設定する。 

#### ステップ2:Brazeダッシュボードでクラウドデータ取り込みを設定する

この統合はBraze Cloud Data Ingestionを使用している。[データウェアハウスの統合の]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/)説明に従って、使用しているウェアハウスのタイプに応じて、[クラウドデータインジェスト]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/overview/)設定をセットアップして構成する。 

#### ステップ3:セレブラスからブレイズにデータを同期する

Celebrusは、電子メール、電話、`external_id`、ユーザーエイリアスなどの一意の識別子を取得し、個人に割り当て、CDIを介してBrazeに送信する。これにより、同じ個人のデータをBrazeに同期させることができる。

セレブラスは、定義された識別子を使用して、セレブラス・プロファイル・ビルダーで定義された顧客属性を送信するが、属性値が変更された場合にのみ送信する。属性名はCelebrusプロファイル・ビルダーで定義されたものになるので、Brazeの属性はCelebrusプロファイルの属性と同じになる。これらは、Brazeの命名規則に合わせて調整する必要があるかもしれない。例えば、Brazeの[標準的な属性の命名規則に]({{site.baseurl}}/api/objects_filters/user_attributes_object/)従う。  

{% alert important %}
今のところ、このリリースはイベントと購入には対応していない。<br><br> この統合では、属性を文字列値として送信するため、一部の属性はリストになる（シグナルなど）。今のところ、リストを配列に変換することはできない。ネストされた属性はない。
{% endalert%}

