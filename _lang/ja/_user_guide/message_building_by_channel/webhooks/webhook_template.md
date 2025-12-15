---
nav_title: ウェブフック・テンプレートを作成する
article_title: Webhookテンプレートを作成する
page_order: 2
tool:
  - Templates
channel:
  - webhooks
description: "このリファレンス記事では、Brazeプラットフォーム内で後で使用するためのWebhookテンプレートの作成とカスタマイズ方法について説明する。"

---

# ウェブフック・テンプレートを作成する

> Webhookを構築しカスタマイズすると、後からBrazeプラットフォーム内で使用するためのWebhookテンプレートを作成し、活用することができる。こうすることで、さまざまなキャンペーンで一貫してさまざまなWebhookを構築することができる。

## ステップ1:Webhookテンプレートエディターに行く

Braze ダッシュボードで、[**テンプレート**] > [**Webhook テンプレート**] に移動します。

![Webhook Templates "ページには、あらかじめデザインされ保存されたWebhookテンプレートがある。]({% image_buster /assets/img_archive/webhook_template_campaign.png %})

## ステップ 2:テンプレートを選ぶ

ここから、新しいテンプレートを作成するか、あらかじめデザインされたWebhookテンプレートを使用するか、既存のテンプレートを編集するかを選択できる。

例えば、[LINEを]({{site.baseurl}}/user_guide/message_building_by_channel/line)メッセージングチャネルとして使っている場合、**LINE Carouselや** **LINE Image**用のテンプレートを使って、いくつかのWebhookを設定することができる。

## ステップ 3:テンプレートの詳細を記入する

1. Webhookテンプレートにユニークな名前をつける。
2. (オプション）テンプレートの説明を追加し、このテンプレートがどのように使用されるかを説明する。
3. 必要に応じて[チームや]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) [タグを]({{site.baseurl}}/user_guide/administrative/app_settings/tags/)追加し、テンプレートの検索やフィルターに役立てる。

## ステップ4:テンプレートを作成する

1. Webhook URL を入力します。
2. HTTPメソッドを選択する。
3. リクエスト本文を追加します。これは**JSONのキーと値のペアか**、**生テキスト**である。
4. (オプション）リクエストヘッダーを追加する。これは、Webhook 送信先で必須の場合があります。

![Webhookテンプレート作成時の「Compose」タブ。利用可能なフィールドは、Webhook URL、HTTP メソッド、リクエスト本文、リクエストヘッダーである。言語を追加することもできる。]({% image_buster /assets/img_archive/Webhook_template_test.png %}){: style="max-width:90%"}

## ステップ 5: テンプレートをテストする

ユーザーに送信する前にWebhookがどのように見えるかを確認するには、**Test**タブを使ってテストWebhookを送信することができる。ここで、ランダムなユーザー、既存のユーザー、カスタムユーザーのいずれかとしてメッセージをプレビューできます。

## ステップ 6:テンプレートを保存する

必ず [**テンプレートを保存**] をクリックしてテンプレートを保存してください。これで、あなたが選んだキャンペーンでこのテンプレートを使う準備ができた。

{% alert note %}
既存のテンプレートに加えた編集は、そのテンプレートの以前のバージョンを使用して作成されたキャンペーンには反映されない。
{% endalert %}

## テンプレートの管理

Webhook テンプレートを[複製したり、アーカイブしたりする]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/)ことで、テンプレートのリストをよりよく整理・管理することができる。

テンプレートとクリエイティブ・コンテンツの作成とマネージャーについては、「[テンプレートとメディア]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/)」で学習しよう。

