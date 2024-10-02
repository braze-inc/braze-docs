---
nav_title: 개요
page_order: 0
noindex: true
---

# 레이아웃 예시: 개요

> 개요 레이아웃은 사용자가 버튼을 클릭하여 페이지의 특정 부분 또는 완전히 다른 페이지로 이동할 수 있도록 페이지 상단에 특정 탐색 옵션을 만드는 데 유용합니다.

셀렉터 레이아웃의 대표적인 예로는 [SDK 체인지로그](https://www.braze.com/docs/developer_guide/platform_integration_guides/sdk_changelogs/) 페이지 또는 [인앱 메시지 크리에이티브 세부 정보 페이지](https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/)가 있습니다.

## 필수 구성 요소

1. YAML 열기 및 닫기 표기법. 즉, 콘텐츠 앞에는 ---, 뒤에는 ---가 표시됩니다.
2. 특정 매개변수 내용을 따옴표로 묶습니다. (헤더 매개변수, 텍스트 매개변수, 하이픈 또는 기타 특수 문자가 포함된 콘텐츠)
3. 용어집 태그 표기법(필터 태그)

## 필수 매개 변수

|매개변수 | 콘텐츠 유형 | 세부 정보 |
|---|---|---|
|`page_order`| 숫자 | 섹션 내에서 페이지를 주문합니다. 이 순서는 왼쪽 탐색에 반영됩니다. |
| `nav-title`| 영숫자 | 왼쪽 탐색에 표시될 제목을 입력합니다. |
|`layout`| 영숫자 - 공백 없음 | 문서의 [레이아웃 섹션에서](https://github.com/Appboy/braze-docs/tree/develop/_layouts) 레이아웃을 선택합니다. | 
|`guide_top_header`|영숫자 | 페이지 제목을 지정합니다.|
|`guide_top_text`|영숫자 | 페이지에 대한 설명을 입력하면 버튼과 버튼의 제목 바로 위에 표시됩니다. 콘텐츠 주위에 따옴표가 필요합니다. |
|`guide_featured_title`| 영숫자 | 카드 제목을 지정합니다. 버튼 바로 위에 표시됩니다.
|`guide_featured_list`| 더 많은 YAML, 영숫자 | 아래 [가이드 목록 형식](#guide-listing-format)을 참조하세요. |

### 가이드 목록 형식

|매개변수 | 콘텐츠 유형 | 세부 정보 |
|---|---|---|
|`name`| 영숫자 | 상자 이름을 지정합니다. |
| `link`| URL 또는 경로 | 상자가 이동할 위치로 연결되는 링크입니다. 전체 URL 또는 `/docs...`(내부 링크인 경우)를 포함해야 합니다  |
|`image`| 경로 | 이미지 위치로 연결되는 링크입니다. |

형식 예제:

```yaml
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
```

## 예시

```yaml
---
nav_title: Creative Details
page_order: 4
layout: featured
guide_top_header: "Creative Details"
guide_top_text: "Get creative with our in-app messages! But you should know some of the guidelines, first! After all, you have to know those rules to break them! Check out the individual message type's Creative Specs or the global Creative Details below."

guide_featured_title: "Message Type Creative Specs"
guide_featured_list:
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
- name: Slideup
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#slideup
  image: /assets/img/braze_icons/arrow-circle-broken-up.svg
- name: Full-Screen
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#full-screen
  image: /assets/img/braze_icons/expand-05.svg
---

# Creative Details {#general}

Braze in-app messages have both global and individual creative specifications. For more information on our more customizable in-app message types, go to our [Customize]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/) page.

{% alert important %}
  These details only apply to our most recent in-app message generation (Generation 3). If you are not using our newest generation of in-app messages, check out our [previous in-app message generations]({{ site.baseurl }}/help/best_practices/in-app_messages/previous_in-app_message_generations/) documentation.
{% endalert %}
```
