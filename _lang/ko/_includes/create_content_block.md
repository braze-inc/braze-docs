1. **템플릿** > **콘텐츠 블록으로** 이동합니다. <i class="fas fa-plus"></i> **콘텐츠 블록 만들기**를 클릭하고 **콘텐츠 블록 끌어서 놓기**를 선택합니다.

{% if include.location == "dnd" %}

{:start="2"}
2\. [편집기 블록]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) 을 끌어다 놓아 드래그 앤 드롭 콘텐츠 블록을 만듭니다.
3\. **행** 탭에서 서식 블록을 편집기로 끌어다 놓아 콘텐츠 블록의 레이아웃을 만듭니다. <br><br> ![]({% image_buster /assets/img_archive/dnd_content_block_composer.png %})<br><br>
4\. 필요에 따라 드래그 앤 드롭 콘텐츠 블록을 추가하여 이메일 캠페인을 구축할 수 있습니다.
5\. 콘텐츠 블록을 만든 후 **완료**를 클릭합니다.
6\. 콘텐츠 블록에 이름을 지정합니다. 이 이름은 **콘텐츠 블록 Liquid 태그**의 일부로 자동 입력됩니다.
7\. (선택 사항) 설명을 추가합니다.
8\. **콘텐츠 블록 시작**을 클릭합니다.

{% elsif include.location == "html" %}

{:start="2"}
2\. **HTML** 탭에서 HTML을 입력하거나 **클래식** 탭에서 콘텐츠 블록을 작성합니다. <br><br> ![]({% image_buster /assets/img_archive/html_content_block_composer.png %})<br><br>
4\. 콘텐츠 블록을 만든 후 **완료**를 클릭합니다.
5\. 콘텐츠 블록의 이름을 입력합니다. 이 이름은 **콘텐츠 블록 Liquid 태그**의 일부로 자동 입력됩니다.
6\. (선택 사항) 설명을 추가합니다.
7\. **콘텐츠 블록 시작**을 클릭합니다.

{% endif %}