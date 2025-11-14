---
nav_title: 테스트
article_title: 콘텐츠 카드 테스트하기
page_order: 3
description: "이 참고 문서에서는 콘텐츠 카드를 미리 보고 테스트하는 방법과 몇 가지 모범 사례를 다룹니다."
channel:
  - content cards
  
---

# 콘텐츠 카드 테스트하기

> 캠페인을 보내기 전에 항상 콘텐츠 카드를 테스트하는 것이 매우 중요합니다. 미리보기 및 테스트 기능은 콘텐츠 카드를 살펴볼 수 있는 두 가지 방법을 제공합니다. 메시지를 작성할 때 시각화할 수 있도록 미리 볼 수 있고, 본인 또는 특정 사용자의 기기에 테스트 메시지를 보낼 수도 있습니다. 두 가지를 모두 활용하는 것이 좋습니다.

## 미리 보기

카드를 작성할 때 미리 볼 수 있습니다. 이를 통해 사용자의 관점에서 최종 메시징이 어떻게 보일지 시각화할 수 있습니다.

작성기의 **미리보기** 탭에서 메시지의 보기가 사용자 기기의 실제 렌더링과 동일하지 않을 수 있습니다. 미디어, 카피, 개인화 및 커스텀 속성이 올바르게 생성되는지 확인하기 위해 항상 기기에 테스트 메시지를 보내는 것이 좋습니다.

## 테스트

[콘텐츠 테스트 그룹]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) 또는 개별 사용자에게 테스트를 보내려면 보내기 전에 테스트 사용자에 대해 등록된 유효한 푸시 토큰으로 테스트 기기에서 푸시를 인에이블먼트해야 합니다. iOS 사용자의 경우, 테스트 콘텐츠 카드를 보려면 Braze에서 보낸 푸시 알림을 탭해야 합니다. 이 동작은 테스트 콘텐츠 카드에만 적용됩니다.

### 사용자로서 메시지 미리보기

**테스트** 탭에서 사용자가 된 것처럼 메시지를 미리 볼 수도 있습니다. 특정 사용자, 임의의 사용자를 선택하거나 커스텀 사용자를 만들 수 있습니다.

'테스트' 탭에서 콘텐츠 카드 미리 보기.]({% image_buster /assets/img/cc-user-preview.png %}){: style="max-width:80%;"}

### 테스트 체크리스트

- 이미지와 미디어가 예상대로 표시되고 작동하나요?
- Liquid가 예상대로 작동하나요? Liquid가 정보를 반환하지 않는 경우의 [기본 속성 값을]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) 고려하셨나요?
- 카피가 명확하고 간결하며 정확한가요?
- 링크가 사용자가 이동해야 하는 곳으로 연결되나요?

## Debug

콘텐츠 카드가 전송된 후에는 개발자 콘솔의 [이벤트 사용자 로그에서]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) 문제를 분석하거나 디버깅할 수 있습니다. 

일반적인 사용 사례는 사용자가 특정 콘텐츠 카드를 볼 수 없는 이유를 디버깅하는 것입니다. 이를 위해 세션 시작 시 소프트웨어 개발 키트에 전달된 콘텐츠 카드의 **이벤트 사용자 로그에서** 노출 횟수 이전에 특정 캠페인을 추적할 수 있습니다:

1. **설정** > 이벤트 사용자 로그로 이동합니다.
2. 테스트 사용자를 위한 소프트웨어 개발 키트 요청을 찾아서 펼칩니다.
3. **원시 데이터를** 클릭합니다.
4. 세션에 대한 `id` 을 찾아보세요. 다음은 발췌한 예시입니다:

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

5. [Base64 디코딩 및 인코딩과](https://www.base64decode.org/) 같은 디코딩 도구를 사용하여 Base64 형식에서 `id` 을 디코딩하고 관련 `campaign_id` 을 찾습니다. 이 예제에서는 다음과 같은 결과가 나타납니다:

    ```
    4861692e-6fce-4215-bd05-3254fb9e9057_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    여기서 `4861692e-6fce-4215-bd05-3254fb9e9057` 은 `campaign_id`.<br><br>

6. **캠페인** 페이지로 이동하여 `campaign_id` 을 검색합니다.

캠페인 페이지에서 campaign_id 검색하기]({% image_buster /assets/img_archive/cc_debug.png %}){: style="max-width:80%;"}

여기에서 메시지 설정과 콘텐츠를 검토하여 드릴다운하여 사용자가 특정 콘텐츠 카드를 볼 수 없는 이유를 파악할 수 있습니다.

