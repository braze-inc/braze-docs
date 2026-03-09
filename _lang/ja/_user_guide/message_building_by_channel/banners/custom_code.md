---
nav_title: カスタムコードとJavaScriptブリッジ
article_title: バナー用のカスタムコードとJavaScriptブリッジ
page_order: 2
page_type: reference
description: "バナーでのカスタムHTMLの使用方法と、JavaScriptブリッジを使ってクリックを記録し、Brazeアクションをトリガーする方法を学ぶ。"
channel:
  - banners
---

# バナー用のカスタムコードとJavaScriptブリッジ

> バナーコンポーザーで**カスタムコード**エディターブロックを使用する場合、クリックをログに記録するには、カスタムHTML内から\`\`を`brazeBridge.logClick()`呼び出す必要がある。バナーはHTMLアプリ内メッセージと同じJavaScriptブリッジを使用するため、同じメソッドとパターンが適用される。

バナーデザインでカスタムHTMLを使用する場合、Braze SDKはカスタムコード内の要素に自動的にクリックリスナーを添付できない。キャンペーン分析でトラッキングしたいクリック可能な要素（リンク、ボタンなど）については、明示的に`brazeBridge.logClick()`呼び出す必要がある。

例えば、カスタムHTML内のボタンをユーザーがタップした際にクリックを記録するには：

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

利用可能な全メソッドとクリックトラッキングオプションを含む、完全なJavaScriptブリッジリファレンスは以下のセクションを参照のこと。

## JavaScriptブリッジ {#javascript-bridge}

{% include javascript_bridge/reference.md %}
