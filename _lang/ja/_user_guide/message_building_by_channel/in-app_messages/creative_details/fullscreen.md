---
nav_title: "全画面"
article_title: フルスクリーンのアプリ内メッセージ
description: "このリファレンス記事では、フルスクリーンのアプリ内メッセージのメッセージとデザイン要件について説明します。"
page_type: reference
page_order: 0
channel:
  - in-app messages
tool:
  - Media

---

# アプリ内メッセージの全画面表示

> 全画面表示のメッセージがデバイスの画面全体を占めます。このメッセージタイプは、必須のアプリの更新など、ユーザーの注意を本当に必要とする場合に最適です。

{% tabs %}
{% tab Portrait %}

![Two fullscreen in-app messages side-by-side in portrait orientation, detailing the image and text recommendations. See following sections for details.]({% image_buster /assets/img/full-screen-spec.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Landscape %}

![Two fullscreen in-app messages side-by-side in landscape orientation, detailing the image and text recommendations. See following sections for details.]({% image_buster /assets/img/full-screen-spec-landscape.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}

## 画像

全画面表示のアプリ内メッセージは、デバイスの高さ全体に表示され、必要に応じて水平方向(左右)にトリミングされます。画像とテキストの全画面表示メッセージは、デバイスの高さの 50% を占めます。すべてのフルスクリーンのアプリ内メッセージは、「ノッチ付き」デバイスのステータスバーに表示されます。

- すべての画像は 5 MB 未満である必要があります。
- ファイル形式は、PNG、JPEG [、GIFのみ]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs#gifs) です。
- 画像は 500 KB にすることをお勧めします。

{% alert tip %} 自信を持ってアセットを作成!アプリ内メッセージ画像テンプレートとセーフゾーンオーバーレイは、あらゆるサイズのデバイスでうまく機能するように設計されています。[デザインテンプレートZIPをダウンロード\](){% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %} {% endalert %}

### 縦

|レイアウト |資産規模 |メモ |
|--- | --- | --- |
|画像とテキスト |アスペクト比 6:5<br> 高解像度 1200 x 1000 ピクセル<br> 最小 600 x 500 ピクセル |トリミングはすべての側面で発生する可能性がありますが、画像は常にビューポートの上位50%を埋めます |
|画像のみ |アスペクト比 3:5<br> 高解像度 1200 x 2000 px<br> 最小 600 x 1000 ピクセル |背の高いデバイスでは、左端と右端でトリミングが発生することがあります |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### 横

|レイアウト |資産規模 |メモ |
|--- | --- | --- |
|画像とテキスト |アスペクト比 10:3<br> 高解像度 2000 x 600px<br> 最小 1000 x 300 ピクセル |トリミングはすべての側面で発生する可能性がありますが、画像は常にビューポートの上位50%を埋めます |
|画像のみ |アスペクト比 5:3<br> 高解像度 2000 x 1200px<br> 最小 1000 x 600 ピクセル |背の高いデバイスでは、左端と右端でトリミングが発生することがあります |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### 画像セーフゾーン

Brazeプラットフォームでフルスクリーンのアプリ内メッセージをプレビューする場合、デバイス間で表示したときにトリミングされないメッセージの領域に対して、画像セーフゾーンを有効にすることができます。プレビューペインで画像セーフゾーンをテストすることに加えて、通常どおり [メッセージをテスト]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) することをお勧めします。

![Brazeで「画像セーフゾーンを表示」を有効にした状態でアプリ内メッセージをプレビューする。画像セーフゾーンは、画像のどの部分がトリミングされても安全かを視覚化する、画像上のオーバーレイです。〔3c〕

## 大画面

タブレットまたはデスクトップ ブラウザーでは、次のスクリーンショットに示すように、全画面表示のアプリ内メッセージがアプリ画面の中央に表示されます。

{% tabs %}
{% tab Portrait %}

![Fullscreen in-app message as it would appear on a large screen in portrait orientation. The message appears as a large modal that sits in the center of the screen.]({% image_buster /assets/img/full-screen-large-viewport.png %}){: style="border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Landscape %}

![Fullscreen in-app message as it would appear on a large screen in landscape orientation. The message appears as a large modal that sits in the center of the screen.]({% image_buster /assets/img/full-screen-large-viewport-landscape.png %}){: style="max-width:80%;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}

[3b]: {% image_buster /assets/img/full-screen-large-viewport.png %}
[3c]: {% image_buster /assets/img/image-safe-zone-full-screen-in-app-message.png %}
