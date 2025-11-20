---
nav_title: "WhatsAppへのクリック広告"
article_title: WhatsAppへのクリック広告
page_order: 1
description: "この参考記事では、WhatsAppへのAds That Clickの設定と使用方法をステップバイステップで紹介している。"
page_type: reference
alias: /whatsapp_use_cases/
channel:
  - WhatsApp
---

# WhatsAppへのクリック広告

> このページでは、WhatsAppへのAds That Clickの設定と使用方法をステップバイステップでご紹介。

WhatsAppへのクリック広告は、FacebookやInstagramなどのプラットフォーム上のメタ広告から新規顧客と既存顧客の両方を呼び込む効率的な方法である。これらの広告を利用して、ユーザーにWhatsAppの存在を認識させながら製品やサービスを宣伝しよう。

![無料配送を宣伝するCalorie RocketのFacebook広告と、ユーザーが広告のボタンを選択したときに発生するWhatsAppの会話。]({% image_buster /assets/img/whatsapp/ads_that_click_whatsapp.png %}){: style="max-width:70%;"}

## クリック広告を設定する

1. Meta Ads Managerで、ステップバイステップのガイド[How to create Ads That Click to WhatsAppに従って](https://business.whatsapp.com/products/create-ads-that-click-to-whatsapp)、Facebook、Instagram、またはその他のプラットフォームで広告を作成する。代わりにBrazeでレスポンスを設定する。

![エンゲージメント広告を作成するためのコンポーザーを備えた広告マネージャー。]({% image_buster /assets/img/whatsapp/meta_ads_composer.png %})

ユーザーからWhatsAppビジネスアカウントに送信されるメッセージを設定する際、特定の広告にトリガーされる特定の単語やフレーズを含める。この例では、フードデリバリーアプリが広告で宣伝されているため、「無料配達」を使っている。 

![広告マネージャーのテンプレート作成画面には、「無料配送を希望する」というメッセージがあらかじめ入力されている。]({% image_buster /assets/img/whatsapp/pre_filled_message.png %})

{% alert tip %}
WhatsAppで今すぐチャット」などのフレーズを使って、広告をクリックするとブランドとの会話が始まることを広告の説明文で明確にする。
{% endalert %}

{: start="2"}
2\.Brazeで、アクションベースのキャンバスを設定する。アクションベースのオプションは**Send a WhatsApp inbound messageで**、メッセージ本文は“YOUR_TRIGGER_WORD”. この例では、フードデリバリーアプリが "free delivery "を使っている。

![アクションベースのBrazeキャンバスのエントリスケジュール。トリガーイベントは "WhatsApp受信メッセージを送信"、メッセージ本文は "無料配送 "の正規表現にマッチする。]({% image_buster /assets/img/whatsapp/action_based_free_delivery.png %})

{: start="3"}
3\.顧客がキャンバスに入った直後に（例えば、遅延なく）送信するレスポンスメッセージをキャンバスに設定する。広告のクリックは厳密にはオプトインにあたるが、レスポンシブメッセージを設定し、今後WhatsAppでマーケティングメッセージを受信したいかユーザーに尋ねることを推奨する。 

{% alert tip %}
クイック返信先（「はい」や「結構です」など）のレスポンシブメッセージを設定し、ユーザーがオプトインするかどうかをすぐに示せるようにする。
{% endalert %}

広告で約束した割引コード、オファー、その他の情報も忘れずに提供すること！

![WhatsAppメッセージ作成画面に「Yes」と「No Thanks」のボタンが表示される。]({% image_buster /assets/img/whatsapp/quick_replies.png %})

![サブスクリプショングループにWhatsAppインバウンドを送信」というトリガーイベントと「YES」というトリガーワードを持つ「オプトイン」グループを持つキャンバスステップ。]({% image_buster /assets/img/whatsapp/opting_in_step.png %})

{: start="4"}
4\.以下のいずれかの更新方法でユーザープロファイルのサブスクリプションステータスを更新し、オプトインユーザーを登録する：
    \- REST APIを通じてサブスクリプションステータスを更新するBraze to Braze webhookを作成する。  
    \- 高度なJSONエディターを使用してユーザープロファイルを更新し、[WhatsAppキャンバスのサブスクリプションステータスを]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#whatsapp-opt-in-and-opt-out-process)テンプレートで更新する。

![ユーザープロファイルを更新するために高度なJSONエディタを使用するステップ。]({% image_buster /assets/img/whatsapp/user_update_step_json.png %})

![3つのアクションパスを含むAds That ClickをWhatsAppに送信するワークフローを示すキャンバス：オプトイン、オプトアウト、そしてみんな。]({% image_buster /assets/img/whatsapp/ads_that_click_canvas.png %})

## 考慮事項

WhatsApp をクリックした広告から始まるコンバージョンは、以下の条件を満たせば無料となる：

- WhatsAppへのクリック広告など、[無料エントリーポイントを](https://developers.facebook.com/docs/whatsapp/pricing#free-entry-point-conversations)経由してユーザーからメッセージングがあった場合、24時間[カスタマーサービスウィンドウが](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows)開封され、そのユーザーにどのようなメッセージでも送ることができる。
- 顧客サービスウィンドウ内（24時間以内）に返信した場合、72時間無料エントリーポイントが開封され、72時間以内のメッセージはすべて無料となる。
- レスポンシブ・メッセージングは無料だ。