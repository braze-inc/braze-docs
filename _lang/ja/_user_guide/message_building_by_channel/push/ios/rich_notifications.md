---
nav_title: "iOS リッチ通知を作成する"
article_title: リッチプッシュ通知を作成する
page_order: 3
page_type: tutorial
description: "このチュートリアルでは、Braze キャンペーン用の iOS リッチ通知を作成するための要件と手順について説明します。"

platform: iOS
channel:
  - push
tool:
  - Campaigns

---

# iOSのリッチ通知を作成する

> リッチ通知を使用すると、コピー以外のコンテンツを追加することで、プッシュ通知をさらにカスタマイズできます。Android の通知では、以前からプッシュ通知に画像が含まれており、「拡張通知画像」としてメッセージが表示されています。iOS 10 以降では、顧客は GIF、画像、ビデオ、またはオーディオを含む iOS プッシュ通知を受信できるようになります。

## 要件

- アプリがリッチ通知を送信できるようにするには、開発者がアプリにサービス拡張機能を追加する必要があるため、[iOS プッシュ統合の][1] 手順に従ってください。
- メディアの制限と仕様については [、Apple のドキュメント][2] も参照してください。

> 2020 年 1 月現在、iOS リッチ プッシュ通知では 10 MB 未満であれば 1038x1038 の画像を処理できますが、できるだけ小さいファイル サイズを使用することをお勧めします。実際には、大きなファイルを送信すると、ネットワークに不要なストレスが発生し、ダウンロードのタイムアウトが頻繁に発生する可能性があります。

- iOS は、画面に収まるように画像を拡大縮小し、アクティブまたはロックされたビューに合わせてリッチ画像を拡大縮小します。
- 現在、ダッシュボード内で直接アップロードできるファイルの種類には、JPEG、PNG、GIF などがあります。これらのファイルは、次の追加ファイル タイプとともに、テンプレート可能な URL フィールドに入力することもできます。AIF、M4A、MP3、MP4、または WAV。

### 文字カウント

プッシュに含める文字数の正確な数について厳格なルールを提供することはできませんが、iOS メッセージを設計する際に考慮すべき [ガイドラインをいくつか提供します]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/) 。画像の有無、ユーザーの端末の通知状態や表示設定、端末のサイズなどにより多少の差異が生じる場合があります。疑問がある場合は、簡潔にまとめましょう。

> 一般的な目安として、Braze では、モバイル プッシュ通知のオプションのタイトルとメッセージ本文の両方について、各行のテキストを約 30 ～ 40 文字に抑えることを推奨しています。

#### 通知の状態

ユーザーはさまざまな状況でプッシュ通知を表示する可能性があり、次のようにテキストの長さも異なる場合があります。

<table>
<thead>
  <tr>
    <th>ロック画面または通知センター</th>
    <th>展開済み</th>
    <th>デバイスがアクティブです</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td width="33%">これは最も一般的なシナリオです。<br><br><b>Title:</b>1行のテキスト<br><b>体：</b>4行のテキスト<br><b>画像:</b> 正方形のサムネイル</td>
    <td width="33%">ユーザーがメッセージを長押ししたとき。<br><br><b>Title:</b>1行のテキスト<br><b>体：</b>7行のテキスト<br><b>画像：</b>2:1 アスペクト比 (推奨、以下の注記を参照)</td>
    <td width="33%">携帯電話がロック解除されアクティブなときにユーザーがプッシュを受信した場合。<br><br><b>Title:</b>1行のテキスト<br><b>体：</b>2行のテキスト</td>
  </tr>
</tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

![Example push notifications for push displayed on the lock screen, when expanded, and when device is active.]({% image_buster /assets/img_archive/push_ios_notification_states.png %})

{% alert note %}
拡張プッシュ通知には 2:1 のアスペクト比を推奨しますが、ほぼすべてのアスペクト比がサポートされています。画像は常に通知の幅全体に広がり、高さはそれに応じて調整されます。
{% endalert %}

#### テキスト切り捨ての変数

コンテンツを作成するときは、表示されるテキストの量に影響する可能性のある次のシナリオを考慮してください。

{% tabs %}
{% tab Timing %}

##### タイミング

ユーザーがプッシュ通知にいつ反応するかに応じて、タイムスタンプによってタイトルテキストが短縮されることがあります。

![Example push notification with a timestamp of "now" and title character count of 35.]({% image_buster/assets/img_archive/push_ios_timing_35.png %})
<br>タイトルの文字数:**35**

![Example push notification with a timestamp of "3h ago" and title character count of 33.]({% image_buster/assets/img_archive/push_ios_timing_33.png %})
<br>タイトルの文字数:**33**

![Example push notification with a timestamp of "Yesterday, 8:37 AM" and title character count of 22.]({% image_buster/assets/img_archive/push_ios_timing_22.png %})
<br>タイトルの文字数:**22**

{% endtab %}
{% tab Images %}

##### 画像

画像がある場合、本文は 1 行あたり約 10 文字短縮されます。

![Example push notification with no image and a body character count of 179.]({% image_buster/assets/img_archive/push_ios_images_179.png %})
<br>本文の文字数:**179**

![Example push notification with an image and a body character count of 154.]({% image_buster/assets/img_archive/push_ios_images_154.png %})
<br>本文の文字数:**154**

{% endtab %}
{% tab Interruption level %}

##### 中断レベル（iOS 15）

Time Sensitive および Critical の指定では、タイトルがタイムスタンプなしで新しい行に押し下げられ、少しスペースが増えます。

![Example push notification with no Time Sensitive or Critical denotation and a title character count of 35.]({% image_buster/assets/img_archive/push_ios_interruption_level_35.png %})
<br>タイトルの文字数:**35**

![Example push notification with a Time Sensitive denotation and a title character count of 39.]({% image_buster/assets/img_archive/push_ios_interruption_level_39.png %})
<br>タイトルの文字数:**39**

{% endtab %}
{% tab More %}

##### その他

次のこともテキストの切り捨てに影響します。

- **電話の表示設定:** ユーザーは、通常はアクセシビリティ上の理由から、電話のグローバル UI フォント サイズを拡大または縮小できます。
- **デバイスの幅:** メッセージは、小さな携帯電話でも、幅の広い iPad でも表示できます。
- **コンテンツ タイプ:** 絵文字や「m」や「w」などの幅の広い文字は、「i」や「t」よりも多くのスペースを占め、「engagement」などの長い単語は短い単語よりも急に行が折り返されることがあります。

{% endtab %}
{% endtabs %}

## iOSのリッチ通知を設定する

### ステップ 1:キャンペーンを作成する

[キャンペーンの手順][3] に従って、iOS 用のプッシュ通知を作成します。リッチ コンテンツを含まないプッシュ通知を設定するために使用するのと同じコンポーザーを使用します。

### ステップ 2:メディアを追加

メッセージの作成者の **「リッチ通知メディア」** フィールドに画像、GIF、オーディオ、またはビデオ ファイルを追加します。コンテンツ ファイルを追加する方法については、 [要件](#requirements) を参照してください。

![][4]{: style="max-width:70%;" }

このメッセージを、iOS 10 を実行するデバイスを持つユーザーにのみ送信するように制限することもできます。iOS 10 にアップグレードしていないユーザーの場合、**「リッチ通知をサポートするデバイスにのみ送信する」の** チェックを外すと、リッチ コンテンツのないテキストのみの通知が表示されます。

![][5]{: style="max-width:70%;" }

### ステップ 3:キャンペーンの作成を続ける

リッチ通知コンテンツがダッシュボードにアップロードされたら、[キャンペーンのスケジュール設定][6]を続行できます。

ユーザーがプッシュ通知を受信すると、プッシュ メッセージを強く押すと画像を拡大できます。

![ユーザーがプッシュ通知を受信し、メッセージを強く押すと、「Hello!」という拡大画像が表示されます。][8]{: style="max-width:50%;" }

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications
[2]: https://developer.apple.com/reference/usernotifications/unnotificationattachment
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[4]: {% image_buster /assets/img_archive/rich_notification_add_image.png %}
[5]: {% image_buster /assets/img_archive/rich_notification_ios10_select.png %}
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#schedule-push-campaign
[8]: {% image_buster /assets/img_archive/rich_notification_ios.gif %}
