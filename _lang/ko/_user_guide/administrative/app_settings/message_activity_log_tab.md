---
nav_title: 메시지 활동 로그
article_title: 메시지 활동 로그
page_order: 5
page_type: reference
description: "이 참고 문서에서는 캠페인 및 전송과 관련된 메시지를 보여주는 메시지 활동 로그에 대해 설명합니다. 여기에서 로그 메시지를 이해하는 방법에 대한 정보도 확인할 수 있습니다."

---

# 메시지 활동 로그 {#dev-console-troubleshooting}

> **메시지 활동 로그에서**는 캠페인 및 전송과 관련된 모든 메시지(특히 오류 메시지)를 확인할 수 있습니다.

API 캠페인 트랜잭션을 확인하고, 실패한 메시지에 대한 세부 정보를 해결하고, 알림 전송을 개선하거나 기존 기술 문제를 해결하는 방법에 대한 인사이트를 수집할 수 있습니다.

로그에 액세스하려면 **설정** > **메시지 활동 로그로** 이동합니다.

![Message Activity Log]({% image_buster /assets/img_archive/message_activity_log.png %})

{% alert tip %}
이 글 외에도 메시지 활동 로그를 사용하여 직접 문제 해결 및 디버깅을 수행하는 방법을 다루는 [품질 보증 및 디버깅 도구](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/) Braze 학습 과정도 확인해 보실 것을 권장합니다.
{% endalert %}

**메시지 활동 로그에** 기록된 다음 콘텐츠를 기준으로 필터링할 수 있습니다:

- 푸시 알림 오류
- 중단된 메시지 오류
- 웹훅 오류
- 메일 오류
- API 메시지 레코드
- 연결된 콘텐츠 오류
- REST API 연결 오디언스 오류
- 사용자 앨리어싱 오류
- A/B 테스트 오류
- SMS/MMS 오류
- WhatsApp errors
- Live Activity errors
- Bad user trigger errors

이러한 메시지는 Facebook 자체 시스템, 사용자의 앱 또는 플랫폼, 타사 파트너로부터 전송될 수 있습니다. 이로 인해 이 로그에 표시될 수 있는 메시지의 수가 무한대로 늘어날 수 있습니다.

## 로그 메시지 이해

문맥 단서를 사용하여 문제를 해결하는 데 도움이 될 수 있으므로 메시지의 의미를 파악하려면 각 메시지의 문구와 해당 열에 주의를 기울이세요. 

예를 들어, 로그 항목에 "empty-cart_app"라는 메시지가 있는데 그 의미가 무엇인지 잘 모르겠다면 왼쪽의 **유형** 열을 살펴보세요. If you see "Aborted Message Error", you can safely assume the message was what was written as the [abort message]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) using Liquid, and that the message was aborted because the intended recipient of the message had an empty cart in your app.

### 공통 메시지

몇 가지 일반적인 메시지 유형이 있으며, 일부 메시지는 문제를 진단하고 해결하는 데 도움이 되는 문제 해결 링크를 제공하기도 합니다.

다음 나열된 메시지는 예시용이며 로그의 **메시지** 열에 표시되는 내용과 정확히 일치하지 않을 수 있습니다.

| 메시지 유형 | 잠재적 메시지 | 설명 |
|---|---|---|
| 소프트바운스 | 이메일 주소 same@example.com 소프트 반송되었습니다. | 이메일 주소는 유효하며 이메일 메시지가 수신자의 메일 서버에 도달했지만 '일시적인' 문제로 인해 거부되었습니다. <br><br>일반적인 소프트 바운스 이유는 다음과 같습니다: {::nomarkdown} <ul> <li> 사서함이 꽉 찼습니다(사용자가 할당량을 초과했습니다). </li> <li> 서버가 다운되었습니다. </li> <li> 메시지가 너무 커서 수신자의 받은 편지함에 넣을 수 없습니다. </li>  </ul> {:/} 이메일이 소프트바운스된 경우 일반적으로 72시간 이내에 재시도하지만 재시도 횟수는 수신자마다 다릅니다. |
| 하드바운스 | 연결하려는 이메일 계정이 존재하지 않습니다. 수신자의 이메일 주소에 오타나 불필요한 공백이 있는지 다시 한 번 확인하세요. | 이 사람의 받은편지함에 메시지가 도착하지 않은 이유는 받은 편지함이 없기 때문입니다. 이러한 메시지의 경우 **세부정보 보기** 열에 수신자의 프로필을 볼 수 있는 링크가 있는 경우가 있습니다.|
| 블록 | 스팸 방지 정책으로 인해 스팸 메시지가 거부되었습니다. | 메시지가 스팸으로 분류되었습니다. 이 메일 오류는 ESP로부터 이메일이 삭제되었음을 나타내는 이벤트를 수신한 사용자에 대해 기록됩니다. 의도한 수신자에게만 해당되는 메시지일 수도 있지만, 이 메시지를 자주 받는다면 자신의 쪽지 보내기 습관이나 쪽지 내용을 다시 한 번 살펴볼 필요가 있습니다. Also, think back—did you [warm up your IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/)? 그렇지 않다면 Braze에 문의하여 진행에 대한 조언을 구하세요.|
| 중단된 메시지 오류 | empty-cart_web | 장바구니가 있는 앱이 있거나 Liquid에서 중단 메시지가 포함된 전송을 생성한 경우 전송이 중단된 경우 어떤 메시지가 반환되는지 사용자 지정할 수 있습니다. 이 경우 반환되는 메시지는 empty-cart_web입니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 내 메시지가 여기에 표시되지 않는 이유는 무엇인가요?

메시지 활동 로그의 메시지는 다양한 출처에서 올 수 있습니다: Braze, 앱 또는 플랫폼 또는 타사 파트너. 즉, 이 로그에 나타날 수 있는 메시지는 무한히 많으며, 상상할 수 있듯이 모든 메시지를 나열할 수는 없습니다!

예를 들어, 앞의 표에 나열된 메시지 외에 잠재적인 '차단' 메시지가 있을 수 있습니다.

- 안타깝게도 [_IP_ADDRESS_] ]로부터 메시지가 전송되지 않았습니다. 인터넷 서비스 제공업체의 일부 네트워크가 차단 목록에 있으므로 해당 서비스 제공업체에 문의하세요.
- 현지 정책으로 인해 메시지가 거부되었습니다.
- 수신자가 이 메시지를 스팸으로 차단했습니다.
- 서비스를 사용할 수 없음, 클라이언트 호스트 [_IP_ADDRESS_] ]가 스팸하우스를 사용하여 차단되었습니다.

## Storage retention period

Errors from the last 60 hours are available in the Message Activity Logs. Logs that are more than 60 hours old are cleaned and no longer accessible. 

### Number of error logs stored

The number of saved logs is influenced by several conditions. For example, if a scheduled campaign is sent to thousands of users, we would potentially see a sample of the errors in the Message Activity Log instead of all errors.

Here's an overview of conditions affecting how many logs will be saved:
- Up to 20 Connected Content error logs will be saved for the same campaign within one fixed clock hour.
- Up to 100 error logs of the same error type will be saved within one fixed clock hour per workspace for the following error types:
    - 중단된 메시지 오류
    - 웹훅 오류
    - 푸시 알림 오류
    - Live Activity errors
    - Bad user trigger errors

