---
nav_title: "Webプッシュ"
article_title: Webプッシュ通知
page_order: 8.5
page_type: reference
description: "このリファレンスページでは、Web プッシュ通知について簡単に説明し、それを作成するために必要なステップへのリンクを示します。"
platform: Web
channel:
  - push

---

# Web プッシュ

> Braze の Web プッシュ通知について学習し、独自に作成するためのリソースを理解します。

Web プッシュは、御社の Web アプリライケーションのユーザーとエンゲージするもう 1 つの優れた方法です。[サポートされているブラウザ](#supported-browsers) からWeb サイトにアクセスするお客様は、ウェブページが読み込むされているかどうかにかかわらず、ウェブアプリライケーションからWeb プッシュを受信することを選択できます。

## 概要

Web プッシュ通知は、迅速なコンバージョンを促進する緊急のアクション可能な更新を配信します。Web プッシュを使用すると、次のことができます。

- 価格が下がるなど、重要なデータが変化したときにメッセージを正しくトリガーします
- シンプルな行動喚起ボタンで Web サイトにユーザーを呼び戻します
- 製品と顧客の情報を使用してプッシュをパーソナライズし、メッセージの関連性を向上させます

Web プッシュは、スマートフォンでのアプリのプッシュ通知と同様に機能します。Web プッシュの作成の詳細については、[プッシュ通知の作成]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message)を参照してください。

![ノートパソコンと電話機に同じプッシュメッセージが表示されるWeb プッシュ例。]({% image_buster /assets/img_archive/Macbook_Push.png %}){: style="border:none"}

## 潜在ユースケースs

以下に、一般的な Web プッシュメッセージのユースケースの例をいくつか示します。

| ユースケース | 説明 |
| --- | --- | 
| 無料トライアル | Web サイトの新規訪問者に、無料トライアルに登録するように促します。御社独自の特別なものを体験する機会を提供して、ユーザーと繋がることで、そのようなユーザーが有料顧客になる可能性を上昇させることができます。 |
| アプリのダウンロード | Web ユーザーをモバイルアプリに誘導して、御社製品からユーザーがさらに高い価値を享受できるようにします。パーソナライゼーションを活用して、ユーザーの現在のエンゲージメントパターンに基づきアプリのメリットを強調することを検討します。 |
| 割引およびセール | 時間的制約のあるイベントやプロモーションに対する顧客の認知度を上昇させます。Web プッシュを含む複数チャネルにわたるメッセージングにより、自社ブランドのプロモーションに対する認知度を上昇させます。 |
| カート放棄 | 取引を完了していないユーザーに自動リマインダーを送信して、購入手続きフローに呼び戻します。<br><br>Brazeが行った調査によると、Web プッシュはメールよりも53%効果が高く、モバイルのプッシュよりも23%影響が大きいことがわかった。これは、受信者を買い戻して完成させるためのものである。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Web プッシュを使用するための前提条件

Braze を使用してプッシュメッセージの作成および送信を行うには、開発者と協力してプッシュを Web サイトに統合する必要があります。ステップの詳細については、[Webプッシュインテグレーションガイド]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)を参照してください。

### プッシュ許可

いずれのブランドでも、自社の Web サイトに Web プッシュ通知を統合して、使用できます。Web 訪問者が Web ブラウザーを開いている限り、通知は現在および以前のいずれの Web 訪問者に到達できますが、従来のモバイルアプリのプッシュと同様に、Web 訪問者は[通知受信にオプトイン]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-permission)する必要があります。

{% alert tip %}
ユーザーに Web プッシュへのオプトインを促すブラウザー内メッセージ ([プッシュプライマー]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)とも呼ばれる) を使用することを検討します。
{% endalert %}

## サポートされているブラウザー

次のブラウザは、Web プッシュ通知に対応しています。ただし、プライベートブラウズウィンドウは現在Web プッシュに対応していません。

- Chrome (および Chrome for Android モバイル)
- Safari
- Firefox(およびAndroid携帯用Firefox)
- Opera
- Edge

プッシュプロトコル標準とブラウザーのサポートの詳細については、ブラウザーに基づくリソースを確認してください。

- [Safari(デスクトップ)](https://developer.apple.com/notifications/safari-push-notifications/)
- [Safari (モバイル)]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=safari)
- [Mozilla Firefox](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)
- [Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/push)


