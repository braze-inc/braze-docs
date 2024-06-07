---
nav_title: "プッシュ通知ストーリー"
article_title: プッシュ通知ストーリー
page_order: 2
page_type: reference
description: "このリファレンス記事では、プッシュストーリーとは何か、作成方法、よくある質問について説明します。"
channel:
  - push

---

# プッシュ通知ストーリー

> プッシュストーリーは、Brazeが導入した新しいタイプのプッシュ通知です。この機能は、InstagramやFacebookで普及している写真カルーセル機能を採用し、マーケターがプッシュ内でページのカルーセルを作成し、豊かでまとまりのあるストーリーを伝えることを可能にします。これらのページは、画像、クリックアクション、タイトル、説明で構成されます。ユーザーはこれらのページをスワイプして、管理者が伝えたストーリーを表示できます。

|Android の例 (拡張) |IOS の例(拡張) |
| :-----: | :----------: |
| ![][1] | ![][2] |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
iOS SDK バージョン 3.13.0+ では、SDK によるイメージのダウンロード方法が変更されたため、最初のイメージのサムネイルはプッシュの要約ビューに表示されません。メッセージのコピーで、プッシュを展開して画像を表示するようにユーザーに求めるプロンプトが表示されるようにします。
{% endalert %}

## 前提 条件

プッシュストーリーを受信するには、次のSDKバージョンが必要です。

{% sdk_min_versions swift:5.0.0 android:2.2.0 %}


## プッシュストーリーの使い方

![][6]{: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

プッシュストーリーを使用するには、[プッシュキャンペーン]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/)を作成し、**通知タイプ**として**プッシュストーリー**を選択します。

### プッシュストーリーコンポーザー

ページを作成するには、次の手順を実行します。

1. メインコンポーザーから **「ページを管理** 」をクリックします。
    <br><br>![][4]{: style="max-width:70%"}<br><br>
2. 各ページの画像と、その画像のクリック動作を挿入します。
3. 必要に応じて、各ページの **[タイトル]** と **[説明** ] を追加します。1 つのページにタイトルと説明を使用する場合は、すべてのページに挿入する必要があります。

プレビューが反映され、インタラクティブになります。

![][3]{: style="max-width:60%"}

{% alert important %}
[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content)を含む画像を取り込む場合は、画像の URL が で始まっ`https://`ていることを確認します。使用する `http://` と、アプリがクラッシュします。
{% endalert %}

### 画像とテキストの仕様

次の画像とテキストの仕様は、Pushストーリーの写真カルーセル部分に適用されます。プッシュストーリーをアクティブ化するためにユーザーが操作する基本的なプッシュについては、 [プッシュのテキストガイドライン]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#native-mobile-push-notifications)を参照してください。

{% tabs %}
{% tab Images %}

- **画像比率:**2:1 (必須)
- **推奨画像サイズ:**500 KB
- **最大画像サイズ:**5 MB
- **ファイルの種類:**PNG、JPEG

{% endtab %}
{% tab Text %}

- **Title:**30 文字以内 (推奨)
- **説明:**30 文字以内 (推奨)

{% alert note %}
デバイスによって文字の長さに多少の違いがあるかもしれませんが、プッシュストーリーのタイトルと説明はそれぞれ1行に制限されています。メッセージの残りの部分は切り捨てられます。メッセージは必ず実機でテストしてください。
{% endalert %}

{% endtab %}
{% endtabs %}

### プッシュストーリーのセグメンテーション

キャンペーンまたはキャンバスを作成する際、プッシュストーリーページをクリックしたかどうかに基づいて、ターゲットとするユーザーをフィルタリングできます。次に、ユーザーのターゲティングに使用するキャンペーンとページを選択します。

### プッシュストーリー分析

分析は、プッシュ通知の現在の分析セクションと非常によく似ています。プッシュストーリー分析では、 **ダイレクトオープン** 指標を開いて、ページごとのクリック数を表示できます。

![iOS プッシュ パフォーマンスの表には、サンプル分析とダイレクト オープン メトリックの詳細が拡張されています。[5]

## トラブルシューティング

### iOS

#### 自分にプッシュストーリーを送信しましたが、通知が届きません

Appleには、さまざまな要因に基づいて特定の種類の通知がデバイスに送信されないようにする特定のルールがあります。これには、顧客のデータプラン、通知サイズ、および顧客のストレージ容量の評価が含まれます。その結果、顧客に通知が送信されない場合があります。

これらはAppleによって課せられた制限であり、プッシュストーリーを設計する際に考慮する必要があります。

#### 私は自分自身にプッシュストーリーを送ったが、代わりに凝縮されたビューを見た

データ接続が失われた場合など、すべてのページが読み込まれない特定の状況では、プッシュストーリーには要約された通知のみが表示されます。

### Android

#### プッシュストーリーが画像をクリックしても閉じない 

デフォルトでは、ユーザーが画像をクリックした後、Androidではプッシュストーリーは閉じられません。通知を閉じるには、 に電話してください [`cancelNotification`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/index.html#-1466259649%2FFunctions%2F-1725759721)。  

[1]: {% image_buster /assets/img_archive/pushstories_android_preview.png %}
[2]: {% image_buster /assets/img_archive/pushstories_ios_preview.png %}
[3]: {% image_buster /assets/img_archive/pushstories_composer.png %}
[4]: {% image_buster /assets/img_archive/pushstories_add_pages.png %}
[5]: {% image_buster /assets/img_archive/pushstories_analytics.png %}
[6]: {% image_buster /assets/img_archive/pushstories_composer_dropdown2.png %}
