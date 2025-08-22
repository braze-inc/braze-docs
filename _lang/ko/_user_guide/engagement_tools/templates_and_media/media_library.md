---
nav_title: 미디어 라이브러리
article_title: 미디어 라이브러리
page_order: 0
page_type: reference
description: "이 참조 기사에서는 미디어 라이브러리에 대해 다룹니다. 여기에서 단일 중앙 집중식 위치에서 자산을 관리하고, AI를 사용하여 이미지를 생성하고, 메시지 작성기에서 미디어에 액세스하는 방법을 배울 수 있습니다."
tool: Media

---

# 미디어 라이브러리

> 미디어 라이브러리를 통해 자산을 단일 중앙 위치에서 관리할 수 있습니다. 

## Media library vs. CDN

Using the media library instead of a Content Delivery Network (CDN) provides better caching and performance for in-app messages. 모든 인앱 메시지에서 발견된 미디어 라이브러리 자산은 더 빠른 표시를 위해 미리 캐시되며 오프라인 표시를 위해 사용할 수 있습니다. 또한 미디어 라이브러리는 Braze 작성기와 통합되어 마케터가 이미지 URL을 복사하여 붙여넣는 대신 이미지를 선택하거나 태그할 수 있습니다.

## Accessing the media library

미디어 라이브러리에서 자산 유형, 크기, 치수, URL, 라이브러리에 추가된 날짜 및 기타 정보를 볼 수 있습니다. To access your Braze media library, go to THIS > **Templates**. Here, you can:

* 한 번에 여러 이미지를 업로드
* 가상 연락처 파일(.vcf) 업로드
* WhatsApp 메시지에 사용할 동영상 파일 업로드
* 이미지가 포함된 폴더를 업로드하세요(최대 50개 이미지)
* [AI를 사용하여 이미지를 생성](#generate-ai)하고 미디어 라이브러리에 저장
* 기존 이미지를 자르고 메시지에 맞는 비율을 만드세요
* 태그 또는 Teams를 추가하여 이미지를 더 잘 정리하세요
* 미디어 라이브러리 그리드에서 태그 또는 Teams로 검색
* 이미지나 폴더를 업로드하려면 드래그 앤 드롭하세요
* 이미지 삭제

![미디어 라이브러리 페이지에는 파일을 드래그 앤 드롭하거나 업로드할 수 있는 "라이브러리에 업로드" 섹션이 포함되어 있습니다. There is also a list of uploaded content in the media library.]({% image_buster /assets/img_archive/media_library_main.png %})

Later when drafting a message in Braze, you can pull in your images from the media library.

![메시지 작성기에 따라 미디어 라이브러리에 접근하는 두 가지 일반적인 방법. 하나는 제목이 "이미지 및 GIF"인 이메일 드래그 앤 드롭 편집기와 "미디어 라이브러리에서 추가" 버튼을 보여줍니다. The other shows the standard editors, such as push and in-app messages, with the title "Media" and a button to "Add Image".]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} 미디어 라이브러리에 대한 추가 도움말은 [템플릿 및 미디어 FAQ]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs)을(를) 확인하세요. {% endalert %}

## 이미지 사양

모든 이미지는 미디어 라이브러리에 업로드된 5MB 미만이어야 합니다. 지원되는 파일 형식은 PNG, JPEG, GIF 및 SVG입니다. 메시징 채널별 특정 이미지 추천은 다음 섹션을 참조하십시오.

### 콘텐츠 카드

{% multi_lang_include image_specs.md variable_name='content cards' %}

### 이메일

{% multi_lang_include image_specs.md variable_name="email"  %}

### 인앱 메시지

{% multi_lang_include image_specs.md variable_name="in-app messages"  %}

자세한 내용은 [인앱 메시지 크리에이티브 세부 정보]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/)를 참조하세요.

### 푸시

{% multi_lang_include image_specs.md variable_name="push notifications"  %}

{% alert note %}
For additional resources, see [Push image and text specifications]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
{% endalert %}

### 동영상

미디어 라이브러리에 업로드된 동영상은 현재 WhatsApp 메시지에서만 사용할 수 있습니다. 자세한 내용은 [Whatsapp 메시지 만들기를]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages) 참조하세요.

{% alert important %}
WhatsApp 메시지에 동영상 추가 기능은 현재 얼리 액세스 중입니다. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Generating images with BrazeAI<sup>TM</sup> {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
Before using this feature, review [how your data is used and sent to OpenAI]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy).
{% endalert %}
