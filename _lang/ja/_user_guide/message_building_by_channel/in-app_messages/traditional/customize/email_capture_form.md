---
nav_title: メール・キャプチャ・フォーム
article_title: メール・キャプチャ・フォーム
page_order: 3
page_type: reference
description: "この記事では、アプリ内メッセージタイプのメールキャプチャーの概要を説明する。"
channel:
  - in-app messages
---

# 電子メール・キャプチャ・フォーム {#email-capture-form}

> Eメールキャプチャメッセージを使えば、サイトのユーザーにEメールアドレスの送信を簡単に促すことができる。

エンドユーザーがこのフォームにEメールアドレスを入力すると、そのEメールアドレスがユーザープロファイルに追加される。

- まだアカウントを持っていない[匿名ユーザーの]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#anonymous-user-profiles)場合、メールアドレスは、ユーザーのデバイスに紐付けられた匿名ユーザープロファイルに登録される。
- ユーザー・プロフィールにすでにEメールアドレスが存在する場合、既存のEメールアドレスは新しく入力されたEメールアドレスで上書きされる。
- 既知のユーザーのメールアドレスが[ハードバウンスの]({{site.baseurl}}/help/help_articles/email/email_bounces#email-bounces)フラグが立っている場合、新しく入力されたメールアドレスがBrazeのプロフィールに登録されているものと異なるかどうかを確認する。提供されたEメールアドレスが異なる場合、Eメールアドレスは更新され、ハードバウンスのステータスは削除される。 
- ユーザーが無効なメールアドレスを入力した場合、エラーメッセージが表示される：「有効なEメールを入力してください。
    - メールアドレスが無効である： 
        - `example`
        - `example@`
        - `@gmail.com`
        - `example@gmail`
    - 有効なメールアドレス 
        - `example@gmail.com`
        - `example@gnail.com` (誤字あり）
    - BrazeにおけるEメール検証の詳細については、[Eメール技術ガイドラインとノートを]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/email_validation/)参照のこと。

{% details 特定ユーザーと匿名ユーザーの比較 %}

一般的に、Eメールキャプチャフォームのロジックは単純だ。Brazeのユーザープロフィールに、現在アクティブなユーザーのEメールアドレスを設定する。しかしそれは、ユーザーが特定されている（ログインしている、`changeUser` 呼び出されている）か否かで、動作が異なることを意味する。

匿名ユーザーがフォームに電子メールを入力して送信すると、Brazeはその電子メールアドレスをプロフィールに追加する。もし、`changeUser` がウェブの旅の後半で呼び出され、新しい`external_id` が割り当てられた場合（新規ユーザーがサービスに登録した場合など）、メールアドレスを含むすべての匿名ユーザー・プロフィール・データが統合される。

`changeUser` が既存の`external_id` で呼び出された場合、匿名ユーザープロファイルは孤児となり、特定ユー ザーにまだ存在しない[特定のユーザープロファイルのデータフィールドは]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior)マージされるが、E メールアドレスを含め、すでに存在するフィールドは失われる。

詳細については、[ユーザープロファイルのライフサイクルを]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/)参照のこと。

{% enddetails %}

## ステップ 1:アプリ内メッセージキャンペーンを作成する

このオプションに移動するには、アプリ内メッセージングキャンペーンを作成する必要がある。そこから、ユースケースに応じて、「**送信**先」を「**ウェブブラウザ**」、「**モバイルアプリ**」、「**モバイルアプリとウェブブラウザの両方**」のいずれかに設定し、**メッセージタイプとして**「**メールキャプチャフォーム**」を選択する。

![][4]

{% alert note %}
Web SDKを通じてHTMLアプリ内メッセージを有効にするには、Brazeに`allowUserSuppliedJavascript` の初期化オプションを与える必要がある。例えば、`braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})` 。HTMLのアプリ内メッセージはJavaScriptを実行することができるため、セキュリティ上の理由から、サイト管理者に有効にしてもらう必要がある。
{% endalert %}

## ステップ 2:フォームをカスタマイズする {#customizable-features}

次に、必要に応じてフォームをカスタマイズする。Eメールキャプチャフォームの以下の機能をカスタマイズできる：

- ヘッダー、本文、送信ボタンのテキスト
- 任意の画像
- オプションの「利用規約」リンク
- ヘッダーとボディのテキスト、ボタン、背景の色が異なる
- キーと値のペア
- ヘッダーとボディのテキスト、ボタン、ボタンのボーダーカラー、背景、オーバーレイのスタイル

![メールキャプチャフォームのコンポーザー。][5]

さらにカスタマイズが必要な場合は、**メッセージタイプに** **カスタムコードを**選択する。[Braze Templates](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates)GitHubリポジトリにあるこの[メールキャプチャモーダルテンプレートを](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/5-email-capture-modal)スターターコードとして使うことができる。

## ステップ 3:エントリーオーディエンスを設定する

このフォームを、既存のメールアドレスを持たないユーザーにだけ送信したい場合は、フィルター`Email Available is false` を使用する。

![利用可能な電子メールによるフィルタリングはfalseである][10]{: style="max-width:50%"}

このフォームを外部IDを持たないユーザー（匿名ユーザー）にのみ送信したい場合は、フィルター`External User ID is blank` を使用する。

![外部ユーザーIDによるフィルタリングが空白][11]{: style="max-width:50%"}

必要であれば、`AND` のロジックを使って2つのフィルターを組み合わせることもできる。

## ステップ 4:フォームに記入したユーザーを対象とする（オプション）

メール収集フォームを立ち上げ、ユーザーからメールアドレスを収集したら、`Clicked/Opened Campaign` 。 

キャンペーン`<CAMPAIGN_NAME>` のフィルタを`Has clicked in-app message button 1` に設定する。`<CAMPAIGN_NAME>` をメールキャプチャフォームのキャンペーン名に置き換える。

![ウェブメールキャプチャフォームのキャンペーンで、アプリ内メッセージボタン1をクリックした人をフィルタリングする。][12]

[4]: {% image_buster /assets/img/email_capture_config.png %}
[5]: {% image_buster /assets/img/email_capture.png %}
[10]: {% image_buster /assets/img_archive/web_email_filter_1.png %}
[11]: {% image_buster /assets/img_archive/web_email_filter_2.png %}
[12]: {% image_buster /assets/img_archive/web_email_filter_3.png %}
