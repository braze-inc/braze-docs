---
nav_title: 알림 환경설정
article_title: 알림 환경설정
page_order: 1
page_type: reference
description: "이 참고 문서에서는 회사 계정의 메시징 및 활동을 모니터링하는 데 사용할 수 있는 옵션에 대해 설명합니다."

---

# 알림 환경설정

> 회사 계정의 메시징 및 활동을 모니터링하려면 특정 알림을 설정하고 알림이 전송되는 위치를 선택할 수 있습니다.

**알림 기본 설정** 페이지에서는 회사에 대한 알림을 받을 사람(있는 경우)을 구성할 수 있습니다. 캠페인 전달 또는 기술적 오류에 대한 알림을 수신할 대상을 구성할 수 있습니다. 주간 분석 보고서의 수신자를 지정할 수도 있습니다. 대부분의 알림에 대해 Braze는 이메일과 웹훅 채널을 지원합니다.

![Braze 대시보드의 알림 환경설정 페이지]({% image_buster /assets/img_archive/notification_preferences.png %})

이 페이지에 액세스하려면 **설정** > **관리자 설정** > **알림 환경설정으로** 이동합니다.

## 사용 가능한 알림

다음 표에서는 사용 가능한 알림과 알림을 전달하는 데 사용되는 채널에 대해 설명합니다.

| 알림 | 설명 | 사용 가능한 알림 채널 |
|--------------|-------------|-----------------|
| AWS 자격증명정보 오류 | Braze가 데이터 내보내기를 위해 Amazon Web Services 자격증명정보를 사용하는 중에 오류 메시지를 받을 때 수신자에게 알립니다. This includes credential error notifications for Google Cloud Services and Azure (Microsoft Cloud Services). | 이메일, 웹훅 |
| 캠페인 자동 중단 | Braze가 캠페인을 중단했을 때 수신자에게 알립니다. | 이메일 |
| 캠페인 상호작용 만료 | 캠페인 상호작용 데이터 만기가 다가온 캠페인, 리타겟팅 필터에서 참조하고 30일 이내에 메시지 발송에 활용된 세그먼트, 캠페인, 캔버스에 대한 정보를 수신자에게 알립니다. | 이메일 |
| 캠페인/캔버스 업데이트됨 | Notifies recipients when an active campaign or Canvas is updated or deactivated, as well as when an inactive campaign or Canvas is reactivated or drafts are launched. | 이메일 |
| Campaign/Canvas Volume Limit Met | Notifies recipients when a campaign or Canvas meets its volume limit. | 이메일 | 
| 캔버스 상호작용 만료 | 캔버스 상호작용 데이터 만기가 다가온 캔버스, 리타겟팅 필터에서 참조하고 30일 이내에 메시지 발송에 활용된 세그먼트, 캠페인, 캔버스에 대한 정보를 수신자에게 알립니다. | 이메일 |
| 푸시 자격증명정보 오류 | 앱의 푸시 인증정보가 유효하지 않은 경우와 앱의 푸시 인증정보가 곧 만료되는 경우 수신자에게 알림을 보냅니다. | 이메일, 웹훅 |
| 예정된 캠페인 발송/미발송 | 예약된 캠페인이 전송을 시작하거나 예약된 캠페인이 전송을 시도했지만 전송할 적격 사용자가 없는 경우 수신자에게 알립니다. | 이메일, 웹훅 |
| 예정 캠페인 한도 도달 | 반복되는 예정 캠페인의 한도에 도달했을 때 수신자에게 알립니다. | 이메일, 웹훅 |
| 예정된 캠페인 발송 종료 | 예정된 캠페인 발송이 종료될 때 수신자에게 알립니다. | 이메일, 웹훅 |
| 주간 분석 보고서 | 지난 주 워크스페이스 활동 요약을 매주 월요일 수신자에게 발송합니다. 수신자는 소속 워크스페이스에 대한 요약서를 수신합니다. | 이메일 |
| 일일 캔버스/캠페인 참가 수량 제한 | 전송 한도에 도달할 때마다 알림을 보냅니다. | 이메일 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 주간 분석 보고

Braze는 선택적으로 매주 월요일 오전 5시에 회사 내에서 지정한 개인에게 이메일을 통해 주간 보고서를 발송합니다. **데이터 설정** > **사용자 지정** 이벤트에서 주간 보고서에 포함할 사용자 지정 이벤트를 선택할 수 있습니다.

주간 보고서에 포함할 이벤트를 최대 5개까지 선택할 수 있습니다:

![애널리틱스 보고서에 포함할 이벤트 선택하기]({% image_buster /assets/img_archive/company_analytics_report_new.png %})

## Slack 수신 웹훅 통합

Slack에는 외부 소스에서 Slack으로 메시지를 게시할 수 있는 [수신 웹훅 앱이](https://my.slack.com/services/new/incoming-webhook/) 있습니다. 시작하려면 수신 웹훅 앱을 엽니다.

1. 알림을 받을 Slack 채널을 선택하고 **수신 웹훅 통합 추가**를 클릭합니다.<br><br>
    ![Slack에 수신 웹훅 통합 추가]({% image_buster /assets/img_archive/slack_f.png %})<br><br>
  Slack은 수신하려는 알림을 위해 Braze에 입력해야 하는 URL을 생성합니다.<br><br>
2. **웹훅 URL**을 복사합니다.<br><br>
    ![웹훅 URL 복사]({% image_buster /assets/img_archive/copy_url.png %})<br><br>
3. **회사 설정의** **알림 환경설정** 탭으로 이동합니다.<br><br>
4. Slack에 사용 설정하려는 알림을 선택합니다. 또는 이 Slack 채널로 보내려는 알림이 여러 개 있는 경우 **대량 추가**를 사용하여 여러 알림에 웹훅을 추가하세요.<br><br>
    ![Slack 알림을 선택하여 사용 설정]({% image_buster /assets/img_archive/click_edit_f.png %}){: style="max-width:60%;"}<br><br>
5. Slack에서 생성한 URL을 입력합니다.

끝입니다! 이 Slack 채널에서 회사에 대한 알림을 받기 시작해야 합니다. 이 주제에 대한 Slack의 도움말 문서도 확인할 수 있습니다: [수신 웹훅을 사용하여 메시지 보내기](https://api.slack.com/incoming-webhooks).

