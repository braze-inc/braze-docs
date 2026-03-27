---
nav_title: 테스트 메시지 보내기
article_title: 테스트 메시지 보내기
page_order: 0
tool: 
  - Campaigns
page_type: reference
description: "이 참고 문서에서는 다양한 Braze 채널에서 테스트 메시지를 보내는 방법과 커스텀 이벤트 속성정보 또는 사용자 속성을 통합하는 방법에 대해 설명합니다."

---

# 테스트 메시지 보내기

> 사용자에게 메시징 캠페인을 보내기 전에 모범 사례로, 메시지가 제대로 표시되고 의도한 대로 작동하는지 테스트하는 것이 좋습니다. Braze 대시보드의 도구를 사용하여 테스트 메시지를 생성하고 선택한 기기 또는 팀원에게 보낼 수 있습니다.

{% alert important %}
캠페인이 삭제되지 않도록 테스트 후 캠페인 초안을 저장해야 합니다. 메시지를 초안으로 저장하지 않고도 테스트 메시지를 보낼 수 있습니다.
{% endalert %}

## 1단계: 테스트 사용자 식별

메시징 캠페인을 테스트하기 전에 테스트 사용자를 식별하는 것이 중요합니다. 이러한 사용자는 기존 사용자 ID 또는 이메일 주소이거나, 메시징 캠페인 테스트 전용으로 사용되는 새 사용자일 수 있습니다. 

### 선택 사항: 콘텐츠 테스트 그룹 만들기

테스트 사용자를 편리하게 구성하는 방법은 [콘텐츠 테스트 그룹]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/)을 만드는 것입니다. 이 그룹에는 캠페인에서 테스트 메시지를 수신할 사용자 그룹이 포함됩니다. 캠페인의 **테스트 수신자** 아래 **콘텐츠 테스트 그룹 추가** 필드에 이 테스트 그룹을 추가하면, 개별 테스트 사용자를 만들거나 추가하지 않고도 테스트를 시작할 수 있습니다.

## 2단계: 채널별 테스트 메시지 보내기

테스트 메시지를 보내는 단계는 각 채널의 다음 섹션을 참조하세요.

{% tabs local %}
{% tab Banners %}

{% alert important %}
Braze에서 배너 메시지를 테스트하려면 먼저 Braze에서 배너 캠페인을 만들어야 합니다. 또한, 테스트하려는 배치가 이미 [앱 또는 웹사이트에 배치되어 있는지]({{site.baseurl}}/developer_guide/banners/placements) 확인하세요.
{% endalert %}

배너 메시지를 만든 후 배너를 미리 보거나 테스트 메시지를 보낼 수 있습니다.

1. 배너 메시지 초안을 작성합니다.
2. **미리보기**를 선택하여 배너를 미리 보거나 테스트 메시지를 보냅니다.
3. 테스트 메시지를 보내려면 콘텐츠 테스트 그룹 또는 한 명 이상의 개별 사용자를 **테스트 수신자**로 추가한 다음 **테스트 보내기**를 선택합니다. 

기기에서 최대 5분 동안 테스트 메시지를 볼 수 있습니다.

![배너 작성기의 미리보기 탭입니다.]({% image_buster /assets/img/banners/preview_banner.png %})

{% alert note %}
하드웨어 차이로 인해 미리보기가 사용자 기기의 최종 렌더링과 동일하지 않을 수 있다는 점을 유념하세요.
{% endalert %}

### 테스트 체크리스트

- 배너 캠페인이 게재 위치에 할당되었나요?
- 이미지와 미디어가 타겟팅한 기기 유형과 화면 크기에서 예상대로 표시되고 작동하나요?
- 링크와 버튼이 사용자를 원하는 곳으로 안내하나요?
- Liquid가 예상대로 작동하나요? Liquid가 정보를 반환하지 않는 경우에 대비해 기본 속성 값을 설정했나요?
- 카피가 명확하고 간결하며 정확한가요?

{% endtab %}
{% tab Content Card %}

{% alert warning %}
[콘텐츠 테스트 그룹]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) 또는 개별 사용자에게 테스트를 보내려면, 테스트 전송 전에 테스트 기기에서 푸시가 활성화되어 있어야 하며 테스트 사용자에 대해 유효한 푸시 토큰이 등록되어 있어야 합니다. iOS 사용자는 테스트 콘텐츠 카드를 보기 위해 Braze에서 보낸 푸시 알림을 탭해야 합니다. 이 동작은 테스트 콘텐츠 카드에만 적용됩니다.
{% endalert %}

테스트 콘텐츠 카드는 푸시 알림을 통해 전달됩니다. 카드는 푸시 페이로드에 패키징되며, 푸시가 수신되면 SDK가 이를 추출하여 로컬에 캐시합니다.

이 프로세스는 일반적인 카드 전달 시스템을 우회하므로, 콘텐츠 카드를 테스트하더라도 푸시가 활성화되어 있어야 합니다.

테스트 콘텐츠 카드는 전송 후 약 5분이 지나면 만료됩니다.

콘텐츠 카드를 만든 후 테스트 콘텐츠 카드를 앱에 전송하여 실시간으로 어떻게 표시되는지 확인할 수 있습니다.

1. 콘텐츠 카드 초안을 작성합니다.
2. **테스트** 탭을 선택하고 이 테스트 메시지를 수신할 콘텐츠 테스트 그룹 또는 개별 사용자를 하나 이상 선택합니다. 
3. **테스트 보내기**를 선택하여 콘텐츠 카드를 앱으로 보냅니다.

![콘텐츠 카드 테스트]({% image_buster /assets/img/contentcard_test.png %})

### 미리보기

**미리보기** 탭에서 카드를 작성하면서 미리 볼 수 있습니다. 이를 통해 사용자의 관점에서 최종 메시지가 어떻게 보일지 시각화할 수 있습니다.

{% alert note %}
작성기의 **미리보기** 탭에서 메시지의 보기가 사용자 기기에서의 실제 렌더링과 동일하지 않을 수 있습니다. 미디어, 카피, 개인화, 커스텀 속성이 올바르게 생성되는지 확인하려면 항상 기기로 테스트 메시지를 보내는 것을 권장합니다.
{% endalert %}

### 테스트 체크리스트

- 테스트 사용자가 유효한 푸시 토큰으로 푸시에 옵트인되어 있나요?
- 이미지와 미디어가 예상대로 표시되고 작동하나요?
- Liquid가 예상대로 작동하나요? Liquid가 정보를 반환하지 않는 경우에 대비해 [기본 속성 값]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values)을 설정했나요?
- 카피가 명확하고 간결하며 정확한가요?
- 링크가 사용자를 올바른 곳으로 안내하나요?

### 디버그

콘텐츠 카드가 전송된 후 개발자 콘솔의 [이벤트 사용자 로그]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/)에서 문제를 분석하거나 디버그할 수 있습니다. 

일반적인 사용 사례는 사용자가 특정 콘텐츠 카드를 볼 수 없는 이유를 디버깅하는 것입니다. 이를 위해 세션 시작 시 SDK에 전달된 콘텐츠 카드를 **이벤트 사용자 로그**에서 확인하고, 노출 이전의 항목을 특정 캠페인으로 추적할 수 있습니다:

1. **설정** > **이벤트 사용자 로그**로 이동합니다.
2. 테스트 사용자에 대한 SDK 요청을 찾아 확장합니다.
3. **원시 데이터**를 클릭합니다.
4. 세션의 `id`를 찾습니다. 다음은 예시입니다:

    ```json
    [
      {
        "session_id": "D1B051E6-469B-47E2-B830-5A728D1D4AC5",
        "data": {
          "ids": [
            "NDg2MTY5MmUtNmZjZS00MjE1LWJkMDUtMzI1NGZiOWU5MDU3"
          ]
        },
        "name": "cci",
        "time": 1636106490.155
      }
    ]
    ```
    
{: start="5"}
5. [Base64 Decode and Encode](https://www.base64decode.org/)와 같은 디코딩 도구를 사용하여 `id`를 Base64 형식에서 디코딩하고 관련된 `campaign_id`를 찾습니다. 이 예에서는 다음과 같은 결과가 나옵니다:

    ```
    4861692e-6fce-4215-bd05-3254fb9e9057_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    여기서 `4861692e-6fce-4215-bd05-3254fb9e9057`이 `campaign_id`입니다.<br><br>

6. **캠페인** 페이지로 이동하여 `campaign_id`를 검색합니다.

![캠페인 페이지에서 campaign_id 검색하기]({% image_buster /assets/img_archive/cc_debug.png %}){: style="max-width:80%;"}

여기에서 메시지 설정 및 콘텐츠를 검토하여 사용자가 특정 콘텐츠 카드를 볼 수 없는 이유를 파악할 수 있습니다.

{% endtab %}
{% tab Email %}

1. 이메일 메시지 초안을 작성합니다.
2. **미리보기 및 테스트**를 선택합니다.
3. **테스트 보내기** 탭을 선택하고 **개별 사용자 추가** 필드에 이메일 주소 또는 사용자 ID를 추가합니다. 
4. **테스트 보내기**를 선택하여 초안 이메일을 받은편지함으로 보냅니다.

![테스트 이메일]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

{% endtab %}
{% tab In-app message %}

{% alert warning %}
[콘텐츠 테스트 그룹]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) 또는 개별 사용자에게 테스트를 보내려면 보내기 전에 테스트 기기에서 푸시가 활성화되어 있어야 합니다. 예를 들어 테스트 메시지가 표시되기 전에 알림을 탭하려면 iOS 기기에서 푸시 알림이 활성화되어 있어야 합니다. {% endalert %}

앱과 테스트 기기에 푸시 알림을 설정한 경우 앱에 테스트 인앱 메시지를 전송하여 실시간으로 어떻게 보이는지 확인할 수 있습니다. 

1. 인앱 메시지 초안을 작성합니다.
2. **테스트** 탭을 선택하고 **개별 사용자 추가** 필드에 이메일 주소 또는 사용자 ID를 추가합니다. 
3. **테스트 보내기**를 선택하여 푸시 메시지를 기기에 보냅니다.

기기 화면 상단에 테스트 푸시 메시지가 표시됩니다.

![인앱 테스트]({% image_buster /assets/img_archive/test-in-app.png %})

{% alert important %}
테스트 전송 시 각 수신자에게 두 개 이상의 인앱 메시지가 전송될 수 있습니다. 
{% endalert %}

푸시 메시지를 직접 클릭하여 열면 앱으로 이동하여 인앱 메시지 테스트를 확인할 수 있습니다. 이 인앱 메시지 테스트 기능은 사용자가 테스트 푸시 알림을 클릭하여 인앱 메시지를 트리거하는 방식에 의존합니다. 따라서 테스트 푸시 알림이 성공적으로 전달되려면 사용자가 해당 앱에서 푸시 알림을 수신할 수 있는 자격이 있어야 합니다.

### 미리보기

**미리보기** 탭에서 인앱 메시지를 작성하면서 미리 볼 수 있습니다. 이를 통해 사용자의 관점에서 최종 메시지가 어떻게 보일지 시각화할 수 있습니다. 무작위 사용자, 특정 사용자 또는 커스텀 사용자에게 메시지가 어떻게 보일지 미리 볼 수 있습니다. 모바일 기기 또는 태블릿용 메시지도 미리 볼 수 있습니다.

![인앱 메시지를 작성할 때 작성 탭에서 메시지가 어떻게 표시될지 미리 볼 수 있습니다. 사용자가 선택되지 않았으므로 본문 섹션에 추가된 Liquid가 그대로 표시됩니다.]({% image_buster /assets/img/in-app-message-preview.png %})

Braze는 3세대 인앱 메시지를 제공합니다. 지원하는 세대에 따라 메시지를 전송할 기기를 세밀하게 조정할 수 있습니다.

![인앱 메시지를 미리 볼 때 세대 간 전환.]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

{% alert warning %}
**미리보기**에서 메시지의 보기가 사용자 기기에서의 실제 렌더링과 동일하지 않을 수 있습니다. 미디어, 카피, 개인화 및 커스텀 속성이 올바르게 생성되는지 확인하려면 항상 기기에 테스트 메시지를 보내는 것을 권장합니다.
{% endalert %}

### 테스트 체크리스트

- 이미지와 미디어가 예상대로 표시되고 작동하나요?
- Liquid가 예상대로 작동하나요? Liquid가 정보를 반환하지 않는 경우에 대비해 [기본 속성 값]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values)을 설정했나요?
- 카피가 명확하고 간결하며 정확한가요?
- 버튼이 사용자를 올바른 곳으로 안내하나요?

### 접근성 스캐너

접근성 모범 사례를 지원하기 위해 Braze는 기존 HTML 편집기를 사용하여 만든 인앱 메시지의 콘텐츠를 접근성 표준에 따라 자동으로 스캔합니다. 이 스캐너는 웹 콘텐츠 접근성 지침([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)) 표준을 충족하지 못할 수 있는 콘텐츠를 식별하는 데 도움이 됩니다. WCAG는 장애가 있는 사람들이 웹 콘텐츠에 더 쉽게 접근할 수 있도록 월드 와이드 웹 컨소시엄(W3C)이 개발한 국제적으로 인정된 기술 표준 세트입니다.

![접근성 검사 결과]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

{% alert note %}
인앱 메시지 접근성 스캐너는 커스텀 HTML로 작성된 메시지에서만 실행됩니다. 
{% endalert %}

#### 작동 방식

스캐너는 커스텀 HTML 메시지에서 자동으로 실행되며 전체 HTML 메시지를 [WCAG 2.1 AA 규칙 세트](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa) 전체에 대해 평가합니다. 플래그가 지정된 각 문제에 대해 다음을 표시합니다:

- 관련된 특정 HTML 요소
- 접근성 문제에 대한 설명
- 추가 컨텍스트 또는 수정 지침에 대한 링크

#### 자동화된 접근성 테스트 이해

{% multi_lang_include accessibility/automated_testing.md %}

{% endtab %}
{% tab LINE %}

1. LINE 메시지를 작성합니다.
2. **테스트** 탭을 선택하고 이 테스트 메시지를 수신할 콘텐츠 테스트 그룹 또는 개별 사용자를 하나 이상 선택합니다.
3. **테스트 보내기**를 선택하여 메시지를 보냅니다.

![LINE 메시지 테스트.]({% image_buster /assets/img/line/test_preview.png %})

{% endtab %}
{% tab Push %}

#### 모바일 푸시

1. 모바일 푸시 초안을 작성합니다.
2. **테스트** 탭을 선택하고 **개별 사용자 추가** 필드에 이메일 주소 또는 사용자 ID를 추가합니다.
3. **테스트 보내기**를 선택하여 초안 메시지를 기기로 전송합니다.

![푸시 테스트]({% image_buster /assets/img_archive/testpush.png %})

#### 웹 푸시

1. 웹 푸시를 만듭니다.
2. **테스트** 탭을 선택합니다. 
3. **나에게 테스트 보내기**를 선택합니다.
4. **테스트 보내기**를 선택하여 웹 푸시를 웹 브라우저로 보냅니다.

![웹 푸시 테스트]({% image_buster /assets/img_archive/testwebpush.png %})

Braze 대시보드에서 이미 푸시 메시지를 수락한 경우, 화면 모서리에 푸시가 표시됩니다. 그렇지 않으면 프롬프트가 표시될 때 **허용**을 클릭하면 메시지가 나타납니다.

{% endtab %}
{% tab SMS/MMS and RCS %}

SMS, MMS 또는 RCS 메시지를 작성한 후 테스트 메시지를 휴대폰으로 전송하여 실시간으로 어떻게 보이는지 확인할 수 있습니다. 

1. SMS, MMS 또는 RCS 메시지 초안을 작성합니다.
2. **테스트** 탭을 선택하고 이 테스트 메시지를 수신할 콘텐츠 테스트 그룹 또는 개별 사용자를 하나 이상 선택합니다. 
3. **테스트 보내기**를 선택하여 테스트 메시지를 보냅니다.

![SMS/MMS 테스트]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

웹훅을 만든 후 테스트 전송을 수행하여 웹훅 응답을 확인할 수 있습니다. **테스트** 탭을 선택하고 **테스트 보내기**를 선택하여 제공된 웹훅 URL로 테스트 전송을 보냅니다. 개별 사용자를 선택하여 특정 사용자로서의 응답을 미리 볼 수도 있습니다. 

![웹훅 테스트]({% image_buster /assets/img/webhook_test.png %})

{% endtab %}
{% tab WhatsApp %}

1. WhatsApp 메시지를 작성합니다.
2. **테스트** 탭을 선택하고 이 테스트 메시지를 수신할 콘텐츠 테스트 그룹 또는 개별 사용자를 하나 이상 선택합니다.
3. 이 메시지에 사용 중인 구독 그룹과 연결된 전화번호로 WhatsApp 메시지를 보내 대화 창을 시작합니다. 연관된 전화번호는 **테스트** 탭의 알림에 나열되어 있습니다.
4. **테스트 보내기**를 선택하여 메시지를 보냅니다.

![WhatsApp 메시지 테스트.]({% image_buster /assets/img/whatsapp/whatsapp_test.png %})

{% endtab %}
{% endtabs %}

## 개인화된 캠페인 테스트 

사용자 데이터를 채우거나 커스텀 이벤트 속성정보를 사용하는 캠페인을 테스트하는 경우 추가적이거나 다른 단계를 수행해야 합니다.

### 사용자 속성으로 개인화된 캠페인 테스트

메시지에서 [개인화]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/)를 사용하는 경우, 캠페인을 제대로 미리 보고 사용자 데이터가 콘텐츠를 올바르게 채우고 있는지 확인하기 위해 추가 단계를 수행해야 합니다.

테스트 메시지를 보낼 때 **기존 사용자 선택** 또는 **커스텀 사용자**로 미리 보기 옵션 중 하나를 선택해야 합니다.

![개인화된 메시지 테스트]({% image_buster /assets/img_archive/personalized_testing.png %}){: style="max-width:70%;" }

#### 기존 사용자 선택하기

기존 사용자를 선택하는 경우 검색 필드에 특정 사용자 ID 또는 이메일을 입력합니다. 그런 다음 대시보드 미리보기를 사용하여 해당 사용자에게 메시지가 어떻게 표시되는지 확인하고, 해당 사용자가 보게 될 내용을 반영한 테스트 메시지를 기기로 보냅니다.

![사용자 선택]({% image_buster /assets/img_archive/personalized_testing_select.png %})

#### 커스텀 사용자 선택하기

커스텀 사용자로 미리 보는 경우 사용자의 이름 및 커스텀 속성 등 개인화에 사용할 수 있는 다양한 필드에 텍스트를 입력합니다. 마찬가지로 자신의 이메일 주소를 입력하여 기기로 테스트를 보낼 수 있습니다.

![커스텀 사용자]({% image_buster /assets/img_archive/personalized_testing_custom.png %})

#### 기존 사용자 커스터마이징

무작위 또는 기존 사용자의 개별 필드를 편집하여 메시지 내의 동적 콘텐츠를 테스트할 수 있습니다. **편집**을 선택하면 선택한 사용자가 수정 가능한 커스텀 사용자로 전환됩니다.

!['사용자로 미리보기' 탭에 '편집' 버튼이 있습니다.]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### 커스텀 이벤트 속성정보로 개인화된 캠페인 테스트

[커스텀 이벤트 속성정보]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties)로 개인화된 캠페인을 테스트하는 것은 앞서 설명한 다른 유형의 캠페인 테스트와 약간 다릅니다. 

{% tabs local %}
{% tab Trigger manually %}

#### 방법 1: 수동으로 캠페인 트리거하기

커스텀 이벤트 속성정보를 사용하여 개인화된 캠페인을 테스트하는 강력한 방법으로 캠페인을 직접 트리거할 수 있습니다:

1. 이벤트 속성정보가 포함된 카피를 작성합니다. 

![속성정보를 사용하여 테스트 메시지 작성]({% image_buster /assets/img_archive/testeventproperties-compose.png %})

{: start="2"}
2. 이벤트 발생 시 [실행 기반 전달]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)을 사용하여 캠페인을 전달합니다.

{% alert note %}
iOS 푸시 캠페인을 테스트하는 경우, iOS는 현재 열려 있는 앱에 대한 푸시 알림을 전달하지 않으므로 앱을 종료할 시간을 확보하기 위해 지연 시간을 1분으로 설정해야 합니다. 다른 유형의 캠페인은 즉시 전달되도록 설정할 수 있습니다.
{% endalert %}

![메시지 전달 테스트]({% image_buster /assets/img_archive/testeventproperties-delivery.png %})

{: start="3"}
3. 테스트 필터를 사용하거나 자신의 이메일 주소를 타겟팅하여 사용자를 타겟팅하고 캠페인 생성을 완료합니다. 

![메시지 타겟팅 테스트]({% image_buster /assets/img_archive/testeventproperties-target.png %})

{: start="4"}
4. 앱으로 이동하여 커스텀 이벤트를 수행합니다.

캠페인이 트리거되고 이벤트 속성정보로 맞춤 설정된 메시지가 표시됩니다.

![테스트 메시지 예제]({% image_buster /assets/img_archive/testeventproperties-message2.png %})

{% endtab %}
{% tab Test message %}

#### 방법 2: 자신에게 테스트 메시지 보내기

또는 커스텀 사용자 ID를 저장하는 경우 자신에게 커스텀 테스트 메시지를 전송하여 캠페인을 테스트할 수도 있습니다.

1. 캠페인에 사용할 카피를 작성합니다.
2. **테스트** 탭을 선택하고 **커스텀 사용자**를 선택합니다. 
3. 페이지 하단에 커스텀 이벤트 속성정보를 추가하고 상단 상자에 사용자 ID 또는 이메일 주소를 추가합니다.
4. **테스트 보내기**를 선택하면 속성정보로 개인화된 메시지를 받을 수 있습니다.

![커스텀 사용자를 사용한 테스트]({% image_buster /assets/img_archive/testeventproperties-customuser.png %})

{% endtab %}
{% tab Liquid %}

#### 방법 3: Liquid 사용

Liquid를 사용하여 값을 수동으로 입력하면 커스텀 이벤트 속성정보를 테스트할 수 있습니다. 

1. 메시지 편집기에서 커스텀 이벤트 속성정보에 대한 값을 입력합니다.
2. **사용자로 미리보기** 탭을 선택하여 올바른 메시지가 표시되는지 확인합니다.

{% endtab %}
{% endtabs %}

## 문제 해결

### 인앱 메시지

인앱 메시지 캠페인이 푸시 캠페인에 의해 트리거되지 않는 경우, 인앱 캠페인 세분화를 확인하여 사용자가 푸시 메시지를 받기 **전에** 타겟 오디언스를 충족하는지 확인하세요.

Android 및 iOS에서 테스트 전송 시, **푸시 권한 요청** 온클릭 동작을 사용하는 인앱 메시지가 일부 기기에서 표시되지 않을 수 있습니다. 해결 방법:
- **Android:** 기기가 Android 13 이상이고 Android SDK 버전 21.0.0 이상이어야 합니다. 또 다른 이유는 인앱 메시지가 표시되는 기기에 이미 시스템 수준의 프롬프트가 있기 때문일 수 있습니다. **다시 묻지 않음**을 선택했을 수 있으므로, 다시 테스트하기 전에 앱을 다시 설치하여 알림 권한을 재설정해야 할 수 있습니다.
- **iOS:** 개발자 팀에서 앱의 푸시 알림 구현을 검토하고 푸시 권한을 요청하는 코드를 수동으로 제거할 것을 권장합니다. 자세한 내용은 [푸시 프라이머 인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)를 참조하세요.

실행 기반 인앱 메시지 캠페인을 전달하려면 REST API가 아닌 Braze SDK를 통해 커스텀 이벤트를 로깅해야 사용자가 적격 인앱 메시지를 기기로 직접 수신할 수 있습니다. 사용자는 세션 중에 이벤트를 수행하면 인앱 메시지를 받게 됩니다.