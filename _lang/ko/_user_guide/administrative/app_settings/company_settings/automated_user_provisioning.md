---
nav_title: 자동화된 사용자 프로비저닝
article_title: 자동화된 사용자 프로비저닝
page_order: 10
page_type: reference
description: "이 참조 문서에서는 자동화된 사용자 프로비저닝을 위해 제공해야 하는 정보와 생성된 SCIM(System for Cross-domain Identity Management) 토큰을 사용하는 방법 및 위치에 대해 설명합니다."
alias: /scim/automated_user_provisioning/

---

# 자동화된 사용자 프로비저닝

> 자동화된 사용자 프로비저닝을 위해 제공해야 하는 사항과 생성된 SCIM(System for Cross-domain Identity Management) 토큰 및 SCIM API 엔드포인트의 사용 방법 및 위치에 대해 알아보세요. 그런 다음 API로 이 엔드포인트를 호출하여 새 대시보드 사용자를 자동으로 프로비저닝할 수 있습니다.

이 페이지에 액세스하려면 **설정** > **관리자 설정** > **SCIM 프로비저닝으로** 이동하세요.

## SCIM 토큰을 받는 방법

SCIM 토큰을 받으려면 다음 정보를 제공해야 합니다:

1. 새 대시보드 개발자를 추가할 기본 작업 영역을 선택합니다. [사용자 만들기 SCIM API 호출]({{site.baseurl}}/post_create_user_account/)에서 워크스페이스를 지정하지 않으면 여기에 워크스페이스가 추가됩니다.
2. 서비스 출처를 입력합니다. 서비스 출처는 Braze가 요청의 출처를 식별하는 방법입니다.
3. 선택 사항으로 쉼표로 구분된 목록 또는 SCIM 요청에 허용되는 IP 주소 범위를 입력합니다. 각 요청의 `X-Origin-Request` 헤더는 허용 목록에서 요청 IP 주소를 확인하는 데 사용됩니다.<br><br>

{% alert note %}
이 SCIM 엔드포인트는 ID 공급자와 직접 통합되지 않습니다.
{% endalert %}

![][1]

필수 필드를 완료하면 SCIM 토큰을 생성하고 SCIM API 엔드포인트를 확인할 수 있습니다. **이 토큰은 한 번만 증정됩니다.** Braze는 모든 SCIM 요청에 HTTP `Authorization` 헤더를 통해 첨부된 SCIM API 베어러 토큰이 포함될 것으로 예상합니다.

[1]: {% image_buster /assets/img/scim.png %}
