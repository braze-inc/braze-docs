---
nav_title: "WhatsAppする広告"
article_title: WhatsAppする広告
page_order: 1
description: "このリファレンス記事では、上に設定し、WhatsAppするためにクリックする広告を使用するためのステップごとの手引きを提供します。"
page_type: reference
alias: /whatsapp_use_cases/
channel:
  - WhatsApp
---

# WhatsAppする広告

> このページでは、設定のステップごとのガイドを提供し、WhatsAppにクリックする広告を使用することで、あなたとあなたのチームがWhatsAppを昇格させることができます。

WhatsAppをクリックする広告は、Fac eBook、Ins タグ ram、または他のプラットフォーム s のメタ広告から、新規および既存の両方の顧客を取得する効率的な方法です。これらの広告を使って、ユーザーにあなたのWhatsAppの存在を認識させながら、あなたの商品やサービスを宣伝しましょう。

![無料配信を宣伝するカロリー・ロケットのFaceBook広告と、ユーザーが広告のボタンを選択したときに起こるそれぞれのWhatsApp対話。]({% image_buster /assets/img/whatsapp/ads_that_click_whatsapp.png %}){: style="max-width:70%;"}

## WhatsAppする広告を設定する

1. Meta Ads Manager で、Fac eBook、Ins タグ ram、または他のプラットフォームs 上に、ステップ別ガイド[ WhatsApp](https://business.whatsapp.com/products/create-ads-that-click-to-whatsapp) をクリックする広告の作成方法に従って広告を作成します。**Do not** 自動レスポンスを設定します。代わりにBraze でレスポンスを設定します。

![エンゲージメント広告を作成するコンポーザー付きのAds Manager。]({% image_buster /assets/img/whatsapp/meta_ads_composer.png %})

事前に入力されたメッセージを設定すると、ユーザーからWhatsAppの取引先に送信されます。このメッセージには、特定の広告に固有のレスポンスをトリガーするために使用する特定の単語または語句が含まれます。この例題では、食品配送アプリは"free delivery"を使用しています。これは、広告でプロモートされるためです。 

![広告マネージャのテンプレートコンポーザーに、&quot の事前入力されたメッセージがあります。無料配信" が欲しいです。]({% image_buster /assets/img/whatsapp/pre_filled_message.png %})

{% alert tip %}
「WhatsApp&クォートでチャット;」のようなフレーズを使って、広告をクリックするとブランドとの会話が始まることを、広告の説明で明確にしてください。
{% endalert %}

{: start="2"}
2\.Braze では、アクション ベースのオプションが**WhatsApp受信メッセージを送信する** で、メッセージ本文が“YOUR_TRIGGER_WORD”. であるアクション ベースのキャンバスを設定します。この例では、食品配送アプリは"free delivery" を使用しています。

![アクション ベースのBrazeキャンバスのエントリスケジュール。トリガーイベントは&quot、WhatsApp受信メッセージ&quot、メッセージ本文は&quot、無料配信&quot、の正規表現に一致します。]({% image_buster /assets/img/whatsapp/action_based_free_delivery.png %})

{: start="3"}
3\.キャンバスで、顧客がキャンバスに入った直後に送信する応答メッセージを設定します(遅延なしの場合など)。アドをクリックすることは技術的にはオプトインを構成しますが、今後WhatsAppでマーケティングを受け取りたい場合は、あなたのレスポンスメッセージを設定してユーザーに問い合わせることをお勧めします。 

{% alert tip %}
応答メッセージをクイック返信("Yes"または"No Thanks"など)で設定すると、ユーザーがすぐにオプトインを希望するかどうかを示すことができます。
{% endalert %}

広告で約束した割引コードやオファーなどもお忘れなく！

!["Yes"および"No Thanks"のボタンリプライでWhatsApp メッセージ作成画面。]({% image_buster /assets/img/whatsapp/quick_replies.png %})

!["Opting in"トリガーイベントが"送信された受信WhatsAppがサブスクリプショングループ"およびトリガー単語が"YES"であるキャンバスステップ。]({% image_buster /assets/img/whatsapp/opting_in_step.png %})

{: start="4"}
4\.次のいずれかの更新方法でユーザープロファイルsのサブスクリプション ステータスを更新することにより、ユーザーsをオプトインします。
    \- REST API を介してサブスクリプション ステータスを更新するBraze-to-Braze Webhookを作成します。  
    \- 高度なJSON エディタを使用して、[ 更新のユーザープロファイルをテンプレートでユーザーのサブスクリプション ステータスをWhatsApp キャンバス]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#whatsapp-opt-in-and-opt-out-process) に更新します。

![高度なJSONエディタを使用してユーザープロファイルを更新するユーザー 更新キャンバスステップ。]({% image_buster /assets/img/whatsapp/user_update_step_json.png %})

![キャンバスは、3 つのアクションパスs を含む、WhatsApp にクリックする広告を送信するためのワークフローを表示します。Opting in、Opting Out、Everyone その他。]({% image_buster /assets/img/whatsapp/ads_that_click_canvas.png %})

## 考慮事項

以下の条件が満たされている場合、WhatsAppにクリックする広告から始まる会話は無料です。

- ユーザーメッセージが[無料の入力ポイント](https://developers.facebook.com/docs/whatsapp/pricing#free-entry-point-conversations)を経由する場合(WhatsAppにクリックする広告など)、任意の種類のメッセージをユーザー送信できる24時間[顧客サービスウィンドウ](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows)開封s。
- 顧客窓口(24時間以内)でご回答いただければ、72時間無料エントリ点数開封s、72時間枠内のメールは無料となります。
- レスポンスメッセージングは無料です。