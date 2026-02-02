---
nav_title: 킥박스
article_title: 킥박스
alias: /partners/kickbox/
description: "이 참고 문서에서는 이메일 목록을 검증하거나 애플리케이션에 인증을 통합하는 데 사용되는 이메일 인증 플랫폼인 Braze와 Kickbox 간의 파트너십에 대해 간략하게 설명합니다."
page_type: partner
search_tag: Partner
---

# 킥박스

> [Kickbox는](https://kickbox.com/) 이메일 데이터를 깨끗하고 전달 가능성 있게 유지하는 데 필요한 기능, 통합, 보안을 갖춘 올인원 이메일 인증 플랫폼입니다. Kickbox 통합은 전송을 누르기 전에 Kickbox 이메일 확인을 사용하여 배달할 수 없는 이메일 주소와 품질이 낮은 이메일 주소를 식별함으로써 Braze 캠페인의 전달 가능성을 향상시킵니다.

킥박스를 사용하면 Braze에서 고객 프로필이 업데이트되는 순간 사용자 이메일 주소의 유효성을 검사할 수 있습니다. 이는 프로필의 `email` 필드의 인구수에 따라 트리거되는 전용 캔버스 또는 캠페인 워크플로우를 통해 이루어집니다.

캔버스 또는 캠페인은 사용자의 이메일 주소를 공유하는 웹훅을 킥박스에 전송합니다. 킥박스는 이메일 주소의 유효성을 검사하고 Braze REST API 엔드포인트를 사용하여 품질을 자세히 설명하는 커스텀 속성으로 고객 프로필을 업데이트합니다.

## 필수 조건

| Requirement                           | 설명                                                                   |
| --------------------------------------|-------------------------------------------------------------------------------|
| 킥박스 계정                       | 이 통합 기능을 사용하려면 활성 Kickbox 계정이 필요합니다.                |
| Braze REST API 키   | A Braze REST API key with `users.track` permissions. <br><br>**설정** > **API 및 식별자** > **API 키로** 이동하여 Braze 대시보드에서 생성할 수 있습니다.|
| 통합에 대한 액세스 권한을 요청하세요.     | Kickbox 지원팀에 문의하여 Braze 통합에 대한 액세스 권한을 요청하세요.        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integration

Kickbox와 통합하려면 [Braze와 통합하기의](https://docs.kickbox.com/docs/integrating-with-braze#/) 단계를 따르세요.

## 사용 사례

### 대량 인증

또한 몇 달 또는 분기별로 전체 목록을 확인하여 고객이탈 이메일이나 시간이 지남에 따라 성능이 저하되어 전달 가능성이 서서히 떨어지는 목록을 방지할 수도 있습니다.

이렇게 하려면 킥박스에 설명된 대로 워크플로우의 **항목 설정** 설정을 변경해야 합니다. **실행 기반 전달을** 선택하는 대신 **예약을** 선택합니다. 그런 다음 목록을 한 번에 확인하도록 예약된 시간을 선택합니다.

### 검증된 세그먼트 만들기

킥박스의 커스텀 속성은 다음 예시와 같이 일관된 스키마를 가지고 있습니다.

{% raw %}
```json
   {
  "attributes": [
    {
      "email": "example1@kickbox.com",
      "_update_existing_only": true,
      "success": true,
      "code": null,
      "message": null,
      "result": "deliverable",
      "reason": "accepted_email",
      "role": false,
      "free": false,
      "disposable": false,
      "accept_all": false,
      "did_you_mean": null,
      "sendex": 1,
      "user": "example1",
      "domain": "kickbox.com"
    },
    {
      "email": "example2@gamil.com",
      "_update_existing_only": true,
      "success": true,
      "code": "44312",
      "message": "SMTP verification",
      "result": "undeliverable",
      "reason": "rejected_email",
      "role": false,
      "free": false,
      "disposable": false,
      "accept_all": false,
      "did_you_mean": "example2@gmail.com",
      "sendex": 0.23,
      "user": "example2",
      "domain": "gamil.com"
    }
  ]
}
```
{% endraw %}

즉, 이메일 주소가 확인된 사용자로 오디언스 세그먼트를 생성하여 캠페인과 캔버스의 전달 성공률을 높이고 이메일 서비스 공급업체와의 평판을 보호할 수 있습니다.

To do so, follow these steps:

1. Braze에서 **오디언스** > **세그먼트** > **세그먼트 만들기로** 이동합니다.
2. **필터 그룹** 섹션에서 **커스텀 속성** 필터를 추가하고 드롭다운에서 '결과'를 선택합니다. 

사용 사례에 따라 고객 프로필에 킥박스 커스텀 속성 "결과"가 존재하거나 해당 값이 "결과물"과 같은 세그먼트를 생성하는 것이 적절할 수 있습니다. 이 필터를 단독으로 사용하여 세그먼트를 만들거나 향후 모든 세그먼트의 일부로 만들어 그 안에 있는 모든 사용자를 검증할 수 있습니다. 