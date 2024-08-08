---
nav_title: MMS キャンペーンの作成
article_title: MMS キャンペーンの作成
page_order: 2
description: "このリファレンス記事では、MMS メッセージの作成、送信、およびプレビューに関連する手順について説明します。"
page_type: reference
tool:
  - Campaigns
channel:
  - MMS
search_rank: 1  
---

# MMS キャンペーンの作成

> このページには、SMS コンポーザーの一部である MMS 作成に固有の情報のみが含まれています。SMS/MMS コンポーザーの詳細については、[SMS Composer][1] を参照してください。

## MMS 送信の基本

BrazeでMMSを送信する:

- **サブスクリプション グループを選択する**
  - MMS 対応の電話番号を持つサブスクリプション グループをターゲットに指定する必要があります (ショート コードまたはロング コードにすることができます)。<br><br>
- **入力メッセージ本文**
  - メディアライブラリからPNG、JPEG、GIF、VCF画像タイプを入力するか、URLを指定します。
  - サポートされている画像は 1 つだけです<br><br>
- **MMS の送信について**
  - MMS は、テキストのみの SMS とは異なるレートで課金されます。
  - すべての携帯通信会社が MMS を利用できるわけではありません。このような場合、TwilioはMMSをユーザーがクリックできる画像リンクに自動的に変換します。

### 連絡先カード

連絡先カード (vCard または仮想連絡先ファイル (vcf) とも呼ばれます) は、アドレス帳や連絡先帳に簡単にインポートできる、勤務先情報や連絡先情報を送信するための標準化されたファイル形式です。これらのカードは、 [プログラムで](https://www.twilio.com/blog/send-vcard-twilio-sms) 作成してBrazeメディアライブラリにアップロードするか、組み込みの [連絡先カードジェネレーター]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/contact_card/)を使用して作成できます。

## MMS メッセージの作成

MMS メッセージを作成するには、サブスクリプション グループを MMS 送信用に構成する必要があります。これは、サブスクリプション グループを選択するときに MMS タグが表示されることで示されます。MMS 対応のサブスクリプション グループを選択すると、画像をアップロードしたり、画像の URL を参照したり、連絡先カードを含めたりできるようになります。

![][2]

### 画像の仕様

**画像仕様** | **推奨プロパティ**
--- | ---
サイズ |最大 5 MB
ファイルの種類 |PNG、JPEG、GIF
{: .reset-td-br-1 .reset-td-br-2}

## MMS メッセージのプレビュー

Braze は、メッセージコンポーザーの **プレビュー** パネルにアップロードした画像のプレビューを提供します。 

{% alert note %}
SMS/MMS アセットの順序はカスタマイズできません。順序は、このメッセージを受信する電話機によって異なります。
{% endalert %}

![][3]


[1]: {{ site.baseurl }}/user_guide/message_building_by_channel/sms/create/
[2]: {% image_buster /assets/img/sms/mms_composer.png %}
[3]: {% image_buster /assets/img/sms/mms_preview.png %}
[4]: {% image_buster /assets/img/sms/contact_card1.png %}
[5]: {% image_buster /assets/img/sms/contact_card2.png %}
