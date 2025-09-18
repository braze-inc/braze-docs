---
nav_title: WSC Sports
article_title: WSC Sports
description: "이 참고 문서에서는 Braze 푸시 알림에 풍부하고 강력한 스포츠 미디어를 포함할 수 있는 스포츠 동영상 플랫폼인 Braze와 WSC Sports의 파트너십에 대해 설명합니다."
alias: /partners/wsc_sports/
page_type: partner
search_tag: Partner

---

# WSC Sports

> [WSC 스포츠][1] 플랫폼은 모든 디지털 플랫폼과 모든 스포츠 팬을 위한 맞춤형 스포츠 동영상을 자동으로 실시간으로 생성합니다. 

_이 통합은 WSC 스포츠에서 유지 관리합니다._

## 통합 정보

Braze와 WSC 스포츠의 통합을 통해 풍부하고 강력한 스포츠 미디어를 Braze 푸시 알림에 포함할 수 있습니다. 

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| WSC 계정 | 이 파트너십을 이용하려면 WSC 계정이 필요합니다. |
| Braze REST API 키 | **메시지**, **세그먼트**, **캠페인** 및 **캔버스** 권한이 있는 Braze REST API 키입니다. <br><br> 이는 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

WSC 스포츠 애플리케이션은 동영상 선택부터 최종 사용자의 디바이스에 푸시 알림이 도착하는 순간까지 엔드투엔드 프로세스를 처리합니다. 

### 1단계: 보내기 설정 선택

![][2]{: style="float:right;max-width:25%;margin-bottom:15px;"}

통합을 시작하기 전에, 원하는 캠페인과 사용자 세그먼트가 Braze에 구축되어 있는지 확인하세요. 완료되면 WSC 스포츠 플랫폼에서 원하는 동영상을 선택하고 전송 설정에서 사용하고자 하는 Braze 사용자 세그먼트와 캠페인 ID를 선택합니다. 마지막으로, 푸시 메시지를 전송할 시간을 선택합니다. 

#### API 호출

푸시 알림이 전송되면 WSC 스포츠는 선택한 옵션에 따라 다음 Braze 엔드포인트를 사용하여 선택한 사용자 세그먼트에 푸시 알림을 전달합니다:
- [/messages/schedule/create]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages#create-scheduled-messages)
- [/messages/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#sending-messages-immediately-via-api-only)

결과 메시지 본문은 다음과 같습니다: 
```
{
  "apple_push": {
    "alert": {
      "body": "Push Message Title"
    },
    "asset_url": "internalURI.mp4",
    "asset_file_type": "mp4"
  }
}
```

### 2단계: 테스트 보내기

이 시점에서 캠페인을 테스트하고 전송할 준비가 된 것입니다. 오류가 발생하면 Braze 오류 메시지 로그를 확인하세요. 


[1]: https://wsc-sports.com/
[2]: {% image_buster /assets/img/wsc_sports/braze_integration.jpg %} "braze_integration.jpg"
