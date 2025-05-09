---
nav_title: 전역 대조군
article_title: 전역 대조군
alias: /global_control_group/
page_order: 0

description: "이 도움말에서는 글로벌 제어 그룹을 설정하고 올바르게 사용하는 방법에 대해 설명합니다. 또한 이러한 그룹 사용으로 인해 발생하는 보고서 및 측정기준을 보는 방법도 다룹니다."
page_type: reference
tool: Reports
search_rank: 1

---

# 전역 대조군

> 글로벌 제어 그룹을 사용하여 캠페인이나 캔버스를 수신해서는 안 되는 전체 사용자의 비율을 지정하면 시간에 따른 메시징 활동의 전반적인 영향을 분석할 수 있습니다. 

메시지를 수신한 사용자와 그렇지 않은 사용자의 행동을 비교함으로써 마케팅 캠페인과 캔버스가 세션 및 맞춤 이벤트의 증가로 이어지는 방식을 더 잘 이해할 수 있습니다.

## 글로벌 제어 그룹의 작동 방식

글로벌 제어 그룹을 사용하면 모든 사용자의 비율을 제어 그룹으로 설정할 수 있습니다. 저장하면 그룹의 사용자는 캠페인이나 캔버스를 받지 않습니다. 

글로벌 컨트롤 그룹은 [API 캠페인]({{site.baseurl}}/api/api_campaigns#api-campaigns) 및 뉴스피드 카드(사용 중단됨)를 제외한 모든 채널, 캠페인 및 캔버스에 적용됩니다. 컨트롤 그룹의 사용자는 계속 API 캠페인과 뉴스피드 카드를 받게 됩니다. 이 예외는 콘텐츠 카드에는 적용되지 않으며, 콘텐츠 카드를 사용하는 경우 대조군에 속한 사용자는 콘텐츠 카드를 받지 못합니다.

### 사용자를 글로벌 제어 그룹에 무작위로 할당하기

Braze는 여러 범위의 무작위 [버킷 번호]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute)를 무작위로 선택하고 선택한 버킷의 사용자를 포함합니다. 현재 다른 용도로 랜덤 버킷 번호를 사용 중인 경우 [주의해야 할 사항을](#things-to-watch-for) 확인하세요. 

### 보고를 위한 데이터 추적

Braze는 대조군에 속한 사용자와 치료 샘플에 속한 사용자의 행동을 측정합니다. 치료 샘플은 동일한 무작위 버킷 번호 방법을 사용하여 생성된 대조군에 속하지 않은 사용자 중 무작위로 선택된 것입니다.

### 기능 플래그에서 사용자 제외

글로벌 제어 그룹에 속한 사용자에게는 [기능 플래그를]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) 활성화할 수 없습니다. 즉, 글로벌 제어 그룹에 속한 사용자도 기능 플래그 실험에 참여할 수 없습니다.

## 글로벌 제어 그룹 만들기

### 1단계: 글로벌 제어 그룹 설정으로 이동합니다.

대시보드에서 **오디언스** > **글로벌 제어 그룹으로** 이동합니다.

{% alert note %}
[이전 탐색을]({{site.baseurl}}/navigation) 사용하는 경우 이 페이지는 **참여** > **글로벌 메시지 설정** > **글로벌 제어 그룹 설정** 아래에 있습니다.
{% endalert %}

### 2단계: 이 제어 그룹에 모든 사용자의 비율을 할당합니다.

대조군에 대한 백분율을 입력하고 **저장을** 클릭합니다. 입력하면 Braze는 전역 제어, 치료 및 치료 샘플에 포함될 사용자 수에 대한 추정치를 표시합니다. 워크스페이스에 사용자가 많을수록 이 추정치는 더 정확해진다는 점에 유의하세요. 

글로벌 컨트롤 그룹의 사용자 수는 초기 설정 후 워크스페이스에 사용자가 추가될 때 이 오디언스 비율에 비례하여 유지되도록 자동으로 업데이트됩니다. 예를 들어, 워크스페이스의 사용자 수가 증가하면 글로벌 컨트롤 그룹의 사용자 수도 증가하여 제어군이 워크스페이스 대상의 일정한 비율을 유지하게 됩니다. 비율 가이드라인은 다음 [모범 사례 섹션](#percentage-guidelines)을 참조하세요.

![오디언스 설정이 "모든 사용자의 5%를 글로벌 컨트롤 그룹에 할당"으로 설정된 글로벌 컨트롤 그룹 설정입니다.][4]

### 3단계: 제외 설정 지정

태그를 사용하여 글로벌 제어 그룹에 제외 설정을 추가합니다. 제외 설정에 포함된 태그를 사용하는 캠페인이나 캔버스는 글로벌 관리 그룹을 사용하지 않습니다. 이러한 캠페인과 캔버스는 글로벌 컨트롤 그룹에 속한 사용자를 포함하여 타겟 오디언스의 모든 사용자에게 계속 전송됩니다.

{% alert tip %}
모든 사용자에게 보내야 하는 트랜잭션 메시지가 있는 경우 제외 설정을 추가할 수 있습니다.
{% endalert %}

![글로벌 제어 그룹에 제외 설정을 추가하는 옵션입니다.][5]

### 4단계: 제어 그룹 저장

이 시점에서 Braze는 무작위로 선택된 사용자 그룹을 생성하여 전체 사용자 기반에서 선택한 비율로 구성합니다. 저장하면 제외 설정에 있는 태그가 포함된 캠페인이나 캔버스를 제외하고 현재 활성화된 모든 캠페인과 향후 캔버스가 더 이상 이 그룹의 사용자에게 전송되지 않습니다.

## 글로벌 제어 그룹 비활성화

**글로벌 컨트롤 그룹 설정** 탭에서 언제든지 글로벌 컨트롤 그룹을 비활성화할 수 있지만, 이렇게 하면 이 그룹의 사용자가 캠페인 및 캔버스를 즉시 사용할 수 없게 됩니다.

대조군을 비활성화하기 전에 나중에 참조해야 할 경우를 대비하여 해당 그룹에 속한 사용자의 CSV를 [내보내는](#export-group-members) 것이 좋습니다. 대조군을 비활성화하면 Braze에서 그룹을 복원하거나 이 그룹에 속한 사용자를 식별할 수 있는 방법이 없습니다.

대조군을 비활성화한 후 새 제어 그룹을 저장할 수 있습니다. 백분율을 입력하고 저장하면 Braze에서 무작위로 선택된 새로운 사용자 그룹을 생성합니다. 이전과 동일한 비율을 입력해도 Braze는 대조군 및 치료군에 대한 새 사용자 그룹을 생성합니다.

!["글로벌 메시징 설정을 변경하고 있습니다."라는 제목의 대화 상자가 다음 텍스트와 함께 표시됩니다: "글로벌 컨트롤 그룹이 비활성화되면 더 이상 신규 또는 현재 활성화된 캠페인이나 캔버스에서 제외되지 않습니다. 이 그룹의 사용자는 즉시 메시지를 받을 수 있는 자격을 얻게 됩니다. 계속 진행하시겠습니까?" 버튼을 두 번 클릭합니다. 취소하고 계속 진행합니다.][2]{: style="max-width:50%" }

## 대조군 구성원 내보내기 {#export-group-members}

글로벌 관리 그룹에 어떤 사용자가 있는지 확인하려면 CSV 또는 API로 그룹 구성원을 내보내면 됩니다. 

CSV 내보내기를 실행하려면 **글로벌 제어 그룹 설정** 탭으로 이동하여 <i class="fas fa-download"></i> **내보내기를** 클릭합니다. API로 내보내려면 [`/users/export/global_control_group` 엔드포인트를]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/) 사용하세요.

{% alert important %}
과거 대조군은 보존되지 않으므로 현재 그룹의 구성원만 내보낼 수 있습니다. 대조군을 비활성화하기 전에 필요한 정보를 내보내야 합니다.
{% endalert %}

## 사용자가 글로벌 제어 그룹에 속해 있는지 보기

개별 사용자 프로필의 **참여** 탭에서 **기타** 섹션으로 이동하여 글로벌 컨트롤 그룹 멤버십을 확인할 수 있습니다.

!['기타' 섹션에서 사용자가 임의의 버킷 번호인 2030을 가지고 있으며 글로벌 관리 그룹에 속해 있다고 보고합니다.][1]{: style="max-width:60%;"}

## 보고

Refer to [Global Control Group Reporting]({{site.baseurl}}/user_guide/analytics/reporting/global_control_group_reporting/) for information on report metrics.

## 문제 해결

글로벌 컨트롤 그룹을 설정하고 리포팅을 볼 때 발생할 수 있는 오류는 다음과 같습니다.

| 이슈 | 문제 해결 |
| --- | --- |
| 글로벌 제어 그룹을 지정할 때 입력한 백분율을 저장할 수 없습니다. | 이 문제는 정수가 아닌 숫자 또는 1에서 15 사이(포함)가 아닌 정수를 입력하는 경우에 발생합니다. |
| 전역 제어 설정 페이지에서 "Braze가 글로벌 컨트롤 그룹을 업데이트할 수 없습니다." 오류가 발생합니다. | 이는 일반적으로 이 페이지의 일부 구성 요소가 변경되었음을 나타내며, 다른 사용자가 내 Braze 계정에서 수행한 작업으로 인해 변경되었을 가능성이 높습니다. 이 경우 페이지를 새로고침하고 다시 시도하세요. |
| 글로벌 제어 그룹 보고서에는 데이터가 없습니다. | 글로벌 컨트롤 그룹을 저장하지 않은 상태에서 글로벌 컨트롤 그룹 보고서에 액세스하면 보고서에 데이터가 표시되지 않습니다. 글로벌 제어 그룹을 만들어 저장하고 다시 시도하세요. |
| 전환율이 0%이거나 이벤트가 0건 이상 발생했는데도 그래프가 표시되지 않습니다. | 전환 수가 매우 적고 대조군 또는 치료군이 매우 많은 경우 전환율이 0%로 반올림되어 그래프에 표시되지 않을 수 있습니다. 총 이벤트 수 메트릭을 확인하면 이를 확인할 수 있습니다. 증분 상승률 메트릭을 사용하여 두 그룹의 효과를 비교할 수 있습니다.  |
| 데이터를 보는 기간에 따라 전환율(또는 기타 지표)이 크게 달라지고 있습니다. | 단기간에 걸쳐 데이터를 보는 경우 측정기준이 매일 또는 매주 변동될 수 있습니다. 최소 한 달에 걸쳐 메트릭을 확인하는 것이 좋습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### {#things-to-watch-for} 관련 주의해야 할 사항

#### 중복되는 무작위 버킷 번호

글로벌 컨트롤 그룹은 무작위 버킷 번호를 사용하여 구성되므로 무작위 버킷 번호 세그먼트 필터를 사용하여 다른 테스트를 실행하는 경우, 생성하는 세그먼트와 글로벌 컨트롤 그룹 사용자 간에 중복이 있을 수 있다는 점에 유의하세요.

#### 중복 이메일 주소

외부 사용자 ID가 다른 두 사용자의 이메일 주소가 같고 그 중 한 사용자는 제어 그룹에 속하고 다른 사용자는 그렇지 않은 경우, 제어 그룹이 아닌 사용자가 이메일을 받을 자격이 있을 때마다 해당 이메일 주소로 이메일이 계속 전송됩니다. 이 경우 두 고객 프로필 모두 해당 이메일이 포함된 캠페인 또는 캔버스를 수신한 것으로 표시합니다.

#### 글로벌 제어 그룹 및 메시지별 제어 그룹

글로벌 컨트롤 그룹을 사용할 수도 있고 캠페인별 또는 캔버스별 대조군을 사용할 수도 있습니다. 캠페인별 또는 캔버스별 대조군을 사용하면 특정 메시지의 영향력을 측정할 수 있습니다.

글로벌 관리 그룹의 사용자는 태그 예외가 있는 메시지 외에는 수신이 보류되며, 캠페인이나 캔버스에 관리 기능을 추가하면 Braze는 글로벌 관리 그룹의 일부가 해당 특정 캠페인이나 캔버스를 수신하지 못하도록 보류합니다. 즉, 글로벌 컨트롤 그룹의 구성원이 특정 캠페인이나 캔버스를 받을 자격이 없는 경우 해당 캠페인이나 캔버스에 대한 컨트롤 그룹에도 포함되지 않습니다.

> 즉, 글로벌 컨트롤 그룹의 사용자는 캠페인 또는 캔버스 오디언스에서 진입하기 전에 필터링됩니다. 캠페인 또는 캔버스에 입장한 사용자 중 일정 비율의 사용자가 컨트롤 배리언트에 할당됩니다.

#### 개발자 콘솔의 글로벌 제어 그룹 세그먼트

[API 키]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) 페이지의 **추가 API 식별자** 섹션에 여러 개의 **글로벌 제어** 세그먼트가 표시될 수 있습니다. 이는 글로벌 컨트롤 그룹이 활성화 또는 비활성화될 때마다 새로운 글로벌 컨트롤 그룹이 형성되기 때문입니다. 이렇게 하면 "글로벌 제어 그룹"이라는 레이블이 붙은 여러 세그먼트가 생성됩니다.

이러한 세그먼트 중 하나만 활성화되어 있으며 [`/users/export/global_control_group` 엔드포인트]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)를 사용하여 쿼리하거나 대시보드에서 내보낼 수 있습니다. 대시보드의 내보내기에는 이 글로벌 컨트롤 그룹을 구성하는 하위 세그먼트가 구체적으로 명시되어 있습니다.

## 테스트 모범 사례

### 최적의 대조군 규모 {#percentage-guidelines}

명심해야 할 두 가지 주요 규칙은\*\*입니다:
1. 대조군의 사용자 수는 1,000명 이상이어야 합니다.
2. 대조군은 전체 오디언스의 10%를 넘지 않아야 합니다.

총 오디언스가 10,000명 미만인 경우 비율을 높여 1,000명 이상의 사용자 그룹을 만들어야 하며, 이 경우 비율을 15%보다 높게 늘리지 않아야 합니다. 전체 워크스페이스의 크기가 작을수록 통계적으로 엄격한 테스트를 실행하기가 더 어려워진다는 점을 명심하세요.

- 대조군 규모를 고려할 때 고려해야 할 몇 가지 장단점은 생성된 행동 분석을 신뢰할 수 있으려면 대조군에 상당히 많은 수의 고객이 있어야 한다는 것입니다. 그러나 대조군이 클수록 캠페인을 받는 고객의 수가 적어지므로 인게이지먼트와 전환을 유도하기 위해 캠페인을 사용하는 경우 단점이 있습니다.
- 전체 오디언스의 이상적인 비율은 총 오디언스의 규모에 따라 달라집니다. 총 오디언스가 많을수록 비율은 더 낮아질 수 있습니다. 그러나 오디언스가 적은 경우에는 대조군 비율을 더 크게 설정해야 합니다.

### 실험 기간 

#### 이상적인 기간 선택 {#reshuffle}

대조군 멤버십을 개편하기 전에 실험을 얼마나 오래 실행할지는 테스트 대상과 사용자의 기본 행동에 따라 달라집니다. 잘 모르겠다면 한 분기(3개월)부터 시작하는 것이 좋지만, 한 달보다 짧게 시작하지 않는 것이 좋습니다.

실험에 적합한 시간을 결정하려면 어떤 질문에 답하고자 하는지 고려하세요. 예를 들어 세션에 차이가 있는지 확인하고 싶으신가요? 그렇다면 사용자가 얼마나 자주 유기적으로 세션을 진행하는지 생각해 보세요. 사용자가 매일 세션을 진행하는 브랜드는 사용자가 한 달에 몇 번만 세션을 진행하는 브랜드보다 더 짧은 실험을 진행할 수 있습니다. 

또는 사용자 지정 이벤트에 관심이 있어서 사용자가 해당 사용자 지정 이벤트를 덜 자주 트리거할 가능성이 있는 경우 세션을 검사하는 실험보다 실험을 더 오래 실행해야 할 수도 있습니다.

{% alert tip %}
동일한 대조군을 오래 유지할수록 트리트먼트 그룹과 차이가 커져 편향이 생길 수 있습니다. 글로벌 컨트롤 그룹을 재설정하면 모집단의 밸런스가 재조정됩니다.
{% endalert %}

#### 실험을 조기에 종료하는 것을 제한하세요.

실험을 시작하기 전에 실험을 얼마나 오래 실행할지 결정한 다음, 미리 정해진 시점에 도달한 후에만 실험을 종료하고 최종 결과를 수집해야 합니다. 실험을 조기에 종료하거나 유망한 데이터를 발견할 때마다 실험을 종료하면 편향이 생길 수 있습니다.

#### 가치 있는 메트릭에 대해 생각해 보세요.

가장 관심 있는 지표에 대한 기준 동작을 고려하세요. 연간 단위로만 갱신되는 구독 플랜의 구매 요금에 관심이 있으신가요? 아니면 측정하려는 이벤트에 대한 고객의 주간 습관이 있나요? 사용자가 메시징으로 인해 잠재적으로 행동을 변경하는 데 걸리는 시간을 생각해 보세요. 실험을 실행할 시간을 결정한 후에는 실험을 일찍 종료하거나 최종 결과를 기록하지 않으면 결과가 편향될 수 있으므로 주의하세요.

[1]: {% image_buster /assets/img/control_group/control_group1.png %}
[2]: {% image_buster /assets/img/control_group/control_group2.png %}
[4]: {% image_buster /assets/img/control_group/control_group4.png %}
[5]: {% image_buster /assets/img/control_group/control_group5.png %}
[6]: {% image_buster /assets/img/control_group/control_group6.png %}
