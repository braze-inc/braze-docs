---
nav_title: Ada
article_title: Ada
description: "이 참고 문서에서는 고객 상호 작용을 자동화하고 개인화하는 AI 기반 플랫폼인 Braze와 Ada의 파트너십을 간략하게 설명합니다. 이 통합을 통해 자동화된 Ada 대화에서 수집한 데이터로 사용자 프로필을 보강할 수 있습니다."
alias: /partners/ada/
page_type: partner
search_tag: Partner

---

# Ada

> [Ada](https://ada.cx)는 대화형 인공지능을 사용하여 고객 경험을 자동화하고 개인화하는 브랜드 상호 작용 플랫폼입니다. Ada를 사용하여 사용자 데이터를 기반으로 메시지를 맞춤화하고 캠페인을 세분화하며, 대화를 측정 및 분석하여 새로운 기회를 발견하고, 고객과의 채팅에서 얻은 인사이트를 활용하여 사용자 프로필을 강화할 수 있습니다.  

Braze와 Ada의 통합을 통해 자동화된 Ada 대화에서 수집한 데이터로 고객 프로필을 보강할 수 있습니다. Ada 채팅 중에 수집한 정보를 기반으로 커스텀 사용자 속성을 설정하고 Ada 대화의 지정된 지점에서 Braze에 커스텀 이벤트를 기록할 수 있습니다. Ada 챗봇을 Braze에 연결하면 소비자가 브랜드에 대해 어떤 질문을 하는지를 기반으로 소비자에 대해 더 많이 알 수 있으며, 선제적으로 대화를 시작하여 소비자의 관심사와 선호도에 대해 더 많이 알 수 있는 질문을 할 수도 있습니다.

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Ada 계정 | 이 파트너십을 이용하려면 Braze 및 Answer Utilities 애플리케이션이 활성화된 [Ada](https://ada.cx) 계정이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> 이는 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [당신의 REST 엔드포인트 URL][1]. 사용자의 엔드포인트는 인스턴스를 위한 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

Braze와 Ada 통합의 일반적인 사용 사례는 다음과 같습니다:
- Braze의 커스텀 이벤트로 소비자와 Ada 봇의 다양한 상호 작용을 추적하여 Ada의 선제적 캠페인에 참여한 고객, 지원 상담원에게 인계된 고객, 특정 질문을 한 고객, 특정 작업을 완료한 고객을 파악할 수 있습니다.
- 소비자의 관심사, 선호도, 인구 통계 등에 대해 물어보세요. 사용자 지정 속성을 사용하여 이 새 정보로 Braze에서 프로필을 자동으로 업데이트합니다.

## 통합

Braze와 Ada를 통합하려면 먼저 Ada 대시보드에서 Braze 애플리케이션을 설정하고 Ada 팀과 협력하여 Ada 임베드 스크립트에서 사용자 ID 메타변수를 설정해야 합니다. 그런 다음, 이벤트나 속성 등의 정보를 Braze에 다시 보내려는 경우에 언제나 Braze 블록을 답변 편집기로 끕니다.

### 1단계: Ada에서 Braze 앱 설정

Ada 대시보드에서 **설정 > 통합 > 핸드오프 통합**으로 이동합니다.

Braze 옆의 **연결**을 클릭하고 다음 정보를 제공합니다.
- **REST 엔드포인트**: Braze REST 엔드포인트 URL을 입력합니다. 
- **API 키**: Braze REST API 키를 입력합니다. 
- **앱 ID**: Ada 채팅을 연결하려는 앱 ID를 입력합니다.

### 2단계: Braze에서 Ada로 식별자를 전달합니다.

올바른 사용자를 업데이트하고 있는지 확인하려면 Ada 팀에 문의하면 Braze에서 식별자를 받기 위해 Ada 임베드 스크립트를 수정하는 데 필요한 도움을 받을 수 있습니다. 이 통합은 외부 ID를 수락하도록 설계되었지만 사용자 별칭과 같은 다른 식별자를 전달할 수도 있습니다. 

### 3단계: Braze 블록을 관련 답변으로 끕니다.

Braze 블록을 사용하려면 블록 드로어에서 해당 답변으로 끌고 작업을 선택합니다. Braze 블록을 사용하면 다음과 같은 두 가지 작업을 수행할 수 있습니다.
* 이벤트 추적
* 속성 업데이트

{% tabs local %}
{% tab 이벤트 추적 %}

#### 답변 유틸리티 블록

1. 블록 드로어에서 답변 유틸리티 블록을 Braze 블록 바로 위의 위치로 끕니다. 
2. **날짜 서식** 지정 작업을 선택하고 **날짜** 필드에 `today` 을 입력합니다.
3. **출력 형식** 필드에 `iso` 을 입력합니다. **응답을 변수로 저장**에서 `iso_time`이라는 **형식화된 날짜**에 대한 변수를 생성합니다

![이전 텍스트에서 설명한 대로 필드가 채워진 답변 유틸리티 블록.]({% image_buster /assets/img/ada/ada-braze-2.png %})

#### 브레이즈 블록

**4\.** Braze 블록의 **외부 ID** 필드에 이전 단계에서 Ada가 설정한 `external_id` 메타변수를 입력합니다.<br>
**5\.** **이벤트 이름** 필드에 추적하려는 Braze 이벤트의 이름을 입력합니다.<br>
**6\.** **이벤트 시간** 필드에 응답 유틸리티 블록에서 만든 `iso_time` 변수를 입력합니다.<br>
**7\.** 이벤트를 Braze에 게시하는 동안 문제가 발생하는 경우 표시할 대체 답변을 선택합니다.

![이전 텍스트에서 설명한 대로 필드가 채워진 Braze 블록.]({% image_buster /assets/img/ada/ada-braze-3.png %})

{% endtab %}
{% tab 속성 업데이트 %}

#### 브레이즈 블록

1. Braze 블록의 **외부 ID** 필드에 이전 단계에서 Ada가 설정한 ** 메타변수를 입력합니다. 
2. **속성 이름** 필드에 추적하려는 Braze 속성의 이름을 입력합니다. 
3. **속성 값** 필드에 설정하려는 값(텍스트, 변수 또는 텍스트와 변수의 조합 등)을 입력합니다. 
4. 속성을 Braze에 게시하는 동안 문제가 발생하는 경우 표시할 대체 답변을 선택합니다.

![이전 텍스트에서 설명한 대로 필드가 채워진 Braze 블록.]({% image_buster /assets/img/ada/ada-braze-4.png %})

{% endtab %}
{% endtabs %}

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/ada/ada-braze-1.png %}
[3]: {% image_buster /assets/img/ada/ada-braze-2.png %}
[4]: {% image_buster /assets/img/ada/ada-braze-3.png %}
[5]: {% image_buster /assets/img/ada/ada-braze-4.png %}