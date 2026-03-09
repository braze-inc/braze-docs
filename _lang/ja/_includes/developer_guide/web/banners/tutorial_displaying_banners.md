## 前提条件

このチュートリアルを始める前に、Braze SDKが最低バージョン要件を満たしていることを確認せよ：

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Web SDKのバナーを表示する

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
lines-=8-23index.js

#### 2\.バナーの更新情報をサブスクライバーが購読する

バナーが更新されるたびに実行されるハンドラを登録するには、\``subscribeToBannersUpdates()`use` を使用する。ハンドラ内で、最新の配置を取得`braze.getBanner("global_banner")`するために呼び出す。

!!step
行index.js番号15-22

#### 3\.バナーを挿入し、コントロールグループを扱う

バナーが返却されたら、を使って`braze.insertBanner(banner, container)`挿入する。レイアウトを整理するために、コントロールグループの一部であるバナーは非表示にするか折りたたむこと（例えば、が`isControl`の場合`true`）。

!!step
lines-index.js=25

#### 4. バナーを更新する

SDKを初期化した後、各セッションの開始時にバナーが更新されるように、\`refreshBanners()\`を`requestBannersRefresh(["global_banner", ...])`呼び出す。

この関数は後でバナー配置を更新するため、いつでも呼び出すことができる。

!!step
lines-=3main.html

#### 5. バナー用のコンテナを追加する

HTMLに新しい\`banner`<div>``要素を追加し、短いバナー関連の`class`を付ける。`global-banner-container`例えば\``id`class="banner"`のように。Brazeはこのコードを使用して、あなたの`<div>`バナーをページに挿入する。

{% endscrolly %}
