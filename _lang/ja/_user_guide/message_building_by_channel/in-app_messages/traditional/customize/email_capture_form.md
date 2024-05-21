---
nav_title: メールキャプチャフォーム
article_title: メールキャプチャフォーム
page_order: 3
page_type: reference
description: "この記事では、メールキャプチャのアプリ内メッセージタイプの概要について説明します。"
channel:
  - in-app messages
---

# メールキャプチャフォーム {#email-capture-form}

> メールキャプチャメッセージを使用すると、サイトのユーザーにメールアドレスを送信するように簡単に促すことができ、その後、すべてのメッセージングキャンペーンで使用するためにユーザープロファイル内で使用できるようになります。

エンドユーザーがこのフォームにメールアドレスを入力すると、そのメールアドレスがユーザープロファイルに追加されます。

- まだアカウントを持っていない [匿名ユーザー]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#anonymous-user-profiles) の場合、メール アドレスは、ユーザーのデバイスに関連付けられている匿名ユーザー プロファイルに存在します。
- ユーザープロファイルにメールアドレスがすでに存在する場合、既存のメールアドレスは新しく入力されたメールアドレスで上書きされます。
- ユーザーが無効なメールアドレスを入力すると、次のエラーメッセージが表示されます。有効なメールアドレスを入力してください
    - 無効なメールアドレス:  
        - `example`
        - `example@`
        - `@gmail.com`
        - `example@gmail`
    - 有効なメールアドレス: 
        - `example@gmail.com`
        - `example@gnail.com` (タイプミスあり)
    - BrazeでのEメール検証の詳細については、 [Eメールの技術ガイドラインと注意事項]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/email_validation/)を参照してください。

{% details More on identified versus anonymous users %}

一般的に、メールキャプチャフォームの背後にあるロジックは単純です。Brazeのユーザープロファイルに、現在アクティブなユーザーのメールアドレスが設定されます。ただし、これは、ユーザーが識別されている(ログインしている、 `changeUser` 呼び出されている)かどうかによって動作が異なることを意味します。

匿名ユーザーがフォームにメールアドレスを入力して送信すると、Brazeはそのメールアドレスをプロフィールに追加します。が Web ジャーニーの後半で呼び出され、新しい`external_id`ユーザーが割り当てられた場合 `changeUser` (新しいユーザーがサービスに登録したときなど)、電子メール アドレスを含むすべての匿名ユーザー プロファイル データがマージされます。

が既存の で呼び出された場合`changeUser`、匿名ユーザー・プロファイルは孤立し、識別されたユーザーにまだ存在しない[特定のユーザー・プロファイル・データ・フィールド]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior)はマージされますが、電子メール・アドレスを含め、すでに存在するフィールドはすべて失われます。`external_id`

詳しくは、 [ユーザープロファイルのライフサイクル]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/)を参照してください。

{% enddetails %}

## ステップ 1:アプリ内メッセージキャンペーンの作成

このオプションに移動するには、アプリ内メッセージングキャンペーンを作成する必要があります。そこから、ユースケースに応じて、[**送信先**] を **[Web ブラウザー**]、[**モバイルアプリ**]、または **[モバイルアプリと Web ブラウザーの両方**] に設定し、[**メッセージタイプ**] として **[メールキャプチャフォーム**] を選択します。

![][4]

{% alert note %}
Web SDK を使用して HTML アプリ内メッセージを有効にするには、Braze に初期化オプションを指定する `allowUserSuppliedJavascript` 必要があります(例: `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`)。これは、HTMLアプリ内メッセージでJavaScriptを実行できるため、サイトメンテナにJavaScriptを有効にする必要があるため、セキュリティ上の理由によるものです。
{% endalert %}

## ステップ 2:フォームをカスタマイズする {#customizable-features}

次に、必要に応じてフォームをカスタマイズします。メールキャプチャフォームの次の機能をカスタマイズできます。

- ヘッダー、本文、送信ボタンのテキスト
- オプションの画像
- オプションの「利用規約」リンク
- ヘッダーと本文のテキスト、ボタン、背景の色が異なる
- キーと値のペア
- ヘッダーと本文のテキスト、ボタン、ボタンの境界線の色、背景、オーバーレイのスタイル

![メールキャプチャフォームのコンポーザー][5]

さらにカスタマイズする必要がある場合は、[**Message Type**] で **[Custom Code**] を選択します。[Braze Templates](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates) GitHubリポジトリのこの[メールキャプチャモーダルテンプレート](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/5-email-capture-modal)をスターターコードとして使用できます。

## ステップ 3:エントリーオーディエンスを設定する

既存のメールアドレスを持たないユーザーにのみこのフォームを送信する場合は、フィルター `Email Available is false`を使用します。

![利用可能な電子メールによるフィルターがfalseです][10]{: style="max-width:50%"}

このフォームを外部 ID を持たないユーザー(匿名ユーザー)にのみ送信する場合は、フィルター `External User ID is blank`を使用します。

![外部ユーザーIDによるフィルターが空白][11]{: style="max-width:50%"}

必要に応じて、ロジックを使用して `AND` 2 つのフィルターを組み合わせることもできます。

## ステップ 4: フォームに入力したユーザーを対象とする(省略可)

メールキャプチャフォームを起動し、ユーザーからメールアドレスを収集したら、フィルター `Clicked/Opened Campaign`を使用してそれらのユーザーをターゲットにすることができます。 

フィルター `Has clicked in-app message button 1` を キャンペーン `<CAMPAIGN_NAME>`に設定します。`<CAMPAIGN_NAME>`メールキャプチャフォームキャンペーンの名前に置き換えます。

![Webメールキャプチャフォームキャンペーンのアプリ内メッセージボタン1をクリックした回数のフィルター][12]

[4]: {% image_buster /assets/img/email_capture_config.png %}
[5]: {% image_buster /assets/img/email_capture.png %}
[10]: {% image_buster /assets/img_archive/web_email_filter_1.png %}
[11]: {% image_buster /assets/img_archive/web_email_filter_2.png %}
[12]: {% image_buster /assets/img_archive/web_email_filter_3.png %}