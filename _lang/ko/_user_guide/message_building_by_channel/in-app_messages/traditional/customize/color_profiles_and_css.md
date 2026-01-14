---
nav_title: 색상 프로필 및 CSS 템플릿
article_title: 인앱 메시지를 위한 컬러 프로필 및 CSS 템플릿
page_order: 4
page_type: reference
description: "이 문서에서는 인앱 메시지 색상 프로필 및 CSS 템플릿에 대한 개요를 제공합니다."
channel:
  - in-app messages
---

# 색상 프로필 및 CSS 템플릿 {#reusable-color-profiles}

> 대시보드에 인앱 메시지와 인브라우저 메시지 템플릿을 저장하여 나만의 스타일로 새로운 캠페인과 메시지를 빠르게 구축할 수 있습니다. 

**템플릿** > **인앱 메시지 템플릿으로** 이동합니다.

이 페이지에서 기존 템플릿을 편집하거나 **\+ 생성을** 클릭하고 **색상 프로필** 또는 **CSS 템플릿을** 선택하여 인앱 메시징에 사용할 새 템플릿을 만들 수 있습니다.

## 색상 프로필

HEX 색상 코드를 입력하거나 색상 상자를 클릭하고 색상 선택기로 색상을 선택하여 메시지 템플릿의 색 구성표를 커스텀할 수 있습니다.

완료했으면 **색상 프로필 저장을** 클릭합니다.

### 색상 프로필 관리하기

템플릿을 [복제하고]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) [보관할]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) 수도 있습니다! 템플릿에서 템플릿 및 크리에이티브 콘텐츠를 만들고 관리하는 방법에 대해 자세히 알아보세요 [ & 미디어]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

## CSS 템플릿 {#in-app-message-templates}

[웹 모달 인앱 메시지에](#web-modal-css) 대한 완전한 CSS 템플릿을 커스텀할 수 있습니다.

CSS 템플릿의 이름을 지정하고 태그를 지정한 다음 기본값 템플릿으로 사용할지 여부를 선택합니다. 제공된 공간에 직접 CSS를 작성할 수 있습니다. 이 공간은 메시지 미리 보기에 표시된 CSS로 이미 미리 채워져 있으므로 필요에 따라 자유롭게 약간 조정하면 됩니다.

```css
.ab-message-header, .ab-message-text {
  color: #333333;
  text-align: center;
}

.ab-message-header {
  font-size: 20px;
  font-weight: bold;
}

.ab-message-text {
  font-size: 14px;
  font-weight: normal;
}

.ab-close-button svg {
  fill: #9b9b9b;
}

.ab-message-button {
  border: 1px solid #1b78cf;
  font-size: 14px;
  font-weight: bold;
}
.ab-message-button:first-of-type {
  background-color: white;
  color: #1b78cf;
}
.ab-message-button:last-of-type, .ab-message-button:first-of-type:last-of-type {
  background-color: #1b78cf;
  color: white;
}

.ab-background {
  background-color: white;
}

.ab-icon {
  background-color: #0073d5;
  color: white;
}

.ab-page-blocker {
  background-color: rgba(51, 51, 51, .75);
}
```

보시다시피 배경색부터 글꼴 크기와 굵기 등 모든 것을 편집할 수 있습니다.

### CSS 템플릿 관리하기

템플릿을 [복제하고]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) [보관할]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) 수도 있습니다! 템플릿에서 템플릿 및 크리에이티브 콘텐츠를 만들고 관리하는 방법에 대해 자세히 알아보세요 [ & 미디어]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

## CSS를 사용한 모달(웹 전용) {#web-modal-css}

웹 전용 웹 모달과 CSS 메시지를 사용하기로 선택한 경우 제공된 공간에 자체 템플릿을 적용하거나 직접 CSS를 작성할 수 있습니다. 이 공간은 메시지 미리 보기에 표시된 CSS로 이미 미리 채워져 있지만 필요에 따라 자유롭게 약간 조정할 수 있습니다.

나만의 템플릿을 적용하려면 **템플릿 적용을** 클릭하고 인앱 메시지 템플릿 갤러리에서 선택하세요. 옵션이 없는 경우 CSS 템플릿 빌더를 사용하여 [CSS 템플릿]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/color_profiles_and_css/#in-app-message-templates) 을 업로드할 수 있습니다.


