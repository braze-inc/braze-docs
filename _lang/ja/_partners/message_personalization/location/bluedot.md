---
nav_title: Bluedot
article_title: Bluedot
alias: /partners/bluedot/
description: "この参考記事では、Brazeと位置情報プラットフォームであるBluedotのパートナーシップについて概説し、アプリに正確でわかりやすいジオフェンシングプラットフォームを提供する。"
page_type: partner
search_tag: Partner

---

# Bluedot

> [ブルードットは](https://bluedot.io/)、正確でわかりやすいジオフェンシングプラットフォームをアプリに提供するロケーションプラットフォームだ。BluedotのSDKを使用して、よりスマートなメッセージを発信し、モバイル注文のチェックインを自動化し、ワークフローを最適化し、摩擦のない体験を生み出す。 

BrazeとBluedotの統合により、Bluedotのジオフェンス位置情報サービスを利用してユーザーイベントを作成し、ジャーニーやキャンペーンの構築、顧客の行動や関心の分析に利用できる。ユーザーがデバイス上で発生させたイベント（入退場）は、すべての関連情報とともに即座にBrazeに送信される。 

## 前提条件

| 必要条件 | 説明 |
|---|---|
| ブルードット・アカウント | この統合を利用するには、ブルードット・アカウントが必要である。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

ブルードットが提供するカスタム・イベント・ロケーション情報は、以下のような一般的なユースケースを達成するためにキャンペーンで使用することができる：
- [`QSR`](https://bluedot.io/solutions/quick-service-restaurants/) (クイックサービスレストラン)
- [`Click and Collect`](https://bluedot.io/solutions/click-and-collect/)
- [`Drive-Thru`](https://bluedot.io/solutions/qsr-drive-thru/) 

## 統合

### ステップ1:ブルードット・プロジェクトを作成する
ブルードット・アカウントを設定し、[ブルードット・キャンバスのダッシュボードに](https://docs.bluedot.io/canvas/)ログインする。新規プロジェクトの作成方法については、[ブルードットのドキュメントを](https://docs.bluedot.io/canvas/creating-a-new-project/)参照されたい。

### ステップ2:SDKを統合する
[Bluedot-Braze統合](https://docs.bluedot.io/integrations/braze-integration/)ドキュメントに記載されている手順で、アプリにBluedot Point SDKとBraze SDKを統合する。

### ステップ3:ブルードットSDKを認証する
ステップ 1 で作成した`projectId` を使用して、Bluedot Point SDK を認証する。

### ステップ4:ブレイズでブルードット・イベントを使う

#### <b>メッセージのトリガー</b>

ブルードットSDKによって生成されたロケーション・イベントからアクションを起こすプッシュ・キャンペーンやキャンバスを設定することができる。この統合ルートは、ユーザーが会場や興味のある場所に入った直後のリアルタイムのメッセージングや、ユーザーがその場を離れた後の遅延したフォローアップ・コミュニケーションに最適である。

Brazeでアクションベースのキャンペーンを設定し、設定した場所に基づいてメッセージを送信する。トリガーには、以下のスクリーンショットに示すように、`bluedot_entry` または`bluedot_exit` のカスタムイベントを使用する：

![配信ステップにおけるアクションベースのキャンペーン。ここでは、ユーザーがカスタム`bluedot_entry` または`bluedot_exit` イベントを実行した場合にキャンペーンを送信する2つのスケジュールオプションがある。]({%image_buster /assets/img_archive/Campaign-Delivery-BD.png %}){: style="max-width:80%"}

#### ユーザーへのターゲット設定

ワークスペースのターゲットが**「すべてのユーザー」**であることを確認する。
![] （{%image_buster /assets/img_archive/Campaign-Target_users-BD.png %} ）「すべてのユーザー」を希望セグメントとして選択するよう、ターゲットユーザーのステップで促すアクションベースのキャンペーン。{: style="max-width:80%"}