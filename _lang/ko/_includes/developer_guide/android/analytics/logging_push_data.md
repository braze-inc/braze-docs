## Braze API로 데이터 로깅(권장)

[`/users/track` 엔드포인트를]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 호출하여 실시간으로 분석을 기록할 수 있습니다. 분석을 기록하려면 Braze 대시보드에서 `braze_id` 값을 전송하여 업데이트할 고객 프로필을 식별합니다.

![개인화된 푸시 대시보드 예제]({% image_buster /assets/img/push_implementation_guide/android_braze_id_configuration.png %}){: style="max-width:79%;"}

## 수동으로 데이터 로깅하기

페이로드의 세부 사항에 따라 `FirebaseMessagingService.onMessageReceived` 구현 또는 스타트업 활동 내에서 수동으로 분석을 기록할 수 있습니다. `FirebaseMessagingService` 서브클래스는 호출 후 9초 이내에 실행을 완료해야 Android 시스템에 의해 [플래그가 지정되거나 종료되지](https://firebase.google.com/docs/cloud-messaging/android/receive) 않는다는 점을 명심하세요.
