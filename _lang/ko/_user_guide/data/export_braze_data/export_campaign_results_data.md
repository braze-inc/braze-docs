---
nav_title: 캠페인 데이터 내보내기
article_title: 캠페인 데이터 내보내기
page_order: 0
page_type: reference
description: "이 참조 문서에서는 단일, 다중 채널 또는 다변량 캠페인에서 캠페인 결과 데이터를 내보내는 방법에 대해 설명합니다. 이 문서에는 수신자로부터 사용자 데이터를 내보내는 방법도 나와 있습니다."
tool: 
  - Campaigns
  - Reports
  
---

# 캠페인 데이터 내보내기

> 대시보드의 **캠페인** 페이지에서 보려는 캠페인을 선택하고 아래로 스크롤하여 내보낼 수 있는 과거 실적 그래프까지 이동합니다.<br><br>이 페이지에서는 단일, 다중 채널 및 다변량 캠페인에서 캠페인 결과 데이터를 내보내는 방법과 수신자의 사용자 데이터를 내보내는 방법에 대해 설명합니다.

## 멀티채널 캠페인

멀티채널 캠페인의 경우 내보낼 수 있는 데이터는 사용한 메시징 채널에 따라 달라집니다. 다음은 iOS 푸시, Android 푸시, 이메일 및 인앱 메시지를 사용한 캠페인에서 내보낼 수 있는 모든 데이터의 목록입니다.

- 날짜별로 보낸 메시지
    - 보낸 총 메시지 수
    - 캠페인 채널에서 전송된 메시지(푸시, 이메일, 인앱 메시지 포함)
- 날짜별 이메일 메시지 인게이지먼트
    - 전달된 이메일 수
    - 전송된 이메일 수
    - 열람 이메일 수
    - 이메일 클릭 수
    - 이메일 반송 횟수
    - 스팸으로 신고된 이메일 수
- 날짜별 인앱 메시지 인게이지먼트
    - 전송된 인앱 메시지 수
    - 인앱 메시지 노출 수
    - 인앱 메시지 클릭 수
- 날짜별 iOS 푸시 인게이지먼트
    - iOS 푸시 알림 전송 횟수
    - 총 열람 수
    - 직접 열람 수
    - 반송 수
- 날짜별 Android 푸시 인게이지먼트
    - 전송된 Android 푸시 알림 수
    - 총 열람 수
    - 직접 열람 수
    - 반송 수

## 다변량 캠페인

하나의 메시징 채널만 사용하는 다변량 캠페인의 경우, 시간 경과에 따른 특정 메시징 채널의 분석에서 각 변형이 어떻게 수행되었는지 보여주는 데이터를 내보낼 수 있습니다. 이 데이터를 통계별로 그룹화하거나 메시지 배리언트별로 그룹화하여 볼 수 있습니다.

푸시 캠페인 결과에는 다음 분석에 대한 그래프가 포함되어 있습니다:

- 각 배리언트에 대한 날짜별 메시지 전송
- 각 배리언트의 날짜별 전환
- 각 배리언트의 날짜별 고유 수신자
- 각 배리언트에 대한 날짜별 열기
- 각 배리언트에 대한 날짜별 직접 열기
- 각 배리언트에 대한 날짜별 반송

이메일 캠페인 결과에는 다음 분석에 대한 그래프가 포함되어 있습니다.

- 각 배리언트에 대한 날짜별 배송 수
- 각 배리언트에 대한 날짜별 전송 수
- 각 배리언트에 대한 날짜별 열기
- 각 배리언트에 대한 날짜별 클릭 수
- 각 배리언트에 대한 날짜별 반송
- 각 배리언트에 대한 날짜별 스팸 신고

인앱 메시지 캠페인 결과에는 다음 분석에 대한 그래프가 포함되어 있습니다.

- 각 배리언트에 대한 날짜별 전송
- 각 배리언트의 날짜별 노출 수
- 각 배리언트에 대한 날짜별 클릭 수

## 캠페인 수신자

캠페인의 모든 수신자에 대한 사용자 데이터를 CSV 파일로 내보낼 수 있습니다. 이렇게 하려면 **캠페인 세부 정보** 섹션에서 **사용자 데이터** 버튼을 선택합니다.

{% alert note %}
**사용자 데이터** 버튼이 보이지 않나요? 사용자 데이터를 내보내려면 해당 워크스페이스에 대한 **사용자 데이터 내보내기** [권한]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions)이 필요합니다.
{% endalert %}

![User Data dropdown on the Campaign Details page]({% image_buster /assets/img/campaign_export_example.png %})

CSV 출력에는 캠페인의 모든 수신자에 대한 고객 프로필 데이터가 포함됩니다. Braze는 백그라운드에서 보고서를 생성하여 현재 로그인한 사용자에게 이메일로 전송합니다.

If you've linked your [Amazon S3 credentials]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) to Braze, then the CSV will also be uploaded in your S3 bucket. 그렇지 않으면 이메일로 전송된 링크가 몇 시간 후에 만료됩니다.

The exported file includes the same user data fields that are included when you [export user data for a segment]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data). 이러한 데이터 필드 외에도 "모든 수신자 데이터 내보내기"를 선택하면 내보낸 파일에 각 사용자에 대한 다음 데이터도 포함됩니다.

- 수신된 캠페인 배리언트 이름
- 수신된 캠페인 배리언트의 API ID
- 사용자가 대조군에 속해 있는지 여부

{% alert tip %}
CSV 및 API 내보내기에 대한 도움말은 [내보내기 문제 해결을]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/) 참조하세요.
{% endalert %}

