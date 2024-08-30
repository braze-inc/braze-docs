---
nav_title: Google Tag Manager
article_title: Webのグーグルタグマネージャ
platform: Web
page_order: 20
description: "ここでは、Googleタグマネージャを使用してBrazeをWeb サイトにデプロイする方法について説明します。"

---

# Google Tag Manager

> ここでは、Googleタグマネージャ(GTM)を使用してWeb サイトにBraze Web SDKを追加する方法について、ステップごとに説明します。[Google タグマネージャ][2]を使用すると、実稼働コードの解放や開発を必要とせずに、Web サイト上のタグをリモートで追加、削除、および編集できます。

Braze によって構築された2 つのGoogle タグマネージャテンプレート、[初期化タグ](#initialization-tag) と[アクションタグ](#actions-tag) があります。

どちらのタグも、\[Googleのコミュニティギャラリー][15]]から、またはコミュニティテンプレートから新しいタグを追加するときにBrazeを検索することで、ワークスペースに追加できます。

![ギャラリー検索の"画像]\[gtm-community-gallery-search]

## Google EU ユーザー同意ポリシーを更新

{% alert important %}
Googleは[EUユーザー同意ポリシー](https://www.google.com/about/company/user-consent-policy/)を[Digital Markets Act (DMA)</この新たな変更は、広告主に対し、一定の事項を自社及び英国のエンドユーザーに開示するとともに、その同意を得ることを要求するものである。詳細については、次のドキュメントを参照してください。
{% endalert %}

Google のEU ユーザー同意ポリシーの一部として、次のブールカスタム属性s をユーザープロファイル s にログに記録する必要があります。

- `$google_ad_user_data`
- `$google_ad_personalization`

GTM インテグレーションを使用してこれらを設定する場合、カスタム属性 s でカスタムHTML タグを作成する必要があります。以下は、これらの値を(文字列としてではなく)ブールデータ型としてログに記録する方法の例です。

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

詳細については、[Audience Sync to Google]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/)を参照してください。

## 初期化タグテンプレート {#initialization-tag}

初期化タグを使用して、Braze Web SDKをWeb サイトに追加します。

### ステップ 1:プッシュセットアップ(オプション)

オプションで、Google タグマネージャをプッシュ送信できるようにするには、まず[push integration]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/) のガイドラインに従い、以下の手順を実行します。
1. サイトのサービスワーカーを設定し、サイトのルートディレクトリに配置します
2. ブラウザ登録を設定する- サービスワーカーが設定されたら、`braze.requestPushPermission()` メソッドをアプリまたはカスタムHTML タグ(GTM ダッシュボードを使用) でネイティブに設定する必要があります。また、SDKが初期化された後にタグが起動されるようにする必要があります。

### ステップ2:初期化タグの選択

コミュニティーテンプレートギャラリーでBrazeを検索し、**Braze初期化タグ**を選択します。

![Braze 初期化タグの設定設定を示すダイアログボックス。設定は"タグ type" " API キー" " &API エンドポイント" " " SDK version" " 外部ユーザー ID" " Safari Web プッシュ ID".]\[gtm-initialization-タグ]

### ステップ 3:設定の設定

Braze API アプリ 識別子キーとSDKエンドポイントを入力します。これは、ダッシュボードの**設定の管理** ページにあります。Web SDKの最新の`major.minor` バージョンを入力します。たとえば、最新バージョンが`4.1.2` の場合、`4.1` と入力します。SDK版の一覧は、\[changelog]\[changelog]] で表示できます。

### ステップ 4:初期化オプションの選択

\[Initial setup][7] ガイドで説明されている追加の初期化オプションのオプションセットから選択します。

### ステップ 5: 検証とQA

このタグをデプロイしたら、適切なインテグレーションを確認する方法が2 つあります。

1. Googleタグマネージャの\[デバッグツール]\[gtm-debugging-tool]]を使用すると、設定したページまたはイベントでBraze初期化タグがトリガーされていることがわかります。
2. Braze へのネットワークリクエストが表示され、グローバル`window.braze` ライブラリーがウェブページで定義されます。

## アクションタグテンプレート {#actions-tag}

Brazeアクションタグテンプレートでは、プライバシー要件のトリガー カスタムイベント、購入の追跡、ユーザー IDの変更、"トラッキングの停止または再開を行うことができます。

![]\[gtm-アクションs-タグ]

### ユーザー外部識別子の変更 {#external-id}

**Change User**タグ型は、[`changeUser`method](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)を呼び出します。 

このタグは、ユーザーがログインするとき、または一意の`external_id` 識別子で識別されるときに使用します。

現行のユーザーの一意のID を**外部ユーザー ID** フィールドに入力してください。通常は、Web サイトから送信されたデータレイヤー変数を使用して入力します。

![Braze アクションタグ設定設定を示すダイアログボックス。含まれる設定は、" タグ type" および" 外部ユーザー ID".]\[gtm-change-ユーザー]

### 履歴カスタムイベントs {#custom-events}

**カスタムイベント**タグ型は、[`logCustomEvent`メソッド](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent)を呼び出します。

このタグを使用して、オプションでカスタムイベントプロパティーを含むカスタムイベントs をBrazeに送信します。

変数を使用するか、イベント名を入力して、**Event Name**を入力します。

イベントプロパティを追加するには、**Add Row** ボタンを使用します。

![Braze アクションタグ設定設定を示すダイアログボックス。含まれる設定は、" タグ type"(カスタムイベント)、" event name"(ボタンをクリック)、"event properties".]\[gtm-custom-event] です]

### Eコマースイベント {#ecommerce}

サイトが標準\[e コマース event]\[e コマース]データレイヤーアイテムをGoogle タグマネージャに記録する場合、**E-commerce Purchase**タグ種別を使用できます。このアクション型では、`items`の一覧で送信されたアイテムごとに、個別の"purchase"がBrazeで記録されます。

購入プロパティリストでキーを指定することで、購入プロパティとして含める追加のプロパティの名前を指定することもできます。Brazeは、一覧に追加した購入プロパティーのログに記録されている個々の`item` 内を検索します。

たとえば、e コマースの給与読み込むに次の`items` が含まれているとします。

```
items: [{
  item_name: "5 L WIV ECO SAE 5W/30",
  item_id: "10801463",
  price: 24.65,
  item_brand: "EUROLUB",
  quantity: 1
}]
```

購入プロパティとして`item_brand` と`item_name` のみを渡す場合は、これら2 つのフィールドs を購入プロパティテーブルに追加します。プロパティを指定しない場合、\[`logPurchase`]\[log-purchase] Braze の呼び出しで購入プロパティは送信されません。

### 購入の追跡 {#purchases}

**Purchase**タグ型は、[`logPurchase`method](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase)を呼び出します。

このタグを使用して、Brazeへの購入を追跡します。オプションで、購入プロパティを含めます。

**商品ID**と**価格**フィールドsが必要です。

購入プロパティを追加するには、**Add Row** ボタンを使用します。

![Braze アクションタグ設定設定を示すダイアログボックス。設定は" タグ type" " external ID" " &price" " &cuot; &currency コード" " quantity" および" purchase properties".<]

### "トラッキングの停止と再開 {#stop-tracking}

Braze "トラッキングがプライバシー上の理由でウェブ"トラッキングをオプトアウトしたことを示すユーザーが表示された後など、Web サイトでBraze "トラッキングを無効にしたり、再有効にしたりする必要が生じることがあります。

ウェブ"トラッキングを無効または再有効にするには、**Disable "トラッキング**または**Resume "トラッキング**タグ型を使用します。これら2 つのオプションは、[`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) および[`enableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) を呼び出します。

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

### 基準ユーザー 属性s {#standard-attributes}

ユーザ定義ユーザー 属性s と同じ方法で、ユーザーの名などのスタンダードユーザー 属性をログに記録する必要があります。標準属性項目に渡す値が、\[ユーザクラス][16] ドキュメントで指定された期待される形式と一致することを確認します。

たとえば、性別属性では、`"m" | "f" | "o" | "u" | "n" | "p"` のいずれかの値を使用できます。したがって、ユーザーの性別を女性に設定するには、次の内容のカスタムHTML タグを作成します。

```html
<script>
window.braze.getUser().setGender("f")
</script>
```

## コンテンツカードの統合

Google Tag Manager を使用して[コンテンツカード]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) メッセージング チャネルを統合するステップがいくつかあります。Google Tag Manager は、[ Braze CDN]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn) (当社Web SDKのバージョン) をWeb サイト コードに直接注入することで機能します。これは、コンテンツカードを実装する場合を除き、Google Tag Manager なしでSDKを統合した場合と同様に、すべてのSDK方法を利用できることを意味します。

### オプション 1: GTM を使用した統合

コンテンツカードフィードを標準的に統合するには、Google タグマネージャで**カスタムHTML**タグを使用できます。以下をカスタムHTML タグに追加すると、標準のコンテンツカードフィードが有効になります。

```html
<script>
   window.braze.showContentCards();
</script>
```

![コンテンツカード フィード.]\[gtm-content-カード s を示すカスタムHTML タグのGoogle タグマネージャでのタグ設定]

### オプション 2: Web サイトに直接的に統合する

コンテンツ・カードとそのフィードのアプリ・イヤーのカスタマイズを自由にするために、コンテンツ・カードをネイティブ・Web サイトに直接的に統合することができます。これには、スタンダードフィードユーザーインターフェイスを使用する方法と、カスタムフィードユーザーインターフェイスを作成する方法の2 つのアプリ侵害があります。

#### 基準フィード

[スタンダードフィード UI]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/#standard-feed-ui)を実装する場合、Brazeメソッドはメソッドの先頭に`window.`を追加する必要があります。たとえば、`braze.showContentCards` は代わりに`window.braze.showContentCards` にする必要があります。

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

Braze Web SDKの最新バージョンにアップグレードするには、Googleタグマネージャダッシュボードで次の3つのステップを実行します。

1. **アップデートタグ テンプレート**<br>ワークスペース内の**Templates** ページに移動します。更新が利用可能であることを示すアイコンが表示されます。<br><br>![更新が表示されるテンプレートページ]\[gtm-更新-available]<br><br>そのアイコンをクリックし、変更を確認した後、**Accept Update**をクリックします。<br><br>![新旧のタグ テンプレート s をボタンと"Accept 更新"]\[gtm-accept-更新]<br><br>
2. **アップデートバージョン番号**<br>タグ テンプレートが更新されたら、Braze初期化タグを編集し、最新の`major.minor`バージョンにSDKバージョンを更新します。たとえば、最新バージョンが`4.1.2` の場合、`4.1` と入力します。SDK版の一覧は、\[changelog]\[changelog]] で表示できます。<br><br>![SDK Version]\[gtm-version-number]を変更するためのインプットフィールドを持つBraze初期化テンプレート]<br><br>
3. **QAおよび発行**<br>Google タグマネージャの\[デバッグツール]\[gtm-debugging-tool]] を使用して、新しいSDKが動作していることを確認してから、タグコンテナーに更新を公開します。

## ステップのトラブルシューティング {#troubleshooting}

### タグデバッグを有効にする {#debugging}

それぞれのBraze タグ テンプレートにはオプションの**GTM タグ デバッグ** チェックボックスがあり、ウェブページのJavaScript コンソールへのデバッグメッセージのログ記録に使用できます。

![Google タグマネージャのデバッグツール]\[gtm-タグ-debugging]

### デバッグモードに入る

Google Tag Manager の統合をデバッグするもう1 つの方法は、Google の\[プレビューモード][14] 機能を使用することです。

これにより、ウェブページのデータレイヤーからトリガーされたBraze タグに送信されている値を特定し、どのタグがトリガーされたか、またはされなかったかを説明することができます。

![Braze 初期化タグの概要ページには、タグの概要が表示されます。これには、どのタグがトリガー ed.]\[gtm-タグ-debug-mode]

### 詳細ログの有効化

Braze テクニカルサポートがテスト中にログにアクセスできるようにするには、Google タグマネージャインテグレーションで詳細ログを有効にします。これらのログは、ブラウザーの[開発者ツール](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools) の**コンソール** タブでアプリ取得されます。

Googleタグマネージャインテグレーションで、Braze初期化タグに移動し、**Web SDKログを有効にする**を選択します。

![Web SDKログを有効にするオプションがオンになっているBraze初期化タグサマリページ。]\[gtm-verbose-logging]]

[2]: https://support.google.com/tagmanager/answer/6103696
\[gtm-community-gallery-search]: {% image_buster /assets/img/web-gtm/gtm-community-gallery-search.png %}
\[gtm-initialization-tag]: {% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %}
\[gtm-actions-tag]: {% image_buster /assets/img/web-gtm/gtm-actions-tag.png %}
[6]: {{ site.baseurl }}/user_guide/administrative/app_settings/manage_app_group/app_group_management/#app-group-management
[7]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#step-2-initialize-braze
\[gtm-change-user]: {% image_buster /assets/img/web-gtm/gtm-change-user.png %}
\[gtm-custom-event]: {% image_buster /assets/img/web-gtm/gtm-custom-event.png %}
\[gtm-purchase]: {% image_buster /assets/img/web-gtm/gtm-purchase.png %}
\[gtm-tag-debugging]: {% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %}
\[gtm-tag-debug-mode]: {% image_buster /assets/img/web-gtm/gtm-debug-mode.png %}
[14]: https://support.google.com/tagmanager/answer/6107056
[15]: https://tagmanager.google.com/gallery/#/?filter=braze
[16]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html
\[gtm-update-available]: {% image_buster /assets/img/web-gtm/gtm-update-available.png %}
\[gtm-accept-update]: {% image_buster /assets/img/web-gtm/gtm-accept-update.png %}
\[gtm-version-number]: {% image_buster /assets/img/web-gtm/gtm-version-number.png %}
\[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md
\[gtm-debugging-tool]: https://support.google.com/tagmanager/answer/6107056?hl=en
\[ecommerce]: https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm
\[log-purchase]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase
\[gtm-verbose-logging]: {% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %}
\[gtm-content-cards]: {% image_buster /assets/img/web-gtm/gtm_content_cards.png %}
