---
nav_title: Foursquare
article_title: Foursquare
alias: /partners/foursquare/
description: "この参考記事では、Brazeと位置情報プラットフォームであるFoursquareのパートナーシップについて概説している。"
page_type: partner
search_tag: Partner

---

# Foursquare

{% multi_lang_include video.html id="G2ZoJqZGqrU" align="right" %}

> [Foursquareは](https://foursquare.com/)、Brazeのキャンペーンに位置情報のターゲティングを提供する位置情報プラットフォームである。iOSとAndroidアプリでFoursquareのPilgrim SDKを使用して、位置情報に基づいたリアルタイムのイベントトリガーを提供し、Foursquareの強力なジオターゲティング機能を利用して、Brazeで関連性の高いパーソナライズされたメッセージを送信できる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| フォースクエアアカウント | このパートナーシップを利用するには、Foursquareのアカウントが必要である。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| BrazeのワークスペースとApp ID | BrazeのワークスペースとApp IDは、[開発者コンソールで]({{site.baseurl}}/api/api_key/)確認できる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 統合

2つのプラットフォームを統合するには、2つのSDKを統合し、一致するユーザー・フィールドをマッピングする必要がある。ピルグリムSDKを統合すると、デバイス上またはウェブフックに位置情報イベントを受信できるようになる。 

### ステップ1:ユーザーIDフィールドをマップする

つのSDK間でフィールドを正しくマッピングするには、Braze SDKの[`changeUser` メソッドと]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#setting-user-ids)Pilgrim SDKの`setUserId` メソッドを使用して、両方のシステムで同じユーザーIDを設定する。 [`PilgrimUserInfo`](https://developer.foursquare.com/docs/pilgrim-sdk/advanced-setup-guide#custom-user-data)のメソッドを使用する。

### ステップ2:ピルグリムコンソールを設定する
![グループID、AndroidアプリID、iOSアプリIDを尋ねるピルグリムのコンソールの画像。][2]{: style="float:right;max-width:40%;margin-left:15px;"}

Braze開発者コンソールでワークスペースとApp IDを見つける。次に、Foursquare Pilgrim ConsoleにBraze REST API KeyとApp IDを入力する。

ピルグリムコンソールを設定すると、ピルグリムSDKがロケーションイベントを記録し、Brazeに転送する。詳細は[Foursquare開発者サイトを](https://developer.foursquare.com/)参照のこと。

{% alert important %}
ピルグリムSDKでは、位置情報サービスを有効にする必要がある。
{% endalert %}

## メッセージのトリガー

統合がセットアップされると、ピルグリムSDKによって生成されたロケーションイベントからアクションを起こすキャンペーンやキャンバスをセットアップすることができる。この統合ルートは、ユーザーが興味のある会場に入った直後のリアルタイムのメッセージングや、お礼状やリマインダーのような、ユーザーが去った後の遅れたフォローアップ・コミュニケーションに最適である。

設定した場所に基づいてメッセージを送信するキャンペーンを行う：
- **アクションベース配信で**送信するBrazeキャンペーンまたはキャンバスを作成する
- トリガーには、以下のスクリーンショットに示すように、`locationType` のイベント・プロパティ・フィルタを持つ`arrival` のカスタム・イベントを使用する。

![配送ステップにおけるアクションベースのキャンペーンで、「カスタムイベントを実行する」オプションとして「到着」が選択されていることを示す。]({% image_buster /assets/img_archive/action-based-campaign.png %})

## リターゲティング

ユーザーを再ターゲットするには、Pilgrim SDKを使用して、Brazeユーザーのユーザープロファイルに`last_location` カスタム属性を設定する。そして、`matches regex` の比較を使って、現実世界で特定の場所に行ったユーザーを再ターゲティングすることができる。例えば、最近ピザ屋に行ったすべてのユーザーをセグメンテーションすることができる。

![ターゲットユーザーのステップで、"last_location "が "Pizza Place "と等しいことを示すアクションベースのキャンペーン。]({% image_buster /assets/img_archive/last-location-segment.png %})

Brazeでは、特定の時間帯にFoursquareの`primaryCategoryId` 、特定のタイプの会場を訪れたユーザーをセグメントすることもできる。このデータポイントをリターゲティングのユースケースに活用するには、オーディエンスのセグメンテーションプロセス中に、イベントプロパティとして`primaryCategoryId` 。Foursquare API と Pilgrim SDK で使用されるユーザーとプロパティを確認するには、[Foursquare の開発者サイトを](https://developer.foursquare.com/)参照のこと。

[1]: {% image_buster /assets/img_archive/dashboard_keys_locations.png %}
[2]: {% image_buster /assets/img_archive/pilgrim-dev-console.png %}