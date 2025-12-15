---
nav_title: SDK の統合
article_title: Braze SDKの統合
description: "Braze SDKの統合方法を学習する。"
page_order: 2.0
---

# ![Brazeロゴ]({% image_buster /assets/Braze_Primary_Icon_BLACK.svg %}){: style="float:right;width:120px;border:0;" class="noimgborder"}Braze SDKの統合

> Braze SDKをモバイルアプリに統合する方法を学習。各SDKは、独自のGitHub公開リポジトリでホストされており、Brazeの機能をテストしたり、独自のアプリケーションと一緒に実装したりするために使用できる、完全にビルド可能なサンプルアプリが含まれている。詳しくは、[参照資料、リポジトリ、サンプルアプリ]({{site.baseurl}}/developer_guide/references/)を参照してください。SDK に関する一般的な情報については、[はじめに] を参照してください。統合の概要]({{site.baseurl}}/developer_guide/getting_started/integration_overview/)。

{% alert tip %}

{% endalert %}

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/sdk_integration.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/sdk_integration.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/sdk_integration.md %}
{% endsdktab %}

{% sdktab cordova %}
{% multi_lang_include developer_guide/cordova/sdk_integration.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/sdk_integration.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/sdk_integration.md %}
{% endsdktab %}

{% sdktab roku %}
{% multi_lang_include developer_guide/roku/sdk_integration.md %}
{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/sdk_integration.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
{% multi_lang_include developer_guide/xamarin/sdk_integration.md %}
{% endsdktab %}

{% sdktab chatgpt apps %}
{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}
{% endsdktab %}

{% sdktab vega %}
{% multi_lang_include developer_guide/vega/sdk_integration.md %}
{% endsdktab %}
{% endsdktabs %}

{% alert note %}
SDKインテグレーションのQAを行う際、[SDKデバッガーを]({{site.baseurl}}/developer_guide/sdk_integration/debugging)使用すれば、アプリの冗長ロギングをオンにすることなく、問題のトラブルシューティングを行うことができる。
{% endalert %}
