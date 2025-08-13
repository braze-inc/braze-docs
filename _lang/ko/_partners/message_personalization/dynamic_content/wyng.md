---
nav_title: Wyng
article_title: Wyng
description: "이 참조 문서에서는 제로파티 데이터 플랫폼인 Wyng와 Braze 간의 파트너십을 설명합니다. 이를 통해 고객 선호도와 속성을 마이크로 경험, 고객 선호도 포털 및 API 플랫폼을 활용하여 쉽게 수집, 사용 및 통합할 수 있습니다."
alias: /partners/wyng/
page_type: partner
search_tag: Partner
---

# Wyng

> [Wyng][0]은 대화형 디지털 경험(즉, 퀴즈, 환경설정 센터, 프로모션 등)을 손쉽게 구축할 수 있습니다. 이를 통해 소비자와 적시에 교류하고 고객의 선호도와 기타 제로파티 데이터를 수집하며 실시간으로 개인화할 수 있습니다.

_이 통합은 Wyng에서 유지 관리합니다._

## 통합 정보

Braze 및 Wyng 통합을 통해 Wyng 경험으로 얻은 제로파티 데이터를 활용하여 Braze 캠페인 및 Braze 캔버스에서 상호 작용을 개인화할 수 있습니다. Wyng은 또한 선호도 센터를 운영할 수 있어 소비자가 귀하의 브랜드와 공유하는 데이터 및 선호도(통신 선호도 포함)를 제어할 수 있습니다.

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Wyng 계정 | 이 파트너십을 활용하려면 Wyng 계정이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: Braze 통합을 연결하십시오

Wyng에서 [**Integrations**][1]로 이동하여 **Add** 탭을 선택합니다. 다음으로, **Braze** 위로 마우스를 가져가서 통합을 위해 **Connect**를 클릭합니다.

![Wyng 플랫폼의 Braze 파트너 타일.][2]{: style="max-width:80%;"}

### 2단계: Braze 커넥터를 구성합니다

1. 열리는 구성 창에서 Braze REST API 키를 입력하세요.
![자격 증명 프롬프트 모습을 보여주는 이미지.][4]{: style="max-width:80%;"}<br><br>
2. 다음으로, 드롭다운을 사용하여 Braze와 공유할 Wyng 캠페인을 선택합니다.![Braze와 공유할 Braze 커넥터를 선택하라는 프롬프트를 보여주는 기존 Wyng 캠페인 이미지.][5]{: style="max-width:80%;"}<br><br>
3. 다음으로, 가입, 속성 및 이벤트 오브젝트, 커스텀 이벤트를 설정해야 합니다.<br><br>
- **구독 설정 (필수)**<br>
사용자를 구독 그룹에 가입하려면 **구독 추가**를 클릭하고 구독 그룹 이름과 ID를 추가하세요. 여러 그룹 이름과 ID를 추가하려면 **구독 추가** 버튼을 다시 클릭하십시오.<br>![구독 그룹 이름과 ID를 묻는 이미지입니다.][8]{: style="max-width:80%;"}<br><br>
- **사용자 추적 설정**<br>
**커스텀 속성정보 추가**를 클릭하여 `/users/track` 엔드포인트로 전송할 속성 및 이벤트 오브젝트 페어를 추가합니다. 이를 사용하여 통합을 위해 전송된 각 데이터 트랜잭션에 대한 하드 코딩된 속성 값을 추가합니다. 여러 속성을 추가하려면 **커스텀 속성** 버튼을 다시 클릭하십시오.<br>![속성 커스텀 속성을 추가하라는 메시지가 표시된 이미지입니다.][9]{: style="max-width:80%;"}<br><br>
- **커스텀 이벤트 전송**<br>
선택적으로 **커스텀 이벤트 보내기**를 활성화할 수 있습니다. 활성화된 경우 이벤트 이름과 해당 앱 ID를 포함해야 합니다.<br>![필요한 경우 커스텀 이벤트를 보내도록 요청하는 이미지입니다.][10]{: style="max-width:80%;"}<br><br>
4. 마지막으로, 사용 사례에 따라 Wyng 필드를 Braze API 필드에 매핑해야 합니다. **필드 선택**을 선택하여 매핑할 필드를 선택한 후, 통합을 **저장**합니다. 저장되면 이러한 매핑된 필드는 **Integrations > Manage** 아래에서 찾을 수 있습니다.
![다양한 Wyng 필드를 특정 Braze 필드에 매핑할 수 있는 예][11]{: style="max-width:80%;"}
![사용 가능한 동기화 필드 목록입니다.][12]{: style="max-width:80%;margin-top:2px"}

### 3단계: 통합을 테스트하세요

Wyng에서 Wyng 캠페인에서 양식을 제출하는 테스트를 수행하세요. 기본 프로덕션 캠페인에 레코드를 추가하지 않으려는 경우 미리보기 캠페인에 제출할 수도 있습니다. 성공적인 트랜잭션이 **통합** 대시보드에 표시되어야 합니다.

## 이 통합 사용

데이터 커넥터가 설정되면 Wyng에서 생성되고 Braze에 추가된 모든 필드는 다른 데이터 필드와 마찬가지로 캠페인을 트리거하고, 청중을 세그먼트화하거나, 개인화된 콘텐츠를 제공하는 데 사용할 수 있습니다.

애플리케이션은 광범위하며, [contact@wyng.com][13] 또는 특정 계정 매니저에게 구체적인 질문을 문의할 수 있습니다.

## 문제 해결

### 제출 실패

제출 실패의 경우, Braze에 데이터를 보낼 때, 실패한 제출 및 관련 오류 메시지를 검토하려면 **로그 보기** 링크를 클릭하십시오.

!['로그 보기' 링크는 작업 헤더 아래에 있습니다.][14]{: style="max-width:80%;"}

로그 페이지에는 실패한 제출, 재시도 횟수, 제출의 데이터, 오류 및 제출을 다시 푸시하는 링크가 표시됩니다.

![실패한 제출물이 표시되는 예시입니다.][15]{: style="max-width:80%;"}

**오류 보기** 섹션은 오류 코드와 오류의 원인에 대한 추가 정보를 표시합니다. 그런 다음 오류 코드를 Braze와 대조하여 원인을 확인할 수 있습니다.

![Wyng 플랫폼에 표시된 예제 오류 로그입니다.][16]{: style="max-width:80%;"}

추가 질문이 있으시면 Wyng 지원팀(support@wyng.com][13])에 문의하십시오.


[0]: https://wyng.com/
[1]: https://wyng.com/dashboard/integrations/
[2]: {% image_buster /assets/img/wyng/2.png %}
[3]: {% image_buster /assets/img/wyng/3.png %}
[4]: {% image_buster /assets/img/wyng/4.png %}
[5]: {% image_buster /assets/img/wyng/5.png %}
[6]: {% image_buster /assets/img/wyng/6.png %}
[7]: {{site.baseurl}}/API/basics/
[8]: {% image_buster /assets/img/wyng/8.png %}
[9]: {% image_buster /assets/img/wyng/9.png %}
[10]: {% image_buster /assets/img/wyng/10.png %}
[11]: {% image_buster /assets/img/wyng/11.png %}
[12]: {% image_buster /assets/img/wyng/12.png %}
[13]: mailto:contact@wyng.com
[14]: {% image_buster /assets/img/wyng/14.png %}
[15]: {% image_buster /assets/img/wyng/15.jpg %}
[16]: {% image_buster /assets/img/wyng/16.jpg %}