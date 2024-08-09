---
nav_title: チャネル別メッセージ構築
article_title: チャネル別メッセージ構築
page_order: 5
layout: dev_guide

guide_top_header: "チャネル別メッセージ構築"
guide_top_text: "メッセージングチャネルは、電話や Web ブラウザでのプッシュ通知、メール、アプリ内メッセージなどを通じて、顧客と実質的にコミュニケーションを図ることができる方法です。これらのチャネルと Braze での活用方法に関する詳細については、以下のセクションを参照してください。または、<a href='https://learning.braze.com/series/messaging-channels' target='_blank'>メッセージングチャネル</a>のBrazeラーニングコースをご覧ください!<br><br>Braze を使えば、各チャネルでアクセスしやすいメッセージングキャンペーンを作成できます。エンジニアと協力して、実装においてアクセシビリティ基準を満たすようにしてください。"
description: "このランディングページは、Braze メッセージングチャネルを対象としています。メッセージングチャネルは、電話や Web ブラウザでのプッシュ通知、メール、アプリ内メッセージなどを通じて、顧客と実質的にコミュニケーションを図ることができる方法です。"

guide_featured_title: "使用可能なチャネル"
guide_featured_list:
- name: コンテンツカードによって促進された
  link: /docs/user_guide/message_building_by_channel/content_cards/
  image: /assets/img/braze_icons/table.svg
- name: メールメッセージ
  link: /docs/user_guide/message_building_by_channel/email/
  image: /assets/img/braze_icons/mail-01.svg
- name: "アプリ内メッセージング"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/
  image: /assets/img/braze_icons/annotation-dots.svg
- name: プッシュメッセージング
  link: /docs/user_guide/message_building_by_channel/push/
  image: /assets/img/braze_icons/marker-pin-01.svg
- name: SMS &amp; MMS
  link: /docs/user_guide/message_building_by_channel/sms/
  image: /assets/img/braze_icons/message-text-circle-01.svg
- name: Webhook
  link: /docs/user_guide/message_building_by_channel/webhooks/
  image: /assets/img/braze_icons/brackets.svg
- name: WhatsApp
  link: /docs/user_guide/message_building_by_channel/whatsapp/
  image: /assets/img/braze_icons/whatsapp.svg
---

## メッセージチャネルの選択

キャンペーンとキャンバスに最適なメッセージチャネルを決定する際には、メッセージのコンテンツと緊急性を常に考慮してください。

- **コンテンツ**は、メッセージを可視化してエンゲージメントする方法です。マルチメディアやその他のアセットをコピーに追加して、コンテンツを充実化できます。
- **緊急性**は、メッセージがユーザーに通知して注意を引く速さの尺度です。ユーザーがすぐに表示できる通知は緊急性が高くなりますが、アプリがユーザーにログインを求めるメッセージは緊急性が低くなります。

次のマトリックスは、重要なメッセージングチャネルの長所と短所を、内容と緊急性の観点から表示しています。メッセージの緊急性とコンテンツがどの程度リッチであるべきかを常に考えてから、キャンペーンに適したチャネルを選択してください。

![モバイル/Web プッシュはシンプルな内容で緊急性が高い。メールはリッチな内容で緊急性が高い。アプリ内/ブラウザーメッセージはシンプルな内容で緊急性が低い。コンテンツカードは緊急性が低く、リッチな内容である]({% image_buster /assets/img_archive/messaging_matrix.png %})

このマトリックスを活用する方法の詳細については、Braze ラーニングコースの「[メッセージングマトリックスを理解する](https://learning.braze.com/understand-the-messaging-matrix)」をご覧ください。

<br><br>
