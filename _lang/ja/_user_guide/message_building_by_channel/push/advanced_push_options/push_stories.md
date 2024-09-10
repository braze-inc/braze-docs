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

| アンドロイドの例（拡大） | IOSの例（拡大） |
| :-----: | :----------: |
| ![][1] | ![][2] |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
iOS SDKバージョン3.13.0以降では、SDKの画像ダウンロード方法の変更により、最初の画像のサムネイルがプッシュのコンデンスビューに表示されない。メッセージのコピーで、画像を見るためにプッシュを展開するようユーザーを促すようにする。
{% endalert %}

## 前提条件

プッシュストーリーを受信するには、以下のSDKバージョンが必要である：

{% sdk_min_versions swift:5.0.0 android:2.2.0 %}


## プッシュストーリーズの使い方

![][6]{: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

プッシュストーリーズを使用するには、[プッシュキャンペーンを]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/)作成し、**通知タイプとして** **プッシュストーリーズを**選択する。

### プッシュストーリーの作曲家

ページを作成するには、以下の手順を実行する：

1. メインコンポーザーから**ページの管理を**クリックする。
    <br><br>![][4]{: style="max-width:70%"}<br><br>
2. 各ページに画像を挿入し、その画像をクリックする動作を追加する。
3. 必要であれば、各ページに**タイトルと** **説明を**追加する。1つのページでタイトルとディスクリプションを使用する場合は、すべてのページに挿入する必要がある。

プレビューは反映され、インタラクティブなものとなる。

![][3]{: style="max-width:60%"}

{% alert important %}
[コネクテッド・コンテンツで]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content)画像を取り込む場合は、画像のURLが`https://` で始まっていることを確認する。`http://` を使うとアプリがクラッシュする。
{% endalert %}

### 画像とテキストの仕様

以下の画像とテキストの仕様は、プッシュストーリーズのフォトカルーセル部分に適用される。ユーザーがプッシュストーリーを起動させるために操作する基本的なプッシュについては、[プッシュのテキストガイドラインを]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#native-mobile-push-notifications)参照のこと。

{% tabs %}
{% tab 画像 %}

- **画像の比率だ：**2:1（必須）
- **推奨画像サイズ**500 KB
- **最大画像サイズ：**5 MB
- **ファイルの種類:**PNG、JPEG

{% endtab %}
{% tab テキスト %}

- **Title:**30文字（推奨）
- **説明:**30文字（推奨）

{% alert note %}
デバイスによって文字の長さに多少の違いはあるが、プッシュストーリーのタイトルと説明文はそれぞれ1行に制限されている。メッセージの残りは切り捨てられる。メッセージは必ず実機でテストすること。
{% endalert %}

{% endtab %}
{% endtabs %}

### プッシュ・ストーリーのセグメンテーション

キャンペーンやキャンバスを作成する際、プッシュストーリーページをクリックしたかどうかに基づいて、ターゲットとするユーザーを絞り込むことができる。次に、キャンペーンとユーザーをターゲットにするページを選択する。

### プッシュストーリーズ分析

アナリティクスは、現在のプッシュ通知のアナリティクス・セクションと非常によく似ている。Push Stories分析では、**Direct Opens**指標を開いてページごとのクリック数を見ることができる。

![iOSのプッシュパフォーマンス表には、分析サンプルとDirect Opens指標の詳細が掲載されている。][5]

## トラブルシューティング

### iOS

#### 自分自身にプッシュストーリーを送ったが、通知は届かなかった。

アップルは、さまざまな要因に基づいて、特定の種類の通知がデバイスに送信されないようにする特定のルールを設けている。これには、顧客のデータプラン、通知サイズ、顧客のストレージ容量の評価が含まれる。その結果、顧客に通知が送られないこともある。

これらは、プッシュストーリーをデザインする際に考慮すべき、アップルが課す制限である。

#### 自分自身にプッシュストーリーを送ったが、代わりに凝縮されたビューを見た。

例えば、データ接続が失われた場合など、すべてのページがロードされない状況では、プッシュストーリーは凝縮された通知のみを表示する。

### Android

#### 画像をクリックしてもプッシュストーリーが解除されない 

デフォルトでは、Androidではユーザーが画像をクリックしてもプッシュストーリーは解除されない。通知を解除したい場合は、次のように電話する。 [`cancelNotification`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/index.html#-1466259649%2FFunctions%2F-1725759721).  

[1]: {% image_buster /assets/img_archive/pushstories_android_preview.png %}
[2]: {% image_buster /assets/img_archive/pushstories_ios_preview.png %}
[3]: {% image_buster /assets/img_archive/pushstories_composer.png %}
[4]: {% image_buster /assets/img_archive/pushstories_add_pages.png %}
[5]: {% image_buster /assets/img_archive/pushstories_analytics.png %}
[6]: {% image_buster /assets/img_archive/pushstories_composer_dropdown2.png %}
