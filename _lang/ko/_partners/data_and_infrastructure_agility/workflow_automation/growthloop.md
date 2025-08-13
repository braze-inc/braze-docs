---
nav_title: GrowthLoop
article_title: GrowthLoop
description: "이 참조 문서에서는 데이터 웨어하우스에서 직접 고객 데이터를 세분화하여 Braze로 전송할 수 있는 플랫폼인 GrowthLoop와 Braze의 파트너십에 대해 설명합니다."
alias: /partners/growthloop/
page_type: partner
search_tag: Partner

---

# GrowthLoop

> [GrowthLoop](https://growthloop.com/)는 마케팅 팀이 클라우드 데이터 웨어하우스에서 Braze 및 기타 채널로 고객 데이터를 활성화할 수 있도록 지원합니다. 클라우드 데이터 웨어하우스에서 마케팅 프로그램을 자동화, 확장 및 측정하여 데이터를 중앙 집중식 단일 위치에 보관합니다.

_This integration is maintained by GrowthLoop._

## 통합 정보

Braze와 GrowthLoop의 통합을 통해 데이터 웨어하우스에서 직접 고객 데이터를 세분화하여 Braze로 전송할 수 있으므로 사용자는 단일 데이터 소스와 함께 Braze의 심층적인 기능 세트를 최적화할 수 있습니다. 고객 세분화 및 활성화를 위한 마케팅 노력을 간소화하여 Braze로 전송된 타겟팅 캠페인의 세분화, 실행, 테스트 및 결과 측정에 걸리는 시간을 단축합니다.

## 필수 조건 

| 요구 사항 | 설명 |
| ----------- | ----------- |
| GrowthLoop 성장 또는 기업 계정 | 이 파트너십을 활용하려면 GrowthLoop 계정이 필요합니다. |
| Braze Rest API 키 | 모든 권한이 있는 Braze REST API 키입니다.<br><br>Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL에][2] 따라 달라집니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## 사용 사례

데이터 웨어하우스의 고객 목록을 Braze로 전송하여 클릭 한 번으로 이메일 및 푸시 알림 캠페인을 타겟팅하고 항상 동기화 상태를 유지할 수 있습니다.

- 가입 활성화에 기반한 이메일 - 가입 흐름에서 이탈한 사용자를 활성 사용자로 전환하는 데 도움이 되는 이메일을 전송합니다.
- 모든 사용자 행동에 기반한 이메일 - "장바구니에 추가" 등의 사용자 행동을 기반으로 이메일을 보냅니다.
- 이탈한 고객에게 보내는 이메일 - 이탈한 고객에게 오퍼가 포함된 이메일을 통해 재참여를 유도합니다.

## 통합

### GrowthLoop에서 Braze 연결 구성하기

GrowthLoop 내에서 세분화 플랫폼에 로그인한 후 왼쪽 사이드바의 **대상** 탭으로 이동하여 오른쪽 상단에 있는 **새 대상**을 클릭합니다.

Braze를 찾을 때까지 스크롤한 다음, **Braze 추가**를 클릭합니다.

대상에 대한 연결을 구성하는 팝업이 나타납니다.

- **대상 이름**: 앞으로 앱에서 대상 이름을 지정하고 참조하는 방식
- **동기화 빈도**: 매일 또는 시간별 선택, 이를 통해 GrowthLoop가 Braze에 오디언스를 내보내는 빈도 제어
- **API 키**: 요구 사항에서 필요한 권한과 함께 생성된 API 키
- **API URL**: 요구 사항에 정의된 URL

**만들기를** 클릭하면 첫 번째 오디언스를 Braze로 내보낼 수 있습니다! GrowthLoop에서 오디언스를 생성하려면 [오디언스 생성](https://www.growthloop.com/help-center-articles/create-an-audience)을 참조하세요.

### 내보내기 후

오디언스를 내보낸 후 15분마다 GrowthLoop가 고객 목록의 업데이트 버전을 생성하여 Braze로 전송합니다.

동시에 GrowthLoop는 더 이상 자격이 없는 사용자를 오디언스에서 제거하고 자격이 있는 사용자를 오디언스에 새로 추가합니다. 

Braze는 사용자를 매칭하고 플래그를 생성하여 해당 사용자가 GrowthLoop 오디언스의 일원임을 표시합니다.

Braze에서 캠페인을 생성할 때 해당 GrowthLoop 오디언스에서 고객을 선택할 수 있습니다. 

## 문제 해결

자세한 정보나 지원이 필요하면 GrowthLoop 팀( solutions@growthloop.com )에 문의하세요.


[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
