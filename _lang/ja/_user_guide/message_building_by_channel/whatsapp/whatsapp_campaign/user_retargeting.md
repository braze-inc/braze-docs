---
nav_title: ユーザーのリターゲット
article_title: ユーザーのリターゲット
page_order: 1
description: "このリファレンス記事では、ユーザがWhatsApp インタラクションによってメッセージを再ターゲットする方法について説明します。"
page_type: reference
channel:
  - WhatsApp
page_order: 4.1

---

# ユーザーのリターゲット 

> ユーザのサブスクリプション状態の変更に加えて、Braze は、メッセージをフィルタリングおよびトリガするためのユーザプロファイルとのやり取りも記録します。<br><br>これらのフィルタとトリガを使用すると、WhatsApp メッセージを受信したユーザ、または特定のWhatsApp キャンペーンまたはキャンバスステップからWhatsApp メッセージを受信したユーザをフィルタリングできます。

## リターゲットオプション

{% alert note %}
ユーザーのリターゲットを使用してオーディエンスを構築する場合は、ユーザーの好みに基づいて特定のユーザーを含めるか除外し、CCPA の下での「販売または共有しない」権限などのプライバシーに関する法律を順守する必要があります。マーケターは、キャンバスおよび/またはキャンペーン登録基準内で、ユーザーの適格性に関連するフィルタを実装する必要があります。
{% endalert %}

### WhatsAppによるユーザーのフィルタリング

ユーザは、WhatsApp を最後に受信したとき、または特定のWhatsApp キャンペーンからWhatsApp を受信したときによってフィルタリングできます。フィルタは、キャンペーンビルダのTarget Users ステップで設定できます。

**最後に受信したWhatsAppによるフィルタ**<br>
![][5]{: style="max-width:75%"}

**WhatsAppキャンペーンから受信したメッセージでフィルタリングする**<br>
特定のWhatsApp キャンペーンからメッセージを受信したユーザーをフィルタリングします。このフィルタを使用すると、WhatsApp キャンペーンからメッセージを受信していないものをフィルタリングすることもできます。<br>
![][4]

### エンゲージメントによるフィルタリング
WhatsApp キャンペーンまたはキャンバスステップを持っているか、持っていないユーザを再ターゲットします。 

**特定のWhatsApp Campaignを開いた/読み込んだユーザーを再ターゲットする**
1\.**Clicked/Opened Campaign**フィルタを使用してセグメントを作成します。
2\.**WhatsAppメッセージを読み取る**を選択します。
3\.目的のキャンペーンを選択します。<br>

![][3]

**特定のCanvas Step を開いた/読み込んだユーザーをリターゲットする**
1\.**Clicked/Opened Step**フィルタを使用してセグメントを作成します。
2\.**WhatsAppメッセージを読み取る**を選択します。
3\.目的のキャンバスステップとキャンバスステップを選択します。<br>

![][2]

**キャンペーンまたはキャンバス属性によるフィルタ**<br>
特定のWhatsApp キャンペーンまたはCanvas コンポーネントまたはタグを開いた/読み込んだユーザのフィルタ。
![][1]

[1]: {% image_buster /assets/img/whatsapp/whatsapp19.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp20.png %}
[3]: {% image_buster /assets/img/whatsapp/whatsapp21.png %}
[4]: {% image_buster /assets/img/whatsapp/whatsapp22.png %}
[5]: {% image_buster /assets/img/whatsapp/whatsapp23.png %} 
