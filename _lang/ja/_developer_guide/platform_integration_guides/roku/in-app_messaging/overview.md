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

[ケーススタディ][6] でアプリ内メッセージの例をチェックしましょう。

![ユーザーが構築できる Roku アプリ内メッセージの3つの画像。これらの例には「全画面表示」、「ホームページバナー」、「コーナー通知」が含まれます。][3]

## アプリ内メッセージの種類

アプリ内メッセージプラットフォームとして [**Roku デバイス**] を選択することで、Roku のアプリ内メッセージを作成します。

![][4]

## テクニカルドキュメント

アプリ内メッセージの表示と、インプレッションおよびクリック分析のロギングに関する説明については、[統合ガイド][5] を参照してください。

![カスタムバナーの作成に必要な異なるコンポーネントを示す「ホームページバナー」の例。リストに含まれるコンポーネントには、メッセージ構成コンポーネント (本文、ボタンテキスト、画像、割り当てられたボタン動作 (ディープリンク)、キーと値のペアを表示) と、バックエンドの詳細 (「シーズン1を視聴したユーザー」のリストに含まれるオーディエンス、意図するインタラクション (アプリへのディープリンク、メッセージを閉じることによるメッセージの無視、10秒後の自動無視)、トリガー (セッション開始)、およびキーと値のペア (テンプレート= homepage\_banner)) が含まれます。][2]

## テストと QA

テスト送信機能は、Roku アプリ内メッセージではサポートされていません。メッセージをテストするには、ユーザー ID のみにフィルターされたキャンペーンを開始します。

[1]: {% image_buster /assets/img/roku/Roku-In-App-Messages-Flow.png %}
[2]: {% image_buster /assets/img/roku/Roku-In-App-Messages-Example.png %}
[3]: {% image_buster /assets/img/roku/Docs-Imagery.png %}
[4]: {% image_buster /assets/img/roku/1-Platform-Selector.png %}
[5]: {{ site.baseurl }}/developer_guide/platform_integration_guides/roku/in-app_messaging/integration
[6]: https://www.braze.com/customers
