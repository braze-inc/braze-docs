---
nav_title: Gimbal
article_title: Gimbal
alias: /partners/gimbal/
description: "이 참조 문서에서는 위치 데이터를 사용하여 마케팅 관련성을 완벽한 수준으로 높일 수 있는 Braze와 Gimbal의 파트너십에 대해 간략히 설명합니다."
page_type: partner
search_tag: Partner

---

# Gimbal

> [Gimbal](https://gimbal.com/)을 통해 위치 데이터를 사용하여 마케팅 관련성을 완벽한 수준으로 높일 수 있습니다. 지오펜싱 소프트웨어 및 비콘과 결합된 위치 SDK는 관련성 높은 개인화된 근접 인식 모바일 경험을 제공합니다.

비콘 또는 지오펜스 지원과 Braze의 타겟팅 및 메시징 기능을 결합하여 사용자의 신체적 행동에 대해 자세히 알아보고 그에 맞는 메시지를 전달하세요. 이 파트너십 통합을 통해 다양한 사용 사례가 열립니다:

- **마케팅:** 상황에 맞는 메시지를 전송하고 경험적인 소비자 여정을 구축하세요.
- **경쟁사 분석:** 경쟁 위치 주변에 트리거를 설정하여 소비자 트렌드와 패턴을 파악합니다.
- **오디언스 인사이트:** 사용자의 방문 행동을 파악하고 이러한 학습을 기반으로 추가로 세분화합니다.

{% alert note %}
이 통합은 짐벌 비콘과 짐벌 지오펜스 솔루션에서도 동일하게 작동합니다.
{% endalert %}

## 전제 조건

| 요구 사항| 설명|
| ---| ---|
| [짐벌 관리자 계정][1] | 이 파트너십을 이용하려면 Gimbal 매니저 계정이 필요합니다. |
|[짐벌 위치 SDK](https://docs.gimbal.com/index.html) | Gimbal 위치 SDK는 근접 비콘과 지오펜스를 사용하여 매크로 및 마이크로 위치 기반 모바일 경험을 강화함으로써 앱 사용자와 보다 효과적으로 소통할 수 있도록 지원합니다. SDK를 구현하고 지오펜스 또는 비콘을 설정해야 합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## SDK 통합

Braze와 Gimbal을 통합하려면 Gimbal 위치 SDK를 구현하고 Gimbal 매니저 계정을 생성해야 합니다. Android, FireOS 및 iOS용 다음 통합은 사용자가 새로 들어오는 각 장소에 대해 고유한 사용자 지정 이벤트를 생성하며, 이러한 이벤트는 캠페인 및 캔버스에서 트리거 및 리타겟팅에 사용할 수 있습니다.

50개 이상의 장소를 생성할 예정이라면 일반 `Places Entered` 사용자 지정 이벤트를 만들고 장소 이름을 이벤트 속성으로 추가하는 것이 좋습니다. 

1. [Gimbal 설명서][3]의 지침에 따라 Android 및 iOS용 [Gimbal SDK][2]를 앱에 통합합니다.
2. Gimbal의 [위치 REST API][4]를 사용하여 사용자 `places` 를 가져옵니다.
3. Braze [REST API 키][5]를 입력하여 Gimbal 계정을 Braze에 연결합니다.
4. Braze SDK에서 [사용자 지정 이벤트를][6] 설정하세요. [Android 및 FireOS][7], [iOS][8]에서 Braze와 Gimbal을 통합할 수 있습니다.
5. 이러한 이벤트에 대한 로그 속성(장소 이름, 체류 시간)을 기록합니다.
6. 이러한 속성과 이벤트를 사용하여 Braze에서 캠페인과 캔버스를 트리거할 수 있습니다. 

[1]: https://manager.gimbal.com/login/users/sign_in
[2]: https://manager.gimbal.com/sdk_downloads
[3]: https://docs.gimbal.com/
[4]: https://docs.gimbal.com/rest.html
[5]: https://manager.gimbal.com/apps
[6]: {{site.baseurl}}/user_guide/data_and_analytics/Custom_Data/custom_events/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#gimbal-beacons
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/#gimbal-beacons