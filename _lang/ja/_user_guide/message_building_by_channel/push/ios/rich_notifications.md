---
nav_title: リッチプッシュ通知の作成
article_title: "iOSのリッチプッシュ通知の作成"
page_order: 3
page_type: tutorial
description: "このチュートリアルでは、Brazeキャンペーン用のiOSリッチプッシュ通知を作成するための要件と手順を説明します。"

platform: iOS
channel:
  - push
tool:
  - Campaigns

---

# iOS用のリッチプッシュ通知を作成する

> リッチプッシュ通知では、コピー以外のコンテンツを追加することで、プッシュ通知をよりカスタマイズできます。Androidの通知には、以前からプッシュ通知に画像が含まれており、「拡張通知画像」として表示されています。iOS 10以降、顧客はGIF、画像、動画、音声を含むiOSプッシュ通知を受信できるようになりました。

## 前提条件

iOSのリッチプッシュ通知を作成する前に、次の詳細に注意してください。

- アプリからリッチプッシュ通知を送信できるようにするには、開発者がアプリにサービス拡張機能を追加する必要があるため、[iOSプッシュ連携]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications)の手順に従ってください。
- 現在、Brazeダッシュボードで直接アップロードがサポートされているファイル形式には、JPEG、PNG、GIFがあります。これらのファイルは、テンプレート可能なURLフィールドに以下の追加ファイルタイプとともに入力することもできます：AIF、M4A、MP3、MP4、またはWAV。
- メディアの制限と仕様については、[Appleのドキュメント](https://developer.apple.com/reference/usernotifications/unnotificationattachment)を参照してください。
- iOSのリッチプッシュ通知は、クイックプッシュキャンペーン作成時には利用できません。
- iOSでは画面に収まるように画像を拡大縮小し、リッチ画像の場合はアクティブなビューまたはロックされたビューに合わせて拡大縮小します。

{% alert note %}
2020年1月現在、iOSのリッチプッシュ通知は1038x1038で10&nbsp;MB以下の画像を扱うことができますが、できるだけ小さいファイルサイズを使用することを推奨します。実際、大きなファイルを送信すると、不要なネットワーク負荷を引き起こしたり、ダウンロードのタイムアウトがより頻繁に発生する可能性があります。
{% endalert %}

### 文字数

プッシュに含めるべき正確な文字数について厳密なルールを提供することはできませんが、iOSのメッセージをデザインする際に考慮すべき[いくつかのガイドラインを提供しています]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push)。画像の有無、ユーザーのデバイスの通知状態や表示設定、デバイスの大きさによって多少の差異が生じる場合があります。迷ったときには、簡潔にまとめましょう。

Brazeはベストプラクティスとして、モバイルプッシュ通知では、オプションのタイトルとメッセージ本文の両方で、各行のテキストを約30～40文字に抑えることを推奨しています。

#### 通知の状態

ユーザーはさまざまな状況でプッシュ通知を見る可能性があり、以下のように異なる長さのテキストが表示されることがあります。

<table>
<thead>
  <tr>
    <th>ロック画面または通知センター</th>
    <th>展開時</th>
    <th>デバイスアクティブ</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td width="33%">これが最も一般的なシナリオです。<br><br><b>タイトル:</b> テキスト1行<br><b>本文:</b> テキスト4行<br><b>画像:</b> 正方形のサムネイル</td>
    <td width="33%">ユーザーがメッセージを長押ししたとき。<br><br><b>タイトル:</b> テキスト1行<br><b>本文:</b> テキスト7行<br><b>画像:</b> 2:1のアスペクト比（推奨。後述の注を参照）</td>
    <td width="33%">携帯電話のロックが解除され、アクティブな状態でプッシュを受信した場合。<br><br><b>タイトル:</b> テキスト1行<br><b>本文:</b> テキスト2行</td>
  </tr>
</tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

![ロック画面に表示されるプッシュ、展開時、およびデバイスがアクティブなときのプッシュ通知の例。]({% image_buster /assets/img_archive/push_ios_notification_states.png %})

{% alert note %}
展開時のプッシュ通知には2:1のアスペクト比を推奨していますが、ほぼすべてのアスペクト比に対応しています。画像は常に通知の幅いっぱいに表示され、高さはそれに応じて調整されます。
{% endalert %}

#### テキスト切り捨ての変動要因

コンテンツを作成する際には、テキストの表示量に影響する可能性のある以下のシナリオを考慮してください。

{% tabs %}
{% tab Timing %}

ユーザーがプッシュ通知に反応したタイミングに応じて、タイムスタンプによりタイトルテキストが短くなることがあります。

![タイムスタンプが「now」でタイトル文字数が35のプッシュ通知の例。]({% image_buster/assets/img_archive/push_ios_timing_35.png %})
<br>タイトルの文字数：**35**

![タイムスタンプが「3h ago」でタイトル文字数が33のプッシュ通知の例。]({% image_buster/assets/img_archive/push_ios_timing_33.png %})
<br>タイトルの文字数：**33**

![タイムスタンプが「Yesterday, 8:37 AM」でタイトル文字数が22のプッシュ通知の例。]({% image_buster/assets/img_archive/push_ios_timing_22.png %})
<br>タイトルの文字数：**22**

{% endtab %}
{% tab Images %}

画像がある場合、本文は1行につき約10文字短くなります。

![画像がなく、本文文字数が179のプッシュ通知の例。]({% image_buster/assets/img_archive/push_ios_images_179.png %})
<br>本文の文字数：**179**

![画像があり、本文文字数が154のプッシュ通知の例。]({% image_buster/assets/img_archive/push_ios_images_154.png %})
<br>本文の文字数：**154**

{% endtab %}
{% tab Interruption level %}

iOS 15では、Time SensitiveとCriticalの表記は、タイトルをタイムスタンプのない新しい行に押し下げ、少しスペースに余裕が生まれます。

![Time SensitiveまたはCriticalの表記がなく、タイトル文字数が35のプッシュ通知の例。]({% image_buster/assets/img_archive/push_ios_interruption_level_35.png %})
<br>タイトルの文字数：**35**

![Time Sensitiveの表記があり、タイトル文字数が39のプッシュ通知の例。]({% image_buster/assets/img_archive/push_ios_interruption_level_39.png %})
<br>タイトルの文字数：**39**

{% endtab %}
{% tab More %}

以下の詳細も、テキストの切り捨てに影響します。

- **端末の表示設定：** ユーザーは、通常アクセシビリティ上の理由から、端末のグローバルUIのフォントサイズを増減できます。
- **デバイスの幅：** メッセージは小さな携帯電話でも、幅の広いiPadでも表示される可能性があります。
- **コンテンツタイプ：** 絵文字、および「m」や「w」のような幅の広い文字は、「i」や「t」よりもスペースを取ります。また、「engagement」のように長い単語は、短い単語よりも突然改行されることがあります。

{% endtab %}
{% endtabs %}

## iOSのリッチプッシュ通知を設定する

### ステップ 1: プッシュキャンペーンを作成する

[キャンペーンの手順]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message)に従って、iOS用のプッシュ通知を作成します。リッチコンテンツを含まないプッシュ通知の設定に使用するのと同じコンポーザーを使います。

### ステップ 2: メディアを追加する

メッセージのコンポーザーにある**Rich Notification Media**フィールドに画像、GIF、オーディオ、ビデオファイルを追加します。コンテンツファイルを追加する方法については、[要件](#requirements)を参照してください。

![プッシュ通知のサマリーテキストの例。]({% image_buster /assets/img_archive/rich_notification_add_image.png %}){: style="max-width:70%;" }

このメッセージは、iOS 10を搭載したデバイスを持っているユーザーだけに送信するよう制限することもできます。iOS 10にアップグレードしていないユーザーの場合、**Only send to devices with Rich Notification support**のチェックを外しておくと、リッチコンテンツを含まないテキストのみの通知として表示されます。

![画像を追加したり、画像のURLを入力したりできる、展開時の通知画像セクション。]({% image_buster /assets/img_archive/rich_notification_ios10_select.png %}){: style="max-width:70%;" }

### ステップ 3: キャンペーンの作成を続ける

リッチプッシュ通知コンテンツがダッシュボードにアップロードされたら、[キャンペーンのスケジュール]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#schedule-push-campaign)を続行できます。

プッシュ通知を受信したユーザーは、プッシュメッセージを強く押して画像を展開できます。

![プッシュ通知を受信したユーザーがメッセージを強く押すと、「Hello!」という展開画像が表示されます。]({% image_buster /assets/img_archive/rich_notification_ios.gif %}){: style="max-width:50%;" }