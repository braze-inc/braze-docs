---
nav_title: NPAW
article_title: NPAW
alias: /partners/npaw/
description: "이 참고 문서에서는 주요 온라인 미디어 전문가에게 실행 가능한 인사이트를 제공하는 지능형 데이터 분석 플랫폼인 Braze와 NPAW의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner
hidden: true

---

# NPAW

> [NPAW](https://nicepeopleatwork.com/)(_Nice People at Work_라고도 함)는 주요 온라인 미디어 전문가에게 유용한 인사이트를 제공하는 지능형 데이터 분석 플랫폼입니다. 이제 Braze 고객은 NPAW의 YOUBORA 도구 제품군을 통해 예측적이고 강력한 AI를 활용하여 고객 행동을 더 잘 이해하고 여러 플랫폼에서 참여를 유도할 수 있습니다.

# 전제 조건

| 요구 사항   |Origin| 설명 |
| --------------|------|-------------|
| YOUBORA API 키 |[YOUBORA 설정](https://youbora.nicepeopleatwork.com/users/login)|사용자 가입 시 생성되는 API 키는 **설정**에서 찾을 수 있습니다. |
| ID |[Braze 설정](https://dashboard.braze.com/sign_in) | YOUBORA는 ***Braze ID***, ***외부 사용자 ID*** 또는 ***사용자 ID***를 통해 소프트웨어를 Braze에 연결할지 여부를 선택할 수 있는 옵션을 제공합니다. |
| 엔드포인트 |[Braze 설정](https://dashboard.braze.com/sign_in)| Braze 대시보드를 통해 완전히 사용자 지정 가능한 URL 엔드포인트를 구성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

# 애널리틱스 통합

## 연동 페이지에 액세스하기

YOUBORA 도구 모음 계정에 로그인한 후 드롭다운 계정 메뉴에서 **연동** 옵션을 선택하여 연동 페이지로 이동합니다.

![NPAW 드롭다운]({% image_buster /assets/img/npaw_dropdown.png %})

## 통합 구성

통합 페이지에 액세스한 후 다음 옵션을 찾을 때까지 아래로 스크롤합니다.
**Braze** 통합 옵션을 참조하세요. 이 옵션을 클릭하면 확장되고 작성해야 하는 여러 필수 매개변수가 제공됩니다.

![NPAW 통합]({% image_buster /assets/img/npaw_integration.png %})

필수 조건 섹션에서 수집한 적절한 정보로 세부 정보를 입력합니다. 여기서,
* **커넥터 이름**은 향후 이 통합을 참조하는 데 사용되는 **영숫자** 문자열입니다. 이 값은 문자와 숫자**만** 포함하는 한 원하는 값으로 설정할 수 있습니다.
* **사용자 ID** 는 이전에 YOUBORA 소프트웨어와 Braze 계정을 연결하기 위해 선택한 ID입니다. 예를 들어, **Braze ID를** 통해 링크를 수행하기로 선택한 경우 드롭다운에서 **Braze ID를** 선택하여 적절한 필드에 값을 할당합니다.
* **API 키**는 이전에 **설정**의 **API** 섹션에서 찾은 YOUBORA 툴 스위트 API 키입니다.
* **엔드포인트**는 이전에 Braze 대시보드 내에서 설정했던 사용자 지정 가능한 URL 엔드포인트입니다.

모든 필드를 작성했으면 **연결** 버튼을 클릭하여 연결을 설정하고 변경 사항을 저장하기만 하면 됩니다.

## NPAW 통합 사용

Braze와의 통합 구성을 완료했으면 **사용자** 제품으로 이동하고 **섹션 매니저**에서 **샘플 매니저**를 선택합니다.

**샘플 매니저**에서 생성한 후 오른쪽에 있는 점 3개 아이콘을 클릭하면 샘플에 포함된 모든 사용자를 Braze로 전송할 수 있습니다.

![NPAW 샘플 관리자]({% image_buster /assets/img/npaw_sample_manager.png %})

이제 사용자를 Braze로 전송한 후, 비활성 사용자를 재참여시키거나 가장 충성도가 높은 사용자에게 연락하거나 모든 사용자 세그먼트에서 작업을 수행하도록 조치를 취하고 캠페인에 집중할 수 있습니다!
