---
nav_title: Bluedot
article_title: Bluedot
alias: /partners/bluedot/
description: "この参考記事では、Brazeと位置情報プラットフォームであるBluedotのパートナーシップについて概説し、アプリに正確でわかりやすいジオフェンシングプラットフォームを提供する。"
page_type: partner
search_tag: Partner

---

# Bluedot

> [Bluedot](https://bluedot.io/) は、アプリのための正確でシンプルなジオフェンシングプラットフォームを提供するロケーションプラットフォームです。BluedotのSDKを使用して、よりスマートなメッセージを発信し、モバイル注文のチェックインを自動化し、ワークフローを最適化し、摩擦のない体験を生み出す。 

_この統合は Bluedot によって管理されます。_

## 統合について

BrazeとBluedotの統合により、Bluedotのジオフェンス位置情報サービスを利用してユーザーイベントを作成し、ジャーニーやキャンペーンの構築、顧客の行動や関心の分析に利用できる。ユーザーがデバイス上で発生させたイベント（入退場）は、すべての関連情報とともに即座にBrazeに送信される。 

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Bluedot アカウント | この統合を活用するには、Bluedot アカウントが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

Bluedot によって提供されるカスタムイベントロケーション情報は、キャンペーンで次のような一般的なユースケースを実現するために使用できます。
- [`QSR`](https://bluedot.io/solutions/quick-service-restaurants/) (クイックサービスレストラン)
- [`Click and Collect`](https://bluedot.io/solutions/click-and-collect/)
- [`Drive-Thru`](https://bluedot.io/solutions/qsr-drive-thru/) 

## 統合

### ステップ1:Bluedot プロジェクトを作成する
Bluedot アカウントを設定し、[Bluedot キャンバスダッシュボード](https://docs.bluedot.io/canvas/)にログインします。新しいプロジェクトの作成方法については、[Bluedot のドキュメント](https://docs.bluedot.io/canvas/creating-a-new-project/)を参照してください。

### ステップ2:SDKを統合する
[Bluedot と Braze の統合](https://docs.bluedot.io/integrations/braze-integration/)に関するドキュメントに記載されている手順を使用して、Bluedot Point SDK とBraze SDK をアプリに統合します。

### ステップ 3:Bluedot SDK を認証する
ステップ1で作成した `projectId` を使用して Bluedot Point SDK を認証します。

### ステップ4:Braze で Bluedot イベントを使用する

#### メッセージのトリガー

Bluedot SDK によって生成されたロケーションイベントから起動するプッシュキャンペーンまたはキャンバスを設定できます。この統合ルートは、ユーザーが会場や興味のある場所に入った直後のリアルタイムのメッセージングや、ユーザーがその場を離れた後の遅延したフォローアップ・コミュニケーションに最適である。

Brazeでアクションベースのキャンペーンを設定し、設定した場所に基づいてメッセージを送信する。トリガーには、以下のスクリーンショットに示すように、`bluedot_entry` または`bluedot_exit` のカスタムイベントを使用する：

![配信ステップでのアクションベースのキャンペーン。ここでは、ユーザーがカスタム`bluedot_entry` または`bluedot_exit` イベントを実行した場合にキャンペーンを送信する2つのスケジュールオプションがある。]({%image_buster /assets/img_archive/Campaign-Delivery-BD.png %}){: style="max-width:80%"}

#### ユーザーへのターゲット設定

ワークスペースのターゲットが**「すべてのユーザー」**であることを確認する。
![セグメントとして「すべてのユーザー」を選択するように促すターゲットユーザーステップを使用したアクションベースのキャンペーン。]({%image_buster /assets/img_archive/Campaign-Target_users-BD.png %}){: style="max-width:80%"}

