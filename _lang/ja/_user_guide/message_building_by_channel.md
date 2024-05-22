---
nav_title: チャネル別メッセージ構築
article_title: チャネル別メッセージ構築
page_order: 5
layout: dev_guide

guide_top_header: "チャネル別メッセージ構築"
guide_top_text: "メッセージングチャネルは、電話やウェブブラウザでのプッシュ通知、メール、アプリ内メッセージなどを通じて、顧客と実質的にコミュニケーションを図ることができる方法です。これらのチャネルと Braze での活用方法に関する詳細については、以下のセクションを参照してください。または、<a href='https://learning.braze.com/series/messaging-channels' target='_blank'>メッセージングチャネル</a>!<br><br>br>Braze を使用して、各チャネルにアクセス可能なメッセージングキャンペーンを作成できます。エンジニアと協力して、実装においてアクセシビリティ基準を満たすようにしてください。"
description: "このランディングページは、Braze メッセージングチャネルを対象としています。メッセージングチャネルは、電話やウェブブラウザでのプッシュ通知、メール、アプリ内メッセージなどを通じて、顧客と実質的にコミュニケーションを図ることができる方法です。"

guide_featured_title: "使用可能なチャネル"
guide_featured_list:
- name: Content Cards
  link: /docs/user_guide/message_building_by_channel/content_cards/
  fa_icon: fa-solid fa-table-list
- name: Email Messaging
  link: /docs/user_guide/message_building_by_channel/email/
  fa_icon: fa-solid fa-envelope
- name: "In-App Messaging"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/
  fa_icon: fa-regular fa-comment-dots
- name: News Feed
  link: /docs/user_guide/engagement_tools/news_feed/
  fa_icon: fa-solid fa-newspaper
- name: Push Messaging
  link: /docs/user_guide/message_building_by_channel/push/
  fa_icon: fa-solid fa-mobile-screen-button
- name: SMS & MMS
  link: /docs/user_guide/message_building_by_channel/sms/
  fa_icon: fa-solid fa-comment-sms
- name: Webhooks
  link: /docs/user_guide/message_building_by_channel/webhooks/
  fa_icon: fa-solid fa-arrows-spin
- name: WhatsApp
  link: /docs/user_guide/message_building_by_channel/whatsapp/
  fa_icon: fa-brands fa-whatsapp
---

## メッセージチャネルの選択

キャンペーンとキャンバスに最適なメッセージチャネルを決定する際には、メッセージのコンテンツと緊急性を常に考慮してください。

- **コンテンツ**は、メッセージを可視化してエンゲージメントする方法です。マルチメディアやその他のアセットをコピーに追加して、コンテンツを充実化できます。
- **緊急性**は、メッセージがユーザーに通知して注意を引く速さの尺度です。ユーザーがすぐに表示できる通知は緊急性が高くなりますが、アプリがユーザーにログインを求めるメッセージは緊急性が低くなります。

次のマトリックスは、重要なメッセージングチャネルの長所と短所を、内容と緊急性の観点から表示しています。メッセージの緊急性とコンテンツがどの程度リッチであるべきかを常に考えてから、キャンペーンに適したチャネルを選択してください。

![Mobile/web push are simple content, high urgency; Emails are rich content, high urgency; In-app/browser messages are simple content, low urgency; Content Cards are low urgency, rich content]({% image_buster /assets/img_archive/messaging_matrix.png %})

このマトリックスを活用する方法の詳細については、[メッセージングマトリックスを理解する](https://learning.braze.com/understand-the-messaging-matrix)の Braze ラーニングコースをご覧ください。

<br><br>
