---
nav_title: Set up KakaoTalk
article_title: "Set up KakaoTalk"
description: "This reference article outlines how to set up your KakaoTalk channel, including how to set up users, reconcile user IDs, and create test users."
page_order: 0
page_type: partner
search_tag: Partner
alias: /kakaotalk_setup/
---

# Set up KakaoTalk

> This article covers how to set up the [KakaoTalk messaging channel]({{site.baseurl}}/kakaotalk/) in Braze, including how to set up users, reconcile user IDs, and create KakaoTalk test users.

## Prerequisites

| Requirement | Description |
| --- | --- |
| Account with a supported KakaoTalk partner | An account with a supported KakaoTalk partner, [CJ OliveNetworks](https://www.braze.com/partners/solutions-partners/cjolivenetworks/) or Infobip, is required to use the KakaoTalk messaging channel. |
| KakaoTalk Business channel | Your KakaoTalk account must be a KakaoTalk Business channel to send KakaoTalk messages through Braze. When you create an account, its default status is basic. To make your account a Business channel, you'll need to verify your business and provide relevant documentation. |
| KakaoTalk Sender Key | A valid KakaoTalk Sender Key. |
| Contact phone number | A contact phone number for your KakaoTalk channel’s administrator. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Types of KakaoTalk accounts

| Account type | Description |
| --- | --- |
| Basic channel | A standard KakaoTalk channel that any organization can set up. It enables broadcast messaging and 1:1 chat through KakaoTalk. |
| [Business channel](https://www.kakaocorp.com/page/service/service/KakaoTalkChannel) | An upgraded, business-verified KakaoTalk channel that requires an application and verification process. It offers enhanced features, such as {::nomarkdown}<ul><li>Verified badge</li><li>Appearance as a recommended channel</li><li>Support for business messaging</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Apply for a business channel 

Before starting the application, gather the following business documentation:
- Korean Business Registration Certificate
- ID of the Business Representative
- Employment Certificate
- Industry-specific Licenses

{% alert important %}
The information on your KakaoTalk Channel (such as channel name, profile image, and others) must exactly match the information on your official submitted documents.
{% endalert %}

After gathering your documentation, follow these steps:

1. Log into the [KakaoTalk Channel Admin Center](https://center-pf.kakao.com/).
2. Select the existing KakaoTalk channel you wish to upgrade.
3. In the **Management (관리)** section, select the option for **Business Channel Application (비즈니스 채널 신청)**.
4. Select the **Apply** or **Request button (신청)** to begin the process.
5. Provide the required information.
6. Wait for a notification with the review results.

## Integrate KakaoTalk

### Step 1: Connect the KakaoTalk channel to Braze

1. Go to **Partner Integrations** > **Technology Partners** and select your KakaoTalk provider.
2. Gather the required credentials for your provider (see below), then enter them into the **Technology Partners** page and save.
3. Use the newly saved credentials for sending.

{% tabs local %}
{% tab CJ OliveNetworks %}

Go to your [Comm.One dashboard](https://ums.cjmplace.com/) and gather the following information.

| Field | Location |
| --- | --- |
| **Comm.One Login ID (로그인 아이디)** | Select your profile. |
| **Sender Key (발신프로필 키)** | Go to **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**. |
| **Channel name (카카오톡 채널 프로필명)** | In your Comm.One dashboard, go to **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**. |
| **Sender number (연락처)** | {::nomarkdown}<ol><li>Go to <b>Account Management (계정 관리)</b>, select the menu icon, then select <b>View Details (자세히보기)</b>.</li><li>Go to <b>Business Detailed Information (업체 상세 정보)</b> > <b>Company Information (기업정보)</b></li></ul>{:/} |
| **Credential (ID) & Password (비밀번호)** | Go to the same location for the **Sender number (사업자 등록번호)**, then go to **API** > **Brand Message (브랜드 메시지)**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% subtabs local %}
{% subtab Comm.One Login ID (로그인 아이디) %}

![Comm.One dashboard showing a censored login ID.]({% image_buster /assets/img/kakaotalk/comm.one_login_id.png %})

{% endsubtab %}
{% subtab Sender Key (발신프로필 키) %}

![Comm.One dashboard showing a censored Sender Key.]({% image_buster /assets/img/kakaotalk/sender_key.png %})

{% endsubtab %}
{% subtab Channel name (카카오톡 채널 프로필명) %}

![Comm.One dashboard showing a censored channel name.]({% image_buster /assets/img/kakaotalk/channel_profile_name.png %})

{% endsubtab %}
{% subtab Credential (ID) & Password (비밀번호) %}

![Comm.One dashboard showing a censored credential ID and password.]({% image_buster /assets/img/kakaotalk/id_and_password.png %})

{% endsubtab %}
{% endsubtabs %}

![Fields on the Technology Partners page for CJ OliveNetworks.]({% image_buster /assets/img/kakaotalk/cj_olivenetworks.png %}){: style="max-width:30%;"}

![Credentials for a Braze KakaoTalk channel.]({% image_buster /assets/img/kakaotalk/cj_credentials.png %})

{% alert note %}
Only the channels mapped to a single common ID can be registered.
{% endalert %}

{% endtab %}
{% tab Infobip %}

Go to your Infobip dashboard and gather the following information.

| Field | Location |
| --- | --- |
| **API Base URL** | Select **Developer Tools** > **API Keys**. |
| **API Key** | Select **Developer Tools** > **API Keys**. |
| **Sender name / Sender key** | Select **Channels and Numbers** > **Channels**, then select the **Senders** tab. |
| **Sender profile UUID** | Provided directly by Infobip. Contact Infobip if you don't have this information. |
| **Channel name** | Provided directly by Infobip. Contact Infobip if you don't have this information. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% subtabs local %}
{% subtab API Base URL and API Key %}

<!-- Screenshot needed: Infobip Developer Tools > API Keys page showing API Base URL and API Key fields -->
![Infobip Developer Tools API Keys page.]({% image_buster /assets/img/kakaotalk/infobip_api_key.png %})

{% endsubtab %}
{% subtab Sender name / Sender key %}

<!-- Screenshot needed: Infobip Channels and Numbers > Channels > Senders tab -->
![Infobip Channels and Numbers Senders tab.]({% image_buster /assets/img/kakaotalk/infobip_sender_key.png %})

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

## Set user profiles

User profiles must have phone numbers to message them through KakaoTalk. Phone numbers are shown on the user profile and in the format that they are provided. Currently, unlike SMS or WhatsApp, KakaoTalk uses the standard phone field (and not a number that has been changed into the E.164 format).

![User profile for a test user with a phone number in an unedited format.]({% image_buster /assets/img/kakaotalk/standard_phone_number.png %}){: style="max-width:50%;"}

### Import phone numbers

Import phone numbers by [uploading a CSV or using the API]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/) to create a user.