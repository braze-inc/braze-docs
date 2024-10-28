---
nav_title: 세그먼트 데이터를 CSV로 내보내기
article_title: 세그먼트 데이터를 CSV로 내보내기
page_order: 2
page_type: reference
description: "이 참조 문서에서는 세그먼트 데이터를 CSV로 내보내는 방법을 다룹니다."

---

# 세그먼트 데이터를 CSV로 내보내기

> 세그먼트에서 사용자 데이터의 CSV 내보내기를 요청하려면 세그먼트를 편집하는 동안 **사용자 데이터** 드롭다운을 선택하고 세그먼트의 사용자 데이터 또는 이메일 주소를 내보내도록 선택하십시오.

![][1]

메인 **세그먼트** 페이지에서 <i class="fas fa-gear"></i> **설정** 드롭다운을 선택하여 세그먼트의 CSV 내보내기를 요청할 수도 있습니다.

![][2]

{% alert tip %}
모든 사용자 프로필에서 데이터를 내보내려면 필터가 없는 세그먼트를 생성한 다음 CSV 내보내기를 요청하십시오.
{% endalert %}

CSV 출력에는 내보내기 시점에 세그먼트에서 캡처된 각 고객 프로필의 데이터가 포함되어 있습니다. 기어 아이콘과 CSV 내보내기를 선택하여 세그먼트를 내보낼 수 있습니다. Braze는 보고서를 백그라운드에서 생성하고 현재 로그인한 사용자에게 이메일로 전송합니다.

{% alert important %}
파일 크기 제한으로 인해 세그먼트의 예상 크기가 500,000명 이상의 사용자일 경우 내보내기가 실패할 수 있습니다. 이 제한은 정확한 계산이 아닌 세그먼트의 예상 크기를 사용한다는 점에 유의하십시오. 자세한 내용은 [큰 세그먼트 내보내기]({{site.baseurl}}/help/help_articles/segments/exporting_large_segments/)를 참조하세요.
{% endalert %}

Amazon S3 자격 증명][26]을 Braze에 연결한 경우 CSV는 대신 키 `segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip` 아래 S3 버킷에 업로드됩니다. 이메일로 전송된 링크는 내보낸 후 하루가 지나면 만료되며, 대시보드에 로그인해야 액세스할 수 있습니다.

## 데이터 포함 내보내기

다음은 선택에 따라 내보내기에 포함됩니다.

### CSV 내보내기 사용자 데이터

| 필드 이름                  | 설명                                              |
| --------------------------- | -------------------------------------------------------- |
| Appboy ID                   | 내부 ID (변경할 수 없음)                           |
| 국가                     | 국가                                    |
| 생성됨                  | 고객 프로필이 생성된 날짜 및 시간                   |
| 장치                     | 기기 정보                           |
| 생년월일               | 생년월일                                            |
| 이메일                       | 이메일 주소                                            |
| 이메일에서 구독 취소됨 | 이메일 구독 취소 날짜                            |
| 사용자_아이디                     | 외부 ID                                              |
| 이름                  | 이름                                               |
| 첫 번째 세션               | 첫 세션의 날짜 및 시간                           |
| 성별                      | 성별                                                   |
| google_ad_ids               | 사용자와 연결된 Google 광고 ID                      |
| 도시                        | 도시                                     |
| IDFAs                       | 광고 식별자 (IDFA) 값                 |
| IDFVs                       | 벤더 식별자 (IDFV) 값                      |
| 언어                    | ISO-639-1 표준의 언어                                        |
| 마지막_앱_버전_사용됨       | 사용된 앱의 마지막 버전                             |
| 성                   | 성                                                |
| 마지막_세션                | 마지막 세션의 날짜 및 시간                            |
| number_of_google_ad_ids     | 연관된 Google 광고 ID 수               |
| IDFA 수             | 연관된 IDFA의 수                                |
| IDFV의_수             | 연관된 IDFV 수                                |
| 푸시 토큰 수       | 연관된 푸시 알림 토큰 수             |
| roku_ad_id_수       | 연관된 Roku 광고 ID 수                 |
| number_of_windows_ad_ids    | 연관된 Windows 광고 ID 수              |
| 전화번호                | 전화번호                                             |
| 푸시_옵트인_시          | 푸시 알림을 수신하도록 선택한 날짜                       |
| 푸시에서 구독 취소됨   | 푸시 알림에서 구독 취소된 날짜                |
| 랜덤_버킷               | 무작위 버킷 번호                                 |
| roku_ad_ids                 | Roku 광고 ID                          |
| 세션 수               | 총 세션 수                                 |
| 시간대                    | 사용자의 시간대는 IANA 시간대 데이터베이스와 동일한 형식입니다                                         |
| 인앱 구매 총액       | 인앱 구매에 사용된 총 금액                   |
| 사용자_별칭                | 사용자 별칭, 있는 경우                                          |
| windows_ad_ids              | Windows 광고 ID                       |
| 사용자 지정 이벤트               | 선택에 따른 내보내기                             |
| 사용자 지정 속성           | 선택에 따른 내보내기                             |
{: .reset-td-br-1 .reset-td-br-2 }

### CSV 내보내기 이메일 주소

| 필드 이름                  | 설명            |
| --------------------------- | ---------------------- |
| 사용자_아이디                     | 사용자의 외부 ID     |
| 이름                  | 이름             |
| 성                   | 성              |
| 이메일                       | 이메일                  |
| 이메일에서 구독 취소됨 | 이메일 탈퇴 날짜 |
| opted_in_to_emails_at       | 이메일 옵트인 날짜      |
| 사용자_별칭                | 사용자 별칭, 있는 경우   |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
CSV 및 API 내보내기에 대한 도움말은 [문제 해결]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/) 기사를 참조하십시오.
{% endalert %} 

[1]: {% image_buster /assets/img_archive/csvexport.png %}
[2]: {% image_buster /assets/img_archive/csvexport2.png %}
[26]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration
