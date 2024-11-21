## 기본 점검

#### 한 사용자에 대한 인앱 메시지가 표시되지 않았습니다.

1. SDK가 새 인앱 메시지를 요청할 때 사용자가 세션 시작 시점에 세그먼트에 있었나요?
2. 사용자가 캠페인 타겟팅 규칙에 따라 인앱 메시지를 수신할 자격이 있거나 재자격이 있나요?
3. 사용자가 주파수 제한의 영향을 받았나요?
4. 사용자가 대조군에 속해 있었나요? 캠페인이 AB 테스트용으로 구성되어 있는지 확인하세요.
5. 예상 메시지 대신 다른 우선순위가 높은 인앱 메시지가 표시되었나요?
6. 내 디바이스가 캠페인에서 지정한 올바른 방향이었나요?
7. SDK에서 시행하는 트리거 간 기본 30초의 최소 시간 간격으로 인해 메시지가 표시되지 않나요?

#### 내 인앱 메시지가 이 플랫폼의 모든 사용자에게 표시되지 않았습니다.

1. 캠페인이 모바일 앱 또는 웹 브라우저를 적절하게 타겟팅하도록 구성되어 있나요? 예를 들어, 캠페인이 웹 브라우저만 타겟팅하는 경우 Android 기기에는 전송되지 않습니다.
2. 사용자 지정 UI를 구현했으며 의도한 대로 작동하고 있나요? 표시를 방해할 수 있는 다른 앱 측의 사용자 지정 처리 또는 억제 기능이 있나요? 
3. 이 특정 플랫폼 및 앱 버전에서 인앱 메시지를 성공적으로 표시한 적이 있나요?
4. 트리거가 디바이스에서 로컬로 발생했나요? REST 호출은 SDK에서 인앱 메시지를 트리거하는 데 사용할 수 없다는 점에 유의하세요.

#### 내 인앱 메시지가 모든 사용자에게 표시되지 않음

1. 트리거 액션이 대시보드와 앱 통합에서 올바르게 설정되었나요?
2. 예상 메시지 대신 다른 우선순위가 높은 인앱 메시지가 표시되었나요?
3. 최신 버전의 SDK를 사용 중이신가요? 일부 인앱 메시지 유형에는 SDK 버전 요구 사항이 있습니다.
4. 세션이 통합에 제대로 통합되었나요? 이 앱에서 세션 분석이 작동하나요?

이러한 시나리오에 대해 자세히 알아보려면 [고급 문제 해결 섹션](#troubleshooting-in-app-advanced)을 참조하세요.

## 노출 및 클릭 분석 관련 문제

{% if include.sdk == "iOS" %}
#### 노출 수 및 클릭 수가 기록되지 않습니다.

메시지 표시 또는 클릭 작업을 수동으로 처리하도록 인앱 메시지 위임자를 설정한 경우 인앱 메시지에 대한 [클릭](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:)) 및 [노출](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logimpression(using:))을 수동으로 기록합니다.
{% elsif include.sdk == "Android" %}
#### 노출 수 및 클릭 수가 기록되지 않습니다.
메시지 표시 또는 클릭 작업을 수동으로 처리하도록 인앱 메시지 위임자를 설정한 경우 인앱 메시지에 대한 클릭 및 노출을 수동으로 기록합니다.
{% endif %}

#### 예상보다 적은 노출 횟수

트리거는 세션 시작 시 기기와 동기화하는 데 시간이 걸리므로 사용자가 세션 시작 직후 구매 또는 이벤트를 기록하면 경합 조건이 발생할 수 있습니다. 한 가지 가능한 해결 방법은 세션 시작 시 트리거하도록 캠페인을 변경한 다음, 의도한 이벤트 또는 구매를 세분화하는 것입니다. 이렇게 하면 이벤트가 발생한 후 다음 세션이 시작될 때 인앱 메시지가 전달됩니다.

## 고급 문제 해결 {#troubleshooting-in-app-advanced}

대부분의 인앱 메시지 문제는 전달과 표시라는 두 가지 주요 카테고리로 분류할 수 있습니다. 예상 인앱 메시지가 기기에 표시되지 않는 문제를 해결하려면 [인앱 메시지가 기기에 전달되었는지](#troubleshooting-in-app-message-delivery) 확인한 다음 [메시지 표시 문제](#troubleshooting-in-app-message-display)를 해결하세요.

### 인앱 메시지 전달 문제 해결 {#troubleshooting-in-app-message-delivery}

SDK는 세션 시작 시 Braze 서버에 인앱 메시지를 요청합니다. 인앱 메시지가 기기에 전달되고 있는지 확인하려면 인앱 메시지가 SDK에 의해 요청되고 Braze 서버에 의해 반환되는지 확인해야 합니다.

#### 메시지 요청 및 반환 여부 확인

1. 대시보드에서 [테스트 유저]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users)로 자신을 추가합니다.
2. 사용자를 대상으로 인앱 메시지 캠페인을 설정합니다.
3. 애플리케이션에서 새 세션이 발생하는지 확인합니다.
4. [이벤트 사용자 로그]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab))를 사용하여 세션 시작 시 기기에서 인앱 메시지를 요청하는지 확인하세요. 테스트 사용자의 세션 시작 이벤트와 연결된 SDK 요청을 찾습니다.
  - 앱에서 트리거된 인앱 메시지를 요청하는 경우 **응답 데이터** 아래 **요청된 응답** 필드에 `trigger`가 표시되어야 합니다.
  - 앱에서 원본 인앱 메시지를 요청하는 경우 **응답 데이터** 아래 **요청된 응답** 필드에 `in_app`이 표시되어야 합니다.
5. [이벤트 사용자 로그]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) )를 사용하여 응답 데이터에서 올바른 인앱 메시지가 반환되고 있는지 확인하세요.<br>![]({% image_buster /assets/img_archive/event_user_log_iams.png %})

##### 요청되지 않는 메시지 문제 해결

인앱 메시지가 요청되지 않는 경우 앱이 세션을 올바르게 추적하지 않을 수 있습니다. 인앱 메시지는 세션 시작 시 새로 고쳐지기 때문입니다. 또한 앱의 세션 제한 시간 의미에 따라 앱이 실제로 세션을 시작했는지 확인해야 합니다.

![성공적인 세션 시작 이벤트를 표시하는 이벤트 사용자 로그에서 발견된 SDK 요청.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

##### 반환되지 않는 메시지 문제 해결

인앱 메시지가 반환되지 않는다면 캠페인 타겟팅에 문제가 있는 것일 수 있습니다:

- 세그먼트에 사용자가 포함되어 있지 않습니다.
  - 사용자의 [\*\*참여**]({{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) 탭에서 **세그먼트** 아래에 올바른 세그먼트가 표시되는지 확인합니다.
- 사용자가 이전에 인앱 메시지를 받은 적이 있으며 다시 받을 자격이 없습니다.
  - **캠페인 작성기**의 **전달** 단계 아래에서 [캠페인 재자격 설정]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/))을 확인하고 재자격 설정이 테스트 설정과 일치하는지 확인합니다.
- 사용자가 캠페인의 빈도 한도에 도달했습니다.
  - 캠페인[빈도 제한 설정]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping))을 확인하여 테스트 설정과 일치하는지 확인하세요.
- 캠페인에 대조 그룹이 있는 경우 사용자가 대조 그룹에 속했을 수 있습니다.
  - 캠페인 이형 상품이 **컨트롤로** 설정된 수신된 캠페인 이형 상품 필터로 세그먼트를 생성하고 사용자가 해당 세그먼트에 속하는지 확인하여 이 문제가 발생했는지 확인할 수 있습니다.
  - 통합 테스트 목적으로 캠페인을 생성할 때는 대조군 추가를 옵트아웃해야 합니다.


### 인앱 메시지 표시 문제 해결 {#troubleshooting-in-app-message-display}

앱에서 인앱 메시지를 성공적으로 요청하고 수신하고 있지만 표시되지 않는 경우 기기 측 로직으로 인해 표시되지 않는 것일 수 있습니다.

{% if include.sdk == "iOS" %}
- 트리거된 인앱 메시지는 트리거 사이의 [최소 시간 간격]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers)을 기준으로 속도 제한이 적용되며, 기본값은 30초입니다.
{% elsif include.sdk == "Android" %}
- 트리거된 인앱 메시지는 트리거 사이의 [최소 시간 간격]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers)을 기준으로 속도 제한이 적용되며, 기본값은 30초입니다.
{% elsif include.sdk == "Web" %}
- 트리거된 인앱 메시지는 트리거 사이의 [최소 시간 간격]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers)을 기준으로 속도 제한이 적용되며, 기본값은 30초입니다.
{% endif %}
- 이미지 다운로드에 실패하면 이미지가 포함된 인앱 메시지가 표시되지 않습니다. 디바이스 로그를 확인하여 이미지 다운로드가 실패하지 않았는지 확인하세요.
{% case include.sdk %}
  {% when "iOS", "Android" %}
- 인앱 메시지 처리를 사용자 지정하기 위해 위임을 설정한 경우, 위임이 인앱 메시지 표시를 방해하지 않는지 확인합니다.
  {% when "Web" %}
- `braze.subscribeToInAppMessage` 또는 `appboy.subscribeToNewInAppMessages`를 통해 커스텀 인앱 메시지를 처리하는 경우 해당 가입을 확인하여 인앱 메시지 표시에 영향을 미치지 않도록 합니다.
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
- 기기 방향이 인앱 메시지에 지정된 방향과 일치하지 않으면 인앱 메시지가 표시되지 않습니다. 디바이스의 방향이 올바른지 확인하세요.
{% endcase %}