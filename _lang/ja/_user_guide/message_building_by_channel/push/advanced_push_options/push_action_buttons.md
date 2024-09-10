---
nav_title: "プッシュ・アクション・ボタン"
article_title: プッシュ・アクション・ボタン
page_order: 1
page_type: reference
description: "この参考記事では、プッシュ・アクション・ボタンとは何か、iOSとAndroidのプラットフォームにおける違いについて説明する。"
channel:
  - Push

---

# アクションボタンを押す

![2つのプッシュアクションボタンを備えたiOSのプッシュ通知：受諾と拒否][1]{: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> プッシュアクションボタンを使用すると、BrazeのiOSおよびAndroidプッシュ通知を使用する際に、ボタンのコンテンツとアクションを設定できる。アクションボタンを使えば、ユーザーはアプリをクリックしなくても、通知から直接アプリと対話することができる。

## アクションボタンを作成する

各インタラクティブ・ボタンは、ウェブページやディープリンクにリンクしたり、アプリを開いたりすることができる。プッシュアクションボタンは、ダッシュボードのプッシュメッセージコンポーザーの**On-Click Behavior**セクションで指定できる。

{% alert important %}
1つのキャンペーンでiOSとAndroidの両方をターゲットにしたい場合は、マルチチャネルキャンペーンを作成する。[クイックプッシュキャンペーンを]({{site.baseurl}}/quick_push)使用してiOSとAndroidの両方をターゲットにする場合、プッシュアクションボタンはサポートされない。
{% endalert %}

### iOS{#ios}

iOSのプッシュ・メッセージでアクション・ボタンを使うには、以下のようにする：

1. iOSの[プッシュキャンペーンを]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/)作成し、「**メール送信」**タブでアクションボタンを有効にする。
2. 以下の利用可能なボタンの組み合わせから、**iOSの通知カテゴリーを**選択する：
 - 受諾する／拒否する
 - はい／いいえ
 - 確認／キャンセル
 - もっと見る
 - 事前登録されたカスタムiOSカテゴリー

![iOS 通知カテゴリのドロップダウンメニュー]({% image_buster /assets/img_archive/push_action_buttons_ios.png %}){: style="max-width:70%"}

{% alert note %}
iOSのボタンの取り扱いのため、プッシュアクションボタンを設定する際には追加の統合手順を実行する必要があります。これらの手順は、当社の[開発者ドキュメント]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/action_buttons/)に記載されています。特に、iOSカテゴリーを設定するか、特定のデフォルトボタンオプションから選択する必要がある。アンドロイドとの統合では、これらのボタンは自動的に機能する。
{% endalert %}

### Android{#android}

Androidのプッシュ・メッセージでアクション・ボタンを使うには、以下のようにする：

1. Androidの[プッシュ・キャンペーンを]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/)作成し、「**メール作成」**タブで通知ボタンを有効にする。
2. <i class="fas fa-plus-circle"></i> **Add Buttonを**クリックし、ボタンテキストと**On-Click Behaviorを**指定する。以下のアクションから選択できる：
  - アプリを開く
  - ウェブURLにリダイレクトする
  - [アプリケーションへのディープリンク]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/)

![]({% image_buster /assets/img_archive/push_action_buttons_android.png %}){: style="max-width:70%"}

プッシュのボタンは3つまで追加できる。

#### アンドロイドの文字数制限

重ねて表示されるiOSのボタンとは異なり、Androidのボタンは横一列に並んで表示される。つまり、ボタンを増やせば増やすほど（最大3つまで）、ボタンコピーのスペースは少なくなる。 

![テキストが切り捨てられたAndroidのプッシュ・アクション・ボタン]({% image_buster /assets/img_archive/push_action_truncated.png %}){: style="max-width:50%" }

次の表は、ボタンの数に応じて、ボタンコピーが切り捨てられるまでに追加できる文字数の概要を示したものである：

| ボタン数 | ボタンあたりの最大文字数 |
| --- | --- |
| 1 | 46文字 |
| 2 | 20文字 |
| 3 | 11文字 |
{: .reset-td-br-1 .reset-td-br-2}


[1]: {% image_buster /assets/img_archive/push_action_example.png %}
