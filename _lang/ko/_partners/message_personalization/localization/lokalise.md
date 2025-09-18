---
nav_title: Lokalise
article_title: Lokalise
description: "이 참조 문서에서는 애자일 팀을 위한 번역 관리 서비스인 Braze와 로칼라이즈의 파트너십에 대해 설명합니다."
alias: /partners/lokalise/
page_type: partner
search_tag: Partner

---

# Lokalise

> [Lokalise는](https://lokalise.com) 애자일 팀을 위한 번역 관리 서비스입니다.

_이 통합은 Lokalise에서 유지 관리합니다._

## 통합 정보

Braze와 Lokalise의 통합을 통해 연결된 콘텐츠를 활용하여 사용자 언어 설정에 따라 번역된 콘텐츠를 Braze 캠페인에 쉽게 삽입할 수 있습니다.

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Lokalise 계정 | 이 파트너십을 활용하려면 Lokalise 계정이 필요합니다. |
| 로칼라이즈 번역 프로젝트 | 이 통합을 설정하기 전에 Lokalise 번역 프로젝트를 만들어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 새 Lokalise 프로젝트 만들기

새 번역 프로젝트를 만들려면 Lokalise에 로그인하고 **새 프로젝트를** 선택하세요. 그런 다음 프로젝트 이름을 지정하고 **기본 언어** (번역할 언어)를 선택한 다음 하나 이상의 **대상 언어를** 추가하고 **소프트웨어 현지화** 프로젝트 유형을 선택합니다. 준비가 완료되면 **진행을** 클릭합니다.

## 통합

Lokalise에서는 Braze에서 정의한 각 연결된 콘텐츠 변수에 대한 번역 키를 생성합니다. 번역이 준비되면 언어당 하나의 JSON 파일을 생성하여 커넥티드 콘텐츠를 제공할 URL에 게시할 수 있습니다.

### 1단계: 사용자 언어 구성

아직 수행하지 않았다면 Braze 대시보드를 열고 **사용자 > 사용자 가져오기**로 진행합니다. 여기에서 사용자를 가져올 수 있습니다. 가져올 CSV 파일을 준비할 때 사용자의 언어가 있는 언어 열을 포함해야 합니다. 이 언어 필드는 나중에 번역을 표시할 때 사용됩니다. 

{% alert important %}
사용되는 언어 코드는 Braze와 Lokalise 모두에서 일치해야 합니다.
{% endalert %}
### 2단계: Lokalise에서 번역 준비

다음으로, Lokalise에서 번역을 준비하려면 Braze 커넥티드 콘텐츠 변수에 사용 중인 것과 동일한 이름의 번역 키를 수동으로 생성해야 합니다. 

예를 들어 간단한 번역 키 `description` 를 만들어 보겠습니다:
1. Lokalise 프로젝트를 열고 **키 추가**를 클릭한 다음, **키** 필드에 '설명'을 입력합니다.
2. **기본 언어 값** 필드에 "데모 설명"을 입력합니다.
3. **플랫폼** 드롭다운에 '웹'을 추가합니다. 
4. 준비가 완료되면 **저장을** 클릭합니다.

![]({% image_buster /assets/img/lokalise/1_add_key.png %}){: style="max-width:60%"}

번역 키가 프로젝트 편집기에 표시되어야 합니다:

![]({% image_buster /assets/img/lokalise/2_translation_key_added.png %}){: style="max-width:90%"}

#### 알려진 문제

- 키는 **웹** 플랫폼에 할당되어야 합니다.
- 마침표(`.`) 또는 `_on` 문자열이 포함된 키는 사용하지 마세요. 예를 들어 `this.is.the.key` 대신 `this_is_the_key`를 사용하고 `join_us_on_instagram` 대신 `join_us_instagram`을 사용합니다.

### 3단계: Lokalise에서 Braze 앱 구성하기

Lokalise 프로젝트를 열고 **앱**을 클릭합니다. 여기에서 Braze 앱을 검색하여 설치합니다. 다음 화면이 표시됩니다:

![프로젝트 ID와 번역 파일 URL을 나열하는 Lokalise의 Braze 구성.]({% image_buster /assets/img/lokalise/3_lokalise_braze_app.png %})

**번역 파일 URL에서** Lokalise는 프로젝트의 키에 대한 모든 번역이 포함된 JSON 파일을 게시합니다. 프로젝트에 있는 대상 언어 수만큼 번역 파일 URL을 얻을 수 있습니다. 그렇기 때문에 결과 번역 파일 URL은 두 부분으로 나누어집니다.

1. URL 경로의 첫 번째 부분은 모든 언어에 공통입니다.
2. URL 끝에 있는 JSON 파일 이름은 언어 코드를 기반으로 합니다.

번역 파일 URL은 Braze 캠페인을 구성할 때 필요한 URL입니다. **새로 고침**을 클릭하여 JSON 파일의 콘텐츠를 업데이트할 수 있습니다. URL은 동일하게 유지되며 Braze에서 연결된 콘텐츠 호출을 변경할 필요가 없습니다.

### 테스트 URL

이 URL을 테스트하려면 복사하여 {% raw %}`{{${language}}}`{% endraw %}를 언어 코드(예: `en`)로 바꾸고 브라우저에서 이 URL을 엽니다. 키와 번역이 포함된 JSON 파일이 표시됩니다:

![]({% image_buster /assets/img/lokalise/4_testing_json_lokalise.png %})

### 4단계: Braze 캠페인에서 번역 사용

#### 연결된 콘텐츠 호출 삽입

준비가 되면 Braze로 돌아가서 기존 캠페인을 열거나 새 캠페인을 만듭니다. 이 예제의 샘플 콘텐츠로 새 이메일 캠페인을 만들어 보겠습니다. **이메일 본문 편집**을 클릭합니다.

번역을 삽입하려면 문서 상단 또는 번역이 필요한 첫 번째 위치 바로 앞에 HTML에 연결된 콘텐츠 요청을 추가해야 합니다. 다음 마크업을 삽입하여 이 작업을 수행할 수 있습니다:

{% raw %}
`{% connected_content https://exports.live.lokalise.cloud/braze/123abc/456xyz/{{${language}}}.json :save translations %}`
{% endraw %}

`https://exports.live.lokalise.cloud/...` URL을 이전 단계에서 가져온 번역 파일 URL로 바꿉니다.

{% raw %}

- `{{${language}}}`는 '이 위치에 사용자 언어 삽입'을 의미합니다. 또는 언어 코드를 하드코딩할 수도 있습니다(예: `en.json`).
  - 각 사용자에 대해 적절한 번역된 JSON 파일이 검색되도록 하려면 번역 파일 URL 끝에 `{{${language}}}` 프로필 속성 또는 사용자의 언어가 포함된 다른 유사한 사용자 지정 속성을 배치해야 합니다. (예: `/{{${language}}}.json`) 이러한 속성에 포함된 값은 번역된 각 JSON 파일의 접두사와 일치해야 합니다. 이렇게 하면 각 사용자에 대해 올바른 번역 파일이 반환됩니다.
- `:save translations` 는 번역 변수 아래에 JSON 콘텐츠를 저장합니다.

#### 번역 표시

이제 번역 변수를 사용하여 원하는 번역을 키별로 표시합니다.

예를 들어 `description` 키를 표시하려면`{{ translations.description }}` 을 사용합니다.

{% endraw %}
![]({% image_buster /assets/img/lokalise/6_integration_usage_sample.png %})

마지막으로 이메일 템플릿을 저장하고 미리 봅니다. 그러면 번역이 표시됩니다.

## 자주 묻는 질문

**Lokalise에서 실수로 키를 삭제하면 어떻게 되나요?**<br>
Braze의 해당 문자열에는 더 이상 번역이 없습니다.

**`en` 로캘이 있는데 Lokalise에서 `en-US` 로 재정의하면 Braze가 `en-US` 로 읽나요?**<br>
아니요. Braze와 Lokalise에서 로캘 ISO 코드가 일치해야 합니다.

**Lokalise 콘텐츠를 연결할 때 `:rerender` 플래그를 사용할 수 있나요?**<br>
네, 물론이죠. 이 플래그를 추가하는 방법은 Braze 문서를 참조하세요.

**Lokalise에서 번역 파일을 새로 고친 후 Braze에서 번역된 콘텐츠의 변경 사항을 볼 수 없는 이유는 무엇인가요?**<br>
Braze는 번역된 콘텐츠를 캐시하므로 새로 고치는 데 몇 분 정도 걸릴 수 있습니다. 캠페인을 테스트하는 중이고 번역 결과를 즉시 확인해야 하는 경우 이 참조 문서에 설명된 대로 `:cache_max_age` 매개 변수를 사용할 수 있습니다.


