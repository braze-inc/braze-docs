---
nav_title: MMSキャンペーンを作成する
article_title: MMSキャンペーンの作成
page_order: 2
description: "このリファレンス記事では、MMS メッセージの作成、送信、およびプレビューに関連するステップについて説明します。"
page_type: reference
alias: /create_mms_message/
tool:
  - Campaigns
channel:
  - MMS
search_rank: 1  
---

# MMSキャンペーンを作成する

> この記事には、SMSコンポーザーの一部であるMMSコンポジション特有の情報が含まれている。SMS / MMS 作成画面の詳細については、[SMS 作成画面]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/create/)を参照してください。

## MMS送信の基本

### 購読グループの選択

MMSが有効な電話番号を持つサブスクリプショングループを指定する必要があります（ショートコードまたはロングコードのいずれか）。

### メッセージ本文の入力

メディアライブラリーからPNG、JPEG、GIF、およびVCF画像タイプを入力するか、URLを指定します。サポートされる画像は1枚のみです。

### MMS 送信に関する知識

MMSは、テキストのみのSMSとは異なる料金で請求され、すべてのキャリアがMMSを受け入れるわけではない。これらの場合、TwilioはMMSを自動的にユーザーがクリックできる画像リンクに変換します。

### 連絡先カードを使う

連絡先カードは vCard または仮想連絡先ファイル (VCF) とも呼ばれ、アドレス帳や連絡先一覧に簡単にインポートできるビジネス情報や連絡先情報を送信するために標準化されたファイル形式です。これらのカードは[プログラムで](https://www.twilio.com/blog/send-vcard-twilio-sms)作成して Braze メディアライブラリにアップロードするか、または組み込みの[連絡先カードジェネレーター]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/)を使用して作成できます。

## MMSメッセージの作成

MMSメッセージを作成するには、サブスクリプショングループをMMS送信用に設定する必要があります。これは、サブスクリプショングループを選択するときにMMSタグが表示されることで示されます。MMS 対応の購読グループを選択すると、画像のアップロード、画像 URL の参照、連絡先カードの取り込みができるようになります。

!["Compose"タブでメッセージを書きます。]({% image_buster /assets/img/sms/mms_composer.png %}){: style="max-width:80%;"}

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

![メッセージ"ジムを打つ準備ができました。。。自宅で?"の例。プレビューには、テキストとして送信されたメッセージと"画像が表示されます。]({% image_buster /assets/img/sms/mms_preview.png %})
