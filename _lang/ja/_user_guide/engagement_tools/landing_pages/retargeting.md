---
nav_title: ユーザーのリターゲティング
article_title: ランディングページを使用したユーザーのリターゲティング
description: "ランディングページを通じてフォームを送信したユーザーを再ターゲットする方法を学習します。"
page_order: 3
---

# ランディングページを使用したユーザーのターゲット変更

> 専用セグメントを作成するか、フォームが送信されたときにメッセージをトリガーすることによって、ランディングページを介してフォームを送信したユーザを再ターゲットする方法を学習します。

## 前提条件

開始する前に、[ランディングページ]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/) を作成する必要があります。

## ユーザーのリターゲティング

ユーザーがランディングページフォームを送信すると、Braze によって自動的に追跡されます。フォームの送信の総数は、[ランディングページアナリティクス]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#viewing-analytics) で表示できます。ただし、ユーザ固有のリターゲットの場合は、以下のいずれかの方法を使用して、ランディングページフォームからユーザをリターゲットする必要があります。

- **セグメントの使用:**新しいセグメントを作成して、ランディングページフォームを送信したユーザまたはまだ送信していないユーザを自動的に識別できます。
- **メッセージトリガーの使用:**メッセージトリガーを設定して、ユーザーがフォームを送信した後に自動的にユーザーにメッセージを送信したり、キャンバスに入力したりすることができます。

{% tabs local %}
{% tab Using a segment %}
[セグメントを作成する]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)場合、「リターゲティング」グループの下で [**ランディングページで送信されたフォーム**] を選択します。

![フィルターグループを「ランディングページの送信フォーム」としてセグメンテーションを作成する。]({% image_buster /assets/img/landing_pages/segmentation_selected.png %})

ここから、ランディングページのランディングページフォームを送信したかどうかに基づいてユーザをセグメンテーションできます。
{% endtab %}

{% tab Using a message trigger %}
[campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/)または[Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/)の配信オプションを選択する場合は、**Action Based Delivery**を選択し、**Submitted Landing Page form**を選択します。

このランディングページフォームを使用してフォームを送信するすべてのユーザは、選択したメッセージングチャネルを使用してメッセージを送信するか、選択したキャンバスに入力されます。

![メッセージングでランディングページのトリガーアクションを起こす。]({% image_buster /assets/img/landing_pages/trigger.png %})

{% alert note %}
ランディングページのアクションベースの配信オプションは、アプリ内メッセージでは使用できません。アプリ内メッセージを含むランディングページでフォームを送信したユーザーをターゲットにするには、キャンペーンの**Targeting Options** で**Submitted Form on Landing Page** フィルタを選択します。
{% endalert %}

{% endtab %}
{% endtabs %}
