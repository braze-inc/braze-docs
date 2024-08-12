---
nav_title: Webhook テンプレートの作成
article_title: Webhook テンプレートの作成
page_order: 2
tool:
  - Templates
channel:
  - webhooks
description: "このリファレンス記事では、Webhook テンプレートを作成およびカスタマイズして、Braze プラットフォーム内で後で使用する方法について説明します。"

---

# Webhook テンプレートの作成

> このリファレンス記事では、Webhook テンプレートを作成およびカスタマイズして、Braze プラットフォーム内で後で使用する方法について説明します。

## ステップ 1:Webhook テンプレートエディタに移動します

**Templates**> **Webhook Templates** に移動します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation) を使用している場合は、**Engagement**> **Templates & Media**> **Webhook Templates** の下にこのページがあります。
{% endalert %}

![ろうそくダッシュボードのテンプレートとメディアページの下のWebhook Templates(Webhook テンプレート)][1]

## ステップ 2:新しいテンプレートの作成

これで、新しいテンプレートを作成したり、既存のテンプレートを編集したり、提供されている事前に署名されたWebhook テンプレートのいずれかを使用したりできます。

## ステップ 3:テンプレートのカスタマイズ

Webhook テンプレートは、さまざまなユースケースで使用できます。 まず、使用する一意のテンプレート名を入力します。 Webhook URL、リクエスト本文、リクエストヘッダーを入力し、使用するHTTP メソッドを選択することもできます。

![Webhook テンプレートを作成するときにタブを作成する]使用可能なフィールドは、言語、webhook URL、およびリクエスト本文です。][2]{: style="max-width:80%"}

ユーザに送信する前にWebhook の外観を確認する場合は、**Settings** タブからテストWebhook を送信できます。

## ステップ 4: テンプレートを保存する

テンプレートを保存するには、**Save Template**ボタンをクリックします。これで、選択したキャンペーンでこのテンプレートを使用する準備ができました。

![Webhook Template Save][3]{: style="max-width:50%"}

{% alert note %}
既存のテンプレートに対する編集は、そのテンプレートの以前のバージョンを使用して作成されたキャンペーンには反映されません。
{% endalert %}

## Webhook テンプレートの管理

また、[duplicate]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/)と[archive]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/)Webhook Templates![Templates & Media]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/) でテンプレートとクリエイティブコンテンツの作成と管理について詳しく説明します。

[1]: {% image_buster /assets/img_archive/webhook_template_campaign.png %}
[2]: {% image_buster /assets/img_archive/Webhook_template_test.png %}
[3]: {% image_buster /assets/img_archive/Webhook_template_save.png %}
