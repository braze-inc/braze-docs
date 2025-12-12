---
nav_title: "フルスクリーン"
article_title: フルスクリーンのアプリ内メッセージ
description: "この参考記事では、フルスクリーンのアプリ内メッセージのメッセージとデザイン要件について取り上げている。"
page_type: reference
page_order: 0
channel:
  - in-app messages
tool:
  - Media

---

# フルスクリーンのアプリ内メッセージ

> フルスクリーンのメッセージは端末の画面全体を占める！このメッセージタイプは、必須アプリのアップデートのように、ユーザーの注意が本当に必要な場合に最適だ。

{% tabs %}
{% tab Portrait %}

![2つのフルスクリーンアプリ内メッセージは、縦向きで並べて表示され、"画像と文字の推奨事項が詳しく説明されています。詳細については、次のセクションを参照してください。]({% image_buster /assets/img/full-screen-spec.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Landscape %}

![2 つのフルスクリーンアプリ内メッセージは横向きで並べて表示され、"画像と文字の推奨事項を詳しく説明します。詳細については、次のセクションを参照してください。]({% image_buster /assets/img/full-screen-spec-landscape.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}

## 画像

全画面のアプリ内メッセージは、デバイスの高さいっぱいに表示され、必要に応じて水平方向 (左右) にクロップされます。画像とテキストのフルスクリーンメッセージは、デバイスの高さの50％を埋める。ノッチ付き」デバイスでは、アプリ内のフルスクリーンメッセージがすべてステータスバーを埋める。

- すべての画像は 5 MB 以下でなければなりません。
- ファイル形式はPNG、JPEG、[GIFのみ]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs#gifs)受け付ける。
- 画像は500KBを推奨する。

{% alert tip %} 自信を持ってアセットを創造しましょう！アプリ内メッセージ "画像 テンプレート sとセーフゾーンオーバーレイは、すべてのサイズの機器でうまく動作するように設計されています。[Down 読み込む Design テンプレート s ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

### ポートレート

| レイアウト | 資産規模 | 注釈 |
|--- | --- | --- |
| 画像とテキスト | アスペクト比6:5<br> 高解像度 1200 x 1000 px<br> 600 x 500 px 以上 | 四方がトリミングされる可能性がありますが、画像は常にビューポートの上部 50% を占めます。 |
| 画像のみ | アスペクト比 3:5<br> 高解像度 1200 x 2000 px<br> 600 x 1000 px 以上 | 背の高いデバイスでは、左右の端でクロッピングが発生することがある。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 景観

| レイアウト | 資産規模 | 注釈 |
|--- | --- | --- |
| 画像とテキスト | アスペクト比10:3<br> 高解像度 2000 x 600px<br> 1000 x 300 px 以上 | 四方がトリミングされる可能性がありますが、画像は常にビューポートの上部 50% を占めます。 |
| 画像のみ | アスペクト比5:3<br> 高解像度 2000 x 1200px<br> 1000 x 600 px 以上 | 背の高いデバイスでは、左右の端でクロッピングが発生することがある。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 画像セーフゾーン

Brazeプラットフォームでフルスクリーンのアプリ内メッセージをプレビューする際、デバイス間で表示される際にトリミングから保護されるメッセージの領域に対して、イメージセーフゾーンを有効にすることができる。プレビューペインでイメージセーフゾーンをテストするだけでなく、いつも通り[メッセージをテスト]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/)することをお勧めする。

![ " Show Image Safe Zone" enabled でBrazeのアプリ内メッセージをプレビューする。"画像セーフゾーンは、"画像のどの部分がクロップから安全かを視覚化する"画像上のオーバーレイです。]({% image_buster /assets/img/image-safe-zone-full-screen-in-app-message.png %})

## 大型スクリーン

タブレットやデスクトップ・ブラウザでは、以下のスクリーンショットのように、フルスクリーンのアプリ内メッセージがアプリ画面の中央に表示される。

{% tabs %}
{% tab Portrait %}

![フルスクリーンは、大型スクリーンで縦向きに耳をアプリようにアプリ内メッセージします。アプリは、スクリーンの中央にある大きなモーダルのように聞こえます。]({% image_buster /assets/img/full-screen-large-viewport.png %}){: style="border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Landscape %}

![横向きで大画面に耳をアプリようにフルスクリーンでアプリ内メッセージします。アプリは、スクリーンの中央にある大きなモーダルのように聞こえます。]({% image_buster /assets/img/full-screen-large-viewport-landscape.png %}){: style="max-width:80%;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}

