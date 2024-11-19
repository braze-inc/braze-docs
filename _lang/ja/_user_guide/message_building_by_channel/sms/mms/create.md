---
nav_title: MMSキャンペーンの作成
article_title: MMSキャンペーンの作成
page_order: 2
description: "このリファレンス記事では、MMS メッセージの作成、送信、およびプレビューに関連するステップについて説明します。"
page_type: reference
tool:
  - Campaigns
channel:
  - MMS
search_rank: 1  
---

# MMSキャンペーンを作成する

> この記事には、SMSコンポーザーの一部であるMMSコンポジション特有の情報が含まれている。SMS/MMSコンポーザーの詳細については、[SMSコンポーザーを]({{site.baseurl}}/user_guide/message_building_by_channel/sms/create/)参照のこと。

## MMS送信の基本

### 購読グループの選択

MMSが有効な電話番号を持つサブスクリプショングループを指定する必要があります（ショートコードまたはロングコードのいずれか）。

### メッセージ本文の入力

メディアライブラリーからPNG、JPEG、GIF、およびVCF画像タイプを入力するか、URLを指定します。画像は1枚のみサポートされる。

### MMS 送信に関する知識

MMSは、テキストのみのSMSとは異なる料金で請求され、すべてのキャリアがMMSを受け入れるわけではない。これらの場合、TwilioはMMSを自動的にユーザーがクリックできる画像リンクに変換します。

### 連絡先カードを使う

連絡先カード（vCardまたはVirtual Contact Files (vcf)として知られることもある）は、ビジネス情報や連絡先情報を送信するための標準化されたファイル形式で、アドレス帳や連絡帳に簡単にインポートすることができる。これらのカードは[プログラムで](https://www.twilio.com/blog/send-vcard-twilio-sms)作成し、Brazeメディアライブラリーにアップロードすることも、内蔵の[連絡先カードジェネレーターで]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/contact_card/)作成することもできる。

## MMSメッセージの作成

MMSメッセージを作成するには、サブスクリプショングループをMMS送信用に設定する必要があります。これは、サブスクリプショングループを選択するときにMMSタグが表示されることで示されます。MMS対応サブスクリプショングループを選択すると、画像写真のアップロード、画像URLの参照、または連絡先カードを含めるイネーブルメントができる。

![]({% image_buster /assets/img/sms/mms_composer.png %}) "メッセージ作成画面 "タブでメッセージを書く。

### 画像の仕様

| **画像の仕様** | **推奨プロパティ** |
|--------------------------|----------------------------|
| サイズ                     | 600KBまで        |
| ファイルの種類               | PNG、JPEG、GIF             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## MMSメッセージのプレビュー

Brazeは、メッセージ作成画面の**プレビュー**パネルにアップロードした画像のプレビューを提供します。 

{% alert note %}
SMS/MMSアセットの順序はカスタマイズできません。順序は、このメッセージを受信する電話機によって異なります。
{% endalert %}

![次の旅行の準備をしよう！！」というメッセージの例。プレビューには、テキストとして送信されたメッセージと画像が表示される。]({% image_buster /assets/img/sms/mms_preview.png %})
