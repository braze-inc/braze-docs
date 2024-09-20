---
nav_title: ベストプラクティス
article_title: WhatsAppのベストプラクティス
page_order: 8
description: "本記事では、WhatsAppメッセージングチャンネルを使用する際のベストプラクティスを紹介する。"
page_type: reference
channel:
  - WhatsApp
 
---
# WhatsAppのベストプラクティス

> WhatsAppメッセージを送信する前に、以下のベストプラクティスを参考にして、高い電話品質評価を維持し、ブロックやレポートを回避し、ユーザーをオプトイン/アウトする。

## 高い電話品質評価を維持する 

WhatsAppの[電話品質評価は](https://www.facebook.com/business/help/896873687365001)、あなたのメッセージを受信したユーザーが、あなたのビジネスをブロックしたり報告したりといったアクションを起こしたかどうかに基づいている。品質評価が低く、一定時間以上改善されない場合、メッセージング上限が減る可能性があるため、高い品質を維持することが重要だ。

WhatsAppで初めてメッセージを送ると、これらのオプションがメッセージスレッド内に表示される。

![WhatsAppのメッセージスレッドには、企業をブロックしたり報告したりするオプションが用意されている。][1]{: style="max-width:30%;"}

{% alert note %}
ブロックやレポートに関する指標を確認するには、WhatsAppマネージャーで[「インサイト」タブが](https://www.facebook.com/business/help/683499390267496)オンになっていることを確認する。
{% endalert %}

ブロックやレポートが多発するのを避けるため、Brazeは、高い電話品質評価と安定したメッセージング制限を維持するために、以下のベストプラクティスを提案している。 

### WhatsAppのオプトイン要件とガイドラインに従う

WhatsAppでのコミュニケーションを開始する前に、全てのユーザーがWhatsAppメッセージの受信に積極的に同意していることを確認すること。ユーザーにオプトインを求める際、WhatsAppで御社からのメッセージを受信することに特に同意する旨を伝える必要がある。

{% alert note %}
オプトインの要件と役立つヒントについては、[WhatsAppのオプトインを取得するを](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)参照。
{% endalert %}

### メッセージングのベストプラクティスに従う

- チャンネル名にブランドを反映させ、ユーザーがスパムではなくあなたからのメッセージだと認識できるようにする。
- オプトインの同意を収集した後、ユーザーに確認メッセージを送信する。
- 適切な時間帯にメッセージを送る。

### 顧客にオプトアウトの選択肢を与える

オプトアウトは電話品質評価に影響を与えないため、ユーザーはWhatsApp通信の受信をオプトアウトした方が、ブロックや報告よりも有利となる。

ベストプラクティスとして推奨されるのは、ユーザーに送る最初のメッセージのフッターに、退会方法について説明することである。例えば、オプトアウトのトリガーとなる言葉を返答することで、ユーザーがWhatsAppチャンネルから退会できることを明記することができる。また、今後のキャンペーンに定期的にオプトアウト・フッターを含めることもできる。この設定方法については、[オプトインとオプトアウトを]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/)参照のこと。
 
![WhatsAppのメッセージのフッターに、チャンネル登録解除のためにSTOPと返信するよう記載する。][2]{: style="max-width:35%;"}

[1]: {% image_buster /assets/img/whatsapp/whatsapp_block_report.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp_unsubscribe.png %}