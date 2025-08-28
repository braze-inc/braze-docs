---
nav_title: 푸시 극대화
article_title: 푸시 극대화
page_type: reference
description: "푸시 극대화는 실패한 푸시 알림을 추적하고 사용자가 푸시를 받을 가능성이 더 높은 시점에 푸시를 다시 발송함으로써 Android 푸시 알림의 효과를 증대시켜 줍니다."

permalink: /user_guide/message_building_by_channel/push/android/push_max/
platform: Android
channel:
  - Push

---

# 푸시 극대화

> 푸시 맥스에 대해 알아보고 이 기능을 사용하여 [중국 OEM 디바이스에]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/) 대한 Android 푸시 알림의 전달성을 잠재적으로 개선하는 방법을 알아보세요.

## 푸시 극대화란 무엇인가요?

푸시 극대화는 실패한 푸시 알림을 추적하고 사용자가 푸시를 받을 가능성이 더 높은 시점에 푸시를 다시 발송함으로써 Android 푸시 알림의 효과를 증대시켜 줍니다.

Xiaomi, OPPO, Vivo 등 중국 OEM(주문자 상표 부착 생산업체)에서 제조한 일부 Android 디바이스는 배터리 수명을 연장하기 위해 강력한 배터리 최적화 방식을 채택하고 있습니다. 이 동작은 백그라운드 앱 처리를 종료하는 의도하지 않은 결과를 초래할 수 있으며, 앱이 포그라운드에 있지 않은 경우 이러한 기기에서 푸시 알림의 전달 가능성을 떨어뜨립니다. 이러한 상황은 아시아 태평양(APAC) 시장에서 가장 자주 발생합니다.

## 가용성

- Android 푸시 알림에만 사용 가능
- 액션 기반 또는 API 트리거 메시지에는 지원되지 않습니다.
- Not supported when the option to [only send to the user's last used device]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#device-options) is selected

## 전제 조건

푸시 극대화를 사용하여 전송된 푸시 알림은 다음 [최소 SDK 버전]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions) 이상의 기기에만 전달됩니다.

{% sdk_min_versions android:29.0.1 %}

## 푸시 최대 사용

{% tabs %}
{% tab 캠페인 %}

캠페인에서 푸시 극대화 사용하기:

1. 푸시 캠페인을 만듭니다.
2. 플랫폼으로 **Android 푸시**를 선택합니다.
3. **배송 예약** 단계로 이동합니다.
4. **푸시를 극대화를 사용하여 보내기**를 선택합니다.

!["푸시 최대값을 사용하여 보내기" 옵션이 있는 배달 예약 단계의 Android 푸시 전달 가능성 섹션(]({% image_buster /assets/img_archive/push_max_campaigns.png %})

{% endtab %}
{% tab 캔버스 %}

캔버스에서 푸시 극대화 사용하기:

1. 캔버스에 메시지 단계를 추가합니다.
2. 플랫폼으로 **Android 푸시**를 선택합니다.
3. **배달 설정** 탭으로 이동합니다.
4. **푸시를 극대화를 사용하여 보내기**를 선택합니다.

![Android 푸시 메시지 단계의 전달 설정 탭에서 '푸시 극대화를 사용하여 보내기' 옵션을 선택합니다.]({% image_buster /assets/img_archive/push_max_canvas.png %})

{% endtab %}
{% endtabs %}

다음 두 가지 기능인 Intelligent Timing과 TTL은 푸시 극대화와 함께 사용하면 Android 푸시 알림의 전달 가능성을 높일 수 있습니다.

### Intelligent Timing

푸시 극대화는 [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)이 켜져 있을 때 가장 잘 작동합니다. Intelligent Timing은 사용자가 앱을 사용할 가능성이 가장 높고 푸시가 전달될 가능성이 가장 높은 시간을 계산하여 푸시 알림을 보낼 수 있습니다.

### TTL

TTL(Time to Live)은 실패한 푸시 알림을 Firebase 클라우드 메시징(FCM)으로 추적하여 사용자가 알림을 받을 가능성이 있을 때 알림을 다시 시도할 수 있습니다.

기본적으로 TTL은 최대인 28일로 설정되어 있습니다. **설정** > **워크스페이스 설정** > **푸시 시간(TTL)**에서 모든 새 Android 푸시 메시지의 기본 TTL을 줄이거나, Android 푸시 알림을 작성할 때 **설정** 탭에서 메시지별로 일 수를 구성할 수 있습니다.

![Time to Live field set to 28 days.]({% image_buster /assets/img_archive/time_to_live.png %}){: style="max-width:60%"}

## 알아두어야 할 사항

### 프로모션 코드

푸시 극대화가 켜져 있는 메시지에는 Braze [프로모션 코드]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/)를 사용하지 않는 것이 좋습니다.

이는 프로모션 코드가 고유하기 때문입니다. 프로모션 코드가 포함된 푸시 알림이 전달되지 않은 경우, 푸시 맥스로 인해 해당 알림이 다시 전송되면 새 프로모션 코드가 전송됩니다. 이로 인해 프로모션 코드가 예상보다 빨리 소모될 수 있습니다.

### 캔버스 이벤트 속성 및 항목 속성

메시지에 [캔버스 항목 속성 또는 이벤트 속성정보]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)에 대한 Liquid 참조를 포함하면 푸시 맥스가 예상대로 작동하지 않을 수 있습니다. 이는 푸시 극대화에서 메시지를 다시 보내려고 할 때 항목 및 이벤트 속성정보를 사용할 수 없기 때문입니다.
