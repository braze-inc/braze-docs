---
nav_title: 連絡先カード
article_title: 連絡先カード
page_order: 3
description: "この参考記事では、MMSやSMSメッセージに含める連絡先カードの作成方法について説明する。"
page_type: reference
channel:
  - MMS
  
---

# 連絡先カード 

> 連絡先カード（vCardまたはVirtual Contact Files (VCF)として知られることもある）は、アドレス帳や連絡帳に簡単にインポートできる、ビジネス情報や連絡先情報を送信するための標準化されたファイル形式である。 

コンタクトカードは、[プログラムで](https://www.twilio.com/blog/send-vcard-twilio-sms)作成し、Braze[メディアライブラリに]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library)アップロードすることも、内蔵のコンタクトカードジェネレーターで作成することもできる。これらのカードには、会社名、電話番号、住所、電子メール、小さな写真などの一般的なプロパティを割り当てることができる。連絡先カードを作り始めるには、まずBrazeでMMSを使えるように設定しておく。

## コンタクトカード・ジェネレーター

<script src="https://fast.wistia.com/embed/medias/7m77mdfr4y.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_7m77mdfr4y videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/7m77mdfr4y/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

### ステップ 1:名前を割り当てる

コンタクトカードはSMSやMMSコンポーザーから作成できる。**Contact Card Generator**タブを選択して開始する。

次に、会社名またはニックネームを入力するよう求められる。これは、ユーザーがカードを保存するときに表示される名前である。ユーザーが連絡先やメッセージングアプリであなたの会社名や別名をすべて確認できるように、20文字の制限が設けられている。 

![]({% image_buster /assets/img/sms/contact_card1.png %}){: style="max-width:60%" }

### ステップ2:電話番号を割り当てる

利用可能なドロップダウンオプションから、契約グループと希望する電話番号を選択する。この番号は、あなたの連絡先カードに記載され、保存された後、相手の携帯電話でテキスト送信できるようになる。

英数字コードは双方向メッセージには対応しておらず、コンタクトカードには対応していない。

### ステップ 3:任意項目

![]({% image_buster /assets/img/sms/contact_card2.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

**コンタクトカード コンタクト写真**<br>
オプションで、連絡先カードの連絡先サムネイル写真をアップロードできる。240×240pxのJPEGまたはPNG画像を推奨する。アップロードされた高解像度の画像は、5MBを超えるMMSメッセージは失敗する可能性があるため、メッセージの配信性を確保するために240×240pxにリサイズされる。

**その他の情報**<br>
その他のフィールドには、名前、小見出し、住所など、ユーザーが手元に置いておきたい連絡先情報を挿入できる。 

<br>

### ステップ 4:連絡先カードを保存する

必要なフィールドをすべて入力したら、「**連絡先カードを作成**」をクリックする。ここから、メッセージを追加し、コンタクトカードをテストし、キャンペーンやキャンバスを立ち上げることができる。

連絡先カードは[メディアライブラリにも]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library)保存され、今後のキャンペーンやキャンバスで簡単に再利用できる。

## 既存の連絡先カードを追加する

既存のコンタクトカードを追加するには、キャンペーンまたはキャンバスを作成し、希望の購読グループを選択する。次に、**メディアを追加する**オプションがメッセージ作成ウィンドウに表示される。ここでは、既存の連絡先カードファイルをアップロードするか、メディアライブラリから見つけることができる。
