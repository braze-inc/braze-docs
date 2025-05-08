---
nav_title: SDK の統合
article_title: Braze SDKの統合
description: "Braze SDKの統合方法を学習する。"
page_order: 2.0
---

# Braze SDKの統合

> Braze SDKをモバイルアプリに統合する方法を学習。各SDKは、独自のGitHub公開リポジトリでホストされており、Brazeの機能をテストしたり、独自のアプリケーションと一緒に実装するために使用できる、完全にビルド可能なサンプルアプリが含まれている。詳しくは、[学習、リポジトリ、サンプルアプリを]({{site.baseurl}}/developer_guide/references/)参照のこと。SDKに関する一般的な情報については、[はじめにを参照のこと：統合の概要]({{site.baseurl}}/developer_guide/getting_started/integration_overview/)。

{% alert tip %}

{% endalert %}

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/android/sdk_integration.md %}
{% endsdktab %}

{% sdktab swift %}
guide/swift/sdk_integration.md developer_ %}
{% endsdktab %}

{% sdktab web %}
guide/web/sdk_integration.md developer_ %}
{% endsdktab %}

{% sdktab cordova %}
guide/cordova/sdk_integration.md developer_ %}
{% endsdktab %}

{% sdktab flutter %}
guide/flutter/sdk_integration.md developer_ %}
{% endsdktab %}

{% sdktab react native %}
guide/react_native/sdk_integration.md developer_ %}
{% endsdktab %}

{% sdktab roku %}
guide/roku/sdk_integration.md developer_ %}
{% endsdktab %}

{% sdktab unity %}
guide/unity/sdk_integration.md developer_ %}
{% endsdktab %}

{% sdktab unreal engine %}
guide/unreal_engine/sdk_integration.md developer_ %}
{% endsdktab %}

{% sdktab xamarin %}
guide/xamarin/sdk_integration.md developer_ %}
{% endsdktab %}
{% endsdktabs %}

{% alert note %}
SDKインテグレーションのQAを行う際、[SDKデバッガーを]({{site.baseurl}}/developer_guide/sdk_integration/debugging)使用すれば、アプリの冗長ロギングをオンにすることなく、問題のトラブルシューティングを行うことができる。
{% endalert %}