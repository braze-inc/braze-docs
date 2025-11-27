---
nav_title: アクセシビリティ
article_title: アクセシビリティ
platform: Web
page_order: 22
page_type: reference
description: "ここでは、Braze がアクセシビリティをサポートする方法について説明します。"

---

# アクセシビリティ

> ここでは、Braze がインテグレーション内でアクセシビリティをサポートする方法について説明します。

Braze Web SDK は、[Web コンテンツアクセシビリティガイドライン(WCAG 2.1)](https://www.w3.org/TR/WCAG21/) によって提供される標準をサポートしています。私たちは、アクセシビリティ・スタンダードを維持するために、すべての新しいビルドで、コンテンツカードsとアプリ内メッセージsの[100/100の灯台スコア](https://developer.chrome.com/docs/lighthouse/accessibility/scoring)を維持します。

## 前提条件

WCAG 2.1を満たす最低SDKはv3.4.0に近い。ただし、大規模な"画像 タグ修正の場合は、少なくともv6.0.0 にアップグレードすることをお勧めします。

### 注目すべきアクセシビリティの修正

| バージョン | タイプ | 主な変更点 |
|---------|------|-------------|
| 4\. | **メジャー** | `<img>` タグ s、`imageAltText`、または`language` フィールド s、全般的なUI アクセシビリティの向上 |
| 4\. | 軽微 | スクロール可能なテキストアクセシビリティの向上 |
| 4\. | 修正する | コンテンツカード`article` ロールの修正 |
| 4\. | 軽微 | ボタン用の45x45px 最小タッチターゲット |
| 4\. | 軽微 | "画像s のデフォルトアルトテキスト |
| 4\. | **メジャー** | セマンティックHTML(`h1`または`button`)、ARIA 属性 s、キーボードナビゲーション、フォーカスマネジメント |
| 4\. | 軽微 | フォーカス管理、キーボードナビゲーション、ラベル |
{: .reset-td-br-1, .reset-td-br-2 role="presentation" }

## サポートされるアクセシビリティ機能

コンテンツカード s およびアプリ内メッセージ s のこれらの機能に対応しています。

- ARIAの役割とラベル
- キーボードナビゲーションのサポート
- 重点管理
- スクリーンリーダーのお知らせ
- "画像 s のアルトテキストサポート

## SDK統合のアクセシビリティガイドライン

基本的なアクセシビリティガイドラインについては、[Braze]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/accessibility)のアクセシブルメッセージの作成を参照してください。本書では、Braze Web SDKをWeb アプリライセンスに統合する際に、アクセスしやすくするためのヒントとベストプラクティスについて説明します。

### コンテンツカードによって促進された

#### 最大高さの設定

コンテンツカードが縦のスペースを過剰に消費し、アクセシビリティを向上させないようにするには、次の例のようにフィードコンテナーに最高の高さを設定します。

{% raw %}
```css
/* Limit the height of the Content Cards feed */
.ab-feed {
  max-height: 600px; /* Adjust to your needs */
  overflow-y: auto;
}

/* For inline feeds (non-sidebar), you may want to limit individual cards */
.ab-card {
  max-height: 400px; /* Optional: limit individual card height */
  overflow: hidden;
}
```
{% endraw %}

#### ビューポートに関する考慮事項

インラインで表示されるコンテンツカードについては、この例のようにビューポートのトレーニングts を考慮してください。

{% raw %}
```css
/* Limit feed height on mobile to prevent covering too much screen */
@media (max-width: 768px) {
  body > .ab-feed {
    max-height: 80vh; /* Leave space for other content */
  }
}
```
{% endraw %}

### アプリ内メッセージ

{% alert warning %}
スクリーンリーダーでは使用できないため、スライドアプリ内メッセージsの中に大切な情報を入れないでください。
{% endalert %}

### モバイルに関する考慮事項

#### レスポンシブデザイン

SDKにはレスポンシブブレークポイントが含まれます。次の例のように、カスタマイズが画面サイズ全体で機能することを確認します。

{% raw %}
```css
/* Mobile-specific accessibility considerations */
@media (max-width: 768px) {
  /* Ensure readable font sizes */
  .ab-feed {
    font-size: 14px; /* Minimum 14px for mobile readability */
  }
  
  /* Ensure sufficient touch targets */
  .ab-card {
    padding: 16px; /* Adequate padding for touch */
  }
}
```
{% endraw %}

### アクセシビリティのテスト

#### 手動テストチェックリスト

次のタスクを実行して、アクセシビリティを手動でテストします。

- コンテンツカードとアプリ内メッセージをキーボードのみでナビゲートする(タブ、入力、空白)
- スクリーンリーダーを使ったテスト(NVDA、JAWS、VoiceOver)
- すべての"画像にアルトテキストがあることを確認する
- カラーコントラスト比の確認(WebAIM Contrast Checkerなどのツールを使用)
- タッチを使ったモバイルデバイスのテスト
- フォーカスインジケータが表示されていることを確認する
- 試験モーダル電文焦点アプリ中
- すべての対話型要素がキーボードで到達可能であることを確認する

### 一般的なアクセシビリティの問題

一般的なアクセシビリティの問題を回避するには、次の手順を実行します。

1. **フォーカススタイルを維持する:**SDKのフォーカスインジケータは、鍵盤ユーザーに不可欠です。
2. **非インタラクティブ要素では、`display: none` のみを使用します。**対話型要素を非表示にするには、`visibility: hidden` または`opacity: 0` を使用します。
3. **ARIA 属性s を上書きしないでください。**SDKは、アプリの適切なARIAロールとラベルを設定します。
4. **`tabindex` 属性s を使用します。**キーボードナビゲーションの順序をコントロールします。
5. **`overflow: hidden` を設定した場合は、スクロールを指定します。**スクロール可能なコンテンツがアクセス可能であることを確認します。
6. **組み込みのキーボードハンドラに干渉しないでください。**既存のキーボードナビゲーションが機能することを確認します。