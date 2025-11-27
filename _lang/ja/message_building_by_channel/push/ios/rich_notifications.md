---
nav_title: "リッチプッシュ通知の作成"
article_title: "iOSのリッチプッシュ通知の作成"
page_order: 3
page_type: tutorial
description: "このチュートリアルでは、Brazeキャンペーン用のiOSリッチ通知を作成するための要件と手順を説明する。"

platform: iOS
channel:
  - push
tool:
  - Campaigns

---

# iOSのリッチプッシュ通知の作成

> リッチ・ノーティフィケーションでは、コピー以外のコンテンツを追加することで、プッシュ通知をよりカスタマイズすることができる。Androidの通知には、以前からプッシュ通知に画像が含まれており、「拡張通知画像」として表示されている。iOS 10 以降、御社の顧客は GIF、画像、動画、音声を含む iOS プッシュ通知を受信できるようになりました。

## 前提条件

iOS のリッチプッシュ通知を作成する前に、次の詳細に注意してください。

- アプリからリッチプッシュ通知を送信できるようにするには、御社の開発者がアプリにサービス拡張機能を追加する必要があるため、「[iOS プッシュ連携]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications)」の手順に従います。
- 現在、Braze ダッシュボードで直接アップロードがサポートされているファイル形式には、JPEG、PNG、GIFがあります。これらのファイルは、これらの追加ファイルタイプとともに、テンプレート可能なURLフィールドに入力することもできる：AIF、M4A、MP3、MP4、またはWAV。
- メディアの制限と仕様については、[Apple のドキュメント](https://developer.apple.com/reference/usernotifications/unnotificationattachment) を参照してください。
- iOSのリッチ通知は、クイックプッシュキャンペーン作成時には利用できない。
- iOS では画面に収まるように画像を拡大縮小し、リッチ画像の場合はアクティブなビューまたはロックされたビューに合わせて拡大縮小します。

{% alert note %}
2020年1月現在、iOSのリッチ・プッシュ通知は1038x1038で10MB以下の画像を扱うことができるが、できるだけ小さいファイルサイズを使うことを推奨する。実際、大きなファイルを送信すると、不要なネットワークストレスを引き起こしたり、ダウンロードのタイムアウトがより頻繁に発生する可能性があります。
{% endalert %}

### 文字数

プッシュに含めるべき正確な文字数について厳密なルールを提供することはできないが、iOSのメッセージをデザインする際に考慮すべき[いくつかのガイドラインを提供する]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/)。画像の有無、ユーザーの端末の通知状態や表示設定、端末の大きさによって多少の誤差が生じる場合がある。迷ったときには、簡潔にまとめます。

Braze はベストプラクティスとして、モバイルプッシュ通知では、オプションのタイトルとメッセージ本文の両方で、各行のテキストを約30～40文字に抑えることを推奨しています。

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
    <td width="33%">ユーザーがメッセージを長押ししたとき。<br><br><b>Title:</b>テキスト1行<br><b>Body:</b>本文 7 行<br><b>Image:</b>2:1 のアスペクト比 (推奨。後述する注を参照)</td>
    <td width="33%">携帯電話のロックが解除され、アクティブな状態でプッシュを受信した場合。<br><br><b>Title:</b>テキスト1行<br><b>Body:</b>テキスト 2 行</td>
  </tr>
</tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

![ロック画面に表示されるプッシュ通知の例。展開した場合と、デバイスがアクティブな場合。]({% image_buster /assets/img_archive/push_ios_notification_states.png %})()

{% alert note %}
プッシュ通知の拡大には2:1のアスペクト比を推奨しているが、ほぼすべてのアスペクト比に対応している。画像は常に通知の幅いっぱいに表示され、高さはそれに応じて調整される。
{% endalert %}

#### テキスト切り捨ての変数

コンテンツを作成する際には、テキストの表示量に影響する可能性のある以下のシナリオを考慮すること。

{% tabs %}
{% tab Timing %}

ユーザーがプッシュ通知に反応したタイミングに応じて、タイムスタンプではタイトルテキストを短くすることができます。

![タイムスタンプ "now"、タイトル文字数35のプッシュ通知例]({% image_buster/assets/img_archive/push_ios_timing_35.png %})()
<br>タイトルの文字数：**35**

![タイムスタンプが "3h ago"、タイトル文字数が33のプッシュ通知例]({% image_buster/assets/img_archive/push_ios_timing_33.png %})()
<br>タイトルの文字数：**33**

![タイムスタンプが "Yesterday, 8:37 AM"、タイトル文字数が22のプッシュ通知例]({% image_buster/assets/img_archive/push_ios_timing_22.png %})()
<br>タイトルの文字数：**22**

{% endtab %}
{% tab Images %}

画像がある場合、本文は1行につき約10文字短くなる。

![画像なし、本文文字数179のプッシュ通知例]({% image_buster/assets/img_archive/push_ios_images_179.png %})()
<br>本文の文字数: **179**

![画像と本文の文字数が154のプッシュ通知例]({% image_buster/assets/img_archive/push_ios_images_154.png %})()
<br>本文の文字数: **154**

{% endtab %}
{% tab Interruption level %}

iOS15では、Time Sensitive とCritical の表記は、タイトルをタイムスタンプのない新しい行に押し下げ、少しスペースを与える。

![]({% image_buster/assets/img_archive/push_ios_interruption_level_35.png %})() 「Time Sensitive」または「Critical」の表記がなく、タイトル文字数が35のプッシュ通知例。
<br>タイトルの文字数：**35**

![「Time Sensitive」の表記があり、タイトル文字数が 39 のプッシュ通知例。]({% image_buster/assets/img_archive/push_ios_interruption_level_39.png %})()
<br>タイトルの文字数：**39**

{% endtab %}
{% tab More %}

以下の詳細は、テキストの切り捨てにも影響します。

- **電話の表示設定:** ユーザーは、通常アクセシビリティ上の理由から、自分の電話のグローバル UI のフォントサイズを増減できます。
- **デバイスの幅：**メッセージは小さな携帯電話でも、幅の広いiPadでも表示できる。
- **コンテンツタイプ:** 絵文字、および「m」や「w」のような幅の広い文字は、「i」や「t」よりもスペースを取ります。また、「engagement」のように長い単語は、短い単語よりも突然改行されることがあります。

{% endtab %}
{% endtabs %}

## iOSのリッチ通知を設定する

### ステップ 1: プッシュキャンペーンを作成する

[キャンペーンの]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message)手順に従って、iOS用のプッシュ通知を作成する。リッチコンテンツを含まないプッシュ通知の設定に使うのと同じコンポーザーを使うことになる。

### ステップ2:メディアを追加する

メッセージのコンポーザーにある**Rich Notification Media**フィールドに画像、GIF、オーディオ、ビデオファイルを追加する。コンテンツファイルを追加する方法については、「[要件](#requirements)」を参照してください。

![プッシュ通知のサマリーテキストの例。]({% image_buster /assets/img_archive/rich_notification_add_image.png %}){: style="max-width:70%;" }

このメッセージは、iOS 10を搭載したデバイスを持っているユーザーだけに送信するよう制限することもできる。iOS10にアップグレードしていないユーザーの場合、「**リッチ通知をサポートするデバイスにのみ送信**」のチェックを外しておくと、リッチコンテンツを含まないテキストのみの通知として表示される。

![画像を追加したり、画像のURLを入力したりすることができる、拡張された通知画像セクションです。]({% image_buster /assets/img_archive/rich_notification_ios10_select.png %}){: style="max-width:70%;" }

### ステップ 3:キャンペーンの作成を続ける

リッチ通知コンテンツがダッシュボードにアップロードされたら、[キャンペーンのスケジュールを続行できます]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#schedule-push-campaign)。

プッシュ通知を受信したユーザーは、プッシュメッセージを長押しして画像を拡大できます。

![プッシュ通知を受信したユーザーがメッセージを長押しすると、「Hello!」という拡大画像が表示されます。]({% image_buster /assets/img_archive/rich_notification_ios.gif %}){: style="max-width:50%;" }

