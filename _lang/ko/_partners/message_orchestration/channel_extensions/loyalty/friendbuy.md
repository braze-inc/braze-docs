---
nav_title: Friendbuy
article_title: Friendbuy
description: "Friendbuy와 Braze를 통합하는 방법을 알아보세요."
alias: /partners/friendbuy/
page_type: partner
search_tag: Partner

---

# Friendbuy

> Friendbuy와 Braze의 통합을 활용하여 이메일 및 SMS 기능을 확장하는 동시에 추천 및 로열티 프로그램 커뮤니케이션을 손쉽게 자동화할 수 있습니다. Braze는 Friendbuy를 통해 수집된 모든 옵트인 전화번호에 대한 고객 프로필을 생성합니다.

_이 통합은 Friendbuy에 의해 유지됩니다._

## 전제 조건

시작하기 전에 다음이 필요합니다:

| 전제 조건          | 설명                                                                                                                              |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Friendbuy 계정   | 이 파트너십을 이용하려면 [Friendbuy 계정이][1] 필요합니다.                                                              |
| Braze REST API 키  | `users.track` 권한이 있는 Braze REST API 키. Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다.        |
| Braze REST 엔드포인트 | Braze 인스턴스의 URL에 따라 달라지는 [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Friendbuy 통합

[Friendbuy에서][1] **개발자 센터** > **연동** 카드로 이동한 다음 Braze 연동 카드에서 **연동 추가를** 선택합니다.

![Friendbuy의 Braze 통합 카드.][100]{: style="max-width:75%;"}

양식에 REST 엔드포인트와 API 키를 입력한 다음, **통합 설치**를 선택합니다.

![Friendbuy 통합 양식입니다.][101]{: style="max-width:55%;"}

[Friendbuy 계정으로][1] 돌아가서 페이지를 새로 고칩니다. 통합에 성공했다면 다음과 비슷한 메시지가 표시됩니다:

![통합 설치][102]{: style="max-width:55%;"}

### 사용자 지정 속성

| 사용자 지정 속성 이름            | 정의                                                                                                                                         | 데이터 유형 |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| **Friendbuy 추천 상태**    | 추천인은 *지지자*, 추천 대상은 *추천받은 친구*로 분류됩니다.                                                          | 문자열    |
| **Friendbuy 고객 이름**      | 고객이 추천 위젯을 통해 정보를 제출할 때 입력한 이름입니다.                                                                 | 문자열    |
| **Friendbuy 추천 링크**      | 지지자를 위해 생성된 개인 추천 링크(PURL). 예: https://fbuy.io/EzcW                                                       | 문자열    |
| **Friendbuy 마지막 공유 날짜** | 지지자가 공유 채널을 통해 친구와 마지막으로 공유한 날짜와 시간. 지지자가 아직 공유하지 않은 경우에는 속성정보는 표시되지 않습니다. | 시간      |
| **Friendbuy 캠페인 ID**        | 어드바이저를 위해 생성된 개인 추천 링크와 연결된 캠페인 ID입니다.                                                               | 문자열    |
| **Friendbuy 캠페인 이름**      | 어드바이저를 위해 생성된 개인 추천 링크와 연결된 캠페인 이름입니다.                                                             | 문자열    |
| **Friendbuy 쿠폰 코드**        | 고객에게 배포된 가장 최근의 추천 쿠폰 코드입니다. 참고: 하나의 코드만 표시됩니다.                                            | 문자열    |
| **Friendbuy 쿠폰 가치**       | 고객에게 가장 최근에 배포된 쿠폰 코드의 통화 가치입니다.                                                                     | 숫자    |
| **Friendbuy 쿠폰 상태**      | 고객에게 가장 최근에 배포된 쿠폰 코드의 상태입니다. 참고: 상태는 '배포됨' 또는 '사용됨'임                            | 문자열    |
| **Friendbuy 쿠폰 통화**    | 고객에게 가장 최근에 배포된 쿠폰 코드와 관련된 통화 코드(USD, CAD 등) 또는 백분율(%)입니다.                             | 문자열    |
| **Friendbuy 쿠폰 캠페인 ID** | 고객에 대해 생성된 쿠폰 코드와 연결된 캠페인 ID입니다.                                                                          | 문자열    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 기본 동작

고객 데이터를 Braze로 전송하기 전에 고객은 추천 위젯을 통해 다음 상자 중 하나 이상의 확인란을 선택하여 옵트인해야 합니다:

![추천 위젯][103]

{% alert note %}
Friendbuy는 국제 표준(E.164)을 사용하여 실제 전화번호를 확인합니다. `555-555-5555` 과 같이 잘못된 번호는 Braze로 전송되지 않습니다.
{% endalert %}

### 확인란 동작

| 확인란 선택 | 동작                                                        |
|-------------------|-----------------------------------------------------------------|
| 이메일 전용        | 고객의 이메일 주소만 Braze로 전송됩니다.             |
| 전화 전용        | 고객의 전화번호만 Braze로 전송됩니다.              |
| 둘 다 아님           | 고객 데이터는 Braze로 전송되지 않습니다.                              |
| 모두              | 고객의 이메일 주소와 전화번호가 Braze로 전송됩니다. |


[1]: https://retailer.friendbuy.io/
[100]: {% image_buster /assets/img/friendbuy/choosing_braze.png %}
[101]: {% image_buster /assets/img/friendbuy/install_form.png %}
[102]: {% image_buster /assets/img/friendbuy/install_success.png %}
[103]: {% image_buster /assets/img/friendbuy/referral_widget.png %}
