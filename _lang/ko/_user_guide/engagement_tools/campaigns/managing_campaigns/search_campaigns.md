---
nav_title: 캠페인 검색
article_title: 캠페인 검색
page_order: 10
page_type: reference
description: "이 문서에서는 캠페인 검색을 사용하여 캠페인을 찾는 방법에 대해 설명합니다."
tool:
  - Campaigns

---

# 캠페인 검색

> 이 문서에서는 캠페인 목록의 검색 필드를 사용하여 결과를 구체화하는 방법에 대해 설명합니다.

## 필터

사이드 메뉴의 필터를 사용하여 크리에이터, 에디터, 전송 날짜 또는 채널별로 결과를 그룹화하거나 **내 것만 표시를** 선택하여 **내가** 만든 캠페인으로 검색 결과를 제한할 수 있습니다. 상태 및 [태그별로]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) 필터링하여 검색 결과를 더욱 좁힐 수도 있습니다.

![][2]

검색 드롭다운을 확장하여 마지막 편집자, 대상 세그먼트, 메시징 채널 또는 날짜별로 필터링합니다.

![][3]

## 검색 구문

캠페인 필터를 선택하면 검색 필드에 적절한 구문이 자동으로 추가됩니다. 하지만 이러한 필터를 수동으로 입력할 수도 있습니다. 수동 검색을 사용하는 경우 구문은 필터 이름 다음에 콜론이 오고, 그 다음에 입력 내용을 입력하는 방식입니다. 예를 들어 푸시 캠페인을 검색하려면 `channel:push` 을 입력합니다.

다음은 지원되는 검색 필터 목록입니다:

| 검색 | 필터 | 입력 |
| --- | --- | --- |
| 캠페인 API 식별자 | `api_id` | 특정 [캠페인 API 식별자]({{site.baseurl}}/api/identifier_types#api-identifier-types) |
| 캠페인 타겟 세분화 | `segment` | 세그먼트 이름 |
| 캠페인이 타겟팅하는 메시지 채널 | `channel` | 다음 중 하나를 선택합니다: <br>-`content_cards` <br>- `email`<br>- `push`<br>- `sms` (SMS와 MMS 모두 반환)<br>- `webhook`
| 상태 또는 배송 유형 | `status` | 다음 중 하나를 선택합니다: <br>- `one-time` <br>- `recurring` <br>- `triggered` <br>- `multivariate` <br>- `transactional` <br> - `drafts` <br> - `stopped` <br> - `archived` <br> - `all` |
| 태그 | `tag` | \- 단일 태그 이름 <br>\- 쉼표로 구분된 태그 이름 목록 |
| 가장 최근 편집기 | `edited_by` | 사용자의 이메일 주소 |
| 날짜 캠페인이 생성되었습니다. | `created` | \- 형식의 단일 날짜 `YYYY/MM/DD`<br> \- 형식의 날짜 범위 `YYYY/MM/DD-YYYY/MM/DD` |
| 날짜 캠페인이 마지막으로 편집되었습니다. | `edited` | \- 형식의 단일 날짜 `YYYY/MM/DD`<br> \- 형식의 날짜 범위 `YYYY/MM/DD-YYYY/MM/DD` |
| 날짜 캠페인이 마지막으로 전송된 날짜 | `sent` | \- 형식의 단일 날짜 `YYYY/MM/DD`<br> \- 형식의 날짜 범위 `YYYY/MM/DD-YYYY/MM/DD` |
| 생성한 캠페인 | `created_by_me` | `true` |


[1]: {% image_buster /assets/img_archive/campaign_search.png %}
[2]: {% image_buster /assets/img_archive/campaign_search2.png %}
[3]: {% image_buster /assets/img_archive/campaign_search3.png %}
