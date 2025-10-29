## 前提条件

このチュートリアルを始める前に、お使いのBraze SDKが最小バージョン要件を満たしていることを確認する：

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Web SDKのバナーを表示する

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="バナーウェブの表示" %}

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
lines-index.js=8-23

#### 2\.バナーの更新をサブスクライバーする

`subscribeToBannersUpdates()` 、バナーが更新されるたびに実行されるハンドラを登録する。ハンドラー内部で、`braze.getBanner("global_banner")` を呼び出し、最新の配置を取得する。

!!step
lines-index.js=15-22

#### 3\.バナーとハンドルコントロールグループを挿入する。

`braze.insertBanner(banner, container)` 、バナーが返されたときに挿入する。レイアウトをすっきりさせるために、コントロールグループに属するバナーは非表示または折りたたむ（たとえば、`isControl` が`true` の場合）。

!!step
lines-index.js=25

#### 4. バナーをリフレッシュする

SDKを初期化した後、`requestBannersRefresh(["global_banner", ...])` を呼び出し、各セッションの開始時にバナーがリフレッシュされるようにする。

また、この関数をいつでも呼び出して、後でバナーの配置をリフレッシュすることもできる。

!!step
lines-main.html=3

#### 5. バナー用のコンテナを追加する

HTMLに新しい`<div>` 要素を追加し、`global-banner-container` のように、バナー関連の短い`id` を付ける。Brazeはこの`<div>` 、あなたのバナーをページに挿入する。

{% endscrolly %}
