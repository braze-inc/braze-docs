---
nav_title: StackAdapt
article_title: StackAdapt
description: "이 참고 문서에서는 Braze와 StackAdapt의 파트너십에 대해 간략하게 설명합니다."
alias: /partners/stackadapt/
page_type: partner
search_tag: Partner
---

# StackAdapt

> [스택어댑트는](https://www.stackadapt.com/) 디지털 마케터들이 타겟팅된 성과 중심 광고를 제공하는 데 사용하는 선도적인 AI 기반 마케팅 플랫폼입니다.

_이 통합은 StackAdapt에서 유지 관리합니다._

Braze와 StackAdapt의 데이터 통합을 통해 Braze의 사용자 프로필 데이터를 StackAdapt 데이터 허브에 동기화할 수 있습니다. 두 플랫폼을 연결하면 고객에 대한 통합된 뷰를 생성하고 퍼스트파티 데이터를 활성화하여 광고 성과를 개선할 수 있습니다.

## 사용 사례

- **휴면 사용자를 재참여시키세요:** Braze의 이메일 마케팅 목록에서 탈퇴한 사용자를 식별하고 StackAdapt의 프로그래매틱 광고로 타겟팅하여 다른 채널을 통해 재참여를 유도할 수 있습니다.
- **멀티채널 경험 만들기:** 사용자의 여정을 이메일을 넘어 확장하세요. 예를 들어, 사용자가 Braze에서 이메일 캠페인을 클릭하면 StackAdapt를 사용하여 보완적인 프로그래매틱 광고를 표시하여 메시지를 강화하고 추가 행동을 유도할 수 있습니다.
- **규모에 맞게 개인화하세요:** '거주 도시' 또는 '언어' 등 Braze의 세분화된 데이터 포인트를 활용하여 관련성이 높고 현지화된 언어별 광고와 이메일을 게재할 수 있습니다.
- **오디언스에 대한 이해도를 높입니다:** 프로필 속성을 동기화하면 StackAdapt에서 더 풍부한 오디언스 세그먼트를 생성하여 보다 정밀한 타겟팅과 개인화된 광고 경험을 제공할 수 있습니다.

## 필수 조건

| Requirement | 설명         |
| ----------- | ------------------- |
| **StackAdapt 계정**  | 데이터 허브 통합을 관리할 수 있는 권한이 있는 활성 StackAdapt 계정이 필요합니다. |
| **Braze REST API key**  | A Braze REST API key with the following permissions: <br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages.schedule_broadcasts<br>- campaigns.list<br>- campaigns.details<br>- canvas.list<br>- canvas.details<br>- segments.list<br>- segments.details<br>- purchases.product_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get<br><br>**설정** > **API 키에서** Braze 대시보드에서 생성할 수 있습니다. |
| **Braze REST endpoint** | [Your REST endpoint URL](https://www.braze.com/docs/api/basics/#endpoints). Your endpoint depends on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 작동 방식

StackAdapt 데이터 허브는 Braze 계정에 직접 연결하여 사용자 프로필 속성을 가져옵니다. 이를 통해 StackAdapt 내에서 직접 Braze 고객 데이터를 활용하여 오디언스 세분화 및 활성화를 진행할 수 있습니다.

### Data flow

1. StackAdapt는 제공된 API 자격 증명을 사용하여 Braze 인스턴스에 대한 보안 연결을 시작합니다.
2. StackAdapt는 사용자 프로필 데이터, 특히 사용자가 선택하고 매핑한 속성을 검색합니다.
3. 데이터는 정규화되어 StackAdapt 데이터 허브에 수집되며, 세그먼트를 세분화하여 캠페인에 사용할 수 있게 됩니다.
4. 데이터 통합을 통해 예약된 데이터 동기화(예: 매일)를 통해 StackAdapt 오디언스에게 Braze의 최신 프로필 데이터를 최신 상태로 유지할 수 있습니다.

## 동기화된 필드

StackAdapt는 다음을 포함하되 이에 국한되지 않는 다양한 Braze 프로필 필드를 동기화할 수 있습니다:

{% tabs local %}
{% tab Standard attributes %}
- Email
- Date of Birth
- First Name
- Last Name
- Phone
- 출생지
- Country
- Gender
- Time Zone
- 생성 시간
- External ID
- Language 

{% endtab %}
{% tab Custom attributes %}
특정 비즈니스 요구 사항에 따라 정의된 앱 또는 비즈니스에 고유한 속성입니다.

{% endtab %}
{% tab Attribution data %}
- Attributed Ad
- Attributed Adgroup
- Attributed Campaign
- Attributed Source

{% endtab %}
{% tab Subscription status %}
- 이메일 구독 상태
- 푸시 구독 상태 

마케팅 커뮤니케이션에 대한 사용자 동의를 반영하는 필드(예: 이메일 구독 상태)를 Braze에 정확하게 매핑하여 광고 활동이 사용자 선호도 및 개인정보 보호 규정을 준수하도록 하는 것이 중요합니다.

{% endtab %}
{% endtabs %}

## Setting up the integration

다음 단계에 따라 Braze 사용자 프로필을 가져오세요:

1. StackAdapt 계정에 로그인합니다.
2. 탐색 메뉴에서 **데이터 허브를** 선택합니다.
3. **프로필 가져오기를** 선택한 다음 사용 가능한 통합 목록에서 **Braze를** 선택합니다.
4. 메시지가 표시되면 Braze API 자격 증명을 입력합니다.
- **Braze REST API 키:** **설정** > **API 키로** 이동하여 Braze에서 찾을 수 있습니다. 보안 모범 사례로, StackAdapt 통합을 위한 전용 API 키를 생성하는 것이 좋습니다.
- **Braze 앱 키:** **설정** > **API 키** 또는 **앱 관리로** 이동하여 Braze에서 찾을 수 있습니다.
- **Braze REST 엔드포인트 URL:** Braze 인스턴스의 기본 URL(예: ```https://rest.iad-01.braze.com```).
5. **연결을** 선택하여 자격 증명을 확인합니다.

![StackAdapt의 Braze 연결.]({% image_buster /assets/img/stackadapt/stackadapt_braze_connection_settings.png %})

{: start="6"}
6\. 연결을 선택하고 스택어댑트 광고주를 선택합니다.
7\. **속성 매핑을** 구성합니다. StackAdapt가 제안하는 기본값 매핑과 미리 선택된 속성을 검토하고 확인합니다.
8\. (선택 사항) 추가 속성을 가져오려면 해당 확인란을 선택하여 선택하고 해당 속성에 PII가 포함되어 있는지 여부와 데이터 유형을 지정합니다.

![StackAdapt의 Braze 연결.]({% image_buster /assets/img/stackadapt/stackadapt_mappings.png %})

{: start="9"}
9\. 프로필을 **목록에** 추가하거나 새 프로필을 만들어 프로필을 그룹화하고 세분화할 수 있습니다.
10\. **통합 활성화를** 선택하여 초기 데이터 동기화를 시작합니다.

## 고려 사항

- **커스텀 이벤트 및 속성 가져오기:** 이 기능은 아직 지원되지 않습니다.
- **데이터 지연 시간:** 모든 사용자 프로필 데이터를 가져오는 데 최대 24시간이 걸릴 수 있습니다.
- **동의 관리:** Braze에서의 데이터 수집 관행이 개인정보 보호 규정을 준수하는지, 광고 목적으로 고객 데이터를 사용하는 데 필요한 동의를 받았는지 확인합니다. StackAdapt는 소스 시스템에서 전달된 동의 상태에 의존합니다.
- **속성 일관성:** 데이터의 효과를 극대화하려면 속성의 이름을 지정하고 채우는 방식에 일관성을 유지한 후 이를 StackAdapt에 동기화하세요.
