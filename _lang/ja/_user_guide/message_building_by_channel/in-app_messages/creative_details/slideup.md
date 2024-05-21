---
nav_title: スライドアップ
article_title: Slideupアプリ内メッセージ
page_order: 2
channel:
  - in-app messages
tool:
  - Media
description: "このリファレンス記事では、スライドアップアプリ内メッセージのメッセージとデザイン要件について説明します。"

---

# アプリ内メッセージのスライドアップ

> スライドアップは通常、アプリ画面の上部または下部に表示されます(これはメッセージの作成時に設定できます)。これらは、新しい利用規約、Cookie、その他の情報スニペットについてユーザーに警告するのに最適です。これらは目立たず、メッセージが表示されている間もユーザーがアプリを操作し続けることができます。

![2 つのスライドアップアプリ内メッセージ、1 つは画面の上部から、もう 1 つは下部から表示され、画像とテキストの推奨事項が詳細に説明されています。詳細については、次のセクションを参照してください。〔2a〕{: style="max-width: 40%; border: none;"}

## イメージとコピーの動作

スライドアップ メッセージには、省略記号で切り捨てられる前に、最大 3 行のコピーを含めることができます。スライドアップ内の画像は切り抜かれたり切り取られたりすることはなく、常に 50 x 50 ピクセルの画像コンテナ内に収まるように縮小されます。

- すべての画像は 5 MB 未満である必要があります。
- ファイル形式は、PNG、JPEG、GIFのみです。
- 画像は 500 KB にすることをお勧めします。

{% alert tip %} 自信を持ってアセットを作成!アプリ内メッセージ画像テンプレートとセーフゾーンオーバーレイは、あらゆるサイズのデバイスでうまく機能するように設計されています。[デザインテンプレートZIPをダウンロード\](){% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %} {% endalert %}

|レイアウト |資産規模 |メモ |
|--- | --- | --- |
|画像 + テキスト |アスペクト比 1:1<br>高解像度 150 x 150 ピクセル<br> 最小 50 x 50 ピクセル |さまざまなアスペクト比の画像は、トリミングされずに正方形の画像コンテナに収まります。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

常にさまざまなデバイスで [メッセージをプレビューしてテスト]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) し、画像とメッセージの最も重要な領域が期待どおりに表示されることを確認する必要があります。コンポーザーでメッセージをプレビューする場合、デバイスでの実際のレンダリングは異なる場合があります。

## モバイル機器

モバイルデバイスでは、スライドアップはアプリ画面の上部または下部に表示されます。これは、メッセージを作成するときに指定できます。ユーザーは、スワイプしてスライドアップを閉じるか、クリックアクションが含まれている場合はタップして開くことができます。スライドアップにクリックアクションを追加すると、シェブロンの「>」が表示されます。

## 大画面

{% tabs %}
{% tab Desktop %}

デスクトップブラウザーでは、次のスクリーンショットに示すように、スライドアップアプリ内メッセージが画面の隅に表示されます(アプリ内メッセージの作成時に特に指定しない限り)。ユーザーは「X」ボタンを閉じると、スライドアップを閉じることができます。

![Slideup in-app message as it appears on a desktop browser. The message appears in the bottom-right corner of the screen and does not take up the full width of the screen.]({% image_buster /assets/img/slideup-large-viewport.png %}){: style="border: none;"}

{% endtab %}
{% tab Tablet %}

タブレットでは、画面の下部にスライドアップのアプリ内メッセージが表示されます。モバイルデバイスと同様に、ユーザーはスワイプしてスライドアップを閉じるか、クリックアクションが含まれている場合はタップして開くことができます。スライドアップにクリックアクションを追加すると、シェブロンの「>」が表示されます。閉じる「X」ボタンはデフォルトでは表示されません。

![Slideup in-app message as it appears on a tablet screen. The message appears in the bottom-middle of the screen and does not take up the full width of the screen.]({% image_buster /assets/img/slideup-tablet.png %}){: style="border: none;"}

{% endtab %}
{% endtabs %}

[2a]: {% image_buster /assets/img/slideup-spec.png %}
