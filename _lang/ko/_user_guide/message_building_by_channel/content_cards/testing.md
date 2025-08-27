---
nav_title: 테스팅
article_title: 콘텐츠 카드 테스팅
page_order: 3
description: "이 참조 문서는 콘텐츠 카드를 미리 보고 테스트하는 방법과 몇 가지 모범 사례를 다룹니다."
channel:
  - content cards
  
---

# 콘텐츠 카드 테스팅

> 캠페인을 보내기 전에 항상 콘텐츠 카드를 테스트하는 것이 매우 중요합니다. 미리보기 및 테스트 기능을 통해 콘텐츠 카드를 확인할 수 있는 두 가지 방법을 제공합니다. 메시지를 작성하는 동안 시각화하는 데 도움이 되도록 메시지를 미리 볼 수 있으며, 테스트 메시지를 자신이나 특정 사용자의 기기로 보낼 수도 있습니다. Braze 둘 다 활용할 것을 권장합니다.

## 미리보기

카드를 작성하는 동안 미리 볼 수 있습니다. 이것은 사용자의 관점에서 최종 메시지가 어떻게 보일지 시각화하는 데 도움이 될 것입니다.

작성기의 **미리보기** 탭에서 메시지의 보기가 사용자의 기기에서 실제 렌더링과 동일하지 않을 수 있습니다. 항상 기기에게 테스트 메시지를 보내서 미디어, 카피, 개인화, 커스텀 속성이 올바르게 생성되는지 확인하는 것을 권장합니다.

## 테스트

테스트를 [콘텐츠 테스트 그룹]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) 또는 개별 사용자에게 보내려면, 푸시가 테스트 사용자에 대해 유효한 푸시 토큰이 등록된 테스트 기기에서 활성화되어 있어야 합니다. iOS 사용자는 테스트 콘텐츠 카드를 보기 위해 Braze에서 보낸 푸시 알림을 탭해야 합니다. 이 동작은 테스트 콘텐츠 카드에만 적용됩니다.

### 사용자로서 메시지 미리보기

사용자인 것처럼 **테스트** 탭에서 메시지를 미리 볼 수도 있습니다. 특정 사용자, 무작위 사용자 또는 커스텀 사용자를 선택할 수 있습니다.

!['테스트' 탭의 콘텐츠 카드 미리 보기]({% image_buster /assets/img/cc-user-preview.png %}){: style="max-width:80%;"}

### 테스트 체크리스트

- 이미지와 미디어가 예상대로 표시되고 작동하나요?
- Liquid가 예상대로 작동하나요? 리퀴드가 정보를 반환하지 않는 경우의 [기본 속성 값을]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) 고려했나요?
- 귀하의 카피가 명확하고 간결하며 정확합니까?
- 당신의 링크가 사용자를 가야 할 곳으로 안내합니까?

## 디버그

After your Content Cards are sent, you can break down or debug any issues from the [Event User Log]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) in the Developer Console. 

일반적인 사용 사례는 사용자가 특정 콘텐츠 카드를 볼 수 없는 이유를 디버깅하려고 시도하는 것입니다. 이를 위해 세션 시작 시 SDK에 전달된 콘텐츠 카드를 **이벤트 사용자 로그**에서 확인하고 노출 횟수 이전에 특정 캠페인으로 추적할 수 있습니다.

1. **설정** > **이벤트 사용자 로그**로 이동합니다.
2. SDK 요청을 테스트 사용자에 대해 찾고 확장하세요.
3. **원시 데이터**를 클릭합니다.
4. 세션을 위한 `id`를 찾으세요. 다음은 예시 발췌문을 보여줍니다:

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

5. Base64 디코드 및 인코드와 같은 [디코딩 도구](https://www.base64decode.org/)를 사용하여 `id`를 Base64 형식에서 디코딩하고 관련된 `campaign_id`를 찾으세요. 우리의 예에서, 이것은 다음과 같은 결과를 낳습니다:

    ```
    4861692e-6fce-4215-bd05-3254fb9e9057_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    `4861692e-6fce-4215-bd05-3254fb9e9057`이 `campaign_id`인 곳.<br><br>

6. **캠페인** 페이지로 이동하여 `campaign_id`을 검색하세요.

![캠페인 페이지에서 캠페인_id 검색]({% image_buster /assets/img_archive/cc_debug.png %}){: style="max-width:80%;"}

거기에서 메시지 설정 및 콘텐츠를 검토하여 사용자가 특정 콘텐츠 카드를 볼 수 없는 이유를 파악할 수 있습니다.

