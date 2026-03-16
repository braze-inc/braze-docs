---
nav_title: SDK 통합
article_title: Braze SDK 통합
description: "Braze SDK를 통합하는 방법을 알아보세요."
page_order: 2.0
---

# ![Braze 로고]({% image_buster /assets/Braze_Primary_Icon_BLACK.svg %}){: style="float:right;width:120px;border:0;" class="noimgborder"} Braze 소프트웨어 개발 키트 통합

> Braze SDK를 통합하는 방법을 알아보세요. 각 SDK는 자체 공개 GitHub 리포지토리에서 호스팅되며, 여기에는 Braze 기능을 테스트하거나 자체 애플리케이션과 함께 구현하는 데 사용할 수 있는 완전히 빌드 가능한 샘플 앱이 포함되어 있습니다. 자세히 알아보려면 [참조, 리포지토리 및 샘플 앱을 참조하세요]({{site.baseurl}}/developer_guide/references/). SDK에 대한 자세한 내용은 [시작하기를 참조하세요: 통합 개요]({{site.baseurl}}/developer_guide/getting_started/integration_overview/).

{% alert tip %}
SDK를 통합한 후에는 [SDK 인증을]({{site.baseurl}}/developer_guide/sdk_integration/authentication/) 인에이블하여 무단 SDK 요청을 방지함으로써 추가적인 보안 계층을 적용할 수 있습니다. 소프트웨어 개발 키트 인증은 웹, Android, 스위프트, React Native, Flutter, Unity, Cordova, .NET MAUI(Xamarin), 엑스포에서 사용할 수 있습니다.
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
SDK 통합에 대한 QA를 수행하는 동안 [SDK 디버거를]({{site.baseurl}}/developer_guide/sdk_integration/debugging) 사용하면 앱에 대한 자세한 로깅을 켜지 않고도 문제를 해결할 수 있습니다.
{% endalert %}
