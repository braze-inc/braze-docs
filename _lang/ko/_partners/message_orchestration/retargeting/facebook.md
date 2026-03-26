---
nav_title: Facebook
article_title: Facebook Audience Export
alias: /partners/facebook/
description: "This reference article outlines the partnership between Braze and Facebook, a leading social platform for brands to reach and engage with their customers."
page_type: partner
search_tag: Partner

---

# Facebook Audience export

> The Braze and Facebook integration allows you to manually export your Braze segments to Facebook to create Facebook Custom Audiences. This is a one-time, static audience export and will only create new Facebook Custom Audiences.

Common use cases for exporting Facebook Custom Audiences include:
- Retargeting users at specific points within their lifecycle
- Creating exclusion targeting lists
- Creating [Lookalike Audiences](https://www.facebook.com/business/help/164749007013531?id=401668390442328) to acquire new users more efficiently
<br><br>

{% alert note %}
The Facebook audience export uses the **User Access Token** to authorize requests.<br><br>
If you are using this feature alongside the [Audience Sync to Facebook]({{site.baseurl}}/audience_sync_facebook/) feature, Braze will default to using the more reliable **System User Token** that you have already generated, to authorize requests.
{% endalert %}

{% alert note %}
If you are participating in testing Meta Work Accounts in beta, ensure you disconnect and reconnect your account to the [Facebook partner page]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync#step-1-connect-to-facebook).
{% endalert %}

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| [Facebook Business Manager](https://www.facebook.com/business/help/113163272211510?id=180505742745347) | A centralized tool to manage your brand's Facebook assets (for example, ad accounts, pages, apps). |
| [Facebook ad account](https://www.facebook.com/business/help/910137316041095?id=420299598837059) | An active Facebook ad account tied to your brand's business manager that you want to use with Braze custom audiences.<br><br>Ensure that your Facebook business manager administrator has granted you administrator permissions to the Facebook ad accounts you plan to use with Braze, and that you have accepted your ad account terms and conditions. Otherwise, you will not be able to access any Facebook ad accounts within Braze. |
| [Facebook Custom Audiences Terms](https://www.facebook.com/ads/manage/customaudiences/tos.php)| You must accept Facebook's Custom Audiences Terms for your Facebook ad accounts you plan to use with Braze.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Connect to Facebook

1. In the Braze dashboard, go to **Partner Integrations** > **Technology Partners** and select **Facebook**. 

{: start="2"}
2\. Facebook 오디언스 내보내기 모듈에서 **Facebook 연결**을 클릭합니다. <br><br>![Braze 플랫폼의 Facebook 기술 파트너 페이지.]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:70%;"}

{: start="3"}
3\. Facebook oAuth 대화 상자 창에서 Facebook 광고 계정에 커스텀 오디언스를 생성할 수 있도록 Braze에 권한을 부여합니다. <br><br>!["X로 연결"이라는 메시지가 표시되는 첫 번째 페이스북 대화상자(여기서 X는 페이스북 사용자 아이디)가 나타납니다.]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![광고 계정에 대한 광고 관리 권한을 묻는 두 번째 Facebook 대화 상자입니다.]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

{: start="4"}
4\. Braze를 Facebook 계정에 연결한 후, Braze 워크스페이스 내에서 동기화할 광고 계정을 선택합니다. <br><br>![Facebook에 연결할 수 있는 사용 가능한 광고 계정 목록입니다.]({% image_buster /assets/img/fb/afb_4.png %}){: style="max-width:70%;"}<br><br> 연결하면 파트너 페이지로 돌아가서 어떤 계정이 연결되어 있는지 확인하고 기존 계정의 연결을 해제할 수 있습니다. <br><br> ![Facebook 기술 파트너 페이지의 업데이트된 버전으로 광고 계정이 성공적으로 연결되었음을 보여줍니다.]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:70%;"}<br>
<br> Facebook 연결은 Braze 워크스페이스 수준에서 적용됩니다. If your Facebook administrator removes you from your Facebook Business Manager or access to the connected Facebook accounts, Braze will detect an invalid token. As a result, your active Canvases using Facebook audience steps will show errors, and Braze will not be able to sync users. 

{% alert important %}
For customers that have previously undergone the Facebook app review process for [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) and [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/access#standard), your system user token will still be valid for the Facebook audience step. You will not be able to edit or revoke the Facebook system user token through the Facebook partner page. Instead, you can connect your Facebook account to replace your Facebook system user token within your Braze workspace. 

<br><br>The new Facebook oAuth configuration will also apply to [Facebook exports via segments]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites).
{% endalert %}

### Step 2: Export your users into Facebook

In Braze, Facebook audience export is accessible through the **Segments** page. 

1. On the **Segments** page, select the segment you'd like to export.
2. **사용자 데이터를** 선택한 다음 **Facebook 오디언스로 내보내기를** 선택합니다. <br><br>!['사용자 데이터'가 선택된 세그먼트의 '세그먼트 세부 정보' 섹션에 'Facebook 오디언스로 내보내기'를 포함한 옵션 드롭다운이 표시됩니다.]({% image_buster /assets/img/fb/afb_6.png %})

{: start="3"}
3\. If you haven't already activated Facebook within Braze, you will be prompted to go to the Facebook Technology Partners page in the dashboard. If you already activated Facebook through **Technology Partners** > **Facebook**, you will be able to select your Facebook ad account and the user fields to export. <br><br> There are three possible user fields you can export:
- Device IDFA
- Phone number 
- Email

{% alert note %}
You can only select one user field within a single export. If you choose more than one data type, Braze will create a separate custom audience for each.
{% endalert %}

{: start="4"}
4\. After you select the user field, select **Export Segment**. Like CSV exports, you will receive an email when the segment has finished exporting into Facebook.
5\. View the custom audience on the [Facebook Ads Manager](https://www.facebook.com/ads/manager/audiences/manage/).

{% alert important %}
Due to user privacy reasons, Facebook doesn't allow you to see:

- The exact users that were successfully added to a Custom Audience. [Learn more.](https://www.facebook.com/business/help/112061095610075)
- The size of the Custom Audience. [Learn more.](https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923)
{% endalert %}

#### Configuring your audience export

When building Facebook audiences, you may wish to include or exclude certain users based on their preferences, and in order to comply with privacy laws, such as the “Do Not Sell or Share” right under the [CCPA](https://oag.ca.gov/privacy/ccpa). Marketers should implement the relevant filters for users’ eligibility within their Canvas entry criteria. Below we list some options. 

- If you have collected the [iOS IDFA through the Braze SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), you will be able to use the **Ads Tracking Enabled** filter. Select the value as `true` to only send users into Audience Sync destinations where they have opted in. 

![]({% image_buster /assets/img/tiktok/tiktok16.png %}){: style="max-width:75%;"}

- If you are collecting opt ins, opt outs, `Do Not Sell Or Share`, or other relevant custom attributes, you should include these within your Canvas entry criteria as a filter: 

![엔트리 오디언스가 "opted_in_marketing" 인 캔버스는 "true"와 같습니다.]({% image_buster /assets/img/tiktok/tiktok13.png %}){: style="max-width:75%;"}


#### Lookalike Audiences

Once you've successfully exported a segment as a Facebook Audience, you can create additional groups using Facebook [Lookalike Audiences](https://www.facebook.com/business/help/164749007013531?id=401668390442328). This feature looks at your chosen audience's demographics, interests, and other attributes and creates a new audience of people with similar attributes.

## 문제 해결

### 액세스 토큰 유효성 검사 중 오류 발생

Facebook 내보내기를 사용할 때 `Error Validating Access Token` 오류가 표시됩니다:
- 비밀번호를 변경하여 현재 세션이 무효화되었습니다.
- 보안 예방 조치로 Facebook에서 로그아웃했습니다.

이 오류를 해결하려면 다음 단계를 따르세요:
1. Facebook에서 로그아웃했다가 다시 로그인합니다.
2. Braze에서 Facebook 자격 증명을 삭제하고 저장합니다. 세그먼트 내보내기를 시도하여 자격 증명이 제거되었는지 확인합니다(내보내기 아이콘이 비활성화되어 있어야 함).
3. Facebook 자격 증명을 다시 추가하고 저장합니다.
4. 내보내기를 다시 시도하세요. 

내보내기가 작동하지 않으면 다음을 수행하세요:
1. 자격 증명을 다시 제거하고 저장합니다.
2. 자격 증명을 다시 추가하고 저장합니다.
3. **기술 파트너** 페이지에서 Facebook **파트너** 통합을 연결 해제했다가 다시 연결합니다.
