---
nav_title: Braze Docs 스타일 가이드
article_title: Braze Docs 스타일 가이드
description: "Braze Docs 작성 스타일 가이드입니다."
page_order: 0
noindex: true
---

# Braze Docs 스타일 가이드

## 작성 스타일 가이드

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

### 일반 가이드라인 {#general-guidelines}

#### 보이스와 톤 {#voice-and-tone}

Braze의 브랜드 보이스는 스마트하고, 대화적이며, 직접적입니다. 기술 전문 용어가 넘치는 세상에서 인간적인 목소리를 내고, 고객 참여라는 기술에 관심 있는 모든 사람에게 명확한 안내를 제공하며, 전문 용어 대신 이해하기 쉬우면서도 강력한 간결한 언어를 사용합니다.

글을 쓰고 편집할 때 이 브랜드 보이스에 맞추기 위해 세 가지 보이스 가이드라인을 사용합니다: **직관적, 역량 강화,** 그리고 **인간적**.

##### 직관적

글을 명확하게 구조화하고 독자가 필요한 정보를 쉽게 찾을 수 있도록 합니다.

* 복잡한 것을 간단하게 설명합니다.
* 간결하게 작성합니다.
* 기능과 동작에 일관된 용어를 사용합니다.

###### 가이드라인

✅ 시각 자료를 활용하여 복잡한 주제를 명확히 합니다. <br>
**예시:** [고객 프로필 수명주기 문서]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)의 고객 프로필 수명주기 이미지는 까다로운 개념을 설명하는 데 도움이 됩니다.

✅ 명확한 정보 계층 구조를 만듭니다. <br>
**예시:** "이 문서는 Braze Docs에서 콘텐츠를 관리하는 방법에 대한 개요입니다. 특정 주제에 대해 자세히 알아보려면 내비게이션에서 해당 주제 페이지를 선택하세요."

✅ 가능하면 전문 용어와 약어를 과감히 제거합니다. 불가능한 경우 정의를 제공합니다. <br>
**예시:** "Short Messaging Service(SMS)는 짧은 텍스트 메시지를 보내고 받는 데 사용됩니다."

##### 역량 강화

글을 통해 어떤 문제를 해결하려고 하나요? 콘텐츠를 만들 때 그 문제를 항상 염두에 두세요.

* "왜"와 "어떻게"를 설명하여 사용자가 자신 있게 행동할 수 있도록 합니다.
* 이점을 설명할 때 구체적으로 하고, 가능한 것과 불가능한 것을 명확히 합니다.
* 실용적인 조언과 진심 어린 격려를 제공합니다.

###### 가이드라인

✅ 최적의 경로를 쉽게 찾을 수 있도록 합니다. <br>
**예시:** "Canvas를 중지하면 다음이 적용됩니다: 1. 사용자가 Canvas에 진입할 수 없습니다. 2. 사용자가 플로우의 어디에 있든 더 이상 메시지가 전송되지 않습니다. 3. **예외:** 이메일 Canvas는 즉시 중지되지 않습니다."

✅ 사용자의 작업을 간소화하거나 향상시키는 예시, 활용 사례, 템플릿을 제공합니다. <br>
**예시:** "`IInAppMessageManagerListener`에는 메시지 자체 또는 버튼 중 하나를 클릭할 때의 델리게이트 메서드도 포함되어 있습니다. 일반적인 활용 사례는 추가 처리를 위해 버튼이나 메시지를 클릭할 때 메시지를 가로채는 것입니다."

##### 인간적

정보 전달 글은 본질적으로 건조합니다. 독자가 전달 방식이 아닌 콘텐츠에 집중하기를 원합니다. 그래도 독자가 소비하는 정보를 처리하는 데 도움이 되고 지식을 내면화할 가능성을 높이는 방식으로 글을 쓸 수 있습니다. 인간적이고, 개성을 드러내며, 기억에 남도록 작성하세요.

* 격식체보다 대화체를 지향합니다.
* 사용자에 초점을 맞추고, 그들의 상황과 감정 상태를 존중합니다.
* 기계 상태가 아닌 인간의 경험을 적극적으로 중심에 둡니다.

###### 가이드라인

✅ 브랜드 톤과 자산을 신중하게 적용합니다. <br>
**예시:** "Braze와의 통합은 가치 있는 과정입니다. 하지만 여러분은 똑똑합니다. 여기 계시잖아요. 분명히 이미 알고 계실 겁니다."

✅ 시각적, 언어적 콘텐츠 모두에 [접근성 모범 사례](#accessibility)를 적용합니다. <br>
**예시:** "out-of-the-box"와 같은 관용구를 "기본"으로 대체하면 영어가 제2언어인 사용자에게 텍스트가 더 접근하기 쉬워집니다.

✅ 사용자 여정 전반에 걸쳐 일관된 지원을 제공합니다. <br>
**예시:** Diátaxis 프레임워크를 사용하여 다양한 시점에서 다양한 사용자의 요구를 충족하고 있는지 확인합니다.

#### 접근성 {#accessibility}

Braze는 포용적인 경험을 제공하는 것을 목표로 합니다. 접근성 요구가 있는 [10억 명의 사람들](https://www.who.int/en/news-room/fact-sheets/detail/disability-and-health)이 학습 콘텐츠에 접근할 수 있도록 다음 가이드라인을 따르세요.

##### 일반

* 편향적이거나 차별적인 언어를 피합니다. 자세한 내용은 [포용적 언어](#inclusive-language) 섹션을 참조하세요.
* [스크린 리더](https://support.apple.com/guide/mac-help/use-accessibility-features-mh35884/mac)를 사용하여 콘텐츠를 테스트합니다.
* 앰퍼샌드(&)를 사용하는 UI 요소를 참조하는 경우가 아니라면 "and" 대신 [앰퍼샌드](#ampersands)(&)를 사용하지 않습니다.

##### 언어와 서식

* [쉬운 언어](https://www.plainlanguage.gov/guidelines/)를 사용합니다.
* 가장 중요한 정보를 섹션 앞부분에 배치합니다. 저널리즘의 [역피라미드](https://en.wikipedia.org/wiki/Inverted_pyramid_(journalism)) 모델을 사용합니다.
* 독자가 정보를 훑어볼 수 있도록 긴 텍스트를 나눕니다. 단락, [목록](#lists), [콜아웃](#callouts-and-alerts), [이미지](#figures-and-other-images)를 사용하여 가독성을 높입니다.
* [짧은 문장과 단락을 작성합니다](https://www.usability.gov/how-to-and-tools/methods/writing-for-the-web.html). 일반적으로 문장당 20단어 이하, 단락당 5문장 이하를 목표로 합니다.
* 라틴어 약어와 구문은 번역하기 어려울 수 있으므로 사용을 피합니다. 대신 간단한 단어나 구문을 사용합니다.

##### 제목

* 고유하고, 설명적이며, 명확한 [제목과 타이틀](#headings-and-titles)을 사용합니다.
* 페이지 제목에는 h1을 사용합니다.
* 제목 수준을 건너뛰지 않습니다. h3은 h2 다음에 와야 합니다.

##### 링크

* "자세히 알아보기", "여기", "이 문서"와 같은 링크 텍스트를 사용하지 않습니다. 피해야 할 구문에 대해서는 [링크 작성](#writing-links) 섹션을 참조하세요.
* 문장에서 두 개의 링크를 연속으로 배치하지 않습니다. 구분을 위해 문자나 단어를 사이에 넣습니다.
* [파일 다운로드 링크](#links-for-file-download)는 링크를 클릭하면 파일이 다운로드된다는 것과 파일 유형(PDF, CSV 등)을 표시해야 합니다.
* 문맥상 명확하지 않은 경우, 같은 문서의 섹션으로 연결되는 링크는 이 동작을 나타내는 [표준 구문](#structuring-links)을 사용해야 합니다.

##### 이미지, 동영상, GIF

* 이미지에 표시된 정보를 요약하는 [대체 텍스트](#alt-text)를 모든 이미지에 제공합니다.
* 이미지를 정보를 표시하는 유일한 방법으로 사용하지 않습니다. 이미지에 표시된 단계, 콘텐츠 또는 기타 세부 정보를 항상 주변 텍스트에 제공합니다.
* 터미널 출력, 코드 샘플 또는 텍스트의 이미지를 사용하지 않습니다. 대신 실제 텍스트를 사용합니다.
* 동영상 콘텐츠에 자막을 제공합니다.
* 동영상이나 GIF에 깜빡이는 요소를 사용하지 않습니다.

##### 표 {#tables-1}

* 항상 표의 목적을 설명하는 소개 문장을 사용합니다.
* 목록 중간, 특히 단계별 목록 중간에 표를 넣지 않습니다.

#### 글로벌 오디언스 {#global-audience}

학습 콘텐츠는 미국 영어로 작성합니다. 그러나 Braze는 글로벌 브랜드이므로 글로벌 오디언스를 위해 작성합니다. 영어가 모국어가 아닌 고객도 글을 이해할 수 있도록 다음 가이드라인을 따르세요.

1. **현지화를 염두에 두고 작성합니다:**
  * [날짜와 시간](#dates-and-times)을 모호하지 않은 형식으로 작성합니다.
  * 이미지에 텍스트 오버레이를 넣지 않습니다. 이 텍스트는 번역할 수 없습니다.
  * [속어와 관용구](#slang-and-idioms)를 피합니다.
  * 맥락을 제공합니다. 독자가 무엇에 대해 이야기하는지 알고 있다고 가정하지 않습니다.
2. **짧고 정확한 문장을 작성합니다:**
  * [쉬운 언어](https://www.plainlanguage.gov/guidelines/)를 사용합니다.
  * [약어](#abbreviations)를 정의합니다.
  * [모호한 대명사](#ambiguous-pronouns)를 피합니다. 대명사가 모호할 수 있는 경우 적절한 명사로 대체합니다.
3. **일관성을 유지합니다:**
  * 동일한 개념에 대해 대소문자와 텍스트 서식을 포함하여 모든 언급에서 동일한 용어를 사용합니다.
  * 주어 + 동사 + 목적어 순서로 문장을 작성합니다.
  * 지시 사항이 조건 충족에 따라 달라지는 경우 조건절을 먼저 배치합니다. 자세한 내용은 [절 순서](#clause-order)를 참조하세요.
4. **포용적으로 작성합니다:**
  * [포용적 언어](#inclusive-language)를 사용합니다.
  * 다양한 [예시 이름](#example-names)을 사용합니다.
  * 문화적으로 특정한 유머를 피합니다.

#### 포용적 언어 {#inclusive-language}

B2B 기업이지만 사람이 우리가 하는 일의 중심에 있으며, 글로벌 브랜드입니다. 콘텐츠에서 사람을 언급할 때마다 포용적이고 배려하는 것을 염두에 둡니다. 의문이 있을 때는 이 섹션이나 [The Diversity Style Guide](https://www.diversitystyleguide.com/)를 참조하세요.

##### 나이

글과 관련이 없는 한 대상의 나이를 언급하지 않습니다. "젊은" 또는 "나이 든"과 같은 수식어를 사용하여 대상이나 오디언스를 설명하지 않습니다.

연령대를 나타내는 경우 "청소년" 대신 "Z세대"와 같이 설명적이고 구체적으로 작성합니다. "대학생 나이"와 같은 모호한 표현 대신 "대학생"이라고 말할 수 있을 때는 그렇게 합니다.

##### 색상

절대적으로 필요한 경우가 아니면 글에 색상 용어를 포함하지 않으며, 필요한 경우 설명 텍스트를 포함합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">✅ 저장을 누릅니다.</td><td style="width: 50%;">녹색 저장 아이콘을 누릅니다.</td></tr>
<tr><td style="width: 50%;">녹색 체크 표시 아이콘을 누릅니다.</td><td style="width: 50%;">빨간색 취소 버튼 옆의 녹색 아이콘을 누릅니다.</td></tr>
<tr><td style="width: 50%;">녹색 아이콘을 누릅니다.</td><td style="width: 50%;"></td></tr>
</tbody>
</table>
{:/}

인터랙티브 요소의 유일한 표시기로 색상에 의존하지 않습니다. 예를 들어, 호버 시 링크에 밑줄을 긋거나 필수 필드에 별표를 표시합니다.

"좋음"과 "나쁨"(또는 더 자주 "권장"과 "비권장") 표시기로 녹색과 빨간색에만 의존하지 않습니다. 적록 색맹은 가장 흔한 유형의 색맹입니다. 색상을 사용하여 권장/비권장을 전달하는 경우 동일한 요점을 전달하기 위해 다른 텍스트나 기호도 포함해야 합니다.

##### 거만한 언어 {#condescending-language}

독자가 따라야 할 지시 사항이나 단계를 작성할 때 다음과 같은 단어나 구문을 사용하지 않습니다:

* simple, 예: "캠페인 만들기는 간단합니다."
* simply, 예: "...X를 Y에 추가하기만 하면 됩니다"
* just, 예: "...X를 설치하기만 하면 됩니다"
* "쉽습니다"

누군가가 단계나 지시 사항에 어려움을 겪는 경우, 이러한 가벼운 표현이 거만하게 느껴질 수 있습니다. 또한 지시 사항을 따를 만큼 숙련되지 않았다는 표시로 해석하는 사람들을 의도치 않게 문서에서 배제할 수 있습니다.

##### 고객 대 클라이언트

회사 사용자와 그들의 소비자를 언급할 때 다음 용어를 적절히 사용합니다:

* **고객:** 우리와 함께 일하는 브랜드. 고객을 "클라이언트"라고 부르지 않습니다.
 * **회사 사용자:** 문서 맥락에서 플랫폼 사용자와 마케팅 메시지를 받는 최종 사용자를 구분해야 할 때 "회사 사용자"를 사용합니다.
* **소비자:** 우리와 함께 일하는 브랜드의 고객.
* **사용자:** 일반적으로 "사용자" 메트릭에 의존하는 특정 통계(예: "사용자 유지")에 사용됩니다. 콘텐츠에서 "사용자"를 언급할 때는 먼저 더 구체적으로 표현하려고 합니다. 쇼핑객, 소비자, 환자, 플레이어 등을 생각해 보세요.

##### 부서와 팀

부서나 팀의 이름은 대문자로 표기합니다. "team"이나 "department"는 대문자로 표기하지 않습니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Marketing, Business Intelligence Product team</td><td style="width: 50%;">marketing, business intelligence Product Team</td></tr>
<tr><td style="width: 50%;">Revenue department</td><td style="width: 50%;">Revenue Department</td></tr>
</tbody>
</table>
{:/}

##### 장애

글과 구체적으로 관련이 없는 한 사람의 장애를 언급하지 않습니다. 관련이 있는 경우 배려하고 대상이 정체성 우선 언어를 선호하는지 사람 우선 언어를 선호하는지 물어봅니다. 장애가 있는 대상을 언급할 때 "handicapped"와 같은 용어를 사용하지 않습니다.

차별적 언어에는 "crazy", "insane", "blind to" 또는 "blind eye to", "cripple", "dumb" 등의 단어나 구문이 포함됩니다. 맥락에 따라 대체 단어를 선택합니다.

##### 질병

질병을 설명할 때 "고통받다", "투쟁하다", "피해자"와 같은 단어를 피합니다. 중립적이고 사실적으로 작성합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">그녀는 암 진단을 받았습니다.</td></tr>
<tr><td style="width: 100%;">그들은 HIV와 함께 살고 있습니다.</td></tr>
<tr><td style="width: 100%;">그는 뇌졸중에서 회복했습니다.</td></tr>
</tbody>
</table>
{:/}


##### 콘텐츠의 포용성

다양한 커뮤니티를 강조하고 대표합니다. 고객, 연사, 업계 전문가, Braze 팀원을 참여시킬 때 배려하고 포용적이어야 합니다.

##### 직함

직함에 관해서는 AP 스타일에서 벗어납니다. 모든 경우에 특정 사람을 언급할 때 직함을 대문자로 표기합니다.

###### 회사명이 포함된 직함

공식 직함이 사람의 이름 앞이나 뒤에 올 때 대문자로 표기합니다. 세 가지 형식으로 작성합니다:

1. **[공식 직함]** at **[회사명]** + **[전체 이름]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Creative Director at PantsLabyrinth David Bowie</td><td style="width: 50%;">creative director at PantsLabyrinth David Bowie</td></tr>
</tbody>
</table>
{:/}

{: start="2"}
2. **[전체 이름]** + 쉼표 + **[공식 직함]** at **[회사명]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">David Bowie, Creative Director at PantsLabyrinth</td><td style="width: 50%;">David Bowie, creative director at PantsLabyrinth</td></tr>
</tbody>
</table>
{:/}

{: start="3"}
3. **[회사명]** + **[공식 직함]** + **[전체 이름]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">PantsLabyrinth Creative Director David Bowie</td><td style="width: 50%;">PantsLabyrinth creative director David Bowie</td></tr>
</tbody>
</table>
{:/}

###### 회사명이 없는 직함

공식 직함으로 특정 사람을 언급할 때 공식 직함과 이름을 다음과 같이 대문자로 표기합니다:

1. **[공식 직함]** + **[전체 이름]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">CEO Robin Fenty</td><td style="width: 50%;">Chief executive officer Robyn Fenty</td></tr>
</tbody>
</table>
{:/}

{: start="2"}
2. **[공식 직함]** + 쉼표 + **[전체 이름]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">SVP, Product, Robin Fenty</td><td style="width: 50%;">senior vice president, product, Robyn Fenty</td></tr>
</tbody>
</table>
{:/}

###### 기타

공식 직함은 "at [회사명]"을 사용합니다. 창립자와 공동 창립자는 "of [회사명]"을 사용합니다. 공식 직함과 직업 자체는 대문자로 표기할 필요가 없습니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">I wrote to their chief data officer.</td><td style="width: 50%;">I wrote to their Chief Data Officer</td></tr>
<tr><td style="width: 50%;">We spoke with several business intelligence analysts.</td><td style="width: 50%;">We spoke with several Business Intelligence Analysts.</td></tr>
<tr><td style="width: 50%;">Braze 계정 매니저에게 문의하세요.</td><td style="width: 50%;">I wrote to their Chief Data Officer Braze Account Manager에게 문의하세요.</td></tr>
</tbody>
</table>
{:/}

성별이 이미 확인되지 않은 한 성별 중립적인 직함을 사용합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">salesperson</td><td style="width: 50%;">salesman/saleswoman</td></tr>
</tbody>
</table>
{:/}

해당 인물이 자신의 직함을 이렇게 부르는 경우 VP 또는 SVP와 같이 적절하게 약어를 사용합니다. 텍스트 공간이 제한된 경우 표준 약어(VP, SVP, Sr., Jr.)를 사용할 수 있습니다.

##### 성별

사람의 성별에 대해 가정하지 않습니다. 콘텐츠에 등장하는 대상에게 어떻게 자신을 정체화하는지 물어봅니다.

커뮤니티 구성원을 언급할 때 "queer"는 허용됩니다. "Gay"는 허용되지 않습니다. 사람들의 그룹을 "LGBTQ"로 지칭할 수 있습니다. 개인을 설명하는 데는 사용하지 않습니다.

콘텐츠에서 사람들의 그룹에게 말할 때 오디언스에 성별을 부여하지 않습니다(예: "자, 여러분!"). 대신 성별 중립적인 표현을 사용합니다(예: "시작해 볼까요, 여러분!").

"They/them/theirs"는 모든 콘텐츠에서 단수 또는 복수 대명사로 항상 사용할 수 있습니다.

##### 정신 건강

정신 건강과 질환은 광범위한 상태를 포함합니다. 글과 관련이 없는 한 사람의 정신 건강을 언급하지 않습니다. 낙인을 찍는 단어와 구문을 피합니다. 의학 용어를 일상적으로 사용하지 않습니다(예: "우울한 상황...").

##### 이름

사람을 처음 언급할 때 이름과 성을 모두 사용합니다. 이후에는 이름이나 성 중 하나를 사용하여 언급합니다.

##### 대명사

대명사의 적절한 사용에 대한 정보는 언어와 문법 섹션의 [대명사](#pronouns)를 참조하세요.

##### 인종, 종교, 민족

글과 관련이 없는 한 사람의 인종, 종교, 민족을 언급하지 않습니다. 인종이나 민족이 관련된 글에서는 대상에게 어떻게 자신을 정체화하는지 물어봅니다.

이중 유산이나 종교를 나타내기 위해 하이픈을 사용하지 않습니다. 대신 공백을 사용합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Muslim American</td><td style="width: 50%;">Muslim-American</td></tr>
<tr><td style="width: 50%;">Cuban American</td><td style="width: 50%;">Cuban-american</td></tr>
</tbody>
</table>
{:/}

민족, 국적, 민족, 부족의 고유 명칭은 대문자로 표기합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Cambodian</td><td style="width: 50%;">cambodian</td></tr>
<tr><td style="width: 50%;">Black Americans</td><td style="width: 50%;">black Americans</td></tr>
</tbody>
</table>
{:/}

종교 또는 종교 용어의 이름은 대문자로 표기합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Bahá'í Faith</td><td style="width: 50%;">bahá'í faith</td></tr>
<tr><td style="width: 50%;">Buddhist</td><td style="width: 50%;">buddhist</td></tr>
</tbody>
</table>
{:/}

아프리카계 미국인 구어체(on fleek, bae, lit, woke)에 속하는 단어나 표현을 도용하지 않습니다.

원주민 고유의 단어나 표현(예: spirit animal, powwow)을 도용하지 않습니다.

#### 제3자 출처 {#third-party-sources}

다른 사이트의 콘텐츠를 복사하지 않습니다. 저작권을 침해할 수 있습니다. 콘텐츠에는 텍스트와 이미지가 모두 포함됩니다.

제3자 사이트를 복사하거나 인용하는 대신 콘텐츠를 의역하거나 자세한 정보를 위해 제3자 사이트 링크를 제공합니다. 자세한 내용은 [다른 사이트 링크](#links-to-other-sites)를 참조하세요.

### 언어와 문법 {#language-and-grammar}

합의된 문법과 규칙을 따르면 글을 명확하고 일관되게 유지할 수 있습니다. 이 섹션에서는 별도로 명시하지 않는 한 기술 문서에서 따르는 내용을 다룹니다.

#### 약어 {#abbreviations}

두문자어, 이니셜리즘, 축약어와 같은 약어는 명확성, 보이스, SEO에 해를 끼칠 수 있습니다.

일부 약어는 널리 이해되지만 다른 약어는 잘 알려지지 않았거나 특정 고객 그룹에만 익숙합니다. 최선의 판단을 사용하고, 일반적으로 [American Heritage Dictionary](https://ahdictionary.com/)에 나열된 약어라면 풀어 쓰지 않아도 됩니다.

약어가 잘 알려지지 않은 경우 첫 번째 언급 시 풀어 쓰고 괄호 안에 약어를 넣습니다. 이후 모든 언급에서는 약어를 사용합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장: <em>잘 알려지지 않은 약어는 첫 번째 언급 시 풀어 씁니다</em></th><th style="width: 50%;">비권장: <em>일반적인 약어를 풀어 씁니다</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Top-level domain (TLD)</td><td style="width: 50%;">Portable Document Format (PDF)</td></tr>
<tr><td style="width: 50%;">Universally unique identifier (UUID)</td><td style="width: 50%;">Universal Serial Bus (USB)</td></tr>
</tbody>
</table>
{:/}


약어를 복수형으로 만들 때는 일반 단어처럼 취급하고 아포스트로피를 추가하지 않습니다. 예를 들어 APIs와 SDKs입니다. 관사(a 또는 an) 사용도 마찬가지로 약어의 발음을 기준으로 합니다. 약어가 모음 소리로 시작하면 "an"을, 자음 소리로 시작하면 "a"를 사용합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">권장: <em>약어의 철자가 아닌 발음에 따라 관사를 사용합니다</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">an ISP</td></tr>
<tr><td style="width: 100%;">a DLL</td></tr>
<tr><td style="width: 100%;">an HTML site</td></tr>
<tr><td style="width: 100%;">a CSV file</td></tr>
</tbody>
</table>
{:/}

#### 능동태 {#active-voice}

Braze에서는 가능한 한 능동태를 사용합니다. 능동태가 우리의 기본 기준입니다. 누가 또는 무엇이 특정 동작을 수행하는지 판단하기 어려운 수동태를 피합니다.

문장이 수동태인지 확인하려면 동사 뒤에 "by somebody"를 삽입해 보세요. 문장이 말이 되면 수동태일 가능성이 높습니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장: <em>능동태를 사용합니다</em></th><th style="width: 50%;">비권장: <em>가능하면 수동태를 피합니다</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Braze는 소비자를 그들이 좋아하는 브랜드와 연결합니다.</td><td style="width: 50%;">소비자는 그들이 좋아하는 브랜드와 연결됩니다.</td></tr>
<tr><td style="width: 50%;">Braze는 직원들에게 주소를 최신 상태로 유지하도록 요구합니다.</td><td style="width: 50%;">직원들은 주소를 최신 상태로 유지하도록 요구됩니다.</td></tr>
<tr><td style="width: 50%;">회사 관리자는 Braze 로그인을 위한 인증 요구 사항을 구성할 수 있습니다.</td><td style="width: 50%;">Braze 로그인을 위한 인증 요구 사항은 회사 관리자가 구성할 수 있습니다.</td></tr>
</tbody>
</table>
{:/}

##### 예외

다음과 같은 경우에는 수동태를 사용해도 됩니다:

* 주어를 강조하지 않기 위해, 일반적으로 독자를 비난하는 것을 피하기 위해:
  - **권장:** 이메일에서 두 개의 오류가 발견되었습니다.
  - **비권장:** 이메일에서 두 개의 오류를 만들었습니다.
* 누가 동작을 담당하는지 아는 것이 중요하지 않은 경우:
  - **권장:** 이 문서는 2020년 12월에 마지막으로 업데이트되었습니다.

#### 관사 {#articles}

"a", "an", "the" 관사를 사용하여 글을 명확하게 하고 번역을 돕습니다. 특정 단수 또는 복수 명사 앞에는 "the"를, 비특정 단수 명사 앞에는 "a" 또는 "an"을 사용합니다.

"a"와 "an" 중 어느 것을 사용할지 결정하려면 뒤따르는 단어의 발음을 확인합니다. 자음 소리 앞에는 "a"를, 모음 소리 앞에는 "an"을 사용합니다. [약어](#abbreviations)에도 동일한 가이드라인이 적용됩니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">권장: <em>선행 단어의 발음에 따라 관사를 사용합니다.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">an hour</td></tr>
<tr><td style="width: 100%;">a minute</td></tr>
<tr><td style="width: 100%;">an FAQ article</td></tr>
<tr><td style="width: 100%;">a LAB course</td></tr>
</tbody>
</table>
{:/}

#### 대명사 {#pronouns}

##### 인칭 대명사

가능하면 2인칭 대명사(you)를 사용합니다.

외부 대상 글에서 Braze 고객을 "사용자"로 지칭하지 않고, 대신 "you"를 사용하여 독자에게 직접 말합니다. 고객의 고객을 지칭할 때는 "your consumers"를 사용하거나, 사용자 통계와 관련된 상황에서는 "your users"를 사용합니다.

다음 경우를 제외하고 1인칭 대명사(I, we, us, our)를 피합니다:

* FAQ 항목. 예: "비밀번호를 어떻게 재설정하나요?"
* 조직으로서의 Braze를 지칭할 때 "we"를 사용합니다.
 * "we"가 누구를 지칭하는지 불분명할 수 있는 경우, 먼저 Braze를 이름으로 언급한 후 이후 언급에서 "we"를 사용합니다.

##### 성별 중립 대명사

대상이 사용하는 대명사를 사용합니다. 불확실한 경우 단수 대명사로 "they", "them", "their"를 사용합니다. 단수 "they"의 대안으로 "he/she" 또는 "(s)he"를 사용하지 않습니다.

언급하는 사람이 실제로 해당 성별인 경우에만 성별 대명사(he/she, him/her, his/hers)를 사용합니다.

##### 모호한 대명사 {#ambiguous-pronouns}

대명사는 명사를 대체합니다. 대명사가 지칭하는 단어를 선행사라고 합니다. 지시 사항이나 학습 자료를 작성할 때 대명사와 선행사 사이의 참조를 명확하게 합니다. 의미를 명확히 하기 위해 주어를 반복해야 할 수도 있습니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장: <em>대명사가 선행사를 명확하게 참조하도록 합니다</em></th><th style="width: 50%;">비권장: <em>모호한 대명사 참조를 사용합니다</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">필드에 텍스트를 입력하면 텍스트가 변경되지 않습니다.</td><td style="width: 50%;">필드에 텍스트를 입력하면 그것이 변경되지 않습니다.</td></tr>
<tr><td style="width: 50%;">그녀는 Sarah에게 Sarah의 답이 틀렸다고 말했습니다.</td><td style="width: 50%;">그녀는 Sarah에게 그녀의 답이 틀렸다고 말했습니다.</td></tr>
<tr><td style="width: 50%;">보관된 캠페인은 편집할 수 없습니다. 캠페인을 편집하려면 보관을 해제하세요.</td><td style="width: 50%;">보관된 캠페인은 편집할 수 없습니다. 편집하려면 보관을 해제하세요.</td></tr>
</tbody>
</table>
{:/}

##### 선택적 대명사

글에 추가적인 명확성을 더하고 현지화를 돕기 위해 "that", "which", "who"와 같은 대명사를 사용합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장: <em>"that", "which", "who"를 사용하여 추가적인 명확성을 더합니다.</em></th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">열려는 링크를 마우스 오른쪽 버튼으로 클릭합니다.</td><td style="width: 50%;">열 링크를 마우스 오른쪽 버튼으로 클릭합니다.</td></tr>
<tr><td style="width: 50%;">여기에서 포함할 Tinyclues 코호트를 선택할 수 있습니다.</td><td style="width: 50%;">여기에서 포함하려는 Tinyclues 코호트를 선택할 수 있습니다.</td></tr>
</tbody>
</table>
{:/}

#### 대문자 표기 {#capitalization}

불필요한 대문자 표기를 피합니다. 대부분의 경우 문장 대소문자를 사용합니다. 타이틀 케이스는 고유 명사나 기능 이름에만 사용해야 합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장: <em>웹사이트 URL과 이메일 주소는 소문자로 작성합니다</em></th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">www.braze.com/docs</td><td style="width: 50%;">www.Braze.com/docs</td></tr>
<tr><td style="width: 50%;">sample@email.com</td><td style="width: 50%;">SAMPLE@EMAIL.COM</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장: <em>방향은 소문자로 작성합니다</em></th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">north, south, east, west</td><td style="width: 50%;">North, South, East, West</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장: <em>특정 지역은 대문자로, 약어 지역은 모두 대문자로 표기합니다</em></th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">the Northwest</td><td style="width: 50%;">the northwest</td></tr>
<tr><td style="width: 50%;">Southern Connecticut</td><td style="width: 50%;">southern Connecticut</td></tr>
<tr><td style="width: 50%;">Eastern Europe</td><td style="width: 50%;">eastern Europe</td></tr>
<tr><td style="width: 50%;">APAC, EMEA</td><td style="width: 50%;">Apac, emea</td></tr>
</tbody>
</table>
{:/}

##### 브랜드와 제품

브랜드나 제품을 언급할 때 해당 브랜드가 사용하는 대문자 표기를 따릅니다. 대부분의 경우 브랜드(Grindr, Walmart)와 제품(Benchmarks, Looker Blocks)의 이름은 대문자로 표기합니다. eBay나 iTunes처럼 양식화된 브랜드 이름이 첫 단어인 경우 소문자로 문장을 시작해도 됩니다.

인터캡의 경우 항상 인쇄물에서 브랜드가 선호하는 사용법을 참조합니다(OkCupid, YouTube). 로고나 그래픽 디자인 처리에서만 나타나는 인터캡은 사용하지 않습니다(Amazon).

#### 절 순서 {#clause-order}

특정 상황에서 독자에게 무언가를 하라고 말하려면 지시 사항을 제공하기 전에 상황을 먼저 언급합니다. 이렇게 하면 해당 상황이 적용되지 않는 경우 독자가 지시 사항을 건너뛸 수 있습니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">문제 해결 단계는 캠페인 FAQ를 참조하세요.</td><td style="width: 50%;">문제 해결 단계를 보려면 캠페인 FAQ를 참조하세요.</td></tr>
<tr><td style="width: 50%;">캠페인을 보관하려면 톱니바퀴 아이콘을 클릭하고 보관을 선택합니다.</td><td style="width: 50%;">톱니바퀴 아이콘을 클릭하고 보관을 선택하여 캠페인을 보관합니다.</td></tr>
</tbody>
</table>
{:/}

#### 결합 형태 {#combining-forms}

구문이 명사 앞에서 형용사로 사용될 때 결합 형태에 [하이픈](#hyphens)을 사용합니다.

**예시:** A one-of-a-kind item

#### 축약형 {#contractions}

축약형은 단어나 구문의 줄임말입니다. 친근하고 비격식적인 톤을 유지하기 위해 축약형을 사용합니다. 그러나 명사와 동사 축약형이나 이중 축약형, 또는 두 축약형의 조합은 사용하지 않습니다. 이는 문장의 흐름과 일관성을 방해할 수 있습니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장: <em>축약형을 사용합니다</em></th><th style="width: 50%;">비권장: <em>명사와 동사 축약형을 사용합니다</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">If you're an admin, you can manage your company's contact information.</td><td style="width: 50%;">Braze'll now support Shoptify integration.</td></tr>
<tr><td style="width: 50%;">You can't edit an archived campaign.</td><td style="width: 50%;">You mightn't've seen the restricted upload size.</td></tr>
</tbody>
</table>
{:/}

#### 매달린 수식어와 잘못 배치된 수식어 {#dangling-and-misplaced-modifiers}

수식어는 다른 단어나 구문을 수식하는 단어나 구문입니다. 매달린 수식어는 문장에서 어떤 주어도 수식하지 않습니다. 잘못 배치된 수식어는 수식하려는 주어에서 멀리 배치됩니다. 본질적으로 매달린 수식어와 잘못 배치된 수식어는 문장의 잘못된 부분에 연결되어 혼란을 야기할 수 있습니다.

능동태로 작성하면 매달린 수식어와 잘못 배치된 수식어의 사용을 방지할 수 있습니다. 명확하게 수식하는 수식어를 사용해야 합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장: <em>문장을 짧고 간결하게 유지합니다. 능동태를 사용합니다.</em></th><th style="width: 50%;">비권장: <em>혼란을 야기할 수 있는 수식어가 포함된 긴 문장을 사용합니다</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">고객은 SAML 설정을 구성해야 합니다.</td><td style="width: 50%;">캠페인에 삭제할 수 있는 테스트 메시지가 있을 수 있습니다.</td></tr>
<tr><td style="width: 50%;">캠페인 초안을 저장하세요.</td><td style="width: 50%;">집에 가는 길에 Sarah는 금으로 된 남자의 회중시계를 발견했습니다.</td></tr>
</tbody>
</table>
{:/}

#### 전치사 {#prepositions}

가독성이 향상되는 경우 전치사로 문장을 끝내는 것은 문제가 없습니다. 전치사나 전치사구를 문장에서 가장 적합한 위치에 배치합니다. 어려움이 있으면 문장을 소리 내어 읽어보고 자연스럽게 들리는지 확인합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Each option corresponds to the priority the notification appears in.</td><td style="width: 50%;">Each option corresponds to the priority in which the notification appears.</td></tr>
<tr><td style="width: 50%;">For details, see the SDK documentation for the platform you're working with.</td><td style="width: 50%;">For details, see the SDK documentation for the platform with which you're working.</td></tr>
</tbody>
</table>
{:/}

#### 현재 시제 {#present-tense}

미래 시제 대신 현재 시제를 사용합니다. 현재 시제는 즉시성을 전달하고 자신감을 보여줍니다. 특히 사용자 동작의 결과를 언급할 때 "will"이나 가정적인 "would"를 사용하지 않습니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">보관된 구독 그룹은 편집할 수 없으며 세그먼트 필터에 더 이상 표시되지 않습니다.</td><td style="width: 50%;">보관된 구독 그룹은 편집할 수 없으며 세그먼트 필터에 더 이상 표시되지 않을 것입니다.</td></tr>
<tr><td style="width: 50%;">짧은 코드를 사용하는 것이 링크를 포함하기에 가장 안정적인 번호 유형입니다.</td><td style="width: 50%;">짧은 코드를 사용하는 것이 링크를 포함하기에 가장 안정적인 번호 유형일 것입니다.</td></tr>
</tbody>
</table>
{:/}

실제로 미래에 대해 이야기할 때만 미래 시제를 사용합니다. [미래 기능](#describing-limitations)을 예측하지 않습니다.

#### 비속어 {#profanity}

전체 이용가 수준을 유지합니다. 이는 도덕성보다는 비속어가 우리처럼 광범위하고 국제적인 오디언스에게 분열적이고 불쾌할 수 있다는 사실과 관련이 있습니다. 또한 비속어가 때때로 미완성된 글의 은폐물이라는 주장도 있습니다. 그것은 우리의 스타일이 아닙니다.

#### 괄호 안의 복수형 {#plurals-in-parentheses}

괄호 안에 복수형을 사용하지 않습니다. 대신 단어의 복수형이나 단수형을 사용합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">다음 필터로 캠페인을 커스터마이즈합니다.</td><td style="width: 50%;">다음 필터(들)로 캠페인을 커스터마이즈합니다.</td></tr>
</tbody>
</table>
{:/}

#### 2인칭과 1인칭 {#second-person-and-first-person}

지시 사항에서 1인칭 대신 2인칭을 사용합니다. "we"가 아닌 "you"를 사용합니다.

독자를 동작을 수행하는 사람으로 지칭합니다. 대화적인 톤을 유지합니다. 대부분의 독자는 지원 담당자에게 즉시 접근할 수 없을 때 문서를 찾습니다. 문서가 독자에게 직접 말하는 것처럼 느끼게 합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">변형을 추가하려면...</td><td style="width: 50%;">변형을 추가하려면(we)...</td></tr>
</tbody>
</table>
{:/}

독자에게 무언가를 하라고 말하는 경우 "you"를 생략하고 명령형을 사용할 수 있습니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">CSV 파일을 업로드합니다.</td><td style="width: 50%;">CSV 파일을 업로드할 수 있습니다.</td></tr>
<tr><td style="width: 50%;">제출을 선택합니다.</td><td style="width: 50%;">제출을 선택해야 합니다.</td></tr>
</tbody>
</table>
{:/}

2인칭을 사용할 때 문서의 오디언스가 누구인지 파악하고, 누구에게 말하고 있는지 일관성을 유지합니다.

#### 속어와 관용구 {#slang-and-idioms}

우리는 솔직한 사람들입니다. 특정 오디언스에게만 해당되는 유행 속어나 관용구를 사용하지 않습니다. 이는 자료를 빠르게 구식으로 만들고 콘텐츠를 현지화하기 어렵게 만들 수 있습니다.

#### 철자 {#spelling}

영국 영어와 다른 단어에는 미국 영어 철자를 사용합니다. 단어의 철자가 확실하지 않으면 먼저 [용어집](#glossary)을 참조합니다. 용어집에 나열되지 않은 경우 [Merriam-Webster's Collegiate Dictionary](https://www.merriam-webster.com/)를 참조합니다.

악센트가 있거나 특수 문자가 포함된 단어의 경우 사전 철자를 정확히 따릅니다. 경우에 따라 이러한 악센트를 의도치 않게 생략하면 다른 단어가 될 수 있습니다. 예를 들어, "resume"은 중단 후 다시 시작한다는 의미이고, "résumé"는 자격 요건의 요약입니다.

### 구두점 {#punctuation}

#### 앰퍼샌드 {#ampersands}

사용자 인터페이스를 직접 참조하는 경우가 아니면 텍스트나 제목에서 "and" 대신 앰퍼샌드(&)를 사용하지 않습니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Drag-And-Drop Editor</td><td style="width: 50%;">Drag & Drop Editor</td></tr>
<tr><td style="width: 50%;">SMS and MMS</td><td style="width: 50%;">SMS & MMS</td></tr>
</tbody>
</table>
{:/}

#### 아포스트로피 {#apostrophes}

아포스트로피는 명사를 소유격으로 만들 때 가장 자주 사용합니다.

* S로 끝나는 단수 명사의 경우 아포스트로피 뒤에 S를 추가해도 됩니다.
 * **예시:** Chris's, business's, alias's
* S로 끝나는 복수 명사의 경우 아포스트로피만 추가하고 S는 추가하지 않습니다.
 * **예시:** users'

#### 콜론 {#colons}

목록이나 예시 앞의 소개 구문 끝에 콜론을 사용합니다. 소개 문장은 완전한 문장으로 독립할 수 있어야 합니다. 이는 접근성과 현지화 목적 모두를 위한 것으로, 문장 조각은 번역하기 어렵습니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">일반적인 구조는 다음과 같습니다:</td><td style="width: 50%;">일반적인 구조는:</td></tr>
</tbody>
</table>
{:/}

콜론 앞의 텍스트가 굵은 글씨인 경우 콜론도 굵게 표시합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><strong>스케줄:</strong> 시간 기반 진입.</td><td style="width: 50%;"><strong>스케줄</strong>: 시간 기반 진입.</td></tr>
</tbody>
</table>
{:/}

콜론 앞의 텍스트가 코드 텍스트인 경우 코드 요소의 일부가 아닌 한 콜론을 코드 텍스트에 포함하지 않습니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>user_alias_label</code>: 사용자 별칭을 그룹화하기 위한 공통 레이블입니다.</td><td style="width: 50%;"><code>user_alias_label:</code> 사용자 별칭을 그룹화하기 위한 공통 레이블입니다.</td></tr>
</tbody>
</table>
{:/}

콜론을 사용하여 문장에서 두 개의 관련 구문을 연결할 수도 있습니다. 그러나 이 용도로는 콜론을 드물게 사용합니다. 두 문장이 일반적으로 더 읽기 쉽습니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">다음 주 예정: West Village 투어를 갑니다.</td></tr>
</tbody>
</table>
{:/}


#### 쉼표 {#commas}

Braze는 지시 사항이나 학습 콘텐츠를 작성할 때 옥스퍼드(직렬) 쉼표를 사용합니다. 시리즈에서 항목을 구분하기 위해 마지막 접속사 앞에 쉼표를 사용합니다.

소개 구문 뒤에 쉼표를 사용합니다.

등위 접속사("and", "but", "or", "yet", "so" 등)가 두 개의 독립절을 분리하는 경우 첫 번째 절 뒤와 접속사 앞에 쉼표를 배치합니다. 그러나 두 절이 모두 짧은 경우 이 쉼표는 필요하지 않습니다.

예를 들어, 다음은 두 개의 독립절입니다:

* "모든 필드는 선택 사항입니다."
* "최소 하나의 필드를 지정해야 합니다."

등위 접속사 "but"을 사용한 문장은 "모든 필드는 선택 사항이지만, 최소 하나의 필드를 지정해야 합니다."입니다.

독립절과 종속절이 같은 문장에 사용되는 경우 쉼표로 구분하지 않습니다. 쉼표 없이 문장이 잘못 해석될 수 있는 경우에만 이 시나리오에서 쉼표를 사용합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">푸시 구독 상태는 필터이며 사용자가 알림 기본 설정을 편집할 수 있도록 합니다.</td><td style="width: 50%;">푸시 구독 상태는 필터이며, 사용자가 알림 기본 설정을 편집할 수 있도록 합니다.</td></tr>
</tbody>
</table>
{:/}

#### 대시 {#dashes}

##### 엠 대시

문장에서 별도의 생각이나 중단을 나타내기 위해 대시를 사용할 때 엠 대시(—)를 사용합니다. 엠 대시 앞뒤에 공백을 넣지 않습니다. 쉼표나 괄호가 동일하게 작동하는 곳에서는 엠 대시를 사용하지 않습니다.

엠 대시를 입력하는 방법은 운영체제를 참조하세요:

* **macOS:** Option + Shift + Hyphen을 누릅니다.
* **Windows:** Num Lock을 켜고 왼쪽 Alt 키를 누른 상태에서 숫자 패드에 0151을 입력합니다.

##### 엔 대시 {#en-dash}

숫자 범위, 빼기 기호, 음수를 나타내기 위해 엔 대시(–)를 사용합니다. 빼기 기호로 사용되는 경우를 제외하고 엔 대시 앞뒤에 공백을 넣지 않습니다. 하이픈(-)을 사용하지 않습니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장: <em>숫자 범위에 엔 대시를 사용합니다</em></th><th style="width: 50%;">비권장: <em>하이픈을 사용합니다</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">2018–2021</td><td style="width: 50%;">2018-2021</td></tr>
</tbody>
</table>
{:/}

시간 범위에는 엔 대시를 사용하지 않습니다. 자세한 내용은 [날짜와 시간](#dates-and-times) 섹션을 참조하세요.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장: <em>빼기 기호에 엔 대시를 사용하고 엔 대시 주위에 공백을 포함합니다</em></th><th style="width: 50%;">비권장: <em>하이픈을 사용합니다</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">15 – 5 = 10</td><td style="width: 50%;">15-5=10</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장: <em>음수에 엔 대시를 사용합니다</em></th><th style="width: 50%;">비권장: <em>하이픈을 사용합니다</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">–30</td><td style="width: 50%;">-30</td></tr>
</tbody>
</table>
{:/}

엔 대시를 입력하는 방법은 운영체제를 참조하세요:

* **macOS:** Option + Hyphen을 누릅니다.
* **Windows:** Num Lock을 켜고 왼쪽 Alt 키를 누른 상태에서 숫자 패드에 0150을 입력합니다.

#### 줄임표 {#ellipses}

줄임표는 하나 이상의 단어가 생략되었음을 나타내는 세 개의 마침표(...)입니다. 일반적으로 지시 사항이나 학습 콘텐츠를 작성할 때 줄임표 사용을 가능한 한 피합니다.

#### 느낌표 {#exclamation-points}

비격식적인 톤을 위해 느낌표를 드물게 사용할 수 있습니다. 그러나 텍스트 전체에 느낌표를 과도하게 사용하지 않습니다. 대신 [알림](#callouts-and-alerts) 사용을 고려합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장: <em>알림과 소개에 비격식적인 톤으로 느낌표를 사용합니다</em></th><th style="width: 50%;">비권장: <em>독자에게 경고나 주의를 나타내기 위해 느낌표를 사용합니다</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">페이지를 떠나기 전에 변경 사항을 저장하세요!</td><td style="width: 50%;">사용자는 고유 수신자로 집계되려면 단계에서 하나 이상의 메시지를 받아야 합니다!</td></tr>
</tbody>
</table>
{:/}

#### 하이픈 {#hyphens}

하이픈은 구문의 단어를 연결하여 독자가 문장에서 더 명확하게 이해할 수 있도록 도와줍니다. 올바르게 사용하기 위한 몇 가지 가이드라인입니다.

독자가 주어를 더 명확하게 이해할 수 있도록 복합 수식어에 하이픈을 사용합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">real-time data streaming</td></tr>
</tbody>
</table>
{:/}

수식어와 주어 사이에 공백을 두고 구문을 연결하기 위해 하이픈을 사용합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">All-in-one solutions</td></tr>
</tbody>
</table>
{:/}

주어를 수식하는 구문에 하이픈을 사용합니다. 구문이 주어인 경우 하이픈을 사용할 필요가 없습니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">It was a well-known fact.</td><td style="width: 50%;">That fact is well-known</td></tr>
</tbody>
</table>
{:/}

문장에서 일시 정지를 만들기 위해 엠 대시 대신 하이픈을 사용하지 않습니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">...third-party integrations—such as Slack—and automate...</td><td style="width: 50%;">...third-party integrations-such as Slack-and automate...</td></tr>
</tbody>
</table>
{:/}

부사 뒤에 하이픈을 사용하지 않습니다. 단어를 분리하여 유지합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Hastily made</td><td style="width: 50%;">Hastily-made</td></tr>
</tbody>
</table>
{:/}

#### 괄호 {#parentheses}

괄호는 드물게 사용합니다. 일부 독자는 괄호 안의 내용을 건너뛰므로 중요한 정보를 괄호 안에 넣지 않습니다.

덜 중요한 괄호 내용의 경우 괄호를 제거하도록 문장을 재구성하는 것을 고려합니다. 예를 들어, 쉼표, 대시, 세미콜론을 사용하여 구문이나 문장을 구분하거나 새 문장을 추가할 수 있습니다.

괄호가 더 큰 문장의 일부인 경우 마침표를 괄호 밖에 배치합니다. 괄호가 완전한 문장을 포함하는 경우 마침표를 안에 배치합니다.

**관련 섹션:** [괄호 안의 복수형](#plurals-in-parentheses)

#### 마침표 {#periods}

문장을 끝내기 위해 마침표를 사용합니다. 헤드라인, 제목, 부제목, UI 요소를 끝내기 위해 마침표를 사용하지 않습니다.

목록 항목에 마침표를 사용하는 시기에 대한 가이드라인은 [목록](#lists)을 참조하세요.

#### 세미콜론 {#semicolons}

세미콜론은 더 길고 복잡한 문장을 나누는 데 유용합니다. 주제가 밀접하게 관련된 두 개의 독립절을 구분하기 위해 세미콜론을 사용합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">권장: <em>관련된 두 개의 독립절이 있는 문장을 나누기 위해 세미콜론을 사용합니다</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">고양이는 폭풍 속에서 잠을 잤고; 개는 침대 아래에서 웅크렸습니다.</td></tr>
</tbody>
</table>
{:/}

목록 항목 중 하나(또는 그 이상)에 쉼표가 포함된 경우 세미콜론을 사용하여 목록 항목을 구분할 수 있습니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">권장: <em>더 긴 문장을 나누기 위해 세미콜론을 사용합니다</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Jane Lang, our moderator; Simon Mayer, CEO and Cofounder of PantsLabyrinth; and Kara Seberg, CMO of Yachtr.</td></tr>
</tbody>
</table>
{:/}

#### 슬래시 {#slashes}

슬래시에는 역슬래시(\\)와 정슬래시(/) 두 가지 유형이 있습니다. 대체 단어나 예시를 나타내기 위해 슬래시를 사용하지 않습니다("and/or").

파일 경로와 URL에서 필요에 따라 슬래시를 사용합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장: <em>파일 경로에 슬래시를 사용합니다</em></th><th style="width: 50%;">비권장: <em>대안을 구분하기 위해 슬래시를 사용합니다</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>/campaigns/data_series</code></td><td style="width: 50%;">you/your customers</td></tr>
</tbody>
</table>
{:/}

#### 따옴표 {#quotation-marks}

따옴표에는 직선형(" ")과 곡선형(" ") 두 가지 유형이 있습니다. 마침표와 쉼표는 따옴표 안에 넣습니다. 예외는 따옴표가 문자열과 같은 정확한 정보를 포함하는 경우입니다. 사용자에게 텍스트 필드에 특정 텍스트 문자열을 입력하도록 안내할 때 따옴표를 사용합니다.

{% alert note %}

검색 구문을 설명할 때 따옴표는 종종 정확한 텍스트를 검색하는 것을 의미합니다. 이 경우 텍스트 문자열 주위에 대괄호를 사용하고 검색 구문에서 요구하는 대로 따옴표를 사용합니다. 예를 들어: <br><br>

*["test segment"]와 같이 단어나 구문 주위에 따옴표를 넣으면 정확히 해당 단어나 구문만 포함하는 결과를 표시합니다.*

{% endalert %}

코드 예시에서는 직선형 따옴표를 사용해야 합니다. 텍스트에서 코드 서식 지정에 대한 자세한 내용은 [텍스트 내 코드](#code-in-text)를 참조하세요.

### 기술 문서 {#technical-documentation}

#### API 엔드포인트 {#api-endpoints}

일반적으로 API 엔드포인트 문서는 이 스타일 가이드의 가이드라인을 따라야 합니다. 그러나 이 문서에 나열된 다른 콘텐츠 가이드라인이 필요할 수 있는 특수한 주제가 있습니다. 엔드포인트의 서식 지정 및 참조 방법에 대한 자세한 내용은 [API 엔드포인트 문서 가이드라인]({{site.baseurl}}/contributing/style_guide/api_endpoint_guidelines/)을 참조하세요.

#### 보증 피하기 {#avoid-guarantees}

문서에서 법적 영향을 초래할 수 있는 약속을 하지 않아야 합니다. "보증" 또는 "보장"과 같은 확정적인 용어를 사용하지 않습니다. 대신 "~하도록 설계됨" 또는 "~을 목적으로 함"과 같은 전향적 표현을 사용하여 제품의 기능과 의도를 정확하게 전달합니다.

#### UI와의 상호작용 설명 {#describing-interactions-with-the-ui}

UI 요소를 참조할 때 UI에 표시되는 대로 대문자 표기를 맞춥니다. 그러나 레이블이 모두 대문자인 경우 문장 대소문자를 사용합니다(예외: AND 또는 OR 연산자와 같은 짧은 레이블).

독자에게 UI와 상호작용하도록 지시할 때 상호작용하는 UI 요소를 굵게 표시합니다. 사용자가 필드에 입력하는 문자열에는 따옴표를 사용합니다.

UI와의 상호작용을 설명할 때 사용할 동사에 대한 안내는 다음 표를 참조하세요:

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<colgroup>
<col style="width: 20%;">
<col style="width: 40%;">
<col style="width: 40%;">
</colgroup>
<thead>
<tr><th>동사</th><th>사용법</th><th>예시</th></tr>
</thead>
<tbody>
<tr><td>Open</td><td><ul><li>앱 열기</li><li>파일 및 폴더 열기</li></ul></td><td><ul><li>Droidboy를 엽니다.</li><li>braze.xml 파일을 엽니다.</li></ul></td></tr>
<tr><td>Close</td><td><ul><li>앱 닫기</li><li>파일 및 폴더 닫기</li></ul></td><td><ul><li>Droidboy를 닫습니다.</li><li>braze.xml 파일을 닫습니다.</li></ul></td></tr>
<tr><td>Go to</td><td><ul><li>UI의 특정 페이지로 이동(탭, 페이지, 섹션)</li><li>웹페이지로 이동</li></ul></td><td><ul><li><strong>Segments</strong> 페이지로 이동하여 클릭합니다…</li><li>example.com으로 이동하여 가입합니다.</li></ul></td></tr>
<tr><td>&gt;</td><td>모든 단계가 동일한 유형일 때 일련의 단계를 따릅니다.</td><td><strong>Segments</strong> &gt; <strong>세그먼트 인사이트</strong>로 이동합니다.</td></tr>
<tr><td>Choose</td><td>주관적이거나, 전략적이거나, 개방적이거나, 복잡한 결정을 내립니다.</td><td>캠페인 전략을 선택합니다.</td></tr>
<tr><td>Select</td><td><ul><li>체크박스 선택</li><li>드롭다운에서 항목 선택</li><li>탭 선택</li><li>간단한 결정 내리기</li></ul></td><td><ul><li><strong>Show Password</strong>를 선택합니다.</li><li>드롭다운에서 데이터 유형을 선택합니다.</li><li><strong>설정 관리</strong> 페이지에서 <strong>커스텀 이벤트</strong> 탭을 선택합니다.</li><li>이미지를 선택합니다.</li></ul></td></tr>
<tr><td>Clear</td><td>체크박스에서 선택을 해제합니다.</td><td><strong>Show Password</strong> 체크박스를 해제합니다.</td></tr>
<tr><td>Select</td><td>UI에서 요소를 선택합니다.</td><td>커스텀 속성을 추가하고 <strong>저장</strong>을 선택합니다.</td></tr>
<tr><td>Turn on</td><td>토글 옵션을 활성화합니다.</td><td><strong>List-Unsubscribe header</strong>를 켭니다.</td></tr>
<tr><td>Turn off</td><td>토글 옵션을 비활성화합니다.</td><td><strong>Inline CSS on New Emails by Default</strong>를 끕니다.</td></tr>
<tr><td>Enter</td><td>값을 입력합니다.</td><td><ul><li>텍스트 필드에 커스텀 속성의 이름을 입력합니다.</li><li>소스 이름으로 "Braze"를 입력합니다.</li></ul></td></tr>
</tbody>
</table>
{:/}

#### 제한 사항 설명 {#describing-limitations}

제품의 제한 사항에 대해 왜곡이나 조작 없이 솔직하게 작성합니다. 독자는 조작당하거나 속는 것에 강하게 반응하며, 이는 문서의 실용적 진실의 원천으로서의 효과를 위태롭게 합니다. 고객은 Braze를 성공적으로 사용할 수 있도록 구축하고 있는 시스템의 한계를 이해하기 위해 문서에 의존합니다.

동시에 적절하고 긍정적인 맥락으로 제한 사항을 프레이밍하여 제품 개발의 의도성을 지원합니다.

* 소프트 제한(예: API 사용량 제한)이 있는 경우 **기본 한도** 또는 **시작 할당량**에 대해 이야기하여 제한을 프레이밍합니다.
* 소프트 제한을 탐색하기 위한 의미 있는 경로를 제공합니다. 적절한 경우 이러한 해결 방법의 예시를 제공합니다.
 * 예를 들어, Braze는 온보딩 중 사이징 연습을 사용하여 고객이 유사한 규모의 다른 비즈니스에서 데이터 포인트와 같은 것이 어떻게 사용되는지 이해하도록 돕습니다. 데이터 포인트를 논의할 때 동시에 사이징 연습에 대해 이야기하는 것이 적절합니다.
* 완화 조치보다는 긍정적인 방식으로 경로를 설명하는 것이 좋습니다.
 * 예를 들어, "Braze는 고객이 직접 이 작업을 수행할 수 없습니다. 지원팀이 이 기능을 활성화해야 합니다."라고 말하는 대신 "이 기능을 활성화하려면 지원팀에 문의하세요."라고 말합니다.
* 소프트 제한을 탐색하기 위해 동일한 상투적 문구에 과도하게 의존하지 않습니다. 사용자가 "고객 서비스 담당자에게 문의하세요"를 반복적으로 읽으면 조언이 무의미해집니다.
* 하드 제한이 있는 경우 이 제한의 근거를 설명합니다.
 * 예를 들어: "메시지 전달 속도를 최적화하고 시간 초과를 방지하기 위해 앱 그룹당 200개의 활성 실행 기반 인앱 메시지 캠페인 제한이 있습니다. …평균 Braze 고객은 한 번에 총 26개의 캠페인을 활성화하므로 이 제한이 영향을 미칠 가능성은 낮습니다."
* 현재 제한 사항을 설명하기 위해 [계획된 기능이나 미래 기능](#future-features)을 설명하지 않습니다.
* 커스텀 데이터 관련 제한을 언급할 때 "제한" 대신 "용량"이라는 용어를 사용합니다.
 * 예를 들어: 기본적으로 워크스페이스당 20개의 세분화 가능한 이벤트 등록정보를 가질 수 있습니다. 용량을 늘리려면 Braze 계정 매니저에게 문의하세요.

#### 미래 기능 {#future-features}

미래 기능에 대한 언급이나 향후 지원될 수 있다는 암시를 피합니다.

글을 특정 시점에 고정시키는 단어와 구문을 사용하지 않습니다. 이는 콘텐츠를 빠르게 구식으로 만듭니다. 변경된 사항이 아닌 제품이 현재 어떻게 작동하는지에 초점을 맞춥니다(릴리스 노트와 같은 시간 중심 콘텐츠 제외).

특히 Google의 [개발자 문서 스타일 가이드](https://developers.google.com/style/timeless-documentation)에서 가져온 다음 단어와 구문 목록을 피합니다:

* as of this writing
* currently
* does not yet
* eventually
* future, in the future
* latest
* new, newer
* now
* old, older
* presently, at present
* soon

#### 기능 지원 중단 {#features-deprecations}

기능 지원 중단에 대한 정보를 포함하기 전에 독자가 기능이 지원 중단될 것으로 예상할 수 있는 대략적인 시간 프레임(예: 2025년 하반기)이 있는지 확인합니다.

대략적인 시간 프레임이 있으면 기능 지원 중단을 조기에 알립니다. 독자가 무엇을 기대해야 하는지 명확하게 이해할 수 있도록 지원 중단에 대해 명확하게 작성합니다.

독자에게 두려움, 불확실성, 의심을 불러일으킬 수 있는 구문을 사용하지 않습니다. 지원 중단된 기능이 무엇으로 대체되는지 또는 대안 솔루션과 같은 명확한 경로를 제공합니다.

#### 일반적 vs 구체적 {#general-vs-specific}

모범 사례로, 일반적으로 적용 가능한 방식으로 기능을 논의하는 문서를 작성합니다. 특정 사례나 예외에 대해 더 자세한 내용이 필요한 경우 이 예외를 설명하는 별도의 섹션(또는 콘텐츠가 웹 문서 길이인 ~500단어인 경우 별도의 문서)을 만듭니다. 일반 문서에서 구체적 문서로의 상호 참조를 만들어 사용자가 이러한 개념을 연결할 수 있도록 합니다.

다른 채널이나 기능에 대해 중복되거나 반복적인 콘텐츠를 만들지 않습니다. 반복이 필요한 경우 `includes` 파일과 기타 [재사용 가능한 콘텐츠 모범 사례]({{site.baseurl}}/contributing/content_management/reusing_content)를 사용합니다.

**예시:** Braze 고객의 일반적인 활용 사례는 이전에 메시징과 상호작용한 사용자를 리타겟팅하는 것입니다. 사용자 리타겟팅은 캠페인, 캔버스, 랜딩 페이지, 세그먼트를 포함한 많은 참여 툴을 통해 수행할 수 있습니다. 사용자 리타겟팅은 WhatsApp, SMS, 콘텐츠 카드, 이메일, 푸시 알림 등 많은 채널을 통해 수행할 수 있습니다. 종종 고객은 이전에 사용한 것과 다른 채널을 통해 사용자를 재참여시키려고 합니다.
각 참여 툴과 각 채널에 대해 하나의 문서를 만드는 대신, 사용자 리타겟팅 전략을 논의하고 사용 가능한 모든 옵션을 설명하는 단일 문서를 만듭니다. 특정 채널/도구에 대한 특별한 고려 사항이 있는 경우 해당 고려 사항을 설명하는 별도의 문서를 만들어 해당 문서 섹션에 배치합니다. 일반 문서와 구체적 문서 사이에 상호 참조를 만듭니다.

#### 메타데이터와 YAML {#metadata-and-yaml}

Braze 문서의 문서에는 검색 및 색인 목적으로 특정 메타데이터가 필요합니다. 필요한 메타데이터에 대한 정보는 GitHub 페이지의 [YAML 및 메타데이터 레이아웃](https://github.com/braze-inc/braze-docs/wiki/YAML-%26-Metadata-Layouts)을 참조하세요.

#### 명명 규칙 {#naming-conventions}

문서와 파일 이름을 지정할 때 제목에 일반적인 주제를 설명해야 합니다. 특히 문서 제목에는 독자가 쉽게 이해할 수 있는 키워드와 간략한 설명을 항상 포함합니다.

파일 이름의 경우 이름을 간결하게 유지하고 관사(a, an, the)를 사용하지 않습니다. 각 단어를 밑줄(_)로 구분합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Targeting users</td></tr>
<tr><td style="width: 100%;">Creating an email campaign</td></tr>
<tr><td style="width: 100%;">API errors and responses</td></tr>
<tr><td style="width: 100%;">sms_historical_performance.png</td></tr>
<tr><td style="width: 100%;">push_notification_test.png</td></tr>
</tbody>
</table>
{:/}

일반적으로 문서와 이미지 파일의 경우 참조된 문서 및 파일과 동일한 철자와 대문자 표기를 사용합니다. 문서 제목 스타일링에 대한 가이드라인은 [제목과 타이틀](#headings-and-titles)을 참조하세요.

특정 파일을 참조할 때 파일 이름과 동일한 철자와 코드 글꼴을 사용합니다. 서식 세부 사항은 GitHub 페이지의 [특수 서식](https://github.com/braze-inc/braze-docs/wiki/Special-Formatting)을 참조하세요.

#### 절차와 지시 사항 {#procedures-and-instructions}

이 섹션에서는 Braze 대시보드의 절차에 대한 지시 사항을 작성할 때 염두에 두어야 할 몇 가지 가이드라인을 다룹니다.

일반 가이드라인:

* **적절한 톤을 사용합니다.** 지시 사항의 경우 글을 짧고, 요점에 맞게, 작업 지향적으로 유지합니다. 글이 딱딱하거나 건조할 필요는 없지만 직접적이어야 합니다. 작업이나 하위 작업을 소개할 때 다양성을 더하기 위해 더 비격식적인 톤을 사용할 수 있습니다. 톤을 비격식적으로 유지하기 위해 "please"를 사용하지 않습니다. 축약형을 자유롭게 사용하여 톤을 친근하게 유지합니다.
* **병렬 제목 형식을 따릅니다.** 제목에 하나의 형식을 선택하고 일관되게 유지합니다. 콘텐츠를 스캔 가능하고 예측 가능하게 유지합니다. 작업 기반 제목과 페이지 제목에는 명령형 동사를 선호합니다(예: "이메일 캠페인 만들기").

지시 사항 전:

* **소개와 필수 조건을 사용합니다.** 바로 단계로 들어가지 않습니다. 대신 문서나 섹션이 다루는 내용에 대한 맥락을 제공하고, 독자가 지시 사항을 스캔하기 전에 알아야 할 정보를 제공합니다. 모든 필수 조건은 "필수 조건" 제목으로 문서 상단에 나열합니다. 이 섹션의 표 헤더는 "요구 사항"이어야 합니다. "요구 사항"은 Braze, 제3자 제공업체 또는 파트너의 요구 사항을 명시하는 데 사용할 수 있는 용어입니다.
* **절차의 시작부터 시작합니다.** 독자가 이전 단계를 완료한 후 이 페이지에 도달했다고 가정하지 않습니다. 작업에 대한 지시 사항이 다른 작업이 끝난 곳에서 시작되는 경우 독자가 절차에서 어디에 있는지, 이 단계 전에 무엇을 완료해야 하는지에 대한 개요를 제공합니다. 이전 단계에 대한 링크를 포함합니다.

지시 사항 작성:

* **실행 가능한 언어를 사용합니다.** 제품이 할 수 있는 것이 아닌 사용자가 할 수 있는 것을 중심으로 문서를 구조화합니다. "이 기능은 [xyz를 합니다]"와 같은 언어를 피합니다. 대신 "이 기능을 사용하여 [xyz를 합니다]"라는 관점에서 생각합니다.
* **필요한 경우 위치 단계를 제공합니다.** "**설정** 페이지에서 **편집**을 선택합니다."와 같은 간단한 구문으로 독자가 올바른 위치를 보고 있는지 확인합니다. 충분히 명확하지 않을 수 있는 경우 소개 단계를 제공합니다. 예를 들어, "**설정 관리**로 이동하여 **설정** 탭을 선택합니다."
* **조건문을 앞에 배치합니다.** [조건절](#clause-order)을 먼저 배치합니다. 조건부 지시 사항의 경우 독자가 조건이 적용되지 않으면 단계를 건너뛸 수 있도록 "if"로 단계를 시작합니다. 예를 들어, "X가 필요한 경우 A > B > C를 수행합니다."
* **작업 순서를 강화합니다.** 일련의 단계 내 진행 상황에는 "완료한 후" 또는 "완료하면"이라는 구문을 사용합니다. 작업 간 진행 상황에는 "이제 완료했으므로" 또는 "완료한 후"로 섹션을 시작합니다. "Once you've"라는 구문은 번역이 잘 되지 않으므로 피합니다.

#### 탭 {#tabs}

탭은 기술 문서에서 그룹화된 정보를 구성하는 방법으로 사용할 수 있습니다.

탭은 워크플로 요약을 보여주거나 그룹화된 정보를 구성하기 위해 지시 사항을 작성할 때 사용할 수 있는 요소를 말합니다. 이는 표나 목록과 유사하지만 정보가 패널로 그룹화됩니다.

중복을 피하거나 독자를 위해 워크플로를 시각화하기 위해 정보를 함께 그룹화할 수 있는 경우 탭 사용을 고려합니다. 탭에 병렬 정보가 포함되어 있는지 확인하고, 독자가 워크플로에서 순차적 단계를 따라야 하는 경우에는 사용하지 않습니다.

예를 들어, 탭을 사용하여 다른 프로그래밍 언어의 코드 예시를 표시할 수 있습니다. 이 경우 독자는 문서를 스크롤하는 대신 탭 레이블을 기반으로 예시 간에 전환합니다.

서식 세부 사항은 GitHub 페이지의 [특수 서식](https://github.com/braze-inc/braze-docs/wiki/Special-Formatting)을 참조하세요. 또는 [목록](#lists)이나 [표](#tables-1)를 사용하여 정보를 구성할 수도 있습니다.

### 서식 지정과 구성 {#formatting-and-organizing}

#### 주소 {#addresses}

숫자 뒤에 거리 이름을 다음과 같이 사용합니다:

*330 W. 34th St.*

전체 주소를 표시하려면 숫자, 거리 이름, 도시, 주, 우편번호를 사용합니다. 주와 우편번호 사이에 쉼표가 필요하지 않습니다.

*330 W. 34th St., New York, NY 10001*

#### 버튼 레이블 {#buttons-labels}

버튼 레이블은 명확하고 예측 가능해야 합니다. 사용자는 버튼을 선택할 때 어떤 동작이 발생하는지 알아야 합니다. 버튼 레이블에는 문장 대소문자를 사용하고 강한 동사로 시작합니다. 동사가 무엇을 지칭하는지 불분명할 수 있는 경우 [동사] + [명사] 형식을 사용합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Sign up</td><td style="width: 50%;">Sign Up</td></tr>
<tr><td style="width: 50%;">Log in</td><td style="width: 50%;">Log In</td></tr>
<tr><td style="width: 50%;">Subscribe</td><td style="width: 50%;">SUBSCRIBE</td></tr>
<tr><td style="width: 50%;">Learn more</td><td style="width: 50%;">More</td></tr>
</tbody>
</table>
{:/}

"a", "an", "the"와 같은 불필요한 단어와 관사를 생략합니다.

#### 콜아웃과 알림 {#callouts-and-alerts}

콜아웃이라고도 하는 알림은 독자에게 도움이 되는 정보에 주의를 끌기 위해 사용됩니다. 문서에서 사용되는 네 가지 알림 유형이 있습니다:

* Important
* Note
* Tip
* Warning

문서 전체에서 알림을 드물게 사용합니다. 자세한 내용은 [알림 모범 사례]({{site.baseurl}}/contributing/style_guide/alerts/)를 참조하세요.

#### 텍스트 내 코드 {#code-in-text}

문장 내에서 텍스트를 코드 글꼴로 서식 지정해야 하는 몇 가지 시나리오가 있습니다. 코드 글꼴로 표시해야 하는 항목의 불완전한 목록은 다음과 같습니다:

* 속성 이름과 값
* API 요청 매개변수
* 파일 이름
* 파일 경로
* 메서드, 변수 또는 매개변수 이름
* HTML 및 XML 요소 이름
* HTTP 상태 코드
* 터미널에 입력하는 텍스트

Braze 문서에서 인라인 코드 텍스트를 만들려면 텍스트를 백틱(`)으로 감쌉니다.

#### 코드 샘플 {#code-samples}

코드 샘플은 샘플 코드 스니펫을 표시하는 코드 텍스트 블록을 말합니다. 접근성을 위해 가능한 경우 설명 문장으로 코드 샘플을 소개합니다.

코드 샘플이 읽기 쉽도록 들여쓰기 수준당 두 칸씩 각 줄을 들여씁니다. 코드 샘플 서식 지정에 어려움이 있으면 [JSON Formatter](https://jsonformatter.org/json-pretty-print)와 같은 프리티 프린트 포매터를 사용하여 코드를 정리해 보세요.

Braze 문서에서 코드 블록을 만들려면 [코드 스니펫 테스트](https://github.com/braze-inc/braze-docs/blob/develop/_docs/_home/styling_test_page.md#code-snippet-test)를 참조하세요. 코드 블록은 적절한 구문 강조를 위해 언어 유형을 지정해야 합니다.

#### 날짜와 시간 {#dates-and-times}

월과 요일을 풀어 씁니다. 가능하면 약어를 피합니다. 월을 약어로 표기해야 하는 경우 다음만 약어로 표기합니다:

* Jan.
* Feb.
* Aug.
* Sept.
* Oct.
* Nov.
* Dec.

날짜와 연도를 구분하기 위해 [쉼표](#commas)를 사용합니다. 요일이 날짜와 함께 사용되는 경우 월 앞에 추가합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">권장: <em>선호하는 날짜 형식을 사용합니다.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">September 2021</td></tr>
<tr><td style="width: 100%;">September 15, 2021</td></tr>
<tr><td style="width: 100%;">Wednesday, September 15, 2021</td></tr>
</tbody>
</table>
{:/}

날짜 범위에는 [엔 대시](#en-dash)를 사용합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">2010–2021</td></tr>
</tbody>
</table>
{:/}

날짜 범위에 엔 대시를 사용합니다.

숫자와 am 또는 pm을 사용하고, 공백 뒤에 시간대(am 또는 pm)를 표시합니다. 정각 시간에서는 분을 제거합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장: <em>숫자와 am 또는 pm을 사용합니다.</em></th><th style="width: 50%;">비권장: <em>정각 시간에 분을 사용합니다(범위가 아닌 경우).</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">12 pm</td><td style="width: 50%;">12:00 P.M.</td></tr>
</tbody>
</table>
{:/}

시간 범위에는 엔 대시를 사용하여 구분합니다. 엔 대시 앞뒤에 공백을 추가하지 않습니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">권장: <em>시간 범위에 엔 대시를 사용합니다.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">12:45–2:30 pm</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">권장: <em>시간 범위에 분을 사용합니다.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">8:00 am–2:30 pm</td></tr>
</tbody>
</table>
{:/}

다른 시간대의 참가자가 포함된 경우(웨비나, 회의, 이벤트 등) 아래와 같이 시간대를 표시합니다:

* Eastern Standard Time: EST
* Central Standard Time: CST
* Mountain Standard Time: MST
* Pacific Standard Time: PST
* Greenwich Mean Time: GMT
* Coordinated Universal Time: UTC
* Central European Time: CET
* Eastern Europe Time: EET
* Western Europe Time: WET
* Singapore Time: SGT
* China Standard Time: CST

#### 이모지 {#emojis}

캐주얼한 분위기이지만 학습 콘텐츠에서 이모지 사용을 피합니다. 이모지는 다양한 방식으로 해석될 수 있으며 종종 비전문적으로 보입니다.

예외는 다음 시나리오를 포함합니다:

* 표에서 ✅와 ❌를 사용하여 지원되는 것과 지원되지 않는 것, 또는 권장되는 것과 권장되지 않는 것을 나타낼 때
* 캠페인이나 Canvas 메시지의 예시 카피에 사용될 때

#### 예시 이름 {#example-names}

실제 이름, 이메일 주소 또는 기타 개인 식별 정보(PII)를 사용하지 않습니다. 대신 가상의 예시나 [입력 안내 텍스트](#placeholder-text)를 사용합니다.

글에 이름을 포함해야 하는 경우 Wikipedia의 [Unisex names](https://en.wikipedia.org/wiki/Unisex_name) 목록을 참조합니다. 가능하면 "they", "their", "theirs" 대명사를 사용하고 특정 성별에 제한된 예시를 사용하지 않습니다.

##### 예시 이메일 주소

일반 이메일 주소에는 "name@example.com" 형식을 사용합니다. "name"을 예시 이름으로 대체합니다. 예를 들어:

* alex@example.com
* lee@example.com
* yuri@example.com

#### 그림과 기타 이미지 {#figures-and-other-images}

그림과 이미지를 만들 때 [이미지 카피 스타일 가이드]({{site.baseurl}}/contributing/style_guide/image_style_guide/)를 참조합니다. 그림이나 이미지에 개인 식별 정보(PII)를 포함하지 않습니다.

##### 대체 텍스트 {#alt-text}

이미지에 항상 대체 텍스트를 포함합니다. 스크린 리더는 시력을 잃은 사람들에게 이미지를 설명하기 위해 대체 텍스트를 읽어줍니다. 따라서 대체 텍스트는 이미지에 표시된 모든 핵심 정보를 전달해야 합니다.
대체 텍스트를 작성할 때 다음 가이드라인을 사용합니다:

* [쉬운 언어](https://www.plainlanguage.gov/guidelines/)를 사용합니다.
* 완전한 문장으로 작성하고 문장 대소문자를 사용합니다.
* 불필요한 단어를 생략합니다.
* "이미지" 또는 "사진"을 포함하지 않습니다. 이미지를 참조하고 있다는 것은 이미 이해됩니다.
* 특수 문자를 포함하지 않습니다. 예를 들어, 앰퍼샌드(&) 대신 "and"를 풀어 씁니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Braze 대시보드의 커스텀 이벤트 설정 페이지에서 Add Report가 강조 표시되어 있습니다.</td><td style="width: 50%;">Braze 대시보드의 Manage Settings > Custom Events 페이지 스크린샷으로 보고서 추가 옵션이 강조 표시되어 있습니다.</td></tr>
</tbody>
</table>
{:/}

이미지가 텍스트에서 설명된 내용에 중복되는 시각적 구성 요소를 추가하는 경우 대체 태그를 명시적으로 비워 둡니다(alt="").

모든 이미지에 대체 텍스트를 추가한다고 해서 웹페이지 콘텐츠가 자동으로 탐색하고 소비하기 쉬워지는 것은 아닙니다. 중복 시각 자료는 시각 정보가 이해하고 기억하기 쉽기 때문에 시력이 있는 사용자에게 강력합니다. 그러나 중복 이미지를 설명하는 대체 텍스트는 이미지를 볼 수 없는 사용자에게 불필요할 수 있습니다. 모든 페이지 요소가 스크린 리더 사용자에게 동일한 주의를 요구하여 작업에 유용한지 판단해야 하기 때문입니다.

##### 예시 회사 이름

가능하면 FakeBrandz 회사 이름 중 하나를 사용할 수 있도록 [dashboard-06](https://dashboard-06.braze.com/)에서 스크린샷을 찍습니다.

#### 파일 유형과 파일 이름 {#file-types-and-filenames}

파일 유형을 참조할 때 유형의 표준 이름을 사용합니다. 파일 유형이 약어인 경우 모두 대문자로 표기합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장: <em>파일 유형의 표준 이름을 사용합니다</em></th><th style="width: 50%;">비권장: <em>파일 확장자를 사용합니다</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">CSV</td><td style="width: 50%;">.csv</td></tr>
<tr><td style="width: 50%;">executable file</td><td style="width: 50%;">.exe</td></tr>
<tr><td style="width: 50%;">GIF</td><td style="width: 50%;">.gif</td></tr>
<tr><td style="width: 50%;">JAR</td><td style="width: 50%;">.jar</td></tr>
<tr><td style="width: 50%;">JPEG</td><td style="width: 50%;">.jpg, .jpeg</td></tr>
<tr><td style="width: 50%;">JSON</td><td style="width: 50%;">.json</td></tr>
<tr><td style="width: 50%;">PDF</td><td style="width: 50%;">.pdf</td></tr>
<tr><td style="width: 50%;">PNG</td><td style="width: 50%;">.png</td></tr>
<tr><td style="width: 50%;">Python file</td><td style="width: 50%;">.py</td></tr>
<tr><td style="width: 50%;">Bash file</td><td style="width: 50%;">.sh</td></tr>
<tr><td style="width: 50%;">text file</td><td style="width: 50%;">.txt</td></tr>
<tr><td style="width: 50%;">YAML</td><td style="width: 50%;">.yaml</td></tr>
<tr><td style="width: 50%;">ZIP</td><td style="width: 50%;">.zip</td></tr>
</tbody>
</table>
{:/}

파일 이름을 참조할 때 파일 이름을 코드 텍스트로 서식 지정합니다. 자세한 내용은 [텍스트 내 코드](#code-in-text) 섹션을 참조하세요.

Braze 문서에서 문서나 이미지 파일과 같은 파일 이름을 지정할 때 모두 소문자를 사용하고 하이픈이 아닌 밑줄로 단어를 구분합니다. 자세한 내용은 GitHub의 [파일 및 폴더 만들기](https://github.com/braze-inc/braze-docs/wiki/Creating-Files-&-Folders)를 참조하세요.

#### 각주 {#footnotes}

각주는 추가 정보를 제공하는 주석으로 일반적으로 페이지 끝에 배치됩니다. 텍스트 서식 때문에 각주는 대부분의 활용 사례에 최적이 아닙니다. 다음은 각주와 다른 출처 표시 방법을 사용해야 하는 경우를 설명합니다:

* 모두 출처에 귀속되어야 하는 통계 목록이나 기타 밀집된 정보를 제시하는 경우 각주를 사용합니다.
* 하나 또는 두 개의 정보를 제시하는 경우 링크나 알림을 사용합니다.
* 표의 항목에 추가 정보를 제공해야 하는 경우 표 항목 옆에 별표(*) 기호를 사용하고 표 뒤에 정보를 제시합니다.

#### 지시 사항의 텍스트 서식 지정 {#formatting-text-in-instructions}

일관된 텍스트 서식을 사용하여 독자가 정보를 찾고 해석하는 데 도움을 줍니다. 이 섹션에서는 지시 사항에서 다양한 텍스트 요소를 설명하거나 참조할 때 사용할 서식에 대한 가이드라인을 제공합니다.

이 섹션에서는 다음 요소를 다룹니다:

* [버튼](#buttons)
* [체크박스](#checkboxes)
* [명령줄 명령과 옵션](#command-line-commands-and-options)
* [대화 상자](#dialog-boxes-(modals))
* [오류 메시지](#error-messages)
* [필터와 연산자 이름](#filter-and-operator-names)
* [폴더와 파일 이름](#folder-and-filenames)
* [키 이름과 조합](#key-names-and-combinations)
* [메트릭](#metrics)
* [페이지](#pages)
* [권한 이름](#permission-names)
* [탭](#tabs-1)
* [텍스트 입력](#text-input)

##### 버튼 {#buttons}

버튼을 참조할 때 버튼 레이블에 굵은 텍스트를 사용합니다. 대부분의 경우 UI의 대문자 표기를 맞춥니다. 레이블이 모두 대문자인 버튼(OK 버튼 제외)의 경우 문장 대소문자를 사용합니다.

버튼을 참조할 때 버튼의 레이블만 사용합니다. "[레이블] 버튼"이라고 참조하지 않습니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><strong>Add Languages</strong>를 선택합니다.</td><td style="width: 50%;"><strong>Add Languages</strong> 버튼을 선택합니다. <br><br> "Add Languages"를 선택합니다.</td></tr>
</tbody>
</table>
{:/}

레이블이 콜론이나 줄임표로 끝나는 경우 끝 구두점을 생략합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><strong>Save as</strong>를 선택합니다</td><td style="width: 50%;"><strong>Save as…</strong>를 선택합니다</td></tr>
</tbody>
</table>
{:/}

버튼이 아이콘인 경우 툴팁에 표시된 버튼 이름을 포함합니다. 아이콘이 있는 버튼에 툴팁이 포함되지 않은 경우 툴팁 추가 요청을 제출합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">➕ <strong>Add</strong>를 선택합니다.</td><td style="width: 50%;">➕ 아이콘을 선택합니다.</td></tr>
</tbody>
</table>
{:/}

##### 체크박스 {#checkboxes}

체크박스를 참조할 때 체크박스 레이블에 굵은 텍스트를 사용합니다. 명확성이 필요하지 않는 한 "체크박스"라는 단어를 포함하지 않습니다. "check/uncheck" 대신 "select/clear"를 선호합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><strong>Send campaign to users in their local time zone</strong>을 선택합니다.</td><td style="width: 50%;"><strong>Send campaign to users in their local time zone</strong>을 체크합니다.</td></tr>
<tr><td style="width: 50%;"><strong>Exit</strong> 체크박스를 해제합니다.</td><td style="width: 50%;"><strong>Exit</strong> 체크박스를 언체크합니다.</td></tr>
</tbody>
</table>
{:/}

##### 명령줄 명령과 옵션 {#command-line-commands-and-options}

명령줄 명령이나 옵션을 참조할 때 코드 서식을 사용합니다. 표시되는 방식이나 입력해야 하는 방식에 맞게 대문자 표기를 맞춥니다.

##### 대화 상자(모달) {#dialog-boxes-(modals)}

명확성이 필요하지 않는 한 대화 상자를 이름으로 참조하지 않습니다. 대신 독자가 해야 할 일을 설명합니다. 대화 상자를 참조하는 경우 대화 상자 이름에 굵은 텍스트를 사용하고 UI의 대문자 표기를 맞춥니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><strong>Upload</strong>를 선택한 다음 업로드할 파일을 선택합니다.</td><td style="width: 50%;"><strong>Upload</strong>를 선택하고 <strong>File Upload</strong> 대화 상자를 사용하여 업로드할 파일을 선택합니다.</td></tr>
</tbody>
</table>
{:/}

##### 오류 메시지 {#error-messages}

독자가 접할 수 있는 오류 메시지를 참조할 때 오류 메시지를 따옴표로 감쌉니다. 더 긴 오류 메시지의 경우 블록 인용을 사용합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">"Push Bounced: MismatchSenderId"</td><td style="width: 50%;"><em>Push Bounced: MismatchSenderID</em><br><br><code>Push Bounced: MismatchSenderID</code></td></tr>
</tbody>
</table>
{:/}

##### 필터와 연산자 이름 {#filter-and-operator-names}

세그먼트나 대시보드의 다른 영역에 대한 필터와 연산자 이름을 참조할 때 코드 텍스트를 사용합니다. `OR`과 `AND` 연산자와 같이 모두 대문자인 요소를 포함하여 UI의 대소문자를 맞춥니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>First Used App</code> 필터를 선택하고…</td><td style="width: 50%;"><strong>First Used App</strong> 필터를 선택하고…</td></tr>
<tr><td style="width: 50%;"><code>OR</code> 연산자로 필터를 결합합니다.</td><td style="width: 50%;">"OR" 연산자로 필터를 결합합니다.</td></tr>
</tbody>
</table>
{:/}

##### 폴더와 파일 이름 {#folder-and-filenames}

폴더 이름과 파일 이름을 참조할 때 코드 텍스트를 사용합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>braze.xml</code> 파일을 엽니다.</td><td style="width: 50%;"><strong>braze.xml</strong> 파일을 엽니다.</td></tr>
</tbody>
</table>
{:/}

##### 키 이름과 조합 {#key-names-and-combinations}

키 이름이나 키 조합을 참조할 때 [HTML `<kbd>` 태그](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd)를 사용합니다. 이는 키보드, 음성 입력 또는 기타 텍스트 입력 장치에서의 텍스트 사용자 입력을 나타냅니다. 커스텀 HTML을 지원하지 않는 편집기에서 작업하는 경우 [코드 텍스트](#code-in-text)를 대신 사용합니다.

Command, Control, Option, Shift와 같은 키 이름을 풀어 씁니다. 해당 키에 기호를 사용하지 않습니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><strong>Option</strong>을 누릅니다.</td><td style="width: 50%;">⌥을 누릅니다.</td></tr>
</tbody>
</table>
{:/}

키 조합의 경우 키 사이에 더하기(+) 기호를 사용하되 특수 서식에서 더하기를 생략합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><strong>Option + F12</strong>를 누릅니다.</td><td style="width: 50%;">⌥ + F12를 누릅니다.</td></tr>
</tbody>
</table>
{:/}

예를 들어, Braze 문서에서 키보드 태그는 다음과 같이 표시됩니다:
명령을 중지하려면 **Control + C**를 누릅니다.

##### 메트릭 {#metrics}

표나 용어집 항목에서 메트릭을 참조할 때 특수 서식 없이 첫 글자를 대문자로 표기합니다. 문장에서 메트릭을 참조할 때 첫 글자를 대문자로 표기하고 이탤릭체를 사용합니다(예: *Machine Opens*).

##### 페이지

일반적으로 웹 페이지나 Braze 대시보드의 특정 페이지를 참조할 때 "페이지"라는 용어를 사용합니다. 페이지 이름을 참조할 때 "[레이블] 페이지" 형식을 사용하고 페이지 이름을 굵게 표시합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Segments 페이지로 이동합니다.</td><td style="width: 50%;">"Segments" 페이지로 이동합니다.</td></tr>
</tbody>
</table>
{:/}

##### 권한 이름 {#permission-names}

대시보드 내 사용자 권한 이름을 참조할 때 권한 이름을 따옴표로 감쌉니다.

{% alert note %}

현재 대시보드의 서식에 맞추기 위해 타이틀 케이스를 사용하고 있습니다. UI 내 권한 이름을 표준에 맞게 문장 대소문자로 업데이트할 계획이 있습니다.

{% endalert %}

##### 탭 {#tabs-1}

탭을 참조할 때 "[레이블] 탭" 형식을 사용하고 탭 이름을 굵게 표시합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><strong>설정 관리</strong> 페이지로 이동하여 <strong>Tags</strong> 탭을 선택합니다.</td><td style="width: 50%;">"설정 관리" 페이지로 이동하여 "Tags" 탭을 선택합니다.</td></tr>
</tbody>
</table>
{:/}

##### 텍스트 입력 {#text-input}

독자에게 특정 텍스트 문자열을 입력하도록 지시할 때 텍스트를 따옴표로 감쌉니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><strong>Name</strong> 필드에 "Lapsing Users"를 입력합니다</td><td style="width: 50%;"><strong>Name</strong> 필드에 <code>Lapsing Users</code>를 입력합니다.</td></tr>
</tbody>
</table>
{:/}

#### 자주 묻는 질문(FAQ) {#frequently-asked-questions-faqs}

사람들이 가장 알고 싶어하거나 알아야 하는 정보부터 시작하여 FAQ를 정렬한 다음, 여러 이슈 카테고리가 있는 경우 이슈 카테고리별로 FAQ를 구성합니다.

각 FAQ에 대해 먼저 질문에 직접 답한 다음 세부 사항을 설명합니다. 일반적인 검색 쿼리와 사용자 어휘에 맞는 실제 질문을 사용하여 FAQ의 검색 가능성을 높입니다. 관련 문서, 지원팀 연락 방법, 교육 자료(사용 방법 가이드, 튜토리얼 등)와 같이 사용자에게 도움이 될 수 있는 리소스 링크를 포함합니다.

#### 지리 {#geography}

##### 도시

카피에서 처음 언급할 때 모든 도시 이름을 풀어 씁니다. 이후에는 NYC나 LA와 같이 잘 알려진 도시 이름을 약어로 사용해도 됩니다.

**첫 번째 언급:** San Francisco
**두 번째 언급:** SF

London이나 Tokyo와 같이 잘 알려진 도시의 경우 주, 도, 국가 뒤에 쉼표 없이 소개해도 됩니다.

오디언스에게 익숙하지 않을 수 있는 도시나 마을의 경우 주, 도, 국가를 포함합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Biloxi, Mississippi</td></tr>
<tr><td style="width: 100%;">New Bedford, MA</td></tr>
<tr><td style="width: 100%;">Antwerp, Belgium</td></tr>
</tbody>
</table>
{:/}

##### 국가

모든 국가 이름을 대문자로 표기합니다. 국가 이름을 약어로 표기하려면 첫 번째 언급은 전체를 풀어 쓰고 이후에는 이니셜을 사용합니다.

**첫 번째 언급:** United States
**두 번째 언급:** US

약어로 된 국가 이름 사이에 마침표를 넣지 않습니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">UK</td><td style="width: 50%;">U.K.</td></tr>
<tr><td style="width: 50%;">Washington, DC</td><td style="width: 50%;">Washington, D.C.</td></tr>
</tbody>
</table>
{:/}

##### 지역

지역과 방향 수식어를 모두 대문자로 표기합니다.

**예시:** Northern California, Eastern Europe

특정 지역이나 장소를 설명하는 고유 명사를 대문자로 표기합니다.

**예시:** West Midlands, South America, South Chicago

##### 주와 도

모든 주와 도를 대문자로 표기합니다.

**예시:** New York, Quebec

#### 제목과 타이틀 {#headings-and-titles}

문서 제목과 타이틀에는 문장 대소문자를 사용합니다. 제목과 타이틀을 작성할 때 설명적으로 작성하고 문서 유형에 따른 콘텐츠의 주요 목적에 초점을 맞춥니다. "and" 대신 앰퍼샌드를 사용하지 않습니다.

문서 제목의 경우 가능하면 동명사(~ing로 끝나는 동사) 대신 명령형 동사를 선호합니다. 문서 제목을 간결하게 유지하고 콘텐츠에 적합한지 확인합니다. 예를 들어, SMS 메시지에 대한 참조 문서의 제목은 "About SMS"가 될 수 있습니다.

문서 제목의 경우 간결하고 제목 전체에서 일관성을 유지합니다. 예를 들어, 문서의 Heading 1 스타일이 각 단계를 정의하는 경우(예: **Step 1: 새 푸시 캠페인 만들기**) 일관성을 위해 문서 제목 전체에서 이 형식을 유지합니다.

Braze Docs의 스타일링 도움말은 [스타일링 예시]({{site.baseurl}}/contributing/styling_examples/?tab=markdown) 기여 페이지를 참조하세요.

##### 숫자 하위 작업

순서가 있는 단계를 설명하는 헤더의 경우 하위 작업 헤더에 숫자를 사용합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Step 2: SMS 캠페인 만들기 <br><br> Step 2.1: 메시지 작성 <br><br> Step 2.2: 전달 스케줄</td><td style="width: 50%;">Step 2: SMS 캠페인 만들기 <br><br> Step 2a: 메시지 작성 <br><br> Step 2b: 전달 스케줄</td></tr>
</tbody>
</table>
{:/}

#### 소개 {#introductions}

소개는 사용자가 다음을 확인하는 빠른 체크 역할을 합니다:

* 올바른 문서에 있는가? 이것이 나에게 관련이 있는가?
* 이 문서를 읽는 데 시간을 투자하면 무엇을 배울 수 있는가?
* SMS, 이메일, IAM 등에 대한 명확한 통합 또는 설정 여정을 따르고 있다고 느끼는가(사용자가 다음에 어떤 문서로 가야 하는지 명시하지 않더라도)?

다음은 소개에 대한 일반 가이드라인입니다. 더 특수한 활용 사례에 대해서는 섹션별 가이드라인을 참조하세요.

* 소개는 1~5문장이 될 수 있습니다
* 소개는 문서 내용의 개요를 제공하거나 주제에 대한 도입부여야 합니다
* 블록 인용을 사용합니다
* 문서의 H1 헤더 아래에 소개를 배치합니다

##### 파트너

파트너의 개요와 간략한 회사 설명을 포함합니다. 또한 파트너 사이트 링크를 포함합니다.

##### API

소개에는 "이 엔드포인트를 사용하여..." 문장만 포함합니다. API 엔드포인트를 가능한 한 쉽게 탐색할 수 있도록 유지하려고 합니다. API 엔드포인트 구조와 서식에 대한 자세한 내용은 [API 엔드포인트 문서 가이드라인]({{site.baseurl}}/contributing/style_guide/api_endpoint_guidelines/)을 참조하세요.

##### 사용자 가이드와 개발자 가이드

소개 단락은 두 가지 방법 중 하나로 작성해야 합니다:

1. 주제에 대한 도입 단락이나 도입부
2. 문서에 포함된 내용에 대한 설명. 이는 종종 "이 참조 문서는...."과 같은 형태입니다.

사용자 가이드와 개발자 가이드의 단계에서 사용자는 고객 여정 전반에 걸쳐 내비게이션의 단서에 크게 의존하지만, 때때로 중복되더라도 문서의 가치를 처음에 명시적으로 말하는 것이 도움이 됩니다.

예를 들어, 사용자가 개발자 가이드를 통해 Unity를 통합하는 경우. "Integration"이라는 제목의 이 페이지는 소개 문장을 포함하지 않으면 충분하지 않습니다.

#### 목록 {#lists}

목록은 관련 정보를 서식 지정하는 데 가장 적합합니다. 하나의 항목만 표시하기 위해 목록을 사용하지 않습니다. 단일 항목을 주변 텍스트에서 분리하려면 다른 서식을 사용합니다.

목록에는 세 가지 유형이 있습니다: 글머리 기호, 문자, 번호. 콜론이나 마침표로 끝날 수 있는 소개 완전 문장을 포함합니다.

* 글머리 기호 목록은 특정 순서가 필요하지 않은 정보를 구성합니다.
* 문자 목록은 상호 배타적인 옵션을 정의하는 데 사용됩니다.
* 번호 목록은 순서가 있는 단계의 시퀀스를 나타냅니다.

가능하면 모든 목록 항목에 동일한 구문을 사용합니다.

목록 항목 대문자 표기의 경우 각 목록 항목을 대문자로 시작합니다. 목록 항목 끝 구두점의 경우 다음 시나리오에서는 끝 구두점을 사용하지 않습니다:

* 목록 항목이 단일 단어이거나 불완전한 문장인 경우
* 목록 항목에 동사가 포함되지 않은 경우
* 목록 항목이 코드 글꼴인 경우
* 목록 항목이 링크이거나 문서 제목인 경우

#### 미디어 서식 {#media-formatting}

이 섹션에는 콘텐츠에서 이미지와 GIF를 서식 지정하기 위한 일반 가이드라인이 포함되어 있습니다. 예시 스크린샷을 포함한 자세한 내용은 [이미지 카피 스타일 가이드]({{site.baseurl}}/contributing/style_guide/image_style_guide/)를 참조하세요.

| **권장** | {::nomarkdown}<ul><li>언급하는 기능이나 구성 요소에 맞게 꼭 맞게 자릅니다.</li><li>고품질 스크린샷을 찍습니다. 가급적 레티나 모니터(MacBook 디스플레이)에서 찍습니다.</li><li>상호작용이나 워크플로의 GIF를 만듭니다.</li><li>사용자가 GIF를 일시 정지하거나 스크러빙하여 세부 사항을 볼 수 없다는 점을 염두에 둡니다.</li><li>이미지를 최적화 도구(ImageOptim, TinyPNG, Ezgif)를 통해 실행하여 파일 크기를 줄입니다.</li><li>접근성을 위해 요소 간 높은 대비를 목표로 합니다.</li><li>고정 픽셀 값이 아닌 높이 백분율로 이미지 크기를 조정합니다.</li></ul>{:/} |
| **비권장** | {::nomarkdown}<ul><li>대시보드의 헤더나 사이드바를 포함하지 않습니다. 간단한 문장으로 설명할 수 있습니다.</li><li>전체 대시보드를 포함하지 않습니다.</li><li>개인 식별 정보를 포함하지 않습니다(흐리게 처리하거나 데모 사용자의 정보가 아닌 한).</li><li>브라우저 프레임(URL 필드, 북마크, 탭 등)을 포함하지 않습니다.</li><li>기술 파트너의 대시보드를 포함하지 않습니다.</li><li>이미지에 테두리나 그림자를 추가하지 않습니다.</li></ul>{:/} |

#### 숫자 {#numbers}

숫자로 문장을 시작하지 않습니다. 예외는 연도를 참조하는 경우입니다(예: "2019년은 대단한 해였습니다").

9까지의 숫자는 풀어 씁니다. 측정 단위나 10 이상의 숫자에는 숫자를 사용합니다. 세 자리 이상의 숫자에는 쉼표를 사용합니다. 더 큰 숫자는 풀어 씁니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">1,000</td><td style="width: 50%;">1000</td></tr>
<tr><td style="width: 50%;">200,000</td><td style="width: 50%;">200000</td></tr>
<tr><td style="width: 50%;">1,000,000</td><td style="width: 50%;">1000000</td></tr>
<tr><td style="width: 50%;">9 billion</td><td style="width: 50%;">9000000000</td></tr>
<tr><td style="width: 50%;">5 MB</td><td style="width: 50%;">five MB</td></tr>
</tbody>
</table>
{:/}

##### 통화

통화 기호를 금액 앞에 사용하거나 풀어 써서(pesos, euros, pounds 등) 어떤 통화를 참조하는지 항상 표시합니다.

센트 수가 0보다 큰 금액에는 소수점을 사용합니다. 세 자리 이상의 금액에는 쉼표를 사용합니다. 금액에 ".00"을 포함하지 않습니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">US $20</td><td style="width: 50%;">$20</td></tr>
</tbody>
</table>
{:/}

##### 전화번호

전화번호를 참조할 때 숫자 사이에 하이픈을 넣습니다. 지역 번호를 괄호 안에 넣지 않습니다.

국가 코드가 포함된 전화번호를 서식 지정할 때 국가 코드 앞에 더하기 기호(+)를 사용하고 지역 번호를 괄호 안에 넣습니다.

국가 코드가 포함된 번호는 다음과 같이 제공합니다: +1 (504) 327-7269

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">123-456-7890</td><td style="width: 50%;">(123)-456-7890</td></tr>
<tr><td style="width: 50%;">+1 (123) 456-7890</td><td style="width: 50%;">1 234-567-9012</td></tr>
</tbody>
</table>
{:/}

##### 분수

분수를 풀어 쓰고 분자와 분모 사이에 하이픈을 사용합니다. 슬래시로 구분된 숫자를 사용하지 않습니다.

분수를 소수로 표현해야 하는 경우 1보다 작은 분수에는 소수점 앞에 0을 추가합니다.

분수를 사용하여 평가 시스템을 표현할 때 숫자를 사용하여 순위를 풀어 씁니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">0.5</td><td style="width: 50%;">1/2</td></tr>
<tr><td style="width: 50%;">one-third</td><td style="width: 50%;">one third</td></tr>
<tr><td style="width: 50%;">9 out of 10</td><td style="width: 50%;">nine out of ten</td></tr>
</tbody>
</table>
{:/}

##### 백분율

숫자와 퍼센트 기호(%) 사이에 공백 없이 사용합니다. 그러나 퍼센트가 문장을 시작하는 경우 전체 백분율(숫자와 퍼센트)을 풀어 씁니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">10%</td><td style="width: 50%;">10 %</td></tr>
<tr><td style="width: 50%;">회사 사용자의 20%가...</td><td style="width: 50%;">20%의 회사 사용자가...</td></tr>
</tbody>
</table>
{:/}

##### 범위

숫자 범위를 나타내기 위해 하이픈을 사용합니다. 범위에서 숫자를 구분하기 위해 엔 대시를 사용하지 않습니다.

단위가 있는 숫자 범위의 경우 숫자 뒤에 측정 단위를 반복합니다. 명사를 반복하는 것은 포함되지 않습니다. 혼동을 피하기 위해 범위의 숫자 사이에 "to"를 사용합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">5 to 100</td><td style="width: 50%;">5–100</td></tr>
<tr><td style="width: 50%;">-10°C to 50°C</td><td style="width: 50%;">-10°C-50°C</td></tr>
</tbody>
</table>
{:/}

#### 입력 안내 텍스트 {#placeholder-text}

독자가 관련 값을 제공해야 하는 위치를 나타내기 위해 입력 안내 텍스트를 사용합니다. 입력 안내 텍스트는 표현되는 콘텐츠를 나타내야 합니다. 예를 들어 *YOUR_API_KEY*는 독자의 API 키를 나타냅니다.

##### 입력 안내 작성

입력 안내 텍스트를 만들 때 다음 가이드라인을 참조합니다:

| 가이드라인 | 예시 |
| :---- | :---- |
| 대문자를 사용하고 단어를 밑줄(_)로 구분합니다. | `PLACEHOLDER_VARIABLE` |
| 인라인 입력 안내 텍스트에는 이탤릭체를 사용합니다. | *`PLACEHOLDER_VARIABLE`* |
| API 코드 블록 입력 안내 텍스트(이탤릭체를 사용할 수 없는 경우)에는 중괄호({})로 입력 안내를 감쌉니다. | `<string name="com_appboy_api_key">{YOUR_APP_IDENTIFIER_API_KEY}</string>` |
| Liquid 코드 블록 입력 안내 텍스트(이탤릭체를 사용할 수 없는 경우)에는 대문자를 사용합니다. | `{% raw %}{%- connected_content YOUR-API-URL :save items -%}{% endraw %}` |
| 간결함을 위해 명확성을 희생하지 않습니다. 입력 안내를 표현하는 데 필요한 만큼의 단어를 사용합니다. | **권장:** `CAMPAIGN_NAME` <br> **비권장**: _`NAME`_|

##### 입력 안내 사용

입력 안내를 소개하거나 설명할 때 다음 가이드라인을 참조합니다:

| 가이드라인 | 예시 |
| :---- | :---- |
| 입력 안내 바로 뒤에 입력 안내를 설명합니다. | `<YOUR_APP_IDENTIFIER_API_KEY>`를 **설정** 페이지에서 찾을 수 있는 [App Identifier API Key]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key)로 대체합니다. |
| 두 개 이상의 입력 안내를 한 번에 설명하려면 글머리 기호 목록을 사용합니다. 코드에 나타나는 순서대로 각 입력 안내를 나열합니다. | 다음을 대체합니다: {::nomarkdown}<ul><li><code>PLACEHOLDER_VARIABLE</code>: 입력 안내가 나타내는 내용에 대한 설명</li><li><code>PLACEHOLDER_VARIABLE</code>: 입력 안내가 나타내는 내용에 대한 설명</li></ul>{:/} |
| 텍스트나 코드에 표시된 것과 동일한 서식으로 입력 안내를 참조합니다. | `target <YOUR_APP_TARGET> do pod 'Appboy-iOS-SDK' end` <br><br> `<YOUR_APP_TARGET>`을 대상 앱의 이름으로 대체합니다. |

#### 제품 {#products}

Braze와 그 기능을 참조할 때 전체 제품 및 기능 이름을 사용하고 UI에 따라 대문자로 표기합니다. 템플릿이나 일반 기능은 대문자로 표기하지 않습니다. 제품 이름과 철자 목록은 [용어집](#glossary)을 참조하세요.

다음 경우를 제외하고 제품이나 기능 이름을 약어로 사용하지 않습니다:

* UI에 맞추기 위해
* 제한된 공간 제약을 충족하기 위해

제품이나 기능 이름을 동사로 사용하지 않습니다.

Braze 뒤에 아포스트로피를 사용하지 않습니다(예: "Braze's"). 어색하게 들립니다. 대신 전치사("to, of, from")를 사용하여 소유격을 형성하고 회사 이름을 뒤에 붙입니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Braze의 최신 제품 업데이트</td><td style="width: 50%;">Braze's 최신 제품 업데이트</td></tr>
<tr><td style="width: 50%;">그것은 Braze의 핵심 기능 중 하나입니다.</td><td style="width: 50%;">그것은 Braze's 핵심 기능 중 하나입니다</td></tr>
</tbody>
</table>
{:/}

"Braze"를 "we/our/ours"로 지칭합니다. "it/its/they/their"로 지칭하지 않습니다.

#### 표 {#tables}

표를 사용하면 정보를 도움이 되고 체계적으로 표시할 수 있습니다. 명확하고 설명적인 헤더와 해당 열과 행에 관련 데이터가 있는지 확인합니다.

항상 표의 목적을 설명하는 소개 문장을 사용합니다. 번호가 매겨진 절차 중간에 표를 사용하지 않습니다. 대신 목록 사용을 고려합니다.

#### 측정 단위 {#units-of-measurement}

HTML과 Markdown에서 측정 단위를 지정할 때 숫자와 단위 사이에 줄바꿈 없는 공백(&nbsp)을 사용합니다. 여기에는 거리, 픽셀, 포인트, 무게, 온도(도와 측정 단위 사이)를 포함한 대부분의 측정 단위가 포함됩니다.

통화, 퍼센트, 각도의 경우 숫자와 단위 사이에 공백을 사용하지 않습니다.

단위가 있는 숫자 범위의 경우 각 숫자에 대해 단위를 반복합니다. 마찬가지로 비율의 경우 슬래시(/) 대신 "per"를 사용합니다.

### 링크 {#linking}

#### 상호 참조 링크 {#cross-reference-links}

상호 참조를 사용하여 사용자를 추가 리소스로 안내합니다. Braze 문서에서는 다른 Braze 문서에 링크하기 위해 사이트 루트 상대 URL을 사용합니다("www.braze.com/docs"를 "{{site.baseurl}}"로 대체).

주어진 페이지 내에서 동일한 문서에 여러 링크를 추가하지 않습니다. 이는 링크 피로를 유발할 수 있습니다. 다른 페이지의 특정 섹션에 링크하거나 링크하는 페이지가 긴 경우 중복 링크는 적당히 사용해도 됩니다.

#### 동영상 삽입 {#embedding-videos}

이미지와 마찬가지로 동영상을 사용하여 학습 자료에 다양성을 만듭니다. 대부분의 사람들은 매체의 조합으로 가장 잘 배우므로 동영상에 포함하는 모든 콘텐츠가 문서나 레슨에서도 다루어지도록 합니다.

Braze 문서에 동영상을 삽입하려면 [삽입 동영상 테스트]({{site.baseurl}}/home/styling_test_page/#embedded-video-test)를 참조하세요.

#### 링크 대상으로서의 제목 {#headings-as-link-targets}

Braze 문서에서는 제목에 대해 앵커가 자동으로 생성됩니다. 그러나 다음과 같은 경우 제목에 커스텀 앵커를 추가할 수 있습니다:

* 자동 생성된 앵커가 매우 긴 경우.
* 제목이 자주 링크될 수 있는 경우. 커스텀 앵커를 추가하면 나중에 제목 텍스트가 변경되더라도 링크가 깨질 가능성이 줄어듭니다.

Braze 문서에서 제목에 앵커를 추가하려면 [커스텀 앵커]({{site.baseurl}}/home/styling_test_page/#custom-header-anchor)를 참조하세요.

#### 링크 텍스트 {#link-text}

효과적인 링크 텍스트는 콘텐츠의 검색 가능성, 발견 가능성, 접근성을 향상시키는 데 도움이 됩니다.

##### 링크 구조화 {#structuring-links}

링크를 작성할 때 다음 형식 중 하나를 사용합니다:

* 링크 텍스트를 링크 대상의 제목이나 헤딩과 일치시킵니다.
* 링크 대상의 설명을 링크 텍스트로 사용합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장: <em>링크 텍스트를 링크 대상의 제목이나 헤딩과 일치시킵니다.</em></th><th style="width: 50%;">권장: <em>링크 대상의 설명을 링크 텍스트로 사용합니다.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Braze <a href="{{site.baseurl}}/user_guide/getting_started/web_sdk/">Web SDK</a>로 시작합니다.</td><td style="width: 50%;">특정 클러스터나 엔드포인트를 확인하려면 <a href="{{site.baseurl}}/braze_support/">지원팀에 문의</a>하세요.</td></tr>
<tr><td style="width: 50%;">자세한 내용은 <a href="{{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/">Liquid 메시지 중단</a>을 참조하세요.</td><td style="width: 50%;">의문이 있을 때는 항상 <a href="{{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password">비밀번호를 재설정</a>할 수 있습니다.</td></tr>
</tbody>
</table>
{:/}

좋은 링크 텍스트를 만들기 위해 문장을 재구성해야 할 수도 있습니다.

같은 페이지의 섹션에 링크하는 경우 이 동작을 나타내는 표준 구문을 사용합니다. 예를 들어:

* 이 페이지에서 [제목]을 참조하세요.
* 이 문서에서 [제목]을 참조하세요.
* 자세한 내용은 [제목] 섹션을 참조하세요.

##### 링크 작성 {#writing-links}

링크 텍스트를 작성할 때 다음 가이드라인을 적용합니다:

* 관련 키워드에 링크를 넣습니다.
* 독자를 다른 문서로 안내하는 완전한 문장을 작성하는 경우 "자세한 내용은 ~을 참조하세요" 또는 "[주제]에 대한 자세한 내용은 ~을 참조하세요"라는 구문을 사용합니다.
* 도움말 텍스트가 둘 이상의 개념을 다루고 각각 자체 도움말 문서에 링크될 수 있는 경우에만 "자세히 알아보기…" 문장을 추가합니다. 이 경우 가장 적절한 링크를 선택하고 "자세히 알아보기…"로 맥락화합니다.
* 비격식적인 톤을 유지하기 위해 링크 텍스트를 소개할 때 "please"를 사용하지 않습니다. 예를 들어, "Please refer to", "Please see", "Please contact"와 같은 구문을 피합니다.
* 주변 텍스트 없이도 의미가 통하는 고유하고 설명적인 링크 텍스트를 작성합니다. [Nielsen Norman Group](https://www.nngroup.com/articles/link-promise/#links-should-stand-alone)(NN/g)의 연구에 따르면 독자는 페이지에서 눈에 띄는 정보를 스캔하므로 링크가 독립적으로 의미가 통하도록 합니다.
* 링크 텍스트에 다음 단어나 구문을 사용하지 않습니다. 접근성과 스캔 가능성에 좋지 않습니다.
 * Learn more (단독으로)
 * Click here
 * here
 * this document
 * this article

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장: <em>주변 텍스트 없이도 링크 텍스트가 의미가 통하도록 합니다</em></th><th style="width: 50%;">비권장: <em>모호하거나 설명적이지 않은 링크 텍스트를 사용합니다</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">고객 데이터 가져오기에 대한 자세한 내용은 <a href="{{site.baseurl}}">사용자 가져오기</a>를 참조하세요.</td><td style="width: 50%;">자세한 내용은 <a href="{{site.baseurl}}">여기를 클릭</a>하세요.</td></tr>
<tr><td style="width: 50%;">이 기능은 <a href="{{site.baseurl}}">Track users</a> 엔드포인트에 연결됩니다.</td><td style="width: 50%;"><a href="{{site.baseurl}}">이 문서</a>를 참조하세요.</td></tr>
<tr><td style="width: 50%;"><a href="{{site.baseurl}}">Android SDK 16.0.0의 새로운 기능</a>에 대해 자세히 알아보세요.</td><td style="width: 50%;"><a href="{{site.baseurl}}">여기</a>의 지시 사항을 따르세요.</td></tr>
<tr><td style="width: 50%;"><a href="https://www.braze.com/product">Braze 플랫폼</a>에 대해 자세히 알아보세요.</td><td style="width: 50%;">단계는 <a href="{{site.baseurl}}">이 문서</a>를 참조하세요. <a href="{{site.baseurl}}">자세히 알아보기</a>.</td></tr>
<tr><td style="width: 50%;">Storefront API 키는 Hydrogen 스토어프론트별로 고유하지만 권한 범위는 모든 Hydrogen 스토어프론트에서 공유됩니다. <a href="{{site.baseurl}}">Storefront API 토큰</a>에 대해 자세히 알아보세요.</td><td style="width: 50%;"><a href="{{site.baseurl}}">Storefront API 토큰</a>은 <a href="{{site.baseurl}}">Hydrogen 스토어프론트</a>별로 고유하지만 <a href="{{site.baseurl}}">권한 범위</a>는 모든 Hydrogen 스토어프론트에서 공유됩니다.</td></tr>
</tbody>
</table>
{:/}

#### 엔드포인트 링크 {#links-for-endpoints}

엔드포인트 문서를 참조할 때 맥락 없이도 의미가 통하는 [의미 있는 링크 텍스트](https://docs.google.com/document/d/e/2PACX-1vTluyDFO3ZEV7V6VvhXE4As_hSFwmnFFdU9g6_TrAYTgH1QmbRoEDDdn5GzKAB9vdBbIdyiFdoaJcNk/pub#h.79ujl0qtumog)를 사용해야 합니다. 엔드포인트의 경로를 링크로 사용하는 경우 경로가 엔드포인트의 기능을 명확하게 전달하지 못할 수 있으므로 주변 텍스트에 세부 정보를 제공해야 합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Braze <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">Delete user 엔드포인트</a>를 사용하여 고객 프로필을 삭제합니다.</td><td style="width: 50%;">Braze <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">Delete user</a> 엔드포인트를 사용하여 고객 프로필을 삭제합니다.</td></tr>
<tr><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/"><code>/users/export/id</code> 엔드포인트</a></td><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/"><code>/users/export/id</code></a> 엔드포인트</td></tr>
</tbody>
</table>
{:/}

#### 파일 다운로드 링크 {#links-for-file-download}

링크가 파일을 다운로드하는 경우 링크 텍스트에 이를 명확히 하고 파일 유형을 언급합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장: <em>링크 텍스트가 선택 시 파일이 다운로드됨을 전달하도록 합니다</em></th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">팁을 보려면 <a href="{{site.baseurl}}">Regex Cheat Sheet PDF</a>를 다운로드하세요.</td><td style="width: 50%;"><a href="{{site.baseurl}}">RegEx Cheat Sheet</a>를 확인하세요.</td></tr>
<tr><td style="width: 50%;">자세한 내용은 <a href="{{site.baseurl}}">Success and Support Services Handbook PDF</a>를 다운로드하세요.</td><td style="width: 50%;"><a href="{{site.baseurl}}">Success and Support Services Handbook</a></td></tr>
</tbody>
</table>
{:/}

#### 다른 사이트 링크 {#links-to-other-sites}

일반적으로 간단한 설명으로 정보를 다룰 수 있는 경우 다른 사이트에 링크하지 않습니다. 다른 사이트의 콘텐츠가 언제 변경되는지 추적할 수 없습니다.

외부 사이트에 링크하는 경우 링크하는 사이트가 고품질이고, 신뢰할 수 있으며, 존경받는 사이트인지 확인합니다. 가능하면 페이지에서 가장 관련 있는 제목에 링크합니다.

링크가 다른 도메인으로 이동함을 나타내기 위해 외부 링크 아이콘을 사용합니다. Braze 문서에서는 외부 링크에 자동으로 적용됩니다.

#### 이미지 URL {#urls-for-images}

Braze 문서에서는 이미지에 링크하기 위해 사이트 루트 상대 URL을 사용합니다. 자세한 내용은 [이미지 추가 및 편집](https://github.com/braze-inc/braze-docs/wiki/Editing-Content#adding-and-editing-images)을 참조하세요.

### 용어집 {#glossary}

⚠️ = 주의하여 사용, 관련 참고 사항 참조
⛔️ = 사용하지 않음

#### 숫자

**24/7**
명사 앞에서 수식어로 사용될 때만 하이픈을 사용합니다(24-7).

**2D / two-dimensional**

**3D / three-dimensional**

#### A

**A/B testing**

⚠️ **abort**
구체적으로 명명된 프로세스를 참조하는 경우가 아니면 사용을 피합니다. 대신 "stop", "exit", "cancel", "end"와 같은 단어를 사용합니다.

**action buttons**

**action-based delivery**
대문자로 표기된 UI 요소를 참조하는 경우를 제외하고 소문자로 표기합니다.

⛔️ **ad hoc**
사용하지 않습니다. "one-time" 또는 유사한 표현을 사용합니다.

**AI**
첫 번째 언급 후 "artificial intelligence"보다 선호됩니다.

**AI item recommendation**

**Alloys / Braze Alloys**
항상 대문자로 표기합니다.

**alphanumeric**
하이픈을 사용하지 않습니다.

**always-on**

**am**
시간에 사용될 때 소문자로 표기합니다(예: "10 am"). [pm](#glossary)도 참조하세요.

**Amazon S3**

**Amazon Web Services (AWS)**
항상 대문자로 표기합니다. 첫 번째 언급 시 풀어 쓰고 이후에는 약어를 사용해도 됩니다.

**AMP for Email / Braze AMP for Email**

**Android**

**API / Application Programming Interface**
첫 번째 언급 시 풀어 쓰고 이후에는 약어를 사용해도 됩니다.

**API key**

**APNs / Apple Push Notification service**

**⛔️ app group**
사용하지 않습니다. 앱 그룹은 워크스페이스로 이름이 변경되었습니다.

**Apple iOS platform**

**AppleWatch**

**.avro**

#### B

**behavior, behaviors**

**Benchmarks**

**beta**

**BI Insights**

**bingeing**

**Binge-watch**

**Bonfire / Bonfire community / Braze Bonfire community**
첫 번째 언급 시 "Braze Bonfire community"를 사용하고 이후에는 "Bonfire" 또는 "Bonfire community"만 사용해도 됩니다.

**boolean**

⛔️ **blacklist**
사용하지 않습니다. 대신 "blocklist" 또는 "denylist"를 사용합니다. 이러한 단어의 동사 형태의 경우 문제가 되는 용어를 제거하도록 문장을 재구성하는 것을 고려합니다. 예를 들어:

>✅ **권장:** 기존 속성이 새 메시지에서 사용되지 않도록 차단하려면 **Manage Properties**를 선택합니다. <br>
>⛔️ **비권장:** 기존 속성을 blocklist하려면 **Manage Properties**를 선택합니다.

**Braze-to-Braze webhook**

**Business Intelligence (BI)**
첫 번째 언급 시 풀어 쓰고 이후에는 약어를 사용해도 됩니다.

#### C

**California Consumer Privacy Act (CCPA)**
첫 번째 언급 시 풀어 쓰고 이후에는 약어를 사용해도 됩니다. [CCPA compliance (noun) / CCPA-compliant (adjective)](#ccpa-compliance)도 참조하세요.

**can**
선택적 동작이나 결과를 참조할 때 "can"을 사용합니다. 예를 들어:

> ✅ **권장:** CSV 파일로 고객 프로필을 업로드하고 업데이트할 수도 있습니다.
> ✅ **권장:** 가져오기 프로세스는 몇 분이 걸릴 수 있습니다.

지시 사항에는 "can"을 사용하지 않습니다. 대신 명령형 동사를 선호합니다. 예시는 [2인칭과 1인칭](#second-person-and-first-person)을 참조하세요.

**Canvas**
항상 대문자로 표기합니다. 복수형은 "Canvases"입니다.

**Canvas Flow**
원래 Canvas 편집기와 Canvas Flow를 구분할 때 사용합니다. 그 외에는 "Canvas"를 사용합니다.

**campaign**
대문자로 표기된 UI 요소를 참조하는 경우를 제외하고 소문자로 표기합니다.

**capacity**
"limit"이라는 단어 대신 커스텀 데이터 제한을 참조할 때 사용합니다.

**catalog**
대문자로 표기된 UI 요소를 참조하는 경우를 제외하고 소문자로 표기합니다.

**CCPA compliance (noun) / CCPA-compliant (adjective)** {#ccpa-compliance}

**CEO, CFO, CMO, COO, CTO**

**churn**
고객 이탈 또는 손실을 참조할 때 사용합니다.

**churn prediction**
UI를 참조하는 경우를 제외하고 소문자로 표기합니다.

**checkbox**

**Check-in (noun) / check in (verb)**

**City x City**

**Cofounder**

**Content Cards / Braze Content Cards**

**Content Blocks**

**control group**

**conversion**

**conversion group analysis**
소문자로 표기합니다.

**Cordova**

**Currents / Braze Currents**
항상 대문자로 표기합니다.

**CRM / customer relationship management**
첫 번째 언급 시 풀어 쓰고 이후에는 약어를 사용해도 됩니다.

**cross-channel messaging / cross-channel personalization**

**C-suite**

**CSV / comma-separated values**

**custom attributes**
대문자로 표기된 UI 요소를 참조하는 경우를 제외하고 소문자로 표기합니다.

**custom events**
대문자로 표기된 UI 요소를 참조하는 경우를 제외하고 소문자로 표기합니다.

**customer attributes**

**customer behavior**

**customer data platform (CDP)**
소문자로 표기합니다.

**customer engagement**

**customer events**

**customer journey**

**customer permissions**

**customer retention**

#### D

**Dark Mode theme / Dark Mode Preview / dark mode concept**

**dashboard / Braze dashboard**
Braze를 플랫폼으로 참조할 때 사용합니다. 소문자(Dashboard가 아닌 dashboard)를 사용합니다.

**data-driven (adjective)**

**data privacy**

**data sheet**

**data streaming**

**DAU / Daily Active Users**

**Decision Splits**

**deep linking**

**Delay Messages**

**Downtime**

**drag and drop (verb) / drag-and-drop (adjective)** {#drag-and-drop}
파일을 업로드 영역으로 드래그하는 것을 참조할 때 사용합니다.

**Drag-And-Drop Editor**
UI의 기능을 참조할 때 타이틀 케이스를 사용합니다. 그 외에는 소문자(drag-and-drop editor)를 사용합니다. 고객이 편집기에서 요소를 [드래그 앤 드롭](#drag-and-drop)하는 방법을 참조할 때 동사를 사용합니다.

**drill down (verb) / drilldown (noun or adjective)**
데이터와 그로부터 생성된 보고서에 대한 콘텐츠에서 사용합니다.

**DTC / direct to consumer**

**dynamic content**

#### E

**early access**

⛔️ **e.g.**
사용하지 않습니다. "for example," "such as," "like" 또는 유사한 구문을 사용합니다.

**eBook**

**eCommerce**
"ecommerce"나 "e-commerce"가 아닙니다.

**ecosystem**

**email**
"Email"이나 "e-mail"이 아닙니다.

**email deliverability**

**email reputation**

**EMEA (Europe, Middle East, and Asia)**

**emoji**
단수형과 복수형이 동일합니다.

**end user (noun) / end-user (adjective)**
"end users"보다 "your users"를 선호합니다.

⚠️ **ensure**
기능이 하는 일에 대해 이야기할 때 사용을 피합니다. 자세한 내용은 [보증 피하기](#avoid-guarantees)를 참조하세요.

**ESP / email service provider**

**event prediction**

**event properties / custom event properties**
대문자로 표기된 UI 요소를 참조하는 경우를 제외하고 소문자로 표기합니다.

**exception events**

**extract**
압축된 폴더에서 파일을 추출하는 것을 참조할 때 "unzip" 대신 "extract"를 사용합니다.

**external ID**
"External ID"가 아닙니다. 코드 스니펫을 참조할 때는 external_id를 사용합니다.

#### F

**Facebook**

**FCM / Firebase Cloud Messaging**

**Firebrand / Firebrands**

**Forge [YEAR]**

**frequency capping**

**Fullscreen**
형용사로 사용될 때(예: "Fullscreen in-app messages") 하이픈 없이 표기합니다.

#### G

**GDPR / General Data Protection Regulation**
첫 번째 언급 시 풀어 쓰고 이후에는 약어를 사용해도 됩니다.

**GDPR compliance (noun) / GDPR-compliant (adjective)**

**geofence**

**GIF**

**GitHub**
"Github"나 "github"가 아닙니다.

**Google / google-able**

#### H

**High-performance**

**High-Value Actions**

**HQ / headquarters**

**HTML Email Editor**

**HTTP**

#### I

⛔️ **i.e.**
사용하지 않습니다. "that is" 또는 유사한 구문을 사용합니다.

**in-app messages**

**in-browser message (IBM)**

**infographic**

**install attribution**

**integer**

**Intelligence Suite**
타이틀 케이스를 사용합니다.

**Intelligent Channel**
타이틀 케이스를 사용합니다.

**Intelligent Selection**
타이틀 케이스를 사용합니다.

**Intelligent Timing**
타이틀 케이스를 사용합니다.

⛔️ **Internet of things**
사용하지 않습니다.

**iOS**

**IP warming**

**iPad**

**iPhone**

**IT**

#### J

**JavaScript**

**JPEG / JPG**

**JSON / JavaScript Object Notation**

#### K

**Keynote (program) / keynote (noun)**

**kick off (verb) / kickoff (noun)**

⚠️ **kill**
구체적으로 명명된 프로세스를 참조하는 경우가 아니면 사용을 피합니다. 대신 "stop", "exit", "cancel", "end"와 같은 단어를 사용합니다.

**KPI / key performance indicator**

#### L

**landing page**

**lifecycle**

**Lift-rate**

**LinkedIn**

**Liquid**
항상 대문자로 표기합니다.

**Live Preview**

**long term (noun) / long-term (adjective)**

**LTV / Lifetime Value**

#### M

**marketing technology**
"martech"보다 선호됩니다.

**MAU / Monthly Active Users**

**maximum**
"max"가 아닙니다.

**media library**
대문자로 표기된 UI 요소를 참조하는 경우를 제외하고 소문자로 표기합니다.

**Microsoft**

**Microsoft Azure**

**ML / machine learning**

**mobile marketing**

**mobile marketing automation**

**mobile moment**

**mobile phone**

**multichannel campaign**
대문자로 표기된 UI 요소를 참조하는 경우를 제외하고 소문자로 표기합니다. 하이픈 없음.

**multi-language support**

**multivariate testing**

#### N

**N/A**
"NA"가 아닙니다. 표에서 특정 셀에 적용되지 않는 열이나 행 콘텐츠를 나타내기 위해 필요에 따라 "N/A"를 사용합니다. 인라인 텍스트에서는 명확성을 위해 "not available" 또는 "not applicable"을 풀어 쓰는 것을 선호합니다.

⚠️ **new**
제품 문서와 학습 자료에서 사용을 피합니다. 콘텐츠를 빠르게 구식으로 만들 수 있습니다. 자세한 내용은 [미래 기능](#describing-limitations)을 참조하세요.

**NRT / near real-time (adjective) / near real time (noun)**

**NYC / New York City**

#### O

**on demand**

**onboarding**

**once**
동작을 한 번 수행하는 것을 참조할 때 사용합니다. "after"나 "when" 대신 "once"를 사용하지 않습니다.

**open rate (OR)**

**opt-in prompt**

**orchestration**

**OS / Operating System**

**OTT / Over-the-top media services**

⛔️ **out-of-the-box**
사용하지 않습니다. 대신 "default"와 같은 대안을 사용합니다.

#### P

**partner, partners, partnership**

**persona (singular) / personas (plural)**

**personalization**

**personally identifiable information (PII)**

**Personalized Path**
타이틀 케이스를 사용합니다.

**Personalized Variant**
타이틀 케이스를 사용합니다.

**PhD / PhDs**

**pm**
시간에 사용될 때 소문자로 표기합니다(예: "10 pm"). [am](#glossary)도 참조하세요.

**preceding**

**prediction**
"Braze"가 앞에 오는 경우를 제외하고 소문자로 표기합니다. 예: "A Braze Prediction is…".

**predictive analytics**

**Predictive Churn**
타이틀 케이스를 사용합니다. Predictive Churn은 제품 이름이며, 고객은 [churn prediction](#glossary)을 만듭니다.

**Predictive Events**
타이틀 케이스를 사용합니다.

**Predictive Purchases**
타이틀 케이스를 사용합니다. Predictive Purchases는 제품 이름이며, 고객은 [purchase prediction](#glossary)을 만듭니다.

**Predictive Suite**
타이틀 케이스를 사용합니다.

**preference center**
대문자로 표기된 UI 요소를 참조하는 경우를 제외하고 소문자로 표기합니다.

**priming for location**

**priming for push**

**promotion code**
대문자로 표기된 UI 요소를 참조하는 경우를 제외하고 소문자로 표기합니다. "promo code"를 사용하지 않습니다.

**purchase prediction**
대문자로 표기된 UI 요소를 참조하는 경우를 제외하고 소문자로 표기합니다.

**purchase properties**
대문자로 표기된 UI 요소를 참조하는 경우를 제외하고 소문자로 표기합니다.

**push action buttons**

**Push Max**
타이틀 케이스를 사용합니다.

**push notification**

**Push Stories**
타이틀 케이스를 사용합니다.

#### Q

**Q&A**

⛔️ **QA (quality assurance)**
약어를 동사로 사용하지 않습니다. 대신 "perform quality assurance"로 재작성합니다.

**quiet hours**
문장 시작 시 "Quiet hours"를 사용하고 문장 중간에서는 "quiet hours"를 사용합니다. 브랜드 기능이 아니므로 타이틀 케이스 "Quiet Hours"를 사용하지 않습니다.

⚠️ **quick / quickly**
사용을 피합니다. 여러분에게 빠른 것이 다른 사람에게는 빠르지 않을 수 있습니다. 관련 가이드라인은 [거만한 언어](#condescending-language)를 참조하세요.

#### R

**rate limiting**

**real time (noun) / real-time (adjective)**

**re-engagement**

⚠️ **regular expression / regex**
약어 "regex"보다 풀어 쓴 버전을 선호합니다. "RegEx"를 사용하지 않습니다.

**relationship marketing**

**retargeting**

**retention**

**rich push**

**right-click**

**right-swipe**

**ROI / return on investment**

#### S

**Sage AI by Braze™**

⛔️ **sanity check**
사용하지 않습니다. 대신 "quick check" 또는 "preliminary check"와 같은 용어를 사용합니다. 또는 "모든 것이 제대로 작동하는지 확인해 봅시다"와 같은 구문으로 확인 지시 사항을 소개합니다.

**scheduled delivery**
대문자로 표기된 UI 요소를 참조하는 경우를 제외하고 소문자로 표기합니다.

**screencap**

**screengrab**

**SDK / Software Developer Kit**

**segment (audience)**

**Segment Extensions**
타이틀 케이스를 사용합니다.

**Segment Insights**
타이틀 케이스를 사용합니다.

**Segmentation**

**selection**
카탈로그 내의 기능으로서. 대문자로 표기된 UI 요소를 참조하는 경우를 제외하고 소문자로 표기합니다.

**SF / San Francisco**

**Silicon Valley**

**silo, silos, siloed**

**simple survey**

**slideshow**

**Smartphone**

**Smartwatch**

**SMS**

**software as a service (SaaS)**
첫 번째 언급 시 풀어 쓰고 이후에는 약어를 사용해도 됩니다.

**spam testing**

**SQL / structured query language**

**SQL Segment Extensions**
타이틀 케이스를 사용합니다.

**stickiness**

**streaming**

**string**
비기술적 오디언스의 경우 문자열을 "영숫자 문자"를 포함하는 텍스트로 정의합니다. 기술적 오디언스의 경우 이 용어를 정의하지 않아도 됩니다.

**subscription group**

**sunset, sunsetting**

#### T

**targeted response**

⚠️ **terminate**
구체적으로 명명된 프로세스를 참조하는 경우가 아니면 사용을 피합니다. 대신 "stop", "exit", "cancel", "end"와 같은 단어를 사용합니다.

**third-party**

**time zone**
"timezone"이 아닙니다.

**timestamp**

**touchscreen**

**triggered message**

**Twitter**

#### U

**UK / United Kingdom**

⛔️ **unzip**
사용하지 않습니다. 대신 "extract"를 사용합니다.

**URL**
개별 문자 U-R-L로 발음되므로 "an URL"이 아닌 "a URL"로 작성합니다. 모두 대문자를 사용합니다. 복수형은 URLs를 사용합니다.

**US / USA**
마침표 없음.

**use cases**

**user attributes / default user attributes**
Braze가 자동으로 캡처하는 사용자 데이터를 참조할 때 사용합니다.

**user profile**

**username**

⚠️ **utilize**
"use"를 의미할 때 "utilize"를 사용하지 않습니다. 원래 의도된 목적을 넘어서 사용되는 것을 참조할 때 "utilize"를 사용합니다.

#### V

**variant**

⛔️ **via**
사용하지 않습니다. 대신 "through" 또는 "by means of", "by way of"와 같은 구문을 사용합니다.

⛔️ **vice versa**
사용하지 않습니다. 대신 "conversely" 또는 "the other way around"와 같은 구문을 사용합니다.

**view-only**

⚠️ **vs.**
"versus"의 약어로 "vs."를 사용하지 않습니다. 대신 단어를 풀어 씁니다.

#### W

**web messaging**

**web push**

**webhook**

**webinar**

**whitelabel**

⛔️ **whitelist**
UI를 참조하는 경우가 아니면 사용하지 않습니다. 대신 "allowlist" 또는 "safelist"를 사용합니다. 이러한 단어의 동사 형태의 경우 문제가 되는 용어를 제거하도록 문장을 재구성하는 것을 고려합니다. 예시는 [blacklist](#glossary)를 참조하세요.

⚠️ **Wi-Fi**
"WiFi", "wi-fi", "wifi"를 사용하지 않습니다.

**will**
"will"이나 "would"를 사용하지 않습니다. [현재 시제](#present-tense)를 참조하세요.

**Winning Path**
타이틀 케이스를 사용합니다.

**Winning Variant**
타이틀 케이스를 사용합니다.

⛔️ **wizard**
사용하지 않습니다. 대신 "composer"를 사용합니다.

**WordPress**

**workspace**

**www**

#### Y

**YAML**
파일 유형을 참조하기 위해 파일 확장자를 사용하지 않습니다. 예를 들어, ".yaml file" 대신 "YAML file"을 사용합니다.

**YouTube**

#### Z

**zip code**

**zip file / zipped files**

**ZIP**
파일 유형을 참조하기 위해 파일 확장자를 사용하지 않습니다. 예를 들어, ".zip file" 대신 "ZIP file"을 사용합니다.