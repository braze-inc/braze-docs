---
nav_title: Bluedot
article_title:Bluedot
alias: /partners/bluedot/
description:"この参考記事では、アプリに正確でわかりやすいジオフェンスプラットフォームを提供する、位置情報プラットフォームのBluedotとBrazeのパートナーシップについて概説している。"
page_type: partner
search_tag:Partner

---

# Bluedot

> [Bluuedotは](https://bluedot.io/)、アプリに正確でわかりやすいジオフェンスプラットフォームを提供するロケーションプラットフォームだ。BluedotのSDKを使用して、よりスマートなメッセージング、モバイル注文チェックインの自動化、ワークフローの最適化、摩擦のないエクスペリエンスを実現しよう。 

BrazeとBluedotの統合により、Bluedotのジオフェンス位置情報サービスを使用してユーザーイベントを作成し、ジャーニーやキャンペーンの構築、顧客行動や興味の分析に使用することができる。ユーザーのデバイスで発生したイベント（エントリ/エグジット）は、すべての関連情報とともに即座にBrazeに送信される。 

## 前提条件

| 必要条件 | 説明 |
|---|---|
|  | この統合を利用するには、Bluedotアカウントが必要である。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

Bluedotが提供するカスタムイベントのロケーション情報は、キャンペーンで使用することで、以下のような一般的なユースケースを実現することができる：
- [`QSR`](https://bluedot.io/solutions/quick-service-restaurants/) (クイックサービスレストラン)
- [`Click and Collect`](https://bluedot.io/solutions/click-and-collect/)
- [`Drive-Thru`](https://bluedot.io/solutions/qsr-drive-thru/) 

## 統合

### ステップ1:Bluuedotプロジェクトを作成する
ブルードット・アカウントを設定し、[ブルードット・キャンバスのダッシュボードに](https://docs.bluedot.io/canvas/)ログインする。新規プロジェクトの作成方法については、[Bluedotのドキュメントを](https://docs.bluedot.io/canvas/creating-a-new-project/)参照されたい。

### ステップ2:SDKを統合する
Bluedot[-Braze統合](https://docs.bluedot.io/integrations/braze-integration/)ドキュメントに記載されているステップを使用して、アプリでBluedot Point SDKとBraze SDKを統合する。

### ステップ3:Bluedot SDKを認証する。
ステップ1で作成した`projectId` を使用して、Bluedot Point SDK を認証する。

### ステップ 4:BrazeでBluedotのイベントを使う

#### <b>メッセージのトリガー</b>

Bluedot SDKによって生成されたロケーションイベントからアクションを起こすプッシュキャンペーンやキャンバスを設定できる。この統合ルートは、ユーザーが会場や興味のある場所に入った直後のリアルタイムのメッセージングや、ユーザーが会場を後にした後の遅延フォローアップ・コミュニケーションに最適である。

設定した場所に基づいてメッセージを送信するアクションベースのキャンペーンをBraze内で設定する。トリガーには、以下のスクリーンショットのように、`bluedot_entry` または`bluedot_exit` のカスタムイベントを使用する：

![An action-based campaign in the delivery step. Here, you have two scheduling options that will send the campaign if a user performs a custom `bluedot_entry` or `bluedot_exit` event.]({%image_buster /assets/img_archive/Campaign-Delivery-BD.png %}){: style="max-width:80%"}

#### ユーザーへのターゲット設定

ワークスペースを「**すべてのユーザー**」に設定する。
![An action-based campaign with the target users step encouraging you to select "All Users" as the desired segment.]({%image_buster /assets/img_archive/Campaign-Target_users-BD.png %}){: style="max-width:80%"}