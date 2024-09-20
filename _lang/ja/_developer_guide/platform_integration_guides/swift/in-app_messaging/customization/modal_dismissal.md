---
nav_title: モーダルを閉じる
article_title: iOS のアプリ内メッセージモーダルを閉じる
platform: Swift
page_order: 7
description: "このリファレンス記事では、Swift SDK のアプリ内メッセージングモーダルを閉じる操作について説明します。"
channel:
  - in-app messages
---

# モーダルを閉じる

> 外側のタップで閉じる操作を有効にするため、カスタマイズするアプリ内メッセージの種類の `Attributes` 構造体で `dismissOnBackgroundTap` プロパティを変更できます。 

たとえば、モーダル画像のアプリ内メッセージに対してこの機能を有効にする場合は、以下を設定します。

{% tabs %}
{% tab 速い %}

```swift
BrazeInAppMessageUI.ModalImageView.Attributes.defaults.dismissOnBackgroundTap = true
```

{% endtab %}
{% tab 目標-C %}

`Attributes` によるカスタマイズは Objective-C では使用できません。

{% endtab %}
{% endtabs %}

デフォルト値は `false` です。これにより、ユーザーがアプリ内メッセージの外側をタップしたときにモーダルアプリ内メッセージが閉じられるかどうかが決まります。

| `DismissModalOnOutsideTap` | 説明 |
|----------|-------------|
| `true`         | モーダルなアプリ内メッセージは、外側のタップで解除される。     |
| `false`        | デフォルトでは、モーダルなアプリ内メッセージは外部タップでは解除されない。 |
{: .reset-td-br-1 .reset-td-br-2}

アプリ内メッセージのカスタマイズの詳細については、こちらの[記事](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization)を参照してください。