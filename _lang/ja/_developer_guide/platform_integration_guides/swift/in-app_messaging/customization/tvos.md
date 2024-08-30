---
nav_title: tvOS
article_title: tvOS のアプリ内メッセージ
platform: tvOS
page_type: reference
description: "AppleのtvOSプラットフォーム向けにアプリ内メッセージをカスタマイズする方法を紹介する。"
page_order: 0
---

# tvOSのアプリ内メッセージをカスタマイズする

> AppleのtvOSプラットフォーム向けにアプリ内メッセージをカスタマイズする方法を紹介する。

{% alert important %}
アプリ内メッセージングはSwift SDKを使ったヘッドレスUIでサポートされており、tvOS用のデフォルトUIやビューは含まれていないため、独自のカスタムUIを実装する必要があることを覚えておこう。
{% endalert %}

## tvOSアプリを設定する

### ステップ 1:新しいiOSアプリを作成する

Brazeで、**Settings**>**App Settingsを**選択し、**Add Appを**選択する。tvOSアプリの名前を入力し、_tvOSではなく_ **iOSを**選択_し、_ **Add Appを**選択する。

![ALT_TEXT.]({% image_buster /assets/img/tvos.png %}){: style="width:70%"}

{% alert warning %}
**tvOS**チェックボックスを選択すると、tvOS用のアプリ内メッセージをカスタマイズできなくなる。
{% endalert %}

### ステップ2:アプリのAPIキーを取得する

アプリの設定で、新しいtvOSアプリを選択し、アプリのAPIキーをメモする。このキーを使ってXcodeでアプリを設定する。

![ALT_TEXT]({% image_buster /assets/img/tvos1.png %}){: style="width:70%"}

### ステップ 3:BrazeKitを統合する

アプリのAPIキーを使用して、Xcodeで[Braze Swift SDKを](https://github.com/braze-inc/braze-swift-sdk)tvOSプロジェクトに統合する。Braze Swift SDKからBrazeKitを統合するだけでよい。

### ステップ 4:カスタムUIを作成する

BrazeはtvOS上でアプリ内メッセージのデフォルトUIを提供していないため、自分でカスタマイズする必要がある。完全なチュートリアルについては、ステップ・バイ・ステップのチュートリアルを参照のこと：[tvOSのアプリ内メッセージをカスタマイズする](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization)。サンプルプロジェクトについては、[Braze Swift SDK samplesを](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui)参照のこと。
