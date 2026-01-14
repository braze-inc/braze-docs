---
nav_title: Infillion
article_title: Infillion
alias: /partners/infillion/
description: "This reference article outlines the partnership between Braze and Infillion, which enables you to perfect your marketing relevance using location data."
page_type: partner
search_tag: Partner

---

# Infillion

> [Infillion](https://infillion.com/) enables you to perfect your marketing relevance using location data. 지오펜싱 소프트웨어 및 비콘과 결합된 위치 SDK는 관련성 높은 개인화된 근접 인식 모바일 경험을 제공합니다.

Combine your beacon or geofence support with Braze targeting and messaging features to learn more about your user's physical actions and message them accordingly. 이 파트너십 통합을 통해 다양한 사용 사례가 열립니다:

- **마케팅:** 상황에 맞는 메시지를 전송하고 경험적인 소비자 여정을 구축하세요.
- **경쟁사 분석:** 경쟁 위치 주변에 트리거를 설정하여 소비자 트렌드와 패턴을 파악합니다.
- **오디언스 인사이트:** 사용자의 방문 행동을 파악하고 이러한 학습을 기반으로 추가로 세분화합니다.

{% alert note %}
This integration works the same for Infillion beacons and Infillion geofence solutions.
{% endalert %}

## 전제 조건

| 요구 사항| 설명|
| ---| ---|
| [Infillion manager account](https://manager.gimbal.com/login/users/sign_in) | A Infillion manager account is required to take advantage of this partnership. |
|[Infillion Location SDK](https://docs.gimbal.com/index.html) | The Infillion Location SDK powers macro and micro location-based mobile experiences using proximity beacons and geofences that allow you to communicate more effectively with your app users. SDK를 구현하고 지오펜스 또는 비콘을 설정해야 합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## SDK 통합

To integrate Braze and Infillion, you must implement the Infillion Location SDK and create a Infillion manager account. Android, FireOS 및 iOS용 다음 통합은 사용자가 새로 들어오는 각 장소에 대해 고유한 사용자 지정 이벤트를 생성하며, 이러한 이벤트는 캠페인 및 캔버스에서 트리거 및 리타겟팅에 사용할 수 있습니다.

50개 이상의 장소를 생성할 예정이라면 일반 `Places Entered` 사용자 지정 이벤트를 만들고 장소 이름을 이벤트 속성으로 추가하는 것이 좋습니다. 

1. Integrate the [Infillion SDK](https://manager.gimbal.com/sdk_downloads) for Android and iOS into your app by following the instructions in the [Infillion documentation](https://docs.gimbal.com/).
2. Use Infillion's [place REST API](https://docs.gimbal.com/rest.html) to get user `places`.
3. Link your Infillion account to Braze by entering the Braze [REST API key](https://manager.gimbal.com/apps).
4. Set up [custom events]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) in the Braze SDK. You can integrate Infillion with Braze for [Android and FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#gimbal-beacons) and [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/#gimbal-beacons).
5. 이러한 이벤트에 대한 로그 속성(장소 이름, 체류 시간)을 기록합니다.
6. 이러한 속성과 이벤트를 사용하여 Braze에서 캠페인과 캔버스를 트리거할 수 있습니다. 

