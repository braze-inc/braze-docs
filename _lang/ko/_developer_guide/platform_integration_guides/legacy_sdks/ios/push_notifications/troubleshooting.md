---
nav_title: 문제 해결
article_title: iOS용 푸시 알림 문제 해결
platform: iOS
page_order: 30
description: "이 참조 문서에서는 iOS 푸시 구현 시 잠재적인 문제 해결 주제를 다룹니다."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 문제 해결 {#push-troubleshooting}

## Braze/APNs 워크플로 이해하기

Apple 푸시 알림 서비스(APN)는 iOS 및 OS X 애플리케이션에 푸시 알림을 전송하기 위한 Apple의 인프라입니다. 다음은 사용자의 디바이스에서 푸시 알림을 활성화하는 방법과 Braze가 푸시 알림을 보내는 방법에 대한 간단한 구조입니다:

1. 푸시 인증서 및 프로비저닝 프로필을 구성합니다.
2. 디바이스가 APN에 등록하고 Braze에 푸시 토큰을 제공합니다.
3. Braze 푸시 캠페인을 시작합니다.
4. Braze는 유효하지 않은 토큰을 제거합니다.

#### 1단계: 푸시 인증서 및 프로비저닝 프로필 구성하기

앱을 개발할 때 푸시 알림을 활성화하려면 SSL 인증서를 생성해야 합니다. 이 인증서는 앱이 빌드된 프로비저닝 프로필에 포함되며, Braze 대시보드에도 업로드되어야 합니다. 이 인증서를 통해 Braze는 사용자를 대신하여 푸시 알림을 전송할 수 있음을 APN에 알릴 수 있습니다.

[프로비저닝 프로필](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) 및 인증서에는 개발 및 배포의 두 가지 유형이 있습니다. 혼동을 피하기 위해 배포 프로필과 인증서만 사용하는 것을 권장합니다. 개발 및 배포에 다른 프로필과 인증서를 사용하기로 선택한 경우 대시보드에 업로드한 인증서가 현재 사용 중인 프로비저닝 프로필과 일치하는지 확인하세요.

{% alert warning %}
푸시 인증서 환경을 변경하지 마세요(개발 대 프로덕션). 푸시 인증서를 잘못된 환경으로 변경하면 푸시 토큰이 실수로 제거되어 푸시가 사용자에게 전달되지 못할 수 있습니다.
{% endalert %}

#### 2단계: 디바이스가 APN에 등록하고 Braze에 푸시 토큰을 제공합니다.

사용자가 앱을 열면 푸시 알림을 수락할지 묻는 프롬프트가 표시됩니다. 이 프롬프트를 수락하면 APN이 해당 특정 기기에 대한 푸시 토큰을 생성합니다. iOS SDK는 기본 [자동 플러시 정책을]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/fine_network_traffic_control/#automatic-request-processing) 사용하는 앱에 대해 푸시 토큰을 즉시 비동기적으로 전송합니다. 푸시 토큰이 사용자와 연결되면 사용자 프로필의 **참여** 탭에 있는 대시보드에 "푸시 등록됨"으로 표시되며, Braze 캠페인에서 푸시 알림을 받을 수 있게 됩니다.

{% alert note %}
Xcode 14부터는 iOS 시뮬레이터에서 원격 푸시 알림을 테스트할 수 있습니다.
{% endalert %}

#### 3단계: Braze 푸시 캠페인 시작

푸시 캠페인이 시작되면 Braze는 APN에 메시지 전달을 요청합니다. Braze는 대시보드에 업로드된 SSL 푸시 인증서를 사용하여 제공된 푸시 토큰으로 푸시 알림을 전송할 수 있는지 인증하고 확인합니다. 기기가 온라인 상태인 경우 캠페인이 전송된 직후에 알림이 수신되어야 합니다. Braze는 알림의 기본 APN [만료일](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607)을 30일로 설정합니다.

#### 4단계: 유효하지 않은 토큰 제거하기

메시지를 보내려고 했던 푸시 토큰이 유효하지 않다고 [APN이](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) 알려주면 해당 토큰이 연결된 사용자 프로필에서 해당 토큰을 제거합니다.

## 푸시 오류 로그 활용하기

Braze는 **메시지 활동 로그** 내에 푸시 알림 오류 로그를 제공합니다. 이 오류 로그는 캠페인이 예상대로 작동하지 않는 이유를 파악하는 데 매우 유용한 다양한 경고를 제공합니다. 오류 메시지를 클릭하면 특정 인시던트 문제를 해결하는 데 도움이 되는 관련 설명서로 리디렉션됩니다.

![오류 발생 시간, 앱 이름, 채널, 오류 유형 및 오류 메시지가 표시된 푸시 오류 로그]({% image_buster /assets/img_archive/message_activity_log.png %})

여기에서 볼 수 있는 일반적인 오류로는 ["푸시 토큰에 등록되지 않은 전송 수신"](#received-unregistered-sending) 등의 사용자별 알림이 있습니다.

또한 Braze는 **참여** 탭의 사용자 프로필에서 푸시 변경 로그를 제공합니다. 이 체인지로그는 토큰 무효화, 푸시 등록 오류, 새 사용자에게 이동되는 토큰 등의 푸시 등록 동작에 대한 인사이트를 제공합니다.

![]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

## 푸시 등록 문제

애플리케이션의 푸시 등록 로직에 대한 검증을 추가하려면 [푸시 단위 테스트를]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/unit_tests/) 구현하세요.

#### 푸시 등록 프롬프트 없음

애플리케이션에서 사용자에게 푸시 알림을 등록하라는 프롬프트를 표시하지 않으면 푸시 등록 통합에 문제가 있을 수 있습니다. [설명서를]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) 준수하고 푸시 등록을 올바르게 통합했는지 확인하세요. 코드에 중단점을 설정하여 푸시 등록 코드가 실행 중인지 확인할 수도 있습니다.

#### 대시보드에 '푸시 등록' 사용자가 표시되지 않음

- 앱에서 푸시 알림을 허용하라는 프롬프트를 표시하는지 확인합니다. 일반적으로 이 프롬프트는 앱을 처음 열 때 표시되지만 다른 경우에 표시하도록 프로그래밍할 수 있습니다. 표시해야 할 위치에 표시되지 않는다면 앱의 푸시 기능 기본 구성에 문제가 있는 것일 수 있습니다.
  - [푸시 통합을]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) 위한 단계가 성공적으로 완료되었는지 확인합니다.
  - 앱이 빌드된 프로비저닝 프로필에 푸시 권한이 포함되어 있는지 확인합니다. Apple 개발자 계정에서 사용 가능한 모든 프로비저닝 프로필을 가져오고 있는지 확인합니다. 이를 확인하려면 다음 단계를 수행하세요:
    1. Xcode에서 **환경설정 > 계정**으로 이동합니다. 또는 키보드 단축키 <kbd>Command</kbd>+<kbd>,</kbd>를 사용합니다.
    2. 개발자 계정에 사용하는 Apple ID를 선택하고 **세부 정보 보기**를 클릭합니다.
    3. 다음 페이지에서 **<i class="fas fa-redo-alt"></i> 새로 고침**을 클릭하고 사용 가능한 모든 프로비저닝 프로필을 가져오는지 확인합니다.
- 앱에서 [푸시 기능을 제대로 활성화했는지]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-2-enable-push-capabilities) 확인하세요.
- 푸시 프로비저닝 프로필이 테스트를 수행하는 환경과 일치하는지 확인합니다. 유니버설 인증서는 개발 또는 프로덕션 APN 환경으로 보내도록 Braze 대시보드에서 구성할 수 있습니다. 프로덕션 앱에 개발 인증서를 사용하거나 개발 앱에 프로덕션 인증서를 사용하는 경우 작동하지 않습니다.
- 코드에 중단점을 설정하여 `registerPushToken` 메서드를 호출하고 있는지 확인하세요.
- 기기를 사용 중이고(시뮬레이터에서는 푸시가 작동하지 않음) 네트워크 연결 상태가 양호한지 확인합니다.

## 푸시 알림을 받지 못하는 기기

#### 푸시 알림을 보낸 후 사용자가 더 이상 '푸시 등록' 상태가 아님

사용자에게 유효하지 않은 푸시 토큰이 있음을 나타낼 수 있습니다. 이는 여러 가지 이유로 발생할 수 있습니다:

##### 대시보드와 앱 인증서 불일치

대시보드에 업로드한 푸시 인증서가 앱이 빌드된 프로비저닝 프로필의 푸시 인증서와 같지 않은 경우 APN은 토큰을 거부합니다. 다른 테스트 알림을 시도하기 전에 올바른 인증서를 업로드하고 앱에서 다른 세션을 완료했는지 확인합니다.

##### 설치 제거 수

사용자가 애플리케이션을 제거한 경우, 해당 푸시 토큰은 유효하지 않으며 다음 전송 시 제거됩니다.

##### 프로비저닝 프로필 다시 생성

마지막 수단으로, 처음부터 완전히 새로운 프로비저닝 프로필을 만들면 여러 환경, 프로필 및 앱에서 동시에 작업할 때 발생하는 구성 오류를 해결할 수 있습니다. iOS 앱용 푸시 알림을 설정할 때 '변동 부분'이 많으므로 때로는 처음부터 다시 시도하는 것이 가장 좋습니다. 또한 문제 해결을 계속해야 하는 경우 문제를 격리하는 데 도움이 됩니다.

#### 푸시 알림을 보낸 후 사용자가 여전히 '푸시 등록' 상태가 아님

##### 앱이 전경에 표시됨

`UserNotifications` 프레임워크를 통해 푸시를 통합하지 않는 iOS 버전에서는 푸시 메시지를 수신할 때 앱이 포그라운드에 있는 경우 푸시 메시지가 표시되지 않습니다. 테스트 메시지를 보내기 전에 테스트 기기에서 앱을 백그라운드로 실행해야 합니다.

##### 잘못 예약된 테스트 알림

테스트 메시지에 대해 설정한 일정을 확인하세요. 현지 시간대 배달 또는 [지능형 타이밍으로]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) 설정되어 있는 경우 메시지를 아직 받지 못했거나 메시지를 받았을 때 앱이 포그라운드에 있었을 수 있습니다.

#### 테스트 중인 앱에서 '푸시 등록'되지 않은 사용자

테스트 메시지를 보내려는 사용자의 사용자 프로필을 확인합니다. **참여** 탭 아래에 '푸시 가능한 앱' 목록이 있어야 합니다. 테스트 메시지를 보내려는 앱이 이 목록에 있는지 확인합니다. 사용자가 워크스페이스의 앱에 대한 푸시 토큰을 보유한 경우 '푸시 등록'으로 표시되므로 이는 오탐일 수 있습니다.

다음은 푸시 등록에 문제가 있거나 사용자의 토큰이 푸시된 후 APN에 의해 유효하지 않은 것으로 Braze에 반환되었음을 나타냅니다:

![사용자의 연락처 설정을 표시하는 사용자 프로필입니다. 여기에서 어떤 앱에 푸시가 등록되어 있는지 확인할 수 있습니다.]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## 메시지 활동 로그 오류

#### 푸시 토큰에 등록되지 않은 전송 수신됨 {#received-unregistered-sending}

- `[[Appboy sharedInstance] registerPushToken:]` 메서드에서 Braze로 전송되는 푸시 토큰이 유효한지 확인합니다. **메시지 활동 로그에서** 푸시 토큰을 확인할 수 있습니다. 문자와 숫자 조합이 포함된 긴 문자열(예: `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`)이어야 합니다. 푸시 토큰이 다르게 보인다면 Braze에 푸시 토큰을 전송하는 [코드를]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-4-register-push-tokens-with-braze) 확인하세요.
- 푸시 프로비저닝 프로필이 테스트 중인 환경과 일치하는지 확인합니다. 유니버설 인증서는 개발 또는 프로덕션 APN 환경으로 보내도록 Braze 대시보드에서 구성할 수 있습니다. 프로덕션 앱에 개발 인증서를 사용하거나 개발 앱에 프로덕션 인증서를 사용하는 경우 작동하지 않습니다.
 - Braze에 업로드한 푸시 토큰이 푸시 토큰을 보낸 앱을 빌드하는 데 사용한 프로비저닝 프로필과 일치하는지 확인합니다.

#### 주제용이 아닌 디바이스 토큰

이 오류는 앱의 푸시 인증서와 번들 ID가 일치하지 않음을 나타냅니다. Braze에 업로드한 푸시 인증서가 푸시 토큰을 보낸 앱을 빌드하는 데 사용한 프로비저닝 프로필과 일치하는지 확인합니다.

#### 푸시 토큰으로 전송하는 BadDeviceToken

`BadDeviceToken`은 APN 오류 코드이며, Braze에서 생성된 오류가 아닙니다. 이 응답이 반환되는 데에는 다음과 같은 여러 가지 이유가 있을 수 있습니다:

- 앱이 대시보드에 업로드된 자격 증명에 대해 유효하지 않은 푸시 토큰을 수신했습니다.
- 이 워크스페이스에 대해 푸시가 비활성화되었습니다.
- 사용자가 푸시 수신을 거부했습니다.
- 앱이 삭제되었습니다.
- Apple이 푸시 토큰을 새로 고침하여 기존 토큰이 무효화되었습니다.
- 앱은 프로덕션 환경용으로 빌드되었지만 Braze에 업로드된 푸시 자격 증명은 개발 환경용으로 설정되어 있습니다(또는 반대의 경우도 마찬가지).

## 푸시 전송 후 문제

애플리케이션의 푸시 처리에 대한 검증을 추가하려면 [푸시 단위 테스트를]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/unit_tests/) 구현하세요.

#### 푸시 클릭이 기록되지 않음 {#push-clicks-not-logged}

- 이 문제가 iOS 10에서만 발생하는 경우 [iOS 10에]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-5-enable-push-handling) 대한 푸시 연동 단계를 따랐는지 확인하세요.
- Braze는 포그라운드에서 무음 수신된 푸시 알림을 처리하지 않습니다(예: `UserNotifications` 프레임워크 이전의 기본 포그라운드 푸시 동작). 즉, 링크가 열리지 않고 푸시 클릭이 기록되지 않습니다. 애플리케이션이 아직 `UserNotifications` 프레임워크를 통합하지 않은 경우, 애플리케이션 상태가 `UIApplicationStateActive`이면 Braze는 푸시 알림을 처리하지 않습니다. 앱에서 [푸시 처리 메서드]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-5-enable-push-handling) 호출이 지연되지 않도록 해야 하며, 그렇지 않으면 iOS SDK에서 푸시 알림을 무음 포그라운드 푸시 이벤트로 처리하여 전달하지 않을 수 있습니다.

#### 푸시 클릭으로 인한 웹 링크가 열리지 않음

iOS 9 이상에서는 웹 보기에서 링크를 열려면 ATS와 호환되는 링크가 필요합니다. 웹 링크가 HTTPS를 사용하는지 확인합니다. 자세한 내용은 [ATS 규정 준수]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#app-transport-security-ats) 문서를 참조하세요.

#### 푸시 클릭으로 인한 딥링크가 열리지 않음

딥링크를 처리하는 대부분의 코드는 푸시 오픈도 처리합니다. 먼저 푸시 오픈이 로깅되고 있는지 확인합니다. 그렇지 않은 경우 [해당 문제를 수정하세요](#push-clicks-not-logged) (수정하면 링크 처리가 수정되는 경우가 많으므로).

열람이 기록되는 경우 일반적인 딥링크 문제인지 또는 딥링크 푸시 클릭 처리에 문제가 있는지 확인합니다. 이를 위해 인앱 메시지 클릭의 딥링크가 작동하는지 테스트합니다.

#### 직접 열기가 거의 또는 전혀 없음

한 명 이상의 사용자가 iOS 푸시 알림을 열었지만 Braze에 _직접 열기가_ 거의 또는 전혀 기록되지 않는다면 [SDK 통합에]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/overview) 문제가 있는 것일 수 있습니다. 테스트 전송 또는 무음 푸시 알림의 경우 _직접 열기는_ 기록되지 않습니다.

- 메시지가 [무음 푸시 알림으로]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/#sending-silent-push-notifications) 전송되고 있지 않은지 확인하세요. 메시지가 무음으로 간주되지 않으려면 제목이나 본문에 텍스트가 있어야 합니다.
- [푸시 연동 가이드에서]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/push_notifications/integration) 다음 단계를 다시 확인하세요:
   - [푸시 등록하기]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns): 앱을 실행할 때마다, 가급적이면 `application:didFinishLaunchingWithOptions:` 내에서 3단계의 코드가 실행되어야 합니다. `UNUserNotificationCenter.current()` 의 델리게이트 속성은 `UNUserNotificationCenterDelegate` 을 구현하고 `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` 메서드를 포함하는 객체에 할당해야 합니다.
   - [푸시 처리를 사용]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/push_notifications/integration/#step-5-enable-push-handling) 설정합니다: `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` 메서드가 구현되었는지 확인합니다.

