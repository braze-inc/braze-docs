---
nav_title: iOS 14 업그레이드 가이드
article_title: iOS 14 SDK 업그레이드 가이드
page_order: 7
platform: iOS
description: "이 참조 문서에서는 지오펜스, 위치 타겟팅, IDFA 등의 변경 사항을 중심으로 iOS 14 SDK 업데이트를 다룹니다."
hidden: true
noindex: true
---

# iOS 14 SDK 업그레이드 가이드

> 이 가이드는 iOS 14에서 도입된 Braze 관련 변경 사항과 Braze iOS SDK 통합을 위한 필수 업그레이드 단계를 설명합니다. 새로운 iOS 14 업데이트의 전체 목록은 Apple의 [iOS 14 페이지](https://www.apple.com/ios/ios-14/)를 참조하세요.

{% alert tip %}
iOS 14.5부터 **IDFA** 수집 및 [특정 데이터 공유](https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track)에는 새로운 [AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency) 프레임워크 권한 프롬프트가 필요합니다[(자세히 알아보기)](#idfa).
{% endalert %}

#### iOS 14 주요 변경 사항 요약

- iOS 14/Xcode 12를 대상으로 하는 앱은 [공식 iOS 14 릴리스](https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.27.0)를 사용해야 합니다.
- 새로운 _대략적인 위치_ 권한을 선택한 사용자에 대해 지오펜스는 [더 이상 iOS에서 지원되지 않습니다](https://developer.apple.com/documentation/corelocation/cllocationmanager/3600215-accuracyauthorization).
- '마지막으로 알려진 위치' 타겟팅 기능을 사용하려면 _대략적인 위치_ 권한과의 호환성을 위해 Braze iOS SDK v3.26.1 이상으로 업그레이드해야 합니다. Xcode 12를 사용하는 경우 v3.27.0 이상으로 업그레이드해야 합니다.
- iOS 14.5부터 IDFA 수집 및 [특정 데이터 공유](https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track)에는 새로운 [AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency) 프레임워크 권한 프롬프트가 필요합니다.
- 캠페인 타겟팅 또는 분석에 대한 '광고 추적 활성화됨' 필드를 사용하는 경우, 사용자의 옵트인 상태를 보고하려면 Xcode 12로 업그레이드하고 새로운 AppTrackingTransparency 프레임워크를 사용해야 합니다.

## 업그레이드 요약

<style>
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2) {
    min-width:230px;
}
table td {
    word-break: break-word;
}
</style>

|앱에서 사용하는 항목:|업그레이드 권장 사항|설명|
|------|--------|---|
|Xcode 12|**iOS SDK v3.27 이상으로 업그레이드하기**|Xcode 12를 사용하는 고객은 호환성을 위해 v3.27.0 이상을 사용해야 합니다. iOS 14 호환성과 관련된 문제나 질문이 있는 경우 새 [GitHub 이슈](https://github.com/Appboy/appboy-ios-sdk/issues)를 개설하세요.|
|가장 최근 위치| **iOS SDK v3.26.1 이상으로 업그레이드하기**|최근 위치 타겟팅 기능을 사용하고 Xcode 11을 계속 사용하는 경우 새로운 _대략적인 위치_ 기능을 지원하는 iOS SDK v3.26.1 이상으로 업그레이드해야 합니다. 사용자가 iOS 14로 업그레이드하고 _또한_ 대략적인 위치를 선택하면 이전 SDK는 위치를 안정적으로 수집할 수 없습니다.<br><br>앱이 iOS 14를 대상으로 하지 않더라도 사용자가 iOS 14로 업그레이드하면 새로운 위치 정확도 옵션을 사용할 수 있습니다. iOS SDK v3.26.1 이상으로 업그레이드하지 않은 앱은 사용자가 iOS 14 기기에서 _대략적인 위치_를 제공할 때 위치 속성을 안정적으로 수집할 수 없습니다.|
|IDFA 광고 추적 ID| **Xcode 12 및 iOS SDK v3.27로 업그레이드해야 할 수 있음**|2021년에 Apple은 IDFA 수집을 위해 권한 프롬프트를 요구하기 시작했습니다. 이때 IDFA를 계속 수집하려면 앱을 Xcode 12로 업그레이드하고 새로운 `AppTrackingTransparency` 프레임워크를 사용해야 했습니다. IDFA를 Braze SDK에 전달하는 경우에도 v3.27.0 이상으로 업그레이드해야 합니다.<br><br>새로운 iOS 14 API를 사용하지 않는 앱은 2021년 Apple이 이 변경 사항을 시행하기 시작하면서 IDFA를 수집할 수 없으며 대신 빈 ID(`00000000-0000-0000-0000-000000000000`)를 수집하게 됩니다. 앱에 이 변경 사항이 적용되는지 여부에 대한 자세한 내용은 [IDFA 세부 정보](#idfa)를 참조하세요.|


## iOS 14 동작 변경 사항

### 대략적인 위치 권한

![정확한 위치]({% image_buster /assets/img/ios/ios14-approximate-location.png %}){: style="float:right;max-width:45%;margin-left:15px;"}

#### 개요

위치 권한을 요청할 때 사용자는 _정확한 위치_(이전 동작)를 제공하거나 새로운 _대략적인 위치_를 제공할 수 있습니다. 대략적인 위치는 정확한 좌표 대신 사용자가 위치한 더 큰 반경을 반환합니다.

#### 지오펜스 {#geofences}

새로운 _대략적인 위치_ 권한을 선택한 사용자에 대해 지오펜스는 [더 이상 iOS에서 지원되지 않습니다](https://developer.apple.com/documentation/corelocation/cllocationmanager/3600215-accuracyauthorization). Braze SDK 연동에는 업데이트가 필요하지 않지만, 지오펜스를 사용하는 캠페인의 경우 [위치 기반 마케팅 전략을](https://www.braze.com/blog/geofencing-geo-targeting-beaconing-when-to-use/) 조정해야 할 수 있습니다.

#### 위치 타겟팅 {#location-tracking}

_대략적인 위치_가 제공된 상태에서 사용자의 _마지막 알려진 위치_를 계속 수집하려면 앱을 Braze iOS SDK v3.26.1 이상으로 업그레이드해야 합니다. 위치는 정확도가 떨어질 수 있으며, 테스트 결과 12,000미터(7마일 이상) 이상에서 측정되었다는 점에 유의하세요. Braze 대시보드에서 _마지막으로 알려진 위치_ 타겟팅 옵션을 사용할 때는 새로운 _대략적인 위치를_ 고려할 수 있도록 위치의 반경을 늘려야 합니다(반경 1마일/1.6km 이상을 권장합니다).

Braze iOS SDK를 v3.26.1 이상으로 업그레이드하지 않은 앱은 iOS 14 기기에서 _대략적인 위치_가 제공될 때 더 이상 위치 추적을 사용할 수 없습니다.

이미 위치 액세스 권한을 부여한 사용자는 업그레이드 후에도 계속해서 _정확한 위치를_ 제공할 수 있습니다.

Xcode 12를 사용하는 경우 v3.27.0 이상으로 업그레이드해야 합니다.

대략적인 위치에 대한 자세한 내용은 Apple의 [새로운 위치](https://developer.apple.com/videos/play/wwdc2020/10660/) 기능 WWDC 비디오를 참조하세요.

### IDFA 및 앱 추적 투명성 {#idfa}

#### 개요

IDFA(광고주 식별자)는 광고 및 어트리뷰션 파트너가 교차 기기 추적을 위해 사용할 수 있도록 Apple에서 제공하는 식별자로, 개인의 Apple ID에 연결됩니다.

iOS 14.5부터 IDFA에 대한 명시적인 사용자 동의를 수집하기 위해 새로운 권한 프롬프트(새로운 `AppTrackingTransparency` 프레임워크에서 실행됨)가 표시되어야 합니다. '다른 회사가 소유한 앱과 웹사이트에서 사용자를 추적'하기 위한 이 권한 프롬프트는 사용자에게 위치를 요청하는 것과 유사한 방식으로 요청됩니다.

사용자가 프롬프트에 동의하지 않거나 Xcode 12의 `AppTrackingTransparency` 프레임워크로 업그레이드하지 않으면 빈 IDFA 값(`00000000-0000-0000-0000-000000000000`)이 반환되고 앱은 사용자에게 다시 메시지를 표시할 수 없습니다.

{% alert important %}
이러한 IDFA 업데이트는 최종사용자가 기기를 iOS 14.5로 업그레이드한 후에 적용됩니다. IDFA를 수집하려는 경우 앱이 Xcode 12에서 새로운 `AppTransparencyFramework`를 사용해야 합니다.
{% endalert %}

#### Braze IDFA 컬렉션 변경 사항
![IDFA]({% image_buster /assets/img/ios/ios14-idfa.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

1. Braze를 통해 앱은 계속해서 사용자의 IDFA 값을 Braze SDK_에_ 제공할 수 있습니다.

2. 선택적 자동 IDFA 수집에서 조건부로 컴파일되는 `ABK_ENABLE_IDFA_COLLECTION` 컴파일 매크로는 iOS 14에서 더 이상 작동하지 않으며 3.27.0에서 제거되었습니다. 

3. 캠페인 타겟팅 또는 분석에 대한 '광고 추적 활성화됨' 필드를 사용하는 경우, 사용자의 옵트인 상태를 보고하려면 Xcode 12로 업그레이드하고 새로운 AppTrackingTransparency 프레임워크를 사용해야 합니다. 이러한 변경의 이유는 iOS 14에서 이전 [`advertisingTrackingEnabled`](https://developer.apple.com/documentation/adsupport/asidentifiermanager/1614148-advertisingtrackingenabled) 필드가 항상 아니요를 반환하기 때문입니다.

4. 앱에서 IDFA 또는 IDFV를 Braze 외부 ID로 사용했다면 이러한 식별자 대신 UUID로 마이그레이션할 것을 적극 권장합니다. 외부 ID 마이그레이션에 대한 자세한 내용은 [외부 ID 마이그레이션 API 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/)를 참조하세요.

Apple의 [개인정보 보호 업데이트](https://developer.apple.com/app-store/user-privacy-and-data-use/) 및 새로운 [앱 추적 투명성 프레임워크](https://developer.apple.com/documentation/apptrackingtransparency)에 대해 자세히 알아보세요.

### 푸시 권한 부여 {#push-provisional-auth}

{% alert important %}
iOS 14에는 임시 푸시 권한 부여에 대한 변경 사항이 포함되어 있지 않습니다. iOS 14의 이전 베타 버전에서 Apple은 변경 사항을 도입했지만 이후에 이전 동작으로 되돌렸습니다.
{% endalert %}

## iOS 14의 새로운 기능

### 앱 개인정보 보호 및 데이터 수집 개요 {#app-privacy}

2020년 12월 8일부터 App Store에 제출하는 모든 앱은 [Apple의 새로운 앱 개인정보 보호 표준](https://developer.apple.com/app-store/app-privacy-details/)을 준수하기 위해 추가 단계를 거쳐야 합니다.

#### Apple 개발자 포털 설문지

_Apple 개발자 포털에서_:
* 앱 또는 서드파티 파트너가 데이터를 수집하는 방법을 설명하기 위해 설문지를 작성하라는 메시지가 표시됩니다.
  * 설문지는 항상 App Store의 최근 릴리스에 따라 최신 상태로 유지됩니다.
  * 설문지는 새로운 앱을 제출하지 않아도 업데이트될 수 있습니다.
* 앱의 개인정보처리방침 URL 링크를 붙여넣어야 합니다.

설문지를 작성할 때 법무팀에 문의하여 다음 항목에 대한 Braze의 사용이 공개 요건에 어떤 영향을 미칠 수 있는지 고려하세요.

#### Braze 기본 데이터 수집
**식별자** \- 익명의 기기 식별자는 항상 Braze SDK에 의해 수집됩니다. 현재 기기 IDFV(제공업체 식별자)로 설정되어 있습니다.

**사용 데이터** \- 여기에는 제품 상호작용을 측정하는 데 사용하는 이벤트 또는 속성 컬렉션뿐만 아니라 Braze 세션 데이터도 포함될 수 있습니다.

#### 선택적 데이터 수집
Braze 사용을 통해 선택적으로 수집할 수 있는 데이터:

**위치** \- 대략적인 위치와 정확한 위치는 모두 Braze SDK에서 선택적으로 수집할 수 있습니다. 이러한 기능은 기본적으로 비활성화되어 있습니다.

**연락처 정보** \- 여기에는 사용자의 신원과 관련된 이벤트 및 속성이 포함될 수 있습니다.

**구매** \- 여기에는 사용자를 대신하여 기록된 이벤트 및 구매가 포함될 수 있습니다.

{% alert important %}
이 목록은 전체 목록이 아닙니다. 앱 개인정보 보호 설문지의 다른 카테고리에 해당하는 사용자에 대한 다른 정보를 Braze에서 수동으로 수집하는 경우, 해당 정보도 공개해야 합니다.
{% endalert %}

이 기능에 대해 자세히 알아보려면 [Apple의 개인정보 보호 및 데이터 사용](https://developer.apple.com/app-store/user-privacy-and-data-use/)을 참조하세요.

