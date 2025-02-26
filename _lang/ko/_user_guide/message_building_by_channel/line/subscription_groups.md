---
nav_title: 구독 그룹
article_title: 구독 그룹
page_order: 3
description: "이 문서에서는 LINE 메시지 구독 그룹에 대해 설명합니다."
page_type: reference
channel:
 - LINE
hidden: true
permalink: /line/subscription_groups/
---

# LINE 구독 그룹

> LINE 사용자에게는 구독 상태와 구독 취소 상태 두 가지가 있습니다. LINE은 워크스페이스당 최대 100개의 구독 그룹을 만들 수 있으며, 각 구독 그룹은 자체 LINE 채널에 연결됩니다.<br><br>이 글은 LINE 베타 컬렉션의 일부입니다. [메인 페이지로 돌아갑니다](https://www.braze.com/docs/line/).

{% alert important %}
LINE 액세스는 베타 버전이며 일부 Braze 패키지에서만 사용할 수 있습니다. 시작하려면 계정 관리자 또는 고객 성공 관리자에게 문의하세요.
{% endalert %}

| 상태 | 정의 |
| --- | --- |
| 가입됨 | 이 사용자는 LINE 앱 내에서 LINE 채널을 팔로우했습니다. 통합 단계를 완료한 후 사용자가 팔로우하면 자동으로 구독하게 됩니다. |
| 탈퇴됨 | 사용자가 LINE 앱 내에서 LINE 채널을 팔로우하지 않았거나 사용자가 명시적으로 LINE 채널을 언팔로우한 경우. <br><br> LINE 정기구독 그룹에서 탈퇴한 사용자는 더 이상 해당 그룹에 속한 채널에서 보내는 LINE 메시지를 받지 않게 됩니다. |
{: .reset-td-br-1 .reset-td-br-2 }

## 사용자의 LINE 구독 그룹 설정하기

LINE은 사용자의 구독 상태를 관리합니다. Braze는 구독 상태를 업데이트하는 팔로우 및 언팔로우 이벤트를 처리합니다.