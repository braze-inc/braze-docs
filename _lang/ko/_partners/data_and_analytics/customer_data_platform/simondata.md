---
nav_title: SimonAI
article_title: SimonAI
description: "Braze와 SimonAI 통합을 사용하면 코드 없이 실시간으로 오케스트레이션을 위해 정교한 오디언스를 생성하고 Braze에 동기화할 수 있습니다."
alias: /partners/simon_data/
page_type: partner
search_tag: Partner
---

# Simon AI

> [Simon AI][1] 에이전틱 마케팅 플랫폼은 마케팅 팀이 진정한 일대일 개인화를 달성할 수 있도록 지원합니다. 컴포저블 CDP와 Snowflake AI 데이터 클라우드에서 직접 작동하는 AI 에이전트를 결합하여 마케터의 데이터 및 실행 팀 역할을 수행합니다.

Braze와 Simon AI 통합을 사용하여 코드 없이 실시간 오케스트레이션을 위해 고급 오디언스를 구축하고 Braze에 동기화할 수 있습니다. 이 통합을 통해 Simon AI의 신원 확인, 고객 데이터 통합, AI 중심 세그먼트를 활용하여 더욱 개인화되고 영향력 있는 Braze 캠페인을 다운스트림에서 진행할 수 있습니다.

## 필수 조건

시작하려면 Simon AI 계정에서 Braze 계정을 인증해야 합니다.

| Requirement         | 설명                                                                                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Simon AI          | Simon AI 내에서 Braze 통합 기능을 활용하려면 기존 Simon AI 계정이 있어야 합니다.                                                                    |
| Braze REST API key  | A Braze REST API key with `users.track`, `campaigns.trigger.schedule.create`, and `campaigns.trigger.send` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze Dashboard URL | [Your REST endpoint URL][3]. Your endpoint will depend on the Braze URL for your instance.                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases

- Trigger a Braze Canvas or email  
- Pass and maintain Segment Properties
- Sync Traits and Contact Properties

{% alert note %}  
When using the Simon and Braze integration, Simon only sends deltas on each sync to Braze avoiding costs for irrelevant data. See [Sync Traits and Contact Properties](#sync-traits-and-contact-properties) for more.
{% endalert %}

## Integration

### Simon AI에서 Braze 계정 인증하기

To use the Braze integration, first authenticate your Braze account in Simon:

1. From the left navigation, click **Integrations** then scroll to Braze.
2. Enter your Braze [REST API key][2] and your [dashboard URL][3].
3. Click **Save Changes**.

A successful connection displays **Connected** in the window.

![Simon AI의 통합 화면][8]{: style="max-width:70%"}

### Simon AI에서 흐름 또는 여정에 Braze 작업 추가하기

Simon AI에서 Braze 계정을 인증한 후에는 [흐름과][4] [여정에][5] Braze 작업을 추가할 수 있습니다.

Three actions are available:

- **Sync Simon segment attribute**: Sync your segment details with a new or existing custom attribute in Braze.
- **Trigger a Braze Canvas**: Trigger a Braze Canvas that leverages your Simon segment data.
- **Send a Braze campaign**: Launch an entire Braze campaign from Simon.

![Simon AI에서 사용 가능한 Braze 액션 목록을 보여주는 드롭다운][9]{: style="max-width:60%"}

Some actions are only available for specific Flow types or Journeys alone. Learn more at [docs.simondata.com][6].

### Sync traits and contact properties

To minimize data consumption, you can choose specific traits to sync by default, rather than updating every field for all customers in a segment.

{% alert note %}
To get started with trait syncing, submit a request in the [Simon Support Center](https://docs.simondata.com/docs/support-center). Your account manager will let you know when you can proceed with the following steps.
{% endalert %}

After Contact Traits is activated by your account manager:

1. In Simon, expand **Admin Center** in the left navigation and select **Sync Contact Traits**.
2. Choose **Braze**. Contact properties are displayed here, nested by dataset.
3. Select any fields you want synced when you use the Simon and Braze integration:
   1. **Number or traits** indicates how many traits are available to choose from in that dataset. You can choose all or expand the row to select individual fields.
   2. Edit the **Downstream name** if you want the field names to appear differently when they arrive in Braze.
   3. If this is your first time integrating with Braze from Simon, click **Backfill all contacts**. Backfilling sends all the data points to Braze the first time you use an action in a flow or journey to be sure all your data is fully in sync. Then on subsequent syncs, only the traits you choose in this screen are sent to Braze. This helps to make sure you're only charged for the data you need.

![Simon AI에서 동기화 특성 선택하기.][10]

[1]: https://www.simondata.com




[1]: https://www.simondata.com
[2]: {{site.baseurl}}/api/basics/#creating-and-managing-rest-api-keys
[3]: {{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints
[4]: https://docs.simondata.com/docs/campaigns-flows
[5]: https://docs.simondata.com/docs/campaigns-journeys-two
[6]: https://docs.simondata.com
[7]: https://docs.simondata.com/docs/support-center
[8]: {% image_buster /assets/img/simon_data/ConnecttoBraze.png %}  
[9]: {% image_buster /assets/img/simon_data/BrazeActions.png %}
[10]: {% image_buster /assets/img/simon_data/BrazeTraitSyncing.png %}

