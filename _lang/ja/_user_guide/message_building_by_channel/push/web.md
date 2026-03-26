---
nav_title: "Web プッシュ"
article_title: Web プッシュ通知
page_order: 8.5
page_type: reference
description: "このリファレンスページでは、Web プッシュ通知について簡単に説明し、それを作成するために必要なステップへのリンクを示します。"
platform: Web
channel:
  - push

---

# Web プッシュ

> Braze の Web プッシュ通知について学び、独自に作成するためのリソースを見つけましょう。

Web プッシュは、Web アプリケーションのユーザーとエンゲージするもう 1 つの優れた方法です。[サポートされているブラウザー](#supported-browsers)から Web サイトにアクセスする顧客は、Web ページが読み込まれているかどうかにかかわらず、Web アプリケーションから Web プッシュを受信することをオプトインできます。

## 概要

Web プッシュ通知は、迅速なコンバージョンを促進する緊急かつアクション可能な更新を配信します。Web プッシュを使用すると、次のことができます。

- 価格の下落など、重要なデータが変化したタイミングでメッセージをトリガーする
- 明確なコールトゥアクションボタンでユーザーを Web サイトに呼び戻す
- 製品や顧客の情報を使用してプッシュをパーソナライズし、メッセージの関連性を高める

Web プッシュは、スマートフォンでのアプリのプッシュ通知と同様に機能します。Web プッシュの作成方法の詳細については、[プッシュ通知の作成]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message)を参照してください。

![ノートパソコンとスマートフォンに同じプッシュメッセージが表示された Web プッシュの例。]({% image_buster /assets/img_archive/Macbook_Push.png %}){: style="border:none"}

## 潜在的なユースケース

以下に、一般的な Web プッシュメッセージのユースケースの例をいくつか示します。

| ユースケース | 説明 |
| --- | --- | 
| 無料トライアル | Web サイトの新規訪問者に、無料トライアルへの登録を促します。御社独自の特別な体験をする機会を提供してユーザーを引きつけることで、有料顧客になる可能性を高めることができます。 |
| アプリのダウンロード | Web ユーザーをモバイルアプリに誘導して、御社の製品からさらに高い価値を得られるようにします。パーソナライゼーションを活用して、ユーザーの現在のエンゲージメントパターンに基づきアプリのメリットを強調することを検討してください。 |
| 割引およびセール | 時間的制約のあるイベントやプロモーションに対する顧客の認知度を高めます。Web プッシュを含む複数のチャネルにわたってメッセージを配信し、自社ブランドのプロモーションに対する認知度を向上させます。 |
| カート放棄 | 取引を完了していないユーザーに自動リマインダーを送信して、購入手続きフローに呼び戻します。<br><br>Braze が実施した調査によると、Web プッシュは受信者を呼び戻して購入を完了させる効果において、メールよりも 53% 高く、モバイルプッシュよりも 23% 高いことがわかっています。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Web プッシュを使用するための前提条件

Braze を使用してプッシュメッセージの作成および送信を行うには、開発者と協力してプッシュを Web サイトに統合する必要があります。詳細なステップについては、[Web プッシュ統合ガイド]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)を参照してください。

### プッシュ許可

いずれのブランドでも、自社の Web サイトに Web プッシュ通知を統合して使用できます。通知は、Web ブラウザーを開いている限り、現在および以前の Web 訪問者の両方に届けることができますが、従来のモバイルアプリのプッシュと同様に、訪問者は[通知の受信をオプトイン]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-permission)する必要があります。

{% alert tip %}
ユーザーに Web プッシュへのオプトインを促すブラウザー内メッセージ（[プッシュプライマー]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)とも呼ばれます）の使用を検討してください。
{% endalert %}

## サポートされているブラウザー

以下のブラウザーは、Web プッシュ通知に対応しています。

{% multi_lang_include alerts/important_alerts.md alert='Web push private browsing' %}

- Chrome（および Chrome for Android モバイル）
- Safari（バージョン 16 以降）
- Firefox（および Firefox for Android モバイル）
- Opera
- Edge

プッシュプロトコル標準とブラウザーサポートの詳細については、ブラウザーに基づくリソースを確認してください。

- [Safari（デスクトップ）](https://developer.apple.com/notifications/safari-push-notifications/)
- [Safari（モバイル）]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=safari)
- [Mozilla Firefox](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)
- [Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/push)