---
nav_title: Octolis
article_title: Octolis
description: "이 참조 문서에서는 데이터를 Braze에 통합할 수 있는 데이터 활성화 플랫폼인 Octolis와 Braze 간의 파트너십을 간략히 설명합니다."
alias: /partners/octolis/
page_type: partner
search_tag: Octolis

---

# Octolis

> [Octolis][0]는 강력한 데이터 활성화 플랫폼(또는 헤드리스 CDP)입니다. 보유한 데이터베이스를 기반으로 하는 Octolis는 비즈니스 도구에서 데이터를 통합, 준비, 점수화 및 동기화할 수 있는 손쉬운 방법입니다.

_This integration is maintained by Octolis._

## 통합 정보

Octolis와 Braze의 통합은 원시 데이터 소스와 Braze 사이의 미들웨어 역할을 하여 온라인과 오프라인의 다양한 소스에서 데이터를 검색하고 통합할 수 있게 해줍니다.
1. Eshop, CRM, POS 시스템 등의 소스에서 데이터 통합 및 결합
2. 정규화 및 점수화
3. 계산된 필드와 이벤트를 Braze에 실시간 동기화

![][7]

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Octolis 계정 | 이 파트너십을 이용하려면 Octolis 계정이 필요합니다. |
| Braze REST API 키 | [**users.track**][1] 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [당신의 REST 엔드포인트 URL][2]. 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
| Braze 앱 키 | 앱 식별자 키. **Braze 대시보드 > 설정 관리 > API 키**에서 찾을 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

통합을 시작하기 전에 연결, 소스, 오디언스 및 동기화에 대한 다음 섹션을 참조하세요.

자세한 내용은 Octolis [시작하기][4] 섹션을 참조하세요.

### 1단계: Octolis를 데이터 소스에 연결

Braze에 데이터를 전송하려면 [오디언스를][5] 하나 이상 생성했는지 확인해야 합니다. 오디언스는 여러 데이터 소스를 결합하고 준비 단계에 적용하며 계산된 필드를 추가합니다.

이러한 오디언스는 여러 데이터 소스를 기반으로 빌드해야 합니다. 소스는 다음 중 어느 것이든 될 수 있습니다:
- Salesforce 개체(연락처, 계정 등)
- Zendesk 개체(티켓)
- SFTP 내부의 파일(일부 연락처가 포함된 CSV 파일, 이벤트가 포함된 JSON 파일...)
- 데이터베이스의 테이블/보기입니다.
- 시스템 중 하나가 웹훅 또는 API 호출을 통해 레코드를 전송합니다.

### 2단계: Braze를 목적지로 추가

다음으로, Braze를 새 대상으로 설정하려면 기본 화면의 현재 대상 맨 위에서 **\+ 더 추가**를 선택하고 사용 가능한 비즈니스 툴에서 **Braze**를 선택합니다.

![][9]

선택한 후 다음을 입력합니다:

- Braze API 키: Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다.
- 기간: Octolis는 주어진 기간에 사용량 제한을 적용합니다.
- 요청 볼륨: 이 기간 내에 요청할 수 있는 요청 횟수입니다.
- 사용자 지정 속성: 여기에서 Braze에 전송할 새 필드와 해당 형식(문자열, 정수, 부동 소수점)을 지정하고, 이 중 하나를 동기화에 필수로 사용하려면 **동기화에 필요를** 체크합니다.

![][10]

구성 후 Braze가 홈 화면에 새 대상으로 표시됩니다.

### 3단계: 새 동기화 만들기

메뉴에서 **동기화**를 클릭하고 오른쪽 상단에서 **동기화 추가**를 선택합니다. 이전에 생성한 오디언스 중에서 선택하려는 오디언스를 선택합니다.
그런 다음, 데이터를 전송할 대상과 엔티티로 **Braze**를 선택합니다.

![][11]

### 4단계: 출력 설정 설정

기본적으로 Braze는 전송할 모든 속성을 생성하지만 동기화할 필드 목록은 사용자가 문서화해야 합니다.

![][12]{: style="max-width:75%;"}

다음은 설정 필드에 대한 구체적인 정의입니다.

| 필드 | 설명 |
| --- | --- |
| 오디언스를 어디에 동기화하나요? | The Braze entity where you will create or update records. |
| 레코드를 식별하는 데 사용되는 필드는 무엇인가요? | 이 필드는 Braze에 이미 존재하는 경우 Octolis를 사용하여 레코드를 식별합니다. |
| 각 레코드를 얼마나 자주 전송하나요? | 기본적으로 동기화는 모든 통합(API, 데이터베이스, FTP)에서 증분 방식으로 이루어집니다. 즉, 마지막 업데이트 이후의 새로운 값만 업데이트됩니다. 필요한 경우 전체 테이블을 일정한 간격으로 전송할 수도 있습니다. 시작 시 Octolis가 전체 테이블을 전송합니다. |
| 어떤 필드를 동기화해야 하나요? | Octolis에서 Braze 필드로 매핑. 모든 사용 가능한 필드의 목록이 드롭다운 메뉴에 나타납니다. 계산된 필드를 Braze로 보내려면 먼저 Braze 엔티티 내에서 해당 열을 생성했는지 확인해야 합니다. |
| 언제 오디언스를 동기화하길 원하나요? | 데이터를 Braze로 전송하는 방법: 수동, 실시간 또는 프로그래밍.  |
| 레코드에 대한 다음 작업에서 동기화... | 만들기: 옵트인의 경우 Braze 테이블이 마스터로 유지되는 것이 중요합니다. 필드가 업데이트될 때 Octolis가 동기화를 트리거하지 않도록 합니다.<br><br>업데이트: 반면에 이름 필드의 경우, 예를 들어 고객이 새 항목을 제공할 때마다 Braze 테이블의 필드를 업데이트할 수 있기를 원합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 다중 키 중복 제거

중복 제거는 특히 온라인과 오프라인의 여러 소스에서 데이터를 조정할 때 중요한 과제입니다. Octolis의 고급 노코드 모듈을 통해 [중복 제거][3]를 위한 여러 키를 사용할 수 있습니다. 이 모듈은 각 마스터 테이블에서 사용할 수 있으므로 각 엔티티에 맞게 로직을 조정할 수 있습니다.


[0]: http://octolis.com
[1]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: https://help.octolis.com/resources/faq/what-is-deduplication-and-how-does-it-work
[4]: https://help.octolis.com/
[5]: https://help.octolis.com/audiences/create-a-no-code-audience
[6]: {{site.baseurl}}/api/api_limits/
[7]: {% image_buster /assets/img/Octolis/Braze_scheme.png %}
[8]: {% image_buster /assets/img/Octolis/Braze_screen1.png %}
[9]: {% image_buster /assets/img/Octolis/Braze_screen2.png %}
[10]: {% image_buster /assets/img/Octolis/Braze_screen3.png %}
[11]: {% image_buster /assets/img/Octolis/Braze_screen4.png %}
[12]: {% image_buster /assets/img/Octolis/Braze_screen5.png %}
