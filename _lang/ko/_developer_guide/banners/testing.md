---
nav_title: 테스트 배너
article_title: 테스트 배너
page_order: 2
description: "캠페인을 시작하기 전에 배너 메시지를 테스트하는 방법을 배우세요. 모든 미디어, 복사, 개인화 및 커스텀 속성이 올바르게 렌더링되는지 확인할 수 있습니다."
channel:
  - banners
noindex: true
---

# 테스트 배너

> 캠페인을 시작하기 전에 배너 메시지를 테스트하는 방법을 배우세요. 모든 미디어, 복사, 개인화 및 커스텀 속성이 올바르게 렌더링되는지 확인할 수 있습니다. 더 일반적인 정보는 [배너에 대한 정보]({{site.baseurl}}/developer_guide/banners)를 참조하세요.

## Prerequisites

Braze에서 배너 메시지를 테스트하기 전에 [Braze에서 배너 캠페인]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/)을 생성해야 합니다. 또한, 테스트하려는 배치가 이미 [앱 또는 웹사이트에 배치되어 있는지]({{site.baseurl}}/developer_guide/banners/placements) 확인하세요. 

테스트를 [콘텐츠 테스트 그룹]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) 또는 개별 사용자에게 보내려면, 푸시가 테스트 사용자에 대해 유효한 푸시 토큰이 등록된 테스트 기기에서 활성화되어 있어야 합니다.

## 배너 테스트

{% multi_lang_include banners/testing.md page="testing" %}
