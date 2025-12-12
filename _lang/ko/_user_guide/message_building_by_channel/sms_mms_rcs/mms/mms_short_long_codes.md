---
nav_title: "MMS 짧은 코드와 긴 코드"
article_title: MMS 짧은 코드 및 긴 코드
page_order: 1
description: "이 참조 문서는 SMS와 MMS 짧은 코드 및 긴 코드 간의 차이를 다룹니다."
page_type: reference
alias: /mms_short_long_codes/
channel:
  - MMS
  
---

# MMS 짧은 코드와 긴 코드

> MMS와 SMS는 모두 Braze SMS 채널에 연결되어 있습니다. 계정에서 MMS에 접근하려면 아직 접근을 구매하지 않은 사람들을 위해 SMS를 구매해야 합니다. 기존 SMS 고객은 MMS를 구매한 후에 접근할 수 있습니다. 

MMS는 현재 미국 짧은 코드(5-6자리 숫자), 미국 및 캐나다 긴 코드(10자리 숫자), 그리고 미국 및 캐나다 고객 번호에 대해 지원됩니다. 미국/캐나다 외부의 번호로 MMS를 보내는 것은 가능하지만, MMS 메시지는 미디어 자산에 대한 링크가 포함된 SMS 메시지로 변환됩니다. 자세한 내용을 보려면 [짧은 코드 및 긴 코드]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/)를 참조하십시오.

## MMS 짧은 코드

일부 사용자는 MMS 짧은 코드를 구현하거나 사용하지 않을 수 있지만, 나중에 필요할 경우 사용할 수 있습니다.

Braze가 MMS를 지원하기 전에 짧은 코드를 받은 사용자에 대해, 모든 기존 고객은 미국 짧은 코드로 MMS를 즉시 활성화할 수 있습니다. 이 상황이 해당되면 고객 성공 관리자에게 연락하여 MMS를 활성화하고 싶다고 말씀해 주십시오.

{% alert important %}
이전에 MMS가 활성화되지 않았던 짧은 코드에 대해 MMS를 활성화할 때, 짧은 코드는 몇 주가 걸릴 수 있는 승인 프로세스에서 재승인되어야 할 수 있습니다. MMS를 활성화하기로 결정할 때 이 타이밍을 고려하는 것이 중요합니다.
{% endalert %}

### MMS 짧은 코드 모범 사례

- Braze에서는 거래 및 프로모션 메시지를 별도로 유지하고 각각 다른 짧은 코드를 사용하는 것을 강력히 권장합니다. MMS가 SMS 채널에 연결되어 있고 SMS 채널이 엄격하게 규제되기 때문에, 고객은 채널을 잘못 사용하여 금전적 벌금을 지불해야 하거나 짧은 코드가 정지될 수 있습니다(이는 되돌릴 수 없습니다). 거래 및 프로모션 메시지를 서로 다른 단축 코드에 연결하면 거래 메시지를 안전하게 보호할 수 있습니다.
- 고객이 이미 프로모션 메시지 전용 단축 코드를 가지고 있고 MMS가 활성화되어 있다면, MMS를 위한 별도의 단축 코드가 필요하지 않습니다.

## MMS 긴 코드

고객은 긴 코드를 사용하여 MMS를 보낼 수 있습니다. 이를 위해서는 긴 코드가 MMS 활성화되어 있는지 확인해야 합니다. 이는 설정 중에 처음에 수행하거나 나중에 계정 내에서 수행할 수 있습니다. 

우리의 MMS 메시지는 영숫자 발신자 ID로 보낼 수 없다는 점에 유의하십시오. 영숫자 ID에 대해 더 알아보려면 [영숫자 발신자 ID]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#alphanumeric-sender-id)를 확인하세요.
