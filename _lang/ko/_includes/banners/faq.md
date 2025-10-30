# 배너: 자주 묻는 질문

> 이것은 Braze의 배너에 대한 자주 묻는 질문에 대한 답변입니다. 더 일반적인 정보는 [배너에 대한 정보]({% if include.section == "user" %}{{site.baseurl}}/user_guide/채널별_메시지_구성/배너{% elsif include.section == "developer" %}{{site.baseurl}}/developer_가이드/배너{% endif %}).

## 배너 업데이트는 사용자가 언제 나타납니까?

배너는 새로고침 메서드를 호출할 때마다 최신 데이터로 새로 고쳐지며, 배너 캠페인을 다시 전송하거나 업데이트할 필요가 없습니다.

## 세션에서 요청할 수 있는 배치 수는 몇 개입니까?

단일 새로고침 요청에서 최대 10개의 배치를 요청할 수 있습니다. 요청한 각 배치에 대해 Braze는 사용자가 자격이 있는 가장 높은 우선 순위의 배너를 반환합니다. 추가 요청은 오류를 반환합니다.

자세한 내용은 [배치 요청]({% if include.section == "user" %}{{site.baseurl}}/user_guide/채널별_메시지_구성/배너#요청{% elsif include.section == "developer" %}{{site.baseurl}}/developer_가이드/배너#요청{% endif %}).

## 동시에 활성화할 수 있는 배너 캠페인은 몇 개입니까?

각 작업 공간은 최대 200개의 활성 배너 캠페인을 지원할 수 있습니다. 이 한도에 도달하면 새 캠페인을 만들기 전에 기존 캠페인을 [아카이브하거나 비활성화]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status)해야 합니다.

## 배치를 공유하는 캠페인에서 어떤 배너가 먼저 표시됩니까?

사용자가 동일한 배치를 공유하는 여러 배너 캠페인에 자격이 있는 경우, 가장 높은 우선 순위의 배너가 표시됩니다. 자세한 내용은 [배너 우선 순위]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "개발자" %}{{site.baseurl}}/developer_가이드/배너#우선순위{% endif %}).

## 기존 콘텐츠 카드 피드에서 배너를 사용할 수 있습니까?

배너는 콘텐츠 카드와 다르므로 같은 피드에서 배너와 콘텐츠 카드를 사용할 수 없습니다. 기존 콘텐츠 카드 피드를 배너로 교체하려면 [앱이나 웹사이트에 배치를 생성해야 합니다.]({{site.baseurl}}/developer_guide/banners/placements/).

## 사용자가 배너를 수동으로 닫을 수 있습니까?

아니요. 사용자는 배너를 수동으로 닫을 수 없습니다. 그러나 사용자 세그먼트 자격을 관리하여 배너 가시성을 제어할 수 있습니다. 사용자가 배너 캠페인에 대한 타겟팅 기준을 더 이상 충족하지 않으면, 다음 세션에서 다시는 배너를 보지 않게 됩니다.

예를 들어, 사용자가 구매를 할 때까지 프로모션 배너를 표시하는 경우, `purchase_completed`과 같은 이벤트를 기록하면 해당 사용자가 타겟 세그먼트에서 제거되어 이후 세션에서 배너가 숨겨질 수 있습니다.

## Braze API를 사용하여 배너 캠페인 분석을 내보낼 수 있나요?

예. [`/campaigns/data_series` 엔드포인트]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)를 사용하여 몇 개의 배너 캠페인이 조회되었는지, 클릭되었는지 또는 전환되었는지에 대한 데이터를 얻을 수 있습니다.

## 사용자는 언제 세그먼트화되나요?

사용자는 세션 시작 시 세그먼트화됩니다. 캠페인의 타겟 세그먼트가 커스텀 속성, 커스텀 이벤트 또는 기타 타겟팅 속성에 의존하는 경우, 세션 시작 시 사용자에게 존재해야 합니다.

## 최소 지연 시간을 보장하기 위해 배너를 어떻게 구성할 수 있나요?

배너의 메시지가 간단할수록 더 빠르게 렌더링됩니다. 배너 캠페인을 사용 사례에 대한 예상 지연 시간과 비교하여 테스트하는 것이 가장 좋습니다. 예를 들어, `catalog_items`과 같은 Liquid 속성을 테스트해야 합니다.

## 모든 Liquid 태그가 지원되나요?

아니요. 그러나 대부분의 Liquid 태그는 배너 메시지에 대해 지원되며, `catalog_items`은 [`:rerender` 태그]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid)를 사용하여 다시 렌더링됩니다.

## 클릭 이벤트를 캡처할 수 있나요?

클릭 이벤트는 `logClick` 요소에 클릭 시 동작이 설정되고 [JS 브리지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#javascript-bridge)를 사용하여 호출되는 경우에만 캡처됩니다.
