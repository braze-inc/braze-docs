---
nav_title: 용어 사전
article_title: 용어집 레이아웃
page_order: 0
noindex: true
---

# 레이아웃 예시: 용어 사전

> 용어집 레이아웃은 YAML로 되어 있습니다. 여기에는 몇 가지 구성 요소와 매개 변수가 필요합니다. 용어집 레이아웃은 사전이나 특정 카테고리의 콘텐츠와 같이 현지화된 검색 가능한 콘텐츠에 적합합니다.

## 필수 구성 요소

1. YAML 열기 및 닫기 표기법. 즉, 콘텐츠 앞에는 `---`, 뒤에는 `---`을 입력합니다. 
2. 특정 매개변수 내용을 따옴표로 묶습니다. (헤더 매개변수, 텍스트 매개변수, 하이픈 또는 기타 특수 문자가 포함된 콘텐츠)
3. 용어집 태그 표기법(필터 태그)

## 필수 매개 변수

|매개변수 | 콘텐츠 유형 | 세부 정보 |
|---|---|---|
|`page_order`| 숫자 | 섹션 내에서 페이지를 주문합니다. 이 순서는 왼쪽 탐색에 반영됩니다. |
| `nav-title`| 영숫자 | 왼쪽 탐색에 표시될 제목을 입력합니다. |
|`layout`| 영숫자 - 공백 없음 | 문서의 [레이아웃 섹션에서](https://github.com/Appboy/braze-docs/tree/develop/_layouts) 레이아웃을 선택합니다. | 
|`glossary_top_header` | 영숫자 | 큰따옴표가 필요합니다. 페이지 상단에 제목이 표시됩니다. |
|`glossary_top_text`| 문자열, 영숫자 | 용어집 페이지를 설명합니다. 검색창과 필터(필터를 선택한 경우) 위에 표시됩니다. 이것은 기본적으로 HTML로 작성되었으므로 \`\`\`를 사용할 수 있습니다.<br> 를 사용하여 줄 바꿈을 만듭니다. | 
|`glossary_tag_name` | 단일 단어, 영숫자 | 필터에 이름을 지정합니다. 검색창 아래의 확인란과 아래 데이터에 표시됩니다. | 
|`glossary_filter_text`| 문자열, 영숫자 | 필터에 대해 설명하세요. 일반적으로 지시하는 데 사용됩니다. | 
|`glossary_tags`| 더 많은 YAML 플러스 콘텐츠. | 아래와 같이 포맷합니다: <br> glossary_tags: <br>  \- 이름: 콘텐츠 카드 <br>  \- 이름: 이메일 | 
| `glossaries`| 더 많은 YAML 플러스 콘텐츠. | 아래 [용어집 매개변수를](#glossaries-parameters) 참조하세요. |

### 용어집 매개변수

|매개변수 | 콘텐츠 유형 | 세부 정보 |
|---|---|---|
|`name`| 영숫자 | 용어집 항목의 이름을 지정합니다.| 
|`description`| 문자열, 영숫자 | 용어집 항목을 설명합니다. | 
|`calculation`| 문자열 | (선택 사항) 용어집 항목의 계산 방법을 설명합니다(일반적으로 데이터 또는 메트릭을 설명할 때 사용됨). | 
|`tags`| 영숫자 | `glossary_tags` 에 `name` 로 표시된 것과 일치해야 합니다. 해당하는 수만큼 나열합니다. `All`을 작성하면 모든 필터에 해당 항목이 포함됩니다.|

## 예시

```
---
page_order: 0
nav_title: Report Metrics Glossary
layout: glossary_page
glossary_top_header: "Report Metrics Glossary"
glossary_top_text: "These are terms you'll find in your reports in your Braze account. Search for the metrics you need, or filter by channel. <br>  <br> This glossary does not necessarily include metrics you might see in Currents or in other downloaded reports outside of your Braze account."

glossary_tag_name: Channels
glossary_filter_text: "Select Channels below to narrow the glossary:"

# channel to icon/fa or image mapping
glossary_tags:
  - name: Content Cards
  - name: Email
  - name: In-App Message
  - name: News Feed
  - name: Web Push
  - name: iOS Push
  - name: Android Push
  - name: Webhook

glossaries:
  - name: Variation
    description: Variation of a campaign, differing as defined by the creator.
    calculation: Count
    tags:
      - All
  - name: Audience
    description: Percentage of users who received a particular message. This number is received from Braze.
    calculation: (Number of Recipients in Variant) / (Unique Recipients)
    tags:
      - All
  - name: Unique Recipients
    description: Exact number of users who received a particular message. This number is received from Braze.
    calculation: Count
    tags:
      - Email
      - Web Push
      - iOS Push
      - Android Push
      - In-App Message
      - News Feed
  - name: Total Impressions
    description: The number of users whose devices reported that the in-app message has been delivered (if a user receives a message twice, they will be counted twice). This number is a sum of number of impression events that Braze receives from the SDKs.
    calculation: Count
    tags:
      - In-App Message
      - News Feed
      - Content Cards
---
```
