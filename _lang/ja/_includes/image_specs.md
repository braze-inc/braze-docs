{% if include.variable_name == "image behavior" %}


| レイアウト | 動作 |
| --- | --- |
| 画像とテキスト | 縦長または縦長の画像は縮小され、横方向の中央に配置されます。幅の広い画像は左右の端が切り取られる。 |
| 画像のみ | メッセージは、ほとんどのアスペクト比の画像に合うようにリサイズされる。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "payload size" %}

次のペイロードサイズを推奨します。

| メッセージングシステム | 推奨可搬質量 |
| --- | --- |
| iOS(プレiOS 8) | 0.256 KB |
| iOS(ポストiOS 8) | 2 KB |
| Android(FCM) | 4 KB |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "in-app messages" %}

モダル・イン・アプリ・メッセージは、選択したイメージまたはコピーのサイズと比率に忠実であると同時に、デバイスを可能な限り最適かつ最大の充填率に収めるように設計されています。

アプリ内メッセージに含めることができるテキスト文字数に制限はありませんが(ボタン、ヘッドライン、メインボディなどと同様に)、使用するテキスト文字数を調整します。テキストが多すぎると、ユーザーはメッセージを展開してスクロールする必要があります。

アプリ内メッセージはすべて、推奨画像サイズ500KB、最大画像サイズ5MB、およびPNG、JPG、およびGIF ファイルタイプをサポートしています。

{% tabs %}
{% tab ポートレート %}

| タイプ | アスペクト比 | 画質 | メモ |
| --- | --- | --- | --- |
| テキスト付き縦型フルスクリーン | 6:5 | 高解像度 1200 x 1000 px <br>最小解像度 600 x 500 px | クロッピングはすべての面で発生しますが、イメージは常にビューポートの上位50% を占めます。 |
| 縦型フルスクリーン(画像のみ、ボタンあり/なし) | 3:5 | 高解像度 1200 x 2000 px <br> 最小解像度 600 x 1000 px | 高いデバイスでは、左右の端でクロップが発生することがあります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% tab 景観 %}

| タイプ | アスペクト比 | 画質 | メモ |
| --- | --- | --- | --- |
| テキストを含む横画面 | 10:3 | 高解像度 2000 x 600 px <br>最小解像度 1000 x 300 px | クロッピングはすべての面で発生しますが、イメージは常にビューポートの上位50% を占めます。 |
| 横向きフルスクリーン(画像のみ、ボタンあり/なし) | 5:3 | 高解像度 2000 x 600 px <br> 最小解像度 1000 x 600 px | 高いデバイスでは、左右の端でクロップが発生することがあります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% tab スライドアップ %}

| タイプ | アスペクト比 | 画質 | メモ |
| --- | --- | --- | --- |
| スライドアップ | 1:1 | 高解像度 150 x 150 px <br> 最小解像度50 x 50 px | さまざまなアスペクト比の画像が、トリミングなしで正方形の画像コンテナに収まる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% tab モーダル %}

| タイプ | アスペクト比 | 画質 | メモ |
| --- | --- | --- | --- |
| モーダル(画像のみ) | 1:1 | 高解像度 1200 x 2000 px <br> 最小解像度 600 x 600 px | メッセージは、ほとんどのアスペクト比の画像に合うようにリサイズされる。 |
| テキスト付きモーダル | 29:10 | 高解像度 1450 x 500 px <br> 最小解像度 600 x 205 px | 背の高い画像は縮小され、水平方向の中央に配置される。幅の広い画像は左右の端が切り取られる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% endtabs %}

{% endif %}

{% if include.variable_name == "push notifications" %}

| メッセージタイプ | 最大メッセージ長 | タイトルの最大長 |
| --- | --- | --- |
| iOSロック画面 | 175文字 | 43文字 |
| iOS通知 | 175文字 | 43文字 |
| iOSバナー警告 | 85文字 | 43文字 |
| Androidロック画面 | 49文字 | 43文字 |
| Android通知ドロワー | 597文字 | 43文字 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

すべてのプッシュ画像の推奨画像サイズは500KB です。

<style>
table td {
    word-break: break-word;
}
</style>

<table>
  <tr>
    <th>画像タイプ</th>
    <th>アスペクト比</th>
    <th>画質</th>
    <th>最大画像サイズ</th>
    <th>ファイルタイプ</th>
    <th>メモ</th>
  </tr>
  <tr>
    <td>iOS</td>
    <td>2:1(推奨)</td>
    <td>最大1038 x 1038 px</td>
    <td>5 MB</td>
    <td>PNG、JPG、GIF</td>
    <td>2020年1 月現在、iOS リッチプッシュ通知では、10MB 未満のイメージであれば1038 x 1038 px のイメージを処理できますが、できるだけ小さいファイルサイズを使用することをお勧めします。実際、大きなファイルを送信すると、不要なネットワークストレスを引き起こしたり、ダウンロードのタイムアウトがより頻繁に発生する可能性があります。<br><br>詳細については、<a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/">iOS リッチ通知</a>を参照してください。</td>
  </tr>
  <tr>
    <td>Androidプッシュアイコン</td>
    <td>1:1</td>
    <td>該当なし</td>
    <td>500 KB</td>
    <td>PNG、JPG</td>
    <td></td>
  </tr>
  <tr>
    <td>Android拡張通知イメージ</td>
    <td>2:1</td>
    <td>小: 512 x 256 px<br>中: 1024 x 512 px<br>大: 2048 x 1024 px</td>
    <td>500 KB</td>
    <td>PNG、JPG</td>
    <td><a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/">Androidリッチ通知</a>で使用されます。</td>
  </tr>
  <tr>
    <td>Android傾斜像</td>
    <td>3:2</td>
    <td>該当なし</td>
    <td>該当なし</td>
    <td>PNG、JPG</td>
    <td>詳細については、<a href="{{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/inline_image_push/">Androidインラインイメージプッシュ</a>を参照してください。</td>
  </tr>
</table>

{% endif %}

{% if include.variable_name == "email" %}

| メールタイプ | 推奨最大プロパティ |
| --- | --- | 
| テキストのみ | 25 KB |
| 画像付きテキスト | 60 KB |
| メール幅 | 600 個 |
{: .reset-td-br-1 .reset-td-br-2}

| 画像の仕様 | 推奨最大プロパティ |
| --- | --- | 
| サイズ | 5 MB |
| 幅 | ヘッダー:600 個<br>Body:480 個 |
| ファイルタイプ | PNG、JPG、GIF |
{: .reset-td-br-1 .reset-td-br-2}

| テキスト仕様 | 推奨最大プロパティ |
| --- | --- | 
| 件名行の長さ | 35 文字<br>6～10ワード |
| `"From: Name"` 長 | 25 文字 |
| プレヘッダ長 | 85文字 |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "content cards" %}

| カードの種類 | アスペクト比     | 画質       |
| --------- | ---------------- | ------------------- |
| クラシック   | 1:1のアスペクト比 | 60 x 60 px        |
| キャプション付き | アスペクト比4:3 | 600 px 最小幅 |
| バナー    | 任意のアスペクト比 | 600 px 最小幅 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

詳細については、[コンテンツカードクリエイティブの詳細]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/)を参照してください。

{% endif %}