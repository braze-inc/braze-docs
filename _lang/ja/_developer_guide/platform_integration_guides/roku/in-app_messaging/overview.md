---
nav_title: 概要
article_title: Roku のアプリ内メッセージの概要
platform: Roku
channel: in-app messages
page_order: 0
page_type: reference
description: "この記事では、ベストプラクティスとユースケースを含む Roku アプリ内メッセージングの概要について説明します。"

---

# アプリ内メッセージの概要

> [アプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/)を使用すると、プッシュ通知でユーザーの日常を邪魔することなく、コンテンツをユーザーに届けることができます。カスタマイズされ調整されたアプリ内メッセージは、ユーザーエクスペリエンスを向上させ、オーディエンスがアプリから最大限の価値を得るのに役立ちます。様々なレイアウトやカスタマイズツールから選べるので、アプリ内メッセージはこれまで以上にユーザーを惹きつけます。

アプリ内メッセージの事例を見るには、\[ケーススタディ][6] ] をチェックしよう。

![ユーザーが作成可能なロクのアプリ内メッセージの3つのイメージ。例えば、「フルスクリーン・テイクオーバー」、「ホームページ・バナー」、「コーナー・ノーティファイア」などである。][3]

## アプリ内メッセージのタイプ

アプリ内メッセージプラットフォームとして \[**Roku デバイス**] を選択することで、Roku のアプリ内メッセージを作成します。

![][4]

## テクニカルドキュメント

アプリ内メッセージの表示、インプレッションとクリック分析のロギングについては、\[統合ガイド][5] ] を参照されたい。

![ホームページバナー」の例では、カスタムバナーを作るために必要なさまざまなコンポーネントを示している。表示されるコンポーネントには、メッセージ構成コンポーネント（本文、ボタンテキスト、画像、割り当てられたボタンの動作（ディープリンク）、キーと値のペア）、バックエンドの詳細（「シーズン1を視聴したユーザー」と表示されたオーディエンス、意図されたインタラクション（ボタンからアプリへのディープリンク、メッセージを閉じるとメッセージが解除される、10秒後に自動的に解除される）、トリガー（セッション開始）、キーと値のペア（template = homepage_banner）が含まれる。）][2]

## テストと QA

テスト送信機能は、Roku アプリ内メッセージではサポートされていません。メッセージをテストするには、ユーザー ID のみにフィルターされたキャンペーンを開始します。

[1]: {% image_buster /assets/img/roku/Roku-In-App-Messages-Flow.png %}
[2]: {% image_buster /assets/img/roku/Roku-In-App-Messages-Example.png %}
[3]: {% image_buster /assets/img/roku/Docs-Imagery.png %}
[4]: {% image_buster /assets/img/roku/1-Platform-Selector.png %}
 {{ site.baseurl }}/developer_guide/platform_integration_guides/roku/in-app_messaging/integration
[6]: https://www.braze.com/customers
