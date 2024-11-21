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

アプリ内メッセージの[事例については、ケーススタディを](https://www.braze.com/customers)ご覧いただきたい。

![ユーザーが作成可能なロクのアプリ内メッセージの3つのイメージ。これらの例には、"fullscreen takeover"、"homepage banner"、および"corner notifier".]({% image_buster /assets/img/roku/Docs-Imagery.png %})が含まれます。

## アプリ内メッセージのタイプ

アプリ内メッセージプラットフォームとして [**Roku デバイス**] を選択することで、Roku のアプリ内メッセージを作成します。

![]({% image_buster /assets/img/roku/1-Platform-Selector.png %})

## テクニカルドキュメント

アプリ内メッセージとロギングインプレッションおよびクリックアナリティクスの表示方法については、弊社[統合ガイド]({{ site.baseurl }}/developer_guide/platform_integration_guides/roku/in-app_messaging/integration))をご覧ください。

![カスタムバナーの作成に必要な異なるコンポーネントを示す「ホームページバナー」の例。リストされているコンポーネントには、メッセージ構成コンポーネント(本文、ボタン、画像、割り当てられたボタンの動作(ディープリンク)、キーと値のペア)、バックエンドの詳細(オーディエンスが&クォートとしてリストされています。シーズン1&クォートを視聴したユーザー。意図したインタラクション(アプリへのディープリンク、メッセージの閉じ、10 秒後の自動解雇)、トリガー(セッション開始)、キーと値のペア(テンプレート= homepage_banner))が含まれます。]({% image_buster /assets/img/roku/Roku-In-App-Messages-Example.png %})

## テストと QA

テスト送信機能は、Roku アプリ内メッセージではサポートされていません。メッセージをテストするには、ユーザー ID のみにフィルターされたキャンペーンを開始します。

