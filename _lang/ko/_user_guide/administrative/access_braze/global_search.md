---
nav_title: Braze 대시보드 검색
article_title: Braze 대시보드 검색
page_order: 0.5
page_type: reference
description: "Braze에서 글로벌 검색에 대해 알아보세요."
---

# Braze 대시보드 검색

검색 창을 사용하여 Braze 대시보드 내에서 작업 및 기타 정보를 찾을 수 있습니다. 검색 창은 Braze 대시보드 상단에 있습니다. 검색창을 클릭하거나 Windows에서 <kbd>Ctrl</kbd> + <kbd>K</kbd>를 누르거나 Mac에서 <kbd>⌘</kbd> + <kbd>K</kbd>를 눌러 검색창으로 바로 이동하세요.

!["promo" 키워드에 대한 검색 결과, promo라는 용어를 포함하는 캠페인 및 항목을 보여주며, 페이지 프로모션 코드가 포함됩니다.][1]

## 무엇을 검색할 수 있습니까?

다음 항목 및 작업을 검색할 수 있습니다:

- 캠페인 이름
- 캔버스 names
- 콘텐츠 블록
- 세그먼트 이름
- 이메일 템플릿 이름
- [페이지 내 Braze](#find-pages-that-have-been-renamed)

{% alert tip %}
정확한 텍스트를 검색하려면 검색어를 따옴표("")로 묶으세요. 예를 들어, [“모든 사용자”]를 검색하면 이름에 “모든 사용자”라는 정확한 구문이 포함된 모든 항목이 반환됩니다.
{% endalert %}

## 주요 기능

### 키보드 단축키

키보드 단축키로 검색 결과를 손쉽게 탐색하세요:

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

| 작업                      | 키보드 단축키                                                             |
| --------------------------- | ----------------------------------------------------------------------------- |
| 검색 메뉴 열기        | {::nomarkdown} <ul> <li> 맥: <kbd>⌘</kbd> + <kbd>K</kbd> </li> <li>윈도우: <kbd>Ctrl</kbd> + <kbd>K</kbd> </li> </ul> {:/}  |
| 검색 결과 간 이동 | <kbd>⬆</kbd> / <kbd>⬇</kbd>  |
| 검색 결과 선택      | <kbd>진입</kbd>    |
| 검색 메뉴 닫기       | <kbd>Esc</kbd>  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 콘텐츠 유형 및 상태 태그

각 검색 결과에는 결과의 콘텐츠 유형(페이지, 캠페인, 캔버스, 세그먼트, 이메일 템플릿) 및 상태(활성, 보관됨, 중지됨 등)를 나타내는 태그가 함께 제공됩니다.

### 최근에 열린 콘텐츠에 액세스

검색 메뉴에서 최근에 액세스한 콘텐츠를 다시 방문할 수 있습니다. 검색 인터페이스는 검색창 아래에 최근에 열었던 결과를 표시하며, Braze 플랫폼 전체에서 상호작용한 항목들을 포함합니다. 이 기능을 사용하면 이전에 본 페이지, 캠페인, 캔버스, 세그먼트 또는 이메일 템플릿으로 돌아가서 클릭 수를 줄이고 중단한 지점에서 바로 다시 시작할 수 있습니다.

![검색이 확장되어 최근에 열린 페이지와 사용자를 위한 Braze 콘텐츠를 보여줍니다.][2]

### 이름이 변경된 페이지 찾기

검색은 [업데이트된 탐색]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/)에서 이름이 변경된 페이지에 대한 동의어를 이해합니다. 예를 들어, 해당 페이지가 이름이 변경되었기 때문에 "커런츠"를 검색하면 "데이터 내보내기"를 찾을 수 있습니다.

!["데이터 내보내기"에 대한 검색 결과로, 사용자가 "커런츠"를 검색한 경우입니다.][3]

<!---

### Quick create campaigns

Search for channels to see quick create options among your top 10 results. For example, searching for "email" shows "Create Email Campaign" or "Create Transactional Email Campaign".

![][X]

--->

### 활성 및 초안 콘텐츠에 대한 필터

검색 결과에 **활성 및 초안만 표시**를 선택하여 활성 및 초안 콘텐츠를 포함할 수 있습니다. 기본값으로, 토글이 켜져 있으며, 보관된 내용을 포함한 모든 내용이 표시됩니다.

!["활성 및 초안만 표시" 토글.][4]

### 이모티콘 검색

Braze에서 작업 이름을 지정할 때 이모지를 사용하나요? 이모지를 검색해 보세요! 이모지를 검색어로 사용할 수 있습니다. 😎

[1]: {% image_buster /assets/img/navigation/global_search_new.png %}
[2]: {% image_buster /assets/img/navigation/search_recently_opened.png %}
[3]: {% image_buster /assets/img/navigation/global_search_synonym.png %}
[4]: {% image_buster /assets/img/navigation/show_active_draft_new.png %}


