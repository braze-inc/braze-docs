---
nav_title: 테스팅
article_title: FireOS용 테스트
platform: FireOS
page_order: 19
page_type: reference
description: "이 참조 문서에서는 명령줄을 통해 FireOS 인앱 메시지 및 푸시 알림을 테스트하는 방법에 대한 정보를 제공합니다."
channel: 
- push

---

# 테스팅

> 이 참조 문서에서는 명령줄을 통해 FireOS 인앱 메시지 및 푸시 알림을 테스트하는 방법에 대한 정보를 제공합니다.

명령줄을 통해 인앱 및 푸시 알림을 테스트하려면 터미널을 통해 cURL 및 [메시징 API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)를 통해 단일 알림을 보낼 수 있습니다. 다음 필드를 테스트 케이스에 맞는 올바른 값으로 바꿔야 합니다:

필수 필드:

- `YOUR-API-KEY-HERE` - **설정** > **API 키**에서 사용할 수 있습니다. `/messages/send` REST API 엔드포인트를 통해 메시지를 발송할 수 있도록 키가 승인되었는지 확인합니다. 
- `EXTERNAL_USER_ID` - **사용자 검색** 페이지에서 사용할 수 있습니다.
- `REST_API_ENDPOINT_URL` - Braze [인스턴스]에 나열됩니다({{site.baseurl}}/api/basics/#endpoints. 엔드포인트 사용이 워크스페이스가 있는 Braze 인스턴스와 일치하는지 확인합니다.

{% alert note %}
[이전 탐색을]({{site.baseurl}}/navigation) 사용하는 경우 이러한 페이지는 다른 위치에 있습니다: <br>- **API 키는** **개발자 콘솔** > **API 설정에서** 찾을 수 있습니다. <br>- **사용자 검색**은 **사용자** > **사용자 검색**에 있음
{% endalert %}

선택적 필드:
- `YOUR_KEY1` (선택 사항)
- `YOUR_VALUE1` (선택 사항)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer YOUR-API-KEY-HERE" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://{REST_API_ENDPOINT_URL}/messages/send 
```

