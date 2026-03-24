---
nav_title: "Push Stories"
article_title: Push Stories
page_order: 2
page_type: reference
description: "この参考記事では、Push Stories とは何か、作成方法、およびよくある質問について説明します。"
channel:
  - push

---

# Push Stories

> Push Stories は、Braze が導入した新しいタイプのプッシュ通知です。この機能は、Instagram や Facebook で普及した写真カルーセル機能を取り入れたもので、マーケターがリッチでまとまりのあるストーリーを伝えるプッシュ内のページカルーセルを作成できます。これらのページは、画像、クリックアクション、タイトル、説明で構成されています。ユーザーはこれらのページをスワイプして、あなたが語るストーリーを閲覧できます。

| Android の例（展開表示） | iOS の例（展開表示） |
| :-----: | :----------: |
| ![]({% image_buster /assets/img_archive/pushstories_android_preview.png %}) | ![]({% image_buster /assets/img_archive/pushstories_ios_preview.png %}) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
iOS SDK バージョン 3.13.0 以降では、SDK の画像ダウンロード方法の変更により、最初の画像のサムネイルがプッシュの縮小表示に表示されません。画像を見るためにプッシュを展開するようユーザーに促すメッセージコピーにしてください。
{% endalert %}

## 前提条件

Push Stories を受信するには、以下の SDK バージョンが必要です。

{% sdk_min_versions swift:5.0.0 android:2.2.0 %}


## Push Stories の使い方

![]({% image_buster /assets/img_archive/pushstories_composer_dropdown2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Push Stories を使用するには、以下の手順を実行します。

1. [プッシュキャンペーン]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/)を作成します。
2. **Notification Type** で **Push Stories** を選択します。
3. **iOS** または **Android** を選択します。プッシュメッセージで両方を選択した場合、Push Stories を作成するオプションは表示されません。

### Push Stories コンポーザー

ページを作成するには、以下のステップを実行します。

1. メインのコンポーザーから [**Manage Pages**] をクリックします。
    <br><br>![]({% image_buster /assets/img_archive/pushstories_add_pages.png %}){: style="max-width:70%"}<br><br>
2. 各ページに画像を挿入し、その画像のクリック動作を設定します。
3. 必要に応じて、各ページに**タイトル**と**説明**を追加します。1つのページでタイトルと説明を使用する場合は、すべてのページに挿入する必要があります。

プレビューはリアルタイムで反映され、インタラクティブに操作できます。

![]({% image_buster /assets/img_archive/pushstories_composer.png %}){: style="max-width:60%"}

{% alert important %}
[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content)で画像を取り込む場合は、画像の URL が `https://` で始まっていることを確認してください。`http://` を使用するとアプリがクラッシュします。
{% endalert %}

### 画像とテキストの仕様

以下の画像とテキストの仕様は、Push Stories のフォトカルーセル部分に適用されます。ユーザーが Push Stories を起動するために操作する基本的なプッシュについては、[プッシュの画像とテキストの仕様]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push)を参照してください。

{% tabs %}
{% tab Images %}

- **画像比率:** 2:1（必須）
- **推奨画像サイズ:** 500 KB
- **最大画像サイズ:** 5 MB
- **ファイルタイプ:** PNG、JPEG

{% endtab %}
{% tab Text %}

- **タイトル:** 30文字（推奨）
- **説明:** 30文字（推奨）

{% alert note %}
デバイスによって文字の長さに多少の違いはありますが、Push Stories のタイトルと説明はそれぞれ1行に制限されています。メッセージの残りの部分は切り捨てられます。必ず実機でメッセージをテストしてください。
{% endalert %}

{% endtab %}
{% endtabs %}

### Push Stories のセグメンテーション

キャンペーンやキャンバスを作成する際、Push Stories ページをクリックしたかどうかに基づいてターゲットとするユーザーをフィルタリングできます。次に、ユーザーをターゲットにするために使用するキャンペーンとページを選択します。

### Push Stories の分析

分析は、プッシュ通知の現行の分析セクションとよく似ています。Push Stories の分析では、**直接開封**指標を開いてページごとのクリック数を確認できます。

![iOS のプッシュパフォーマンステーブルには、分析サンプルと直接開封指標の詳細が表示されます。]({% image_buster /assets/img_archive/pushstories_analytics.png %})

## トラブルシューティング

### iOS

#### 自分自身に Push Stories を送ったが、通知を受信しなかった

Apple は、さまざまな要因に基づいて特定の種類の通知がデバイスに送信されないようにする特定のルールを設けています。これには、顧客のデータプラン、通知サイズ、顧客のストレージ容量の評価が含まれます。その結果、顧客に通知が送信されないこともあります。

これらは Apple が課す制限であり、Push Stories をデザインする際に考慮する必要があります。

#### 自分自身に Push Stories を送ったが、縮小表示が表示された

データ接続の喪失などにより、すべてのページが読み込まれない状況では、Push Stories は縮小された通知のみを表示します。

### Android

#### 画像をクリックしても Push Stories が閉じない

デフォルトでは、Android ではユーザーが画像をクリックしても Push Stories は閉じません。通知を閉じたい場合は、[`cancelNotification`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/index.html#-1466259649%2FFunctions%2F-1725759721) を呼び出してください。