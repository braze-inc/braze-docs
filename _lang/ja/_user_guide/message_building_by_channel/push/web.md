---
nav_title: "Webプッシュ"
article_title: Webプッシュ通知
page_order: 8.5
page_type: reference
description: "このリファレンスページでは、Web プッシュ通知 s について簡単に説明し、s を作成するために必要なステップにリンクします。"
platform: Web
channel:
  - push

---

# Web プッシュ

> Braze で Web プッシュ通知について学習し、独自に作成するためのリソースを見つけます。

Webプッシュは、あなたのWeb アプリライケーションのユーザーと関わるもう1つの素晴らしい方法です。[サポートされているブラウザ](#supported-browsers) からWeb サイトにアクセスするお客様は、ウェブページが読み込むされているかどうかにかかわらず、ウェブアプリライケーションからWeb プッシュを受信することを選択できます。

## 概要

Web プッシュ通知 s は、迅速なコンバージョン s を駆動する緊急のアクション対応更新 s を提供します。Web プッシュを使用すると、次のことができます。

- 価格が下がるなど、重要なデータが変化したときにメッセージを正しくトリガーします
- 簡単なアクション通話ボタンでWeb サイトに人員を戻す
- 商品と顧客をカスタマイズして、あなたの情報を適切なものにしましょう

Webプッシュは、スマートフォンでアプリ プッシュ通知が操作するのと同じように機能します。Web プッシュの作成の詳細については、[プッシュ通知の作成][11]を参照してください。

![Webプッシュサンプルは、ラップトップと電話機に表示されるのと同じプッシュメッセージを使用します。][12]{: style="border:none"}

## 潜在ユースケースs

一般的なWeb プッシュ電文ユースケースsの事例をいくつか紹介する。

| ユースケース | 説明 |
| --- | --- | 
| 無料トライアル | Web サイトの新規訪問者に無料トライアルに登録するよう促す。ユーザー s を、あなたが特殊なものを体験できるチャンスに引っ掛けることで、有料顧客になる可能性を高めることができます。 |
| アプリダウン読み込む | ウェブユーザーを携帯アプリに描き、商品からさらに価値を引き出すのに役立ててください。パーソナライゼーションを活用して、現行のエンゲージメント形態に基づいてアプリの便益を強調することを検討する。 |
| 値引き・販売 | 時間に敏感な行事やプロモーションに対する顧客の意識を高める。Web プッシュを含む複数のチャネルにまたがって、自社のプロモーションに対する認知度を高めるための連絡。 |
| カート放棄 | トランスアクションを終了していないユーザーに自動リマインダーを送信して、チェックアウトフローに戻します。<br><br>Brazeが行った調査によると、Web プッシュはメールよりも53%効果が高く、モバイルのプッシュよりも23%影響が大きいことがわかった。これは、受信者を買い戻して完成させるためのものである。 |
{: .reset-td-br-1 .reset-td-br-2}

## Web プッシュを使用するための前提条件

Braze を使用してプッシュメッセージを作成および送信するには、開発者 s を使用してプッシュをWeb サイトに統合する必要があります。ステップの詳細については、[Webプッシュインテグレーションガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/)を参照してください。

### プッシュ許可

どのブランドでも、自社のWeb サイト上でウェブプッシュ通知sを統合し、使用することができる。通知s は、Web ブラウザー開封を持っている限り、現行および以前の両方のWeb ビジターに到達できますが、ビジターは通知s を受信するために、従来のモバイルアプリプッシュと同様に[opt in する必要があります。

{% alert tip %}
[プッシュプライマー]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)としても知られている、Web プッシュを選択するためにユーザーsをプライミングするために、ブラウザ内メッセージを使用することを検討します。
{% endalert %}

## サポートされているブラウザー

次のブラウザは、Web プッシュ通知に対応しています。ただし、プライベートブラウズウィンドウは現在Web プッシュに対応していません。

- クロム(Android用クロム)
- サファリ
- Firefox(およびAndroid携帯用Firefox)
- オペラ
- エッジ

プッシュプロトコルの標準とブラウザのサポートの詳細については、ブラウザに基づいてリソースを確認できます。

- [Safari(デスクトップ)](https://developer.apple.com/notifications/safari-push-notifications/)
- [Safari(モバイル)]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/safari_mobile_push/)
- [Mozilla Firefox](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)
- [Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/push)


[11]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[12]: {% image_buster /assets/img_archive/Macbook_Push.png %}
[13]: {% image_buster /assets/img_archive/WebPush_Prompt.png %}
