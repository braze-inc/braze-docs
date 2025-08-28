---
nav_title: SDK 통합
article_title: Braze SDK 통합
description: "Braze SDK를 통합하는 방법을 알아보세요."
page_order: 2.0
---

# Braze SDK 통합

> Braze SDK를 모바일 앱에 통합하는 방법을 알아보세요. 각 SDK는 자체 공개 GitHub 리포지토리에서 호스팅되며, 여기에는 Braze 기능을 테스트하거나 자체 애플리케이션과 함께 구현하는 데 사용할 수 있는 완전히 빌드 가능한 샘플 앱이 포함되어 있습니다. 자세히 알아보려면 [참조, 리포지토리 및 샘플 앱을 참조하세요]({{site.baseurl}}/developer_guide/references/). SDK에 대한 자세한 내용은 [시작하기를 참조하세요: 통합 개요]({{site.baseurl}}/developer_guide/getting_started/integration_overview/).

{% alert tip %}

{% endalert %}

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/android/sdk_integration.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/sdk_integration.md %}
{% endsdktab %}

{% sdktab web %}
{% multi_lang_include developer_guide/web/sdk_integration.md %}
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

{% sdktab unreal engine %}
{% multi_lang_include developer_guide/unreal_engine/sdk_integration.md %}
{% endsdktab %}

{% sdktab xamarin %}
{% multi_lang_include developer_guide/xamarin/sdk_integration.md %}
{% endsdktab %}

{% endsdktabs %}

{% alert note %}
SDK 통합에 대한 QA를 수행하는 동안 [SDK 디버거를]({{site.baseurl}}/developer_guide/sdk_integration/debugging) 사용하면 앱에 대한 자세한 로깅을 켜지 않고도 문제를 해결할 수 있습니다.
{% endalert %}
