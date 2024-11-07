---
nav_title: LINE 설정
article_title: LINE 설정
description: "이 문서에서는 사전 요구 사항과 제안된 다음 단계를 포함하여 Braze LINE 채널을 설정하는 방법을 설명합니다."
page_type: partner
search_tag: Partner
page_order: 0
channel:
 - LINE
hidden: true
permalink: /line/line_setup/
---


# LINE 설정

> 이 문서는 Braze에서 LINE 채널을 설정하는 방법을 다루고 있으며, LINE 베타 컬렉션의 일부입니다. [메인 페이지로 돌아갑니다](https://www.braze.com/docs/line/).

{% alert important %}
LINE 액세스는 베타 버전이며 일부 Braze 패키지에서만 사용할 수 있습니다. 시작하려면 계정 관리자 또는 고객 성공 관리자에게 문의하세요.
{% endalert %}

## 전제 조건

LINE과 Braze를 연동하려면 다음이 필요합니다:

- [LINE 비즈니스 계정](https://www.linebiz.com/jp-en/manual/OfficialAccountManager/tutorial-steps/?list=7171)
- [프리미엄 또는 인증된 계정](https://www.infobip.com/docs/line/get-started#premium-id-line-official-account) 상태(기존 팔로워를 동기화하는 데 필요)
   - [LINE의 계정 가이드라인](https://terms2.line.me/official_account_guideline_oth) 보기
- [LINE 개발자 계정](https://developers.line.biz/en/docs/line-developers-console/login-account/)
- [LINE 메시징 API 채널](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

## 통합

### 1단계: LINE 채널을 Braze에 연결

1. LINE에서 **메시징 API** 탭으로 이동하여 **웹훅 설정을** 편집합니다:
   - **웹훅 URL을** `https://anna.braze.com/line/events` 으로 설정합니다.
       - Braze는 통합 시 대시보드 클러스터에 따라 자동으로 이 URL을 다른 URL로 변경합니다.
   - **웹훅 사용** 및 **웹훅 재전송을** 켭니다. <br><br> ![웹훅 설정 페이지에서 '웹훅 사용', '웹훅 재전송' 및 '오류 통계 집계'를 켜거나 끄면서 웹훅 URL을 확인하거나 편집할 수 있습니다.][1]{: style="max-width:70%;"}
2. **제공업체** 탭에서 다음 정보를 참고하세요:

| 정보 유형 | 위치 |
| --- | --- |
| 공급자 ID | 제공업체를 선택한 다음 **\*설정** > **기본 정보로** 이동합니다. |
| 채널 ID | 제공업체를 선택한 다음 **채널** > 내 채널 > **기본 설정으로** 이동합니다. |
| 채널 비밀 | 제공업체를 선택한 다음 **채널** > 내 채널 > **기본 설정으로** 이동합니다. |
| 채널 액세스 토큰 | 제공업체를 선택한 다음 **채널** > 내 채널 > **메시징 API로** 이동합니다. 채널 액세스 토큰이 없는 경우 **이슈를** 선택합니다. |
{: .reset-td-br-1 .reset-td-br-2}

{: start="3"}
3\. **설정** 페이지 > **응답 설정으로** 이동하여 다음을 수행합니다:
   - **인사말 메시지를** 끕니다. 이는 팔로우 시 트리거를 통해 Braze에서 처리할 수 있습니다.
   - **자동 응답 메시지를** 끕니다. 트리거된 모든 메시징은 Braze를 통해 이루어져야 합니다. 그렇다고 해서 LINE 콘솔에서 직접 전송하는 것을 막지는 않습니다.
   - **웹훅을** 켭니다.

![응답 설정 페이지에서 계정에서 채팅을 처리하는 방법에 대한 토글을 설정할 수 있습니다.][2]{: style="max-width:80%;"}

### 2단계: Braze에서 LINE 페이지 설정

1. LINE의 Braze 기술 파트너 페이지로 이동하여 LINE **제공자** 탭에서 확인한 정보를 입력합니다:
   - 공급자 ID
   - 채널 ID
   - 채널 비밀
   - 채널 액세스 토큰

![LINE 메시징 통합 페이지와 LINE 통합 섹션.][3]{: style="max-width:80%;"}

{: start="2"}
2\. 연결 후, Braze는 워크스페이스에 성공적으로 추가된 각 LINE 연동 서비스에 대해 자동으로 Braze 구독 그룹을 생성합니다. <br><br> 팔로워 목록의 모든 변경 사항(예: 새 팔로워 또는 언팔로워)은 자동으로 Braze에 푸시됩니다.

![LINE 구독 그룹 섹션에 'LINE' 채널에 대한 하나의 구독 그룹이 표시됩니다.][4]{: style="max-width:80%;"}

## LINE 계정 유형

| 계정 유형 | 설명 |
| --- | --- |
| 미인증 계정 | 누구나(개인 또는 기업) 얻을 수 있는 검토되지 않은 계정입니다. 이 계정은 회색 배지로 표시되며 LINE 앱 내 검색 결과에 표시되지 않습니다. |
| 인증된 계정 | 라인 야후 심사를 통과한 계정입니다. 이 계정은 파란색 배지로 표시되며 LINE 앱 내 검색 결과에 표시됩니다.<br><br>이 계정은 일본, 대만, 태국, 인도네시아에 소재한 계정만 사용할 수 있습니다.  |
| 프리미엄 계정 | 라인 야후 심사를 통과한 계정입니다. 이 계정은 녹색 배지로 표시되며 LINE 앱 내 검색 결과에 표시됩니다. 이 계정 유형은 LINE의 재량에 따라 심사 과정에서 자동으로 부여됩니다. |
{: .reset-td-br-1 .resest-td-br-2}

## 기존 팔로워를 Braze에 동기화

팔로워를 Braze에 동기화하려면 LINE 계정을 인증하거나 프리미엄 계정을 사용해야 합니다. 계정을 만들면 기본 상태는 확인되지 않습니다. 계정 인증을 요청해야 합니다.

### 인증된 LINE 계정 신청하기

{% alert important %}
인증된 계정은 일본, 대만, 태국, 인도네시아에 소재한 계정만 사용할 수 있습니다.
{% endalert %}

1. LINE **공식 계정** 페이지에서 **설정을** 선택합니다.
2. **정보 공개 확인 상태** 아래에서 **계정 확인 요청을** 선택합니다.
3. 필수 정보를 입력합니다.
4. 검토 결과가 담긴 알림을 기다립니다.

해당 채널이 Braze와 동기화되기 전에 특정 채널을 팔로우한 사용자를 동기화하려면 고객 성공 관리자 또는 계정 관리자에게 [요청하여](https://servicedesk.braze.com/plugins/servlet/desk/portal/12) WhatsApp 팀에 [요청을 제출하세요](https://servicedesk.braze.com/plugins/servlet/desk/portal/12).

## Braze에서 LINE 테스트 사용자 만들기

사용자 조정을 설정하기 전에 LINE 채널을 테스트할 수 있는 방법은 두 가지가 있습니다:

### 라인 세그먼트 참조

1. 계정을 연결한 후 LINE 채널을 팔로우하세요.

2. Braze에서 **세그먼트로** 이동하여 LINE 구독 그룹을 위한 세그먼트를 생성합니다. <br><br>![구독 그룹으로 그룹을 필터링합니다.][5]{: style="max-width:80%;"}<br><br>

3. **사용자 데이터** > **사용자 데이터 CSV 내보내기를** 선택합니다. <br><br>!['가입한 회선'이라는 이름의 세그먼트가 있는 세그먼트 세부정보와 내보내기 옵션 목록이 있는 '사용자 데이터' 메뉴가 표시됩니다.][6]{: style="max-width:80%;"}<br><br>

4. CSV 다운로드에서 `created_at` 필드와 LINE 채널을 팔로우한 시점을 참조하여 사용자를 찾습니다.

5. Braze에서 앱보이 ID를 사용하여 특정 사용자를 검색하고 필요에 따라 수정할 수 있습니다.

### "나는 누구인가" 캔버스 또는 캠페인 만들기

1. 특정 트리거 단어에 대해 사용자의 Braze 사용자 ID를 반환하는 캔버스를 설정합니다. <br><br>트리거 예시 <br><br>![특정 구독 그룹에 인바운드 라인을 보낸 사용자에게 캠페인을 전송하는 트리거입니다.][7]{: style="max-width:80%;"}<br><br>메시지 예시<br><br>![Braze 사용자 ID가 표시된 LINE 메시지입니다.][8]{: style="max-width:40%;"}<br><br>

2. Braze에서는 Braze ID를 사용하여 특정 사용자를 검색하고 필요에 따라 수정할 수 있습니다.

{% alert important %}
캔버스에 글로벌 제어 또는 전송을 방지하는 제어 그룹이 없는지 확인하세요.
{% endalert %}


[1]: {% image_buster /assets/img/line/webhook_settings.png %}
[2]: {% image_buster /assets/img/line/response_settings.png %}
[3]: {% image_buster /assets/img/line/integration.png %}
[4]: {% image_buster /assets/img/line/line_subscription_groups.png %}
[5]: {% image_buster /assets/img/line/filter_group.png %}
[6]: {% image_buster /assets/img/line/csv_export_user_data.png %}
[7]: {% image_buster /assets/img/line/trigger.png %}
[8]: {% image_buster /assets/img/line/message.png %}