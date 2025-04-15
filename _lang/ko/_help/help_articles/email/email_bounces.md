---
nav_title: 이메일 반송
article_title: 이메일 반송
page_order: 0
page_type: solution
description: "이 도움말 문서에서는 하드 바운스와 소프트 바운스의 차이점을 명확하게 설명합니다."
channel: email
---

# 이메일 반송

이메일 캠페인에서 보낸 메시지가 사용자의 이메일 주소에서 반송되면 어떻게 해야 하나요? 먼저 이메일 반송의 두 가지 유형인 하드 반송과 소프트 반송을 정의하고 문제를 해결해 보겠습니다. 

## 하드 바운스

{% multi_lang_include metrics.md metric='Hard Bounce' %}

자세한 내용은 [하드 바운스를]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#hard-bounce) 참조하세요.

## 소프트 바운스

{% multi_lang_include metrics.md metric='Soft Bounce' %} 

이메일이 소프트바운스되면 일반적으로 72시간 이내에 재시도하지만, 재시도 횟수는 수신자마다 다릅니다.

소프트바운스는 캠페인 분석에서 추적되지 않지만, [메시지 활동 로그][3]에서 소프트바운스를 모니터링할 수 있습니다. 여기에서 소프트바운스의 원인을 확인하고 이메일 캠페인의 "전송"과 "전달" 간에 발생할 수 있는 불일치를 파악할 수도 있습니다.

이메일 구독 및 캠페인 관리에 대해 자세히 알아보려면 [이메일 관련 모범 사례][2]를 확인하세요.

아직도 도움이 필요하신가요? [지원 티켓]({{site.baseurl}}/braze_support/)을 여세요.

_마지막 업데이트 2024년 5월 2일_

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices
[3]: {{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/
