---
nav_title: ViralSweep
article_title: ViralSweep
alias: /partners/viralsweep/
description: "이 참고 문서에서는 브랜드가 경품, 콘테스트, 즉석 당첨, 대기자 명단, 추천 프로모션 등과 같은 디지털 마케팅 프로모션을 구축, 실행 및 관리할 수 있는 소프트웨어 서비스인 Braze와 ViralSweep 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# ViralSweep

> [ViralSweep](https://viralsweep.com)는 브랜드에서 추첨, 콘테스트, 즉석 당첨, 대기자 명단, 추천 프로모션 등의 디지털 마케팅 캠페인을 개발하고 실행하며 관리할 수 있도록 지원하는 소프트웨어 서비스입니다. 

_This integration is maintained by ViralSweep._

## 통합 정보

Braze와 ViralSweep의 통합을 통해 ViralSweep 플랫폼에서 경품 행사와 콘테스트를 개최하고(이메일 및 SMS 목록을 늘리고), 캠페인이나 캔버스에서 사용할 경품이나 콘테스트 참가 정보를 Braze로 전송할 수 있습니다. 

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| ViralSweep 계정 | 이 파트너십을 이용하려면 비즈니스 플랜을 사용하는 ViralSweep 계정이 필요합니다. |
| Braze REST API 키 | 모든 사용자 데이터 및 이메일 권한이 포함된 Braze REST API 키입니다. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
|Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의]({{site.baseurl}}/api/basics/#endpoints) Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계 : ViralSweep 내에서 Braze에 연결하기

ViralSweep에서 **통합 > 이메일 및 SMS > 서비스 추가**로 이동하고 **Braze**를 선택합니다. 

![][1]

### 2단계 : Braze 자격 증명 추가

통합 구성 창에서 Braze REST API 키와 REST 엔드포인트를 제공합니다. 제공하는 엔드포인트에 `https://`(예: `dashboard-03.braze.com`)가 포함되지 않았는지 확인합니다. 

![사용자에게 Braze API 키와 Braze 대시보드 URL을 입력하라는 메시지가 표시되는 ViralSweep 서비스 통합 페이지입니다.][2]{: style="max-width:40%;"}

**연결**을 클릭합니다.

### 3단계 : Braze 자격 증명 추가
연결되었습니다! 이제 프로모션이 Braze에 연결되며 ViralSweep에서 수집한 모든 항목이 자동으로 Braze로 전송됩니다.

## 자주 묻는 질문

### ViralSweep은 어떤 필드를 Braze에 전달하나요?
- 이름
- 성
- 이메일 주소
- 주소
- 주소 2
- 도시
- 상태
- 우편번호
- 국가
- 생년월일
- 전화
- 프로모션 ID
- 추천 링크
- 추적 캠페인 이름

### ViralSweep은 구독자를 업데이트하나요?
예. 프로모션을 진행하여 ViralSweep이 누군가를 Braze에 전달한 후 나중에 다른 프로모션을 진행하여 같은 사람이 참가하는 경우, 그 사람의 정보는 자동으로 Braze에 업데이트됩니다(새로운 정보가 제공된 경우). 주로 추천 URL은 입력한 각 프로모션의 최신 URL로 업데이트되며, 프로모션 ID 필드에는 입력한 모든 프로모션의 ID가 포함됩니다.

## 문제 해결

Braze에 연결했는데 데이터가 계정에 추가되지 않는다면 그 이유가 있을 수 있습니다:

- **이메일이 이미 Braze에 존재합니다.**<br>
프로모션에 입력한 이메일 주소는 이미 Braze 계정에 있을 수 있으므로 다시 추가되지 않으며, 해당 연락처에 대한 새 정보가 제공될 경우에만 업데이트됩니다.<br><br>
- **이미 ViralSweep에 입력된 이메일**<br>
프로모션에 입력한 이메일 주소는 이미 이전에 입력한 적이 있으므로 Braze에 다시 전달되지 않습니다. 이미 프로모션에 참가한 후에 Braze 연동 기능을 설정한 경우 이러한 문제가 발생할 수 있습니다.


[1]: {% image_buster /assets/img/viralsweep/connect.gif %}
[2]: {% image_buster /assets/img/viralsweep/connect2.png %}
