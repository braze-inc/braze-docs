---
nav_title: 연결된 콘텐츠 재시도
article_title: 연결된 콘텐츠 재시도
page_order: 3
description: "이 참조 문서에서는 연결된 콘텐츠 재시도 처리 방법에 대해 다룹니다."

---

# 연결된 콘텐츠 재시도 횟수

> 연결된 콘텐츠은 API로부터 데이터를 수신하는 것에 의존하기 때문에, Braze가 호출하는 동안 API가 간헐적으로 사용할 수 없을 가능성이 있습니다. 이 경우 Braze는 지수 백오프를 사용하여 요청을 재시도하는 재시도 로직을 지원합니다. <br><br> This page covers how to add retries to your Connected Content calls.

## How to enable retries

재시도를 활성화하려면 다음 코드 스니펫에 표시된 대로 연결된 콘텐츠 호출에 `:retry`를 추가하세요.
{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

## Retry outcomes

### When the API call fails and retries are enabled

API 호출이 실패하고 이것이 활성화된 경우 Braze는 각 재전송에 대해 설정한 [속도 제한][47]을 준수하면서 호출을 재시도합니다. Braze는 실패한 메시지를 대기줄의 뒤로 이동시키고, 필요한 경우 메시지를 보내는 데 걸리는 총 시간에 추가 시간을 더합니다.

### When a retry succeeds

재시도한 시도가 성공하면 메시지가 전송되고 해당 메시지에 대한 추가 재시도는 시도되지 않습니다. 연결된 콘텐츠 호출이 5번 오류가 발생하면 [중단 메시지 태그][1]가 트리거된 것처럼 메시지가 중단됩니다.

{% alert note %}
연결된 콘텐츠 `:retry`는 인앱 메시지에 사용할 수 없습니다.
{% endalert %}


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[16]: [success@braze.com](mailto:success@braze.com)
[47]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting
