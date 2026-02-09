---
nav_title: Braze 대시보드 검색하기
article_title: Braze 대시보드 검색하기
page_order: 0.5
page_type: reference
description: "Braze의 글로벌 검색에 대해 알아보세요."
---

# Braze 대시보드 검색하기

검색창을 사용해 Braze 대시보드 내에서 작업 및 기타 정보를 찾을 수 있습니다. 검색창은 Braze 대시보드 상단에 있습니다. 검색창을 클릭하거나 Windows의 경우 <kbd>Ctrl</kbd> + <kbd>K</kbd>, Mac의 경우 <kbd>⌘</kbd> + <kbd>K를</kbd> 눌러 검색창으로 바로 이동합니다.

'프로모션' 키워드 검색 결과, 프로모션 코드 페이지를 포함하여 프로모션이라는 용어가 포함된 캠페인과 아이템을 표시합니다.]({% image_buster /assets/img/navigation/global_search_new.png %})

## 무엇을 검색할 수 있나요?

다음 항목 및 작업을 검색할 수 있습니다:

- 캠페인 이름
- 캔버스 이름
- 콘텐츠 블록
- 세그먼트 이름
- 이메일 템플릿 이름
- [Braze 내 페이지](#find-pages-that-have-been-renamed)

{% alert tip %}
정확한 텍스트를 검색하려면 검색어를 따옴표("") 안에 넣으세요. 예를 들어, ["모든 사용자"]를 검색하면 이름에 "모든 사용자"라는 정확한 문구가 포함된 모든 항목이 반환됩니다.
{% endalert %}

## 주요 기능

### 키보드 단축키

키보드 단축키를 사용하여 검색 결과를 손쉽게 탐색할 수 있습니다:

<style>
  div.small_table + table {
    max-width: 60%;
  }
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2), {
    width:20%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

| 액션                      | 키보드 단축키                                                             |
| --------------------------- | ----------------------------------------------------------------------------- |
| 검색 메뉴 열기        | {::nomarkdown} <ul> <li> Mac: <kbd>⌘</kbd> + <kbd>K</kbd> </li> <li>Windows: <kbd>Ctrl</kbd> + <kbd>K</kbd> </li> </ul> {:/}  |
| 검색 결과 간 이동 | <kbd>⬆</kbd> / <kbd>⬇</kbd>  |
| 검색 결과 선택      | <kbd>입력</kbd>    |
| 검색 메뉴 닫기       | <kbd>Esc</kbd>  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 콘텐츠 유형 및 상태 태그

각 검색 결과는 결과의 콘텐츠 유형(페이지, 캠페인, 캔버스, 세그먼트, 이메일 템플릿) 및 상태(활성, 보관됨, 중지됨 등)를 나타내는 태그와 짝을 이룹니다.

### 최근에 연 콘텐츠에 액세스

검색 메뉴에서 최근에 액세스한 콘텐츠를 다시 방문할 수 있습니다. 검색 인터페이스는 검색창 아래에 최근에 열어본 결과를 표시하며, 전체 Braze 플랫폼에서 상호작용한 항목도 포함됩니다. 이를 통해 이전에 보았던 페이지, 캠페인, 캔버스, 세그먼트 또는 이메일 템플릿으로 돌아가서 더 적은 클릭으로 중단한 부분부터 바로 시작할 수 있습니다.

\![검색이 확장되어 최근에 연 페이지와 사용자에 대한 Braze 콘텐츠가 표시됩니다.]({% image_buster /assets/img/navigation/search_recently_opened.png %})

### 이름이 변경된 페이지 찾기

검색은 [업데이트된 탐색]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/) 기능에서 이름이 변경된 페이지의 동의어를 이해합니다. 예를 들어 '커런츠'를 검색하면 해당 페이지의 이름이 변경되었으므로 '데이터 내보내기'를 찾을 수 있습니다.

사용자가 "커런츠"를 검색한 "데이터 내보내기"에 대한 검색 결과입니다.]({% image_buster /assets/img/navigation/global_search_synonym.png %})

<!---

### Quick create campaigns

Search for channels to see quick create options among your top 10 results. For example, searching for "email" shows "Create Email Campaign" or "Create Transactional Email Campaign".

![][X]

--->

### 활성 및 초안 콘텐츠 필터링

**활성 및 초안만 표시를** 선택하여 검색 결과에 활성 및 **초안** 콘텐츠를 포함할 수 있습니다. 기본값은 토글이 켜져 있으며 보관된 콘텐츠를 포함한 모든 콘텐츠가 표시됩니다.

'활성 및 초안만 표시' 토글.]({% image_buster /assets/img/navigation/show_active_draft_new.png %})

### 이모티콘 검색

Braze에서 작품 이름을 지을 때 이모티콘을 사용하나요? 검색해 보세요! 이모티콘을 검색어로 사용할 수 있습니다. 😎



