---
nav_title: MMSキャンペーンの作成
article_title: MMSキャンペーンの作成
page_order: 2
description: "この記事では、MMSメッセージの作成、送信、プレビューの手順について説明します。"
page_type: reference
tool:
  - Campaigns
channel:
  - MMS
search_rank: 1  
---

# MMSキャンペーンの作成

> このページには、SMS作成ツールの一部であるMMS作成に特化した情報のみが含まれています。SMS/MMS作曲家の詳細については、\[SMS Composer][1]をご覧ください。

## MMS送信の基本

BrazeでMMSを送信する:

- **サブスクリプショングループを選択してください**
  - MMSが有効な電話番号を持つサブスクリプショングループを指定する必要があります（ショートコードまたはロングコードのいずれか）。<br><br>
- **入力メッセージ本文**
  - メディアライブラリーからPNG、JPEG、GIF、およびVCF画像タイプを入力するか、URLを指定します。
  - 画像1枚のみ対応<br><br>
- ** MMS送信を理解する **
  - MMSはテキストのみのSMSとは異なる料金で請求されます。
  - すべてのキャリアがMMSを受け入れるわけではありません。これらの場合、TwilioはMMSを自動的にユーザーがクリックできる画像リンクに変換します。

### 連絡先カード

連絡先カード（vCardまたは仮想連絡先ファイル（vcf）として知られることもあります）は、アドレス帳や連絡先帳に簡単にインポートできるビジネスおよび連絡先情報を送信するための標準化されたファイル形式です。これらのカードは[プログラムで](https://www.twilio.com/blog/send-vcard-twilio-sms)作成してBrazeメディアライブラリーにアップロードするか、組み込みの[連絡先カードジェネレーター]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/contact_card/)を使用して作成できます。

## MMSメッセージの作成

MMSメッセージを作成するには、サブスクリプショングループをMMS送信用に設定する必要があります。これは、サブスクリプショングループを選択するときにMMSタグが表示されることで示されます。MMS対応のサブスクリプショングループを選択すると、画像をアップロードしたり、画像URLを参照したり、連絡先カードを含めたりすることができます。

![][2]

### 画像の仕様

**画像の仕様** | **おすすめのプロパティ**
--- | ---
サイズ | 最大600KB
ファイルタイプ | PNG、JPEG、GIF
{: .reset-td-br-1 .reset-td-br-2}

## MMSメッセージのプレビュー

Brazeは、メッセージ作成画面の**プレビュー**パネルにアップロードした画像のプレビューを提供します。 

{% alert note %}
SMS/MMSアセットの順序はカスタマイズできません。このメッセージを受信する電話に依存します。
{% endalert %}

![][3]


[1]: {{ site.baseurl }}/user_guide/message_building_by_channel/sms/create/
[2]: {% image_buster /assets/img/sms/mms_composer.png %}
[3]: {% image_buster /assets/img/sms/mms_preview.png %}
[4]: {% image_buster /assets/img/sms/contact_card1.png %}
[5]: {% image_buster /assets/img/sms/contact_card2.png %}
