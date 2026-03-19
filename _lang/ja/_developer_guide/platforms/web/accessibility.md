---
nav_title: アクセシビリティ
article_title: アクセシビリティ
platform: Web
page_order: 22
page_type: reference
description: "この記事は、Brazeがアクセシビリティをどのようにサポートしているかを説明する。"

---

# アクセシビリティ

> この記事は、Brazeが統合環境内でアクセシビリティをどのようにサポートしているかについて概説する。

Braze Web SDKは、[Webコンテンツアクセシビリティガイドライン（WCAG 2.1）](https://www.w3.org/TR/WCAG21/)が提供する標準をサポートしている。我々はアクセシビリティ基準を維持するため、新規ビルド全てにおいてコンテンツカードとアプリ内メッセージに対し[100/100のライトハウススコア](https://developer.chrome.com/docs/lighthouse/accessibility/scoring)を維持している。

## 前提条件

WCAG 2.1を満たす最小のSDKバージョンは、v3.4.0に近い。ただし、画像タグの重大な修正のため、少なくともバージョン6.0.0へのアップグレードを推奨する。

### 主なアクセシビリティの修正

| バージョン | タイプ | 主な変更点 |
|---------|------|-------------|
| **6.0.0** | **主要** | 画像の`<img>`タグ化、フィールド`language``imageAltText`化、一般的なUIアクセシビリティの改善 |
| **3.5.0** | 軽微 | スクロール可能なテキストのアクセシビリティ改善 |
| **3.4.0** | 修正する | コンテンツカードの`article`役割修正 |
| **3.2.0** | 軽微 | ボタンの最小タッチターゲットは45×45ピクセルである |
| **3.1.2** | 軽微 | 画像のデフォルト代替テキスト |
| **2.4.1** | **主要** | 意味論的HTML（`h1`または`button`）、ARIA属性、キーボード操作、フォーカス管理 |
| **2.0.5** | 軽微 | フォーカス管理、キーボード操作、ラベル |
{: .reset-td-br-1, .reset-td-br-2 role="presentation" }

## サポートされているアクセシビリティ機能

コンテンツカードとアプリ内メッセージでは、以下の機能をサポートしている：

- ARIAの役割とラベル
- キーボードによる操作をサポートする
- 集中管理
- スクリーンリーダーの読み上げ
- 画像の代替テキスト対応

## SDK統合のためのアクセシビリティガイドライン

アクセシビリティに関する一般的なガイドラインについては[、Brazeにおけるアクセシブルなメッセージの作成]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/accessibility)を参照せよ。このガイドは、Braze Web SDKをWebアプリケーションに統合する際のアクセシビリティを最大限に高めるためのヒントとベストプラクティスを提供する。

### コンテンツカードによって促進された

#### 最大高さを設定する

コンテンツカードが縦方向に過剰なスペースを占めるのを防ぎ、アクセシビリティを向上させるため、フィードコンテナに最大高さを設定できる。例えば以下の例のように：

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

#### ビューポートの考慮事項

インラインで表示されるコンテンツカードについては、この例のようにビューポートの制約を考慮せよ。

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
重要な情報をスライドアップするアプリ内メッセージ内に配置してはならない。スクリーンリーダーでは読み取れないからだ。
{% endalert %}

### モバイルに関する考慮事項

#### レスポンシブデザイン

SDKにはレスポンシブブレークポイントが含まれている。カスタマイズが画面サイズを問わず機能することを確認せよ。例えばこの例のように：

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

アクセシビリティを手動でテストするには、以下のタスクを完了するんだ。

- コンテンツカードとアプリ内メッセージをキーボードのみ（Tab、Enter、スペース）で操作する
- スクリーンリーダー（NVDA、JAWS、VoiceOver）でテストする
- すべての画像に代替テキストがあることを確認せよ
- 色のコントラスト比を確認する（WebAIMコントラストチェッカーなどのツールを使用する）
- タッチ操作が可能なモバイル端末でテストする
- フォーカスインジケーターが表示されていることを確認せよ
- テスト用モーダルメッセージのフォーカス捕捉
- すべてのインタラクティブな要素がキーボードで操作可能であることを確認せよ

### よくあるアクセシビリティの問題

一般的なアクセシビリティの問題を避けるには、次のことを行え：

1. **フォーカススタイルを維持する：**SDKのフォーカスインジケーターはキーボードユーザーにとって不可欠だ。
2. **非対話`display: none`型要素でのみ使用せよ：**インタラクティブな要素を非表示にするには、`opacity: 0`または`visibility: hidden`を使用する。
3. **ARIA属性を上書きするな。**SDKは適切なARIAロールとラベルを設定する。
4. **属性`tabindex`を使う：**これらはキーボード操作の順序をコントロールする。
5. **設定した場合`overflow: hidden`、スクロールを提供する。**スクロール可能なコンテンツがアクセス可能であることを確認せよ。
6. **組み込みのキーボードハンドラに干渉するな：**既存のキーボード操作が機能することを確認せよ。