---
nav_title: Criteo
article_title: Canvas Audience Sync to Criteo
description: "This reference article will cover how to use Braze Audience Sync to Criteo, to deliver advertisements based upon behavioral triggers, segmentation, and more."
page_order: 1
alias: /audience_sync_criteo/

Tool:
  - Canvas
---

# Audience Sync to Criteo

Using the Braze Audience Sync to Criteo, brands can elect to add user data from their own Braze integration to Criteo customer lists to deliver advertisements based on behavioral triggers, segmentation, and more. Any criteria you’d normally use to trigger a message (push, email, SMS, webhook, etc.) in a Braze Canvas based on your user data can now be used to trigger an ad to that user in your Criteo customer lists.

**Common use cases for audience syncing include:**

- Targeting high-value users via multiple channels to drive purchases or engagement
- Retargeting users who are less responsive to other marketing channels
- Creating suppression audiences to prevent users from receiving advertisements when they’re already loyal consumers of your brand
- Creating Lookalike Audiences to acquire new users more efficiently

This feature gives brands the option to control what specific first-party data is shared with Criteo. At Braze, the integrations you can and cannot share your first-party data with are given the utmost consideration. For more information, refer to our [privacy policy](https://www.braze.com/privacy).

{% alert important %}
**Audience Sync Pro disclaimer**<br>
Braze Audience Sync to Criteo is an Audience Sync Pro integration. 이 통합에 대한 자세한 내용은 Braze 계정 매니저에게 문의하세요. <br> 
{% endalert %}

## 필수 조건 

크리테오에 오디언스 동기화를 설정하기 전에 다음 항목을 생성 및/또는 완료했는지 확인해야 합니다.

| Requirement | Origin | Description |
| --- | --- | --- |
| Criteo ad account | [Criteo](https://marketing.criteo.com/) | An active Criteo ad account tied to your brand.<br><br>Ensure that your Criteo admin has granted you the appropriate permissions to access Audiences. |
| [Criteo Advertising Guidelines](https://www.criteo.com/advertising-guidelines/)<br>and<br>[Criteo Brand Safety Guidelines](https://www.criteo.com/wp-content/uploads/2017/11/Criteo-Brand-Safety-Guidelines-UK-March-2016.pdf) | Criteo | As an active Criteo customer, you must ensure that you can comply with Criteo’s Advertising and Brand Safety Guidelines prior to launching any Criteo campaigns. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration 

### Step 1: Connect to Criteo

{% alert important %}
Braze 계정에 크리테오를 연결하려면 ['관리자' 권한이]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin) 있어야 합니다.
{% endalert %}

In the Braze dashboard, go to **Partner Integrations** > **Technology Partners** and select **Criteo**. Under Criteo Audience Export, select **Connect Criteo**.

![Braze의 크리테오 기술 페이지에는 개요 섹션과 연결된 크리테오 버튼이 있는 크리테오 섹션이 포함되어 있습니다.]({% image_buster /assets/img/criteo/criteo5.png %}){: style="max-width:80%;"}

오디언스 동기화 통합과 관련된 권한에 대해 Braze에 권한을 부여하는 크리테오 oAuth 페이지가 나타납니다.

Once you have selected confirm, you’ll then be redirected back into Braze to select which Criteo ad accounts you wish to sync to. 

![Criteo에 연결할 수 있는 사용 가능한 광고 계정 목록.]({% image_buster /assets/img/criteo/criteo7.png %}){: style="max-width:80%;"}

연결에 성공하면 파트너 페이지로 돌아가서 어떤 계정이 연결되어 있는지 확인하고 기존 계정의 연결을 해제할 수 있습니다.

![광고 계정이 성공적으로 연결되었음을 보여주는 Criteo 기술 파트너 페이지의 업데이트된 버전.]({% image_buster /assets/img/criteo/criteo4.png %}){: style="max-width:80%;"}

Criteo 연결은 Braze 워크스페이스 수준에서 적용됩니다. If your Criteo admin removes you from your Criteo ad account, Braze will detect an invalid token. As a result, your active Canvases using Criteo will show errors, and Braze will not be able to sync users.

### Step 2: Configure your Canvas entry criteria

When building audiences for Ad Tracking, you may wish to include or exclude certain users based on their preferences, and in order to comply with privacy laws, such as the “Do Not Sell or Share” right under the [CCPA](https://oag.ca.gov/privacy/ccpa). Marketers should implement the relevant filters for users’ eligibility within their Canvas entry criteria. Below we list some options.

If you have collected the [iOS IDFA through the Braze SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), you will be able to use the Ads Tracking Enabled filter. Select the value as true to only send users into Audience Sync destinations where they have opted in.

![]({% image_buster /assets/img/criteo/criteo11.png %})

If you are collecting `opt-ins`, `opt-outs`, `Do Not Sell Or Share`, or any other relevant custom attributes, you should include these within your Canvas entry criteria as a filter:

![]({% image_buster /assets/img/criteo/criteo12.png %})

To learn more on how to comply with these Data Protection laws within the Braze platform, see [Data Protection Technical Assistance]({{site.baseurl}}/dp-technical-assistance/).

### Step 3: Add an Audience Sync Step with Criteo

Add a component in your Canvas and select **Audience Sync**.

![캔버스에서 크리테오 오디언스 컴포넌트를 추가하는 이전 단계의 워크플로입니다.]({% image_buster /assets/img/criteo/criteo9.png %}){: style="max-width:35%;"} ![캔버스에서 크리테오 오디언스 컴포넌트를 추가하는 이전 단계의 워크플로입니다.]({% image_buster /assets/img/criteo/criteo10.png %}){: style="max-width:28%;"}

### 4단계: Sync setup

Click on the **Custom Audience** button to open the component editor.

Select **Criteo** as the desired Audience Sync partner. 

![]({% image_buster /assets/img/criteo/criteo6.png %})

Then select your desired Criteo ad account. Under the **Choose a New or Existing Audience** dropdown, type in the name of a new or existing audience.

{% tabs %}
{% tab Create a New Audience %}
**Create a New Audience**<br>
Enter a name for the new audience, select **Add Users to Audience**, and select which fields you would like to sync with Criteo. Next, save your audience by clicking the **Create Audience** button at the bottom of the step editor.

![Expanded view of the Custom Audience Canvas step. 여기에서 원하는 광고 계정을 선택하면 새 오디언스가 생성됩니다.]({% image_buster /assets/img/criteo/criteo3.png %})

Braze는 오디언스가 성공적으로 생성되거나 오류가 발생하면 단계 편집기 상단에 알림을 표시합니다. Users can reference this audience for user removal later in the Canvas journey because the audience was created in draft mode.

![캔버스 구성 요소에서 새 오디언스가 생성된 후 표시되는 알림입니다.]({% image_buster /assets/img/criteo/criteo1.png %})

When you launch a Canvas with a new audience, Braze syncs users in near real-time as they enter the Audience Sync component.
{% endtab %}
{% tab Sync with an Existing Audience %}
**Sync with an Existing Audience**<br>
Braze also offers the ability to add users to existing Criteo audiences to ensure that these audiences are up-to-date. To sync with an existing audience, type the existing audience name in the dropdown and **Add to the Audience**. Braze will then add users in near real-time as they enter the Audience Sync component.

![Expanded view of the Custom Audience Canvas step. 여기에서 원하는 광고 계정과 기존 오디언스가 선택됩니다.]({% image_buster /assets/img/criteo/criteo8.png %})

{% endtab %}
{% endtabs %}

### Step 5: Launch Canvas

Once you have configured your Audience Sync to Criteo, simply launch the Canvas! The new audience will be created, and users who go through the Audience Sync step will be passed into this audience on Criteo. If your Canvas contains subsequent components, your users will then advance to the next step in their user journey.

You can view the audience in Criteo by going into your ads manager account and then selecting Segments from the **Audience Library** of the navigation. **세그먼트** 페이지에서 최대 1,000명에 도달한 후 각 오디언스의 크기를 확인할 수 있습니다.

![세그먼트, ID, 소스, 유형, 크기, 현재 사용량, 마지막 업데이트가 표시된 오디언스 라이브러리.]({% image_buster /assets/img/criteo/criteo.png %})

## User syncing and rate limit considerations

사용자가 오디언스 동기화 단계에 도달하면, Braze는 크리테오의 API 속도 제한을 준수하면서 거의 실시간으로 동기화합니다. Braze는 5초마다 최대한 많은 사용자를 배치하고 처리한 후 크리테오로 전송합니다.

크리테오의 API 속도 제한은 분당 250건 이하의 요청만 허용합니다. 고객이 이 제한에 도달하면 Braze는 최대 13시간 동안 동기화를 다시 시도합니다. 그래도 동기화가 되지 않으면 Braze는 이러한 사용자를 사용자 오류 측정기준 아래에 나열합니다. 

## Understanding analytics

The following table includes metrics and descriptions to help you better understand analytics from your Audience Sync component.

| Metric | Description |
| --- | --- |
| Entered | Number of users who entered this component to be synced to Criteo. |
| Proceeded to Next Step | How many users advanced to the next component if there is one. All users will auto-advance if this is the last step in the Canvas branch. |
| Users Synced | Number of users who have successfully been synced to Criteo. |
| Users Not Synced | Number of users that have not been synced due to missing fields to match. |
| Users Pending | Number of users currently being processed by Braze to sync into Criteo. |
| Users Errored | Number of users who were not synced to Criteo due to an API error after about 13 hours of retries. Potential causes of errors can include an invalid Criteo token or if the audience was deleted on Criteo. |
| Exited Canvas | Number of users who have exited the Canvas. This occurs when the last step in a Canvas is an Audience Sync component. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Remember that there will be a delay in reporting for users synced and users errored metrics due to the bulk flusher and the 13-hour retry, respectively.
{% endalert %}

## Frequently asked questions

### What should I do next if I receive an invalid token error?
You can simply disconnect and reconnect your Criteo account on the Criteo partner page. Ensure with your Criteo admin that you have the appropriate permissions to the ad account you wish to sync with.

### Why is my Canvas not allowed to launch?

Confirm that your Criteo ad account has successfully connected to Braze on the Criteo partner page. Next, check that you've selected an ad account, entered a name for the new audience, and selected fields to match.

### How do I know if users have matched after passing users to Criteo?

Criteo does not provide this information for their own data privacy policies.

### How many audiences can Criteo support?

At this time, you can only have 1,000 audiences within your Criteo account. If you're exceed this limit, Braze will notify you that we are unable to create new audiences. You'll need to remove audiences that you're no longer using in your Criteo ad account.


