---
nav_title: 사용자 프로비저닝 자동화
article_title: 사용자 프로비저닝 자동화
page_order: 10
page_type: reference
description: "이 참조 문서에서는 사용자 프로비저닝 자동화를 위해 제공해야 하는 정보 및 생성된 SCIM(시스템 간 ID 관리) 토큰을 사용하는 방법과 위치에 대해 설명합니다."
alias: /scim/automated_user_provisioning/

---

# 사용자 프로비저닝 자동화

> SCIM 프로비저닝을 사용하여 API를 통해 자동으로 Braze 사용자를 생성하고 관리하세요. 이 도움말에서는 제공할 정보, SCIM 토큰을 생성하는 방법, SCIM API 엔드포인트를 찾을 수 있는 위치를 안내합니다.

## 1단계: SCIM 권한 부여 설정에 액세스

Braze 대시보드에서 **설정** > **관리자 설정** > **SCIM 프로비저닝으로** 이동합니다.

## 2단계: SCIM 설정 구성

SCIM 프로비저닝을 인에이블하려면 다음 정보를 제공하세요:

- **기본값 워크스페이스:** 새 사용자가 기본값으로 추가될 워크스페이스를 선택합니다. [SCIM API 요청에]({{site.baseurl}}/post_create_user_account/) 워크스페이스를 지정하지 않으면 Braze는 이 워크스페이스에 사용자를 할당합니다.
- **서비스 출처:** SCIM 요청의 오리진 도메인을 입력합니다. Braze는 `X-Request-Origin` 헤더에서 이를 사용하여 요청이 어디에서 오는지 확인합니다.
- **IP 허용 목록(선택 사항):** SCIM 요청을 특정 IP 주소로 제한할 수 있습니다.
허용할 IP 주소의 쉼표로 구분된 목록 또는 범위를 입력합니다. 각 요청의 `X-Request-Origin` 헤더는 허용 목록에서 요청 IP 주소를 확인하는 데 사용됩니다.

{% alert note %}
이 SCIM 엔드포인트는 ID 공급자와 직접 통합되지 않습니다.
{% endalert %}

세 개의 필드가 있는 SCIM 프로비저닝 설정 양식입니다: 기본값인 워크스페이스, 서비스 오리진 및 선택 사항인 IP 허용 목록. "SCIM 토큰 생성" 버튼이 비활성화됩니다.]({% image_buster /assets/img/scim_unfilled.png %})

## 3단계: SCIM 토큰 및 엔드포인트 받기

필수 입력란을 완료한 후 SCIM **토큰 생성을** 눌러 SCIM 토큰을 생성하고 SCIM API 엔드포인트를 확인합니다. 이동하기 전에 SCIM 토큰을 복사해 두세요. **이 토큰은 한 번만 증정됩니다.** 

마스킹된 값과 복사 버튼이 표시된 SCIM API 엔드포인트 및 SCIM 토큰 필드. 토큰 필드 아래에는 '토큰 재설정' 버튼이 있습니다.]({% image_buster /assets/img/scim.png %})

Braze는 모든 SCIM 요청에 HTTP `Authorization` 헤더를 통해 첨부된 SCIM API 베어러 토큰을 포함할 것으로 예상합니다.

