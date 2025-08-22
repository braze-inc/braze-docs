---
nav_title: "MMS 짧은 코드 및 긴 코드"
article_title: MMS 짧은 코드 및 긴 코드
page_order: 1
description: "이 참조 문서는 SMS 및 MMS 짧은 코드와 긴 코드 간의 차이점을 다룹니다."
page_type: reference
alias: /mms_short_long_codes/
channel:
  - MMS
  
---

# MMS 단문 및 장문 코드

> MMS와 SMS는 모두 Braze SMS 채널과 연결되어 있습니다. 계정에서 MMS에 액세스하려면 아직 액세스를 구매하지 않은 사람들을 위해 SMS를 구매해야 합니다. 기존 SMS 고객은 MMS를 구매한 후에 MMS에 액세스할 수 있습니다. 

MMS는 현재 미국 짧은 코드(5-6자리 숫자), 미국 및 캐나다 긴 코드(10자리 숫자), 그리고 미국 및 캐나다 고객 번호를 지원합니다. 미국/캐나다 외부의 번호로 MMS를 보내는 것은 가능하지만, MMS 메시지는 미디어 자산에 대한 링크가 포함된 SMS 메시지로 변환됩니다. To read more, refer to [Short and long codes]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/).

## MMS 단축 코드

일부 사용자는 MMS 짧은 코드를 구현하거나 사용하지 않을 수 있지만, 나중에 필요할 경우 사용할 수 있습니다.

Braze에서 MMS를 지원하기 전에 짧은 코드를 받은 사용자의 경우, 미국 짧은 코드를 가진 모든 기존 고객은 MMS를 즉시 활성화할 수 있습니다. 해당 상황이 귀하에게 적용되고 MMS를 활성화하고 싶다면 고객 성공 매니저에게 문의하세요.

{% alert important %}
짧은 코드에 대해 MMS를 활성화할 때 이전에 MMS가 활성화되지 않은 경우, 짧은 코드는 몇 주가 걸릴 수 있는 승인 절차에서 다시 승인되어야 할 수 있습니다. MMS를 활성화하기로 결정할 때 이 타이밍을 고려하는 것이 중요합니다.
{% endalert %}

### MMS 짧은 코드 모범 사례

- Braze에서는 트랜잭션 및 프로모션 메시징을 각각 다른 단축 코드로 분리할 것을 강력히 권장합니다. MMS는 SMS 채널에 연결되어 있고 SMS 채널은 매우 엄격하게 규제되기 때문에, 고객은 채널을 오용한 대가로 금전적 벌금을 지불해야 하며 짧은 코드가 정지될 수 있습니다(이는 되돌릴 수 없습니다). 트랜잭션 및 프로모션 메시징을 다른 단축 코드에 연결하여 트랜잭션 메시징을 보호합니다.
- 고객이 이미 프로모션 메시징에 전용된 짧은 코드를 가지고 있고, MMS가 활성화되어 있다면, MMS를 위한 별도의 짧은 코드가 필요하지 않습니다.

## MMS 장문 번호

고객은 긴 코드로 MMS를 보낼 수 있습니다. 이 작업을 수행하려면 긴 코드가 MMS를 지원하는지 확인해야 합니다. 이 작업은 초기 설정 중에 또는 나중에 계정 내에서 수행할 수 있습니다. 

MMS 메시지는 영숫자 발신자 ID로 보낼 수 없습니다. 영숫자 ID에 대해 자세히 알아보려면 [영숫자 발신자 ID]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#alphanumeric-sender-id)를 확인하세요.
