---
nav_title: クリエイティブの詳細
article_title: クリエイティブの詳細
page_order: 3.5
layout: dev_guide
guide_top_header: "クリエイティブの詳細"
guide_top_text: "アプリ内メッセージで創造力を発揮する前に、いくつかのガイドラインを知っておく必要があります。すべてのアプリ内メッセージテンプレートは、最新のデバイスでさまざまな長さのテキストや画像サイズを表示できるように設計されている。すべての携帯電話、タブレット、コンピューターでメッセージがうまく表示されるようにするため、以下のガイドラインに従い、起動前に必ず<a href='/docs/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/'>メッセージをテストする</a>ことをお勧めする。"
description: "このランディングハブでは、モーダル、スライドアップ、フルスクリーンの3種類のアプリ内メッセージのデザインとコンテンツの要件をカバーしている。"

channel:
  - in-app messages
tools:
  - Media

guide_featured_title: "メッセージタイプ別の仕様"

guide_featured_list:
- name: モーダル
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal/
  image: /assets/img/braze_icons/layout-alt-01.svg
- name: スライドアップ
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup/
  image: /assets/img/braze_icons/arrow-circle-broken-up.svg
- name: "フルスクリーン"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/
  image: /assets/img/braze_icons/expand-05.svg

---

## コンテンツのガイドライン

### テキスト

アプリ内メッセージの本文やヘッダーは、1～2行、本文は3行程度に短くまとめることをお勧めする。3行を超えると、メッセージは縦にスクロールする必要があり、ユーザーはすべてのコンテンツに目を通さないかもしれない。スクロールのトリガーとなる閾値は、エンドユーザーのデバイスサイズ、カスタムスタイル、メッセージ内の画像の有無によって異なるが、通常は3行が安全である。

アプリ内メッセージの最新世代（ジェネレーション3）を使っている場合、iOSとAndroidのフォントのデフォルトはOSデフォルトのサンセリフであることがわかるだろう。Web のアプリ内メッセージはデフォルトで Helvetica になります。

### 画像

画像に関するガイドラインは、テキストに関するガイドラインよりも構造化されており、あらゆるモデルやサイズの携帯電話、タブレット、コンピュータで、意図したとおりにメッセージが美しく表示されるように配慮している。

一般的に、Brazeは16:10の画面に収まる画像を使用することを推奨している。

- **画像はすべて、5 MB 未満でなければなりません。**
- ファイル形式はPNG、JPEG、GIFのみ受け付ける。
- オフラインメッセージ表示のためにBraze SDKが当社のCDNからアセットをダウンロードできるように、[メディアライブラリに]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/)画像をホスティングすることを推奨する。
- フルスクリーンのメッセージについては、[画像のセーフゾーンに関する]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone)ガイドラインに従うこと。

{% alert tip %} 自信を持ってアセットを創造しましょう！アプリ内メッセージ "画像 テンプレート sとセーフゾーンオーバーレイは、すべてのサイズの機器でうまく動作するように設計されています。[Down 読み込む Design テンプレート s ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

{% tabs %}{% tab Fullscreen %}

![アプリ内メッセージがフルスクリーンでアプリの画面を占領する。フルスクリーンメッセージには、大きな"画像、ヘッダー、メッセージ本文、および2つのボタンが含まれます。]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

| レイアウト | アセットのサイズ | メモ |
|--- | --- | --- |
| 画像＋テキスト | アスペクト比6:5<br>高解像度 1200 x 1000 px<br> 600 x 500 px 以上 | 四方がトリミングされる可能性がありますが、画像は常にビューポートの上部 50% を占めます |
| 画像のみ | アスペクト比 3:5<br>高解像度 1200 x 2000 px<br> 600 x 1000 px 以上 | 背の高いデバイスでは、左右の端でクロッピングが発生することがある。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[全画面表示の詳細]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen)


{% endtab %}
{% tab Modal %}

![アプリやウェブサイトの中央にダイアログとして表示される、モーダルなアプリ内メッセージ。モーダルには、"画像、ヘッダー、メッセージ本文、および2つのボタンが含まれています。]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

| レイアウト | アセットのサイズ | メモ |
|--- | --- | ------ |
| 画像＋テキスト | アスペクト比29:10<br>高解像度 1450 x 500 px<br> 最小 600 x 205 px | 背の高い画像は縮小され、水平方向の中央に配置される。幅の広い画像は左右の端が切り取られる。 |
| 画像のみ | ほぼすべてのアスペクト比<br>最大1200 x 2000 pxの高解像度<br> 600 x 500 px 以上 | メッセージは、ほとんどのアスペクト比の画像に合うようにリサイズされる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[モーダルの詳細]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/modal)

{% endtab %}
{% tab Slideup %}

![アプリ画面下部から表示されるアプリ内メッセージのスライドアップ。スライドアップには、アイコン"画像と短いメッセージが表示されます。]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

| レイアウト | アセットのサイズ | メモ |
|--- | --- | --- |
| 画像+テキスト | 1:1のアスペクト比<br>高解像度150 x 150 px<br> 50 x 50 px 以上 | さまざまなアスペクト比の画像が、トリミングなしで正方形の画像コンテナに収まる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[スライドアップの詳細]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup)

{% endtab %}
{% endtabs %}

### GIFとビデオ

Braze は現在、アプリ内メッセージングで GIF をサポートしており、Web (標準装備)、[Android]({{site.baseurl}}/developer_guide/in_app_messages/gifs/?sdktab=android)、およびの iOS (標準装備) に対応しています。ただし、目的のプラットフォームの連携時に有効にしておく必要があります。アプリ内メッセージの動画については、[カスタマイズのドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#video)を参照してください。

## その他の考慮事項

Brazeのアプリ内メッセージには、グローバル仕様と個別クリエイティブ仕様がある。アプリ内メッセージのフルカスタマイズの詳細については、[カスタマイズ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/)のページを参照してください。

<br>
