---
nav_title: コンタクトカード
article_title: コンタクトカード
page_order: 3
description: "この参考記事では、MMSやSMSメッセージに含める連絡先カードの作成方法について説明します。"
page_type: reference
channel:
  - MMS
  
---

# コンタクトカード 

> コンタクトカード（vCardまたはVirtual Contact Files (VCF)として知られることもある）は、アドレス帳や連絡帳に簡単にインポートできる、ビジネス情報や連絡先情報を送信するための標準化されたファイル形式です。 

コンタクトカードは、[プログラムで](https://www.twilio.com/blog/send-vcard-twilio-sms)作成し、Braze[メディアライブラリに]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library)アップロードするか、内蔵のコンタクトカードジェネレーターで作成することができます。これらのカードには、会社名、電話番号、住所、電子メール、小さな写真などの一般的なプロパティを割り当てることができます。連絡先カードを作成するには、まずBrazeでMMSを使用するように設定してください。

## 連絡先カードジェネレーター

<script src="https://fast.wistia.com/embed/medias/7m77mdfr4y.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_7m77mdfr4y videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;">(+<img src="https://fast.wistia.com/embed/medias/7m77mdfr4y/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" />)</div></div></div></div>

### ステップ 1:名前を割り当てる

コンタクトカードは、SMSおよびMMSコンポーザーから作成できます。**コンタクトカードジェネレータタブを**選択し、開始します。

次に、会社名またはニックネームを入力するよう求められます。これは、ユーザーがカードを保存するときに表示される名前です。ユーザーが連絡先やメッセージアプリで会社名や別名をすべて確認できるように、20文字の制限が設けられています。 

![\]({% image_buster /assets/img/sms/contact_card1.png %}){: style="max-width:60%" }

### ステップ 2:電話番号の割り当て

利用可能なドロップダウンオプションから、購読グループと希望する電話番号を選択します。この番号はあなたの連絡先カードに記載され、保存された後、相手の携帯電話からメールできるようになります。

英数字コードは双方向メッセージには対応しておらず、コンタクトカードには対応していませんのでご注意ください。

### ステップ 3:オプション

![\]({% image_buster /assets/img/sms/contact_card2.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

**コンタクトカード コンタクト写真**<br>
連絡先カードにサムネイル写真をアップロードできます。240×240pxのJPEGまたはPNG画像を推奨します。アップロードされた高解像度の画像は、5MBを超えるMMSメッセージは失敗する可能性があるため、メッセージの配信性を確保するために240×240pxにリサイズされます。

**その他の情報**<br>
その他のフィールドには、名前、小見出し、住所など、ユーザーが手元に置いておきたい連絡先情報を挿入できます。 

<br>

### ステップ 4: 連絡先カードの保存

必要なフィールドをすべて入力したら、「**連絡先カードを作成**」をクリックすると、キャンペーンまたはキャンバスに自動的に添付されます。ここから、メッセージを追加したり、コンタクトカードをテストしたり、キャンペーンやキャンバスを立ち上げることができます。

連絡先カードは[メディアライブラリにも]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library)保存され、今後のキャンペーンやキャンバスで簡単に再利用できます。

## 既存の連絡先カードを追加する

既存の連絡先カードを追加するには、キャンペーンまたはキャンバスを作成し、希望の購読グループを選択します。次に、**メディアを追加する**オプションがメッセージ作成ウィンドウに表示されます。ここでは、既存の連絡先カードファイルをアップロードするか、メディアライブラリから見つけることができます。
