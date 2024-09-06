---
nav_title: "iOSリッチ通知を作成する"
article_title: リッチなプッシュ通知を作成する
page_order: 3
page_type: tutorial
description: "このチュートリアルでは、Brazeキャンペーン用のiOSリッチ通知を作成するための要件と手順を説明する。"

platform: iOS
channel:
  - push
tool:
  - Campaigns

---

# iOSリッチ通知を作成する

> リッチ・ノーティフィケーションでは、コピー以外のコンテンツを追加することで、プッシュ通知をよりカスタマイズすることができる。Androidの通知には、以前からプッシュ通知に画像が含まれており、「拡張通知画像」として表示されている。iOS10から、あなたの顧客はGIF、画像、動画、音声を含むiOSプッシュ通知を受け取ることができるようになった。

## 要件


- アプリがリッチ通知を送信できるようにするには、[iOSプッシュ統合の][1]手順に従って、開発者がアプリにサービス拡張機能を追加する必要がある。
- メディアの制限や仕様については、[アップルのドキュメントも][2]参照してほしい。
- iOSのリッチ通知は、クイックプッシュキャンペーン作成時には利用できない。
- iOSは画面に収まるように画像を拡大縮小し、リッチ画像はアクティブまたはロックされたビュー用に拡大縮小する。
- 現在、ダッシュボード内で直接アップロードできるファイル形式には、JPEG、PNG、GIFがある。これらのファイルは、これらの追加ファイルタイプとともに、テンプレート可能なURLフィールドに入力することもできる：AIF、M4A、MP3、MP4、またはWAV。

{% alert note %}
2020年1月現在、iOSのリッチ・プッシュ通知は1038x1038で10MB以下の画像を扱うことができるが、できるだけ小さいファイルサイズを使うことを推奨する。実際には、大きなファイルを送信することは、不必要なネットワークストレスを引き起こし、ダウンロードのタイムアウトをより一般的にする可能性がある。
{% endalert %}

### 文字数

プッシュに含めるべき正確な文字数について厳密なルールを提供することはできないが、iOSのメッセージをデザインする際に考慮すべき[いくつかのガイドラインを提供する]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/)。画像の有無、ユーザーの端末の通知状態や表示設定、端末の大きさによって多少の誤差が生じる場合がある。迷ったときは、短く、甘く。

> 一般的な経験則として、Brazeは、モバイルプッシュ通知では、オプションのタイトルとメッセージ本文の両方で、各行のテキストを約30～40文字に抑えることを推奨している。

#### 通知内容

ユーザーは様々な状況でプッシュ通知を見る可能性があり、以下のように異なる長さのテキストを見る可能性がある。

<table>
<thead>
  <tr>
    <th>ロック画面または通知センター</th>
    <th>拡大</th>
    <th>デバイス・アクティブ</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td width="33%">これが最も一般的なシナリオだ。<br><br><b>Title:</b>テキスト1行<br><b>Body:</b>テキスト4行<br><b>画像：</b>正方形のサムネイル</td>
    <td width="33%">ユーザーがメッセージを長押ししたとき。<br><br><b>Title:</b>テキスト1行<br><b>Body:</b>本文7行<br><b>Image:</b>2:1のアスペクト比（推奨。）</td>
    <td width="33%">携帯電話のロックが解除され、アクティブな状態でプッシュを受信した場合。<br><br><b>Title:</b>テキスト1行<br><b>Body:</b>テキスト2行</td>
  </tr>
</tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

![] （{% image_buster /assets/img_archive/push_ios_notification_states.png %} ）。

{% alert note %}
プッシュ通知の拡大には2:1のアスペクト比を推奨しているが、ほぼすべてのアスペクト比に対応している。画像は常に通知の幅いっぱいに表示され、高さはそれに応じて調整される。
{% endalert %}

#### テキスト切り捨ての変数

コンテンツを作成する際には、テキストの表示量に影響する可能性のある以下のシナリオを考慮すること。

{% tabs %}
{% tab タイミング %}

##### タイミング

ユーザーがいつプッシュ通知に関与したかによって、タイムスタンプはタイトルテキストを短くすることができる。

![タイムスタンプ "now"、タイトル文字数35のプッシュ通知例]({% image_buster/assets/img_archive/push_ios_timing_35.png %})
<br>タイトルの文字数：**35**

![タイムスタンプが "3h ago"、タイトル文字数が33のプッシュ通知例]({% image_buster/assets/img_archive/push_ios_timing_33.png %})
<br>タイトルの文字数：**33**

![タイムスタンプが "Yesterday, 8:37 AM"、タイトル文字数が22のプッシュ通知例]({% image_buster/assets/img_archive/push_ios_timing_22.png %})
<br>タイトルの文字数：**22**

{% endtab %}
{% tab 画像 %}

##### 画像

画像がある場合、本文は1行につき約10文字短くなる。

![画像なし、本文文字数179のプッシュ通知例]({% image_buster/assets/img_archive/push_ios_images_179.png %})
<br>ボディーの文字数だ：**179**

![画像と本文の文字数が154のプッシュ通知例]({% image_buster/assets/img_archive/push_ios_images_154.png %})
<br>ボディーの文字数だ：**154**

{% endtab %}
{% tab 中断レベル %}

##### 中断レベル（iOS 15）

Time SensitiveとCriticalの表記は、タイトルをタイムスタンプのない新しい行に押し下げ、少しスペースを与える。

![]({% image_buster/assets/img_archive/push_ios_interruption_level_35.png %}) 「Time Sensitive」または「Critical」の表記がなく、タイトル文字数が35のプッシュ通知例。
<br>タイトルの文字数：**35**

![]({% image_buster/assets/img_archive/push_ios_interruption_level_39.png %}) タイムセンシティブの表記とタイトル文字数39のプッシュ通知例。
<br>タイトルの文字数：**39**

{% endtab %}
{% tab もっと見る %}

##### そしてさらに

以下もテキストの切り捨てに影響する：

- **電話の表示設定：**ユーザーは、アクセシビリティ上の理由から、自分の電話でグローバルUIのフォントサイズを増減できる。
- **デバイスの幅：**メッセージは小さな携帯電話でも、幅の広いiPadでも表示できる。
- **コンテンツの種類：**絵文字や "m "や "w "のような幅の広い文字は、"i "や "t "よりもスペースを取る。"engagement "のような長い単語は、短い単語よりも突然改行されることがある。

{% endtab %}
{% endtabs %}

## iOSのリッチ通知を設定する

### Step 1:キャンペーンを作成する

[キャンペーンの][3]手順に従って、iOS用のプッシュ通知を作成する。リッチコンテンツを含まないプッシュ通知の設定に使うのと同じコンポーザーを使うことになる。

### Step 2:メディアを追加する

メッセージのコンポーザーにある**Rich Notification Media**フィールドに画像、GIF、オーディオ、ビデオファイルを追加する。コンテンツファイルを追加する方法については、[要件を](#requirements)参照のこと。

![][4]{: style="max-width:70%;" }

このメッセージは、iOS 10を搭載したデバイスを持っているユーザーだけに送信するよう制限することもできる。iOS10にアップグレードしていないユーザーの場合、「**リッチ通知をサポートするデバイスにのみ送信**」のチェックを外しておくと、リッチコンテンツを含まないテキストのみの通知として表示される。

![][5]{: style="max-width:70%;" }

### Step 3:キャンペーンの作成を続ける

リッチ通知コンテンツがダッシュボードにアップロードされたら、\[キャンペーンのスケジューリング][6] を続けることができる。

プッシュ通知を受け取ったユーザーは、プッシュ・メッセージを強く押して画像を拡大することができる。

![プッシュ通知を受け取ったユーザーがメッセージを強く押すと、「Hello！」と書かれた拡大画像が表示される。][8]{: style="max-width:50%;" }

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications
[2]: https://developer.apple.com/reference/usernotifications/unnotificationattachment
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[4]: {% image_buster /assets/img_archive/rich_notification_add_image.png %}
[5]: {% image_buster /assets/img_archive/rich_notification_ios10_select.png %}
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#schedule-push-campaign
[8]: {% image_buster /assets/img_archive/rich_notification_ios.gif %}
