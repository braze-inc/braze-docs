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

**미디어 라이브러리**를 **템플릿**에서 찾을 수 있습니다.

**미디어 라이브러리**를 사용할 수 있습니다:

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

![미디어 라이브러리 페이지에는 파일을 드래그 앤 드롭하거나 업로드할 수 있는 "라이브러리에 업로드" 섹션이 포함되어 있습니다. 미디어 라이브러리에는 업로드된 콘텐츠 목록도 있습니다.][1]

{% alert tip %} 미디어 라이브러리에 대한 추가 도움말은 [템플릿 및 미디어 FAQ]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs)을(를) 확인하세요. {% endalert %}

## 이미지 세부 정보

미디어 라이브러리에서 자산 유형, 크기, 치수, URL, 라이브러리에 추가된 날짜 및 기타 정보를 볼 수 있습니다. 

### 미디어 라이브러리를 사용하는 것과 CDN을 사용하는 것

미디어 라이브러리를 사용하면 인앱 메시지에 대해 더 나은 캐싱 및 성능을 제공합니다. 모든 인앱 메시지에서 발견된 미디어 라이브러리 자산은 더 빠른 표시를 위해 미리 캐시되며 오프라인 표시를 위해 사용할 수 있습니다. 또한 미디어 라이브러리는 Braze 작성기와 통합되어 마케터가 이미지 URL을 복사하여 붙여넣는 대신 이미지를 선택하거나 태그할 수 있습니다.

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

##### 추가 자료

- [푸시 이미지 및 텍스트 사양]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)

### 동영상

미디어 라이브러리에 업로드된 동영상은 현재 WhatsApp 메시지에서만 사용할 수 있습니다. 자세한 내용은 [Whatsapp 메시지 만들기를]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages) 참조하세요.

{% alert important %}
WhatsApp 메시지에 동영상 추가 기능은 현재 얼리 액세스 중입니다. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## 메시지 작성기에서 미디어 라이브러리에 접근하기

미디어 라이브러리는 모든 이미지가 직접 업로드되는 대시보드의 중앙 위치로 작동합니다. 이렇게 하면 여러 메시지에서 이미지를 재사용할 수 있습니다.

![메시지 작성기에 따라 미디어 라이브러리에 접근하는 두 가지 일반적인 방법. 하나는 제목이 "이미지 및 GIF"인 이메일 드래그 앤 드롭 편집기와 "미디어 라이브러리에서 추가" 버튼을 보여줍니다. 다른 하나는 "미디어"라는 제목과 "이미지 추가" 버튼이 있는 푸시 및 인앱 메시지와 같은 표준 편집기를 보여줍니다.][1.5]{: style="border:none"}

## AI {#generate-ai}를 사용하여 이미지를 생성하세요

Braze 타사 제공업체인 OpenAI의 AI 시스템인 [DALL-E 3를](https://openai.com/index/dall-e-3/) 사용하여 미디어 라이브러리용 이미지를 생성할 수 있습니다. 이 시스템은 자연어로 된 설명에서 현실적인 이미지와 예술을 만들 수 있습니다. 각 요청은 프롬프트의 네 가지 배리언트를 생성하며, 회사는 하루에 10번 이미지를 생성할 수 있습니다. 이 총계는 귀하의 회사의 모든 사용자에게 적용됩니다.

1. 미디어 라이브러리에서 <i class="fas fa-wand-magic-sparkles"></i> **AI 이미지 생성기**를 선택합니다.
2. 생성하려는 이미지에 대한 설명을 300자 이내로 입력하세요. 설명이 자세할수록 결과가 더 좋습니다. 이 기능은 텍스트 입력만 지원하므로 참조용으로 이미지를 업로드할 수 없습니다.
3. **이미지 생성**을 선택하십시오. 이미지를 생성하는 데 약 1분이 걸릴 수 있습니다.
4. 선택 <i class="fas fa-download" title="미디어 라이브러리에 이미지 추가"></i> 를 선택하여 미디어 라이브러리에 추가하려는 이미지를 클릭합니다.

![모달 미디어 라이브러리의 AI 이미지 생성기.][6]{: style="max-width:75%"}

귀하와 Braze 사이에서 DALL-E 3를 사용하여 생성된 모든 이미지는 귀하의 지적 재산입니다. Braze는 그러한 이미지에 대해 어떠한 저작권의 권리를 주장하지 않으며, AI로 생성된 콘텐츠 또는 이미지에 대해 어떠한 유형의 보증도 하지 않습니다.

이미지를 생성하기 위해 Braze는 사용자의 쿼리를 OpenAI의 API 플랫폼으로 전송합니다. Braze에서 OpenAI로 전송되는 모든 쿼리는 익명으로 처리되므로, 사용자가 제공하는 입력에 고유 식별 정보를 포함하지 않는 한 OpenAI는 해당 쿼리가 누구로부터 전송되었는지 확인할 수 없습니다. [OpenAI의 API 플랫폼](https://openai.com/policies/api-data-usage-policies) 약관에 명시된 바와 같이, Braze를 통해 OpenAI의 API로 전송된 데이터는 모델을 학습하거나 개선하는 데 사용되지 않으며 30일 후에 삭제됩니다. OpenAI의 [사용 정책](https://openai.com/policies/usage-policies) 및 [공유 및 출판 정책](https://openai.com/policies/sharing-publication-policy)을 포함하여 관련 정책을 준수해야 합니다. Braze는 AI가 생성한 콘텐츠와 관련하여 어떠한 종류의 보증도 하지 않습니다. 


[1]: {% image_buster /assets/img_archive/media_library_main.png %}
[1.5]: {% image_buster /assets/img_archive/media_library_composers.png %}
[2]: {% image_buster /assets/img_archive/media_library_crop1.png %}
[3]: {% image_buster /assets/img_archive/media_library_crop2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/
[5]:https://imageoptim.com/mac
[6]: {% image_buster /assets/img_archive/media_library_dalle.png %}
