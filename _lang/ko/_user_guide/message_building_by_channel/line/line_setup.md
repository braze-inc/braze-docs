---
nav_title: LINE 설정
article_title: LINE 설정
description: "이 문서에서는 선행 조건과 제안된 다음 단계를 포함하여 Braze LINE 채널을 설정하는 방법에 대해 설명합니다."
page_type: partner
search_tag: Partner
page_order: 0
channel:
 - LINE
alias: /line/line_setup/
---


# LINE 설정

> 이 문서에서는 사용자 설정, 사용자 ID 조정, LINE 테스트 사용자 생성 등 Braze에서 LINE 채널을 설정하는 방법에 대해 설명합니다.

## 전제 조건

LINE과 Braze를 통합하려면 다음이 필요합니다:

- [LINE 비즈니스 계정](https://www.linebiz.com/jp-en/manual/OfficialAccountManager/tutorial-steps/?list=7171)
- 프리미엄 또는 인증된 계정 상태(기존 팔로워를 동기화하는 데 필요)
   - [LINE의 계정 가이드라인](https://terms2.line.me/official_account_guideline_oth) 보기
- [LINE 개발자 계정](https://developers.line.biz/en/docs/line-developers-console/login-account/)
- [LINE 메시징 API 채널](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

Braze에서 LINE 메시지를 보내면 계정의 메시지 크레딧이 사용됩니다.

## LINE 계정 유형

| 계정 유형 | 설명 |
| --- | --- |
| 미인증 계정 | 누구나(개인 또는 기업) 얻을 수 있는 검토되지 않은 계정입니다. 이 계정은 회색 배지로 담당자가 표시되며, LINE 앱 내 검색 결과에 표시되지 않습니다. |
| 인증된 계정 | 라인 야후 심사를 통과한 계정입니다. 이 계정은 파란색 배지로 담당자가 표시되며, LINE 앱 내 검색 결과에 표시됩니다.<br><br>이 계정은 일본, 대만, 태국, 인도네시아에 소재한 계정만 사용할 수 있습니다.  |
| 프리미엄 계정 | 라인 야후 심사를 통과한 계정입니다. 이 계정은 녹색 배지로 담당자가 표시되며, LINE 앱 내 검색 결과에 표시됩니다. 이 계정 유형은 LINE의 재량에 따라 심사 과정에서 자동으로 부여됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 필수 계정 유형

팔로워를 Braze에 동기화하려면 LINE 계정을 인증하거나 프리미엄 계정을 사용해야 합니다. 계정을 만들면 기본값이 확인되지 않은 상태로 유지됩니다. 계정 인증을 요청해야 합니다.

### 인증된 LINE 계정 신청하기

{% alert important %}
인증된 계정은 일본, 대만, 태국, 인도네시아에 소재한 계정만 사용할 수 있습니다.
{% endalert %}

1. LINE **공식 계정** 페이지에서 **설정을** 선택합니다.
2. **정보 공개 확인 상태** 아래에서 **계정 확인 요청을** 선택합니다.
3. 필수 정보를 입력합니다.
4. 검토 결과가 담긴 알림을 기다립니다.

## LINE 통합

일관된 사용자 업데이트를 설정하려면 기존 사용자의 LINE ID를 가져와서 모두 LINE의 구독 상태에 동기화하세요:

1. [기존 알려진 사용자 가져오기 또는 업데이트하기](#step-1-import-or-update-existing-line-users)
2. [LINE 채널 통합하기](#step-2-integrate-line-channel)
3. [사용자 ID 조정하기](#step-3-reconcile-user-ids)
4. [사용자 업데이트 방법 변경](#step-4-change-your-user-update-methods)
5. [(선택 사항) 고객 프로필 병합하기](#step-5-merge-profiles-optional)

## 1단계: 기존 LINE 사용자 가져오기 또는 업데이트하기

이 단계는 기존에 식별된 LINE 사용자가 있는 경우 반드시 필요한데, 나중에 Braze가 자동으로 구독 상태를 가져와 올바른 고객 프로필을 업데이트하기 때문입니다. 이전에 LINE ID로 사용자를 조정하지 않았다면 이 단계를 건너뛰세요. 

사용자 가져오기 또는 업데이트는 Braze에서 지원하는 방법 중 하나를 사용하여 수행할 수 있습니다. [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 엔드포인트, [CSV 가져오기]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) 또는 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/cloud_ingestion/). 

어떤 방법을 사용하든 `native_line_id` 을 업데이트하여 사용자의 LINE ID를 제공하세요. 자세한 내용은 `native_line_id`, [사용자 설정을](#user-setup) 참조하세요.

{% alert note %}
구독 그룹 상태는 지정하지 않으면 무시됩니다. LINE은 사용자 구독 상태의 출처이며, 구독 동기화 도구를 통해 또는 이벤트 업데이트를 통해 Braze에 동기화됩니다.
{% endalert %}

## 2단계: LINE 채널 통합하기

통합 프로세스가 완료되면 해당 채널의 LINE 팔로워를 자동으로 Braze로 가져옵니다. 이미 Braze 고객 프로필과 연결된 LINE ID의 경우 각 프로필이 '가입함' 상태로 업데이트되며, 나머지 LINE ID는 익명 사용자를 생성합니다. 또한, LINE 채널의 신규 팔로워가 채널을 팔로우하면 신원이 확인되지 않은 고객 프로필이 생성됩니다.

### 2.1단계: 웹훅 설정 편집하기

1. LINE에서 **메시징 API** 탭으로 이동하여 **웹훅 설정을** 편집합니다:
   - **웹훅 URL을** `https://anna.braze.com/line/events` 으로 설정합니다.
      - 통합 시 대시보드 클러스터에 따라 Braze가 자동으로 다른 URL로 변경합니다.
   - **웹훅 사용** 및 **웹훅 재전송을** 켭니다. <br><br> 웹훅 설정 페이지에서 '웹훅 사용', '웹훅 재전송', '오류 통계 집계'를 토글하여 웹훅 URL을 확인하거나 편집할 수 있습니다.]({% image_buster /assets/img/line/webhook_settings.png %}){: style="max-width:70%;"}
2. **공급자** 탭에서 다음 정보를 기록해 두세요:

| 정보 유형 | 위치 |
| --- | --- |
| 제공자 ID | 제공업체를 선택한 다음 **\*설정** > **기본 정보로** 이동합니다. |
| 채널 ID | 제공업체를 선택한 다음 **채널** > 내 채널 > **기본 설정으로** 이동합니다. |
| 채널 비밀 | 제공업체를 선택한 다음 **채널** > 내 채널 > **기본 설정으로** 이동합니다. |
| 채널 액세스 토큰 | 제공업체를 선택한 다음 **채널** > 내 채널 > **메시징** 채널 > **메시징 API로** 이동합니다. 채널 액세스 토큰이 없는 경우에는 **이슈를** 선택합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="3"}
3\. **설정** 페이지 > **응답 설정으로** 이동하여 다음을 수행합니다:
   - **인사말 메시지를** 끕니다. 이는 팔로우 시 트리거를 통해 Braze에서 처리할 수 있습니다.
   - **자동 응답 메시지를** 끕니다. 트리거된 모든 메시징은 Braze를 통해 이루어져야 합니다. 그렇다고 해서 LINE 콘솔에서 직접 전송하는 것을 막지는 않습니다.
   - **웹훅을** 켭니다.

계정에서 채팅을 처리하는 방식에 대한 토글이 있는 응답 설정 페이지입니다.]({% image_buster /assets/img/line/response_settings.png %}){: style="max-width:80%;"}

### 2.2단계: Braze에서 LINE 구독 그룹 생성하기

1. LINE의 Braze 기술 파트너 페이지로 이동하여 LINE **파트너** 탭에서 입력한 정보를 입력합니다:
   - 제공자 ID
   - 채널 ID
   - 채널 비밀
   - 채널 액세스 토큰

LINE 계정에 IP 화이트리스트를 추가하려면 [IP 허용]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-allowlisting) 목록에 클러스터에 등록된 모든 IP 주소를 허용 목록에 추가하세요.

{% alert important %}
통합하는 동안 채널 비밀 번호가 올바른지 확인하세요. 올바르지 않은 경우 구독 상태에 불일치가 있을 수 있습니다.
{% endalert %}

LINE 메시징 통합 페이지로 이동합니다.]({% image_buster /assets/img/line/integration.png %}){: style="max-width:80%;"}

{: start="2"}
2\. 연결 후, 작업 영역에 성공적으로 추가된 각 LINE 통합에 대해 Braze 구독 그룹이 자동으로 생성됩니다. <br><br> 팔로워 목록의 모든 변경사항(예: 새 팔로워 또는 언팔로워)은 자동으로 Braze에 푸시됩니다.

LINE 구독 그룹 섹션에 'LINE' 채널에 대한 하나의 구독 그룹이 표시됩니다.]({% image_buster /assets/img/line/line_subscription_groups.png %}){: style="max-width:80%;"}

## 3단계: 사용자 ID 조정하기

[사용자 ID 조정의](#user-id-reconciliation) 단계에 따라 사용자의 LINE ID를 기존 Braze 사용자 프로필과 결합하세요.

## 4단계: 사용자 업데이트 방법 변경 

이미 Braze에 사용자 업데이트를 제공하는 메서드가 있다고 가정할 때, 새 필드 `native_line_id` 를 포함하도록 업데이트해야 이후 Braze로 전송되는 사용자 업데이트에 해당 필드가 포함됩니다.

구독 상태 동기화 프로세스의 일부로 생성되었거나 새 팔로워가 내 채널을 팔로우할 때 생성된 `native_line_id` 주소의 확인되지 않은 고객 프로필이 Braze에 존재할 수 있습니다. 

[사용자 조정](#user-id-reconciliation) 등을 통해 애플리케이션에서 LINE 사용자를 식별한 경우, 확인되지 않은 잠재적 고객 프로필을 Braze의 [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) 엔드포인트. `native_line_id` 이 있는 모든 미확인 사용자 프로필에는 식별할 사용자 프로필을 타겟팅하는 데 사용할 수 있는 사용자 별칭 `line_id` 도 있습니다.

`/users/identify` 다음은 `line_id` 이라는 사용자 별칭 지정으로 미확인 고객 프로필을 타겟팅하는 페이로드의 예시입니다: 

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

제공한 `external_id` 에 대한 기존 고객 프로필이 없는 경우 미확인 고객 프로필에 추가되어 식별됩니다. `external_id` 에 대한 고객 프로필이 존재하는 경우 미확인 고객 프로필에만 있는 모든 속성이 `native_line_id` 및 사용자의 구독 상태를 포함하여 알려진 고객 프로필에 복사됩니다.

애플리케이션에서 알려진 LINE 사용자를 업데이트할 수 있습니다. [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 엔드포인트에 외부 식별자와 `native_line_id` 를 전달하여 업데이트할 수 있습니다. 사용자에 대한 미확인 고객 프로필이 이미 존재하고 `/users/track` 을 통해 동일한 `native_line_id` 이 다른 사용자 프로필에 추가되는 경우 미확인 고객 프로필의 모든 구독 상태가 상속됩니다. 그러나 동일한 `native_line_id` 으로 중복된 고객 프로필이 존재할 수 있습니다. 이후 이벤트 업데이트에 따른 구독 업데이트는 모든 프로필을 그에 따라 업데이트합니다. 

다음은 외부 사용자 ID로 고객 프로필을 업데이트하여 `native_line_id` 을 추가하는 `/users/track` 페이로드 예시입니다: 

{% raw %}
```json
{
   "attributes": [
       {
           "external_id": "known_external_id_from_your_application",
           "native_line_id": "U89f4a626548ccd48482f529a482f138b",
           "other": "attribute"
       }
   ]
}
```
{% endraw %}

## 5단계: 프로필 병합(선택 사항)

위에서 설명한 것처럼 동일한 `native_line_id` 에 여러 개의 고객 프로필이 존재할 수 있습니다. 업데이트 방법으로 중복된 고객 프로필이 생성되는 경우 `/user/merge` 엔드포인트를 사용하여 식별되지 않은 사용자 프로필을 식별된 사용자 프로필에 병합할 수 있습니다. 

`/users/merge` 다음은 사용자 별칭 지정 `line_id` 으로 미확인 고객 프로필을 타겟팅하는 페이로드 예시입니다:

{% raw %}
```json
{
 "merge_updates": [
   {
     "identifier_to_merge": {
       "user_alias": {
         "alias_name": "U89f4a626548ccd48482f529a482f138b",
         "alias_label": "line_id"
       }
     },
     "identifier_to_keep": {
       "external_id": "known_external_id_from_your_application"
     }
   }
 ]
}
```
{% endraw %}

{% alert tip %}
Braze에서 중복 사용자 관리에 대해 자세히 알아보려면 [중복 사용자를]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users) 참조하세요.
{% endalert %}

## 사용자 설정

LINE은 사용자 구독 상태에 대한 진실의 원천입니다. 사용자의 LINE ID(`native_line_id`)가 있더라도 해당 사용자가 보내는 LINE 채널을 팔로우하지 않는다면, LINE은 해당 사용자에게 메시지를 전달하지 않습니다.

이를 관리하기 위해 Braze는 LINE 팔로우 및 언팔로우를 위한 구독 동기화, 이벤트 업데이트 등 잘 통합된 사용자 기반을 지원하는 툴과 로직을 제공합니다.

### 구독 동기화 및 이벤트 로직

1. **구독 동기화 도구:** 이 도구는 LINE 채널 통합이 성공적으로 완료되면 자동으로 배포됩니다. 이를 사용하여 기존 프로필을 업데이트하고 새 프로필을 만들 수 있습니다.<br><br>LINE 채널을 팔로우하는 `native_line_id` 이 있는 모든 Braze 고객 프로필은 구독 그룹 상태가 `subscribed` 으로 업데이트됩니다. 라인 채널의 팔로워 중 Braze 고객 프로필( `native_line_id` )이 없는 사람은 누구나 가입할 수 있습니다:<br><br>\- 채널 다음에 사용자 LINE ID를 `native_line_id` 로 설정하여 생성한 익명 사용자 프로필입니다. <br>\- 채널 다음에 사용자 별칭 `line_id` 을 사용자 LINE ID로 설정합니다. <br>\- 구독 그룹 상태는 다음과 같습니다. `subscribed`

{: start="2"}
2\. **이벤트 업데이트:** 이는 사용자의 구독 상태를 업데이트하는 데 사용됩니다. 통합된 LINE 채널에 대한 사용자 이벤트 업데이트를 Braze가 수신하고 해당 이벤트가 팔로우인 경우, 고객 프로필의 구독 그룹 상태는 `subscribed` 입니다. 이벤트가 언팔로우인 경우 고객 프로필의 구독 그룹 상태는 `unsubscribed` 입니다.<br><br>\- 일치하는 모든 Braze 고객 프로필( `native_line_id` )이 자동으로 업데이트됩니다. <br>\- 이벤트에 대해 일치하는 고객 프로필이 없는 경우 Braze는 [익명 사용자를 생성합니다]({{site.baseurl}}/line/user_management/).

## 사용 사례

다음은 위의 설정 단계를 따른 후 사용자를 업데이트하는 방법의 사용 사례입니다.

##### 기존 Braze 고객 프로필이 이미 LINE 채널을 팔로우하고 있습니다.

1. Braze 고객 프로필은 `native_line_id` 속성으로 업데이트됩니다. 기본값 구독 상태는 `unsubscribed` 입니다.
2. 구독 동기화 도구를 실행하여 사용자가 LINE 채널을 팔로우하고 있는지 확인한 후 고객 프로필을 구독 상태 `subscribed` 로 업데이트합니다.
3. 사용자가 채널을 차단, 언팔로우, 리피로우하는 등 구독 상태에 변화가 발생하면 Braze는 LINE으로부터 업데이트를 수신하고 그에 따라 고객 프로필을 `native_line_id` 으로 업데이트합니다.

##### 기존 고객 프로필에 LINE 채널이 차단, 언팔로우 또는 언팔로우된 경우 

1. Braze 고객 프로필은 `native_line_id` 속성으로 업데이트됩니다. 기본값 구독 상태는 `unsubscribed` 입니다.
2. 구독 동기화 도구에서 사용자가 LINE 채널을 팔로우하고 있는 것으로 확인되지 않고 사용자의 구독 상태가 `unsubscribed` 로 유지됩니다.
3. 사용자가 나중에 해당 채널을 팔로우하면 Braze는 LINE에서 업데이트를 수신하고 고객 프로필을 구독 상태로 업데이트합니다 `subscribed`.

##### 고객 프로필 생성은 LINE 팔로우 후 발생합니다.

1. 채널에 새로운 LINE 팔로워가 생깁니다.
2. Braze는 `native_line_id` 속성을 팔로워의 LINE ID로 설정하고 사용자 별칭 `line_id` 을 팔로워의 LINE ID로 설정한 익명 사용자 프로필을 생성합니다. 프로필의 구독 상태는 `subscribed` 입니다.
3. 사용자는 [사용자 조정을](#user-id-reconciliation) 통해 LINE ID를 보유한 것으로 식별됩니다.
  - 익명 사용자 프로필은 다음을 사용하여 식별할 수 있습니다. [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) 엔드포인트. 이 사용자 프로필에 대한 후속 업데이트( [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 엔드포인트, [CSV 가져오기]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) 또는 [클라우드 데이터 수집을]({{site.baseurl}}/user_guide/data/cloud_ingestion/) 통한) 이 고객 프로필에 대한 후속 업데이트는 `external_id` 으로 알려진 사용자를 타겟팅할 수 있습니다.

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

  - 새 고객 프로필을 생성할 수 있습니다( [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 엔드포인트, [CSV 가져오기]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) 또는 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/cloud_ingestion/))을 설정하여 `native_line_id`. 이 새 프로필은 기존 익명 사용자 프로필의 구독 상태 상태를 상속합니다. 이렇게 하면 여러 프로필이 동일한 `native_line_id` 을 공유하게 됩니다. [5단계에](#step-5-merge-profiles-optional) 설명된 프로세스에서 `/users/merge` 엔드포인트를 사용하여 언제든지 병합할 수 있습니다.

##### 고객 프로필 생성은 LINE 팔로우 전에 이루어집니다.

1. 새 사용자를 확보하고 해당 정보를 Braze에 보냅니다. 새 고객 프로필이 생성됩니다(프로필 1).
2. 사용자가 LINE 계정을 팔로우합니다.
3. Braze가 팔로우 이벤트를 수신하고 익명 사용자 프로필(프로필 2)을 생성합니다.
4. 사용자는 [사용자 조정을](#user-id-reconciliation) 통해 LINE ID를 보유한 것으로 식별됩니다.
5. 프로필 1을 업데이트하여 `native_line_id` 속성을 설정합니다. 이 프로필은 프로필 2의 구독 상태 상태를 상속합니다.
  - 이제 동일한 `native_line_id` 을 가진 두 개의 고객 프로필이 있습니다. [5단계에](#step-5-merge-profiles-optional) 설명된 프로세스에서 `/users/merge` 엔드포인트를 사용하여 언제든지 병합할 수 있습니다.

## 사용자 ID 조정 

사용자가 채널을 팔로우하거나 일회성 '팔로워 동기화' 워크플로우를 사용할 때 라인 ID가 자동으로 Braze에 수신됩니다. 또한 LINE ID는 사용자가 팔로우하는 채널에 따라 달라지기 때문에 사용자가 자신의 LINE ID를 제공할 가능성은 낮습니다.

LINE ID와 기존 Braze 고객 프로필을 결합하는 방법은 두 가지가 있습니다:

- [LINE 로그인](#line-login)
- [사용자 계정 연결](#user-account-linking)

### LINE 로그인

이 방법은 조정을 위해 소셜 미디어 로그인을 사용합니다. 사용자가 앱에 로그인하면 [LINE 로그인을](https://developers.line.biz/en/docs/line-login/overview/) 사용하여 사용자 계정을 만들거나 로그인할 수 있는 옵션이 제공됩니다.

{% alert note %}
각 사용자에 대한 올바른 LINE ID를 얻으려면, Braze 통합 LINE 공식 계정 또는 채널과 동일한 제공업체에서 LINE 로그인을 설정하세요.
{% endalert %}

1. LINE 개발자 콘솔로 이동하여 LINE 로그인을 통해 앱에 로그인하는 [사용자의 이메일 주소를 가져올 수 있는 권한을 요청하세요](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission).

2. LINE에서 제공하는 적절한 단계에 따라 LINE 로그인을 구현하세요:<br><br>
  - [웹 앱 길 찾기](https://developers.line.biz/en/docs/line-login/integrate-line-login/)
  - [기본 앱 길 찾기](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-openid-to-register-new-users)<br><br>인증 요청을 위해 설정한 [범위에](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes) `email` 을 포함해야 합니다. 

{: start="3"}
3\. [ID 확인 토큰 호출을](https://developers.line.biz/en/reference/line-login/#verify-id-token) 사용하여 사용자의 이메일을 획득합니다. 

4. 데이터베이스에 있는 일치하는 이메일과 함께 사용자의 LINE ID(`native_line_id`)를 사용자 프로필에 저장하거나 사용자의 이메일과 LINE ID로 새 사용자 프로필을 생성합니다.

5. [`/user/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users/), [CSV 가져오기]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) 또는 [클라우드 데이터 수집을]({{site.baseurl}}/user_guide/data/cloud_ingestion/) 사용하여 신규 또는 업데이트된 사용자 정보를 Braze로 전송하세요.

#### 워크플로

##### 기존 팔로워가 LINE 로그인을 사용하는 경우

**시나리오:** 익명 사용자는 초기 가입자 동기화 중 또는 '팔로우' 이벤트를 통해 통합된 후에 생성됩니다.

1. 사용자가 LINE 로그인을 사용하여 앱에 로그인합니다.
2. LINE은 사용자의 이메일을 제공합니다.
3. 업데이트된 사용자(기존 사용자 프로필에 해당 이메일을 첨부하여 LINE ID를 추가)를 Braze에 보내거나 익명 사용자를 이메일로 업데이트합니다.

##### 신규 팔로워가 LINE 로그인 사용

**시나리오:** 사용자의 LINE ID로 Braze에 고객 프로필이 존재하지 않습니다.

1. 사용자가 LINE 로그인을 사용하여 앱에 로그인합니다.
2. LINE은 사용자의 이메일을 제공합니다.
3. 여러분도 마찬가지입니다:
  - 해당 이메일로 기존 고객 프로필을 업데이트하여 해당 사용자의 LINE ID를 추가합니다.
  - 이메일과 LINE ID로 새 고객 프로필을 만듭니다.
4. 사용자가 LINE 공식 계정을 팔로우하면 Braze는 팔로우 이벤트를 수신하고 사용자의 구독 상태를 `subscribed` 로 업데이트합니다.

### 사용자 계정 연결 

이 방법을 사용하면 사용자가 LINE 계정을 앱의 사용자 계정에 연결할 수 있습니다. 그런 다음, 예를 들어 {% raw %}`{{line_id}}`{% endraw %} 와 같이 Braze에서 Liquid를 사용하여 사용자의 LINE ID를 웹사이트나 앱에 전달하는 개인화된 URL을 생성하고, 이를 통해 알려진 사용자와 연결할 수 있습니다.

1. 가입 상태 변화를 기반으로 사용자가 LINE 채널에 가입할 때 트리거되는 동작 기반 캔버스를 만들어 보세요.<br>사용자가 LINE 채널에 가입할 때 트리거되는 캔버스입니다.]({% image_buster /assets/img/line/account_link_1.png %})
2. 사용자가 웹사이트나 앱에 로그인하도록 유도하는 메시지를 작성하여 사용자의 LINE ID를 쿼리 파라미터로 전달합니다(예: Liquid를 통해):

```
Thanks for following Flash n' Thread on LINE! For personalized offers and 20% off your next purchase, sign-in to your account: https://flashandthread.com/sign_in?line_user_id={{line_id}}
```

{: start="3"}
3\. 쿠폰 코드를 전달하는 후속 메시지를 생성합니다.
4\. (선택 사항) LINE 사용자가 식별되면 쿠폰 코드를 전송하는 동작 기반 캠페인 또는 캔버스를 생성하여 사용자에게 쿠폰 코드를 전송합니다. <br>LINE 사용자가 식별되면 트리거되는 액션 기반 캠페인입니다.]({% image_buster /assets/img/line/account_link_2.png %})

#### 작동 방식

사용자가 로그인한 후 웹사이트나 앱에서 사용자 ID를 다시 Braze로 전송하여 URL의 일부로 전달된 LINE ID와 연결되도록 변경합니다(예시 코드: 다음과 같은 코드):

```json
const currentUrl = new URL(window.location.href)
const queryParams = new URLSearchParams(currentUrl.search);
const lineUserId = queryParams.get("line_user_id")

if (user && isLoggedIn && lineUserId) {
  post(
   "https://rest.iad-03.braze.com	/users/identify",
   {
     "aliases_to_identify": [
       {
   "external_id": user.getUserId(),
   "user_alias": {
     "alias_name": lineUserId,
     "alias_label": "line_id"
   }
 }
      ]
    }
  )
  braze.logCustomEvent("identified_line_user_for_promotion");
}
```

#### 워크플로

##### 기존 사용자가 내 LINE 채널을 팔로우하는 경우

**시나리오:** Braze의 기존 사용자가 LINE에서 내 채널을 팔로우하고 있습니다.

1. LINE에서 Braze에게 팔로우 이벤트를 보냅니다.
2. Braze는 LINE ID, `line_id` 사용자 별칭 지정, LINE 구독 그룹 상태 `subscribed` 로 익명 사용자 프로필을 생성합니다.
3. 사용자는 웹사이트와 앱으로 연결되는 링크가 포함된 LINE 메시지를 수신하고 로그인합니다. 이제 고객 프로필을 알 수 있습니다.
4. 생성된 익명 사용자 프로필이 식별되고 [/users/identify 엔드포인트를]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) 통해 사용자의 알려진 사용자 프로필에 병합됩니다. 이제 알려진 고객 프로필에 LINE ID가 포함되고 가입 상태는 `subscribed` 입니다.
5. (선택 사항) 사용자는 쿠폰 코드가 포함된 LINE 메시지를 수신하고, Braze는 전송 내용을 Braze 고객 프로필에 기록합니다.

## Braze에서 LINE 테스트 사용자 생성하기

[사용자 조정을](#user-id-reconciliation) 설정하기 전에 '나는 누구인가' 캔버스 또는 캠페인을 생성하여 LINE 채널을 테스트할 수 있습니다.

1. 특정 트리거 단어에 대해 사용자의 Braze 사용자 ID를 반환하는 캔버스를 설정합니다. <br><br>트리거 예시 <br><br>특정 구독 그룹에 인바운드 라인을 보낸 사용자에게 캠페인을 전송하는 트리거입니다.]({% image_buster /assets/img/line/trigger.png %}){: style="max-width:80%;"}<br><br>메시지 예시<br><br>Braze 사용자 ID가 표시된 LINE 메시지.]({% image_buster /assets/img/line/message.png %}){: style="max-width:40%;"}<br><br>

2. Braze에서는 Braze ID를 사용하여 특정 사용자를 검색하고 필요에 따라 수정할 수 있습니다.

{% alert important %}
캔버스에 전송을 차단하는 글로벌 컨트롤 그룹이나 대조군이 없는지 확인하세요.
{% endalert %}


