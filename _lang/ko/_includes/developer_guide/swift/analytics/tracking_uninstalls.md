## 제거 추적 설정

### 1단계: 백그라운드 푸시 사용

Xcode 프로젝트에서 **기능으로** 이동하여 **백그라운드 모드가** 활성화되어 있는지 확인합니다. 자세한 내용은 [무음 푸시 알림을]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) 참조하세요.

### 2단계: 내부 푸시 알림 무시하기

Swift Braze SDK는 백그라운드 푸시 알림을 사용하여 제거 추적 분석을 수집합니다. 이러한 [알림이]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications) 전송될 때 앱이 원치 않는 작업을 수행하지 않도록 하려면 [내부 푸시 알림이 무시되도록]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications) 설정해야 합니다.

### 3단계: 테스트 푸시 보내기(선택 사항)

다음으로, Braze 대시보드에서 테스트 푸시 알림을 보내세요(사용자 프로필이 업데이트되지는 않으니 걱정하지 마세요).

1. **메시징** > **캠페인으로** 이동하여 관련 플랫폼을 사용하여 푸시 알림 캠페인을 만듭니다.
2. **설정** > **앱 설정으로** 이동하여 `appboy_uninstall_tracking` 키에 관련 `true` 값을 추가한 다음 **콘텐츠 사용 가능 플래그 추가에** 체크합니다.
3. **미리보기** 페이지를 사용하여 테스트 제거 추적 푸시를 직접 전송합니다.
4. 앱이 푸시 알림을 수신할 때 원치 않는 자동 동작을 수행하지 않는지 확인하세요.

{% alert note %}
테스트 푸시 알림과 함께 배지 번호가 전송되지만, 실제 제거 추적 푸시에서는 배지 번호가 전송되지 않습니다.
{% endalert %}

### 3단계: 제거 추적 활성화

마지막으로 Braze에서 제거 추적을 활성화합니다. 전체 안내는 [제거 추적 사용을]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking) 참조하세요.

{% alert important %}
제거 추적은 정확하지 않을 수 있습니다. Braze에 표시되는 지표는 지연되거나 부정확할 수 있습니다.
{% endalert %}
