---
nav_title: Nift
article_title: Nift
description: "이 참조 문서에서는 기업의 고객 확보, 참여, 유지에 도움을 주는 양방향 플랫폼인 Nift와 Braze 간의 파트너십을 간략히 설명합니다."
alias: /partners/nift/
page_type: partner
search_tag: Partner

---

# Nift

> [Nift](https://gonift.com/)는 기업의 고객 확보, 참여, 유지를 지원합니다. 양면 플랫폼을 통해 파트너는 Nift 기프트 카드로 고객에게 감사의 마음을 전할 수 있습니다. 고객에게 감사를 표하면 고객의 생애주기 가치가 높아지고 매출이 증가합니다.

_This integration is maintained by Nift._

## 통합 정보

Braze와 Nift의 통합을 통해 고객 생애주기의 중요한 순간에 Nift 선물이 포함된 '감사' 메시지를 자동으로 트리거하고 어떤 고객이 선물을 사용했는지 파악할 수 있습니다. Nift 기프트 카드는 Nift의 매치메이킹 기술에 의존하는 브랜드가 제공하는 제품과 서비스에 액세스하여 대규모로 비용 효율적으로 신규 고객을 확보하는 데 사용할 수 있습니다.

## 필수 조건

| 요구 사항 | 설명 |
|---|---|
| Nift 계정 | 이 파트너십을 이용하려면 Nift 계정이 필요합니다. |
| Braze REST API 키 | 모든 사용자 데이터 권한이 있는 Braze REST API 키입니다. <br><br> 이것은 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의]({{site.baseurl}}/api/basics/#endpoints) Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: Nift에서 Braze에 연결

[Nift 대시보드][2]를 방문하여 **계정** > **통합** > **Braze**로 이동한 다음, **연결**을 클릭합니다.

### 2단계: Braze 자격 증명 추가

**Braze 계정 연결** 페이지에서 Braze REST API 키를 제공하고 [인스턴스]({{site.baseurl}}/api/basics/#endpoints)의 Braze URL에 따라 달라지는 Braze 엔드포인트를 선택합니다.

고객에게 전송된 추천 링크에서 고객 ID 매개변수 이름을 변경할 수 있습니다. Nift는 고객이 당사 브랜드 중 하나에서 선물을 선택했을 때 이를 사용하여 Braze에서 처리된 것으로 표시합니다.

**계정 연결**을 클릭합니다.

![사용자에게 Braze API 키와 Braze 대시보드 URL을 입력하라는 프롬프트를 표시하는 'Nift 서비스 통합 페이지'.][5]

## 통합 사용

연동 기능을 사용하려면 메시지에 추천 링크를 배포하세요. 고객이 추천 링크를 사용하여 당사 브랜드 중 하나에서 선물을 선택하면, Nift는 해당 선물을 Braze에서 처리된 것으로 표시합니다.

Braze와 통합한 후 Nift는 다음 데이터와 함께 기존 고객 Braze 레코드에 자동으로 이벤트를 푸시합니다.

- 이벤트 이름: `nift_processed`
- 시간: 고객이 선물을 선택/사용한 시간



[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.gonift.com/users/sign_in
[5]: {% image_buster /assets/img/nift/link_your_braze_account.png %}
[6]: {% image_buster /assets/img/nift/braze_account_linked.png %}