---
nav_title: 連絡先カード
article_title: コンタクトカード
page_order: 3
description: "このリファレンス記事では、MMS およびSMS メッセージに含める連絡先カードを作成する方法について説明します。"
page_type: reference
channel:
  - MMS
  
---

# コンタクトカード 

> コンタクトカード(vCard またはVirtual Contact Files(VCF)とも呼ばれます)は、ビジネスおよびコンタクト情報を送信するための標準化されたファイル形式で、アドレス帳またはコンタクトブックに簡単にインポートできます。 

コンタクトカードは、[プログラムで作成し、Braze [メディアライブラリー]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library)にアップロードするか、当社の内蔵コンタクトカードジェネレーターで作成することができます。これらのカードには、会社名、電話番号、住所、電子メール、小さな写真などの一般的なプロパティを割り当てることができる。コンタクトカードの作成を開始するには、まず、ブレーズでMMS を使用するように設定されていることを確認します。

## コンタクトカード発生器

<script src="https://fast.wistia.com/embed/medias/7m77mdfr4y.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_7m77mdfr4y videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/7m77mdfr4y/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

### ステップ 1:名前の割り当て

コンタクトカードは、SMSおよびMMSコンポーザーから作成できます。開始するには、[**連絡先カードジェネレーター**] タブを選択します。

次に、会社名またはニックネームを入力するよう求められる。これは、ユーザーがカードを保存するときに表示される名前である。ユーザーが連絡先やメッセージングアプリであなたの会社名や別名をすべて確認できるように、20文字の制限が設けられている。 

![]({% image_buster /assets/img/sms/contact_card1.png %}){: style="max-width:60%" }

### ステップ2:電話番号の割り当て

利用可能なドロップダウンオプションから、サブスクリプショングループと希望する電話番号を選択します。この番号は、連絡先カードにリストされ、保存後に電話機でテキストとして使用できます。

英数字コードは双方向メッセージングと互換性がないため、コンタクトカードではサポートされていません。

### ステップ 3:任意項目

![]({% image_buster /assets/img/sms/contact_card2.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

#### コンタクトカードの連絡先写真をアップロードする

連絡先カードのオプションのサムネイル連絡先写真をアップロードできます。240×240pxのJPEGまたはPNG画像を推奨する。アップロードされた高解像度の画像は、5MBを超えるMMSメッセージは失敗する可能性があるため、メッセージの配信性を確保するために240×240pxにリサイズされる。

#### 追加情報

その他のフィールドでは、名前、サブヘッダー、住所、およびユーザーが使用可能にしたいその他の連絡先情報を挿入できます。 

### ステップ 4:連絡先カードの保存

必須フィールドにすべて入力したら、[**連絡先カードを作成**] をクリックします。これにより、連絡先カードが自動的にキャンペーンまたはキャンバスに添付されます。ここから、メッセージを追加したり、コンタクトカードをテストしたり、キャンペーンまたはキャンバスを起動したりできます。

また、コンタクトカードは[メディアライブラリー]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library)に保存され、今後のキャンペーンやキャンバスで簡単に再利用できます。

## 既存の連絡先カードを追加する

既存のコンタクトカードを追加するには、キャンペーンまたはキャンバスを作成し、目的のサブスクリプショングループを選択します。次に、メッセージ作成画面に [**メディアを追加**] オプションが表示されます。ここでは、既存のコンタクトカードファイルをアップロードするか、メディアライブラリーを介して見つけることができます。
