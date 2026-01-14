---
nav_title: 세그먼트 데이터를 CSV로 내보내기
article_title: 세그먼트 데이터를 CSV로 내보내기
page_order: 2
page_type: reference
description: "이 참조 문서에서는 세그먼트 데이터를 CSV로 내보내는 방법에 대해 설명합니다."

---

# 세그먼트 데이터를 CSV로 내보내기

> 이 페이지에서는 세그먼트에서 사용자 데이터의 CSV 내보내기를 요청하는 방법과 내보내기에 포함된 데이터에 대해 설명합니다.

세그먼트 데이터를 CSV로 내보내려면 세그먼트를 편집하는 동안 **사용자 데이터** 드롭다운을 선택하고 해당 세그먼트의 사용자 데이터 또는 이메일 주소 중 하나를 선택하여 내보내도록 선택합니다.

사용자 데이터 드롭다운이 있는 세그먼트 세부 정보 섹션에 내보내기 옵션이 표시됩니다.]({% image_buster /assets/img_archive/csvexport.png %})

세그먼트에 대한 <i class="fas fa-gear"></i> **설정** 드롭다운을 선택하여 기본 **세그먼트** 페이지에서 CSV 내보내기를 요청할 수도 있습니다:

메인 세그먼트 페이지의 설정 드롭다운을 클릭합니다.]({% image_buster /assets/img_archive/csvexport2.png %})

{% alert tip %}
모든 고객 프로필에서 데이터를 내보내려면 필터가 없는 세그먼트를 만든 다음 CSV 내보내기를 요청하세요.
{% endalert %}

CSV 출력에는 내보내기 시점에 세그먼트에서 캡처한 각 사용자 프로필의 데이터가 포함됩니다. 톱니바퀴 아이콘과 CSV 내보내기를 선택하면 원하는 세그먼트를 내보낼 수 있습니다. Braze 커런츠는 백그라운드에서 보고서를 생성하여 현재 로그인한 사용자에게 이메일로 전송합니다.

{% alert important %}
파일 크기 제한으로 인해 세그먼트의 예상 사용자 수가 500,000명을 초과하는 경우 내보내기가 실패할 수 있습니다. 이 제한은 정확한 계산이 아닌 세그먼트의 예상 크기를 사용한다는 점에 유의하세요. 자세한 내용은 [대규모 세그먼트 내보내기를](#exporting-large-segments) 참조하세요.
{% endalert %}

[Amazon S3 인증정보를]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration) Braze에 연결한 경우, CSV는 대신 `segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip` 키 아래에 있는 S3 버킷에 업로드됩니다. 이메일로 전송된 다운로드 링크에 액세스하려면 대시보드에 로그인해야 합니다.

{% multi_lang_include alerts/important_alerts.md alert='S3 file bucket export' %}

## 내보내기에 포함된 데이터

선택 항목에 따라 내보내기에 포함되는 항목은 다음과 같습니다.

### CSV 내보내기 사용자 데이터

| 필드 이름                  | 설명                                              |
| --------------------------- | -------------------------------------------------------- |
| Appboy ID                   | 내부 ID(변경 불가)                           |
| 국가                     | 국가                                    |
| created_at                  | 고객 프로필이 생성된 날짜 및 시간                   |
| 기기                     | 기기 정보                           |
| date_of_birth               | 생년월일                                            |
| 이메일                       | 이메일 주소                                            |
| unsubscribed_from_emails_at | 이메일 탈퇴 날짜                            |
| user_id                     | 외부 ID                                              |
| first_name                  | 이름                                               |
| first_session               | 첫 세션 날짜 및 시간                           |
| 성별                      | 성별                                                   |
| google_ad_ids               | 사용자와 연결된 Google 광고 ID                      |
| 도시                        | 도시                                     |
| IDFAs                       | 광고 식별자(IDFA) 값                 |
| IDFVs                       | 공급업체 식별자(IDFV) 값                      |
| 언어                    | ISO-639-1 표준의 언어                                        |
| last_app_version_used       | 마지막으로 사용한 앱 버전                             |
| last_name                   | 성                                                |
| last_session                | 마지막 세션 날짜 및 시간                            |
| number_of_google_ad_ids     | 연결된 Google 광고 ID 수               |
| number_of_IDFAs             | 연결된 IDFA 수                                |
| number_of_IDFVs             | 연결된 IDFV 수                                |
| number_of_push_tokens       | 연결된 푸시 알림 토큰 수             |
| number_of_roku_ad_ids       | 연관된 Roku 광고 ID 수                 |
| number_of_windows_ad_ids    | 연결된 Windows 광고 ID 수              |
| phone_number                | 전화번호                                             |
| opted_into_push_at          | 푸시 알림을 옵트인한 날짜                       |
| unsubscribed_from_push_at   | 푸시 알림에서 탈퇴한 날짜                |
| random_bucket               | 무작위 버킷 번호                                 |
| roku_ad_ids                 | Roku 광고 ID                          |
| session_count               | 총 세션 수                                 |
| 시간대                    | 사용자의 표준 시간대는 IANA 표준 시간대 데이터베이스와 동일한 형식입니다.                                         |
| in_app_purchase_total       | 앱 내 구매에 지출한 총 금액                   |
| user_aliases                | 사용자 별칭 지정(있는 경우)                                          |
| windows_ad_ids              | Windows 광고 ID                       |
| 커스텀 이벤트               | 내보내기 시 선택 기준                             |
| 커스텀 속성           | 내보내기 시 선택 기준                             |
{: .reset-td-br-1 .reset-td-br-2 }

### CSV 내보내기 이메일 주소

| 필드 이름                  | 설명            |
| --------------------------- | ---------------------- |
| user_id                     | 사용자의 외부 ID     |
| first_name                  | 이름             |
| last_name                   | 성              |
| 이메일                       | 이메일                  |
| unsubscribed_from_emails_at | 이메일 탈퇴 날짜 |
| opted_in_to_emails_at       | 이메일 옵트인 날짜      |
| user_aliases                | 사용자 별칭 지정(있는 경우)   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
CSV 및 API 내보내기에 대한 도움말은 [문제 해결]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/) 도움말 문서를 참조하세요.
{% endalert %} 

## 대규모 세그먼트 내보내기

500,000명 이상의 사용자를 포함하는 대규모 사용자 세그먼트를 내보내는 방법에는 여러 가지가 있습니다.

{% tabs %}
{% tab Multiple segments %}

큰 세그먼트를 작은 세그먼트로 세분화한 다음 각각의 작은 세그먼트를 Braze에서 내보낼 수 있습니다. 

{% endtab %}
{% tab Random bucket numbers %}

[무작위 버킷 번호를]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) 사용하여 사용자 기반을 여러 세그먼트로 나눈 다음 내보내기 후에 결합할 수도 있습니다. 예를 들어 세그먼트를 두 개의 다른 세그먼트로 세분화해야 하는 경우 다음 필터를 사용하여 세분화할 수 있습니다:
- 세그먼트 1: 무작위 버킷 번호가 5000 미만(0-4999 포함)입니다.
- 세그먼트 2: 무작위 버킷 번호가 4999(5000-9999 포함) 이상입니다.

{% endtab %}
{% tab Endpoints %}

다음 엔드포인트를 활용하여 특정 세그먼트에 대한 사용자 데이터를 내보낼 수도 있습니다. 이러한 엔드포인트에는 데이터 제한이 적용된다는 점에 유의하세요.
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)

{% endtab %}
{% endtabs %}
