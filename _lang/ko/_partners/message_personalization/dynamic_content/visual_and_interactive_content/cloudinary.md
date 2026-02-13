---
nav_title: Cloudinary
article_title: Cloudinary
description: "이 참고 문서에서는 Braze와 Cloudinary의 파트너십에 대해 간략하게 설명합니다."
alias: /partners/cloudinary/
page_type: partner
search_tag: Partner
---

# Cloudinary

> [클라우디너리는](https://www.cloudinary.com?utm_source=braze_partner_page) 채널과 고객 여정에 걸쳐 모든 캠페인에 이미지와 비디오를 대규모로 관리, 편집, 최적화 및 전달하는 데 사용되는 이미지 및 비디오 플랫폼입니다. Cloudinary의 미디어 매니저를 통합하고 인에이블먼트하면 Braze 캠페인과 캔버스에 동적, 상황별, 개인화된 자산을 전달할 수 있습니다. 

## 이 통합 정보

Cloudinary를 Braze에 연결하면 브랜드는 Cloudinary 자산에 저장된 시각적 미디어에 액세스하여 Braze 메시징 채널에서 사용할 수 있습니다. Cloudinary의 다이내믹 링크를 사용하면 Braze 사용자 속성에 따라 이미지와 동영상을 실시간으로 선택하고 커스텀할 수 있습니다. Cloudinary와 Braze는 함께 각 제품의 스토리를 전달하고 특별한 경험을 대규모로 제공하는 시각적으로 풍부하고 개인화된 캠페인을 제작할 수 있도록 지원합니다.

이 페이지에서는 Cloudinary와 Braze 간의 가능한 네 가지 통합 방법을 간략하게 설명합니다. 이러한 통합 방법은 주로 Cloudinary의 미디어 라이브러리에서 수동으로 복사한 자산 링크를 수정하는 데 의존합니다. 

{% alert important %}
[연결된 콘텐츠를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) 사용하여 Cloudinary의 [관리자 API를](https://cloudinary.com/documentation/admin_api#banner) 호출하는 등 보다 진행된 통합 방법도 가능하지만, 접근 방식은 고객마다 다를 수 있습니다. Cloudinary 및 Braze 고객 성공 매니저에게 문의하여 안내를 받으세요.
{% endalert %}

## Prerequisites

| Requirements     | 설명 |                        
|-----------------------|-----------------|
| Cloudinary 계정  | 이 파트너십을 이용하려면 [Cloudinary 계정이](https://cloudinary.com/users/register_free?utm_source=braze+docs+page) 필요합니다.  |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## 통합 방법

{% alert tip %}
이러한 통합 방법 중 일부는 [이미지](https://cloudinary.com/documentation/image_transformations#banner) 및 [동영상](https://cloudinary.com/documentation/video_manipulation_and_delivery#banner) 자산의 동작과 모양을 보다 심층적으로 커스텀할 수 있는 `f_auto` 및 `q_auto` 클라우디너리 트랜스포메이션을 사용합니다. 트랜스포메이션을 포함하도록 Cloudinary 자산 링크를 수정하는 방법에 대한 자세한 내용은 트랜스포메이션 [URL 구조를](https://cloudinary.com/documentation/image_transformations#transformation_url_structure) 참조하세요.
{% endalert %}

{% tabs %}
{% tab Cloudinary DAM %}

## 클라우디너리 DAM을 통한 캠페인 자산 선택

Braze 캠페인과 캔버스에서 Cloudinary의 DAM에 있는 이미지와 동영상을 직접 사용하는 가장 직접적인 방법은 Cloudinary 미디어 라이브러리의 자산 **페이지에서** URL을 가져오는 것입니다.

![이미지 중 하나의 오른쪽 상단에 강조 표시된 'URL 복사' 도구 설명이 표시된 Cloudinary의 이미지 자산 라이브러리 그리드 보기입니다.]({% image_buster /assets/img/cloudinary/one.png %})

### 이미지 및 GIF 설정

1. **자산** > **미디어 라이브러리** > **자산** > **URL 복사로** 이동하여 Cloudinary의 DAM에서 이미지 또는 GIF URL을 복사합니다.
2. HTML로 이미지 태그를 만든 다음 복사한 URL에 `f_auto,q_auto` 을 추가하여 이미지 또는 GIF를 최적화합니다.

#### 이미지 URL 예시

{% raw %}
```bash
<img src="https://res.cloudinary.com/demo/image/upload/v1678993440/f_auto,q_auto/cld-sample.jpg" alt="Summer Campaign">
</img>
```
{% endraw %}

### 동영상 설정

1. **자산** > **미디어 라이브러리** > **자산** > **URL 복사로** 이동하여 Cloudinary의 DAM에서 이미지 또는 GIF 링크를 복사합니다.
2. HTML로 동영상 태그를 만든 다음 복사한 URL에 `f_auto,q_auto` 을 추가하면 동영상의 형식과 품질이 자동으로 최적화됩니다.

#### 동영상 URL 예시

{% raw %}
```bash
<video class="video" autoplay muted playsinline controls>
  <source src="https://res.cloudinary.com/demo/video/upload/v1651840278/f_auto,q_auto/samples/cld-sample-video.mp4">
</video>
```
{% endraw %}

구체적인 Android 및 iOS 고려 사항은 [동영상을]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/video/) 참조하세요. 

{% endtab %}
{% tab Convert videoes into GIFs %}

## 이메일을 위해 동영상을 GIF로 변환하기

`f_auto:animated` [Cloudinary 변환을](https://cloudinary.com/documentation/image_transformations/) 사용하여 동영상 자산을 GIF로 자동 변환할 수 있습니다. GIF는 이메일 페이로드를 줄이기 위해 최적화되어 있으며, 너무 많으면 전달 가능성 문제를 일으킬 수 있으므로 Braze 이메일 채널을 사용하는 경우 특히 유용합니다. 

### 전환 설정

1. Cloudinary DAM에서 동영상 URL을 복사합니다.
2. 이미지 태그를 생성하고 `f_auto:animated,fl_lossy` 을 추가하여 GIF 크기를 줄이고 클라이언트에 가장 적합한 애니메이션 형식을 선택합니다.
3. 이메일 레이아웃에서 원하는 GIF 너비에 해당하는 `c_scale,w_nnn` 을 추가합니다.
4. `e_loop` 를 추가하여 애니메이션을 반복합니다.

#### GIF URL 예시

{% raw %}
```
https://res.cloudinary.com/demo/video/upload/c_scale,w_500,e_loop/f_auto:animated,fl_lossy/samples/cld-sample-video.gif
```
{% endraw %}

{% endtab %}
{% tab Target attributes %}

## 타겟팅 속성에 따라 캠페인 자산을 동적으로 선택합니다.

이 통합 방식은 사용자 속성에 따라 실시간으로 각 사용자에게 가장 적합한 자산을 지능적으로 선택함으로써 동적인 미디어 개인화를 가능하게 합니다. 

메시징 캠페인 메시지 내 Cloudinary 링크의 파라미터로 Liquid 태그를 포함하면 메시지가 전송될 때 연결된 Braze 속성이 동적으로 Liquid 태그를 대체합니다. 이는 언어 또는 고객 계층과 같은 사용자별 데이터일 수 있습니다. 그런 다음 Cloudinary는 이러한 속성을 사용하여 해당 사용자에게 가장 적합한 캠페인 자산을 결정하고 올바른 이미지 또는 동영상을 자동으로 반환합니다. 따라서 수신자는 상황별 관련성이 있고 브랜드가 승인한 자산만 수신할 수 있습니다.

### 작동 방식

Cloudinary는 [태그와](https://cloudinary.com/documentation/assets_onboarding_metadata_tags_tutorial#tags) [구조화된 메타데이터(SMD)를](https://cloudinary.com/documentation/assets_onboarding_metadata_tags_tutorial#structured_metadata) 사용하여 캠페인 자산을 정리하여 검색할 수 있도록 합니다. 

각 캠페인 자산은 캠페인 태그(예: `spring_launch`)로 그룹화되고 `language=en` 또는 `tier=gold` 과 같은 Braze 속성에 해당하는 구조화된 메타데이터 필드로 보강됩니다. Braze가 Cloudinary 링크를 호출하면 [커스텀 함수가](https://cloudinary.com/documentation/custom_functions#javascript_filters) 들어오는 속성을 처리하고 태그와 메타데이터가 일치하는 자산을 검색한 다음 가장 적합한 일치 항목을 반환합니다. 

정확히 일치하는 항목을 찾을 수 없는 경우 모든 경험의 연속성을 위해 대체 또는 '차선책' 옵션을 자동으로 선택합니다. 자산을 선택하면 Cloudinary의 변환 레이어(예: `f_auto` 또는 `q_auto`)가 전달할 미디어를 최적화합니다. 태그, 메타데이터, 커스텀 기능의 조합을 통해 개발자는 API 기반의 유연한 방식으로 개인화된 자산 전달을 자동화할 수 있습니다.

{% alert tip %}
커스텀 함수 생성 및 적용에 대한 지침과 특정 캠페인의 자산 선택 및 대체 옵션에 대한 커스텀 함수 예시는 Cloudinary의 [`braze-personalization` GitHub 리포지토리를](https://github.com/cloudinary-devs/braze-personalization) 참조하세요. 자세한 안내는 Cloudinary 지원팀에 문의하세요.
{% endalert %}

### 필수 조건

동적 자산 선택을 인에이블먼트하려면 Cloudinary가 태그와 메타데이터를 기반으로 자산 집합을 반환할 수 있어야 합니다. 목록 전달 유형이 제한되어 있는 경우, Cloudinary는 Braze 캠페인에서 개인화된 자산 선택에 필요한 동적 목록을 제공할 수 없습니다.
- 목록 전달 유형을 제한 해제합니다: Cloudinary 콘솔에서 보안 설정을 열고 제한된 이미지 유형 아래의 리소스 목록 항목을 선택 취소합니다.

### 동적 선택 설정

1. Cloudinary에서 자산에 대한 태그와 메타데이터를 설정합니다.
2. Cloudinary DAM에 커스텀 함수를 업로드하세요.
3. 원하는 태그의 Cloudinary URL을 만듭니다.
4. 태그 URL을 기본으로 사용하여 동적 이미지 Liquid 태그를 추가하여 Braze 속성과 커스텀 기능을 통합합니다.

#### URL 예시

이 예제에서는 Cloudinary의 자산에 Braze 속성에 해당하는 예상 값으로 채워진 두 개의 정의된 SMD 필드("로케일" 및 "오디언스")가 있다고 가정합니다. 또한 캠페인에 필요한 자산에 '샘플' 태그를 부여하고, 커스텀 기능( `segmentedBanner.js` )을 클라우디너 계정에 업로드했습니다. 

{% raw %}
```bash

// Use the appropriate Braze attributes.
{% assign audience = {{custom_attribute.${sample_audience_identifier}}} %} 
{% assign locale = {{${language}}}%} 

// The URL for the "samples" tag used in the campaign is https://papish.cloudinary.us/image/list/v1690000000/samples.json, which is the base for the dynamic image URL.
<img src="https://papish.cloudinary.us/image/list/f_auto,q_auto/$locale_#{locale}/$audience_!{audience}!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/campaigns/samples.json" alt="Banner"> 
```
{% endraw %}

##### 출력 URL

- 오디언스 `internal` 및 로캘 `en` 을 가진 사용자를 위한 출력 URL: 
```
https://papish.cloudinary.us/image/list/f_auto,q_auto/$locale_!en!/$audience_!Internal!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```
- 오디언스 `external` 및 로캘 `es` 을 가진 사용자를 위한 출력 URL: 
```
https://papish.cloudinary.us/image/list/$locale_!es!/$audience_!External!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```
- 대체 이미지 URL입니다: 
```
https://papish.cloudinary.us/image/list/$locale_!unknown!/$audience_!unknown!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```

{% endtab %}
{% tab Personalized image generation %}

## 개인화된 이미지 생성

Cloudinary의 [텍스트 오버레이 변환은](https://cloudinary.com/documentation/accessible_media_visual_audio_clarity#text_overlays_on_images_and_videos/) Cloudinary 자산 내에서 직접 Braze의 사용자 데이터를 사용합니다. 

다음 예는 `l_text` 변환을 사용하여 자산에 사용자 이름을 삽입하는 방법을 보여줍니다. 캠페인과 캔버스를 개발할 때 Liquid 태그를 활용하여 `l_text` 매개변수를 채울 텍스트를 결정하면 더욱 커스텀화할 수 있습니다.

변환 매개변수를 사용하여 자산을 디자인하는 방법에 대한 자세한 안내는 Cloudinary 지원팀에 문의하세요.

### 예 `l_text` 변환

{% raw %}
```bash
{% assign first_name = {{${first_name}}}%} 
{% assign second_name = {{${last_name}}}%} 

<img src="https://res.cloudinary.com/demo/image/upload/l_text:Arial_300:%20{{first_name}}%20{{second_name}}%20,co_white,b_rgb:00000080/fl_layer_apply,g_north_west,y_200/docs/white-church-europe-sea.jpg">
```
{% endraw %}

#### 출력 URL 예시

{% raw %}
```bash
<img src="https://res.cloudinary.com/demo/image/upload/l_text:Arial_300:%20John%20Smith%20,co_white,b_rgb:00000080/fl_layer_apply,g_north_west,y_200/docs/white-church-europe-sea.jpg">
```
{% endraw %}

![바다가 내려다보이는 푸른 지붕의 흰색 교회, 이미지 왼쪽 상단에는 "존 스미스"라는 글자가 오페이지의 어두운 큰 직사각형에 새겨져 있습니다.]({% image_buster /assets/img/cloudinary/two.png %})

```
{% endtab %}
{% endtabs %}
