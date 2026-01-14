{% if include.variable_name == "image behavior" %}


| レイアウト | 動作 |
| --- | --- |
| 画像とテキスト | 縦長または細長い画像は縮小され、水平方向の中央に配置される。幅の広い画像は左右の端が切り取られる。 |
| 画像のみ | メッセージは、ほとんどのアスペクト比の画像に合うようにリサイズされる。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "payload size" %}

次のペイロードサイズを推奨します。

| メッセージングシステム | 推奨ペイロード |
| --- | --- |
| iOS(プレiOS 8) | 0.256 KB |
| iOS(ポストiOS 8) | 2 KB |
| Android(FCM) | 4 KB |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "in-app messages" %}

モーダル形式のアプリ内メッセージは、選択した画像またはメッセージのコピーのサイズや比率を守りつつ、デバイスに最適で最もフィットする比率で表示されるように設計されています。

アプリ内メッセージに含めることができるテキスト文字数に制限はありませんが(ボタン、ヘッドライン、メインボディなどと同様に)、使用するテキスト文字数を調整します。テキストが多すぎると、ユーザーはメッセージを展開してスクロールする必要があります。

すべてのアプリ内メッセージの推奨画像サイズは500 KB、最大画像サイズは5 MB で、PNG、JPEG、GIF のファイルタイプをサポートしています。

{% tabs %}
{% tab Portrait %}

| タイプ | アスペクト比 | 画質 | メモ |
| --- | --- | --- | --- |
| ポートレート全画面（テキスト付き） | 6:5 | 高解像度 1200 x 1000 px <br>最小解像度 600 x 500 px | クロッピングはすべての面で発生しますが、イメージは常にビューポートの上位50% を占めます。 |
| 縦型フルスクリーン(画像のみ、ボタンあり/なし) | 3:5 | 高解像度 1200 x 2000 px <br> 最小解像度 600 x 1000 px | 背の高いデバイスでは、左右の端でクロッピングが発生することがある。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% tab Landscape %}

| タイプ | アスペクト比 | 画質 | メモ |
| --- | --- | --- | --- |
| ランドスケープ全画面 (テキスト付き) | 10:3 | 高解像度 2000 x 600 px <br>最小解像度 1000 x 300 px | クロッピングはすべての面で発生しますが、イメージは常にビューポートの上位50% を占めます。 |
| 横向きフルスクリーン(画像のみ、ボタンあり/なし) | 5:3 | 高解像度 2000 x 600 px <br> 最小解像度 1000 x 600 px | 背の高いデバイスでは、左右の端でクロッピングが発生することがある。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% tab Slideup %}

| タイプ | アスペクト比 | 画質 | メモ |
| --- | --- | --- | --- |
| スライドアップ | 1:1 | 高解像度 150 x 150 px <br> 最小解像度50 x 50 px | さまざまなアスペクト比の画像が、トリミングなしで正方形の画像コンテナに収まる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% tab Modal %}

| タイプ | アスペクト比 | 画質 | メモ |
| --- | --- | --- | --- |
| モーダル(画像のみ) | 1:1 | 推奨最大再ソリューション:1200 x 2000 px <br> 最低再ソリューション:600 x 600 px | メッセージは、ほとんどのアスペクト比の画像に合うようにリサイズされる。推奨される最大再ソリューションのアスペクト比は3:5 であり、最適な結果が得られない場合があります。"画像sが大きいほど使用可能ですが、読み込む時間が長くなる場合があります。<br> "画像sのアイデアlの縦横比は1:1であり、この比を満たさないと、アップロード中にワーニングがトリガーされることがあります。この警告は最良の結果のための提案であり、大きな"画像s のアップロードを妨げるものではありません。 |
| テキスト付きモーダル | 29:10 | 高解像度 1450 x 500 px <br> 最小解像度 600 x 205 px | 背の高い画像は縮小され、水平方向の中央に配置される。幅の広い画像は左右の端が切り取られる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% endtabs %}

{% endif %}

{% if include.variable_name == "push notifications" %}

| メッセージタイプ | メッセージの最大長 | タイトルの最大長 |
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
  <thead>
    <tr>
      <th>画像タイプ</th>
      <th>アスペクト比</th>
      <th>最大画素数</th>
      <th>最大画像サイズ</th>
      <th>ファイルタイプ</th>
      <th>メモ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>iOS</td>
      <td>2:1(推奨)</td>
      <td>1038 x 1038</td>
      <td>5 MB</td>
      <td>PNG、JPEG、GIF</td>
      <td>2020年1月現在、iOS リッチプッシュ通知では、10MB 未満の画像であれば1038 x 1038 px の画像を処理できますが、できるだけ小さいファイルサイズを使用することをお勧めします。実際、大きなファイルを送信すると、不要なネットワークストレスを引き起こしたり、ダウンロードのタイムアウトがより頻繁に発生する可能性があります。<br><br>詳細については、<a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/">iOS リッチ通知</a>を参照してください。</td>
    </tr>
    <tr>
      <td>Androidプッシュアイコン</td>
      <td>1:1</td>
      <td>該当なし</td>
      <td>500 KB</td>
      <td>PNG、JPEG</td>
      <td></td>
    </tr>
    <tr>
      <td>Android拡張通知イメージ</td>
      <td>2:1</td>
      <td><b>小:</b><br>512 x 256<br><br><b>中:</b><br>1024 x 512<br><br><b>大:</b><br>2048 x 1024</td>
      <td>500 KB</td>
      <td>PNG、JPEG</td>
      <td><a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/">Androidリッチ通知</a>で使用されます。</td>
    </tr>
    <tr>
      <td>Android傾斜像</td>
      <td>3:2</td>
      <td>該当なし</td>
      <td>N/A</td>
      <td>PNG、JPEG</td>
      <td>詳細については、<a href="{{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/inline_image_push/">Androidインラインイメージプッシュ</a>を参照してください。</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4  .reset-td-br-5 .reset-td-br-6 role="presentation"}

{% endif %}

{% if include.variable_name == "email" %}

| メールタイプ | 推奨最大プロパティ |
| --- | --- | 
| テキストのみ | 25 KB |
| 画像付きテキスト | 60 KB |
| メール幅 | 600 px |
{: .reset-td-br-1 .reset-td-br-2}

| 画像の仕様 | 推奨最大プロパティ |
| --- | --- | 
| サイズ | 5 MB |
| 幅 | ヘッダー:600 px<br>Body:480 px |
| ファイルタイプ | PNG、JPEG、GIF |
{: .reset-td-br-1 .reset-td-br-2}

| テキスト仕様 | 推奨最大プロパティ |
| --- | --- | 
| 件名の長さ | 35 文字<br>6～10ワード |
| `"From: Name"` 長 | 25 文字 |
| プレヘッダーの長さ | 85文字 |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "content cards" %}

| カードの種類 | アスペクト比     | 画質       |
| --------- | ---------------- | ------------------- |
| クラシック   | 1:1のアスペクト比 | 60 x 60 px        |
| キャプション付き | アスペクト比4:3 | 最小幅 600 px |
| バナー    | 任意のアスペクト比 | 最小幅 600 px |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

詳細については、[コンテンツカードクリエイティブの詳細]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/)を参照してください。

{% endif %}
