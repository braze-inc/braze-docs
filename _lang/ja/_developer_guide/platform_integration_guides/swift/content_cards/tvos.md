---
nav_title: tvOS
article_title: tvOS用コンテンツカード
platform: tvOS
page_type: reference
description: "AppleのtvOSプラットフォーム用にコンテンツカードをカスタマイズする方法を学ぶ。"
page_order: 1
---

# コンテンツカードをtvOS用にカスタマイズする

> AppleのtvOSプラットフォーム用にコンテンツカードをカスタマイズする方法を学ぶ。

{% alert important %}
コンテンツカードはSwift SDKを使ったヘッドレスUIでサポートされているため、独自のカスタムUIを実装する必要がある。
{% endalert %}

## tvOSアプリを設定する

### ステップ 1:新しいiOSアプリを作成する

Brazeで、**Settings**>**App Settingsを**選択し、**Add Appを**選択する。tvOSアプリの名前を入力し、_tvOSではなく_ **iOSを**選択_し、_ **Add Appを**選択する。

![ALT_TEXT.]({% image_buster /assets/img/tvos.png %}){: style="width:70%"}

{% alert warning %}
**tvOS**チェックボックスを選択した場合、コンテンツカードをtvOS用にカスタマイズすることはできない。
{% endalert %}

### ステップ2:アプリのAPIキーを取得する

アプリの設定で、新しいtvOSアプリを選択し、アプリのAPIキーをメモする。このキーを使ってXcodeでアプリを設定する。

![ALT_TEXT]({% image_buster /assets/img/tvos1.png %}){: style="width:70%"}

### ステップ 3:BrazeKitを統合する

アプリのAPIキーを使用して、Xcodeで[Braze Swift SDKを](https://github.com/braze-inc/braze-swift-sdk)tvOSプロジェクトに統合する。Braze Swift SDKからBrazeKitを統合するだけでよい。

### ステップ 4:カスタムUIを作成する

BrazeはtvOS上のコンテンツカードのデフォルトUIを提供していないため、自分でカスタマイズする必要がある。完全なチュートリアルについては、ステップ・バイ・ステップのチュートリアルを参照のこと：[コンテンツカードをtvOS用にカスタマイズする](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/content-cards-customization/)。サンプルプロジェクトについては、[Braze Swift SDK samplesを](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#contentcards-custom-ui)参照のこと。
