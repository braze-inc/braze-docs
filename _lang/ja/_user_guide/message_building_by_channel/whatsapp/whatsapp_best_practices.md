---
nav_title: ベストプラクティス
article_title: WhatsAppのベストプラクティス
page_order: 9
page_order: 9
description: "この記事では、WhatsApp メッセージングチャネルを使用する際に推奨されるベストプラクティスの概要を示します。電話の高品質評価を維持する方法、高いブロック率とレポート率を回避する方法などがあります。"
page_type: reference
channel:
  - WhatsApp
 
---
# WhatsAppのベストプラクティス

> WhatsApp メッセージを送信する前に、電話の高品質評価を維持、ブロックとレポートの回避、ユーザーのオプトインおよびオプトアウトに関して推奨されるベストプラクティスを参照してください。

## 電話の高品質評価の維持 

WhatsAppの[電話品質評価は](https://www.facebook.com/business/help/896873687365001)、あなたのメッセージを受信したユーザーが、あなたのビジネスをブロックしたり報告したりといったアクションを起こしたかどうかに基づいている。高品質の評価を維持することが重要です。評価が低く、一定期間に改善されないと、メッセージング制限が低下する可能性があるためです。

WhatsAppで 初めてユーザーにメッセージを送信すると、以下のオプションがメッセージスレッド内に表示されます。

![WhatsAppのメッセージスレッドにブロックやレポートオプションが追加された。]({% image_buster /assets/img/whatsapp/whatsapp_block_report.png %}){: style="max-width:30%;"}

{% alert note %}
ブロックとレポートに関する指標については、WhatsApp Manager の [[Insights] タブ](https://www.facebook.com/business/help/683499390267496)を必ずオンにしてください。
{% endalert %}

ブロックやレポートの多発を回避するため、Braze では、電話の高品質評価と安定したメッセージング制限を維持する以下のベストプラクティスをお勧めしています。 

### WhatsAppのオプトイン要件とガイドラインに従う

WhatsApp でユーザーとの通信を開始する前に、必ず、すべてのユーザーから WhatsApp メッセージの受信について、積極的な同意を得てください。ユーザーにオプトインを求める際、WhatsAppで御社からのメッセージを受信することに特に同意する旨を伝える必要がある。

{% alert note %}
オプトインの要件と役立つヒントについては、[WhatsApp のオプトインを取得する](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)を参照してください。
{% endalert %}

### メッセージングのベストプラクティスに従う

- チャンネル名にブランドを反映させ、ユーザーがスパムではなくあなたからのメッセージだと認識できるようにする。
- ユーザーからオプトインの同意を収集した後、ユーザーに確認メッセージを送信します。
- 適切な時間帯にメッセージを送る。

### 顧客用にオプトアウトのオプションを用意する

オプトアウトは電話の品質評価に影響しないため、ユーザーがWhatsApp 通信の受信をオプトアウトするほうが、ブロックやレポートをよりも優れています。

推奨されるベストプラクティスは、ユーザーに送信する最初のメッセージのフッターにオプトアウトする方法の手順を記載することです。例えば、ユーザーがオプトアウトをトリガーする言葉を応答することで WhatsApp チャネルを購読解除できる、と記載できます。また、今後のキャンペーンに定期的にオプトアウトのフッターを含めることもできます。この設定方法については、[オプトインとオプトアウトを]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/)参照のこと。
 
![WhatsAppのメッセージには、配信停止のためにSTOPの返事をするようフッターに書かれている。]({% image_buster /assets/img/whatsapp/whatsapp_unsubscribe.png %}){: style="max-width:35%;"}

