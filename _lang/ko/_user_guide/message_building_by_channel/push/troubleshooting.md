---
nav_title: 문제 해결
article_title: 푸시 문제 해결
page_order: 23
page_type: reference
description: "이 페이지에는 푸시 메시징 채널과 관련된 다양한 문제에 대한 문제 해결 단계가 포함되어 있습니다."
channel: push
---

# 푸시 문제 해결

> 이 페이지에서는 푸시 메시징 채널에서 발생할 수 있는 다양한 문제를 해결하는 데 도움이 됩니다.

## 누락된 푸시 알림

푸시 알림으로 인해 전달 문제가 발생하고 있나요? 이 문제를 해결하기 위해 취할 수 있는 여러 단계가 있습니다:

- [푸시 구독 상태](#push-subscription-status)
- [세그먼트](#segment)
- [푸시 알림 캡](#push-notification-caps)
- [요금 제한](#rate-limits)
- [대조군 상태](#control-group-status)
- [유효한 푸시 토큰](#valid-push-token)
- [푸시 알림 유형](#push-notification-type)
- [현재 앱](#current-app)

#### 푸시 구독 상태

푸시는 가입하거나 옵트인한 사용자에게만 보낼 수 있습니다. **사용자 프로필** 섹션의 [참여]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) 탭에서 고객 프로필을 확인하여 테스트 중인 워크스페이스에 푸시 등록이 되어 있는지 확인하세요. 여러 앱에 등록되어 있는 경우 **푸시 등록 대상** 필드에 해당 앱이 나열됩니다:

푸시 등록하기]({% image_buster /assets/img_archive/trouble1.png %})

Braze 내보내기 엔드포인트를 사용하여 고객 프로필을 내보낼 수도 있습니다:
- [식별자별 사용자]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [세그먼트별 사용자 수]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

두 엔드포인트 모두 기기별 푸시 인에이블먼트 정보가 포함된 푸시 토큰 객체를 반환합니다.

#### 세그먼트

타겟팅하는 세그먼트에 속하는지 확인하세요(테스트가 아닌 라이브 캠페인인 경우). **고객 프로필에는** 현재 사용자가 속한 세그먼트 목록이 표시됩니다. 세그먼트는 실시간으로 업데이트되므로 계속 변화하는 변수라는 점을 기억하세요.

\![세그먼트 목록]({% image_buster /assets/img_archive/trouble2.png %})

세그먼트를 만들 때 사용자 **조회를** 사용하여 사용자가 세그먼트의 일부인지 확인할 수도 있습니다.

검색 필드가 있는 사용자 조회 섹션.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### 푸시 알림 캡

글로벌 최대 게재빈도 설정을 확인합니다. 워크스페이스에 글로벌 최대 게재빈도 제한이 설정되어 있고 지정된 기간 동안 푸시 알림 한도에 이미 도달했기 때문에 푸시 알림을 받지 못했을 수 있습니다.

대시보드에서 [글로벌 최대 게재빈도]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over) 설정을 확인하면 됩니다. 캠페인이 최대 게재빈도 제한 규칙을 준수하도록 설정된 경우 다음 설정의 영향을 받는 사용자가 다수 있습니다.

\![캠페인 세부 정보]({% image_buster /assets/img_archive/trouble3.png %})

#### 요금 제한

캠페인 또는 캔버스에 속도 제한이 설정되어 있는 경우 이 제한을 초과하여 메시징 수신을 받지 못할 수 있습니다. 자세한 내용은 [요금 제한을]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting) 참조하세요.

#### 대조군 상태

단일 채널 캠페인이거나 대조군이 있는 캔버스인 경우 대조군에 속할 가능성이 있습니다.

  1. [배리언트 분포를]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants) 확인하여 대조군이 있는지 확인합니다.
  2. 그렇다면 [캠페인 대조군에서]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter) 세그먼트 필터링을 생성한 다음 [세그먼트를 내보내고]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv) 사용자 ID가 이 목록에 있는지 확인합니다.

#### 유효한 푸시 토큰
푸시 토큰은 발신자가 푸시 알림을 통해 특정 기기를 타겟팅할 때 사용하는 식별자입니다. 따라서 기기에 유효한 푸시 토큰이 없는 경우 푸시 알림을 보낼 방법이 없습니다. 

#### 푸시 알림 유형

올바른 유형의 푸시 알림을 사용하고 있는지 확인하세요. 예를 들어, FireTV를 타겟팅하려는 경우 Android 푸시 캠페인이 아닌 Kindle 푸시 알림을 사용해야 합니다. 마찬가지로 Android를 타겟팅하려면 iOS 푸시 캠페인이 아닌 Android 푸시 알림을 사용하세요. Braze 워크플로우를 이해하는 방법에 대한 자세한 내용은 다음 문서를 참조하세요:
- [Apple 푸시 알림]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [파이어베이스 클라우드 메시징]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

#### 현재 앱

내부 사용자를 대상으로 푸시 전송을 테스트할 때는 푸시 알림을 받으려는 사용자가 현재 해당 앱에 로그인되어 있는지 확인하세요. 이로 인해 사용자가 푸시를 받지 못하거나 세그먼트가 세분화되지 않은 푸시를 받게 될 수 있습니다.

## 푸시 클릭이 앱에서 예기치 않게 열림

푸시 알림의 링크가 웹 브라우저가 아닌 앱에서 예기치 않게 열리는 문제가 발생하는 경우 캠페인 구성 또는 SDK 구현에 문제가 있는 것일 수 있습니다. 도움이 필요하면 다음 단계를 참조하세요.

### 클릭 동작 확인

캠페인 또는 캔버스 단계에서 **모바일 앱 내에서 웹 URL 열기가** 선택되어 있지 않은지 다시 확인합니다. 그렇다면 선택을 취소하고 다시 실행하세요. 

푸시 구성의 '클릭 시 동작' 필드에서 '모바일 앱 내에서 웹 URL 열기'가 선택 해제된 상태에서 '웹 URL 열기'로 설정되어 있습니다.]({% image_buster /assets/img/push_on_click.png %})

클릭 시 동작 '웹 URL 열기'의 기본값 상호 작용은 소프트웨어 개발 키트 버전에 따라 다릅니다. 소프트웨어 개발 키트 버전 iOS 2.29.0 및 Android 2.0.0 이상의 경우 이 옵션이 기본값으로 선택되어 있으며 웹 URL이 앱 내의 웹 보기에서 열립니다. 이 버전 이전에는 이 옵션이 기본적으로 선택 해제되어 있으며 기기의 기본값 웹 브라우저에서 웹 URL이 열립니다.

이 문제가 아니라면 푸시 구현에 문제가 있는 것일 수 있습니다. 

### 푸시 통합 다시 확인

푸시 알림의 링크가 앱에서 예기치 않게 열리는 경우 푸시 알림 통합 또는 커스텀 설정에 문제가 있기 때문일 수 있습니다. 다음 단계에 따라 문제를 해결하세요:

1. **푸시 위임자 구현을 검토합니다:** Braze 푸시 델리게이트가 올바르게 구현되었는지 확인합니다. 자세한 지침은 사용 중인 [플랫폼의]({{site.baseurl}}/developer_guide/home/) 푸시 알림 통합 가이드를 참조하세요.
2. **커스텀 링크 처리를 검사합니다:** 앱에 모든 `https://` 링크에 대한 커스텀 처리가 포함되어 있는지 확인하세요. 커스텀 구성이 기본값보다 우선할 수 있습니다. 필요한 경우 개발자 팀과 협력하여 이러한 설정을 검토하고 조정하세요.
3. **iOS 푸시 등록을 확인합니다:** iOS의 경우 푸시 통합 가이드의 푸시 [알림 등록하기]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns) 1단계를 참조하여 [APN에 푸시 알림을 등록하세요]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns). 앱 실행이 완료되기 전에 델리게이트 개체가 동기적으로 할당되었는지 확인하세요. 이 단계는 `application:didFinishLaunchingWithOptions:` 방법으로 완료해야 합니다.
4. **통합을 테스트하세요:** 조정을 마친 후 iOS 및 Android 기기에서 푸시 알림 동작을 테스트하여 문제가 해결되었는지 확인합니다.

## 웹 푸시 알림이 예상대로 작동하지 않습니다.

브라우저에서 푸시 알림에 문제가 발생하는 경우 사이트의 알림 권한을 재설정하고 사이트의 저장소를 지워야 할 수 있습니다. 도움이 필요하면 다음 단계를 참조하세요.

{% tabs %}
{% tab Chrome %}

### 데스크톱에서 Chrome 재설정

1. Chrome 브라우저에서 URL 옆에 있는 **사이트 정보 보기** 슬라이더 아이콘을 선택합니다.
2. **알림에서** **권한 재설정을** 선택합니다.
3. Chrome 개발자 도구를 엽니다. 다음은 운영 체제별 관련 단축키입니다.

<style> 
table {
    max-width: 50%;
}
</style>

| OS      | 키보드 단축키                                                  |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="4"}
4\. 개발 도구에서 **애플리케이션** 탭으로 이동합니다.
5\. 사이드바에서 **저장소를** 선택합니다.
6\. **사이트 데이터 지우기를** 선택합니다.
7\. Chrome에서 페이지를 새로고침하여 업데이트된 설정을 적용하라는 메시지가 표시됩니다. **다시 로드를** 선택합니다.

이제 푸시 권한이 재설정되었습니다. 사이트에 새 탭을 열고 사용해 보세요.

### Android에서 Chrome 초기화하기

Android 알림 서랍에 사이트의 알림이 표시되는 경우:

1. 푸시 알림에서 다음을 탭합니다. <i class="fas fa-cog" title="설정"></i> 을 탭하고 **사이트 설정을** 선택합니다.
2. **사이트 설정에서** **지우기 & 재설정을** 탭합니다.

사이트가 열려 있지 않은 경우 알림을 받지 못합니다:

1. Android에서 Chrome을 엽니다.
2. <i class="fas fa-ellipsis-vertical"></i> 메뉴를 탭합니다.
3. **설정** > **사이트 설정** > **알림으로** 이동합니다.
4. 알림 확인을 **보내기 전에 묻기(권장)**로 설정합니다.
5. 목록에서 사이트를 찾아보세요.
6. 항목을 선택하고 **지우기 및 재설정을** 탭합니다.

이제 푸시 권한이 재설정되었습니다. 사이트에 새 탭을 열고 사용해 보세요.

{% endtab %}
{% tab Firefox %}

### 데스크톱에서 Firefox 재설정

1. 사이트 URL 옆에 있는 <i class="fa-solid fa-circle-info" alt="info icon"></i> 또는 <i class="fas fa-lock" alt="lock icon"></i> 을 선택합니다.
2. **권한의** **알림 받기** 옆에서 다음을 선택합니다. <i class="fa-solid fa-circle-xmark" title="이 권한 지우기를 선택한 후 다시 요청"></i> 를 클릭하여 알림 권한을 지웁니다.
3. 같은 메뉴에서 **쿠키 및 사이트 데이터 지우기를** 선택합니다.
4. 선택을 확인하는 대화 상자에서 **확인을** 선택합니다.

이제 푸시 권한이 재설정되었습니다. 사이트에 새 탭을 열고 사용해 보세요.

### Android에서 Firefox 재설정하기

Android에서 푸시 권한을 재설정하려면 이 [Mozilla 지원 문서를](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser) 참조하세요.

{% endtab %}
{% tab Safari %}

### MacOS에서 Safari 재설정하기

{% alert note %}
이 단계는 MacOS에만 해당되며, Apple은 Windows의 Safari용 웹 푸시를 지원하지 않습니다.
{% endalert %}

1. Safari를 엽니다.
2. [Mac의 메뉴 모음에서](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac) **Safari** > **설정** > **웹 사이트** > **알림으로** 이동합니다.
3. 목록에서 사이트를 선택합니다.
4. **제거를** 선택하여 사이트에 대한 알림 권한을 삭제합니다.
5. 그런 다음 **개인정보** > **웹사이트 데이터 관리로** 이동합니다.
6. 목록에서 사이트를 선택합니다.
7. **제거를** 선택하거나 모든 사이트 데이터를 제거하려면 **모두 제거를** 선택합니다.
8. **완료를** 선택합니다.

이제 푸시 권한이 재설정되었습니다. 사이트에 새 탭을 열고 사용해 보세요.

{% endtab %}
{% endtabs %}

아직도 도움이 필요하신가요? [지원 티켓을]({{site.baseurl}}/braze_support/) 엽니다.

