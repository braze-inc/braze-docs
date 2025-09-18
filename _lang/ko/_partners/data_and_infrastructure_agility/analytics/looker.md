---
nav_title: Looker
article_title: Looker
alias: /partners/looker/
description: "이 참조 문서에서는 비즈니스 인텔리전스 및 빅데이터 분석 플랫폼인 Looker와 Braze 간의 파트너십을 간략히 설명합니다."
page_type: partner
search_tag: Partner

---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/looker-integration-with-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Looker

> 비즈니스 인텔리전스 및 빅데이터 분석 플랫폼인 [Looker를](https://looker.com/) 사용하면 실시간 비즈니스 분석을 원활하게 탐색, 분석 및 공유할 수 있습니다.

Braze와 Looker의 통합으로 Braze 사용자는 REST API를 통해 퍼스트파티 [Looker 블록](#looker-blocks) 및 [Looker 작업](#looker-actions) 사용자 플래그 지정 기능을 활용할 수 있습니다. 이렇게 플래그가 지정된 사용자를 세그먼트에 추가하여 향후 Braze 캠페인 또는 캔버스를 [타겟팅](#segment-users)할 수 있습니다. To use Looker with Braze, we recommend sending your Braze data to a [data warehouse using Braze currents][6], then use Braze Looker Blocks to quickly model and visualize your Braze data in Looker.

## 전제 조건

| 요구 사항 | 설명 |
|---|---|
|Looker 계정 | 이 파트너십을 활용하려면 [Looker 계정](https://looker.com/)이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> 이는 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| Braze REST 엔드포인트  | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL에][1] 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### 제한 사항

- 이 프로세스는 피벗되지 않은 데이터에 대해서만 작동합니다.
- API는 한 번에 최대 100,000개의 행을 처리합니다.
- 사용자 플래그의 최종 개수는 중복 또는 비사용자로 인해 더 낮을 수 있습니다.

## 통합

### Looker 블록

Looker 블록을 사용하면 고객이 [커런츠][5]를 통해 제공하는 세분화된 데이터 보기에 빠르게 액세스할 수 있습니다. 블록은 커런츠 데이터에 대한 미리 만들어진 시각화 및 모델링을 제공합니다. 이를 통해 유지와 같은 분석 패턴을 쉽게 구현하고, 메시지 전달 가능성을 평가하며, 사용자 행동을 더 자세히 살펴보는 등 Braze 고객에게 다양한 기능을 지원합니다.

Looker 블록을 구현하려면 GitHub 코드의 README 파일에 있는 지침을 따르세요.
- [메시지 참여 분석 블록 README][2]
- [사용자 행동 분석 블록 README][3]

두 통합 모두 필요한 데이터를 캡처하고 전송하도록 [초기 Braze 통합][4]과 Looker 호환 [데이터 웨어하우스][7]와의 Braze 통합이 적절하게 구성되어 있다고 가정합니다.


{% alert important %}
Braze는 [Snowflake](https://www.snowflake.com/)를 데이터 웨어하우스로 사용하여 Looker 블록을 빌드합니다. 블록이 가능한 한 많은 데이터 웨어하우스에서 작동하는 것을 목표로 하고 있지만, 방언에 따라 일부 SQL 함수는 가용성, 구문 또는 동작이 다를 수 있습니다.
{% endalert %}

{% alert warning %}
다양한 이름 지정 규칙에 유의하세요! 커스텀 이름을 사용하는 경우 해당 이름을 모두 변경하지 않으면 데이터에 불일치가 발생할 수 있습니다. 보기/표 또는 모델 이름을 사용자 지정한 경우 LookML에서 각 이름을 선택한 이름으로 변경합니다.
{% endalert %}

#### 사용 가능한 블록

| 블록 | 설명 |
|---|---|
| 메시지 참여 분석 블록 | 이 블록에는 푸시, 이메일, 인앱 메시지, 웹훅, 뉴스피드, 전환, 캔버스 진입, 캠페인 대조군 등록 이벤트에 대한 데이터가 포함되어 있습니다. <br><br>이 [Looker 블록](https://looker.com/platform/blocks/source/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)에 대해 자세히 알아보거나 [GitHub 코드](https://github.com/llooker/braze_message_engagement_block)를 확인하세요. |
| 사용자 행동 분석 블록 | 이 블록에는 커스텀 이벤트, 구매, 세션, 위치 이벤트 및 제거에 관한 데이터가 포함되어 있습니다.<br><br>이 [Looker 블록](https://looker.com/platform/blocks/source/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)에 대해 자세히 알아보거나 [GitHub 코드](https://github.com/llooker/braze_retention_block)를 확인하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Looker 작업

Looker 작업을 사용하면 Looker Look에서 REST API 엔드포인트를 통해 Braze에서 사용자에게 플래그를 지정할 수 있습니다. 작업에서는 차원에 `braze_id` 태그가 지정되어야 합니다. 이 작업은 플래그가 지정된 값을 사용자의 `looker_export` 사용자 지정 속성에 추가합니다.

{% alert important %}
기존 사용자만 플래그가 지정됩니다. Braze에서 데이터에 플래그를 지정할 때는 피벗 모양을 사용할 수 없습니다.
{% endalert %}

#### 1단계: Braze Looker 작업 설정

Braze REST API 키와 REST 엔드포인트로 Braze Looker 작업을 설정합니다.

![Looker Braze 구성 페이지. 여기에서 Braze API 키와 Braze REST API 엔드포인트에 대한 필드를 찾을 수 있습니다.][12]

#### 2단계: Looker Develop 설정

Looker Develop 내에서 적절한 보기를 선택합니다. 차원 태그에 `braze_id` 을 추가하고 변경 사항을 커밋합니다.
이 `braze_id` 태그는 어떤 필드가 고유 키인지 확인하는 데 사용됩니다.

```json
dimension: external_id {
    type: string
    primary_key: yes
    sql: ${TABLE}.external_id ;;
    tags: ["braze_id"]
}
```

**변경 사항을 커밋해야 합니다. Looker Action은 프로덕션 설정에서만 작동합니다.**

#### 3단계: 태그에서 사용자 속성 설정

선택적으로 속성 이름을 괄호로 묶은 `braze[]` 태그를 사용하여 속성을 설정할 수 있습니다. 예를 들어 커스텀 속성 `user_segment`를 전송하려는 경우 태그는 `braze[user_segment]`가 됩니다.

다음 제한 사항에 유의하세요:
- 속성은 **모양에 필드로 포함**된 경우에만 전송됩니다.
- 지원되는 유형은 `Strings`, `Boolean`, `Numbers`, `Dates`입니다.
- 속성 이름은 대소문자를 구분합니다.
- 표준 속성은 [표준 사용자 프로필]({{site.baseurl}}/api/endpoints/user_data/#braze-user-profile-fields) 이름과 정확히 일치하는 한 설정할 수도 있습니다.
- 전체 태그는 따옴표 안에 서식을 지정해야 합니다. 예: `tags: ["braze[first_name]"]`. 다른 태그도 지정할 수 있지만 무시됩니다.
- 추가 정보는 [GitHub](https://github.com/looker/actions/tree/master/src/actions/braze)에서 확인할 수 있습니다.

#### 4단계: Looker 액션 보내기

1. `braze_id` 차원이 선택된 모양에서 오른쪽 상단의 설정 톱니(<i class="fas fa-cog"></i>)를 클릭하고 **전송...**을 선택합니다.
2. 사용자 지정 브레이즈 액션을 선택합니다.
3. **고유 키**에서 Braze 계정의 기본 사용자 매핑 키(`external_id` 또는 `braze_id`)를 제공합니다.
4. 내보내기에 이름을 지정합니다. 제공되지 않으면 `LOOKER_EXPORT` 이 사용됩니다.
5. **고급 옵션**에서 **표의 결과** 또는 **모든 결과**를 선택한 다음, **전송**을 선택합니다.<br><br>![][13]<br><br>내보내기가 올바르게 전송된 경우 `LOOKER_EXPORT`는 고객 프로필에서 작업에서 입력한 값과 함께 커스텀 속성으로 표시되어야 합니다.<br><br>![][14]

##### 발신 API 예시

다음은 [`/users/track/` 엔드포인트][10]로 전송되는 발신 API 호출 예제입니다.

###### 헤더
```
Authorization: Bearer [API_KEY]
```

###### 본문
```json
{
   "attributes" : [
      {
        "external_id" : "user_01",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      {
        "external_id" : "user_02",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      {
        "external_id" : "user_03",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      .....
   ]
}
```

### Braze에서 사용자 세분화 {#segment-users}

Braze에서 이러한 플래그가 지정된 사용자의 세그먼트를 만들려면 **참여** 아래의 **세그먼트로** 이동하여 세그먼트의 이름을 지정하고 필터로 **Looker_Export를** 선택합니다. 그런 다음, '값 포함' 옵션을 사용하고 Looker에서 할당한 커스텀 속성 플래그를 제공합니다.

![Braze 세그먼트 빌더에서 "looker_export" 필터는 "includes_value" 및 "Looker"로 설정됩니다.][15]

저장한 후에는 사용자 타겟팅 단계에서 캔버스 또는 캠페인을 생성하는 동안 이 세그먼트를 참조할 수 있습니다.

## 문제 해결
Looker 작업에 문제가 있는 경우 [내부 그룹][16]에 테스트 사용자를 추가하고 다음을 확인합니다.

* API 키에는 `users.track` 권한이 있습니다.
* `https://rest.iad-01.braze.com` 과 같이 올바른 REST 엔드포인트를 입력합니다.
* 차원 보기에 `braze_id` 태그가 설정됩니다.
* 쿼리에 Id 차원 또는 속성이 열로 포함되어 있습니다.
* 뷰어 결과는 피벗되지 않습니다.
* 고유 키가 올바르게 선택되었습니다. 일반적으로 `external_id`입니다.
* 차원의 `braze_id`는 API의 `braze_id`와 다르며, 차원의 `braze_id`는 Braze API의 `id` 필드임을 나타내는 데 사용됩니다. 대부분의 경우 `external_id`를 전송할 때 기본 키입니다.
* `external_id` 사용자는 Braze 플랫폼에 존재합니다.
* `looker_export` 필드는 `Braze Platform > Settings > Manage Settings > Custom Attributes`에서 `Automatically Detect`로 설정됩니다.
* 변경 사항은 프로덕션에 커밋됩니다. Looker Action은 프로덕션 설정에서 작동합니다.

[1]: {{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/
[2]: https://github.com/llooker/braze_message_engagement_block/blob/master/README.md
[3]: https://github.com/llooker/braze_retention_block/blob/master/README.md
[4]: {{site.baseurl}}/user_guide/onboarding_with_braze/integration/
[5]: {{site.baseurl}}/partners/braze_currents/about/
[6]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/
[7]: https://looker.com/solutions/other-databases?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct
[8]: https://dashboard.braze.com/app_settings/developer_console/
[9]: {{site.baseurl}}/api/basics/#endpoints
[10]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[11]: {% image_buster /assets/img/user_track_api.png %}
[12]: {% image_buster /assets/img/braze-looker-action.png %}
[13]: {% image_buster /assets/img/send-looker-action.png %}
[14]: {% image_buster /assets/img/custom-attributes-looker.png %}
[15]: {% image_buster /assets/img/braze_segments.png %}
[16]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/
