---
nav_title: Webhookテンプレートを作成する
article_title: Webhookテンプレートを作成する
page_order: 2
tool:
  - Templates
channel:
  - webhooks
description: "このリファレンス記事では、Brazeプラットフォーム内で後で使用するためのWebhookテンプレートの作成とカスタマイズ方法について説明する。"

---

# ウェブフック・テンプレートを作成する

> このリファレンス記事では、Brazeプラットフォーム内で後で使用するためのWebhookテンプレートの作成とカスタマイズ方法について説明する。

## ステップ 1:ウェブフック・テンプレート・エディターに移動する

**Templates**>**Webhook Templatesに**進む。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合、このページは**Engagement**>**Templates & Media**>**Webhook Templatesの**下にある。
{% endalert %}

![Brazeダッシュボードの「Templates and Media」ページにある「Webhook Templates」タブ。][1]

## ステップ2:新しいテンプレートを作成する

新しいテンプレートを作成したり、既存のテンプレートを編集したり、あらかじめデザインされたウェブフック・テンプレートのいずれかを使用したりすることができる。

## ステップ 3:テンプレートをカスタマイズする

Webhookテンプレートは様々なユースケースに使用できる。 使用する一意のテンプレート名を入力することから始めることができる。 また、ウェブフックURL、リクエストボディ、リクエストヘッダーを入力し、使用するHTTPメソッドを選択することもできる。

![ウェブフック・テンプレートを作成するときに「Compose」タブをクリックする。利用可能なフィールドは、言語、ウェブフックURL、リクエストボディである。][2]{: style="max-width:80%"}

ユーザーに送信する前に、Webhookがどのように見えるかを確認したい場合は、**Settings**タブからテストWebhookを送信することができる。

## ステップ 4:テンプレートを保存する

**Save Template**ボタンをクリックしてテンプレートを保存する。これで、あなたが選んだキャンペーンでこのテンプレートを使う準備ができた。

![Webhookテンプレート保存][3]{: style="max-width:50%"}

{% alert note %}
既存のテンプレートに加えた編集は、そのテンプレートの旧バージョンを使用して作成されたキャンペーンには反映されない。
{% endalert %}

## Webhookテンプレートを管理する

Webhookテンプレートの[複製や]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) [アーカイブも]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/)できる！テンプレートとクリエイティブ・コンテンツの作成と管理については、「[テンプレートとメディア]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/)」をご覧ください。

[1]: {% image_buster /assets/img_archive/webhook_template_campaign.png %}
[2]: {% image_buster /assets/img_archive/Webhook_template_test.png %}
[3]: {% image_buster /assets/img_archive/Webhook_template_save.png %}
