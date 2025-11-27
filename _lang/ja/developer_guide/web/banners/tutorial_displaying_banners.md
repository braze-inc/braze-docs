## 前提条件

このチュートリアルを開始する前に、Braze SDKが最低バージョン要件を満たしていることを確認してください。

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Web SDKのバナーの表示

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Displaying Banners Web" %}

{% scrolly %}

```js file=index.js
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  enableLogging: true,
});

braze.subscribeToBannersUpdates((banners) => {
  // Get this placement's banner. If it's `null`, the user did not qualify for any banners.
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  const container = document.getElementById("global-banner-container");

  braze.insertBanner(globalBanner, container);

  if (globalBanner.isControl) {
    // Hide or collapse the container
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

```html file=main.html
<!-- your html -->

<div id="global-banner-container" style="width: 100%; height: 450px;"></div>

<!-- ...the rest of your html -->
```

!!step
lines-index.js=5

#### 1\.デバッグを有効にする(オプション)

開発中のトラブルシューティングを容易にするために、デバッグを有効にすることを検討してください。

!!step
lines-index.js=9-21

#### 2\.バナー更新の購読

`subscribeToBannersUpdates()` を使用して、バナーが更新d のときに実行されるハンドラーを登録します。ハンドラ内で、`braze.getBanner("global_banner")` を呼び出して最新の配置を取得します。

!!step
lines-index.js=9-21

#### 3\.バナーを挿入し、コントロールグループsを扱う

返されたバナーを挿入するには、`braze.insertBanner(banner, container)` を使用します。レイアウトをきれいに保つには、コントロールグループから離れたバナーを隠したり折りたたんだりします(たとえば、`isControl` が`true` の場合)。

!!step
lines-index.js=25

#### 4\.バナーの更新

SDKを初期化した後、`requestBannersRefresh(["global_banner", ...])` を呼び出して、セッションの最初にバナーが更新されるようにします。

この関数は、後でバナーの配置を更新するためにいつでも呼び出すことができます。

!!step
lines-main.html=9-21

#### 5. バナーのコンテナを追加する

HTMLで、新しい`<div>` 要素を追加し、`global-banner-container` のような短いバナー関連の`id` を指定します。Braze は、この`<div>` を使用してバナーをページに挿入します。

{% endscrolly %}
