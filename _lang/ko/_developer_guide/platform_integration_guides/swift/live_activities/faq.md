---
nav_title: FAQ
article_title: 라이브 활동 FAQ
page_order: 20
description: "이 페이지에서는 Swift SDK의 라이브 활동에 대해 자주 묻는 질문에 대한 답변을 제공합니다."
tool: Live Activities
platform:
  - iOS
---

# 자주 묻는 질문

> 이 문서에서는 라이브 활동에 대해 몇 가지 자주 묻는 질문에 대한 답변을 제공합니다.

## 기능 및 지원

### 어떤 플랫폼에서 라이브 활동을 지원하나요?

라이브 활동은 현재 iOS에만 적용되는 기능입니다. 라이브 활동 문서에서는 Braze Swift SDK를 통해 라이브 활동을 관리하기 위한 [전제 조건]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/#prerequisites)을 다룹니다.

### React Native 앱이 라이브 활동을 지원하나요?

예. React Native SDK 3.0.0 이상에서 Braze Swift SDK를 통해 라이브 활동을 지원합니다. 즉, Braze Swift SDK에 직접 React Native iOS 코드를 작성해야 합니다. 

Apple에서 제공하는 라이브 활동 기능은 JavaScript로 변환할 수 없는 언어(예: Swift 동시성, 제네릭, SwiftUI)를 사용하기 때문에 라이브 활동을 위한 React Native 전용 JavaScript 편의 API가 없습니다.

### Braze는 캠페인 또는 캔버스 단계로 라이브 활동을 지원하나요?

아니요, 현재 이 기능은 지원되지 않습니다.

## 푸시 알림 및 실시간 활동

### 실시간 활동이 활성화되어 있는 동안 푸시 알림이 전송되면 어떻게 되나요? 

![화면 중앙에 불스 대 베어스 스포츠 경기 실시간 활동이 표시된 휴대폰 화면과 화면 하단에 푸시 알림 텍스트가 표시됩니다.]({% image_buster /assets/img/push-vs-live-activities.png %}){: style="max-width:30%;float:right;margin-left:15px;"}

실시간 활동과 푸시 알림은 서로 다른 화면 공간을 차지하며 사용자 화면에서 충돌하지 않습니다.

### 라이브 활동이 푸시 메시지 기능을 활용하는 경우, 라이브 활동을 수신하려면 푸시 알림을 사용 설정해야 하나요?

라이브 활동은 푸시 알림을 통해 업데이트를 받지만, 다른 사용자 설정에 의해 제어됩니다. 사용자는 라이브 활동을 옵트인할 수 있지만 푸시 알림을 옵트아웃할 수 있습니다. 반대의 경우도 마찬가지입니다.

실시간 활동 업데이트 토큰은 8시간 후에 만료됩니다.

### 라이브 활동에 푸시 프라이머가 필요한가요?

[푸시 프라이머]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)는 사용자가 앱에서 푸시 알림을 옵트인하라는 프롬프트를 표시하는 모범 사례입니다. 그러나 라이브 활동을 선택하라는 시스템 프롬프트는 표시되지 않습니다. 기본적으로 사용자는 iOS 16.1 이상에서 해당 앱을 설치할 때 개별 앱의 실시간 활동에 옵트인합니다. 이 권한은 앱별로 디바이스 설정에서 비활성화하거나 다시 활성화할 수 있습니다.

## 기술 주제 및 문제 해결

### 실시간 활동에 오류가 있는지 어떻게 알 수 있나요?

모든 라이브 활동 오류는 Braze 대시보드의 [메시지 활동 로그]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)에 기록됩니다. 이는 'LiveActivity 오류'를 기준으로 필터링할 수 있습니다.

### 푸시 시작 알림을 보낸 후에도 내 실시간 활동을 받지 못한 이유는 무엇인가요?

먼저 페이로드에 엔드포인트에 설명된 모든 필수 필드가 포함되어 있는지 확인합니다. [`messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start) 엔드포인트에 설명된 모든 필수 필드가 포함되어 있는지 확인합니다. `activity_attributes` 및 `content_state` 필드는 프로젝트 코드에 정의된 속성과 일치해야 합니다. 페이로드가 정확하다고 확신하는 경우, APN에 의해 속도 제한이 적용될 수 있습니다. 이 제한은 Braze가 아닌 Apple에서 부과합니다.

푸시 투 스타트 알림이 장치에 성공적으로 도착했지만 속도 제한으로 인해 표시되지 않았는지 확인하려면 Mac의 콘솔 앱을 사용하여 프로젝트를 디버그할 수 있습니다. 원하는 디바이스의 기록 프로세스를 첨부한 다음 검색창에서 `process:liveactivitiesd` 으로 로그를 필터링합니다.

### `live_activity/update` 엔드포인트를 사용하려고 할 때 액세스 거부됨 응답을 받습니다. 왜인가요?

사용하는 API 키에 올바른 권한을 부여해야 다양한 Braze API 엔드포인트에 액세스할 수 있습니다. 이전에 생성한 API 키를 사용하는 경우 해당 권한을 업데이트하지 않았을 수 있습니다. [API 키 보안 개요]({{site.baseurl}}/api/basics/#rest-api-key-security)를 다시 한 번 살펴보세요.

### `messages/send` 엔드포인트는 `messages/live_activity/update` 엔드포인트와 공유 비율을 제한하나요? 

기본적으로 `messages/live_activity/update` 엔드포인트의 사용량 제한은 여러 엔드포인트에 걸쳐 워크스페이스당 매시간 250,000건의 요청입니다. 자세한 내용은 [API 요금 한도를]({{site.baseurl}}/api/api_limits/) 참조하세요.

### 푸시 투 스타트 토큰이 생성되지 않는 이유는 무엇인가요?

Apple은 iOS 17.2에 도입된 `pushToStartToken` 및 `pushToStartTokenUpdates` API를 제한했습니다. 실제로 푸시하여 시작 토큰은 첫 번째 설치 후 `application(_:didFinishLaunchingWithOptions:)`에서 앱을 처음 실행하는 동안에만 생성됩니다. 이 단계를 반복해야 하는 경우 해당 라이브 활동의 새 인스턴스를 수동으로 생성하거나 앱을 재부팅하고 다시 설치한 후에만 토큰을 다시 생성할 수 있습니다.

### 내 앱에 몇 개의 라이브 활동을 시작할 수 있나요?

제한은 Apple에서 정의하며 여러 요인에 따라 달라질 수 있습니다. 또한 향후 변경될 수 있습니다. 실제로는 앱당 한 번에 실행할 수 있는 동시 활동 인스턴스가 5개로 제한되어 있습니다. 이후 이 제한을 초과하여 새 인스턴스를 시작하려는 모든 시도는 시스템에서 무시됩니다.

### 문제 해결 중에 주의해야 할 다른 사항은 무엇인가요?

- `.p12` 또는 `.pem` 파일 대신 `.p8` 키를 인증에 사용하고 있는지 확인하세요.
- 푸시 프로비저닝 프로필이 테스트 중인 환경과 일치하는지 확인합니다. 유니버설 인증서는 개발 또는 프로덕션 Apple 푸시 알림(APN) 서비스 환경으로 보내도록 Braze 대시보드에서 구성할 수 있습니다. 프로덕션 앱에 개발 인증서를 사용하거나 개발 앱에 프로덕션 인증서를 사용하는 경우 작동하지 않습니다.


