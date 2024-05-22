---
nav_title: ベストプラクティス
article_title: WhatsApp ベストプラクティス
page_order: 8
description: "本記事では、WhatsAppメッセージングチャンネルを利用する際のベストプラクティスをご紹介します。"
page_type: reference
channel:
  - WhatsApp
 
---
# WhatsAppのベストプラクティス

> WhatsAppメッセージを送信する前に、以下のベストプラクティスをご参照ください。

## 高い電話品質評価を維持する 

WhatsAppの[電話品質評価は](https://www.facebook.com/business/help/896873687365001)、あなたのメッセージを受信したユーザーがあなたのビジネスをブロックしたり報告したりするなどのアクションに基づいています。品質評価が低く、一定時間以上改善されない場合、メッセージの上限が下がる可能性があるため、高い品質を維持することが重要です。

WhatsAppで初めてメッセージを送ると、これらのオプションがメッセージスレッド内に表示されます。

WhatsAppのメッセージスレッドにブロックや通報のオプションが追加された][1]。{: style="max-width:30%;"}

{% alert note %}
ブロックやレポートに関する指標は、WhatsApp マネージャーの「[インサイト」タブが](https://www.facebook.com/business/help/683499390267496)オンになっていることをご確認下さい。
{% endalert %}

ブロックやレポートが多発するのを避けるため、Brazeでは、高い電話品質評価と安定したメッセージング制限を維持するために、以下のベストプラクティスを提案しています。 

### WhatsAppのオプトイン要件とガイドラインに従う

WhatsAppでコミュニケーションを開始する前に、全てのユーザーがWhatsAppメッセージの受信に同意していることを確認して下さい。ユーザーにオプトインを求める際は、御社からのメッセージをWhatsAppで受信することに同意する旨を伝える必要があります。

{% alert note %}
オプトイン要件と役立つヒントについては、[WhatsAppのオプトイン取得を](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)ご覧下さい。
{% endalert %}

### メッセージングのベストプラクティスに従う

- チャンネル名にブランドを反映させ、ユーザーがスパムではなく、あなたからのメッセージだと認識できるようにしましょう。
- オプトインの同意を収集した後、ユーザーに確認メッセージを送信する。
- 適切な時間帯にメッセージを送る。

### 顧客にオプトアウトの選択肢を与える

オプトアウトは電話品質評価に影響を与えないため、WhatsAppの受信をオプトアウトする方が、ブロックや報告よりもユーザーにとって有益です。

ベストプラクティスとして推奨されるのは、ユーザーに送る最初のメッセージのフッターに、退会方法について説明することです。例えば、オプトアウトのトリガーとなる言葉を使って返答することで、ユーザーがWhatsAppチャンネルから退会できることを明記することができます。また、今後のキャンペーンに定期的にオプトアウトフッターを含めることもできます。設定方法については、[オプトインとオプトアウトを]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/)ご覧ください。
 
WhatsAppのメッセージには、チャンネルから退会するにはSTOPと返信するようフッターに書かれている][2]。{: style="max-width:35%;"}

[1]: {% image_buster /assets/img/whatsapp/whatsapp_block_report.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp_unsubscribe.png %}