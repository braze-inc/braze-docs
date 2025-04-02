---
nav_title: 중국 Android 기기의 전달 가능성
article_title: 중국 Android 기기의 푸시 전달 가능성
page_order: 10

page_type: reference
description: "이 기사에서는 중국 OEM이 제조한 Android 기기에서 사용자를 타겟팅할 때 알아야 할 푸시 전달 가능성의 미묘한 차이점을 다룹니다."
channel: push

---

# 중국 Android 기기의 푸시 전달 가능성

> 일부 Android 기기는 Xiaomi, OPPO, Vivo와 같은 중국의 원래 장비 제조업체(OEM)가 제조하며, 공격적인 앱 수명 주기 관리를 통해 더 긴 배터리 수명을 최적화합니다. 이 최적화는 백그라운드 앱 처리를 중단시키는 의도치 않은 결과를 초래할 수 있으며, 이는 푸시 알림의 전달 가능성을 감소시킬 수 있습니다.<br><br>이 기사의 단계에 따라 앱의 메시징 성능이 이러한 기기에서 예상대로 작동하도록 마케팅 및 엔지니어링 팀이 협력해야 합니다.

## 개발자를 위한 단계
이들 OEM은 백그라운드 애플리케이션을 공격적으로 종료하고 백그라운드 작업을 실행하기 위해 자체 시작을 차단함으로써 최적화를 수행합니다. 개발자로서 사용자가 이러한 제한을 완화하도록 앱을 구성해야 합니다.

이는 앱이 최종 사용자의 기기에서 자동으로 시작되도록 하여 앱이 백그라운드에서 실행되고 Braze로부터의 메시지를 수신할 수 있도록 허용함으로써 달성할 수 있습니다. 불행히도, 이것은 Android 문제가 아닌 OEM 특정 문제이기 때문에 각 OEM에 대한 자동 시작 권한 프롬프트를 표시하는 문서화된 API가 없습니다.

이를 해결하려면 [AutoStarter](https://github.com/judemanutd/AutoStarter)와 같은 라이브러리를 애플리케이션에 통합하십시오. AutoStarter는 여러 제조업체를 지원하여 다양한 기기에서 시작 권한 매니저를 쉽게 호출할 수 있는 방법을 제공합니다. AutoStarter를 통합한 후, `AutoStartPermissionHelper.getInstance().getAutoStartPermission(context)`을 호출하여 최종사용자의 기기에서 시작 권한 매니저를 불러옵니다. 이 작업을 앱의 "자동 시작"을 활성화하도록 최종 사용자에게 권장하는 메시지와 결합하세요. 귀하의 마케팅 팀이 이 메시지를 작성할 것입니다. 다음 섹션을 참조하십시오!

## 마케터를 위한 단계
사용자가 푸시 알림을 받도록 선택한 후, 이러한 기기의 메시지 전달을 개선하기 위해 추가로 취할 수 있는 단계가 있습니다. We recommend you follow up your [push primer message]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) with an in-app message targeted to users on Chinese OEM devices with these additional steps:

- 앱의 "자동 시작"을 활성화하십시오
- 앱의 배터리 최적화를 비활성화합니다

메시지를 더욱 증폭시키기 위해 SMS, WhatsApp, LINE과 같은 앱 외 채널과 인앱 메시지 및 콘텐츠 카드와 같은 인앱 채널을 통해 열리지 않은 푸시 알림의 정보를 다시 표면화하는 다른 채널을 추가하세요. 사용자가 앱을 열 때 놓친 내용을 확인할 수 있습니다.