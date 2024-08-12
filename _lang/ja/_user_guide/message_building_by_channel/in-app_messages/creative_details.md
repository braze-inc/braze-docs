---
nav_title: クリエイティブ詳細
article_title: クリエイティブ詳細
page_order: 4
layout: dev_guide
guide_top_header: "クリエイティブ詳細"
guide_top_text: "アプリ内メッセージで創造性を発揮する前に、いくつかのガイドラインを知っておく必要があります。すべてのアプリ内メッセージテンプレートは、最新のデバイスでさまざまな長さのテキストとサイズの画像を表示するように設計されています。メッセージがすべての携帯電話、タブレット、パソコンで正しく表示されるようにするには、以下のガイドラインに従い、<a href='/docs/user_guide/message_building_by_channel/in-app_messages/testing/'>起動前に必ずメッセージをテストすることをお勧めします</a>。<br><br>次のメッセージタイプの「クリエイティブスペック」または「クリエイティブの詳細」のグローバル記事を確認してください。"
description: "このランディングハブは、モーダル、スライドアップ、フルスクリーンの3種類のアプリ内メッセージのデザインとコンテンツ要件をカバーしています。"

channel:
  - in-app messages
tools:
  - Media

guide_featured_title: "メッセージタイプ別の仕様"

guide_featured_list:
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal/
  image: /assets/img/icon_modal.png
- name: Slideup
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup/
  image: /assets/img/icon_slideup.png
- name: "Fullscreen"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/
  image: /assets/img/icon_full_screen.png

---

## コンテンツガイドライン

### テキスト

アプリ内のメッセージ本文やヘッダーは、短く簡潔にすることをおすすめします。ヘッダーは 1 ～ 2 行、本文は 3 行にしてください。3 行を過ぎると、メッセージを垂直方向にスクロールする必要があるため、ユーザーがすべてのコンテンツにアクセスできなくなる可能性があります。スクロールをトリガーするしきい値は、エンドユーザーのデバイスサイズ、カスタムスタイル、メッセージ内の画像の有無によって異なりますが、通常は 3 行で十分です。

最新世代のアプリ内メッセージ (第 3 世代) を使用している場合は、フォントのデフォルトが iOS と Android のオペレーティングシステムのデフォルトの Sans Serif に設定されていることがわかります。ウェブアプリ内メッセージはデフォルトでHelveticaに設定されます。

### 画像

画像に関するガイドラインは、テキストに関するガイドラインよりも体系化されています。これは、メッセージが意図したとおりに、あらゆるモデルとサイズのスマートフォン、タブレット、およびコンピューターで美しく表示されるようにするためです。

一般的に、Braze は 16:10 の画面に収まる画像を使用することを推奨しています。

- **すべての画像は 5 MB 未満でなければなりません。**
- PNG、JPEG、および GIF ファイルタイプのみ受け付けています。
- Braze SDK が CDN からアセットをダウンロードしてオフラインメッセージを表示できるように、[メディアライブラリに画像をホストすることをおすすめします]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/)。
- 全画面表示のメッセージについては、[画像セーフゾーンのガイドラインに従ってください]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone)。

{% alert tip %} 自信を持ってアセットを作成しましょう！アプリ内メッセージ画像テンプレートとセーフゾーンオーバーレイは、あらゆるサイズのデバイスでうまく機能するように設計されています。[デザインテンプレートをZIP形式でダウンロード] () {% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %} {% endalert %}

{% tabs %}{% tab Fullscreen %}

![Fullscreen in-app message taking over an app screen. The fullscreen message includes a large image, header, message body, and two buttons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

| レイアウト | アセットサイズ | 注意事項 |
|--- | --- | --- |
| 画像+テキスト| アスペクト比 6:5<br>高解像度 1200 x 1000 ピクセル<br> 最小 600 x 500 px | トリミングはすべての面で可能ですが、画像は常にビューポートの上部 50% を占めます |
| 画像のみ | アスペクト比 3:5<br>高解像度 1200 x 2000 ピクセル<br> 最小 600 x 1000 px | 背の高い端末では左右の端が切り取られることがある |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

[フルスクリーンの詳細]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen)


{% endtab %}
{% tab Modal %}

![Modal in-app message appearing in the center of an app and website as a dialog. The modal includes an image, header, message body, and two buttons.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

| レイアウト | アセットサイズ | 注意事項 |
|--- | --- | ------ |
| 画像+テキスト| アスペクト比 29:10<br>高解像度 1450 x 500 ピクセル<br> 最小 600 x 205 ピクセル | 背の高い画像は縮小され、水平方向の中央に表示されます。幅の広い画像は左右の端で切り取られます。|
| 画像のみ | ほぼすべてのアスペクト比<br>最大1200 x 2000ピクセルの高解像度<br> 最小 600 x 600 ピクセル | ほとんどの縦横比の画像に合うようにメッセージのサイズが変更されます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

[モーダルの詳細]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/modal)

{% endtab %}
{% tab Slideup %}

![Slideup in-app message appearing from the bottom of the app screen. The slideup includes an icon image and a brief message.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

| レイアウト | アセットサイズ | 注意事項 |
|--- | --- | --- |
| 画像+テキスト | 1:1 のアスペクト比<br>高解像度 150 x 150 ピクセル<br> 最小 50 x 50 px | さまざまな縦横比の画像が、トリミングせずに正方形の画像コンテナに収まります。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

[スライドアップの詳細]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup)

{% endtab %}
{% endtabs %}

### GIF とビデオ

Brazeは現在、ウェブ（付属）、[Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs/)、iOS（付属）のアプリ内メッセージング用のGIFをサポートしています。これは、目的のプラットフォーム統合中に有効になっているためです。アプリ内メッセージの動画について詳しくは、[カスタマイズドキュメントをご覧ください]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#video)。

## その他の考慮事項

Brazeのアプリ内メッセージには、グローバルなクリエイティブ仕様と個別のクリエイティブ仕様の両方があります。アプリ内メッセージを完全にカスタマイズする方法の詳細については、[カスタマイズページをご覧ください]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/)。

<br>
