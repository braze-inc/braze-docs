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

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"}MMSメッセージについて

> MMSはマルチメディア・メッセージ・サービスとも呼ばれ、マルチメディア資産（JPEG、GIF、PNG）を含むメッセージを携帯電話に送信するために使われる。<br><br>SMSと同様、MMSは緊急性の高いメッセージング・チャネルであり、他のチャネルではできない方法で顧客と即座にコミュニケーションをとることができる。しかし、MMSはSMSの機能を拡張し、テキストだけのSMSにメディアを加えることができる。

## 想定される使用例

| ユースケース | 説明 |
| --- | --- |
| プロモーション | 知名度の高いSMSキャンペーンでユーザーを獲得するだけでなく、MMSのメディアとしての側面も活用し、提供する商品で購買意欲をそそる。 | 
| 再エンゲージメント・キャンペーン | SMSを受信するようにオプトインした顧客を、他のすべてのチャネルで呼び戻すことができなかった場合に、再度エンゲージする。 |
{: .reset-td-br-1 .reset-td-br-2}

## MMSを知る

### MMSの可用性

米国とカナダのほとんどの通信事業者は、顧客の携帯電話でのマルチメディア資産の受信と表示をサポートしている。国際キャリアの場合、Brazeは、サポートされている米国またはカナダベースの電話番号から送信されたMMSメッセージを自動的に変換し、MMSをサポートしていない宛先にのみ送信する。このようなメッセージの場合、Brazeは添付されたメディアを、メッセージ本文に追加されたファイルにリンクする短いURLに置き換える。

### サブスクリプショングループ

サブスクリプショングループ][1] ]は、特定のタイプのメッセージング目的で使用される送信電話番号（ショートコード、ロングコード、英数字の送信者ID）の集まりである。購読グループには、MMSが有効な電話番号が必要である。この機能の有効化については、Brazeのアカウントマネージャーに相談すること。

### MMSメッセージの上限とスループット

MMSの場合、メッセージの上限は1MBである（これにはマルチメディア・アセットとメッセージ・ボディのサイズが含まれる）。安全面を考慮し、Brazeではメッセージ本文も含め、マルチメディア資産は600KBを超えないことを推奨している。

MMSのスループットは、ロングコード経由で1秒間に1セグメントである。

### インバウンドMMS

ユーザーがメディアアイテムを含むインバウンドメッセージを送信すると、BrazeはLiquidタグを通してLiquidと同様にCurrentsでメディアアイテムのURLを公開する。 {%raw%}`{{sms.${inbound_media_url}}}`{%endraw%}

### 使用可能なファイルの種類

Brazeは、JPEG、GIF、PNG、VCFファイルに対応しており、MMSメッセージに1つのマルチメディア資産を添付することができる。


\[picture] ： {% image_buster /assets/img/sms/MMS.png %}
[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement
