---
nav_title: 電子メール・キャプチャ・フォーム
article_title: メールキャプチャフォーム
page_order: 3
page_type: reference
description: "この記事では、アプリ内メッセージタイプのメールキャプチャの概要を説明します。"
channel:
  - in-app messages
---

# メールキャプチャフォーム {#email-capture-form}

> メールキャプチャメッセージを使用すると、サイトのユーザーにメールアドレスの送信を簡単に促すことができます。その後、このメールアドレスがユーザープロファイル内で利用可能になり、すべてのメッセージングキャンペーンで使用できます。

エンドユーザーがこのフォームにEメールアドレスを入力すると、そのEメールアドレスがユーザープロファイルに追加される。

- まだアカウントを持っていない[匿名ユーザーの]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#anonymous-user-profiles)場合、メールアドレスは、ユーザーのデバイスに紐付けられた匿名ユーザープロファイルに登録される。
- ユーザー・プロフィールにすでにEメールアドレスが存在する場合、既存のEメールアドレスは新しく入力されたEメールアドレスで上書きされる。
- 既知のユーザーのメールアドレスに[ハードバウンス]({{site.baseurl}}/help/help_articles/email/email_bounces#email-bounces)のフラグが設定されている場合、新しく入力したメールアドレスが Braze のユーザープロファイルにあるメールアドレスと異なるかどうかが確認されます。入力したメールアドレスが異なる場合、メールアドレスが更新され、ハードバウンスのステータスが削除されます。 
- ユーザーが無効なメールアドレスを入力した場合、エラーメッセージが表示される：「有効なEメールを入力してください。
    - 無効なメールアドレス: 
        - `example`
        - `example@`
        - `@gmail.com`
        - `example@gmail`
    - 有効なメールアドレス 
        - `example@gmail.com`
        - `example@gnail.com` (誤字あり）
    - Braze でのメールアドレス検証の詳細については、[メールの技術ガイドラインと注記]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/)を参照してください。

{% details More on identified versus anonymous users %}

一般的に、Eメールキャプチャフォームのロジックは単純だ。Brazeのユーザープロフィールに、現在アクティブなユーザーのEメールアドレスを設定する。ただし、ユーザーが識別されている (ログインし、`changeUser` が呼び出されている) かどうかによって、動作が異なることを意味します。

匿名ユーザーがフォームに電子メールを入力して送信すると、Brazeはその電子メールアドレスをプロフィールに追加する。ユーザーの Web ジャーニー で `changeUser` が後で呼び出され、新しい `external_id` が割り当てられた場合 (新規ユーザーがサービスに登録した場合など) 、その匿名ユーザーについて、メールアドレスを含むすべてのユーザープロファイルデータがマージされます。

既存の `external_id` を使用して `changeUser` が呼び出された場合、その匿名ユーザーのユーザープロファイルは孤立し、識別されたユーザーにまだ存在しない[特定のユーザープロファイルのデータフィールド]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior)がマージされます。ただし、メールアドレスを含めて、すでに存在するフィールドは失われる。

詳細については、「[ユーザープロファイルのライフサイクル]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/)」を参照してください。

{% enddetails %}

## ステップ 1:アプリ内メッセージキャンペーンを作成する

このオプションに移動するには、アプリ内メッセージングキャンペーンを作成する必要があります。そこから、ユースケースに応じて、「**送信**先」を「**ウェブブラウザ**」、「**モバイルアプリ**」、「**モバイルアプリとウェブブラウザの両方**」のいずれかに設定し、**メッセージタイプとして**「&メールキャプチャフォーム&」を選択する。

{% alert note %}
**Web ユーザーをターゲットに設定できますか?**<br>Web SDK を介して HTML アプリ内メッセージを有効にするには、`allowUserSuppliedJavascript` 初期化オプションを Braze に指定する必要があります。例: `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`。これはセキュリティ上の理由によるもので、HTML のアプリ内メッセージは JavaScript を実行できるため、サイト管理者が有効にする必要があります。
{% endalert %}

## ステップ2:フォームをカスタマイズする {#customizable-features}

次に、必要に応じてフォームをカスタマイズする。Eメールキャプチャフォームの以下の機能をカスタマイズできる：

- ヘッダー、本文、送信ボタンのテキスト
- 任意の画像
- オプションの「利用規約」リンク
- ヘッダーとボディのテキスト、ボタン、背景の色が異なる
- キーと値のペア
- ヘッダーとボディのテキスト、ボタン、ボタンのボーダーカラー、背景、オーバーレイのスタイル

]({% image_buster /assets/img/email_capture.png %})メールキャプチャフォーム作成画面。()

さらにカスタマイズが必要な場合は、[**メッセージタイプ**] に [**カスタムコード**] を選択します。[Braze Templates](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates) GitHub リポジトリにあるこの[メールキャプチャモーダルテンプレート](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/5-email-capture-modal)をスターターコードとして使用できます。

## ステップ 3:エントリーオーディエンスを設定する

アプリ内メッセージを使用してユーザーメールをキャプチャする場合は、この情報をまだ提供していないユーザーにオーディエンスを制限できます。

- **メールアドレスのないユーザーをターゲットにするには:**フィルター `Email Available` is`false` を使用します。これにより、メールが登録されていないユーザーのみにフォームが表示されるようになり、既知のユーザーに対して冗長なプロンプトを表示することを回避できます。
- **external ID を持たない匿名ユーザーをターゲットにするには:**フィルター `External User ID` `is blank` を使用します。これは、まだ認証または登録されていないユーザーを識別する場合に便利です。

必要であれば、`AND` のロジックを使って2つのフィルターを組み合わせることもできる。これにより、メールアドレスと外部ユーザー ID の両方が欠落しているユーザーのみに対して表示されます。これは、新規リードをキャプチャする場合やアカウントの作成を促す場合に最適です。

## ステップ 4:フォームに記入したユーザーを対象とする（オプション）

メールキャプチャフォームを起動して、ユーザーからメールアドレスを収集したら、フォームに入力したユーザーをターゲットに設定できます。

1. Braze のセグメントフィルターで、フィルター `Clicked/Opened Campaign` を選択します。 
2. ドロップダウンから `clicked in-app message button 1` を選択します。
3. メールキャプチャフォームキャンペーンを選択します。

