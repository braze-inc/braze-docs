---
nav_title: Foursquare
article_title: Foursquare
alias: /partners/foursquare/
description: "このリファレンス記事では、Braze と Foursquare のパートナーシップについて説明します。Foursquare は、位置情報に基づいてリアルタイムでイベントをトリガーする機能を提供する位置情報データプラットフォームです。"
page_type: partner
search_tag: Partner

---

# Foursquare

{% multi_lang_include video.html id="G2ZoJqZGqrU" align="right" %}

> [Foursquare](https://foursquare.com/) は、Braze キャンペーンに位置情報データターゲティング機能を提供する位置情報データプラットフォームです。iOSとAndroidアプリでFoursquareのPilgrim SDKを使用して、位置情報に基づいたリアルタイムのイベントトリガーを提供し、Foursquareの強力なジオターゲティング機能を利用して、Brazeで関連性の高いパーソナライズされたメッセージを送信できる。

_この統合は Foursquare によって管理されます。_

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Foursquare アカウント | このパートナーシップを利用するには、Foursquareのアカウントが必要である。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| BrazeのワークスペースとApp ID | Braze ワークスペースと アプリ ID は[開発者コンソール]({{site.baseurl}}/api/api_key/)で確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 統合

2つのプラットフォームを統合するには、2つの SDK を統合し、一致するユーザーフィールドをマッピングする必要があります。Pilgrim SDK を統合すると、デバイスまたは Webhook で位置情報イベントを受け取ることができます。 

### ステップ1:ユーザーIDフィールドをマップする

2つの SDK 間でフィールドを正しくマッピングするには、Braze SDK の[`changeUser` メソッド]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#setting-user-ids)と Pilgrim SDK の [`PilgrimUserInfo`](https://developer.foursquare.com/docs/pilgrim-sdk/advanced-setup-guide#custom-user-data) の `setUserId` メソッドを使用して、両方のシステムで同じユーザー ID を設定します。

### ステップ2:Pilgrim コンソールを設定する
![Group ID、Android App ID、iOS App ID の入力を求める Pilgrim コンソールの画像。]({% image_buster /assets/img_archive/pilgrim-dev-console.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Braze開発者コンソールでワークスペースとApp IDを見つける。次に、Foursquare Pilgrim ConsoleにBraze REST API KeyとApp IDを入力する。

Pilgrim コンソールの設定が完了したら、Pilgrim SDK が位置情報イベントを記録して Braze に転送します。これにより、条件を満たした顧客をリターゲティングおよびセグメント化できます。詳細は[Foursquare開発者サイトを](https://developer.foursquare.com/)参照のこと。

{% alert important %}
Pilgrim SDK を使用するには、位置情報サービスを有効にする必要があります。
{% endalert %}

## メッセージのトリガー

統合が設定されたら、Pilgrim SDK により生成される位置情報イベントからアクションを実行するキャンペーンやキャンバスを設定できます。この統合ルートは、ユーザーが特定の会場に入った直後にリアルタイムメッセージを送信する場合、または退場後にフォローアップコミュニケーション (お礼やリマインダーなど) を行う場合に最適です。

設定した場所に基づいてメッセージを送信するキャンペーンを行う：
- **アクションベースの配信**で送信する Braze キャンペーンまたはキャンバスを作成する
- トリガーには、以下のスクリーンショットに示すように、`locationType` のイベントプロパティフィルターを含むカスタムイベント `arrival` を使用します。

![配送ステップにおけるアクションベースのキャンペーン。「カスタムイベントを実行」オプションとして「arrival」が選択されており、「locationType」が「home」と等しいという条件が設定されている。]({% image_buster /assets/img_archive/action-based-campaign.png %})

## リターゲティング

ユーザーを再ターゲットするには、Pilgrim SDKを使用して、Brazeユーザーのユーザープロファイルに`last_location` カスタム属性を設定する。そして、`matches regex` の比較を使って、現実世界で特定の場所に行ったユーザーを再ターゲティングすることができる。例えば、最近ピザ屋に行ったすべてのユーザーをセグメンテーションすることができる。

![ターゲットユーザーのステップで、"last_location "が "Pizza Place "と等しいことを示すアクションベースのキャンペーン。]({% image_buster /assets/img_archive/last-location-segment.png %})

また Braze で、特定のタイプの会場を訪問したユーザーを、特定の期間内の Foursquare の `primaryCategoryId` に基づいてセグメント化することもできます。このデータポイントをリターゲティングのユースケースに利用するには、オーディエンスのセグメンテーションプロセスでイベントプロパティとして `primaryCategoryId` をログに記録します。Foursquare API と Pilgrim SDK で使用されるユーザーとプロパティを確認するには、[Foursquare の開発者サイトを](https://developer.foursquare.com/)参照のこと。


