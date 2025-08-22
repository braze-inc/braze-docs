{% if include.location == "dnd" %}

1. **템플릿** > **콘텐츠 블록으로** 이동합니다. <i class="fas fa-plus"></i> **콘텐츠 블록 만들기를** 선택하고 **콘텐츠 블록 끌어서 놓기를** 선택합니다.
2. [편집기 블록]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) 을 끌어다 놓아 드래그 앤 드롭 콘텐츠 블록을 만듭니다. 
3. **행** 탭에서 서식 블록을 편집기로 끌어다 놓아 콘텐츠 블록의 레이아웃을 만듭니다. <br><br> ![드래그 앤 드롭 콘텐츠 블록 작성기]({% image_buster /assets/img_archive/dnd_content_block_composer.png %})<br><br>
4. 필요에 따라 드래그 앤 드롭 콘텐츠 블록을 추가하여 이메일 캠페인을 구축할 수 있습니다.
5. 콘텐츠 블록을 생성한 후 **완료를** 선택합니다.
6. 콘텐츠 블록에 이름을 지정합니다. 이 이름은 **콘텐츠 블록 Liquid 태그**의 일부로 자동 입력됩니다.
7. (선택 사항) 설명을 추가합니다.
8. 콘텐츠 블록이 어떻게 표시되는지 확인하려면 **미리 보기** 탭을 선택합니다. 선택 사항으로 **미리보기 링크 복사를** 선택하여 임의의 사용자에게 이메일이 어떻게 표시되는지 보여주는 공유 가능한 미리보기 링크를 생성하고 복사합니다. 링크는 7일 동안 지속되며 그 후 다시 생성해야 합니다.<br><br> !["드래그 앤 드롭 콘텐츠 블록 작성기의 '미리보기' 탭.]({% image_buster /assets/img_archive/dnd_content_block_preview_link.png %})<br><br>
9. **콘텐츠 블록 시작을** 선택합니다.

{% elsif include.location == "html" %}

1. **템플릿** > **콘텐츠 블록으로** 이동합니다. <i class="fas fa-plus"></i> **콘텐츠 블록 생성을** 선택하고 **HTML 콘텐츠 블록을** 선택합니다.
2. **HTML** 탭에서 HTML을 입력하거나 **클래식** 탭에서 콘텐츠 블록을 작성합니다. <br><br> ![HTML 콘텐츠 블록 작성기]({% image_buster /assets/img_archive/html_content_block_composer.png %})<br><br>
4. 콘텐츠 블록을 생성한 후 **완료를** 선택합니다.
5. 콘텐츠 블록의 이름을 입력합니다. 이 이름은 **콘텐츠 블록 Liquid 태그**의 일부로 자동 입력됩니다.
6. (선택 사항) 설명을 추가합니다.
7. 콘텐츠 블록이 어떻게 표시되는지 확인하려면 **미리 보기** 탭을 선택합니다. 선택 사항으로 **미리보기 링크 복사를** 선택하여 임의의 사용자에게 이메일이 어떻게 표시되는지 보여주는 공유 가능한 미리보기 링크를 생성하고 복사합니다. 링크는 7일 동안 지속되며 그 후 다시 생성해야 합니다.<br><br> !["HTML 콘텐츠 블록 작성기의 '미리보기' 탭.]({% image_buster /assets/img_archive/content_block_html_preview_link.png %})<br><br>
8. **콘텐츠 블록 시작을** 선택합니다.

{% endif %}