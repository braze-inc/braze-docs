---
nav_title: 기타 통합
article_title: 기타 통합
page_order: 6
---

# 기타 통합

> 이 통합은 Cordova Braze SDK에서 지워되는 다른 통합입니다.

{% multi_lang_include cordova/prerequisites.md %}

## 인앱 메시징

기본적으로 Cordova SDK는 변경 없이 인앱 메시지를 지원합니다. 인앱 메시지 사용자 지정에 대한 자세한 내용은 [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/) 또는 [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/) 통합 예시를 참조하세요. 또한 구현 샘플을 보려면 샘플 [Cordova 애플리케이션](https://github.com/braze-inc/braze-cordova-sdk/blob/master/sample-project/www/js/index.js)이나 샘플 [Android](https://github.com/braze-inc/braze-android-sdk) 또는 [iOS](https://github.com/braze-inc/braze-swift-sdk) 애플리케이션에서 확인할 수 있습니다.

### GIF 지원

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

## 뉴스피드

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

뉴스피드를 Cordova 앱에 통합하는 방법에 대한 자세한 내용은 [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/integration/) 및 [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/news_feed/integration/) 통합 지침을 참조하세요. 또는 Cordova 플러그인에서는 추가 통합 없이 Modal 뉴스피드를 실행하는 메서드(`launchNewsFeed`)를 제공합니다.

Braze Cordova SDK에는 다양한 카테고리의 열람 또는 미열람 뉴스피드 카드 수를 가져오는 여러 메서드가 있습니다. 예제는 [샘플 프로젝트 구현 샘플](https://github.com/braze-inc/braze-cordova-sdk/blob/master/sample-project/www/js/index.js)에서 확인하세요.
