---
nav_title: 기타 레벨
article_title: 기타 레벨
alias: /partners/otherlevels/
description: "이 문서에서는 OtherLevels Experience Platform과 Braze 간의 통합에 대해 설명합니다."
page_type: partner
search_tag: OtherLevels

---

# 기타 레벨

> [기타레벨](https://www.otherlevels.com/) 경험 플랫폼은 GenAI를 사용하여 스포츠 브랜드, 퍼블리셔 및 운영자가 기존 콘텐츠를 대규모의 브랜드 맞춤형 비디오 및 리치 미디어 경험으로 전환함으로써 고객과 연결하는 방식을 혁신합니다.

*이 통합은 OtherLevels에서 유지 관리합니다.*

## Overview

Braze와 OtherLevels의 통합을 통해 OtherLevels 경험 플랫폼에 대한 API 호출을 통해 커스텀 GenAI 비디오를 만든 다음, 이러한 비디오를 [Braze 연결된 콘텐츠를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) 통해 iOS 푸시 비디오로 사용자에게 전송할 수 있습니다.

다른 레벨의 AI 기반 경험으로 사용자에게 더 나은 경험을 제공하세요. 기존 콘텐츠와 타사 콘텐츠를 확장성이 뛰어난 비디오 및 리치 미디어로 변환하여 이미 다양한 방식으로 콘텐츠를 소비하고 상황별 개인화된 경험에 강력하게 반응하는 오디언스에게 제공할 수 있습니다.

## 필수 조건

Before you start, you'll need the following:

| Prerequisite          | 설명                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| 기타 레벨 계정   | 이 파트너십을 이용하려면 OtherLevels 계정이 필요합니다.                                                                     |
| A Braze REST API key  | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| A Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance.                                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

이 통합을 위해서는 비디오 생성 프로세스의 일부로 OtherLevels Experience Platform API를 호출해야만 Braze에서 사용자에게 메시지를 보낼 수 있습니다. 이 설명서의 일부로 cURL 예제가 제공되지만, API 호출을 자동화하려면 Postman과 같은 API 클라이언트를 사용하는 것이 좋습니다.

## 사용 사례

다른 레벨 경험 플랫폼으로 제작한 GenAI 동영상을 사용하여 다음을 수행할 수 있습니다:
- 스포츠 구단주 및 리그, 팬 참여, 스포츠 북, i게이밍, 복권을 위한 더 나은 경험을 만들어 보세요.
- 텍스트 기반 콘텐츠를 리치 미디어와 비디오로 변환하여 인간적이고 고객 참여도가 높은 경험을 만들어 고객 마케팅을 강화하세요.
- 기존 Braze 통합을 재구축하지 않고 확장하여 고객 확보부터 유지까지 성과를 높일 수 있습니다.

## 다른 레벨 경험 플랫폼 통합하기

### 1단계: 기타 레벨 경험 플랫폼 API를 호출하여 비디오 생성하기 {#step-1}

통합의 첫 번째 단계는 다른 레벨의 경험 플랫폼 API를 호출하여 새 동영상을 생성하는 것입니다. 동영상 생성은 즉시 이루어지지 않는다는 점에 유의하세요. 동영상의 길이와 복잡성에 따라 콘텐츠 제작에 최대 30분이 소요될 수 있습니다. 메시징 일정과 API 호출을 적절히 계획하여 동영상 생성을 위한 API 호출이 Braze 메시지 전송 예정 시간보다 충분히 앞서 이루어질 수 있도록 하세요.

{% alert important %}
다음 요청은 cURL을 사용합니다. 보다 효율적인 API 요청 관리를 위해 Postman과 같은 API 클라이언트를 사용하는 것이 좋습니다.
{% endalert %}

API 호출을 구조화하는 방법은 다음 예시를 참조하세요. 동영상 세부 사항을 커스텀하고 API 호출을 구성하는 방법에 대한 자세한 내용은 [GenAI 동영상 커스터마이징하기를](#customizing-the-genai-video) 참조하세요.

{% raw %}
```bash
curl --request POST \
  --url 'https://exp-platform-api.prod.awsotherlevels.com/v1/app/OTHERLEVELS_PROJECT_KEY/media?=' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/10.3.0' \
  --data '{
    "task": {
        "type": "tasks",
        "tasks": {
            "image_video_overlay": {
                "width": "= .orientation == '\''portrait'\'' ? '\''1080'\'' : .orientation == '\''landscape'\'' ? '\''1920'\''",
                "height": "= .orientation == '\''portrait'\'' ? '\''1920'\'' : .orientation == '\''landscape'\'' ? '\''1080'\''",
                "color": "255,255,255,0",
                "y_pos": "0",
                "x_pos": "0",
                "image_input": "= tasks.resize_image.jpg ?? tasks.resize_image.png",
                "video_input": "= tasks.talking_talent_replace_bg.mp4",
                "type": "compose.ImageVideoOverlay"
            },
            "resize_image": {
                "media_input": "= tasks.bg_image.jpg ?? tasks.bg_image.png",
                "type": "compose.MediaResize",
                "width": "= .orientation == '\''portrait'\'' ? '\''1080'\'' : .orientation == '\''landscape'\'' ? '\''1920'\''",
                "height": "= .orientation == '\''portrait'\'' ? '\''1920'\'' : .orientation == '\''landscape'\'' ? '\''1080'\''"
            },
            "bg_image": {
                "type": "load",
                "url": "BACKGROUND_IMAGE_URL",
                "refresh_interval": "12h"
            },
            "talking_head": {
                "test": false,
                "title": "INSERT_TITLE",
                "caption": false,
                "templateId": "TALENT_TEMPLATE",
                "type": "TALENT_MODEL",
                "variables": {
                    "script": {
                        "name": "script",
                        "properties": {
                            "content": "= tasks.translate_text.text"
                        },
                        "type": "text"
                    }
                }
            },
            "translate_text": {
                "type": "translate_text",
                "source": "en",
                "target": "en",
                "text": "INSERT_SCRIPT"
            },
            "talking_talent_speed": {
                "type": "compose.VideoSetSpeed",
                "speed": "1.0",
                "video_input": "= tasks.talking_head.mp4"
            },
            "talking_talent_replace_bg": {
                "type": "compose.VideoReplaceBg",
                "video_background": "= tasks.resize_image.jpg ?? tasks.resize_image.png",
                "video_input": "= tasks.talking_talent_speed.mp4"
            }
        },
        "output": "image_video_overlay"
    }
}'
```
{% endraw %}

Replace the following:

| Placeholder          | Description                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `OTHERLEVELS_PROJECT_KEY`   | 기타 레벨 계정이 프로비저닝되면 기타 레벨 프로젝트 키가 제공됩니다.                                                                     |
| `BACKGROUND_IMAGE_URL`  | 동영상의 배경에 대한 HTTPS URL입니다. |
| `INSERT_TITLE` | 동영상 제목은 내부 참조용이며 동영상에 표시되지 않습니다.                                                 |
| `TALENT_TEMPLATE` | 재능 템플릿 ID. 기타 레벨은 계정 프로비저닝 중에 재능(아바타)을 생성하기 위해 사용자와 협력합니다. 사용할 수 있는 Talent ID가 하나 또는 여러 개 제공됩니다.                                                 |
| `TALENT_MODEL` | 인재 모델 ID. 기타 레벨은 계정 프로비저닝 중에 재능(아바타)을 생성하기 위해 사용자와 협력합니다. 사용할 수 있는 재능 모델을 하나 또는 여러 개 제공받게 됩니다.                                                 |
| `INSERT_SCRIPT` | 동영상에서 출연자가 말하길 원하는 정확한 대본입니다.                                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

API 응답의 일부로 OtherLevels는 성공적인 API 호출을 나타내는 JSON 페이로드를 반환합니다. JSON에는 생성된 동영상을 식별할 수 있는 고유 식별자 `recipe_id` 가 포함됩니다. 다음 단계에서는 `recipe_id` 주소가 필요합니다.

다음은 API의 응답 예시입니다:

{% raw %}
```bash
{"$schema":"https://exp-platform-api.prod.awsotherlevels.com/schemas/GenerateMediaResBody.json","message":"success","recipe_id":"LMINHWXV2BBD6JGV5VF3ZNZV7BDDRR7FH5FJH6MMX4BVLTPRKTWQ","media_short_id":"LMINHWX","status":"triggered"}
```
{% endraw %}

### 2단계: `recipe_id` 을 커스텀 속성으로 설정하기

이제 [1단계에서](#step-1) 받은 `recipe_id` 이 동영상을 전송할 사용자의 Braze 커스텀 속성으로 설정됩니다.

사용 사례에 따라 많은 오디언스를 대상으로 하는 단일 동영상을 생성했을 수 있으며, 이 경우 여러 사용자를 위해 동일한 `recipe_id` 을 설정할 수 있습니다. 또는 각각 다른 사용자를 타겟팅하는 여러 개의 고유 동영상을 생성했을 수 있으며, 이 경우 각 사용자마다 Braze 커스텀 속성으로 설정된 `recipe_id` 을 사용해야 합니다.

{% alert important %}
다음 요청은 cURL을 사용합니다. 보다 효율적인 API 요청 관리를 위해 Postman과 같은 API 클라이언트를 사용하는 것이 좋습니다.
{% endalert %}

{% raw %}
```bash
curl --location --request POST 'BRAZE_API_ENDPOINT/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer BRAZE_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "USER_ID",
      "olxpmedia": "RECIPE_ID"
    }
  ]
}'
```
{% endraw %}

Replace the following:

| Placeholder             | Description                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT`    | The Braze REST endpoint URL of your current Braze instance. 자세한 내용은 [REST API 키를]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys) 참조하세요. |
| `BRAZE_API_KEY`         | Your Braze REST API key with the `users.track` permission.                                                                                                                                      |
| `USER_ID`              | 이 특정 동영상을 수신할 사용자 ID입니다. 사용할 수 있는 식별자의 더 많은 예는 [/users/track을]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users) 참조하세요.                                                                                                                                                  |
| `RECIPE_ID`       | [1단계의](#step-1) OtherLevels API 응답에서 받은 `recipe_id`.                                                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### 3단계: Braze를 통해 연결된 콘텐츠 보내기

GenAI 동영상을 iOS 푸시 메시지로 사용자에게 전송하려면 다음 단계를 따르세요:

1. Braze iOS 푸시 알림 캠페인을 만듭니다.
2. 캠페인을 작성하는 동안 **자산** 섹션으로 이동하여 **URL에서 추가** 필드에 다음 연결된 콘텐츠 구문을 붙여넣습니다.

{% raw %}
```
{% connected_content https://exp-platform-api-external.prod.awsotherlevels.com/v1/app/OTHERLEVELS_PROJECT_KEY/media/{{custom_attribute.${olxpmedia}}} %}
```
{% endraw %}

그런 다음 `OTHERLEVELS_PROJECT_KEY` 을 OtherLevels에서 제공한 프로젝트 키로 바꿉니다.

{: start="3"}
3\. **URL 파일 형식** 드롭다운에서 **MP4를** 선택합니다.
4\. 원하는 기본 설정에 따라 나머지 캠페인(예: 메시지 내용, 전송 일정, 타겟 오디언스)을 구성합니다.

![연결된 콘텐츠의 자산 필드 예시.]({% image_buster /assets/img/otherlevels/1.png %})

## GenAI 비디오 커스텀하기

### 동영상 크기 및 속성

동영상 배경은 `bg_image` 키 내에서 지정할 수 있습니다.

| 매개변수             | 설명                  |
|-------------------------|----------------------------|
| `url`    | 배경 이미지의 HTTPS URL입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

동영상 배경 크기는 `resize_image` 키 내에서 지정할 수 있습니다. 배경 이미지의 크기는 여기에서 구성한 것과 동일한 크기를 사용하는 것이 좋습니다.

| 매개변수             | 설명                  |
|-------------------------|----------------------------|
| `width`    | 배경 이미지의 너비(세로 및 가로 모드 모두에 대한 옵션 포함)입니다. |
| `height`     | 배경 이미지의 높이로, 세로 및 가로 모드 모두에 대한 옵션이 있습니다.                              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

동영상 오버레이 옵션은 `image_video_overlay` 키에서 지정할 수 있습니다.

| 매개변수             | 설명                  |
|-------------------------|----------------------------|
| `width`    | 오버레이의 너비(세로 및 가로 모드 모두에 대한 옵션 포함)입니다. |
| `height`         | 오버레이의 높이로, 세로 및 가로 모드 모두에 대한 옵션이 있습니다.                                              |
| `color`              | 투명도 동영상과 함께 RGB로 지정된 오버레이의 색상입니다.                                                                   |
| `y_pos`       | Y축이 중앙에서 오프셋됩니다.                                                              |
| `x_pos`    | X축이 중앙에서 오프셋됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### 재능 및 스크립트

프로비저닝의 일환으로 OtherLevels는 사용자와 협력하여 동영상에 사용할 하나 또는 여러 개의 재능(아바타라고도 함)을 생성합니다. 사용 사례와 브랜드에 따라 기존 브랜드 홍보대사 중 한 명을 활용하거나 고유한 창작물을 제작할 수 있습니다.

이렇게 생성된 후에는 API에서 사용할 수 있는 `TALENT_TEMPLATE` 및 `TALENT_MODEL` ID가 제공됩니다. 

입력 스크립트를 처리하는 데 사용되는 음성 모델은 사람이 읽을 수 있는 자연스러운 스크립트를 제공할 때 가장 잘 작동합니다. 대부분의 경우 스크립트를 수동으로 안내하기 위해 별도의 구두점이 필요하지 않습니다. 하지만 실제 오디언스에게 전송하기 전에 모든 스크립트를 테스트하는 것이 좋습니다. 탤런트가 스크립트를 읽는 속도는 `talking_talent_speed` 키 내에서 지정할 수 있습니다.

| 매개변수             | 설명                  |
|-------------------------|----------------------------|
| `speed`    | 재능이 스크립트를 읽는 속도를 지정합니다. For example, `1.5`.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Additional considerations

- iOS 푸시 알림 플랫폼만 기본적으로 동영상 미디어를 지원합니다. Android 푸시 알림은 기본적으로 동영상을 지원하지 않으므로 이 통합 기능은 iOS 오디언스에서만 사용할 수 있습니다.
- iOS 기기에서 동영상 푸시 알림을 수신할 때, 사용자가 푸시 알림을 길게 누르면 동영상이 로드되고 재생됩니다. 이는 iOS 플랫폼의 표준 동작이며 커스텀할 수 없습니다.