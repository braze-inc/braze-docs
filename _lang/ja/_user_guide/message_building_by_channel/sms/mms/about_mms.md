---
nav_title: "MMSについて"
article_title: MMSについて
page_order: 0
description: "この参考記事では、MMSメッセージとは何か、MMSチャンネルの一般的な使用例について説明する。"
page_type: reference
channel:
  - MMS
search_rank: 2  
---

# [![Braze ラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"}MMS メッセージについて

> MMSはマルチメディア・メッセージ・サービスとも呼ばれ、マルチメディア資産（JPEG、GIF、PNG）を含むメッセージを携帯電話に送信するために使われる。<br><br>SMSと同様、MMSは緊急性の高いメッセージング・チャネルであり、他のチャネルではできない方法で顧客と即座にコミュニケーションをとることができる。しかし、MMSはSMSの機能を拡張し、テキストだけのSMSにメディアを加えることができる。

## 想定される使用例

| ユースケース | 説明 |
| --- | --- |
| プロモーション | 知名度の高いSMSキャンペーンでユーザーを獲得するだけでなく、MMSのメディアとしての側面も活用し、提供する商品で購買意欲をそそる。 | 
| 再エンゲージメントキャンペーン | 他のすべてのチャネルで顧客の再誘導に失敗した場合、SMS の受信をオプトインした顧客を再びエンゲージします。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## MMSを知る

### MMSの可用性

米国とカナダのほとんどの通信事業者は、顧客の携帯電話でのマルチメディア資産の受信と表示をサポートしている。国際キャリアの場合、Brazeは、サポートされている米国またはカナダベースの電話番号から送信されたMMSメッセージを自動的に変換し、MMSをサポートしていない宛先にのみ送信する。このようなメッセージの場合、Brazeは添付されたメディアを、メッセージ本文に追加されたファイルにリンクする短いURLに置き換える。

### サブスクリプショングループ

[購読グループ][1] は、特定のタイプのメッセージング目的で使用される送信電話番号 (ショートコード、ロングコード、英数字の送信者 ID) の集まりです。購読グループには、MMS が有効にされた電話番号が必要です。この機能の有効化については、Brazeのアカウントマネージャーに相談すること。

### MMSメッセージの上限とスループット

MMS の場合、メッセージの上限は 1 MB です (これにはマルチメディアアセットとメッセージ本文のサイズが含まれます)。安全面を考慮し、Brazeではメッセージ本文も含め、マルチメディア資産は600KBを超えないことを推奨している。

MMSのスループットは、ロングコード経由で1秒間に1セグメントである。

### インバウンドMMS

ユーザーがメディアアイテムを含むインバウンドメッセージを送信すると、Braze は Liquid タグ {%raw%}`{{sms.${inbound_media_url}}}`{%endraw%} を介して Currents のメディアアイテムの URL と Liquid を公開します。

### 使用できるファイルタイプ

Braze は、JPEG、GIF、PNG、VCF ファイルに対応しており、MMS メッセージに 1 つのマルチメディアアセットを添付できます。


[picture] ： {% image_buster /assets/img/sms/MMS.png %}
[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement
