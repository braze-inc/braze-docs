---
nav_title: TikTok
article_title: Canvas Audience Sync to TikTok
alias: /tiktok_audience_sync/
description: "This reference article will cover how to use Braze Audience Sync to TikTok to deliver advertisements based upon behavioral triggers, segmentation, and more."
Tool:
  - Canvas
page_order: 7

---

# Audience Sync to TikTok

Using the Braze Audience Sync to TikTok, brands can elect to add user data from their own Braze integration to TikTok Audiences to deliver advertisements based on behavioral triggers, segmentation, and more. Any criteria you’d normally use to trigger a message (push, email, SMS, webhook, etc.) in a Braze Canvas. 

**Common use cases for Audience Syncing include**:

- Targeting high-value users via multiple channels to drive purchases or engagement
- Retargeting users who are less responsive to other marketing channels
- Creating suppression audiences to prevent users from receiving advertisements when they're already loyal consumers of your brand
- Creating Actalike Audiences to acquire new users more efficiently

This feature lets brands control what specific first-party data is shared with TikTok. At Braze, the integrations you can and cannot share your first-party data with are given the utmost consideration. For more information, refer to our [privacy policy](https://www.braze.com/privacy).

{% alert important %}
**Audience Sync Pro disclaimer**<br>
Braze Audience Sync to TikTok is an Audience Sync Pro integration. 이 통합에 대한 자세한 정보는 Braze 계정 매니저에게 문의하십시오.
{% endalert %}

## Prerequisites

You must ensure the following items are created, completed, and/or accepted before setting up your TikTok Audience Step in Canvas.

| Requirement | Origin | Description |
| ----------- | ------ | ----------- |
| TikTok for Business Center Account | [TikTok](https://business.tiktok.com/) | A centralized tool to manage your brand's TikTok assets (such as ad accounts, pages, apps). |
| TikTok Ad Account | [TikTok](https://ads.tiktok.com/) | An active TikTok ad account tied to your brand's Business Center account.<br><br>Ensure that your TikTok Business Center manager admin has granted you admin permissions to the TikTok ad accounts you plan to use with Braze. |
| TikTok 용어 & 정책 | [TikTok](https://ads.tiktok.com/i18n/official/policy/terms) | Agree to comply with any of TikTok’s required terms, policies, guidelines, and documentation related to your use of the Pinterest Audience Sync, including any terms, policies, guidelines, and documentation incorporated by reference therein, which may include: the Commercial Terms of Service, Advertising Terms, Privacy Policy, Custom Audience Terms, Developer Terms of Service, Developer Data Sharing Agreement, Advertising Policies, Brand Guidelines, and Community Guidelines. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration 

### Step 1: Connect to TikTok

{% alert important %}
TikTok을 Braze 계정에 연결하려면 ["관리자" 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin)이 필요합니다.
{% endalert %}

In the Braze dashboard, go to **Partner Integrations** > **Technology Partners** and select **TikTok**. Under TikTok Audience Sync, select **Connect TikTok**.

![Braze의 틱톡 기술 페이지에는 개요 섹션과 연결된 틱톡 버튼이 있는 틱톡 오디언스 동기화 섹션이 있습니다.]({% image_buster /assets/img/tiktok/tiktok1.png %}){: style="max-width:75%;"}

You'll then be redirected to the TikTok OAuth page to authorize Braze for ad account management and Audience Management. After you have selected **Confirm**, you'll be redirected back into Braze to select which TikTok ad accounts you wish to sync to. 

![]({% image_buster /assets/img/tiktok/tiktok2.png %}){: style="max-width:75%;"}

Once successfully connected, you will return to the partner page. Here, you can view which accounts are connected and disconnect existing accounts.

![]({% image_buster /assets/img/tiktok/tiktok3.png %}){: style="max-width:75%;"}

Your TikTok connection will be applied at the Braze app-group level. If your TikTok admin removes you from your TikTok Business Center or access to the connected TikTok accounts, Braze will detect an invalid token. As a result, your active Canvases using TikTok Audience components will show errors, and Braze will not be able to sync users.

### 2단계: 캔버스에 TikTok 오디언스 구성 요소 추가

Add a component in your Canvas and select **Audience Sync**. 

![]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### 3단계: Sync setup

Click on the **Custom Audience** button to open the component editor.

Select **TikTok** as the desired Audience Sync partner.

![]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Then select the desired TikTok ad account. Under the **Choose a New or Existing Audience** dropdown, type in the name of a new or existing audience.

![]({% image_buster /assets/img/tiktok/tiktok11.png %})

{% tabs %}
{% tab Create a New Audience %}

**Create a New Audience**<br>
Enter a name for the new audience, select **Add Users to Audience**, and select which fields you would like to sync with TikTok. Next, save your audience by clicking the **Create Audience** button at the bottom of the step editor.

![]({% image_buster /assets/img/audience_sync/tiktok3.png %})

Braze는 오디언스가 성공적으로 생성되거나 오류가 발생할 경우 단계 편집기 상단에 알림을 표시합니다. Users can reference this audience for user removal later in the Canvas journey because the audience was created in draft mode.

![]({% image_buster /assets/img/audience_sync/tiktok2.png %})

When you launch a Canvas with a new audience, Braze syncs users in near real-time as they enter the audience step.

{% endtab %}
{% tab Sync with an Existing Audience %}

**Sync with an Existing Audience**<br>
Braze also offers the ability to add users to existing TikTok audiences to ensure that these audiences are up-to-date. To sync with an existing audience, type the existing audience name in the dropdown and **Add to the Audience**. Braze will then add users in near real-time as they enter the TikTok Audience step.

![Expanded view of the Custom Audience Canvas step. 여기에서 원하는 광고 계정과 기존 오디언스가 선택됩니다.]({% image_buster /assets/img/audience_sync/tiktok.png %})

{% endtab %}
{% endtabs %}

### Step 4: Launch Canvas
Once you have configured your TikTok Audience component, simply launch the Canvas! A new audience will be created, and users who flow through the TikTok Audience component will be passed into this audience on TikTok. If your Canvas contains subsequent components, your users will advance to the next step in their user journey.

You can view the audience in TikTok by entering your **Ads Manager Account** and selecting **Audiences** from the **Assets** dropdown. **오디언스** 페이지에서 최대 1,000명에 도달한 후 각 오디언스의 규모를 확인할 수 있습니다.

![지정된 오디언스에 대한 다음 측정지표가 나열된 TikTok 페이지입니다.]({% image_buster /assets/img/tiktok/tiktok5.png %})

## User syncing and rate limit considerations

사용자가 오디언스 동기화 단계에 도달하면 Braze는 TikTok의 마케팅 API 속도 제한을 준수하면서 거의 실시간으로 동기화합니다. Braze는 TikTok으로 전송하기 전에 5초마다 가능한 많은 사용자를 배치하고 처리합니다.

TikTok의 세그먼트 API 속도 제한은 초당 50개의 쿼리와 요청당 10,000명의 사용자를 허용합니다. 고객이 이 한도에 도달하면 Braze는 최대 ~13시간 동안 동기화를 재시도합니다. 동기화가 여전히 불가능한 경우 Braze는 이러한 사용자를 사용자 오류 메트릭 아래에 나열합니다.

## Understanding analytics

The following table includes metrics and descriptions to help you better understand analytics from your Audience Sync component.

| Metric | Description |
| ------ | ----------- |
| Entered | Number of users who entered this component to be synced to TikTok. |
| Proceeded to Next Step | Number of users that advanced to the next component if one exists. All users will auto-advance if this is the last step in the Canvas branch. |
| Users Synced | Number of users who have successfully been synced to TikTok. Note that this does not equate to users matched on TikTok. |
| Users Not Synced | Number of users that have not been synced due to missing fields to match. |
| Users Pending | Number of users currently being processed by Braze to sync into TikTok. |
| Users Errored | Number of users who were not synced to TikTok due to an API error after about 13 hours of retries. Potential causes of errors can include an invalid TikTok token or if the audience was deleted on TikTok. |
| Exited Canvas | Number of users who have exited the Canvas. This occurs when the last step in a Canvas is an Audience sync component. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Remember that there will be a delay in reporting for users synced and users errored metrics due to the bulk flusher and the 13-hour retry, respectively.
{% endalert %}

## Frequently asked questions

### What should I do next if I receive an invalid token error?

You can disconnect and reconnect your TikTok account on the TikTok partner page. Ensure with your TikTok Business Center admin that you have the appropriate permissions to the ad account you wish to sync.

### Why is my Canvas not allowed to launch?

Confirm that your TikTok account successfully connects to Braze on the TikTok partner page. Next, make sure you've selected an ad account, entered a name for the new audience, and selected fields to match.

### How do I know if users have matched after passing users to TikTok?

TikTok does not provide this information for their data privacy policies.

### How long will it take for my audiences to populate in TikTok?

The audience size will update within 24-48 hours on the Audiences page in TikTok’s Ads Manager.

### What is the maximum number of audiences I can have in my TikTok ad account?

You can have up to 400 audiences per TikTok ad account.

### Why is my audience size or match rate in TikTok higher than the users synced in Braze with Audience Sync?

This is because in TikTok, one ID may be associated with multiple TikTok users. This occurs most often when clients use mobile ad IDs (iOS IDFA and Android GAID) because one device may have multiple TikTok users logged in. 

Additionally, TikTok also counts Pangle users as matched users, which in some cases can result in an elevated match rate. However, when you use the audience for ad delivery, the actual deliverable audience size may not be as high as the matched user size as it depends on placement and other influencing factors.

### "캔버스에 대한 오디언스가 존재하지 않습니다"라는 제목의 이메일을 받는 이유는 무엇인가요?

동기화하려는 오디언스가 스트리밍 오디언스가 아닌 경우(예: 유사 오디언스 또는 사용자 파일 오디언스인 경우) 발생할 수 있습니다. Braze 오디언스 동기화 캔버스 단계를 통해 새 오디언스를 생성해 보십시오.