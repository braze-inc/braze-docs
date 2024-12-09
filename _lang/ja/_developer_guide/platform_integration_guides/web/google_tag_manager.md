---
nav_title: Google Tag Manager
article_title: Google Tag Manager for Web
platform: Web
page_order: 20
description: "ここでは、Googleタグマネージャを使用してBrazeをWeb サイトにデプロイする方法について説明します。"

---

# Google Tag Manager

> ここでは、Google Tag Manager (GTM) を使用して Web サイトに Braze Web SDK を追加する手順について説明します。[Google タグマネージャ](https://support.google.com/tagmanager/answer/6103696)を使用すると、実稼働コードの解放や開発を必要とせずに、Web サイト上のタグをリモートで追加、削除、および編集できます。

Braze によって構築された2 つのGoogle タグマネージャテンプレート、[初期化タグ](#initialization-tag) と[アクションタグ](#actions-tag) があります。

どちらのタグも、[Googleのコミュニティ・ギャラリーから](https://tagmanager.google.com/gallery/#/?filter=braze)、またはコミュニティ・テンプレートから新しいタグを追加する際にBrazeを検索することで、ワークスペースに追加することができる。

![ギャラリー検索の画像]({% image_buster /assets/img/web-gtm/gtm-community-gallery-search.png %})

## 更新された Google EU ユーザー同意ポリシー

{% alert important %}
Googleは、2024年3月6日から施行される[デジタル市場法（DMA）](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html)の変更に対応して、[EUユーザー同意ポリシー](https://www.google.com/about/company/user-consent-policy/)を更新しています。この新しい変更により、広告主は EEA および英国のエンドユーザーに特定の情報を開示し、必要な同意を得る必要があります。次のドキュメントを確認して、詳細を学んでください。
{% endalert %}

Google のEU ユーザー同意ポリシーの一部として、次のブール値カスタム属性をユーザープロファイルに記録する必要があります。

- `$google_ad_user_data`
- `$google_ad_personalization`

GTM 統合を使用してこれらを設定する場合、カスタム属性でカスタム HTML タグを作成する必要があります。以下は、これらの値を(文字列としてではなく)ブールデータ型としてログに記録する方法の例です。

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

詳細については、[オーディエンスを Google に同期する]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/)を参照してください。

## 初期化タグテンプレート {#initialization-tag}

初期化タグを使用して、Braze Web SDKをWeb サイトに追加します。

### ステップ1:プッシュセットアップ(オプション)

オプションで、Google タグマネージャをプッシュ送信できるようにするには、まず[push integration]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/) のガイドラインに従い、以下の手順を実行します。
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

## アクションタグテンプレート {#actions-tag}

Braze アクションタグテンプレートを使用すると、カスタムイベントのトリガー、購入の追跡、ユーザー ID の変更、プライバシー要件の追跡の停止または再開を行うことができます。

![]({% image_buster /assets/img/web-gtm/gtm-actions-tag.png %})

### ユーザー外部 ID の変更 {#external-id}

**Change User**タグ型は、[`changeUser`method](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)を呼び出します。 

このタグは、ユーザーがログインするとき、または一意の `external_id` 識別子で識別されるときに使用します。

現行のユーザーの一意のID を**外部ユーザー ID** フィールドに入力してください。通常は、Web サイトから送信されたデータレイヤー変数を使用して入力します。

![Braze アクションタグ構成設定を示すダイアログボックス。含まれる設定は、「タグのタイプ」と「外部ユーザーID」です。]({% image_buster /assets/img/web-gtm/gtm-change-user.png %})

### カスタムイベントをログに記録する{#custom-events}

**カスタムイベント**タグ型は、[`logCustomEvent`メソッド](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent)を呼び出します。

このタグを使用して、オプションでカスタムイベントプロパティーを含むカスタムイベントs をBrazeに送信します。

変数を使用するか、イベント名を入力して、**Event Name**を入力します。

イベントプロパティを追加するには、**Add Row** ボタンを使用します。

![Braze アクションタグ構成設定を示すダイアログボックス。設定には、「タグタイプ」（カスタムイベント）、「イベント名」（ボタンクリック）、「イベントプロパティ」が含まれる。]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})

### e コマースイベント {#ecommerce}

サイトで標準の [[e コマースイベント](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm)] データ層アイテムを使用して購入を Google Tag Manager に記録する場合は、**e コマース購入**タグタイプを使用できます。このアクションタイプでは、`items` のリストで送信されたアイテムごとに個別の「購入」を Braze に記録します。

購入プロパティリストでキーを指定することで、購入プロパティとして含める追加のプロパティの名前を指定することもできます。Brazeは、一覧に追加した購入プロパティーのログに記録されている個々の`item` 内を検索します。

たとえば、e コマースのペイロードには次の `items` が含まれているとします。

```
items: [{
  item_name: "5 L WIV ECO SAE 5W/30",
  item_id: "10801463",
  price: 24.65,
  item_brand: "EUROLUB",
  quantity: 1
}]
```

`item_brand` と `item_name` だけを購入プロパティとして渡す場合は、これら2つのフィールドを購入プロパティテーブルに追加するだけです。プロパティを指定しない場合、[[`logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase)] Braze の呼び出しで購入プロパティは送信されません。

### 購入の追跡 {#purchases}

**Purchase**タグ型は、[`logPurchase`method](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase)を呼び出します。

このタグを使用して、Brazeへの購入を追跡します。オプションで、購入プロパティを含めます。

**商品ID**と**価格**フィールドsが必要です。

購入プロパティを追加するには、**Add Row** ボタンを使用します。

![Braze アクションタグ構成設定を示すダイアログボックス。含まれる設定は、「タグタイプ」、「外部ID」、「価格」、「通貨コード」、「数量」、「購入プロパティ」である。]({% image_buster /assets/img/web-gtm/gtm-purchase.png %})

### トラッキングの停止と再開 {#stop-tracking}

場合によっては、たとえば、ユーザーがプライバシー上の理由でウェブトラッキングをオプトアウトしたことを示した後などに、Web サイトで Braze トラッキングを無効または再度有効にする必要があります。

Web トラッキングを無効または再度有効にするには、それぞれ**トラッキング無効**タグタイプまたは**トラッキング再開**タグタイプを使用します。これら2 つのオプションは、[`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) および[`enableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) を呼び出します。

### カスタムユーザー 属性 {#custom-attributes}

Googleタグマネージャのスクリプト言語が制限されているため、カスタムユーザー 属性は使用できません。カスタム属性s を記録するには、次の内容でカスタムHTML タグを作成します。

```html
<script>
  // Note: If using SDK version 3.x or below, use `window.appboy` instead of `window.braze`
  // Version 4 or greater should use `window.braze`
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>
```

{% alert important %}
GTM テンプレートでは、イベントまたは購買のネストされたプロパティは使用できません。前述のHTMLを使用して、ネストされたプロパティーを必要とするすべての行動または購入を記録できます。
{% endalert %}

### 標準ユーザー属性 {#standard-attributes}

ユーザーの名などの標準ユーザー属性は、カスタムユーザー属性と同じ方法でログに記録する必要があります。標準属性項目に渡す値が、[[ユーザークラス](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)] のドキュメントで指定されている予期される形式と一致していることを確認します。

たとえば、性別属性は、値として次のいずれかを使用できます。`"m" | "f" | "o" | "u" | "n" | "p"`したがって、ユーザーの性別を女性に設定するには、次の内容のカスタムHTML タグを作成します。

```html
<script>
window.braze.getUser().setGender("f")
</script>
```

## コンテンツカードの統合

Google Tag Manager を使用して[コンテンツカード]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)メッセージングチャネルを統合するには、いくつかの追加ステップがあります。Google Tag Manager は、[ Braze CDN]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn) (当社Web SDKのバージョン) をWeb サイト コードに直接注入することで機能します。これは、コンテンツカードを実装する場合を除き、Google Tag Manager なしでSDKを統合した場合と同様に、すべてのSDK方法を利用できることを意味します。

### オプション 1: GTM を使用した統合

コンテンツカードフィードを標準的に統合するには、Google タグマネージャで**カスタムHTML**タグを使用できます。以下をカスタムHTML タグに追加すると、標準のコンテンツカードフィードが有効になります。

```html
<script>
   window.braze.showContentCards();
</script>
```

![コンテンツカードのフィードを表示するカスタムHTMLタグのGoogleタグマネージャーでのタグ設定]({% image_buster /assets/img/web-gtm/gtm_content_cards.png %})

### オプション 2: Web サイトに直接統合する

コンテンツカードとそのフィードの外観をより自由にカスタマイズするために、コンテンツカードをネイティブ Web サイトに直接統合できます。これには、標準フィード UI を使用する方法と、カスタムフィード UI を作成する方法の2つの方法があります。

#### 基準フィード

[スタンダードフィード UI]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/#standard-feed-ui)を実装する場合、Brazeメソッドはメソッドの先頭に`window.`を追加する必要があります。たとえば、`braze.showContentCards` の代わりに `window.braze.showContentCards` にする必要があります。

#### カスタムフィードユーザーインターフェイス

[カスタムフィード]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/custom_styling)スタイルの場合、ステップsは、GTMなしでSDKを統合した場合と同じです。たとえば、コンテンツカードフィードの幅をカスタマイズする場合は、以下をCSSに貼り付けることができます。

{% raw %}
```css
body .ab-feed { 
    width: 800px;
}
```
{% endraw %}

## テンプレートのアップグレードと更新 {#upgrading}

Braze Web SDK の最新バージョンにアップグレードするには、Google Tag Manager ダッシュボードで次の3つのステップを実行します。

1. **タグテンプレートを更新する**<br>ワークスペース内の**Templates** ページに移動します。更新が利用可能であることを示すアイコンが表示されます。<br><br>![更新があることを示すテンプレートページ]({% image_buster /assets/img/web-gtm/gtm-update-available.png %})<br><br>そのアイコンをクリックし、変更を確認した後、**Accept Update**をクリックします。<br><br>![新旧タグテンプレートの比較画面と「更新を受け入れる」ボタン]({% image_buster /assets/img/web-gtm/gtm-accept-update.png %})<br><br>
2. **バージョン番号を更新する**<br>タグテンプレートが更新されたら、Braze 初期化タグを編集し、SDK バージョンを最新の `major.minor` バージョンに更新します。たとえば、最新バージョンが`4.1.2` の場合、`4.1` と入力します。SDKのバージョン一覧は[変更履歴で](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)見ることができる。<br><br>![SDKバージョンを変更するための入力フィールドを持つBraze初期化テンプレート]({% image_buster /assets/img/web-gtm/gtm-version-number.png %})<br><br>
3. **QA および公開**<br>Google Tag Manager の [[デバッグツール](https://support.google.com/tagmanager/answer/6107056?hl=en)] を使用して、新しい SDK バージョンが動作していることを確認してから、タグコンテナーに更新を公開します。

## トラブルシューティングのステップ {#troubleshooting}

### タグデバッグを有効にする {#debugging}

それぞれのBraze タグ テンプレートにはオプションの**GTM タグ デバッグ** チェックボックスがあり、ウェブページのJavaScript コンソールへのデバッグメッセージのログ記録に使用できます。

![Google Tag Managerのデバッグツール]({% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %})

### デバッグモードに入る

Google Tag Manager の統合をデバッグするもう1つの方法は、Google の [[プレビューモード](https://support.google.com/tagmanager/answer/6107056)] 機能を使用することです。

これにより、Web ページのデータレイヤーから、トリガーされた Braze 各タグに送信されている値を特定できるほか、トリガーされたタグとトリガーされなかったタグについても確認できます。

![Braze 初期化タグの概要ページには、トリガーされたタグに関する情報など、タグの概要が表示されます。]({% image_buster /assets/img/web-gtm/gtm-debug-mode.png %})

### 詳細ログの有効化

Braze テクニカルサポートがテスト中にログにアクセスできるようにするには、Google Tag Manager 統合で詳細ログを有効にします。これらのログは、ブラウザーの[開発者ツール](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools)の [**コンソール**] タブに表示されます。

Google Tag Manager 統合で、Braze 初期化タグに移動し、[**Web SDK ログを有効にする**] を選択します。

![Web SDK ログを有効にするオプションがオンになっている Braze 初期化タグの概要ページ。]({% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %})

[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md
