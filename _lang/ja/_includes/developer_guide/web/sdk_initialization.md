## Googleタグマネージャーを使う {#initialization-tag}

### ステップ1:プッシュセットアップ(オプション)

オプションで、Google タグマネージャをプッシュ送信できるようにするには、まず[push integration]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) のガイドラインに従い、以下の手順を実行します。
1. サイトのサービスワーカーを設定し、サイトのルートディレクトリに配置します
2. ブラウザ登録を設定する- サービスワーカーが設定されたら、`braze.requestPushPermission()` メソッドをアプリまたはカスタムHTML タグ(GTM ダッシュボードを使用) でネイティブに設定する必要があります。また、SDK が初期化された後にタグが実行されるようにする必要があります。

### ステップ2:初期化タグの選択

コミュニティーテンプレートギャラリーでBrazeを検索し、**Braze初期化タグ**を選択します。

![Braze 初期化タグの構成設定を示すダイアログボックス。含まれる設定は、「タグのタイプ」、「API キー」、「API エンドポイント」、「SDK バージョン」、「外部ユーザー ID」、「Safari Web プッシュ ID」です。]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

### ステップ3: 設定の構成

Braze API アプリ 識別子キーとSDKエンドポイントを入力します。これは、ダッシュボードの**設定の管理** ページにあります。Web SDKの最新の`major.minor` バージョンを入力します。たとえば、最新バージョンが`4.1.2` の場合、`4.1` と入力します。SDKのバージョン一覧は[変更履歴で](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)見ることができる。

### ステップ 4:初期化オプションの選択

[初期設定]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#step-2-initialize-braze) ガイドで説明されている追加の初期化オプションのオプションセットから選択します。

### ステップ5: 検証とQA

このタグを展開したら、次の2つの方法で適切な統合を確認できます。

1. Googleタグマネージャーの[デバッグツールを使って](https://support.google.com/tagmanager/answer/6107056?hl=en)、設定したページやイベントでBraze初期化タグがトリガーされたことを確認する。
2. Braze に対して行われたネットワークリクエストが表示され、グローバル `window.braze` ライブラリが Web ページで定義されます。
