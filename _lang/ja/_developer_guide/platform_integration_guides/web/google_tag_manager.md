---
nav_title: Google Tag Manager
article_title: ウェブ向け Google タグ マネージャー
platform: Web
page_order: 20
description: "この記事では、Google タグ マネージャーを使用して Braze を Web サイトに導入する方法について説明します。"

---

# Google Tag Manager

> この記事では、Google タグ マネージャー (GTM) を使用して Braze Web SDK を Web サイトに追加する方法の手順を説明します。[Google タグ マネージャーを使用すると、][2] 本番環境のコードのリリースやエンジニアリング リソースを必要とせずに、ウェブサイト上のタグをリモートで追加、削除、編集できます。

Braze によって作成された Google タグ マネージャー テンプレートには、 [初期化タグ](#initialization-tag) と [アクション タグの](#actions-tag)2 つがあります。

どちらのタグも、[Google のコミュニティ ギャラリー][15] からワークスペースに追加できます。また、コミュニティ テンプレートから新しいタグを追加するときに Braze を検索することでも追加できます。

![ギャラリー検索の画像][gtm-community-gallery-search]

## Google EU ユーザー同意ポリシーの更新

{% alert important %}
Google は、2024 年 3 月 6 日に発効する [デジタル市場法 (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html)の変更に応じて、[EU ユーザー同意ポリシー](https://www.google.com/about/company/user-consent-policy/) を更新しています。この新しい変更により、広告主は EEA および英国のエンドユーザーに特定の情報を開示し、必要な同意を得ることが義務付けられます。詳細については、次のドキュメントを参照してください。
{% endalert %}

Google の EU ユーザーの同意ポリシーの一環として、次のブール値のカスタム属性をユーザー プロファイルに記録する必要があります。

- `$google_ad_user_data`
- `$google_ad_personalization`

GTM 統合を介してこれらを設定する場合、カスタム属性にはカスタム HTML タグを作成する必要があります。以下は、これらの値をブールデータ型 (文字列ではなく) としてログに記録する方法の例です。

\`\`\`js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

詳細については、[「Audience Sync to Google」]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/)を参照してください。

## 初期化タグテンプレート {#initialization-tag}

初期化タグを使用して、Braze Web SDK を Web サイトに追加します。

### ステップ 1:プッシュ設定（オプション）

オプションとして、Google タグ マネージャーを通じてプッシュを送信できるようにするには、まず [プッシュ統合]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/) ガイドラインに従って次の操作を行います。
1. サイトのサービスワーカーを設定し、サイトのルートディレクトリに配置します。
2. ブラウザ登録の設定 - サービスワーカーの設定が完了したら、 `braze.requestPushPermission()` メソッドは、アプリ内でネイティブに、またはカスタム HTML タグ (GTM ダッシュボード経由) を通じて使用できます。また、SDK が初期化された後にタグが実行されることを確認する必要があります。

### ステップ 2: 初期化タグを選択する

コミュニティ テンプレート ギャラリーで Braze を検索し、**Braze 初期化タグ**を選択します。

![Braze 初期化タグの構成設定を表示するダイアログ ボックス。含まれる設定は、「タグタイプ」、「API キー」、「API エンドポイント」、「SDK バージョン」、「外部ユーザー ID」、「Safari ウェブプッシュ ID」です。][gtm-initialization-tag]

### ステップ 3: 設定を構成する

ダッシュボードの **「設定の管理」** ページにある Braze API アプリ識別子キーと SDK エンドポイントを入力します。Web SDKの最新版を入力してください `major.minor` バージョン。たとえば、最新バージョンが `4.1.2`、 入力 `4.1`。SDK バージョンのリストは、[changelog][changelog] で確認できます。

### ステップ 4: 初期化オプションを選択

[初期設定][7]ガイドに記載されている追加の初期化オプションのオプションセットから選択します。

### ステップ 5: 検証と品質保証

このタグを展開したら、適切な統合を確認する方法は 2 つあります。

1. Google タグ マネージャーの [デバッグ ツール][gtm-debugging-tool] を使用すると、設定したページまたはイベントで Braze 初期化タグがトリガーされたことを確認できます。
2. Brazeへのネットワークリクエストとグローバル `window.braze` これで、Web ページでライブラリが定義されるはずです。

## アクションタグテンプレート {#actions-tag}

Braze アクション タグ テンプレートを使用すると、カスタム イベントをトリガーしたり、購入を追跡したり、ユーザー ID を変更したり、プライバシー要件に応じて追跡を停止または再開したりできます。

![][gtm-アクションタグ]

### ユーザーの外部IDの変更 {#external-id}

**ユーザー変更** タグタイプは、 [`changeUser` 方法](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)。 

ユーザーがログインしたり、独自のタグで識別されるときはいつでもこのタグを使用します。 `external_id` 識別子。

**外部ユーザー ID** フィールドに現在のユーザーの一意の ID を必ず入力してください。この ID は通常、Web サイトから送信されたデータ レイヤー変数を使用して入力されます。

![Braze アクション タグの構成設定を表示するダイアログ ボックス。設定には「タグタイプ」と「外部ユーザーID」が含まれます。][gtm-change-user]

### カスタムイベントをログに記録する {#custom-events}

**カスタムイベント** タグタイプは、 [`logCustomEvent` 方法](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent)。

このタグを使用して、オプションでカスタム イベント プロパティを含め、カスタム イベントを Braze に送信します。

変数を使用するか、 **イベント名を入力してイベント名** を入力します。

イベント プロパティを追加するには、**[行の追加]** ボタンを使用します。

![Braze アクション タグの構成設定を表示するダイアログ ボックス。含まれる設定は、「タグタイプ」（カスタム イベント）、「イベント名」（ボタン クリック）、「イベント プロパティ」です。][gtm-custom-event]

### 電子商取引イベント {#ecommerce}

サイトで標準の [eコマース イベント][eコマース] データレイヤー アイテムを使用して購入を Google タグ マネージャーに記録する場合は、**e コマース購入** タグタイプを使用できます。このアクションタイプは、リスト内の各アイテムごとにBrazeで個別の「購入」を記録します。 `items`。

購入プロパティ リストでキーを指定することにより、購入プロパティとして含める追加のプロパティ名を指定することもできます。Brazeは個人の内部を見ることに注意してください `item` リストに追加した購入物件について記録されます。

例えば、eコマースのペイロードに次のような内容が含まれているとします。 `items`:

```
items: [{
  item_name: "5 L WIV ECO SAE 5W/30",
  item_id: "10801463",
  price: 24.65,
  item_brand: "EUROLUB",
  quantity: 1
}]
```

もしあなたが望むなら `item_brand` そして `item_name` 購入物件として渡される場合は、その 2 つのフィールドを購入物件テーブルに追加するだけです。プロパティを指定しないと、[\`logPurchase\`][log-purchase] 呼び出しで Braze への購入プロパティは送信されません。

### 購入を追跡する {#purchases}

**購入** タグタイプは、 [`logPurchase` 方法](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase)。

このタグを使用して、Braze への購入を追跡します (オプションで購入プロパティも含む)。

**製品 ID** と **価格の** フィールドは必須です。

購入プロパティを追加するには、**[行の追加]** ボタンを使用します。

![Braze アクション タグの構成設定を表示するダイアログ ボックス。含まれる設定は、「タグタイプ」、「外部 ID」、「価格」、「通貨コード」、「数量」、「購入プロパティ」です。][gtm-purchase]

### 追跡を停止して再開する {#stop-tracking}

場合によっては、たとえばユーザーがプライバシー上の理由で Web トラッキングをオプトアウトした後など、Web サイトで Braze トラッキングを無効にしたり再度有効にしたりすることが必要になることがあります。

Web トラッキング **を無効にするか再度有効にするには、それぞれ「トラッキング** を無効にする」または **「トラッキングを再開する」** タグ タイプを使用します。これら2つのオプションは [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) そして [`enableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk)。

### カスタムユーザー属性 {#custom-attributes}

Google タグ マネージャーのスクリプト言語の制限により、カスタム ユーザー属性は使用できません。カスタム属性をログに記録するには、次の内容のカスタム HTML タグを作成します。

\`\`\`html
<script>
  // Note: If using SDK version 3.x or below, use `window.appboy` instead of `window.braze`
  // Version 4 or greater should use `window.braze`
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>
```

{% alert important %}
GTM テンプレートは、イベントまたは購入のネストされたプロパティをサポートしていません。上記の HTML を使用して、ネストされたプロパティを必要とするイベントや購入をログに記録できます。
{% endalert %}

### 標準ユーザー属性 {#standard-attributes}

ユーザーの名などの標準ユーザー属性は、カスタム ユーザー属性と同じ方法でログに記録する必要があります。標準属性に渡す値が、[User クラス][16] ドキュメントで指定されている想定される形式と一致していることを確認します。

たとえば、gender 属性は次のいずれかを値として受け入れることができます。 `"m" | "f" | "o" | "u" | "n" | "p"`。したがって、ユーザーの性別を女性に設定するには、次の内容のカスタム HTML タグを作成します。

\`\`\`html
<script>
window.braze.getUser().setGender("f")
</script>
```

## コンテンツカードの統合

Google タグ マネージャーを使用して [コンテンツ カード]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) メッセージング チャネルを統合するには、いくつかの追加手順が必要です。Google タグ マネージャーは、[Braze CDN]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn)(Web SDK のバージョン) をウェブサイトのコードに直接挿入することで機能します。つまり、コンテンツ カードを実装する場合を除き、Google タグ マネージャーを使用せずに SDK を統合した場合と同じように、すべての SDK メソッドを利用できます。

### オプション 1: GTMを使用した統合

コンテンツ カード フィードの標準的な統合には、Google タグ マネージャーで **カスタム HTML** タグを使用できます。カスタム HTML タグに次のコードを追加すると、標準のコンテンツ カード フィードがアクティブになります。

\`\`\`html
<script>
   window.braze.showContentCards();
</script>
```

![コンテンツ カード フィードを表示するカスタム HTML タグの Google タグ マネージャーでのタグ設定][gtm-content-cards]

### オプション 2: ウェブサイトに直接統合

コンテンツ カードとそのフィードの外観をより自由にカスタマイズするには、コンテンツ カードをネイティブ Web サイトに直接統合できます。これには、標準のフィード UI を使用するか、カスタム フィード UI を作成するという 2 つのアプローチがあります。

#### 標準フィード

[標準フィードUI]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/#standard-feed-ui)を実装する場合、Brazeメソッドには `window.` メソッドの先頭に追加されました。例えば、 `braze.showContentCards` 代わりに `window.braze.showContentCards`。

#### カスタムフィードUI

[カスタム フィード]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/custom_styling) スタイルの場合、手順は GTM を使用せずに SDK を統合した場合と同じです。たとえば、コンテンツ カード フィードの幅をカスタマイズする場合は、次のコードを CSS ファイルに貼り付けます。

{% raw %}
```css
body .ab-feed { 
    width: 800px;
}
```
{% endraw %}

## テンプレートのアップグレードと更新 {#upgrading}

Braze Web SDK を最新バージョンにアップグレードするには、Google タグ マネージャー ダッシュボードで次の 3 つの手順を実行します。

1. **タグテンプレートを更新**<br>ワークスペース内の **テンプレート** ページに移動します。ここで、アップデートが利用可能であることを示すアイコンが表示されます。<br><br>![更新が利用可能であることを示すテンプレート ページ][gtm-update-available]<br><br>そのアイコンをクリックし、変更を確認した後、**「更新を承認」**をクリックします。<br><br>![古いタグ テンプレートと新しいタグ テンプレートを比較する画面と「更新を承認」ボタン][gtm-accept-update]<br><br>
2. **バージョン番号の更新**<br>タグテンプレートが更新されたら、Braze初期化タグを編集し、SDKバージョンを最新のものに更新します。 `major.minor` バージョン。たとえば、最新バージョンが `4.1.2`、 入力 `4.1`。SDK バージョンのリストは、[changelog][changelog] で確認できます。<br><br>![SDK バージョンを変更するための入力フィールドを備えた Braze 初期化テンプレート][gtm-version-number]<br><br>
3. **QAと公開**<br>タグ コンテナに更新を公開する前に、Google タグ マネージャーの [デバッグ ツール][gtm-debugging-tool] を使用して、新しい SDK バージョンが動作していることを確認します。

## トラブルシューティングの手順 {#troubleshooting}

### タグのデバッグを有効にする {#debugging}

各 Braze タグ テンプレートにはオプションの **GTM タグ デバッグ** チェックボックスがあり、これを使用してデバッグ メッセージを Web ページの JavaScript コンソールに記録できます。

![Google タグ マネージャーのデバッグ ツール][gtm-tag-debugging]

### デバッグモードに入る

Google タグ マネージャーの統合をデバッグするもう 1 つの方法は、Google の [プレビュー モード][14] 機能を使用することです。

これにより、Web ページのデータ レイヤーからトリガーされた各 Braze タグに送信されている値を特定し、どのタグがトリガーされたか、またはトリガーされなかったかがわかります。

![Braze 初期化タグの概要ページには、どのタグがトリガーされたかの情報など、タグの概要が表示されます。][gtm-tag-debug-mode]

### 詳細ログを有効にする

テスト中に Braze テクニカル サポートがログにアクセスできるようにするには、Google タグ マネージャー統合で詳細ログを有効にします。これらのログは、ブラウザの [開発者ツール](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools)の **コンソール** タブに表示されます。

Google タグ マネージャーの統合で、Braze 初期化タグに移動し、「**Web SDK ログを有効にする」**を選択します。

![Web SDK ログ記録を有効にするオプションがオンになっている Braze 初期化タグの概要ページ。][gtm-verbose-logging]

[2]: https://support.google.com/tagmanager/answer/6103696
[gtm-community-gallery-search]: {% image_buster /assets/img/web-gtm/gtm-community-gallery-search.png %}
[gtm-initialization-tag]: {% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %}
[gtm-actions-tag]: {% image_buster /assets/img/web-gtm/gtm-actions-tag.png %}
[6]: {{ site.baseurl }}/user_guide/administrative/app_settings/manage_app_group/app_group_management/#app-group-management
[7]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#step-2-initialize-braze
[gtm-change-user]: {% image_buster /assets/img/web-gtm/gtm-change-user.png %}
[gtm-custom-event]: {% image_buster /assets/img/web-gtm/gtm-custom-event.png %}
[gtm-purchase]: {% image_buster /assets/img/web-gtm/gtm-purchase.png %}
[gtm-tag-debugging]: {% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %}
[gtm-tag-debug-mode]: {% image_buster /assets/img/web-gtm/gtm-debug-mode.png %}
[14]: https://support.google.com/tagmanager/answer/6107056
[15]: https://tagmanager.google.com/gallery/#/?filter=braze
[16]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html
[gtm-update-available]: {% image_buster /assets/img/web-gtm/gtm-update-available.png %}
[gtm-accept-update]: {% image_buster /assets/img/web-gtm/gtm-accept-update.png %}
[gtm-version-number]: {% image_buster /assets/img/web-gtm/gtm-version-number.png %}
[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md
[gtm-debugging-tool]: https://support.google.com/tagmanager/answer/6107056?hl=en
[ecommerce]: https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm
[log-purchase]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase
[gtm-verbose-logging]: {% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %}
[gtm-content-cards]: {% image_buster /assets/img/web-gtm/gtm_content_cards.png %}
