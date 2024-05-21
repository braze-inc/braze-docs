---
nav_title: "MMSについて"
article_title: MMSについて
page_order: 0
description: "このリファレンス記事では、MMS メッセージの概要と MMS チャネルの一般的なユース ケースについて説明します。"
page_type: reference
channel:
  - MMS
search_rank: 2  
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"}MMS メッセージについて

> MMSはマルチメディアメッセージサービスとも呼ばれ、マルチメディアアセット(JPEG、GIF、PNG)を含むメッセージを携帯電話に送信するために使用されます。<br><br>SMSと同様に、MMSは緊急性の高いメッセージングチャネルであり、他のチャネルでは不可能な方法で顧客とすぐにコミュニケーションをとることができます。ただし、MMS は、テキストのみの SMS にメディアを追加する機能を提供することで、SMS の機能を拡張します。

## 想定されるユースケース

|ユースケース |解説 |
| --- | --- |
|プロモーション |視認性の高いSMSキャンペーンでユーザーにリーチするだけでなく、MMSのメディア面を活用して、提供する商品で購入者を惹きつけます。|
|リエンゲージメントキャンペーン |SMSの受信をオプトインした顧客を、他のすべてのチャネルで呼び戻せなかった場合に再エンゲージします。|
{: .reset-td-br-1 .reset-td-br-2}

## MMSについて知る

### MMS の可用性

米国とカナダのほとんどの通信事業者は、顧客の電話でのマルチメディアアセットの受信と表示をサポートしています。国際通信事業者の場合、Brazeは、サポートされている米国またはカナダの電話番号から送信されたMMSメッセージを、MMSをサポートしていない宛先にのみ自動的に変換します。これらのメッセージの場合、Brazeは添付されたメディアを、ファイルにリンクする短いURLをメッセージ本文に追加して置き換えます。

### サブスクリプショングループ

[サブスクリプション グループ][1] は、特定の種類のメッセージング目的で使用される送信電話番号 (ショート コード、ロング コード、英数字の送信者 ID) のコレクションです。サブスクリプション グループには、MMS が有効になっている電話番号が必要です。この機能の有効化については、Brazeのアカウントマネージャーにご相談ください。

### MMS メッセージの制限とスループット

MMS の場合、メッセージの制限は 5 MB です (これには、マルチメディア資産とメッセージ本文のサイズが含まれます)。安全のために、Brazeはマルチメディアアセットに600KBを超えないようにし、メッセージ本文を含めることを推奨しています。

MMS のスループットは、ロング コードによる 1 秒あたり 1 セグメントです。

### インバウンド MMS

ユーザーがメディアアイテムを含む受信メッセージを送信すると、Braze は Liquid タグを通じて Currents と Liquid でメディアアイテムの URL を公開します {%raw%}`{{sms.${inbound_media_url}}}`{%endraw%}

### 使用可能なファイルタイプ:

Brazeは、JPEG、GIF、PNG、およびVCFファイルを受け入れ、MMSメッセージに単一のマルチメディアアセットを添付できます。


[写真]: {% image_buster /assets/img/sms/MMS.png %}
[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement
