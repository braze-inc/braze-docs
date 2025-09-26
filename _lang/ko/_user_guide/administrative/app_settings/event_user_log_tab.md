---
nav_title: 이벤트 사용자 로그
article_title: 이벤트 사용자 로그
page_order: 7
page_type: reference
description: "이 참조 문서에서는 Braze 통합에서 문제를 디버깅하거나 해결하는 데 도움이 되는 이벤트 사용자 로그를 다룹니다."

---

# 이벤트 사용자 로그

> 이벤트 사용자 로그는 Braze 통합의 문제를 분석, 디버깅하거나 기타 문제를 해결하는 데 도움이 될 수 있습니다. 이 탭에서는 오류 유형, 오류와 관련된 앱, 발생 시기 등이 자세히 나와 있는 오류 로그를 볼 수 있으며, 종종 오류와 관련된 원시 데이터를 볼 수도 있습니다.

{% alert tip %}
이 글 외에도 이벤트 사용자 로그를 사용하여 직접 문제 해결 및 디버깅을 수행하는 방법을 다루는 [품질 보증 및 디버깅 도구](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/) Braze 학습 과정도 확인해 보실 것을 권장합니다.
{% endalert %}

로그에 액세스하려면 **설정** > **이벤트 사용자 로그로** 이동합니다.

로그를 쉽게 찾기 위해 다음을 기준으로 필터링할 수 있습니다:

* SDK 또는 API
* 앱 이름
* 시간 프레임
* 사용자

각 로그는 여러 섹션으로 나뉘며, 여기에는 다음이 포함될 수 있습니다.

* 기기 속성
* 사용자 속성
* 이벤트
* 캠페인 이벤트
* 응답 데이터

Select the **Expand data** icon to show the raw JSON data for that specific log.

![The "Expand data icon" next to a specific log.]({% image_buster /assets/img_archive/expand_data.png %})

이벤트 사용자 로그는 기록된 후 30일 동안 대시보드에 남아 있습니다.

![Raw logs for events]({% image_buster /assets/img_archive/rawlogs.png %}){: style="max-width:60%;"}

## 문제 해결

### 테스트 사용자에 대한 누락된 SDK 로그

내부 그룹에 사용자를 추가했지만 이벤트 사용자 로그에 SDK 로그가 표시되지 않는다면 구성 옵션이 누락되었기 때문일 수 있습니다. In order to capture SDK logs, make sure to select **Record User Events for group members** in the **Internal Group Settings** for that [internal group]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/).

### 로그 업데이트 지연

이는 API의 정상적인 속도 저하일 수 있습니다.

SDK 메서드를 호출하면 일반적으로 SDK는 해당 이벤트를 로컬에 캐시하고 10초마다 서버로 플러시합니다. 작업 처리 대기열이 이벤트를 수집하는 데는 당시의 전체 로드에 따라 1초에서 몇 분 정도 걸릴 수 있습니다.  

이벤트가 최대한 빨리 도착하기를 원한다면 `requestImmediateDataFlush()` 함수를 호출해 보세요.

### 세션 종료와 세션 시작의 타임스탬프가 비슷합니다(iOS).

이벤트 사용자 로그에는 Braze가 세션 종료 알림을 받은 시점의 타임스탬프가 표시되며, 다음 세션이 시작되기 몇 밀리초 전이 됩니다. iOS는 앱이 백그라운드에 있을 때 스레드 실행을 적극적으로 중지하기 때문에 앱이 다시 열리기 전에는 세션이 종료되었는지 알 수 없으므로, 앱이 다시 열릴 때까지 어떤 데이터도 Braze로 플러시될 수 없습니다.

세션 종료 시간은 세션 시작 전 초로 지정되지만 이벤트가 플러시되면 세션 지속 시간은 별도로 플러시되며 앱이 열려 있던 시간을 정확하게 반영합니다. 따라서 이 동작은 `Median Session Duration` 필터에는 영향을 미치지 않습니다.

사용자 세션과 관련하여 Braze를 사용하여 다음과 같은 데이터를 모니터링할 수 있습니다:

- 사용자가 참여한 세션 수
- 사용자가 마지막으로 세션을 시작한 시기
- 사용자가 캠페인을 수신한 후 세션을 시작하는 경우
- 사용자의 평균 세션 지속 시간

이러한 동작은 다음 세션에서 플러시되는 세션 종료 이벤트의 영향을 받지 않습니다.

