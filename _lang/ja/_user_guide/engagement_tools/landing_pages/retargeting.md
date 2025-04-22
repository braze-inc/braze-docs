---
nav_title: ユーザーのリターゲット
article_title: ランディングページを使用したユーザのリターゲット
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
{% tab セグメントの使用 %}
[でセグメント]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)を作成する場合、"Retargeting"groupの下で、**ランディングページで送信フォーム**を選択します。

![フィルタグループを&quot として選択したセグメントの作成;Landing Page&quot で送信されるフォーム;]({% image_buster /assets/img/landing_pages/segmentation_selected.png %})

ここから、ランディングページのランディングページフォームを送信したかどうかに基づいて、ユーザをセグメンテーションできます。
{% endtab %}

{% tab メッセージトリガーの使用 %}
[campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/)または[Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/)の配信オプションを選択する場合は、**Action Based Delivery**を選択し、**Submitted Landing Page form**を選択します。

このランディングページフォームを使用してフォームを送信するすべてのユーザは、選択したメッセージングチャネルを使用してメッセージを送信するか、選択したキャンバスに入力されます。

![メッセージング]({% image_buster /assets/img/landing_pages/trigger.png %})のランディングページトリガアクション
{% endtab %}
{% endtabs %}
