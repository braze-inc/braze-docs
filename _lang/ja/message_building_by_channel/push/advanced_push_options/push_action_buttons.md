---
nav_title: "プッシュアクションボタン"
article_title: プッシュアクションボタン
page_order: 1
page_type: reference
description: "この参考記事では、プッシュ・アクション・ボタンとは何か、iOSとAndroidのプラットフォームにおける違いについて説明する。"
channel:
  - Push

---

# プッシュアクションボタン

![2つのプッシュアクションボタンを備えたiOSのプッシュ通知：受諾と拒否]({% image_buster /assets/img_archive/push_action_example.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> プッシュアクションボタンを使用すると、BrazeのiOSおよびAndroidプッシュ通知を使用する際に、ボタンのコンテンツとアクションを設定できる。アクションボタンを使用すると、ユーザーはアプリエクスペリエンスをクリックすることなく、通知からアプリと直接対話できます。

## アクションボタンを作成する

各操作ボタンは、Web ページやディープリンクにリンクしたり、アプリを開いたりできます。 

- 標準的なプッシュキャンペーンでは、プッシュアクションボタンは、ダッシュボードのプッシュメッセージ作成画面の [**クリック時動作**] セクションで指定できます。
- [クイックプッシュキャンペーン]({{site.baseurl}}/quick_push)では、アクションボタンは [**設定**] タブでプラットフォーム別に個別に設定できます。

{% tabs %}
{% tab iOS %}
### iOS{#ios}

iOSのプッシュ・メッセージでアクション・ボタンを使うには、以下のようにする：

1. 標準的なキャンペーンの場合は [**作成**] タブで、クイックプッシュの場合は [**設定**] タブでアクションボタンをオンにします。
2. 以下の利用可能なボタンの組み合わせから、**iOSの通知カテゴリーを**選択する：
 - 受諾する／拒否する
 - はい／いいえ
 - 確認／キャンセル
 - もっと見る
 - 事前登録されたカスタムiOSカテゴリー

![iOS 通知カテゴリのドロップダウンメニュー]({% image_buster /assets/img_archive/push_action_buttons_ios.png %})({: style="max-width:70%"})

{% alert note %}
iOS でのボタンの処理に起因して、プッシュアクションボタンを設定するときには追加の連携手順を実行する必要があります。これらの手順は、当社の[開発者ドキュメント]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories)で概説しています。特に、iOSカテゴリーを設定するか、特定のデフォルトボタンオプションから選択する必要がある。Android との連携の場合、これらのボタンは自動的に機能します。
{% endalert %}
{% endtab %}
{% tab Android %}
### Android{#android}

Androidのプッシュ・メッセージでアクション・ボタンを使うには、以下のようにする：

1. 標準的なキャンペーンの場合は [**作成**] タブで、クイックプッシュの場合は [**設定**] タブでアクションボタンをオンにします。
2. **[追加] ボタン** <i class="fas fa-plus-circle"></i> を選択し、ボタンテキストと [**クリック時動作**] を指定します。次の使用できるアクションを選択できます。
  - アプリを開く
  - ウェブURLにリダイレクトする
  - [アプリケーションへのディープリンク]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/)

![通知ボタンのクリック時の動作として [アプリを開く] を選択する。]({% image_buster /assets/img_archive/push_action_buttons_android.png %})({: style="max-width:70%"})

プッシュのボタンは3つまで追加できる。

#### Android の文字数制限

重ねて表示されるiOSのボタンとは異なり、Androidのボタンは横一列に並んで表示される。つまり、追加するボタンが増えるほど (最大 3 つ)、ボタンの説明のスペースは少なくなります。 

![テキストが切り捨てられたAndroidのプッシュ・アクション・ボタン]({% image_buster /assets/img_archive/push_action_truncated.png %})({: style="max-width:50%"})

次の表に、ボタンのテキストが切り詰められるまでに追加できる文字数を、ボタンの数に応じて示します。

| ボタン数 | ボタンあたりの最大文字数 |
| --- | --- |
| 1 | 46文字 |
| 2 | 20文字 |
| 3 | 11文字 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

