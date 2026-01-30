---
nav_title: Survicate
article_title: Survicate
description: "This reference article outlines the partnership between Braze and Survicate, a customer feedback platform that helps you collect, analyze, and act on customer insights across multiple channels and throughout the user journey."
alias: /partners/survicate/
page_type: partner
search_tag: Partner

---

# Survicate

> [Survicate는](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter) 여러 채널과 고객 여정 전반에 걸쳐 고객 인사이트를 수집, 분석 및 조치하는 고객 피드백 플랫폼입니다. [빠른 데모 보기](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter)

_This integration is maintained by Survicate._

## 통합 정보

Survicate와 Braze 기본 통합 기능을 사용하여 이메일, 인앱, 모바일 또는 웹 설문조사 응답을 Braze 고객 프로필과 동기화할 수 있습니다. Survey responses sync automatically with Braze user profiles as custom attributes or events. 실시간 피드백 인사이트를 통해 고객 데이터와 함께 피드백을 쉽게 추적 및 분석하고 타겟팅 후속 조치와 고도로 개인화된 세그먼트를 생성할 수 있습니다. 

## 사용 사례

Braze and Survicate work together to cover a range of feedback use cases, helping you collect actionable user insights and improve the customer experience:

- 이메일 받은편지함에서 응답할 수 있는 임베디드 설문조사로 설문조사 응답률을 향상하세요. 
- Braze 인앱 메시지를 통해 고객 여정의 중요한 단계에서 인사이트를 수집하세요. 
- Survicate에 저장된 피드백을 사용하여 Braze에서 더 스마트한 세그먼트를 만들 수 있습니다. 
- 고객 피드백을 기반으로 후속 캠페인을 자동화하세요. 
- 고객 인사이트를 활용하여 개인화된 워크플로를 트리거하세요. 
- 자동 번역된 설문조사로 더 많은 오디언스에게 다가갈 수 있습니다.
- 누군가가 설문조사에 응답하면 Braze 연락처 프로필로 이벤트 보내기

## 필수 조건

| Requirement | Description |
| ----------- | ----------- |
| Survicate account | You need a Survicate account to activate this integration. |
| Braze REST API key | A Braze REST API key with the permission `users.track`. <br><br> This can be created in the Braze dashboard from **Settings** > **APIs and Identifiers**. |
| Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Key features of the integration

The Survicate and Braze integration offers real-time data syncing, so the most up-to-date information from Survicate surveys is immediately available in Braze. Based on survey responses, you can use this data to take timely, personalized actions.

- **Send survey responses to Braze as custom user attributes**: Enrich Braze user profiles with data from survey responses.
- **Trigger custom events in Braze**: Use events based on survey answers to target specific groups or initiate follow-up campaigns.
- **Build detailed segments**: Create Braze segments using data from Survicate surveys to personalize your outreach further.

## Integration

### 서바이베이트에서 설문조사 만들기

#### 이메일에 설문조사를 포함하거나 공유 가능한 링크 설문조사 만들기 

1.  Survicate에서 **\+ 새 설문조사 만들기를** 클릭하고 생성 방법(템플릿, AI 설문조사 만들기 사용, 나만의 질문 추가)과 이메일 또는 공유 가능한 링크 설문조사 유형을 선택합니다:
![설문조사 작성자에서 Braze가 선택됩니다.]({% image_buster /assets/img/survicate/survicate_1.gif %})

{: start="2"}
2\. 설문조사의 구성 탭에서 응답자를 식별할 도구로 **Braze를** 선택합니다:
![설문조사의 구성 탭에서 Braze를 선택합니다.]({% image_buster /assets/img/survicate/survicate_2.png %})

{: start="3"}
3\. 설문조사를 설정한 후 공유 탭으로 이동하여 이메일 설문조사 전송 방법을 결정합니다. **설문조사를 링크로** 보내거나 **이메일에 첫 번째 질문을 포함시켜** 응답자가 이메일에서 바로 설문조사에 응답할 수 있도록 하는 두 가지 옵션이 있습니다.

{% details Survey link option %}

1. 설문조사 링크 복사 버튼에서 설문조사 링크를 가져옵니다:

![설문조사 링크 복사 버튼에서 설문조사 링크를 가져옵니다.]({% image_buster /assets/img/survicate/survicate_3.png %})

{: start="2"}
2\. Braze 이메일의 CTA 버튼이나 하이퍼링크 뒤에 설문조사 링크를 숨기세요.

![Braze 이메일의 CTA 버튼이나 하이퍼링크 뒤에 설문조사 링크를 숨기세요.]({% image_buster /assets/img/survicate/survicate_4.png %})

{% enddetails %}

{% details Email embed option %}

이메일 본문에 첫 번째 질문을 바로 표시하여 이메일에서 설문조사를 시작하세요. 그런 다음 응답자는 나머지 설문조사에 참여할 수 있는 랜딩 페이지로 리디렉션됩니다.

1. **이메일 코드 받기를** 클릭한 다음 **HTML 코드를 복사합니다**:

![이메일 코드 받기]({% image_buster /assets/img/survicate/survicate_5.gif %})

{: start="2"}
2\. 설문조사에 사용하려는 Braze 캠페인으로 이동하여 **이메일 본문 편집을** 클릭하고 템플릿에 HTML 블록을 추가합니다:

![HTML 블록 코드 가져오기]({% image_buster /assets/img/survicate/survicate_6.png %})

{: start="3"}
3\. 코드를 서베이케이트 설문조사에서 복사한 코드로 바꿉니다. 그러면 템플릿에 설문조사의 첫 번째 질문이 표시됩니다:

![서베이케이트 설문조사에서 복사한 코드로 코드를 교체합니다.]({% image_buster /assets/img/survicate/survicate_7.png %})

{: start="4"}
4\. 이메일을 예약하고 타겟 그룹을 선택하면 캠페인을 보낼 준비가 완료됩니다.

{% enddetails %}

### Braze 인앱 메시지 설문조사

1. **새 설문조사 만들기를** 클릭하고 생성 방법(템플릿, AI 설문조사 생성 사용, 나만의 질문 추가)을 선택한 다음 플랫폼 내 설문조사 및 Braze 인앱 메시지 설문조사 유형을 선택합니다:

![새 설문조사 만들기를 클릭하고 생성 방법을 선택합니다.]({% image_buster /assets/img/survicate/survicate_8.gif %})

{: start="2"}
2\. Braze 계정으로 이동한 다음 **메시징 > 캠페인 > 캠페인 만들기 > 인앱 메시지**로 이동하여 Braze 인앱 메시지 설문조사를 시작하세요 **:**
![Braze 인앱 메시지 설문조사 시작하기]({% image_buster /assets/img/survicate/survicate_9.gif %})

### 기존 편집기를 통해 Braze 인앱 메신저 설문조사를 시작하세요.

1. 기존 편집기를 사용하는 경우 메시지 유형에서 **커스텀 코드를** 선택합니다:

![커스텀 코드를 선택합니다.]({% image_buster /assets/img/survicate/survicate_10.gif %})

{: start="2"}
2\. 그런 다음 설문조사의 시작 탭에서 HTML 필드에 코드를 붙여넣습니다:

![설문조사의 시작 탭에서 HTML 필드에 코드를 붙여넣습니다.]({% image_buster /assets/img/survicate/survicate_11.gif %})

{% alert note %}
Braze는 앱의 배경이 차단된 상태에서 인앱 메시지를 기본값으로 iframe에 표시합니다. Survicate 설문조사가 표시되는 동안 앱과 상호 작용할 수 있도록 허용해야 합니다:<br><br>

- Survicate-Braze 스니펫에 `opts.useBrazeIframeClipper = true` 을 추가하세요.
- Braze를 초기화하는 파일에 `@survicate/braze-bridge-npm` [패키지를](https://www.npmjs.com/package/@survicate/braze-bridge-npm) 설치하고 `initBrazeBridge` 기능을 사용합니다.

[Survicate의 개발자 사이트에서](https://developers.survicate.com/javascript/installation/#braze) 샘플 스니펫과 React 구현을 확인할 수 있습니다.
{% endalert %}

{: start="3"}
3\. Braze 캠페인에서 타겟 및 할당 단계를 설정합니다. 완료되면 캠페인을 시작할 준비가 된 것입니다. 검토 단계에서는 캠페인이 어떻게 보이는지 확인할 수 있습니다. 설문조사는 위에서 설명한 대로 Survicate 패널에 지정된 위치에 웹사이트에 표시됩니다.

### Braze 통합 활성화하기

1. Braze 통합을 인에이블하려면 **통합으로** 이동하여 "Braze"를 검색하고 선택합니다.

![Braze 선택]({% image_buster /assets/img/survicate/survicate_12.gif %})

{: start="2"}
2\. **연결을** 클릭하여 인증을 설정합니다.

3. Braze 계정 워크스페이스 API 키와 Braze 인스턴스 URL을 입력합니다:

![Braze 계정 워크스페이스 API 키와 Braze 인스턴스 URL을 삽입하세요.]({% image_buster /assets/img/survicate/survicate_13.png %})

{% alert important %}
Survicate를 Braze에 연결하려면 API 키에 `users.track` 권한이 있어야 합니다.
{% endalert %}

### 설문조사를 Braze에 연결하기

이제 Braze 통합이 연결되었으므로 각 설문조사에 대한 개별 설정을 설정할 수 있습니다. 설문조사로 이동하여 **연결** 탭을 선택한 다음 사용 가능한 통합 목록에서 **Braze를** 선택합니다.

![설문조사로 이동하여 연결 탭을 선택한 다음 Braze를 선택합니다.]({% image_buster /assets/img/survicate/survicate_14.png %})

### 응답을 커스텀 속성으로 Braze에 보내기

설문조사 응답을 커스텀 속성으로 설정하여 수집된 데이터로 Braze 고객 프로필을 더욱 풍부하게 만들 수 있습니다.

1. Braze 통합의 설정 탭에서 **필드 업데이트** 섹션을 미세 조정합니다.

![필드 업데이트 섹션을 선택합니다.]({% image_buster /assets/img/survicate/survicate_15.png %})

{: start="2"}
2\. 필드를 업데이트할 질문을 선택합니다. Braze 사용자 프로필에 데이터가 넘치지 않게 하려면 선택한 질문에만 응답을 보낼 수 있습니다.

![다음에서 필드를 업데이트할 문제를 선택합니다.]({% image_buster /assets/img/survicate/survicate_16.png %})

{% alert note %}
순위 및 매트릭스 문제는 이번 Braze 통합에서 지원되지 않습니다.
{% endalert %}

{: start="3"}
3\. **사용자** 필드 아래에 업데이트하려는 커스텀 속성의 이름을 추가합니다:

![사용자 필드 아래에 업데이트하려는 커스텀 속성의 이름을 추가합니다.]({% image_buster /assets/img/survicate/survicate_17.png %})

기본적으로 Survicate는 설문조사 응답의 내용을 속성 값으로 전송합니다. **매핑 편집을** 클릭하여 이 값을 수정하여 레이블을 더 짧게 만들거나 데이터 구조에 맞게 변경할 수 있습니다:

![속성 값으로서의 설문조사 응답]({% image_buster /assets/img/survicate/survicate_18.png %})

![매핑 편집을 클릭하여 다음 값을 수정합니다.]({% image_buster /assets/img/survicate/survicate_19.png %})

{% alert note %}
순고객추천지수의 경우 Survicate는 순고객추천지수 질문에 대한 응답 그룹을 기반으로 매핑된 값을 전송합니다. 그러나 숫자 값을 받으려면 0~10개의 값으로 답변 보내기를 켜면 됩니다.
{% endalert %}

![Survicate는 응답 그룹에 따라 매핑된 값을 전송합니다.]({% image_buster /assets/img/survicate/survicate_20.png %})

{: start="4"}
4\. **새로 추가를** 클릭하고 동일한 단계를 적용하여 더 많은 질문을 통합에 연결하세요.

![통합에 더 많은 질문 연결하기]({% image_buster /assets/img/survicate/survicate_21.png %})

### Braze 연락처의 프로필에 이벤트 보내기

이전 설정과 별도로 응답자가 설문조사 질문에 답할 때마다 Survicate는 Braze에서 `survicate-question-answered` 이라는 이름의 커스텀 이벤트를 보낼 수 있습니다.
Survicate 패널의 커스텀 속성으로 응답 보내기에서 모든 질문, 필드 업데이트 탭에서 선택한 질문 또는 전혀 선택하지 않은 질문에 대해 이벤트를 보낼지 여부를 선택할 수 있습니다:

![모든 질문에 대해 이벤트를 보낼지 여부를 선택할 수 있습니다.]({% image_buster /assets/img/survicate/survicate_22.png %})

이벤트를 보내도록 선택하면 사용자의 프로필에서 Survicate 설문조사에 응답한 횟수와 마지막으로 응답한 시간을 확인할 수 있습니다:

![응답 ]({% image_buster /assets/img/survicate/survicate_23.png %})

이벤트에는 질문에 대한 답변과 설문조사, 질문 및 응답자에 대한 정보가 포함된 이벤트 속성정보가 포함되어 있습니다. 이 이벤트를 사용하여 세그먼트를 만들 수 있습니다. 예를 들어 특정 날짜 또는 특정 횟수 이후에 설문조사에 응답한 사용자 세그먼트를 만들 수 있습니다:

![이벤트에는 다음과 같은 답변이 있는 이벤트 속성정보가 포함되어 있습니다.]({% image_buster /assets/img/survicate/survicate_24.png %})

이 데이터는 Braze에서 캠페인을 만들 때도 사용할 수 있습니다.

![이 데이터는 Braze에서 캠페인을 생성할 때도 사용할 수 있습니다.]({% image_buster /assets/img/survicate/survicate_25.png %})

### Test the integration

설문조사가 준비되고 통합 설정이 완료되면, 생성한 속성, 태그 또는 새 연락처 설정 옆에 있는 통합 테스트 버튼을 클릭하여 Survicate를 종료하지 않고도 테스트할 수 있습니다. Survicate는 Braze 계정에 테스트 연락처(`braze-test@survicate.com`)를 생성합니다. 연락처의 프로필에는 설정에 따라 업데이트된 필드가 포함됩니다.

![통합 테스트 버튼을 클릭합니다.]({% image_buster /assets/img/survicate/survicate_26.png %})

Braze에서는 Survicate 더미 연락처의 매핑된 필드에서 샘플 데이터를 볼 수 있습니다:

![Survicate 더미 연락처에서 매핑된 필드의 샘플 데이터]({% image_buster /assets/img/survicate/survicate_27.png %})

### 설문조사 결과 분석하기

Braze 설문조사를 통해 응답을 수집했다면 이제 응답자들이 공유한 피드백과 인사이트를 살펴볼 차례입니다. Survicate를 사용하면 결과, 통계 및 추세를 쉽게 검토하여 추가 조치를 취할 수 있습니다.

### Survicate에 대한 피드백

설문조사에서 응답 수집이 시작되면 설문조사의 분석 탭에서 즉시 응답을 확인할 수 있습니다.

![분석 탭의 응답]({% image_buster /assets/img/survicate/survicate_28.png %})

분석 탭에는 통계 및 시간 경과에 따른 데이터가 포함된 전체 결과와 각 설문조사 제출을 자세히 살펴볼 수 있는 개별 응답이 표시됩니다.

### Braze의 피드백

설문조사 응답으로 사용자 필드를 업데이트하거나 커스텀 이벤트로 응답을 보내면 실시간으로 동기화된 설문조사 데이터를 확인할 수 있습니다. Braze에서 설문조사에 응답한 특정 연락처로 이동합니다. 연락처의 기본 보기에서 응답 기반 데이터와 이벤트를 모두 볼 수 있습니다.

![실시간으로 동기화된 설문조사 데이터]({% image_buster /assets/img/survicate/survicate_29.png %}) 