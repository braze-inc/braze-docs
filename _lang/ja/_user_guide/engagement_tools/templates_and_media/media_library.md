---
nav_title: メディアライブラリ
article_title: メディアライブラリ
page_order: 0
page_type: reference
description: "この参考記事では、メディアライブラリについて説明します。ここでは、資産を一元管理する方法、AIで画像を生成する方法、メッセージ作成画面でメディアにアクセスする方法を学べる。"
tool: Media

---

# メディアライブラリ

> メディアライブラリを使用すると、アセットを1か所で一元管理できます。 

## メディアライブラリー対CDN

コンテンツデリバリネットワーク (CDN) の代わりにメディアライブラリを使用すると、アプリ内メッセージのキャッシュとパフォーマンスが向上します。アプリ内メッセージで見つかったすべてのメディアライブラリアセットは、より速く表示できるように事前にキャッシュされ、オフラインで表示できるようになります。さらに、メディアライブラリは Braze コンポーザーと統合されているため、マーケターは画像のURLをコピーして貼り付けるのではなく画像を選択またはタグ付けできます。

## メディアライブラリにアクセスする

メディアライブラリー内では、アセットの種類、サイズ、寸法、URL、ライブラリーに追加された日付、その他の情報を確認できる。Braze メディアライブラリにアクセスするには、[**テンプレート**] > [**メディアライブラリ**] に移動します。次の操作を実行できます。

* 複数の画像を一度にアップロードする
* 仮想連絡先ファイル (.vcf) をアップロードする
* WhatsApp メッセージで使用する動画ファイルのアップロード
* 画像が入ったフォルダをアップロードせよ（最大50枚まで）
* [AI を使用して画像を生成し](#generate-ai)、メディアライブラリに保存する
* 既存の画像をトリミングして、メッセージに適した比率にする
* タグやチームを追加して、画像をさらに整理しやすくする
* メディアライブラリグリッドでタグまたはチームで検索する
* アップロードする画像またはフォルダーをドラッグ＆ドロップする
* 画像を削除する

![メディアライブラリページ。ファイルをドラッグ＆ドロップしてアップロードするための [ライブラリにアップロード] セクションがあります。メディアライブラリには、アップロードされたコンテンツのリストもあります。]({% image_buster /assets/img_archive/media_library_main.png %})

後で、Brazeでメッセージの下書きを行う際に、メディアライブラリーから画像を取り込むことができる。

![メディアライブラリにアクセスするための一般的な 2 つの方法 (メッセージ作成画面によって異なる)。そのうちの1つでは、「画像とGIF」というタイトルの付いたメールドラッグ＆ドロップエディターと「メディアライブラリから追加」ボタンが表示されます。もう一方には、標準的な編集機能（プッシュ通知やアプリ内メッセージなど）が表示されている。タイトルは「メディア」で、「画像, 写真を追加」ボタンが付いている。]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} メディアライブラリーに関する詳細情報は、[テンプレート &メディア FAQ]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs) を参照せよ。 {% endalert %}

## 画像の仕様

メディアライブラリにアップロードされるすべての画像は5 MB 未満でなければなりません。サポートされているファイル形式はPNG、JPEG、GIF、SVG、WebPである。メッセージングチャネル別の特定の推奨画像については、次のセクションを参照してください。

{% alert important %}
非常に細長い形状のGIF（例えば3000×2ピクセル）や、300フレーム以上のGIFは、ファイルサイズが小さくてもアップロードに失敗する可能性がある。
{% endalert %}

### コンテンツカード

{% multi_lang_include image_specs.md variable_name='content cards' %}

### メール

{% multi_lang_include image_specs.md variable_name="email"  %}

### アプリ内メッセージ

{% multi_lang_include image_specs.md variable_name="in-app messages"  %}

詳しくは、[アプリ内メッセージクリエイティブの詳細]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/)をご覧ください。

### プッシュ通知

{% multi_lang_include image_specs.md variable_name="push notifications"  %}

{% alert note %}
その他のリソースについては、[プッシュ画像、テキストの仕様を]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)参照のこと。
{% endalert %}

### 動画

メディアライブラリーにアップロードされた動画は、WhatsAppメッセージでのみ使用できる。詳細については、[WhatsAppメッセージの作成]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages)を参照せよ。

## BrazeAI<sup>TM</sup> で画像写真を生成する {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
この機能を使用する前に、[あなたのデータがどのように使用され、OpenAI に送信されるか]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy)をご確認ください。
{% endalert %}
