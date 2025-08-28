---
nav_title: 콘텐츠 블록 라이브러리
article_title: 콘텐츠 블록 라이브러리
page_order: 1
page_type: reference
description: "이 참조 문서는 재사용 가능한 크로스채널 콘텐츠를 단일 중앙 위치에서 관리하기 위해 콘텐츠 블록 라이브러리를 사용하는 방법을 설명합니다."
tool: 
  - Templates
  - Media

---

# 콘텐츠 블록 라이브러리

> 콘텐츠 블록 라이브러리를 사용하면 재사용 가능한 크로스채널 콘텐츠를 단일 중앙 위치에서 관리할 수 있습니다.

콘텐츠 블록을 사용하면 다음을 수행할 수 있습니다.

- 이메일 캠페인의 헤더와 푸터로 사용하여 일관된 모양과 느낌을 만드세요.
- 다양한 채널을 통해 동일한 제안 코드를 배포하세요.
- 미리 정의된 자산을 생성하여 일관된 정보와 자산으로 메시지를 구축하는 데 사용할 수 있습니다.
- 전체 메시지 본문을 다른 메시지로 복사합니다.

## 콘텐츠 블록 만들기

콘텐츠 블록을 생성하는 데 사용되는 편집기에는 클래식과 드래그 앤 드롭의 두 가지 유형이 있습니다. 이 두 가지 유형의 편집기는 콘텐츠 블록 유형에 해당합니다: HTML 및 드래그 앤 드롭. You can also create and manage your Content Blocks [using the API]({{site.baseurl}}/api/endpoints/templates/).

{% tabs %}
{% tab 드래그 앤 드롭 %}

{% multi_lang_include create_content_block.md location="dnd" %}

{% endtab %}
{% tab HTML %}

{% multi_lang_include create_content_block.md location="html" %}

{% endtab %}
{% endtabs %}

### 콘텐츠 블록 사양

| 콘텐츠 블록 속성 | 사양 |
|---|---|
| 이름 | 최대 100자까지 입력 가능한 필수 필드입니다. 콘텐츠 블록이 저장된 후에는 이름을 변경할 수 없습니다. 또한, 이전 콘텐츠 블록이 보관되었더라도 새 콘텐츠 블록에 이전 콘텐츠 블록과 동일한 이름을 지정할 수 없습니다. |
| 설명 | (선택 사항) 최대 250자. 콘텐츠 블록을 설명하여 다른 Braze 사용자가 그것이 무엇을 위한 것이며 어디에 사용되는지 알 수 있도록 하세요. |
| 콘텐츠 크기 | 최대 50KB. |
| 배치 | 콘텐츠 블록은 이메일 바닥글 내에서 사용할 수 없습니다. |
| 생성 | HTML 편집기 또는 드래그 앤 드롭 편집기. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
콘텐츠 블록을 만들 때 줄 바꿈을 추가하여 HTML과 Liquid를 시각화하면 도움이 될 수 있습니다. 이 줄 바꿈이 전송 중에 남아 있으면 블록이 렌더링되는 방식에 영향을 줄 수 있는 불필요한 공백이 생길 위험이 있습니다. 이를 피하려면 블록에 **Capture** 태그를 사용하고 **| strip** 필터를 함께 사용하십시오.
{% raw %}
```
{% capture your_variable %}
{{content_blocks.${your_content_block}}}
{% endcapture %}{{your_variable | strip}}
```
{% endraw %}
{% endalert %}

## 콘텐츠 블록 사용

콘텐츠 블록을 만든 후 다음 단계를 따라 메시지에 삽입할 수 있습니다: 

1. **콘텐츠 블록 Liquid 태그**를 **콘텐츠 블록 세부 정보** 섹션에서 복사합니다.
2. 메시지에 콘텐츠 블록 Liquid 태그를 삽입합니다. Liquid 및 태그를 자동으로 채우기 위해 입력을 시작할 수도 있습니다.

### 알아두어야 할 사항

- 끌어서 놓기 이메일에 HTML 콘텐츠 블록을 **사용하거나** HTML 이메일에 콘텐츠 블록을 끌어서 놓으면 예기치 않은 렌더링 문제가 발생할 수 있습니다. 드래그 앤 드롭 편집기는 콘텐츠를 동적으로 렌더링하는 HTML 및 CSS를 생성하는 반면 HTML 편집기는 정적이기 때문입니다.
- Canvas event properties are only supported in a Canvas. If you reference a Content Block with Canvas entry properties in a campaign, it won’t populate.

### 콘텐츠 블록 업데이트 및 복사

콘텐츠 블록을 업데이트하기로 선택하면 Liquid를 통해 삽입된 경우 콘텐츠 블록이 사용되는 모든 메시지에서 업데이트됩니다. 드래그 앤 드롭 편집기에서 **행** 아래의 **콘텐츠 블록** 드롭다운을 사용하여 콘텐츠 블록을 가져오면 모든 메시지에서 업데이트되지 않습니다.

단일 메시지에 대한 콘텐츠 블록을 업데이트하거나 다른 메시지에서 사용할 복사본을 만들려면 원본 메시지에서 HTML을 새 메시지로 복사하거나 원본 콘텐츠 블록을 편집(이미 메시지에서 사용된 경우)하고 저장할 수 있습니다. 새로운 콘텐츠 블록으로 저장할 수 있는 프롬프트가 표시됩니다.

After making edits to a Content Block, you can save and launch the updated Content Block by selecting **Launch Content Block**. 또는 **더보기** > **복제**를 선택하여 콘텐츠 블록의 복제본을 만들 수 있습니다.

![A Content Block that reads "Welcome to our newsletter".]({% image_buster /assets/img/copy-content-block.png %})

You can also [duplicate]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) a Content Block. 이것은 콘텐츠 블록의 초안 사본을 만듭니다.

### 콘텐츠 블록 미리보기

활성 캠페인 또는 캔버스에 콘텐츠 블록을 추가한 후, 콘텐츠 블록 위에 마우스를 올리고 <i class="fa fa-eye preview-icon"></i> **미리보기** 아이콘을 선택하여 콘텐츠 블록 라이브러리에서 이 콘텐츠 블록을 미리볼 수 있습니다. 

이 미리보기에는 콘텐츠 블록에 대한 정보가 포함되어 있습니다. 예를 들어, 누가 만들었는지, 태그, 생성 날짜, 마지막 편집 날짜, 설명, 편집기 유형, 세부 사항이 포함된 포함 횟수, 그리고 실제 콘텐츠 블록의 미리보기가 포함됩니다.

![A preview of a Content Block "Workout_Promo" for cycling and dancing that has six inclusions.]({% image_buster /assets/img/preview_tab_content_block.png %}){: style="max-width:60%;"} 

### 중첩 콘텐츠 블록

콘텐츠 블록은 중첩될 수 있지만 한 번만 가능합니다. 콘텐츠 블록 A를 콘텐츠 블록 B에 중첩할 수 있지만, 콘텐츠 블록 B를 콘텐츠 블록 C에 중첩할 수는 없습니다.

{% alert warning %}
셋째 수준의 콘텐츠 블록을 중첩하는 것을 막을 수는 없지만, 콘텐츠가 두 번째 수준을 넘어 중첩되는 것은 볼 수 없습니다. 콘텐츠와 Liquid 스니펫이 메시지에서 제거됩니다.
{% endalert %}

또한 콘텐츠 블록은 이메일 바닥글 내에서 사용할 수 없지만, 이메일 바닥글은 콘텐츠 블록 내에서 사용할 수 있습니다.

### 콘텐츠 블록 보관

![확장된 설정 드롭다운 메뉴에는 세 가지 옵션이 표시됩니다: Archive, Duplicate, and Copy to workspace.]({% image_buster /assets/img/template_archive_cog.png %}){: style="max-width:20%;float:right;margin-left:15px;" }

Once you have finished using a Content Block, you can archive it from the [Templates & Media]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) page. 보관된 콘텐츠 블록은 읽기 전용이므로 편집하기 전에 콘텐츠 블록의 보관을 해제하십시오. 콘텐츠 블록은 메시지에서 사용되는 경우 보관할 수 없습니다.

#### 모범 사례

- 블록이 몇 개의 이메일에서만 사용되는 경우, 오래된 블록을 보관하고 보관되지 않은 새 블록으로 실시간 메시지를 업데이트하는 것이 좋습니다.
- 블록에 오타가 있거나 사소한 변경이 필요한 경우, 블록을 보관하는 것을 권장하지 않습니다. Instead, update the block and get sending!
- When your block is used in more messages than you can reasonably manage with the first suggestion in this list, we recommend removing all content from the block and archiving it. 이것은 새로 보낸 이메일에 오래된 정보가 포함되지 않도록 보장할 것입니다.
- 콘텐츠 블록을 실수로 보관하면 보관 해제할 수 있습니다.

![저장된 콘텐츠 블록 패널에서 "Test_32"의 설정 드롭다운 메뉴가 확장되어 세 가지 옵션이 표시됩니다: Unarchive, Duplicate, and Copy to workspace]({% image_buster /assets/img/unarchive-content-block.png %})

