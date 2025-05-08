---
nav_title: TV 및 OTT
article_title: Braze를 위한 TV 및 OTT 통합
page_order: 15

description: "이 문서에서는 Braze TV 및 OTT 기능, 통합, 사용 가능한 플랫폼 및 기타 기능을 자세히 설명합니다."
platform:
  - tvOS
  - Roku
  - Web
  - Android
  - FireOS
---

# TV 및 OTT 통합

> 기술이 새로운 플랫폼과 기기로 발전함에 따라 Braze를 사용한 메시징도 발전할 수 있습니다! Braze는 다양한 TV 운영 체제 및 OTT(Over-the-Top) 콘텐츠 전송 방법을 위한 다양한 참여 채널을 제공합니다.

## 플랫폼 및 기능

다음은 현재 지원되는 기능 및 메시징 채널 목록입니다.

<style>
#tv-feature-table td,
#tv-feature-table th {
    text-align: center !important;
    vertical-align: center;
}

</style>
<table id="tv-feature-table">
    <thead>
        <tr>
            <th>기기 유형</th>
            <th>데이터 및 분석</th>
            <th>인앱 메시지</th>
            <th>콘텐츠 카드</th>
            <th>푸시 알림</th>
            <th>캔버스</th>
            <th>피처 플래그</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Amazon Fire TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Kindle Fire</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Android TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>LG TV(webOS)</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push">N/A</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>삼성 Tizen TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push">N/A</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Roku</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-times text-warning"></i></td>
            <td for="push">N/A</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Apple TV OS</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
             <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fa-solid fa-minus"></i></td>  
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
       <tr>
          <td>Apple Vision Pro</td>
          <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
           <td for="iam"><i class="fas fa-check text-success"></i></td>
          <td for="content-cards"><i class="fas fa-check text-success"></i></td>
          <td for="push"><i class="fa-solid fa-minus"></i></td>  
          <td for="canvas"><i class="fas fa-check text-success"></i></td>
          <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
      </tr>
    </tbody>
</table>

- <i class="fas fa-check text-success"></i> = 지원됨
- <i class="fa-solid fa-minus"></i> = 부분 지원
- <i class="fas fa-times text-warning"></i> = Braze에서 지원되지 않음
- N/A = OTT 플랫폼에서 지원되지 않음

## 통합 가이드

### Amazon Fire TV {#fire-tv}

Braze Fire OS SDK를 사용하여 Amazon Fire TV 디바이스와 통합하세요.

다음과 같은 기능을 지원합니다.

- 크로스 채널 인게이지먼트를 위한 데이터 및 분석 수집
- 푸시 알림( ["헤드업 알림")](https://developer.amazon.com/docs/fire-tv/notifications.html#headsup)
  - 이러한 항목이 표시되려면 우선순위를 "높음"으로 설정해야 합니다. 모든 알림은 Fire TV 설정 메뉴에 표시됩니다.
- 콘텐츠 카드
- 피처 플래그
- 인앱 메시지
  - TV와 같은 비터치 환경에서 HTML 메시지를 표시하려면 `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` 을 `false` 으로 설정하세요( [Android SDK v23.1.0부터](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310) 사용 가능).

자세한 내용은 [Fire OS 통합 가이드를]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) 참조하세요.

### Kindle Fire {#kindle-fire}

Braze Fire OS SDK를 사용하여 Amazon Kindle Fire 디바이스와 통합하세요.

다음과 같은 기능을 지원합니다.

- 크로스 채널 인게이지먼트를 위한 데이터 및 분석 수집
- 푸시 알림
- 콘텐츠 카드
- 피처 플래그
- 인앱 메시지

자세한 내용은 [Fire OS 통합 가이드를]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) 참조하세요.

### Android TV {#android-tv}

Braze Android SDK를 사용하여 Android TV 디바이스와 통합할 수 있습니다.

다음과 같은 기능을 지원합니다.

- 크로스 채널 인게이지먼트를 위한 데이터 및 분석 수집
- 콘텐츠 카드
- 피처 플래그
- 인앱 메시지 
  - TV와 같은 비터치 환경에서 HTML 메시지를 표시하려면 `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` 을 `false` 으로 설정하세요( [Android SDK v23.1.0부터](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310) 사용 가능).
- \* 푸시 알림(수동 통합 필요)
  - Android TV에서는 기본적으로 푸시 알림이 지원되지 않습니다. 그 이유를 알아보려면 Google의 [디자인 가이드라인을](https://designguidelines.withgoogle.com/android-tv/patterns/notifications.html) 참조하세요. 그러나 **이를 위해 푸시 알림 UI를 수동으로 통합**할 수도 있습니다. 설정 방법에 대한 [설명서를]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android%20tv) 참조하세요.

자세한 내용은 [Android SDK 통합 가이드를]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) 참조하세요.

{% alert note %}
대시보드에서 Android OTT를 통합하려면 새 Android 앱을 생성해야 합니다.
{% endalert %}

### LG webOS {#lg-webos}

Braze 웹 SDK를 사용하여 [LG webOS TV와](https://webostv.developer.lge.com/discover) 통합하세요.

다음과 같은 기능을 지원합니다.

- 크로스 채널 인게이지먼트를 위한 데이터 및 분석 수집
- 콘텐츠 카드([헤드리스 UI](#custom-ui) 사용)
- 피처 플래그
- 인앱 메시지([헤드리스 UI](#custom-ui) 사용)

자세한 내용은 [웹 스마트 TV 통합 가이드를]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs/) 참조하세요.

### 삼성 Tizen {#tizen}

Braze 웹 SDK를 사용하여 [삼성 Tizen TV](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html)와 통합합니다.

다음과 같은 기능을 지원합니다.

- 크로스 채널 인게이지먼트를 위한 데이터 및 분석 수집
- 콘텐츠 카드([헤드리스 UI](#custom-ui) 사용)
- 피처 플래그
- 인앱 메시지([헤드리스 UI](#custom-ui) 사용)

자세한 내용은 [웹 스마트 TV 통합 가이드를]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs/) 참조하세요.

### Roku {#roku}

Braze Roku SDK를 사용하여 [Roku TV와](https://developer.roku.com/docs/developer-program/getting-started/roku-dev-prog.md) 통합할 수 있습니다.

다음과 같은 기능을 지원합니다.

- 크로스 채널 인게이지먼트를 위한 데이터 및 분석 수집
- 인앱 메시지([헤드리스 UI](#custom-ui) 사용)
  - 웹 보기는 Roku 플랫폼에서 지원되지 않으므로 HTML 인앱 메시지는 지원되지 않습니다.
- 피처 플래그

자세한 내용은 [Roku 통합 가이드를]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=roku) 참조하세요.

### Apple TV OS {#tvos}

Braze Swift SDK를 사용하여 tvOS와 통합하세요. Swift SDK에는 tvOS용 기본 UI나 보기가 포함되어 있지 않으므로 직접 구현해야 합니다.

다음과 같은 기능을 지원합니다.

- 크로스 채널 인게이지먼트를 위한 데이터 및 분석 수집
- 콘텐츠 카드([헤드리스 UI](#custom-ui) 사용)
- 피처 플래그
- 인앱 메시지([헤드리스 UI](#custom-ui) 사용)
  - 웹 보기는 tvOS 플랫폼에서 지원되지 않으므로 HTML 인앱 메시지는 지원되지 않습니다.
  - tvOS에서 맞춤형 메시징을 위해 헤드리스 UI를 사용하는 방법에 대해 자세히 알아보려면 [샘플 앱을](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui) 참조하세요.
- 무음 푸시 알림 및 업데이트 배지

자세한 내용은 [iOS Swift SDK 통합 가이드를](https://github.com/braze-inc/braze-swift-sdk) 참조하세요.

{% alert note %}
TV 사용자에게 모바일 인앱 메시지를 표시하지 않으려면 [앱 타겟팅](#app-targeting)을 설정하거나 키-값 페어를 사용하여 메시지를 필터링합니다. 예를 들어, 특별한 `tv = true` 키-값 페어가 포함된 경우에만 tvOS 메시지를 표시합니다.
{% endalert %}

### Apple Vision Pro {#vision-pro}

Braze Swift SDK를 사용하여 비전OS와 통합하세요. iOS에서 사용할 수 있는 대부분의 기능은 visonOS에서도 사용할 수 있습니다.

- 애널리틱스(세션, 사용자 지정 이벤트, 구매 등)
- 인앱 메시징(데이터 모델 및 UI)
- 콘텐츠 카드(데이터 모델 및 UI)
- 푸시 알림(사용자가 볼 수 있는 동작 버튼 및 무음 알림)
- 피처 플래그
- 위치 분석

자세한 내용은 [iOS Swift SDK 통합 가이드를](https://github.com/braze-inc/braze-swift-sdk) 참조하세요.

{% alert important %}
일부 iOS 기능은 부분적으로 지원되거나 지원되지 않습니다. 전체 목록은 [visionOS 지원](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/visionos)을 참조하세요.
{% endalert %}

## 앱 타겟팅 {#app-targeting}

메시징을 위해 OTT 앱을 타겟팅하려면 OTT 앱 전용 세그먼트를 생성하는 것이 좋습니다.

![Android OTT 앱을 사용하여 만든 세그먼트.]({% image_buster /assets/img/android_ott.png %})

## 헤드리스 UI {#custom-ui}

{% alert important %}
헤드리스 UI를 통해 인앱 메시지 또는 콘텐츠 카드를 지원하는 플랫폼에는 기본 UI 또는 보기가 포함되어 있지 **않으므로** 커스텀 UI를 직접 구현해야 합니다.
{% endalert %}

헤드리스 UI를 사용하면 Braze는 앱이 제어하는 UI 내에서 앱이 읽고 사용할 수 있는 JSON과 같은 데이터 모델을 제공합니다. 이 데이터에는 대시보드에 구성된 필드(제목, 본문, 버튼 텍스트, 색상 등)가 포함되며, 앱이 이를 읽고 적절히 표시할 수 있습니다. 커스텀 처리 메시징에 대한 자세한 내용은 다음을 참조하세요.

**Android SDK**
- [인앱 메시지 사용자 지정]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners)
- [콘텐츠 카드 사용자 지정]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style/)

**Swift SDK**
- [인앱 메시지 사용자 지정](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/)
- [헤드리스 UI 샘플 앱](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui)
- [콘텐츠 카드 사용자 지정](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/)

**웹 SDK**
- [인앱 메시지 사용자 지정]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web)
- [콘텐츠 카드 사용자 지정]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style/)

