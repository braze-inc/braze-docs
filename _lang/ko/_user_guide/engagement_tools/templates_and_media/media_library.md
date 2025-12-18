---
nav_title: 미디어 라이브러리
article_title: 미디어 라이브러리
page_order: 0
page_type: reference
description: "이 참고 문서에서는 미디어 라이브러리를 다룹니다. 여기에서 중앙 집중식 단일 위치에서 자산을 관리하고, AI를 사용하여 이미지를 생성하고, 메시지 작성기에서 미디어에 액세스하는 방법을 배울 수 있습니다."
tool: Media

---

# 미디어 라이브러리

> 미디어 라이브러리를 사용하면 중앙 집중식 단일 위치에서 자산을 관리할 수 있습니다. 

## 미디어 라이브러리 vs. CDN

CDN(콘텐츠 전송 네트워크) 대신 미디어 라이브러리를 사용하면 인앱 메시지의 캐싱 및 성능/성과가 향상됩니다. 인앱 메시지에 있는 모든 미디어 라이브러리 자산은 더 빠른 표시를 위해 미리 캐시되며 오프라인에서 표시할 수 있습니다. 또한 미디어 라이브러리는 Braze 컴포저와 통합되어 있어 마케터가 이미지 URL을 복사하여 붙여넣는 대신 이미지를 선택하거나 태그를 지정할 수 있습니다.

## 미디어 라이브러리 액세스하기

미디어 라이브러리에서 자산 유형, 크기, 크기, URL, 라이브러리에 추가된 날짜 및 기타 정보를 볼 수 있습니다. Braze 미디어 라이브러리에 액세스하려면 이쪽 > 템플릿으로 이동합니다. 여기에서 할 수 있습니다:

* 한 번에 여러 이미지 업로드
* 가상 연락처 파일(.vcf) 업로드
* WhatsApp 메시징에 사용할 동영상 파일 업로드하기
* 이미지가 있는 폴더 업로드(최대 50개 이미지)
* [AI를 사용하여 이미지를 생성하고](#generate-ai) 미디어 라이브러리에 저장합니다.
* 기존 이미지를 잘라 메시징에 적합한 비율로 만들기
* 태그 또는 팀을 추가하여 이미지를 더욱 체계적으로 정리하세요.
* 미디어 라이브러리 그리드에서 태그 또는 팀으로 검색하기
* 업로드할 이미지 또는 폴더를 드래그 앤 드롭합니다.
* 이미지 삭제

파일을 드래그 앤 드롭하거나 업로드할 수 있는 '라이브러리에 업로드' 섹션이 포함된 미디어 라이브러리 페이지입니다. 미디어 라이브러리에는 업로드된 콘텐츠 목록도 있습니다.]({% image_buster /assets/img_archive/media_library_main.png %})

나중에 Braze에서 메시지 초안을 작성할 때 미디어 라이브러리에서 이미지를 가져올 수 있습니다.

메시지 작성기에 따라 미디어 라이브러리에 액세스하는 두 가지 일반적인 방법이 있습니다. 하나는 "이미지 및 GIF"라는 제목과 함께 "미디어 라이브러리에서 추가" 버튼이 있는 이메일 드래그 앤 드롭 편집기를 보여줍니다. 다른 하나는 푸시 및 인앱 메시지와 같은 표준 편집기를 보여주며, '미디어'라는 제목과 '이미지 추가' 버튼이 있습니다.]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} 미디어 라이브러리에 대한 자세한 도움말은 [템플릿 & 미디어 FAQ를]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs) 참조하세요. {% endalert %}

## 이미지 사양

미디어 라이브러리에 업로드되는 모든 이미지는 5MB 미만이어야 합니다. 지원되는 파일 형식은 PNG, JPEG, GIF 및 SVG입니다. 메시징 채널별 구체적인 이미지 추천은 다음 섹션을 참조하세요.

### 콘텐츠 카드

{% multi_lang_include image_specs.md variable_name='content cards' %}

### 이메일

{% multi_lang_include image_specs.md variable_name="email"  %}

### 인앱 메시지

{% multi_lang_include image_specs.md variable_name="in-app messages"  %}

자세한 내용은 [인앱 메시지 크리에이티브 세부 정보를]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/) 참조하세요.

### 푸시

{% multi_lang_include image_specs.md variable_name="push notifications"  %}

{% alert note %}
추가 리소스는 [푸시 이미지 및 텍스트 사양을]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications) 참조하세요.
{% endalert %}

### 비디오

미디어 라이브러리에 업로드된 동영상은 현재 WhatsApp 메시지에서만 사용할 수 있습니다. 자세한 내용은 [Whatsapp 메시지 만들기를]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages) 참조하세요.

## <sup>BrazeAITM으로</sup> 이미지 생성 {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
이 기능을 사용하기 전에 [데이터가 어떻게 사용되고 OpenAI로 전송되는지]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy) 검토하세요.
{% endalert %}
