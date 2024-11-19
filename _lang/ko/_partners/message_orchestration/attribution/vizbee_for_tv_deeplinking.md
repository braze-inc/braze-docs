---
nav_title: Vizbee
article_title: TV 딥링킹을 위한 Vizbee
alias: /partners/vizbee_for_tv_deeplinking/
page_type: partner
description: "이 참조 문서에서는 Braze와 Vizbee 간의 파트너십과 TV 딥링킹을 지원하기 위해 이를 사용하는 방법을 설명합니다."
search_tag: Partner

---
# Vizbee {#vizbee}

> [Vizbee][1]는 모든 스마트폰과 스마트 TV가 하나의 원활한 기기로 함께 작동하여 훌륭한 사용자 경험을 제공합니다. Vizbee는 알림, 딥링크 및 이메일과 같은 기존 모바일 앱 마케팅 채널을 활용하여 모든 연결된 TV(CTV) 장치(예: Roku, FireTV, Samsung TV, LG TV 등)에서 시청자를 원활하게 확보하고 참여할 수 있도록 도와줍니다.

Braze와 Vizbee 통합을 통해 단일 콘솔을 사용하여 모바일 및 CTV 기기에서 스트리밍 앱의 시청자를 확보하고 유지하기 위한 마케팅 캠페인을 예약할 수 있습니다. 이 통합을 통해 다음을 수행할 수 있습니다.
- 타겟 사용자에게 보낼 모바일 알림을 예약합니다. 탭하면 모바일 앱 시청률이 증가하거나 근처 스트리밍 기기 또는 TV에서 원활하게 재생할 수 있습니다.
- 타겟 사용자에게 이메일 마케팅 캠페인을 예약하면 탭 한 번으로 자동 CTV 앱 설치 및 Roku 또는 FireTV와 같은 CTV 기기에서 사용자의 로그인까지 가능합니다.

## 필수 조건

| 요구 사항 | 설명 |
|---|---|
| Vizbee 계정 | 이 파트너십을 활용하려면 [Vizbee][1] 계정이 필요합니다. Vizbee에 앱을 등록하고 할당된 Vizbee ID를 가져야 합니다. |
| iOS 또는 Android 앱 | 이 통합은 iOS 및 Android 앱을 지원합니다. 플랫폼에 따라 애플리케이션에 코드 스니펫이 필요할 수 있습니다. |
| Vizbee SDK | 필수 Braze SDK 외에도 Vizbee SDK를 설치해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

Vizbee의 [SDK 통합 가이드][2]를 따라 Vizbee 및 Braze 통합을 시작 및 실행합니다. 여기에서 모바일 대 TV로의 딥링킹, TV 앱 설치 및 시청 기여도에 대한 지침을 확인할 수 있습니다. 

### 설치 및 기여도 보고서 보기 {#vizbee-tv-app-installs-viewership-attribution}

또한 Vizbee와 Braze는 모바일 및 CTV 기기 전반에 걸쳐 캠페인의 전체적인 성능을 볼 수 있습니다. Vizbee SDK는 커스텀 이벤트를 Braze SDK로 전송하며, Braze 대시보드의 캠페인 보고서에서 확인할 수 있습니다.

[1]: https://vizbee.tv/
[2]: https://console.vizbee.tv/app/vzb1765003429/develop/guides/ios-continuity
