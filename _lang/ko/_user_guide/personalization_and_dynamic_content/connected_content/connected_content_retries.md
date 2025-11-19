---
nav_title: 연결된 콘텐츠 재시도
article_title: 연결된 콘텐츠 재시도
page_order: 5
description: "이 참조 문서에서는 연결된 콘텐츠 재시도를 처리하는 방법에 대해 설명합니다."

---

# 연결된 콘텐츠에 재시도 로직 사용

> 이 페이지에서는 연결된 콘텐츠 통화에 재시도를 추가하는 방법에 대해 설명합니다.

## 재시도 작동 방식 

연결된 콘텐츠는 API로부터 데이터를 수신하는 데 의존하기 때문에 Braze가 호출하는 동안 API를 간헐적으로 사용할 수 없을 수 있습니다. 이 경우 Braze는 지수 백오프를 사용하여 요청을 다시 시도하는 재시도 로직을 지원합니다.

{% alert note %}
연결된 콘텐츠 `:retry` 는 인앱 메시징에 사용할 수 없습니다.
{% endalert %}

## 재시도 로직 사용

재시도 로직을 사용하려면 다음 코드 스니펫에 표시된 것처럼 연결된 콘텐츠 호출에 `:retry` 태그를 추가하세요:

{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

연결된 콘텐츠 통화에 `:retry` 태그가 포함되어 있으면 Braze는 최대 5회까지 통화를 재시도합니다.

### 결과 다시 시도

#### 재시도가 성공한 경우

재시도가 성공하면 메시징이 전송되고 해당 메시징에 대해 더 이상 재시도가 시도되지 않습니다.

#### API 호출이 실패하고 재시도가 인에이블먼트된 경우

API 호출이 실패하고 이 기능이 인에이블먼트된 경우, Braze는 각 재전송에 대해 설정한 [속도 제한을]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting) 준수하면서 호출을 다시 시도합니다. Braze는 실패한 메시지를 대기줄의 뒤쪽으로 이동하고 필요한 경우 메시지를 보내는 데 걸리는 총 시간에 추가 시간을 더합니다.

연결된 콘텐츠 호출 오류가 5회 이상 발생하면 [중단 메시지 태그가]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/) 트리거되는 방식과 유사하게 메시지가 중단됩니다.