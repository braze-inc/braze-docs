---
nav_title: Pinterest
article_title: Canvas Audience Sync to Pinterest
description: "This reference article will cover how to use Braze Audience Sync to Pinterest, to deliver advertisements based upon behavioral triggers, segmentation, and more."
page_order: 5
alias: "/audience_sync_pinterest/"

Tool:
  - Canvas

---

# Audience Sync to Pinterest

Using the Braze Audience Sync to Pinterest, brands can elect to add user data from their own Braze integration to Pinterest Audiences to deliver advertisements based on behavioral triggers, segmentation, and more. Any criteria you'd normally use to trigger a message (push, email, SMS, webhook, etc.) in a Braze Canvas based upon your user data can now be used to trigger an ad to that user in your Pinterest Audiences.

**Common use cases for audience syncing include:**

- Targeting high-value users via multiple channels to drive purchases or engagement
- Retargeting users who are less responsive to other marketing channels
- Creating suppression audiences to prevent users from receiving advertisements when they're already loyal consumers of your brand
- Creating Actalike Audiences to acquire new users more efficiently

This feature allows brands to control what specific first-party data is shared with Pinterest. At Braze, the integrations you can and cannot share your first-party data with are given the utmost consideration. For more information, refer to our [privacy policy](https://www.braze.com/privacy).

{% alert important %}
**Audience Sync Pro disclaimer**<br>
Braze Audience Sync to Pinterest is an Audience Sync Pro integration. 이 통합에 대한 자세한 정보는 Braze 계정 매니저에게 문의하십시오.
{% endalert %}

## Prerequisites 
You must ensure the following items are created, completed, and/or accepted before setting up your Pinterest Audience Step in Canvas.

| Requirement | Origin | Description |
| --- | --- | --- |
| Pinterest Business Hub | [Pinterest](https://www.pinterest.com/business/hub/) | A centralized tool to manage your brand's Pinterest assets (such as ad accounts, pages, apps). |
| Pinterest ad account | [Pinterest](https://ads.pinterest.com/) | An active Pinterest ad account tied to your brand's Pinterest Business Hub.<br><br>Ensure that your Pinterest Business Hub admin has granted you admin permissions to the Pinterest ad accounts you plan to use with Braze. |
| Pinterest 용어 & 정책 | Pinterest | Agree to comply with any of Pinterest’s required terms, policies, guidelines, and documentation related to your use of the Pinterest Audience Sync, including any terms, policies, guidelines, and documentation incorporated by reference therein, which may include: the Terms of Service, Business Terms of Service, Privacy Policy, Developer and API Terms of Service, Ad Data Terms, Advertising Guidelines, Advertising Services Agreement, Community Guidelines, and Brand Guidelines. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration 

### Step 1: Connect to Pinterest

{% alert important %}
Pinterest를 Braze 계정에 연결하려면 ["관리자" 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin)이 필요합니다.
{% endalert %}

In the Braze dashboard, go to **Partner Integrations** > **Technology Partners** and select **Pinterest**. Under Pinterest Audience Sync, select **Connect Pinterest**.

![브레이즈의 핀터레스트 기술 페이지로, 개요 섹션과 핀터레스트 오디언스 동기화 섹션이 포함되어 있으며, 연결된 핀터레스트 버튼이 있습니다.]({% image_buster /assets/img/pinterest/pinterest1.png %}){: style="max-width:80%;"}

You'll then be redirected to the Pinterest OAuth page to authorize Braze for Ad Account Management and Audience Management.

After selecting **Confirm**, you'll be redirected back into Braze to select which Pinterest ad accounts you wish to sync. 

![Pinterest에 연결할 수 있는 사용 가능한 광고 계정 목록.]({% image_buster /assets/img/pinterest/pinterest2.png %}){: style="max-width:80%;"}

When successfully connected, you'll return to the partner page, where you can view which accounts are connected and disconnect existing accounts.

![성공적으로 연결된 광고 계정을 보여주는 Pinterest 기술 파트너 페이지의 업데이트된 버전입니다.]({% image_buster /assets/img/pinterest/pinterest3.png %}){: style="max-width:80%;"}

귀하의 Pinterest 연결은 Braze 작업 공간 수준에서 적용됩니다. If your Pinterest admin removes you from your Pinterest Business Hub or access to the connected Pinterest accounts, Braze will detect an invalid token. As a result, your active Canvases using Pinterest Audience components will show errors, and Braze will not be able to sync users.

### Step 2: Add an Audience Sync Step with Pinterest

Add a component in your Canvas and select **Audience Sync**.

![]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### 3단계: Sync setup

Click on the **Custom Audience** button to open the component editor.

Select **Pinterest** as the desired Audience Sync partner.

![]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Then select your desired Pinterest ad account. Under the **Choose a New or Existing Audience dropdown**, type in the name of a new or existing audience.

{% tabs %}
{% tab Create a New Audience %}

**Create a New Audience**<br>
Enter a name for the new audience, select **Add Users to Audience**, and select which fields you would like to sync with Pinterest. Next, save your audience by clicking the **Create Audience** button at the bottom of the step editor.

![Expanded view of the Custom Audience Canvas step. 여기에서 원하는 광고 계정을 선택하고 새로운 오디언스를 생성합니다.]({% image_buster /assets/img/audience_sync/pinterest_sync.png %})

Braze는 오디언스가 성공적으로 생성되거나 오류가 발생할 경우 단계 편집기 상단에 알림을 표시합니다. Users can reference this audience for user removal later in the Canvas journey because the audience was created in draft mode.

![Canvas 구성 요소에서 새로운 오디언스가 생성된 후 나타나는 경고입니다.]({% image_buster /assets/img/audience_sync/pinterest_sync3.png %})

When you launch a Canvas with a new audience, Braze syncs users in near real-time as they enter the Audience Sync step.
{% endtab %}
{% tab Sync with an Existing Audience %}
**Sync with an Existing Audience**<br>
Braze also offers the ability to add users to existing Pinterest audiences to ensure that these audiences are up-to-date. To sync with an existing audience, type the existing audience name in the dropdown and add it to the audience. Braze will then add users in near real-time as they enter the Audience Sync step.

![Expanded view of the Custom Audience Canvas step. 여기에서 원하는 광고 계정과 기존 오디언스를 선택합니다.]({% image_buster /assets/img/audience_sync/pinterest_sync2.png %})

{% endtab %}
{% endtabs %}

### Step 4: Launch Canvas

Once you have configured your Audience Sync to Pinterest, launch the Canvas! The new audience will be created, and users who flow through the Audience Sync step will be passed into this audience on Pinterest. If your Canvas contains subsequent components, your users will advance to the next step in their user journey.

You can view the audience on Pinterest by entering your ads manager account and selecting Audiences from the Ads dropdown. 오디언스 페이지에서 ~100에 도달한 이후 각 오디언스의 크기를 확인할 수 있습니다.

![오디언스 이름, 오디언스 ID, 오디언스 유형, 오디언스 크기를 포함하는 지정된 Pinterest 오디언스의 오디언스 세부 정보.]({% image_buster /assets/img/pinterest/pinterest11.png %})

## User syncing and rate limit considerations

사용자가 오디언스 동기화 단계에 도달하면 Braze는 Pinterest의 마케팅 API 속도 제한을 준수하면서 거의 실시간으로 동기화합니다. Braze는 Pinterest로 전송하기 전에 5초마다 가능한 많은 사용자를 배치하고 처리합니다.

Pinterest의 세그먼트 API 속도 제한은 사용자당 초당 7개의 쿼리와 요청당 1,900명의 사용자를 허용합니다. 고객이 이 한도에 도달하면 Braze는 최대 ~13시간 동안 동기화를 재시도합니다. 동기화가 여전히 불가능한 경우 Braze는 이러한 사용자를 사용자 오류 메트릭 아래에 나열합니다.

## Understanding analytics

The following table includes metrics and descriptions to help you better understand analytics from your Audience Sync component.

| Metric | Description |
| --- | --- |
| Entered | Number of users who entered this component to be synced to Pinterest. |
| Proceeded to Next Step | How many users advanced to the next component if there is one? All users will auto-advance if this is the last step in the Canvas branch. |
| Users Synced | Number of users who have successfully been synced to Pinterest. |
| Users Not Synced | Number of users that have not been synced due to missing fields to match. |
| Users Pending | Number of users currently being processed by Braze to sync into Pinterest. |
| Users Errored | Number of users who were not synced to Pinterest due to an API error after about 13 hours of retries. Potential causes of errors can include an invalid Pinterest token or if the audience was deleted on Pinterest. |
| Exited Canvas | Number of users who have exited the Canvas. This occurs when the last step in a Canvas is an Audience Sync component. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Remember that there will be a delay in reporting for synced users and errored metrics due to the bulk flusher and the 13-hour retry, respectively.
{% endalert %}   

## Frequently asked questions

### How long will it take for my audiences to populate in Pinterest?

The audience size will update within 24-48 hours on the **Audiences** page in Pinterest's Ads Manager.

### How do I know if users have matched after passing users to Pinterest?

Pinterest does not provide this information for its own data privacy policies.

### What should I do next if I receive an invalid token error?

Confirm with your Pinterest Business Hub admin that you have the appropriate permissions to the ad account you wish to sync. You can also disconnect and reconnect your Pinterest account on the Pinterest partner page. 

### Why is my Canvas not allowed to launch?

Ensure your Pinterest account successfully connects to Braze on the Pinterest partner page. 광고 계정을 선택하고, 새 오디언스의 이름을 입력하고, 일치시킬 필드를 선택했는지 확인합니다.

### Why can't I select my ad account for my Audience Sync step?

Check that your token was generated with the correct account permissions. Note that if you have too many audiences in your Pinterest ad account, the dropdown to select your ad account may timeout. In this case, we recommend reducing the amount of audiences in your ad account.

