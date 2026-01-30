---
nav_title: Snapchat
article_title: Canvas Audience Sync to Snapchat
description: "This reference article will cover how to use Braze Audience Sync to Snapchat, to deliver advertisements based upon behavioral triggers, segmentation, and more."
page_order: 6
alias: "/audience_sync_snapchat/"

Tool:
  - Canvas

---

# Audience Sync to Snapchat

Using the Braze Audience Sync to Snapchat, brands can add user data from their Braze integration to Snapchat customer lists to deliver advertisements based on behavioral triggers, segmentation, and more. Any criteria you'd normally use to trigger a message (push, email, SMS, webhook, etc.) in a Braze Canvas based on your user data can now be used to trigger an ad to that user in your Snapchat customer lists.

**Common use cases for audience syncing include:**

- Targeting high-value users via multiple channels to drive purchases or engagement
- Retargeting users who are less responsive to other marketing channels
- Creating suppression audiences to prevent users from receiving advertisements when they're already loyal consumers of your brand
- Creating lookalike audiences to acquire new users more efficiently

This feature allows users to control what specific first-party data is shared with Snapchat. At Braze, the integrations you can and cannot share your first-party data with are given the utmost consideration. For more information, refer to our [privacy policy](https://www.braze.com/privacy).

{% alert important %}
**Audience Sync Pro disclaimer**<br>
Braze Audience Sync to Snapchat is an Audience Sync Pro integration. 이 통합에 대한 자세한 내용은 Braze 계정 매니저에게 문의하세요.
{% endalert %}

## Prerequisites 

You must ensure the following items are created, completed and/or accepted before setting up your Snapchat Audience Step in Canvas.

| Requirement | Origin | Description |
| --- | --- | --- |
| Snapchat Business Manager | Snapchat | A centralized tool to manage your brand's Snapchat assets (such as ad accounts, pages, apps). |
| Snapchat ad account | Snapchat | An active Snapchat ad account tied to your brand's Snapchat Business Manager.<br><br>Ensure that your Snapchat Business Manager admin has granted you admin permissions to the Snapchat ad accounts you plan to use with Braze. |
| 스냅챗 약관 & 정책 | [Snapchat](https://www.snap.com/en-US/policies) | Agree to comply with any of Snapchat’s required terms, policies, guidelines, and documentation related to your use of the Snapchat Audience Sync, including any terms, policies, guidelines, and documentation incorporated by reference therein, which may include: the Terms of Service, Business Terms of Service, Developer Terms, Audience Match, Advertising Policies, Commercial Content Policy, Community Guidelines, and Supplier Responsibility. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration 

### Step 1: Connect to Snapchat

{% alert important %}
Snapchat을 Braze 계정에 연결하려면 ['관리자' 권한이]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin) 있어야 합니다.
{% endalert %}

In the Braze dashboard, go to **Partner Integrations** > **Technology Partners** and select **Snapchat**. Under Snapchat Audience Sync, select **Connect Snapchat**.

![개요 섹션과 Snapchat 오디언스 동기화 섹션이 포함된 Braze의 Snapchat 기술 페이지에 연결된 Snapchat 버튼이 있습니다.]({% image_buster /assets/img/snapchat/snapchat1.png %}){: style="max-width:80%;"}

You'll then be redirected to the Snapchat OAuth page to authorize Braze for the permissions related to your Audience Sync integration.

확인을 선택하면 다시 Braze로 리디렉션되어 동기화할 Snapchat 광고 계정을 선택할 수 있습니다. 

![스냅챗에 연결할 수 있는 사용 가능한 광고 계정 목록입니다.]({% image_buster /assets/img/snapchat/snapchat2.png %}){: style="max-width:80%;"}

연결에 성공하면 파트너 페이지로 돌아가 연결된 계정을 확인하고 기존 계정을 연결 해제할 수 있습니다.

![광고 계정이 성공적으로 연결되었음을 보여주는 업데이트된 버전의 Snapchat 기술 파트너 페이지입니다.]({% image_buster /assets/img/snapchat/snapchat3.png %}){: style="max-width:80%;"}

Snapchat 연결은 Braze 워크스페이스 수준에서 적용됩니다. If your Snapchat admin removes you from your Snapchat Business Manager or access to the connected Snapchat ad accounts, Braze will detect an invalid token. As a result, your active Canvases using Snapchat will show errors, and Braze will not be able to sync users.

### Step 2: Add an Audience Sync Step with Snapchat

Add a component in your Canvas and select **Audience Sync**.

![]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### 3단계: Sync setup

Click on the **Custom Audience** button to open the component editor.

Select **TikTok** as the desired Audience Sync partner.

![]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Then select your desired Snapchat ad account. Under the **Choose a New or Existing Audience** dropdown, type in the name of a new or existing audience.

{% tabs %}
{% tab Create a New Audience %}

**Create a New Audience**<br>
Enter a name for the new audience, select **Add Users to Audience**, and select which fields you would like to sync with Snapchat. Next, save your audience by clicking the **Create Audience** button at the bottom of the step editor.

![Expanded view of the Custom Audience Canvas step. 여기에서 원하는 광고 계정을 선택하면 새 오디언스가 생성됩니다.]({% image_buster /assets/img/audience_sync/snapchat3.png %})

Braze는 오디언스가 성공적으로 생성되거나 오류가 발생하면 단계 편집기 상단에 알림을 표시합니다. Users can reference this audience for user removal later in the Canvas journey because the audience was created in draft mode.

![캔버스 구성 요소에서 새 오디언스가 생성된 후 표시되는 알림입니다.]({% image_buster /assets/img/audience_sync/snapchat2.png %})

When you launch a Canvas with a new audience, Braze syncs users in near real-time as they enter the Audience Sync component.

{% endtab %}
{% tab Sync with an Existing Audience %}
**Sync with an Existing Audience**<br>
Braze also offers the ability to add users to existing Snapchat audiences to ensure that these audiences are up-to-date. To sync with an existing audience, type the existing audience name in the dropdown and **Add to the Audience**. Braze will then add users in near real-time as they enter the Audience Sync component.

![Expanded view of the Custom Audience Canvas step. 여기에서 원하는 광고 계정과 기존 오디언스가 선택됩니다.]({% image_buster /assets/img/audience_sync/snapchat.png %})

{% endtab %}
{% endtabs %}

### Step 4: Launch Canvas

Once you have configured your Audience Sync to Snapchat, launch the Canvas! A new audience will be created, and users who flow through the Audience Sync step will be passed into this audience on Snapchat. If your Canvas contains subsequent components, your users will advance to the next step in their user journey.

You can view the audience in Snapchat by entering your ads manager account and selecting **Audiences** from the Assets section of the navigation. From the **Audiences** page, you can see the size of each audience after it reaches ~1,000.

![Audience details for a given Snapchat audience that includes audience name, audience type, audience size, and audience retention in days.]({% image_buster /assets/img/snapchat/snapchat7.png %})

## User syncing and rate limit considerations

사용자가 오디언스 동기화 단계에 도달하면, Braze는 Snapchat의 API 속도 제한을 준수하면서 거의 실시간으로 동기화합니다. Braze는 5초마다 가능한 한 많은 사용자를 일괄 처리하여 Snapchat으로 보내기 전에 처리합니다.

Snapchat의 API 속도 제한은 초당 쿼리 10건, 요청당 사용자 수 10만 명을 넘지 못하도록 설정되어 있습니다. 고객이 이 제한에 도달하면 Braze는 최대 13시간 동안 동기화를 다시 시도합니다. 그래도 동기화가 되지 않으면 Braze는 이러한 사용자를 사용자 오류 측정기준 아래에 나열합니다.

### Understanding analytics

The following table includes metrics and descriptions to help you better understand analytics from your Audience Sync component.

| Metric | Description |
| --- | --- |
| Entered | Number of users who entered this component to be synced to Snapchat. |
| Proceeded to Next Step | How many users advanced to the next component if there is one? All users will auto-advance if this is the last step in the Canvas branch. |
| Users Synced | Number of users who have successfully been synced to Snapchat. |
| Users Not Synced | Number of users that have not been synced due to missing fields to match. |
| Users Pending | Number of users currently being processed by Braze to sync into Snapchat. |
| Users Errored | Number of users who were not synced to Snapchat due to an API error after about 13 hours of retries. Potential causes of errors can include an invalid Snapchat token or if the audience was deleted on Snapchat. |
| Exited Canvas | Number of users who have exited the Canvas. This occurs when the last step in a Canvas is an Audience Sync component. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Remember that there will be a delay in reporting for synced users and errored metrics due to the bulk flusher and the 13-hour retry, respectively.
{% endalert %}   

## Frequently asked questions

### How many audiences can Snapchat support

At this time, you can only have 1,000 audiences within your Snapchat account. 

If you exceed this limit, Braze will notify you that we can't create new audiences. You'll need to remove audiences you're no longer using in your Snapchat ad account.

### How do I know if users have matched after passing users to Snapchat?

Snapchat doesn't provide this information for their data privacy policies.

### What should I do next if I receive an invalid token error?

You can disconnect and reconnect your Snapchat account on the Snapchat partner page. Confirm with your Snapchat Business Manager admin that you have the appropriate permissions to the ad account you wish to sync with.

### Why is my Canvas not allowed to launch?

Make sure your Snapchat ad account successfully connects to Braze on the Snapchat partner page. Check that you've selected an ad account, entered a name for the new audience, and selected fields to match.


