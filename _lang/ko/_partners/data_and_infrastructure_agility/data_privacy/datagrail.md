---
nav_title: DataGrail
article_title: DataGrail
description: "이 참고 문서에서는 Braze와 개인정보 관리 플랫폼인 DataGrail의 파트너십을 간략하게 설명하며, 이를 통해 Braze 내에서 수집 및 저장된 소비자 데이터를 감지하여 DSR을 신속하게 처리할 수 있습니다."
alias: /partners/datagrail/
page_type: partner
search_tag: Partner

---

# DataGrail

> 개인정보 관리 플랫폼인 [DataGrail](https://www.datagrail.io/)은 소비자의 신뢰를 구축하고 비즈니스의 위험 요소를 제거하는 데 도움이 됩니다. 지속적인 시스템 감지 및 자동화된 데이터 주체 요청(DSR) 이행을 통해 DataGrail은 개인정보 보호 프로그램을 강화하여 GDPR, CCPA, CPRA 등 진화하는 개인정보 보호법 및 규정을 준수할 수 있도록 지원합니다. 

_This integration is maintained by DataGrail._

## 통합 정보

Braze와 DataGrail의 통합을 통해 Braze 내에서 수집 및 저장된 소비자 데이터를 감지하여 DSR(액세스, 삭제 및 판매 금지 요청)을 신속하게 처리할 수 있습니다. 자동화된 데이터 매핑을 통해 조직에서 상주하는 소비자 데이터의 정확한 청사진에 Braze를 추가합니다. 그러면 개인정보 보호 프레임워크를 유지 관리하거나 처리 활동 기록(RoPA)을 생성하기 위해 더 이상 설문조사나 스프레드시트를 작성할 필요가 없습니다. 

## 필수 조건

| 요구 사항 | 설명 |
|---|---|
| DataGrail 계정 | 이 파트너십을 활용하기 위한 DataGrail 계정입니다.<br>통합과 관련된 문제나 질문이 있는 경우 관리자에게 문의하거나 이메일(support@datagrail.io)로 문의하세요. |
| Braze API 키 | `events.list`, `users.export.ids`, `users.delete`, `users.track` 권한이 있는 Braze REST API 키.<br><br>Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| 브레이즈 인스턴스 | Braze 인스턴스는 Braze 온보딩 매니저로부터 가져오거나 [API 개요 페이지]({{site.baseurl}}/api/basics/#endpoints)에서 찾을 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

DataGrail 포털에 로그인하고 Braze의 통합 페이지에서 **연결을** 선택합니다. 그런 다음 인스턴스와 Braze API 키를 입력하고 **Braze 연결을** 선택합니다.

통합할 Braze 계정이 추가로 있는 경우:
1. Braze의 연동 페이지에서 **연결 수정을** 선택합니다.
2. 드롭다운에서 **+새 연결 추가를** 선택합니다.
3. **연결 이름** 아래에 이 별도의 계정을 식별할 수 있는 새 이름을 입력합니다(예: Braze 교육 계정).
4. 이 새 계정에 대해 별도의 Braze 인스턴스와 API 키를 입력합니다.
5. **연결을** 선택합니다.

통합과 관련된 문제나 질문이 있는 경우 DataGrail에 이메일(support@datagrail.io)로 문의하세요.

