---
nav_title: "プッシュ通知ストーリー"
article_title: プッシュ通知ストーリー
page_order: 2
page_type: reference
description: "この参考記事では、プッシュ・ストーリーとは何か、プッシュ・ストーリーを作成する方法、そしてよくある質問について説明する。"
channel:
  - push

---

# プッシュ通知ストーリー

> プッシュストーリーは、Brazeが導入した新しいタイプのプッシュ通知である。この機能は、インスタグラムやフェイスブックで普及した写真のカルーセル機能を取り入れたもので、マーケティング担当者は、リッチでまとまりのあるストーリーを伝えるプッシュ内のページのカルーセルを作成することができる。これらのページは、画像、クリックアクション、タイトル、説明文で構成されている。ユーザーはこれらのページをスワイプして、あなたが語るストーリーを見ることができる。

| Android の例 (展開表示) | IOSの例（拡大） |
| :-----: | :----------: |
| ![]({% image_buster /assets/img_archive/pushstories_android_preview.png %}) | ![]({% image_buster /assets/img_archive/pushstories_ios_preview.png %}) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
iOS SDKバージョン3.13.0以降では、SDKの画像ダウンロード方法の変更により、最初の画像のサムネイルがプッシュのコンデンスビューに表示されない。メッセージのコピーで、画像を見るためにプッシュを展開するよう必ずユーザーを促してください。
{% endalert %}

## 前提条件

プッシュストーリーを受信するには、以下のSDKバージョンが必要である：

{% sdk_min_versions swift:5.0.0 android:2.2.0 %}


## プッシュストーリーズの使い方

![]({% image_buster /assets/img_archive/pushstories_composer_dropdown2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

プッシュストーリーを使用するには、次の手順を実行します。

1. [プッシュキャンペーン]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/) を作成します。
2. **Notification Type**では、**プッシュストーリー**を選択します。
3. **iOS**または**Android**を選択します。プッシュメッセージの両方を選択した場合、プッシュストーリーを作成するオプションは表示されません。 

### プッシュストーリーの作曲家

ページを作成するには、以下の手順を実行する：

1. メインの作成画面から [**ページを管理**] をクリックします。
    <br><br>![]({% image_buster /assets/img_archive/pushstories_add_pages.png %}){: style="max-width:70%"}<br><br>
2. 各ページに画像を挿入し、その画像をクリックする動作を追加する。
3. 必要であれば、各ページに**タイトルと** **説明を**追加する。1つのページでタイトルとディスクリプションを使用する場合は、すべてのページに挿入する必要がある。

プレビューは反映され、インタラクティブなものとなる。

![]({% image_buster /assets/img_archive/pushstories_composer.png %}){: style="max-width:60%"}

{% alert important %}
[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content)で画像を取り込む場合は、画像の URL が `https://` で始まっていることを確認します。`http://` を使うとアプリがクラッシュする。
{% endalert %}

### 画像とテキストの仕様

以下の画像とテキストの仕様は、プッシュストーリーズのフォトカルーセル部分に適用される。ユーザーがプッシュストーリーを起動させるために操作する基本的なプッシュについては、[プッシュのテキストガイドラインを]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#native-mobile-push-notifications)参照のこと。

{% tabs %}
{% tab Images %}

- **画像比:**2:1（必須）
- **推奨画像サイズ**500 KB
- **最大画像サイズ：**5 MB
- **ファイルの種類:**PNG、JPEG

{% endtab %}
{% tab Text %}

- **Title:**30文字（推奨）
- **説明:**30文字（推奨）

{% alert note %}
デバイスによって文字の長さに多少の違いはあるが、プッシュストーリーのタイトルと説明文はそれぞれ1行に制限されている。メッセージの残りは切り捨てられる。メッセージは必ず実機でテストすること。
{% endalert %}

{% endtab %}
{% endtabs %}

### プッシュ・ストーリーのセグメンテーション

キャンペーンやキャンバスを作成する際、プッシュストーリーページをクリックしたかどうかに基づいて、ターゲットとするユーザーを絞り込むことができる。次に、ユーザーをターゲットにするために使用するキャンペーンとページを選択します。

### プッシュストーリーズ分析

分析は、プッシュ通知の現行の分析セクションとよく似ています。Push Stories分析では、**Direct Opens**指標を開いてページごとのクリック数を見ることができる。

![iOS のプッシュパフォーマンス表には、分析サンプルと直接開封数指標の詳細が表示されます。]({% image_buster /assets/img_archive/pushstories_analytics.png %})

## トラブルシューティング

### iOS

#### 自分自身にプッシュストーリーを送ったが、通知は届かなかった。

アップルは、さまざまな要因に基づいて、特定の種類の通知がデバイスに送信されないようにする特定のルールを設けている。これには、顧客のデータプラン、通知サイズ、顧客のストレージ容量の評価が含まれます。その結果、顧客に通知が送られないこともあります。

これらは、プッシュストーリーをデザインする際に考慮すべき、アップルが課す制限である。

#### 自分自身にプッシュストーリーを送ったが、代わりに凝縮されたビューを見た。

例えば、データ接続が失われた場合など、すべてのページがロードされない状況では、プッシュストーリーは凝縮された通知のみを表示する。

### Android

#### 画像をクリックしてもプッシュストーリーが解除されない 

デフォルトでは、Androidではユーザーが画像をクリックしてもプッシュストーリーは解除されない。通知を解除したい場合は、[`cancelNotification`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/index.html#-1466259649%2FFunctions%2F-1725759721) を呼び出します。  

