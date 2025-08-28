---
nav_title: loplat
article_title: loplat
description: "この参考記事では、Brazeとloplatの提携について説明しています。loplatはオフラインの位置情報ベースのマーケティングプラットフォームで、位置情報のコンテキストを追加することで、近接マーケティングキャンペーンを実行できるようにします。"
alias: /partners/loplat/
page_type: partner
search_tag: Partner

---

# loplat

> [Loplat](https://www.loplat.com/)は、主要なオフラインの位置情報ベースのプラットフォームです。loplat SDK を使用して店舗の来店者数を賢く増やし、店内購入を促進するマーケティングキャンペーンを実行します。キャンペーン終了後、フットフォール分析で店舗のパフォーマンスを測定できます。

_この統合は Loplat によって管理されます。_

## 統合について

Brazeとloplatの統合により、loplatの位置情報サービス（店舗POIおよびカスタムジオフェンス）を使用して、ジオ文脈に応じたマーケティングキャンペーンをトリガーし、オフラインセグメンテーションを使用してカスタムイベントを作成できます。ユーザーがloplat Xで設定したターゲットロケーションを訪れると、キャンペーンおよびロケーション情報が即座にBrazeに送信されます。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| loplat X アカウント | この統合を利用するには、loplat Xアカウントが必要です。<br><br>メール [support@loplat.com](mailto:support@loplat.com) にメールして loplat X アカウントをリクエストしてください。 |
| loplat SDK | loplat SDK はユーザーの店舗訪問を認識し、位置イベントを処理し、ユーザーが場所に滞在しているか移動しているかを区別します。ロプラットSDKを使用して、店舗のフットフォールを分析したり、ユーザーが店舗に入ったときにプッシュメッセージを送信したりすることができます。<br><br>SDKはAndroidとiOSでのみ利用可能です。 |
| Braze REST API キー | 以下の権限を持つBraze REST APIキー：<br>- `users.track`<br>- `campaigns.trigger.send`<br>- `campaigns.list`<br>- `canvas.trigger.send`<br>- `canvas.list`<br><br>これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

loplat によって提供されるカスタムイベントロケーション情報は、キャンペーンで次のようなユースケースを実現するために使用できます。

- [免税プロモーションアラート](https://www.loplat.com/loplat-x#usecase)
    - 空港の搭乗ゲート付近にいるユーザーに免税店の割引クーポンを送信します。
- 電気自動車（EV）充電ステーションの場所プッシュ
    - EV充電ステーションの周りにジオフェンスを設定し、ユーザーがステーションの近くにいるときに通知して充電を促します。

## 統合

### ステップ1:SDKを統合する

loplat SDKとBraze SDKをアプリに統合するには、[loplat-Braze統合](https://developers.loplat.com/braze/)ドキュメントに記載されている手順を使用します。

### ステップ2:Brazeとloplat Xのダッシュボードを同期し、キャンペーンを作成する

Braze ダッシュボードで新しい API キーを作成します。API キーをコピーして、loplat X ダッシュボードの**設定 > API 設定**に貼り付けます。詳細については、[loplat X ユーザーのガイド](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e?pvs=25)を参照してください。

#### API トリガー配信

1. **APIトリガー配信**で送信するBrazeキャンペーンまたはキャンバスを作成し、キャンペーンIDをコピーします。
2. すべてのステップを完了した後、Brazeでキャンペーンを開始します。
3. loplat Xに移動し、[loplat Xユーザーガイド](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e#2ed232c885014f19b1870b9fca4230fb)の指示に従ってキャンペーンを作成します。
4. **キャンペーンメッセージ設定**の下にBrazeキャンペーンIDを貼り付け、キャンペーンを開始します。

![]({% image_buster /assets/img/loplat/loplat_api_triggered_delivery.png %})

#### アクションベースの配信

統合により、ジオフェンス情報、地域、ブランド名、または店舗名を送信することで、ロケーション条件を適用できます。さらに、作成したカスタムイベントを使用してセグメントを追加したり、コンバージョンを割り当てたりできます。
1. [loplat X ユーザーのガイド](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e#f898aa55ef74440aba76dd9a0e3e7598)の指示に従って、loplat X キャンペーンを作成します。
2. **キャンペーンメッセージ設定**の下にカスタムイベントを追加し、キャンペーンを開始します。
3. Brazeのダッシュボードに移動して、**アクションベースの配信**で送信するキャンペーンまたはキャンバスを作成します。
4. loplat Xで作成したカスタムイベントを選択して、ロケーショントリガーアクションを設定します。

![]({% image_buster /assets/img/loplat/loplat_action_based_delivery.png %})


