---
nav_title: Foursquare
article_title:Foursquare
alias: /partners/foursquare/
description:"この参考記事では、位置情報プラットフォームであるFoursquareとBrzeの提携について概説しており、位置情報に基づくリアルタイムのイベントトリガーを提供している。"
page_type: partner
search_tag:Partner

---

# Foursquare

{% multi_lang_include video.html id="G2ZoJqZGqrU" align="right" %}

> [Foursquareは](https://foursquare.com/)、Brazeキャンペーンに位置情報ターゲティングを提供する位置情報プラットフォームである。Foursquare's Pilgrim SDK on iOS and Android apps to provide real-time event triggering based on location, allowing you to harness Foursquare'の強力なジオターゲティング機能を使い、Brazeを使って関連性の高いパーソナライズされたメッセージを送信しよう。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Foursquareアカウント | このパートナーシップを利用するには、Foursquareのアカウントが必要である。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これはダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| BrazeワークスペースとアプリID | BrazeのワークスペースとアプリIDは、[開発者コンソールで]({{site.baseurl}}/api/api_key/)確認できる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 統合

2つのプラットフォームを統合するには、2つのSDKを統合し、一致するユーザーフィールドをマッピングする必要がある。Pilgrim SDKを統合すると、デバイス上またはWebhookに位置情報を受信できるようになる。 

### ステップ1:ユーザーIDフィールドをマップする

2つのSDK間でフィールドを正しくマッピングするには、Braze SDKの[`changeUser` メソッドと]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#setting-user-ids)Pilgrim SDKの`setUserId` メソッドを使用して、両方のシステムで同じユーザーIDを設定する。 [`PilgrimUserInfo`](https://developer.foursquare.com/docs/pilgrim-sdk/advanced-setup-guide#custom-user-data)のメソッドを使用する。

### ステップ2:ピルグリムコンソールを設定する
![グループID、AndroidアプリID、iOSアプリIDを尋ねるピルグリムコンソールの画像写真。][2]{: style="float:right;max-width:40%;margin-left:15px;"}

Braze開発者コンソールでワークスペースとアプリIDを検索する。次に、Foursquare ConsoleにREST APIキーとアプリIDを入力する。

Pilgrim Consoleを設定すると、Pilgrim SDKがロケーションイベントを記録し、Brazeに転送するため、適格な顧客をリターゲティングし、セグメンテーションすることができる。詳細は[Foursquare開発者サイトを](https://developer.foursquare.com/)参照のこと。

{% alert important %}
ピルグリムSDKでは、位置情報サービスをイネーブルメントにする必要がある。
{% endalert %}

## メッセージのトリガー

インテグレーションが設定されると、ピルグリムSDKによって生成されたロケーションイベントからアクションを起こすキャンペーンやキャンバスを設定することができる。この統合ルートは、ユーザーが興味のある会場に入った直後のリアルタイムのメッセージングや、お礼やリマインダーのような、ユーザーが去った後の遅れたフォローアップ・コミュニケーションに最適である。

設定した場所に基づいてメッセージを送信するキャンペーンを行う：
- **アクションベース配信で**送信するBrazeキャンペーンまたはキャンバスを作成する。
- トリガーには、以下のスクリーンショットのように、`locationType` のイベントプロパティフィルターを持つ`arrival` のカスタムイベントを使用する。

![An action-based campaign in the delivery step showing "arrival" selected as the "perform custom event" option, where "locationType" equals "home".]({% image_buster /assets/img_archive/action-based-campaign.png %})

## リターゲティングする

ユーザーをリターゲティングするには、Pilgrim SDKを使用して、Brazeユーザーのユーザープロファイルに`last_location` カスタム属性を設定する。その後、`matches regex` 比較を使用して、現実世界で特定の場所に行ったユーザーをリターゲティングすることができる。例えば、最近ピザ屋に行ったすべてのユーザーをセグメンテーションすることができる。

![An action-based campaign in the target users step showing "last_location" equals "Pizza Place".]({% image_buster /assets/img_archive/last-location-segment.png %})

Brazeでは、特定の時間帯にFoursquareの`primaryCategoryId` 、特定のタイプの会場を訪れたユーザーをセグメントすることもできる。リターゲティングのユースケースにこのデータポイントを活用するには、オーディエンスのセグメンテーションプロセス中に、イベントプロパティとして`primaryCategoryId` 。Foursquare APIとPilgrim SDKが使用するユーザーとプロパティの識別子については、[Foursquare開発者](https://developer.foursquare.com/)サイトを参照のこと。

[1]: {% image_buster /assets/img_archive/dashboard_keys_locations.png %}
[2]: {% image_buster /assets/img_archive/pilgrim-dev-console.png %}