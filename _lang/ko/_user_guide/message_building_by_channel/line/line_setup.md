---
nav_title: LINE 설정
article_title: LINE 설정
description: "이 문서에서는 사전 요구 사항과 제안된 다음 단계를 포함하여 Braze LINE 채널을 설정하는 방법을 설명합니다."
page_type: partner
search_tag: Partner
page_order: 0
channel:
 - LINE
alias: /line/line_setup/
---


# LINE 설정

> 이 문서에서는 사용자 설정, 사용자 ID 조정, Braze에서 LINE 테스트 사용자 생성 등 Braze에서 LINE 채널을 설정하는 방법에 대해 설명합니다.

## 필수 조건

LINE과 Braze를 연동하려면 다음이 필요합니다:

- [LINE 비즈니스 계정](https://www.linebiz.com/jp-en/manual/OfficialAccountManager/tutorial-steps/?list=7171)
- 프리미엄 또는 인증된 계정 상태(기존 팔로워 동기화에 필요)
   - [LINE의 계정 가이드라인](https://terms2.line.me/official_account_guideline_oth) 보기
- [LINE 개발자 계정](https://developers.line.biz/en/docs/line-developers-console/login-account/)
- [LINE 메시징 API 채널](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

브레이즈에서 LINE 메시지를 보내면 귀하의 계정의 메시지 크레딧이 차감됩니다.

## LINE 계정 유형

| 계정 유형 | 설명 |
| --- | --- |
| 미인증 계정 | 누구나(개인 또는 기업) 얻을 수 있는 검토되지 않은 계정입니다. 이 계정은 회색 배지로 표시되며 LINE 앱 내 검색 결과에 표시되지 않습니다. |
| 인증된 계정 | 라인 야후 심사를 통과한 계정입니다. 이 계정은 파란색 배지로 표시되며 LINE 앱 내 검색 결과에 표시됩니다.<br><br>이 계정은 일본, 대만, 태국, 인도네시아에 소재한 계정만 사용할 수 있습니다.  |
| 프리미엄 계정 | 라인 야후 심사를 통과한 계정입니다. 이 계정은 녹색 배지로 표시되며 LINE 앱 내 검색 결과에 표시됩니다. 이 계정 유형은 LINE의 재량에 따라 심사 과정에서 자동으로 부여됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 필수 계정 유형

팔로워를 Braze에 동기화하려면 LINE 계정을 인증하거나 프리미엄 계정을 사용해야 합니다. 계정을 만들면 기본 상태는 확인되지 않습니다. 계정 인증을 요청해야 합니다.

### 인증된 LINE 계정 신청하기

{% alert important %}
인증된 계정은 일본, 대만, 태국, 인도네시아에 소재한 계정만 사용할 수 있습니다.
{% endalert %}

1. LINE **공식 계정** 페이지에서 **설정을** 선택합니다.
2. **정보 공개 확인 상태** 아래에서 **계정 확인 요청**을 선택합니다.
3. 필수 정보를 입력합니다.
4. 검토 결과가 담긴 알림을 기다립니다.

## 라인 통합

일관된 사용자 업데이트를 설정하려면 기존 사용자의 LINE ID를 가져오고 이를 모두 LINE의 구독 상태와 동기화하십시오.

1. 기존의 알려진 사용자를 가져오거나 업데이트합니다.
2. LINE 채널 통합
3. [사용자 ID 조정](#step-3-reconcile-user-ids)
4. [사용자 업데이트 방법 변경](#step-4-change-your-user-update-methods)
5. [사용자 프로필 병합(선택 사항)](#step-5-merge-profiles-optional)

## 1단계: 기존 LINE 사용자를 가져오거나 업데이트합니다.

이 단계는 기존의 식별된 LINE 사용자가 있는 경우 필요합니다. Braze는 나중에 자동으로 그들의 구독 상태를 가져오고 올바른 고객 프로필을 업데이트합니다. 이전에 사용자를 LINE ID와 조정하지 않았다면 이 단계를 건너뛰십시오. 

You can import or update users using any of the methods that Braze supports, including the [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint, [CSV import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import), or [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/). 

사용하는 방법에 관계없이, 사용자의 LINE ID를 제공하기 위해 <1>를 업데이트하십시오. 더 알아보려면 사용자 설정을 참조하세요.

{% alert note %}
구독 그룹 상태는 지정되지 않아야 하며 무시됩니다. LINE은 사용자 구독 상태의 진실의 원천이며, 이는 구독 동기화 도구 또는 이벤트 업데이트를 통해 Braze와 동기화됩니다.
{% endalert %}

## 2단계: LINE 채널 통합

통합 프로세스가 완료되면, Braze는 자동으로 해당 채널의 LINE 팔로워를 Braze로 가져옵니다. Braze 사용자 프로필과 이미 연결된 모든 LINE ID에 대해 각 프로필은 "구독됨" 상태로 업데이트되며, 남아 있는 LINE ID는 익명 사용자를 생성합니다. 또한, 귀하의 LINE 채널의 새로운 팔로워는 채널을 팔로우할 때 식별되지 않은 사용자 프로필이 생성됩니다.

### 2.1 단계: 편집 웹훅 설정

1. LINE에서 **메시징 API** 탭으로 이동하여 **웹훅 설정을** 편집합니다:
   - **웹훅 URL을** `https://anna.braze.com/line/events` 으로 설정합니다.
      - Braze는 통합 시 대시보드 클러스터에 따라 자동으로 이 URL을 다른 URL로 변경합니다.
   - **웹훅 사용** 및 **웹훅 재전송**을 켭니다. <br><br> ![웹훅 설정 페이지에서 "웹훅 사용", "웹훅 재전송" 및 "오류 통계 집계"를 켜거나 끄면서 웹훅 URL을 확인하거나 편집할 수 있습니다.][1]{: style="max-width:70%;"}
2. **제공업체** 탭에서 다음 정보를 참고하세요:

| 정보 유형 | 위치 |
| --- | --- |
| 공급자 ID | 제공업체를 선택한 다음 **\*설정** > **기본 정보로** 이동합니다. |
| 채널 ID | 제공업체를 선택한 다음 **채널** > 내 채널 > **기본 설정으로** 이동합니다. |
| 채널 비밀 | 제공자를 선택한 다음 **채널** > 귀하의 채널 > **기본 설정**로 이동하십시오. |
| 채널 액세스 토큰 | 제공업체를 선택한 다음 **채널** > 내 채널 > **메시징 API로** 이동합니다. 채널 액세스 토큰이 없는 경우 **이슈**를 선택합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="3"}
3\. **설정** 페이지 > **응답 설정으로** 이동하여 다음을 수행합니다:
   - **인사말 메시지**를 끕니다. 이는 팔로우 시 트리거를 통해 Braze에서 처리할 수 있습니다.
   - **자동 응답 메시지**를 끕니다. 트리거된 모든 메시징은 Braze를 통해 이루어져야 합니다. 그렇다고 해서 LINE 콘솔에서 직접 전송하는 것을 막지는 않습니다.
   - **웹훅**을 켭니다.

![응답 설정 페이지에서 계정에서 채팅을 처리하는 방법에 대한 토글을 설정할 수 있습니다.][2]{: style="max-width:80%;"}

### 2.2 단계: Braze에서 LINE 구독 그룹 생성

1. LINE의 Braze 기술 파트너 페이지로 이동하여 LINE **제공자** 탭에서 확인한 정보를 입력합니다:
   - 공급자 ID
   - 채널 ID
   - 채널 비밀
   - 채널 액세스 토큰

{% alert important %}
통합 중에 채널 비밀이 올바른지 확인하십시오. 잘못된 경우 구독 상태에 불일치가 있을 수 있습니다.
{% endalert %}

![LINE 메시징 통합 페이지와 LINE 통합 섹션.][3]{: style="max-width:80%;"}

{: start="2"}
2\. 연결 후, Braze는 워크스페이스에 성공적으로 추가된 각 LINE 연동 서비스에 대해 자동으로 Braze 구독 그룹을 생성합니다. <br><br> 팔로워 목록의 모든 변경 사항(예: 새 팔로워 또는 언팔로워)은 자동으로 Braze에 푸시됩니다.

![LINE 구독 그룹 섹션에 'LINE' 채널에 대한 하나의 구독 그룹이 표시됩니다.][4]{: style="max-width:80%;"}

## 3단계: 사용자 ID 조정

사용자의 LINE ID를 기존 Braze 사용자 프로필과 결합하려면 사용자 ID 조정의 단계를 따르십시오.

## 4단계: 사용자 업데이트 방법을 변경하세요. 

Braze에 사용자 업데이트를 제공하는 방법이 이미 있다고 가정하면, 이후 Braze에 전송되는 사용자 업데이트에 해당 필드가 포함되도록 새 필드를 포함하도록 업데이트해야 합니다.

Braze에서 구독 상태 동기화 프로세스의 일환으로 생성되었거나 새로운 팔로워가 귀하의 채널을 팔로우할 때 생성된 식별되지 않은 사용자 프로필이 존재할 수 있습니다. 

LINE 사용자가 사용자 조정 또는 기타 수단을 통해 귀하의 애플리케이션에서 식별되면, 엔드포인트를 사용하여 Braze에서 잠재적인 미식별 고객 프로필을 타겟팅할 수 있습니다. 모든 식별되지 않은 고객 프로필은 또한 사용자를 식별하기 위해 고객 프로필을 타겟팅하는 데 사용할 수 있는 사용자 별칭이 있습니다.

여기 사용자 별칭으로 식별되지 않은 고객 프로필을 대상으로 하는 예제 페이로드가 있습니다. 

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

제공된 사용자 프로필이 존재하지 않으면, 이는 식별되지 않은 사용자 프로필에 추가되어 식별됩니다. 사용자 프로필이 존재하는 경우, 확인되지 않은 사용자 프로필에만 있는 모든 속성이 알려진 사용자 프로필로 복사됩니다. 여기에는  및 사용자의 구독 상태가 포함됩니다.

귀하의 애플리케이션에서 알려진 LINE 사용자에게 외부 식별자를 전달하여 엔드포인트를 통해 업데이트할 수 있습니다. 사용자에 대한 식별되지 않은 사용자 프로필이 이미 존재하고 동일한 프로필이 다른 사용자 프로필에 추가되면, 식별되지 않은 사용자 프로필의 모든 구독 상태를 상속받습니다. 그러나 중복 사용자 프로필이 동일하게 존재할 것입니다. 이후의 구독 업데이트는 이벤트 업데이트로부터 모든 프로필을 적절히 업데이트합니다. 

여기 외부 사용자 ID로 사용자 프로필을 업데이트하여 추가하는 예제 페이로드가 있습니다: 

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

## 5단계: 프로필 병합 (선택 사항)

위에서 설명한 바와 같이, 동일한 `native_line_id`을 가진 여러 사용자 프로필이 존재할 가능성이 있습니다. 업데이트 방법이 중복 사용자 프로필을 생성하는 경우, 엔드포인트를 사용하여 식별되지 않은 사용자 프로필을 식별된 사용자 프로필로 병합할 수 있습니다. 

다음은 사용자 별칭으로 식별되지 않은 사용자 프로필을 대상으로 하는 예제 페이로드입니다.

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
중복 사용자를 관리하는 방법에 대해 더 알아보려면 Braze에서 중복 사용자 항목을 참조하세요.
{% endalert %}

## 사용자 설정

LINE은 사용자 구독 상태에 대한 진실의 원천입니다. 사용자의 LINE ID가 있더라도 (), 해당 사용자가 당신이 보내는 LINE 채널을 팔로우하지 않았다면, LINE은 사용자에게 메시지를 전달하지 않습니다.

이것을 관리하는 데 도움을 주기 위해, Braze는 구독 동기화 및 LINE 팔로우 및 언팔로우에 대한 이벤트 업데이트를 포함하여 잘 통합된 사용자 기반을 지원하는 도구 및 논리를 제공합니다.

### 구독 동기화 및 이벤트 로직

1. 구독 동기화 도구: 이 도구는 성공적인 LINE 채널 통합 후 자동으로 배포됩니다. 기존 프로필을 업데이트하고 새로운 프로필을 생성하는 데 사용하세요.<br><br>모든 Braze 사용자 프로필은 LINE 채널을 따르는 경우 구독 그룹 상태가 업데이트됩니다. LINE 채널의 모든 팔로워는 Braze 고객 프로필이 없으면 다음과 같은 혜택을 받게 됩니다:<br><br>\- 익명 사용자 프로필이 채널을 따라 사용자 LINE ID로 설정되어 생성되었습니다. <br>\- 사용자 별칭이 채널에 따라 사용자 LINE ID로 설정됨 <br>구독 그룹 상태의 

{: start="2"}
2\. 이벤트 업데이트: 이것들은 사용자의 구독 상태를 업데이트하는 데 사용됩니다. LINE 채널과 통합된 사용자 이벤트 업데이트를 Braze가 수신할 때 이벤트가 팔로우인 경우, 고객 프로필은 구독 그룹 상태를 가집니다. 이벤트가 언팔로우인 경우, 고객 프로필은 구독 그룹 상태가 가질 것입니다.<br><br>모든 Braze 사용자 프로필이 일치하는  자동으로 업데이트됩니다. <br>\- 이벤트에 대한 일치하는 사용자 프로필이 없으면, Braze는 [익명 사용자]({{site.baseurl}}/line/user_management/)를 생성합니다.

## 사용 사례

이것은 사용자가 위의 설정 단계를 따른 후 어떻게 업데이트될 수 있는지에 대한 사용 사례입니다.

##### 기존 Braze 고객 프로필은 이미 LINE 채널을 따릅니다.

1. 브레이즈 고객 프로필이 속성으로 업데이트되었습니다. 기본값 구독 상태는 .
2. 구독 동기화 도구가 실행되어 사용자가 LINE 채널을 팔로우하고 있음을 찾은 다음 구독 상태로 고객 프로필을 업데이트합니다.
3. 구독 상태에 변화가 발생하면(예: 사용자가 채널을 차단하거나 친구 목록에서 제거하거나 다시 팔로우하는 경우), Braze는 LINE으로부터 업데이트를 수신하고 고객 프로필을 accordingly로 업데이트합니다.

##### 기존 고객 프로필이 LINE 채널을 차단했거나 친구를 삭제했거나 팔로우를 취소했습니다. 

1. 브레이즈 고객 프로필이 속성으로 업데이트되었습니다. 기본값 구독 상태는 .
2. 구독 동기화 도구는 사용자가 LINE 채널을 팔로우하고 있지 않다고 판단하며 사용자의 구독 상태는 그대로 유지됩니다.
3. 사용자가 나중에 채널을 팔로우하면, Braze는 LINE으로부터 업데이트를 받고 구독 상태로 고객 프로필을 업데이트합니다.

##### 고객 프로필 생성은 LINE 팔로우 후에 발생합니다.

1. 채널에 새로운 LINE 팔로워가 생깁니다.
2. 브레이즈는 익명 사용자 프로필을 생성하며, 속성은 팔로워의 LINE ID로 설정되고, 사용자 별칭은 팔로워의 LINE ID로 설정됩니다. 프로필은 구독 상태가 있다.
3. 사용자는 사용자 조정을 통해 LINE ID로 식별됩니다.
  - 익명 사용자 프로필은 엔드포인트를 사용하여 식별될 수 있습니다. 이 사용자 프로필에 대한 후속 업데이트( [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 엔드포인트, [CSV 가져오기]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) 또는 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/cloud_ingestion/)을 통해) 이 사용자 프로필에 대한 후속 업데이트는 이 알려진 `external_id` 으로 사용자를 타겟팅할 수 있습니다.

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

  - 새 사용자 프로필은 ( [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 엔드포인트, [CSV 가져오기]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) 또는 [클라우드 데이터 수집을]({{site.baseurl}}/user_guide/data/cloud_ingestion/) 통해) `native_line_id`. 이 새로운 프로필은 기존 익명 사용자 프로필의 구독 상태를 상속받습니다. 이로 인해 여러 프로필이 동일한 것을 공유하게 됩니다. 이들은 5단계에 설명된 프로세스의 엔드포인트를 사용하여 언제든지 병합할 수 있습니다.

##### 고객 프로필 생성은 LINE 팔로우 이전에 발생합니다.

1. 당신은 새로운 사용자를 확보하고 정보를 Braze에 보냅니다. 새로운 고객 프로필이 생성되었습니다 (프로필 1).
2. 사용자가 귀하의 LINE 계정을 팔로우합니다.
3. 브레이즈는 팔로우 이벤트를 수신하고 익명 사용자 프로필(프로필 2)을 생성합니다.
4. 사용자는 사용자 조정을 통해 LINE ID로 식별됩니다.
5. 당신은 프로필 1을 업데이트하여 속성을 설정합니다. 이 프로필은 프로필 2의 구독 상태를 상속합니다.
  - 이제 동일한 두 개의 사용자 프로필이 있습니다. 이들은 5단계에 설명된 프로세스의 엔드포인트를 사용하여 언제든지 병합할 수 있습니다.

## 사용자 ID 조정 

LINE ID는 사용자가 귀하의 채널을 팔로우할 때 또는 일회성 "팔로워 동기화" 워크플로를 사용할 때 Braze에 의해 자동으로 수신됩니다. LINE ID는 사용자가 따르는 채널에 특정적이므로 사용자가 자신의 LINE ID를 제공할 가능성은 낮습니다.

LINE ID를 기존 Braze 고객 프로필과 결합하는 두 가지 방법이 있습니다:

- LINE 로그인
- 사용자 계정 연결

### 라인 로그인

이 방법은 소셜 미디어 로그인을 사용하여 조정을 수행합니다. 사용자가 앱에 로그인하면, 사용자 계정을 생성하거나 로그인하기 위해 LINE 로그인을 사용할 수 있는 옵션이 제공됩니다.

{% alert note %}
각 사용자에 대한 올바른 LINE ID를 얻으려면 Braze와 통합된 LINE 공식 계정 또는 채널과 동일한 공급자 아래에서 LINE 로그인을 설정하십시오.
{% endalert %}

1. LINE 개발자 콘솔로 이동하여 LINE 로그인을 통해 앱에 로그인하는 사용자의 이메일 주소를 얻기 위한 권한을 요청하세요.

2. LINE 로그인을 구현하기 위해 LINE에서 제공하는 적절한 단계를 따르세요.<br><br>
  - 웹 앱 방향
  - 네이티브 앱 방향<br><br>검증 요청을 위한 범위 설정에 포함되도록 하십시오. 

{: start="3"}
3\. 사용자 이메일을 얻으려면 Verify ID 토큰 호출을 사용하십시오. 

4. 사용자의 LINE ID ()를 데이터베이스의 일치하는 이메일로 사용자의 프로필에 저장하거나, 사용자의 이메일과 LINE ID로 새 사용자 프로필을 생성합니다.

5. [`/user/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users/), [CSV 가져오기]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) 또는 [클라우드 데이터 수집을]({{site.baseurl}}/user_guide/data/cloud_ingestion/) 사용하여 신규 또는 업데이트된 사용자 정보를 Braze로 전송합니다.

#### 워크플로우

##### 기존 팔로워는 LINE 로그인을 사용합니다.

시나리오: 익명 사용자 는 초기 가입자 동기화 중 또는 통합 후 "팔로우" 이벤트를 통해 생성되었습니다.

1. 사용자는 LINE 로그인을 사용하여 귀하의 앱에 로그인합니다.
2. LINE은 사용자 이메일을 제공합니다.
3. 당신은 Braze에 업데이트된 사용자를 전송합니다 (해당 이메일로 LINE ID를 추가한 기존 사용자 프로필) 또는 이메일로 익명 사용자를 업데이트합니다.

##### 새로운 팔로워가 LINE 로그인을 사용합니다.

시나리오: Braze에 사용자의 LINE ID가 있는 고객 프로필이 존재하지 않습니다.

1. 사용자는 LINE 로그인을 사용하여 귀하의 앱에 로그인합니다.
2. LINE은 사용자에게 이메일을 제공합니다.
3. 당신은 다음 중 하나입니다:
  - 기존 고객 프로필을 업데이트하여 해당 이메일에 사용자의 LINE ID도 추가합니다.
  - 이메일과 LINE ID로 새로운 고객 프로필을 생성하세요.
4. 사용자가 귀하의 LINE 공식 계정을 팔로우하면, Braze는 팔로우 이벤트를 수신하고 사용자의 구독 상태를 업데이트합니다.

### 사용자 계정 연결 

이 방법은 사용자가 LINE 계정을 귀하의 앱 사용자 계정에 연결할 수 있도록 합니다. 그런 다음, 예를 들어 {% raw %}`{{line_id}}`{% endraw %} 과 같은 Braze의 Liquid를 사용하여 사용자의 LINE ID를 웹사이트나 앱에 전달하는 사용자 맞춤 URL을 생성하고, 이를 알려진 사용자와 연결할 수 있습니다.

1. 구독 상태 변경을 기반으로 하고 사용자가 LINE 채널에 구독할 때 트리거되는 액션 기반 캔버스를 생성하세요.<br>![][9]
2. 사용자가 웹사이트나 앱에 로그인하도록 유도하는 메시지를 생성하고, 사용자의 LINE ID를 쿼리 매개변수(리퀴드)를 통해 전달합니다. 예를 들어:

```
Thanks for following Flash n' Thread on LINE! For personalized offers and 20% off your next purchase, sign-in to your account: https://flashandthread.com/sign_in?line_user_id={{line_id}}
```

{: start="3"}
3\. 쿠폰 코드를 전달하는 후속 메시지를 작성하세요.
4\. (선택 사항) LINE 사용자가 확인될 때 사용자에게 쿠폰 코드를 전송하는 작업 기반 캠페인 또는 캔버스를 생성합니다. <br>![][10]

#### 작동 방식

사용자가 로그인한 후, 웹사이트나 앱에서 변경이 이루어져 사용자 ID가 Braze로 전송되어 URL의 일부로 전달된 LINE ID와 연결됩니다. 예제 코드와 같은:

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

#### 워크플로우

##### 기존 사용자가 귀하의 LINE 채널을 팔로우합니다.

시나리오: 기존 사용자가 Braze에서 LINE의 채널을 팔로우합니다.

1. LINE은 Braze에 팔로우 이벤트를 보냅니다.
2. 브레이즈는 LINE ID, 사용자 별칭 및 LINE 구독 그룹 상태로 익명 사용자 프로필을 생성합니다.
3. 사용자는 귀하의 웹사이트와 앱에 대한 링크가 포함된 LINE 메시지를 수신하고 로그인합니다. 그들의 고객 프로필은 이제 알려졌습니다.
4. 생성된 익명 사용자 프로필은 식별되며, 사용자의 알려진 고객 프로필에 /users/identify 엔드포인트를 통해 병합됩니다. 알려진 고객 프로필에는 이제 LINE ID가 포함되어 있으며 구독 상태가 있습니다.
5. (선택 사항) 사용자는 쿠폰 코드가 포함된 LINE 메시지를 수신하고 Braze는 Braze 사용자 프로필에 전송 로그를 기록합니다.

## Braze에서 LINE 테스트 사용자 만들기

사용자 조정을 설정하기 전에 "나는 누구인가" 채널 또는 캔버스를 생성하여 LINE 채널을 테스트할 수 있습니다.

1. 특정 트리거 단어에 대해 사용자의 Braze 사용자 ID를 반환하는 캔버스를 설정합니다. <br><br>트리거 예시 <br><br>![특정 구독 그룹에 인바운드 라인을 보낸 사용자에게 캠페인을 전송하는 트리거입니다.][7]{: style="max-width:80%;"}<br><br>메시지 예시<br><br>![Braze 사용자 ID가 표시된 LINE 메시지입니다.][8]{: style="max-width:40%;"}<br><br>

2. Braze에서는 Braze ID를 사용하여 특정 사용자를 검색하고 필요에 따라 수정할 수 있습니다.

{% alert important %}
캔버스에 전역 제어 또는 전송을 방지하는 대조군이 없는지 확인하세요.
{% endalert %}


[1]: {% image_buster /assets/img/line/webhook_settings.png %}
[2]: {% image_buster /assets/img/line/response_settings.png %}
[3]: {% image_buster /assets/img/line/integration.png %}
[4]: {% image_buster /assets/img/line/line_subscription_groups.png %}
[5]: {% image_buster /assets/img/line/filter_group.png %}
[6]: {% image_buster /assets/img/line/csv_export_user_data.png %}
[7]: {% image_buster /assets/img/line/trigger.png %}
[8]: {% image_buster /assets/img/line/message.png %}
[9]: {% image_buster /assets/img/line/account_link_1.png %}
[10]: {% image_buster /assets/img/line/account_link_2.png %}