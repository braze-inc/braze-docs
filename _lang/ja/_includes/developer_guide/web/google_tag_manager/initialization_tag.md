### 前提条件

この連携方法を使用する前に、[Google Tag Managerのアカウントとコンテナを作成](https://support.google.com/tagmanager/answer/14842164)する必要がある。

### ステップ 1: タグテンプレートギャラリーを開け

[Google Tag Manager](https://tagmanager.google.com/)で、ワークスペースを選択し、次に**「テンプレート」**を選ぶ。**タグテンプレート** ペインで、**検索ギャラリー**を選択する。

![Google Tag Managerのサンプルワークスペース用テンプレートページ。]({% image_buster /assets/img/web-gtm/search_tag_template_gallery.png %}){: style="max-width:95%;"}

### ステップ 2:初期化タグのテンプレートを追加する

テンプレートギャラリーでを検索し、次に**Braze **`braze-inc`**Initialization Tag**を選択する。

![様々な「Braze-inc」テンプレートを表示するテンプレートギャラリー。]({% image_buster /assets/img/web-gtm/template_gallery_results.png %}){: style="max-width:80%;"}

**ワークスペースに追加**＞**追加**を選択する。

![Google Tag Managerの「Braze 初期化タグ」ページ。]({% image_buster /assets/img/web-gtm/add_to_workspace.png %}){: style="max-width:70%;"}

### ステップ 3:タグを設定する

**テンプレート**セクションから、新しく追加したテンプレートを選択する。

![Google Tag Managerの「テンプレート」ページに、Braze 初期化タグのテンプレートが表示されている。]({% image_buster /assets/img/web-gtm/select_tag_template.png %}){: style="max-width:95%;"}

鉛筆アイコンを選択すると、**タグ設定**のドロップダウンが開く。

![鉛筆アイコンが表示されたタグ設定タイル。]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

必要な最低限の情報を入力せよ：

| フィールド         | 説明 |
| ------------- | ----------- |
| **API キー**   | [Braze API キー]({{site.baseurl}}/api/basics/#about-rest-api-keys)は、Braze ダッシュボードの「**設定**」＞「**アプリ設定**」にある。 |
| **API エンドポイント** | RESTエンドポイントのURL。エンドポイントは、[インスタンス]({{site.baseurl}}/api/basics/#endpoints)のBraze URLによって異なります。 |
| **SDK バージョン**  | 変更履歴に記載されている最新のWeb Braze SDK`MAJOR.MINOR`バージョン。たとえば、最新バージョンが`4.1.2` の場合、`4.1` と入力します。詳細については、[SDKのバージョン管理についてを]({{site.baseurl}}/developer_guide/sdk_integration/version_management/)参照せよ。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

追加の初期化設定を行うには、**Braze 初期化オプション**を選択し、必要な設定を選択する。

![「タグ設定」の下にあるBraze初期化オプションの一覧だ。]({% image_buster /assets/img/web-gtm/braze_initialization_options.png %}){: style="max-width:65%;"}

### ステップ 4: 初期化オプションの選択

Brazeの初期化タグは、以下のオプションを公開する。これらのほとんどは[Web SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)に直接対応している。また一部は、タグが初期化時に[`InitializationOptions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)呼び出すWeb SDKのメソッドに対応している。統合のニーズに合うオプションを選択せよ：

| GTMオプション | Web SDKの設定またはメソッド | 説明 |
| --- | --- | --- |
| **アプリ内メッセージでHTMLを許可する** | `allowUserSuppliedJavascript` | アプリ内メッセージ、バナー、およびユーザーが提供するJavaScriptクリックアクションでHTMLをイネーブルメントする。カスタムHTMLを使用する[アプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/)や[バナー]({{site.baseurl}}/developer_guide/banners/placements/?sdktab=web)の[HTML]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/)に必須である。HTMLとJavaScriptの内容を信頼できる場合にのみイネーブルメントせよ。これはユーザーが提供したJavaScriptの実行を許可するからだ。 |
| **アプリバージョン番号** | `appVersion`, `appVersionNumber` | セグメンテーション用のアプリ版（例：`1.2.3.4`）。 |
| **自動的に新しいセッションを開く** | `braze.openSession()` | このメソッドを呼び出すことで、SDKが初期化された後に新しいセッションを開く。 |
| **アプリ内メッセージを自動的に表示する** | `braze.automaticallyShowInAppMessages()` | 初期化後にこのメソッドを呼び出すことで、サーバーから新しいアプリ内メッセージが届いた際に自動的に表示する。 |
| **自動プッシュトークンメンテナンスを無効にする** | `disablePushTokenMaintenance` | 新しいセッションでは、SDKがプッシュトークンをBrazeバックエンドと同期するのを止める。 |
| **自動サービスワーカー登録を無効にする** | `manageServiceWorkerExternally` | サービスワーカーを自分で登録してコントロールする場合に使用する。 |
| **Cookieを無効にする** | `noCookies` | ユーザー／セッションデータにはCookieではなくlocalStorageを使用する。クロスサブドメイン認識を防ぐ。 |
| **Font Awesomeを無効化する** | `doNotLoadFontAwesome` | SDKがCDNからFont Awesomeを読み込むのを防ぐ。サイトに独自のFont Awesomeがある場合に使用する。 |
| **SDK認証を有効にする** | `enableSdkAuthentication` | [SDK認証を]({{site.baseurl}}/developer_guide/sdk_integration/authentication/)イネーブルメントする。 |
| **Web SDKのログ記録を有効にする** | `enableLogging` | デバッグ用のコンソールログのイネーブルメント。本番環境では削除せよ。 |
| **トリガーメッセージ間の最小間隔** | `minimumIntervalBetweenTriggerActionsInSeconds` | トリガーアクション間の最小秒数（デフォルト：30）。 |
| **カードを新しいタブで開く** | `openCardsInNewTab` | デフォルトのフィードUIを使用している場合、コンテンツカードのリンクは新しいタブで開封する。 |
| **サービスワーカーの位置** | `serviceWorkerLocation` | サービスワーカーファイルのカスタムパス（デフォルト：`/service-worker.js`）。 |
| **セッションタイムアウト（秒）** | `sessionTimeoutInSeconds` | セッションタイムアウト（秒単位）（デフォルト値：1800年。 |

{% alert note %}
Google Tag ManagerのBraze初期化タグを使用する際、[カスタムHTMLアプリ内メッセージを]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/)有効にするには、**Braze初期化オプション**で**「HTMLアプリ内メッセージを許可する」**を選択する。このチェックボックスは、の`allowUserSuppliedJavascript`初期化`braze.initialize()`オプションに対応し、それをに設定する`true`。Google Tag ManagerのBraze初期化タグは、オプション名ではなくこのラベルを使用する。
{% endalert %}

GTMテンプレートで公開されていないオプション（例えば`contentSecurityNonce`、`localization`やなど`devicePropertyAllowlist`）については、代わりに[実行時初期化]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)を使用する。

### ステップ 5: *すべてのページ*でトリガーされるように設定する

初期化タグはサイトの全ページで実行すべきだ。これにより、Braze SDKメソッドを使用し、Web プッシュの分析を記録できる。

### ステップ 6: 統合を確認せよ

以下のいずれかの方法で統合を確認できる：

- **オプション 1:**Google Tag Manager の[デバッグツール](https://support.google.com/tagmanager/answer/6107056?hl=en)を使えば、設定したページやイベントで Braze の初期化タグが正しくトリガーされているか確認できる。
- **オプション 2:**ウェブページからBrazeへのネットワークリクエストがないか確認せよ。さらに、グローバル`window.braze`ライブラリーを定義する必要がある。
