---
nav_title: 이메일 목록 가져오기
article_title: Braze로 이메일 목록 가져오기
page_order: 4
page_type: reference
description: "이 참고 문서에서는 이메일 목록을 Braze로 가져오는 모범 사례를 다룹니다."
channel: email

---

# 이메일 목록을 Braze로 가져오기 {#importing-email-lists}

> 성공적인 이메일 발신자로 자리매김하기 위한 중요한 단계는 양질의 이메일 목록을 확보하는 것입니다. 적절한 이메일 목록 관리를 통해 전달률을 높이고 보다 정확하고 깔끔한 캠페인 결과를 얻을 수 있습니다.

## 가져오기 전 고려 사항

{% multi_lang_include email-via-sms-warning.md %}

### 이메일 목록 유효성 검사

이메일 목록을 Braze로 가져오기 전에 목록에 진짜 이메일 주소만 포함되어 있는지 확인하세요. 반송률이 높으면 이메일 발신자의 평판이 손상될 수 있습니다. 

이메일 목록 정리 서비스는 이메일 주소가 올바른 구문을 따르고 이메일 주소의 물리적 특성을 가지고 있는지 확인하고, 이메일 도메인을 확인하고, 이메일 서버에 연결하여 이메일 주소가 존재하는지 인증함으로써 이 작업을 대신 수행할 수 있습니다.

### 참여도 높은 사용자 식별

참여도가 가장 높은 사용자를 파악하려면 먼저 장기 휴면 사용자를 제거하세요. 6개월 이상 이메일에 참여하지 않은 사용자에게 이메일을 보내면 이메일 발송자 평판이 손상될 수 있으므로 이메일을 보내지 않는 것이 좋습니다. 이메일 목록을 가져올 때는 지난 6개월 이내에 회원님이 보낸 이메일을 열어본 사용자만 포함해야 합니다.

In the long term, you should also consider implementing a [sunset policy]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/).

### 금지 목록 피하기

기존 이메일 제공업체에서 전환하는 경우에는 사용 중지 목록에서 사용자를 가져오지 않도록 하세요. 수신 거부 목록에는 수신 거부되었거나, 스팸으로 표시되었거나, 하드 반송된 이메일 주소가 포함됩니다.

## 가져오기 방법

이메일 목록이 준비되면 Braze REST API 또는 CSV 파일 등 여러 가지 방법으로 사용자를 Braze로 가져올 수 있습니다. Read more at our dedicated [User Import]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/) article.

