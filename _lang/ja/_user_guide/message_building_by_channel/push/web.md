---
nav_title: "Web プッシュ"
article_title: Web プッシュ通知
page_order: 8.5
page_type: reference
description: "この参照ページでは、Web プッシュ通知と、それを作成するために必要なステップへのリンクアウトについて簡単に説明します。"
platform: Web
channel:
  - push

---

# Web プッシュ

> Braze でWeb プッシュ通知について学習し、独自に作成するためのリソースを見つけます。

Web プッシュは、Web アプリケーションのユーザーと連携するもう1 つのすばらしい方法です。[supported browsers](#supported-browsers)からウェブサイトを訪れるお客様は、ウェブページがロードされているかどうかにかかわらず、ウェブアプリケーションからウェブプッシュを受信するためにオプトインできます。

## 概要

Webプッシュ通知は、迅速な変換を可能にする緊急の実用的な更新を提供します。Web プッシュでは、次の操作を実行できます。

- 価格が下がるなど、重要なデータが変化したときにメッセージを正しくトリガーします
- 簡単なコール・ツー・アクション・ボタンで人々をウェブサイトに戻す
- 製品情報と顧客情報でプッシュをカスタマイズし、メッセージを関連づけます

Web プッシュは、スマートフォンでアプリプッシュ通知を操作するのと同じように機能します。Web プッシュの作成の詳細については、[プッシュ通知の作成][11]を参照してください。

![ノートパソコンと携帯電話に同じプッシュメッセージが表示されたWebプッシュ例][12]{: style="border:none"}

## 潜在的なユースケース

一般的なWeb プッシュメッセージのユースケースの例を次に示します。

| 使用例| 説明|
| --- | --- |
| 無料トライアル| ウェブサイトの新規訪問者に無料トライアルに登録するように促します。ユーザーに特別なことを体験する機会を与えれば、有料の顧客になる可能性が高くなる。|
| App download | Web ユーザをモバイルアプリに描画して、製品からさらに大きな価値を得ることができます。パーソナライゼーションを活用して、現在のエンゲージメントパターンに基づいてアプリの利点を強調することを検討します。|
| 割引と販売| 時間に敏感なイベントやプロモーションに対する顧客の意識を高める。ブランドのプロモーションに対する認知度を高めるために、ウェブプッシュを含む複数のチャネルにわたるメッセージ。|
| カート放棄| トランザクションを完了していないユーザーに自動リマインダーを送信して、チェックアウトフローに戻します。<br><br>Brazeが実施した調査によると、ウェブプッシュはEメールよりも53%効果が高く、受信者が戻ってきて購入を完了する際のモバイルプッシュよりも23%影響が大きいことがわかりました。|
{: .reset-td-br-1 .reset-td-br-2}

## Web プッシュを使用するための前提条件

Brazeを使用してプッシュメッセージを作成して送信する前に、開発者と協力してウェブサイトにプッシュを統合する必要があります。詳細な手順については、[Webプッシュ統合ガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/)を参照してください。

### プッシュ許可

どのブランドでも、ウェブサイトでウェブプッシュ通知を統合し、使用することができます。通知は、Web ブラウザが開いている限り、現在のWeb 訪問者と以前のWeb 訪問者の両方に到達できますが、従来のモバイルアプリプッシュと同様に、通知を受信するには[opt in が必要です。

{% alert tip %}
ブラウザ内のメッセージを使用して、Web プッシュを選択するようにユーザーをプライミングすることを検討します。これは、[プッシュプライマー]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) とも呼ばれます。
{% endalert %}

## 対応ブラウザ

次のブラウザは、Web プッシュ通知をサポートしています。ただし、プライベートブラウジングウィンドウでは、現在Web プッシュはサポートされていません。

- Chrome (およびAndroid モバイル用のChrome)
- Safari
- Firefox (およびAndroidモバイル版Firefox)
- Opera
- Edge

プッシュプロトコルの標準とブラウザのサポートの詳細については、ブラウザに基づいてリソースを確認できます。

- [Safari(デスクトップ)](https://developer.apple.com/notifications/safari-push-notifications/)
- [Safari(モバイル)]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/safari_mobile_push/)
- [Mozilla Firefox](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)
- [Microsoft Edge](https://developer.microsoft.com/en-us/microsoft-edge/status/pushapi/)


[11]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[12]: {% image_buster /assets/img_archive/Macbook_Push.png %}
[13]: {% image_buster /assets/img_archive/WebPush_Prompt.png %}
