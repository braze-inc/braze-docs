---
nav_title: メディアライブラリ
article_title: メディアライブラリ
page_order: 0
page_type: reference
description: "この参考記事では、メディアライブラリについて説明します。ここでは、アセットを1か所で一元管理する方法、AI を使用して画像を生成する方法、メッセージコンポーザーでメディアにアクセスする方法を学ぶことができます。"
tool: Media

---

# メディアライブラリ

> メディアライブラリを使用すると、アセットを1か所で一元管理できます。 

## メディアライブラリとCDN

コンテンツデリバリネットワーク (CDN) の代わりにメディアライブラリを使用すると、アプリ内メッセージのキャッシュとパフォーマンスが向上します。アプリ内メッセージで見つかったすべてのメディアライブラリアセットは、より速く表示できるように事前にキャッシュされ、オフラインで表示できるようになります。さらに、メディアライブラリは Braze コンポーザーと統合されているため、マーケターは画像のURLをコピーして貼り付けるのではなく画像を選択またはタグ付けできます。

## メディアライブラリにアクセスする

メディアライブラリー内では、アセットの種類、サイズ、寸法、URL、ライブラリーに追加された日付、その他の情報を確認できる。Braze メディアライブラリにアクセスするには、[THIS] > [**テンプレート**] に移動します。次の操作を実行できます。

* 複数の画像を一度にアップロードする
* 仮想連絡先ファイル (.vcf) をアップロードする
* WhatsApp メッセージで使用する動画ファイルのアップロード
* 画像を含むフォルダーをアップロードする (最大50画像)
* [AI を使用して画像を生成し](#generate-ai)、メディアライブラリに保存する
* 既存の画像をトリミングして、メッセージに適した比率にする
* タグやチームを追加して、画像をさらに整理しやすくする
* メディアライブラリグリッドでタグまたはチームで検索する
* アップロードする画像またはフォルダーをドラッグ＆ドロップする
* 画像を削除する

![メディアライブラリページ。ファイルをドラッグ＆ドロップしてアップロードするための [ライブラリにアップロード] セクションがあります。メディアライブラリには、アップロードされたコンテンツのリストもあります。]({% image_buster /assets/img_archive/media_library_main.png %})

後で Braze でメッセージの下書きを作成するときに、メディアライブラリから画像を取り込むことができます。

![メディアライブラリにアクセスするための一般的な 2 つの方法 (メッセージ作成画面によって異なる)。そのうちの1つでは、「画像とGIF」というタイトルの付いたメールドラッグ＆ドロップエディターと「メディアライブラリから追加」ボタンが表示されます。もう1 つは、プッシュおよびアプリ内メッセージs などの標準エディタと、タイトル"Media"ボタンから"Add Image"を表示します。]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} メディアライブラリーの詳細については、[テンプレート&メディアFAQ]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs)を参照してください。 {% endalert %}

## 画像の仕様

メディアライブラリにアップロードされるすべての画像は5 MB 未満でなければなりません。サポートされているファイルタイプはPNG、JPEG、GIF、SVGである。メッセージングチャネル別の特定の推奨画像については、次のセクションを参照してください。

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

メディアライブラリにアップロードされた動画は、今のところWhatsAppメッセージでのみ使用できる。詳細については、[WhatsApp メッセージを作成する]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages)を参照してください。

## BrazeAI<sup>TM</sup> で画像写真を生成する {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
この機能を使用する前に、[あなたのデータがどのように使用され、OpenAI に送信されるか]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy)をご確認ください。
{% endalert %}
