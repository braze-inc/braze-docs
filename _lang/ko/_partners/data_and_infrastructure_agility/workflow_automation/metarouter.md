---
nav_title: MetaRouter
article_title: MetaRouter
description: "MetaRouter를 사용하여 Braze에서 고객 데이터 관리를 개선합니다. 이 고성능 서버 측 태그 관리 솔루션은 MetaRouter 호스팅 프라이빗 클라우드 또는 자체 인프라에서 원활한 배포 옵션을 통해 규정 준수 및 제어 기능을 극대화합니다."
alias: /partners/MetaRouter/
page_type: partner
search_tag: Partner
---

# MetaRouter

> [MetaRouter](https://www.metarouter.io/)는 강력한 서버 측 태그 관리 플랫폼으로 원활하게 통합되어 Braze의 경험을 개선합니다. 30%까지 보강된 신뢰할 수 있는 완전한 퍼스트파티 데이터 수집부터 개인화된 여정을 위한 실시간 이벤트 스트림 활성화까지, Braze 내에서 전체 고객 데이터 여정을 오케스트레이션할 수 있습니다. 또한 MetaRouter는 Braze 태그나 기타 서드파티 태그가 필요하지 않으므로 구현을 간소화하여 Braze로 유입되는 데이터를 매개변수 단위로 정밀하게 제어할 수 있습니다.

_This integration is maintained by Metarouter._

## 지원되는 기능

- 재시도 기능이 내장되어 있습니다.
- 요청이 배치 처리됩니다.
- 사용량 제한조치 문제는 재시도로 처리됩니다.
- 외부 ID 및 PII가 지원됩니다. MetaRouter는 클라이언트가 원하는 익명 ID와 PII(이메일, 전화번호, 이름)를 전달합니다.
- Braze 구매 및 사용자 지정 이벤트 데이터를 전송할 수 있습니다.
  - 이벤트 속성이 지원됩니다.
  - 중첩된 이벤트 속성은 지원되지 않습니다.

## 필수 조건

시작하기 전에 다음이 필요합니다:

| 요구 사항           | 설명                                                                                                                                          |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| MetaRouter 계정  | [MetaRouter Enterprise 계정](https://enterprise.metarouter.io/).                                                                                |
| Braze REST API 키    | `users.track` 권한이 있는 Braze REST API 키. 생성하려면 **설정** > **API 키로** 이동합니다.                                                |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). 사용자의 엔드포인트는 인스턴스를 위한 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## MetaRouter 설정

Braze 통합을 위해 MetaRouter를 설정하려면 다음을 수행합니다.

1. MetaRouter로 이동하여 새 클러스터를 생성합니다.
2. 추적할 이벤트를 선택합니다.
3. MetaRouter SDK를 설치하고 웹사이트에 이벤트를 통합합니다.
4. 클러스터를 웹사이트의 UI에 연결합니다.
5. 새 파이프라인을 만듭니다.
6. 웹사이트가 MetaRouter로 이벤트를 전송하고 있는지 확인합니다.

## Braze 통합

### 1단계: Braze 통합 추가

Enterprise MetaRouter에서 **통합** > **새 통합** > **Braze**를 선택한 다음, 통합의 이름을 지정합니다. 다음으로, 인스턴스 URL과 API 키를 입력한 다음, **변경 사항 적용**을 선택합니다.

![MetaRouter에서 Braze를 통합으로 추가.]({% image_buster /assets/img/metarouter/img1.png %}){: style="max-width:50%;"}

### 2단계: 이벤트 매핑 추가

각 ID 출력에 대한 이벤트 매핑을 추가한 다음, Braze로 전송할 이벤트를 구성합니다. 완료했으면 **새 수정본으로 저장**을 선택합니다.

![각 ID 출력에 대한 이벤트 매핑을 추가합니다.]({% image_buster /assets/img/metarouter/img2.png %})

