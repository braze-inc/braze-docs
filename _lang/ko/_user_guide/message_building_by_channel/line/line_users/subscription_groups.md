---
nav_title: 구독 그룹
article_title: 구독 그룹
page_order: 1
description: "이 문서에서는 LINE 메시지 구독 그룹에 대해 설명합니다."
page_type: reference
channel:
 - LINE
alias: /line/subscription_groups/
---

# LINE 구독 그룹

> LINE 사용자에게는 구독 및 구독 해지의 두 가지 구독 상태가 있습니다. LINE은 작업 공간당 최대 100개의 구독 그룹을 가질 수 있으며, 각 구독 그룹은 자체 LINE 채널에 연결되어 있습니다.

| 상태 | 정의 |
| --- | --- |
| 구독됨 | 사용자가 LINE 앱 내에서 LINE 채널을 팔로우했습니다. 사용자가 통합 단계를 완료한 후 팔로우하면 자동으로 구독됩니다. |
| 구독 해지됨 | 사용자가 LINE 앱 내에서 LINE 채널을 팔로우하지 않았거나, 사용자가 명시적으로 LINE 채널의 팔로우를 해제했습니다. <br><br> LINE 구독 그룹에서 구독 해지한 사용자는 구독 그룹에 속한 발신 채널로부터 더 이상 LINE 메시지를 받지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 }

## 사용자의 LINE 구독 그룹 설정

LINE은 사용자의 구독 상태를 호스팅합니다. Braze는 구독 상태를 업데이트하는 팔로우 및 언팔로우 이벤트를 처리합니다.