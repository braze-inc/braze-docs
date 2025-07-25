---
nav_title: Quick Push Messages
article_title: Quick Push Messages
alias: "/quick_push/"
description: "이 문서에서는 빠른 푸시 편집 환경을 사용하여 푸시 캠페인 또는 캔버스를 만들 때 알아야 할 사항에 대해 설명합니다."
---

# Quick push messages

When creating a push campaign or Canvas in Braze, you can select multiple platforms and devices to craft one message for all platforms in a single editing experience called quick push.

## 사용 사례

이 편집 환경은 다음과 같은 사용 사례에 가장 적합합니다:

- Mobile push campaigns and Canvas Message steps that need to be sent to multiple device types (such as both iOS and Android).
- 여러 플랫폼에 걸쳐 콘텐츠가 동일한 경우(예: 속보 또는 실시간 게임 업데이트) 여러 플랫폼을 빠르고 정확하게 타겟팅해야 하는 시간에 민감한 푸시 알림입니다.

## Creating a quick push campaign or Canvas

여러 플랫폼과 기기를 타겟팅하는 캠페인을 만들려면 다음과 같이 하세요.

1. Create a campaign or add a [Message step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) to a Canvas.  
2. Select **Push notification**.
3. 원하는 플랫폼(모바일, 웹, Kindle) 및 모바일 디바이스(iOS, Android)를 선택합니다. 여러 기기를 선택하면 캠페인에 다변량 테스트를 사용할 수 없습니다.

### Selecting platforms for a campaign
![푸시 캠페인에 대해 모바일, 웹, 킨들 등 여러 플랫폼과 iOS, Android 등 여러 기기를 선택할 수 있는 옵션입니다.][1]

### Selecting platforms for a Canvas step
![Options to select multiple platforms for a push Message step, such as Mobile, Web, and Kindle, and multiple devices, such as iOS and Android.][8]

{:start="4"}
4\. Select **Confirm**. After selecting **Confirm**, you will be unable to change your selected platforms or devices.
5\. Continue setting up your campaign or Canvas.

작성기가 평소와 약간 다르게 보일 것입니다. 무엇이 달라졌는지 계속 읽어보세요.

### 달라진 점

**작성** 탭에서 선택한 모든 플랫폼 및 기기에 대해 하나의 제목, 메시지 및 클릭 시 동작을 지정할 수 있습니다.

미리보기 창에는 각 플랫폼에서 메시지가 어떻게 보일지에 대한 대략적인 모습이 표시됩니다. 글자 수 제한에 도달할 수 있는 지점을 파악할 수 있지만, 캠페인을 보내기 전에 항상 실제 기기에서 메시지를 테스트해야 한다는 점을 잊지 마세요.

![iOS, Android, 웹의 세 가지 푸시 유형에 대해 하나의 제목, 메시지, 클릭 시 동작 필드가 포함된 단일 편집 보기를 제공합니다.][2]

**자산** 섹션에서 각 플랫폼에 표시할 이미지를 선택하거나 업로드합니다. 기기마다 이미지와 글자 수에 대한 사양이 다르다는 점에 유의하세요. 푸시 메시지 및 이미지 형식][3] 도움말을 참조하세요.

![단일 편집 보기의 자산 섹션에 푸시 아이콘 이미지, iOS 알림 이미지, Android 알림 이미지 및 웹 알림 이미지 필드가 있습니다.][4]{:style="max-width:50%"}

그런 다음 평소와 같이 푸시 캠페인 설정을 완료합니다. 자세한 내용은 [푸시 캠페인 만들기][5] ]를 참조하세요.

## 알아두어야 할 사항

### 알림 유형

알림 유형은 기본적으로 '표준 푸시'로 설정되어 있으며 변경할 수 없습니다. 푸시 스토리 또는 인라인 이미지(Android)와 같은 다른 푸시를 만들려면 각 기기 유형에 대해 별도의 캠페인을 만드세요.

### 다변량 테스트

iOS 및 Android와 같은 모바일 플랫폼에 대해 여러 디바이스를 선택하는 경우 캠페인에 다변량 테스트를 사용할 수 없습니다. 다변량 테스트를 수행하려면 각 기기 유형에 대해 별도의 캠페인을 만드세요.

### 기기별 설정

편집기에서 플랫폼별 설정을 편집할 수 있습니다. 여기에는 [푸시 실행 버튼]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_action_buttons/), 알림 채널 및 그룹, TTL, 디스플레이 우선순위, 소리 등의 설정이 포함됩니다. 

퀵 푸시 캠페인을 사용하여 iOS와 안드로이드를 모두 타겟팅하는 경우 푸시 액션 버튼은 지원되지 않습니다. 기기별 설정에 대한 자세한 내용은 다음 문서 모음을 참조하세요.

- [iOS 옵션][6]
- [안드로이드 옵션][7]


[1]: {% image_buster /assets/img_archive/quick_push_1.png %}
[2]: {% image_buster /assets/img_archive/quick_push_2.png %}
[4]: {% image_buster /assets/img_archive/quick_push_3.png %}
[8]: {% image_buster /assets/img_archive/quick_push_4.png %}
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/push/ios
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/push/android