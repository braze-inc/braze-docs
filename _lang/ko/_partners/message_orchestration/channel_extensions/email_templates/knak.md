---
nav_title: Knak
article_title: Knak
alias: /partners/knak/
description: "이 참고 문서에서는 며칠 또는 몇 주가 아닌 몇 분 또는 몇 시간 만에 완벽하게 반응하는 이메일을 만들고 바로 사용할 수 있는 Braze 템플릿으로 내보낼 수 있는 캠페인 제작 플랫폼인 Braze와 Knak의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Knak

---

# Knak

> [Knak][1]는 엔터프라이즈 마케팅 팀을 위해 사내용으로 최초로 제작된 캠페인 제작 플랫폼입니다. 드래그 앤 드롭 방식의 플랫폼이므로 별다른 코딩이나 외부 도움 없이도 누구나 몇 분 내에 브랜드 이미지에 맞는 매력적인 이메일과 랜딩 페이지를 제작할 수 있습니다.

_This integration is maintained by Knak._

## 통합 정보

Braze와 Knak의 통합을 통해 며칠 또는 몇 주가 아닌 몇 분 또는 몇 시간 만에 완벽하게 반응하는 이메일을 작성하고 바로 사용할 수 있는 Braze 템플릿으로 내보낼 수 있습니다. Knak은 외부 에이전시나 수작업 코딩 없이도 Braze에서 관리하는 캠페인의 이메일 작성 수준을 높이고자 하는 마케터를 위해 만들어졌습니다. 

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Knak 계정 | 이 파트너십을 이용하려면 Knak 계정이 필요합니다. |
| Braze REST API 키 | 전체 **템플릿** 권한이 있는 Braze REST API 키입니다. <br><br>Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [당신의 REST 엔드포인트 URL][2]. 사용자의 엔드포인트는 인스턴스를 위한 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

Knak은 코딩이나 외부의 도움 없이도 이메일 작성의 수준을 높이고자 하는 마케터를 위해 구축되었습니다. 다음 사용자에게 적합합니다.
- 현재 이메일에 간단한 템플릿을 사용하고 있으며, 이메일의 수준을 높이고 싶은 사람
- 외부 대행사나 개발자에게 Braze용 이메일 제작을 의뢰하세요.
- 에셋 제작에 대한 창의적인 통제권을 되찾고 시장 출시 기간을 단축하고 싶으신가요?

## 통합

### 1단계: 통합 구성

Knak에서 **통합 > 플랫폼 > + 새 통합 추가**로 이동합니다.

![통합 버튼 추가][5]

그런 다음, **Braze** 플랫폼을 선택하고 Braze API 키와 REST 엔드포인트를 제공합니다. **새 통합 생성**을 클릭하여 통합을 완료합니다. 

![새 통합 만들기][6]

### 2단계: Knak 템플릿 동기화

Knak에서 Braze에 동기화하려는 이메일을 찾아 **게시**를 선택한 다음, **동기화**를 선택합니다.

![Knak 통합 1][8]

그런 다음 이메일 이름을 확인하고 **동기화를** 클릭합니다.

![Knak 통합 2][9]

## 통합 사용

업로드한 Knak 이메일은 Braze의 **인게이지먼트 > 템플릿 및 미디어**에서 찾을 수 있습니다. 아름답고, 브랜드에 부합하며, 반응성이 뛰어납니다. 유일한 한계는 여러분의 창의력입니다!


[1]: https://knak.com/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[5]: {% image_buster /assets/img/knak/integration-setup-step-2-add-new-integration.png %}
[6]: {% image_buster /assets/img/knak/integration-setup-step-4-add-api-key.png %}
[8]: {% image_buster /assets/img/knak/integration-post-step-1-sync.png %}
[9]: {% image_buster /assets/img/knak/integration-post-step-2-asset-name.png %}