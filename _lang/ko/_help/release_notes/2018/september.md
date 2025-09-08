---
nav_title: 9월
page_order: 5
noindex: true
page_type: update
description: "이 문서에는 2018년 9월 릴리스 노트가 포함되어 있습니다."
---
# 2018년 9월

## iOS 12 알림 그룹: 추가 능력

이제 Braze를 사용하여 [Apple의 알림 그룹 기능]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups)에 액세스할 수 있습니다! 요약 인수 및 그룹을 추가하고, 중요 경고를 활용하고, 필터를 사용하여 임시 인증된 사용자를 표시하고, 고객 프로필에서 임시 인증된 상태를 볼 수 있습니다.

## 조용한 시간

고객은 이제 캔버스에 대해 [방해금지 시간]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-5-select-your-send-settings) (메시지가 전송되지 않는 시간)을 지정할 수 있습니다. 그냥 **캔버스 전송 설정**으로 가서 "방해금지 시간 활성화"를 확인하세요. 그런 다음 사용자의 로컬 시간에 맞춰 방해금지 시간을 선택하고 메시지가 해당 방해금지 시간 내에 트리거될 경우 어떤 조치가 따를지 선택합니다.

캠페인은 이제 "하루 중 특정 시간에 이 메시지를 보내기" 대신 조용한 시간을 사용합니다.

## 고객 조정

Braze 고객은 이제 [Adjust]({{site.baseurl}}/partners/message_orchestration/attribution/adjust/)를 사용하여 Braze API 키와 Braze 인스턴스 URL을 확인할 수 있으며, 이를 Adjust 플랫폼에서 통합하는 데 사용할 수 있습니다.

## 세그먼트 필터에 없음

고객은 이제 [특정 세그먼트에 포함되지 않은]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#retargeting) 사용자를 세그먼트로 만들 수 있습니다.

## 캔버스 수신자 CSV 내보내기

고객은 이제 캔버스에 들어간 사용자에 대한 [데이터]({{site.baseurl}}/user_guide/data/export_braze_data/export_canvas_data/)를 내보낼 수 있습니다. 생성된 CSV는 캠페인 CSV와 유사할 것입니다.

## 임시로 승인된 iOS 12 세그먼트 필터

iOS 12에서 특정 앱에 대해 임시로 승인된 사용자를 찾을 수 있는 [세그먼트 필터]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#other)가 추가되었습니다.

## 인앱 메시지 이미지 업로더

인앱 메시지용 이미지 업로더가 디자인 패널에서 작성 패널로 이동했습니다.

## 읽기 전용 권한 고객 프로필 페이지에서

이 릴리스 이전에는 고객이 [읽기 전용 권한]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions)으로 고객 프로필에서 구독 상태 및 이메일 주소를 변경할 수 있었습니다. Braze는 `import_user` 권한의 이름을 `import_and_update_user` 권한으로 변경하고 구독 상태 및 이메일 주소에 대한 편집 액세스를 제한했습니다. 이제 개발자가 읽기 전용으로 가장하거나 이 권한이 없는 경우 구독 상태나 이메일 주소를 변경할 수 없습니다.
