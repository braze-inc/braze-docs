---
nav_title: 連絡先カード
article_title: コンタクトカード
page_order: 3
description: "この参考記事では、MMSやSMSメッセージに含める連絡先カードの作成方法について説明する。"
page_type: reference
channel:
  - MMS
  
---

# 連絡先カード 

> 連絡先カードは vCard または仮想連絡先ファイル (VCF) とも呼ばれ、アドレス帳や連絡先一覧に簡単にインポートできるビジネス情報や連絡先情報を送信するために標準化されたファイル形式です。 

コンタクトカードは、[プログラムで](https://www.twilio.com/blog/send-vcard-twilio-sms)作成し、Braze [メディアライブラリー]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library)にアップロードするか、当社の内蔵コンタクトカードジェネレーターで作成することができます。これらのカードには、会社名、電話番号、住所、電子メール、小さな写真などの一般的なプロパティを割り当てることができる。連絡先カードの作成を開始するには、まず、Braze で MMS を使用するように設定してください。

## 連絡先カードジェネレーター

<script src="https://fast.wistia.com/embed/medias/7m77mdfr4y.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_7m77mdfr4y videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/7m77mdfr4y/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

### ステップ 1:名前の割り当て

連絡先カードは、SMS および MMS の作成画面で作成できます。開始するには、[**連絡先カードジェネレーター**] タブを選択します。

次に、会社名またはニックネームを入力するよう求められる。これは、ユーザーがカードを保存するときに表示される名前である。ユーザーが連絡先やメッセージングアプリであなたの会社名や別名をすべて確認できるように、20文字の制限が設けられている。 

![]({% image_buster /assets/img/sms/contact_card1.png %}){: style="max-width:60%" }

### ステップ2:電話番号の割り当て

利用可能なドロップダウンオプションから、サブスクリプショングループと希望する電話番号を選択します。この番号はお客様の連絡先カードに記載され、保存後に購読グループ側の電話からテキスト送信ができます。

英数字コードは双方向メッセージングと互換性がなく、連絡先カードではサポートされていません。

### ステップ 3:任意項目

![]({% image_buster /assets/img/sms/contact_card2.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

#### 連絡先カードの連絡先写真をアップロードする

連絡先カードのオプションのサムネイル連絡先写真をアップロードできます。240×240pxのJPEGまたはPNG画像を推奨する。アップロードされた高解像度の画像は、5MBを超えるMMSメッセージは失敗する可能性があるため、メッセージの配信性を確保するために240×240pxにリサイズされる。

#### 追加情報

その他のフィールドには、名前、小見出し、住所など、ユーザーが利用可能にしたい連絡先情報を挿入できる。 

### ステップ 4:連絡先カードの保存

必須フィールドにすべて入力したら、[**連絡先カードを作成**] をクリックします。これにより、連絡先カードが自動的にキャンペーンまたはキャンバスに添付されます。ここから、メッセージの追加、連絡先カードのテスト、およびキャンペーンまたはキャンバスの開始ができます。

また、コンタクトカードは[メディアライブラリー]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library)に保存され、今後のキャンペーンやキャンバスで簡単に再利用できます。

## 既存の連絡先カードを追加する

既存の連絡先カードを追加するには、キャンペーンまたはキャンバスを作成して、目的の購読グループを選択します。次に、メッセージ作成画面に [**メディアを追加**] オプションが表示されます。ここでは、既存の連絡先カードファイルをアップロードするか、メディアライブラリから見つけることができます。
