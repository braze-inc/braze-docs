---
nav_title: 템플릿 관리
article_title: 템플릿 관리
page_order: 3

page_type: reference
description: "이 참조 문서에서는 Braze 대시보드의 템플릿 및 미디어 섹션에서 템플릿을 복제하고 보관하는 방법을 설명합니다."
tool:
  - Templates
  - Media

---

# 템플릿 관리

> 템플릿을 보관하거나 복제하면 더 잘 조직하고 관리할 수 있습니다. 이 참조 문서에서는 Braze 대시보드의 **템플릿** 섹션에서 템플릿을 보관하고 복제하는 방법을 다룹니다.

## 템플릿 복제

### 개별 템플릿

![][8]{: style="float:right;max-width:15%;margin-left:15px;"}

개별 템플릿을 복제하려면 개별 템플릿의 <i class="fas fa-cog"></i> 톱니바퀴 아이콘을 선택하고 드롭다운 메뉴에서 **복제**를 선택합니다.
<br><br>

{% alert note %}
[콘텐츠 블록]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) 템플릿의 경우, 초안 사본이 생성됩니다. 다른 모든 템플릿의 경우 새 복제본이 자동으로 생성됩니다.
{% endalert %}

### 다중 템플릿

{% raw %}

여러 템플릿을 복제하려면 템플릿 이름 옆의 체크박스를 선택하면 됩니다. 먼저 템플릿을 선택한 다음 나타나는 **복제** 버튼을 선택합니다.

중복된 템플릿은 **마지막 편집** 열을 정렬하여 찾을 수 있습니다. 기본값으로, 새 템플릿은 `Copy of ORIGINAL_TEMPLATE_NAME`로 명명됩니다.

{% endraw %}

![사용자가 두 개의 템플릿을 선택하고 '복제'를 클릭하면 총 네 개의 템플릿이 생성되며, 템플릿이 마지막으로 편집된 시간 순서대로 정렬되는 GIF입니다.][9]

## 템플릿 보관

![세 가지 옵션을 보여주는 확장된 설정 드롭다운 메뉴: 아카이브 옵션이 강조 표시된 편집, 아카이브, 및 복제.][10]{: style="float:right;max-width:20%;margin-left:15px;"}

개별 템플릿을 보관하려면 템플릿 그리드 화면에서 설정 아이콘을 선택하고 **보관**을 선택합니다. 템플릿이 보관될 때 다음과 같은 다양한 시나리오를 참고하십시오:

- 활성 캠페인은 중단 없이 보관된 템플릿을 계속 사용합니다.
- 초안 캠페인은 보관된 템플릿의 내용을 유지하며 편집 및 시작할 수 있습니다.
- 보관된 템플릿을 편집하려면 먼저 보관 해제해야 합니다. 마찬가지로, 캠페인에 보관된 템플릿을 사용하려면 먼저 템플릿의 보관을 해제해야 합니다.

여러 템플릿을 보관하려면 보관하려는 각 템플릿 옆의 체크박스를 선택하십시오. 여러 템플릿을 선택한 후 **선택한 항목 보관**을 선택합니다. 템플릿 그리드에서 **보기** 아래 **보관됨**을 선택하여 보관된 템플릿을 찾을 수 있습니다.

![저장된 드롭 앤 드롭 이메일 템플릿 섹션에 두 개의 선택된 템플릿이 표시됩니다: 프리미엄 템플릿 시도하기 사용자가 "선택된 항목 보관" 버튼을 강조합니다.][11]

{% alert important %}
보관은 현재 [링크 템플릿]({{site.baseurl}}/user_guide/message_building_by_channel/email/link_templates/#link-templates)에 사용할 수 없습니다.
{% endalert %}

[10]: {% image_buster /assets/img/template_archive_cog.png %}
[11]: {% image_buster /assets/img/archive_multiple_template.png %}
[8]: {% image_buster /assets/img/template_duplicate_cog.png %}
[9]: {% image_buster /assets/img/duplicate_multiple_template.gif %}