---
nav_title: "プッシュアクションボタン"
article_title: プッシュアクションボタン
page_order: 1
page_type: reference
description: "この参考記事では、プッシュアクションボタンとは何か、iOS プラットフォームと Android プラットフォームの違いについて説明します。"
channel:
  - Push

---

# プッシュアクションボタン

![2 つのプッシュアクションボタンがある iOS プッシュ通知:承諾および拒否。] [1]{: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> プッシュアクションボタンを使用すると、Braze iOS および Android プッシュ通知を使用する際のボタンのコンテンツとアクションを設定できます。アクションボタンを使用すると、ユーザーはアプリエクスペリエンスをクリックしなくても、通知からアプリを直接操作できます。

## アクションボタンの作成

各インタラクティブボタンは、ウェブページまたはディープリンクにリンクしたり、アプリを開いたりできます。プッシュアクションボタンは、ダッシュボードのプッシュメッセージコンポーザーの **On-Click Behavior** セクションで指定できます。

{% alert important %}
1つのキャンペーンでiOSとAndroidの両方をターゲットにしたい場合は、マルチチャネルキャンペーンを作成してください。[クイックプッシュキャンペーンを使用してiOSとAndroidの両方をターゲットにする場合、プッシュアクションボタンはサポートされません]({{site.baseurl}}/quick_push)。
{% endalert %}

### iOS {#ios}

iOS プッシュメッセージでアクションボタンを使用するには、次の操作を行います。

1. iOS [プッシュキャンペーンを作成し]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/)、「**作成**」タブでアクションボタンを有効にします。
2. 以下のボタンの組み合わせから **iOS 通知カテゴリを選択します**。
 - 受諾する / 辞退する
 - はい / いいえ
 - 確認 / キャンセル
 - その他
 - 事前登録済みのカスタム iOS カテゴリ

![iOS Notification Category dropdown menu.]({% image_buster /assets/img_archive/push_action_buttons_ios.png %}){: style="max-width:70%"}

{% alert note %}
iOS ではボタンが処理されるため、プッシュアクションボタンを設定する際には追加の統合手順を実行する必要があります。[詳細については開発者向けドキュメントを参照してください]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/action_buttons/)。特に、iOSカテゴリを設定するか、特定のデフォルトボタンオプションから選択する必要があります。Android インテグレーションの場合、これらのボタンは自動的に機能します。
{% endalert %}

### Android{#android}

Android プッシュメッセージでアクションボタンを使用するには、次の操作を行います。

1. Android [プッシュキャンペーンを作成し]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/)、**作成タブで通知ボタンを有効にします**。
2. 「<i class="fas fa-plus-circle"></i>**ボタンを追加」** をクリックし、**ボタンのテキストとクリック時の動作を指定します**。次のアクションから選択できます。
  - アプリを開く
  - Web URL にリダイレクトする
  - [アプリケーションへのディープリンク]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/)

![\]({% image_buster /assets/img_archive/push_action_buttons_android.png %}){: style="max-width:70%"}

プッシュにはボタンを 3 つまで追加できます。

#### アンドロイドの文字数制限

積み重ねられている iOS ボタンとは異なり、Android のボタンは一列に並べて表示されます。つまり、追加するボタンが多いほど (最大 3 つ)、ボタンのコピーに必要なスペースが少なくなります。 

![Android push action buttons with truncated text.]({% image_buster /assets/img_archive/push_action_truncated.png %}){: style="max-width:50%" }

次の表は、ボタンの数に応じて、ボタンのコピーが切り捨てられるまでに追加できる文字数の概要を示しています。

| ボタン数 | ボタンあたりの最大文字数 |
| --- | --- |
| 1 | 46 キャラクター |
| 2 | 20 キャラクター |
| 3 | 11 キャラクター |
{: .reset-td-br-1 .reset-td-br-2}


[1]: {% image_buster /assets/img_archive/push_action_example.png %}
