---
nav_title: 연결된 콘텐츠 재시도
article_title: 연결된 콘텐츠 재시도
page_order: 5
description: "이 참조 문서에서는 연결된 콘텐츠 재시도 처리 방법에 대해 다룹니다."

---

# 

> This page covers how to add retries to your Connected Content calls.

##  

 이 경우 Braze는 지수 백오프를 사용하여 요청을 재시도하는 재시도 로직을 지원합니다.

{% alert note %}
연결된 콘텐츠 `:retry`는 인앱 메시지에 사용할 수 없습니다.
{% endalert %}

## 




```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}



### Retry outcomes

#### When a retry succeeds



#### When the API call fails and retries are enabled

 Braze는 실패한 메시지를 대기줄의 뒤로 이동시키고, 필요한 경우 메시지를 보내는 데 걸리는 총 시간에 추가 시간을 더합니다.

