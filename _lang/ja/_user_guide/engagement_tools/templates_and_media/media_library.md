---
nav_title: メディアライブラリー
article_title: メディアライブラリー
page_order: 0
page_type: reference
description: "この参考記事では、メディアライブラリーについて説明します。ここでは、アセットを一元管理する方法、AIで画像を生成する方法、メッセージ作成画面でメディアにアクセスする方法を学べます。"
tool: Media

---

# メディアライブラリー

> メディアライブラリーを使用すると、アセットを1か所で一元管理できます。 

## メディアライブラリー対CDN

コンテンツデリバリーネットワーク (CDN) の代わりにメディアライブラリーを使用すると、アプリ内メッセージのキャッシュとパフォーマンスが向上します。アプリ内メッセージに含まれるすべてのメディアライブラリーアセットは、より速く表示できるように事前にキャッシュされ、オフラインでも表示できるようになります。さらに、メディアライブラリーは Braze コンポーザーと統合されているため、マーケターは画像のURLをコピーして貼り付ける代わりに、画像を選択またはタグ付けできます。

## メディアライブラリーにアクセスする

メディアライブラリー内では、アセットの種類、サイズ、寸法、URL、ライブラリーに追加された日付、その他の情報を確認できます。Braze メディアライブラリーにアクセスするには、[**テンプレート**] > [**メディアライブラリー**] に移動します。次の操作を実行できます。

* 複数の画像を一度にアップロードする
* 仮想連絡先ファイル (.vcf) をアップロードする
* WhatsApp メッセージで使用する動画ファイルをアップロードする
* 画像が入ったフォルダをアップロードする（最大50枚まで）
* [AI を使用して画像を生成し](#generate-ai)、メディアライブラリーに保存する
* 既存の画像をトリミングして、メッセージに適した比率にする
* タグやチームを追加して、画像をさらに整理しやすくする
* メディアライブラリーグリッドでタグまたはチームで検索する
* アップロードする画像またはフォルダーをドラッグ＆ドロップする
* 画像を削除する

![メディアライブラリーページ。ファイルをドラッグ＆ドロップしてアップロードするための [ライブラリーにアップロード] セクションがあります。メディアライブラリーには、アップロードされたコンテンツのリストもあります。]({% image_buster /assets/img_archive/media_library_main.png %})

後で、Braze でメッセージの下書きを行う際に、メディアライブラリーから画像を取り込むことができます。

![メディアライブラリーにアクセスするための一般的な 2 つの方法 (メッセージ作成画面によって異なる)。そのうちの1つでは、「画像とGIF」というタイトルの付いたメールドラッグ＆ドロップエディターと「メディアライブラリーから追加」ボタンが表示されます。もう一方には、標準的なエディター（プッシュ通知やアプリ内メッセージなど）が表示されています。タイトルは「メディア」で、「画像を追加」ボタンが付いています。]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} メディアライブラリーに関する詳細情報は、[テンプレート＆メディア FAQ]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs) を参照してください。 {% endalert %}

## 画像の仕様

メディアライブラリーにアップロードされるすべての画像は5&nbsp;MB 未満でなければなりません。サポートされているファイル形式はPNG、JPEG、GIF、SVG、WebPです。メッセージングチャネル別の推奨画像については、次のセクションを参照してください。

{% alert important %}
非常に細長い形状のGIF（例えば3000×2ピクセル）や、300フレーム以上のGIFは、ファイルサイズが小さくてもアップロードに失敗する可能性があります。
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

#### 推奨メッセージ長

最良の結果を得るために、プッシュメッセージを作成する際は以下のメッセージ長ガイドラインを参照してください。画像の有無、通知の状態（iOS）、ユーザーのデバイスの表示設定、デバイスのサイズによって多少の差異が生じる場合があります。

| メッセージタイプ | 推奨長（テキストのみ） | 推奨長（リッチ） |
| --- | --- | --- |
| iOS ロック画面 | 160文字 | 130文字 |
| iOS 通知センター | 160文字 | 130文字 |
| iOS バナーアラート | 80文字 | 65文字 |
| Android ロック画面 | 49文字 | N/A |
| Android 通知ドロワー | 597文字 | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

iOS の文字数の詳細については、[iOS 文字数ガイドライン]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count)を参照してください。

#### Web プッシュ

{% tabs %}
{% tab 画像 %}

| ブラウザ | 推奨アイコンサイズ |
| --- | --- |
| Chrome | 192 x 192 px 以上 |
| Firefox | 192 x 192 px 以上 |
| Safari | 192 x 192 px 以上（MacOS 13+ の Safari 16 でキャンペーンごとに設定可能） |
| Opera | 192 x 192 px 以上 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

| ブラウザ | プラットフォーム | 大きい画像サイズ |
| --- | --- | --- |
| Chrome | Android | 2:1 アスペクト比 |
| Firefox | Android | N/A |
| Chrome | Windows | 2:1 アスペクト比 |
| Edge | Windows | 2:1 アスペクト比 |
| Firefox | Windows | N/A |
| Opera | Windows | 2:1 アスペクト比 |
| Chrome | MacOS | N/A |
| Safari | MacOS | N/A |
| Firefox | MacOS | N/A |
| Opera | MacOS | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab テキスト %}

| ブラウザ | プラットフォーム | 最大タイトル長 | 最大本文長 |
| --- | --- | --- | --- |
| Chrome | Android | 35 | 50 |
| Firefox | Android | 35 | 50 |
| Chrome | Windows | 50 | 120 |
| Edge | Windows | 50 | 120 |
| Firefox | Windows | 54 | 200 |
| Opera | Windows | 50 | 120 |
| Chrome | MacOS | 35 | 50 |
| Safari | MacOS | 38 | 84 |
| Firefox | MacOS | 38 | 42 |
| Opera | MacOS | 38 | 42 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% endtabs %}

#### プッシュ通知の例

{% tabs %}
{% tab iOS %}

![「Hi! This is an iOS Push with an image」というテキストと絵文字が表示されたiOSプッシュ通知。テキストの横に小さな画像があります。]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![前のメッセージと同じテキストが表示されたiOSプッシュ通知（ハードプッシュ時）。テキストの前に拡大された画像が表示されています。]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Android %}

![メッセージテキストの下に大きな画像が表示されたAndroidプッシュ通知。]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
大きな画像の通知は、600 x 300 ピクセル以上の画像を使用すると最適に表示されます。
{% endalert %}

{% endtab %}
{% endtabs %}

### 動画

メディアライブラリーにアップロードされた動画は、WhatsApp メッセージでのみ使用できます。詳細については、[WhatsApp メッセージの作成]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages)を参照してください。

## BrazeAI<sup>TM</sup> で画像を生成する {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
この機能を使用する前に、[データがどのように使用され、OpenAI に送信されるか]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy)をご確認ください。
{% endalert %}