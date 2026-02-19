---
nav_title: MyPostcard
article_title: MyPostcard
page_order: 1
description: "This reference article outlines the partnership between Braze and MyPostcard, which allows you to use direct mail as an additional channel for your CRM workflow."
alias: /partners/mypostcard/
page_type: partner
search_tag: Partner

---

# MyPostcard

> [MyPostcard](https://www.mypostcard.com), a leading global postcard app, empowers you to execute direct mail campaigns with ease, providing a seamless and profitable way to connect with your customers. 

Use the MyPostcard and Braze integration to effortlessly send your customers print mailings.

## Prerequisites

| Requirement                      | Description                                                                                                             |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| MyPostcard B2B account           | Registering with MyPostcard is required to take advantage of this integration.                                          |
| B2B API key and credentials        | You can find your API Key and the credentials in the MyPostcard B2B Admin Tool.                                         |
| Approved MyPostcard B2B campaign | To take advantage of this integration, you need to set up a print mailing campaign in the MyPostcard B2B tool. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases

To elevate your direct mail campaigns, it’s crucial to move beyond traditional mass mailings and integrate print mailing seamlessly into your workflows. This approach allows you to reach specific customers who have opted out of your email newsletters or whose emails are marked as spam. With MyPostcard, you can effortlessly send print mailing campaigns directly through Braze.

- Build intuitive workflows in Braze, incorporating print mail as a powerful new channel, without any technical expertise.
- Unlock the potential of personalized print mailings with a few simple steps.
- Benefit from a straightforward implementation that is backed by personalized support from a dedicated team.

## Integration

To integrate with MyPostcard, [log in or sign up](https://www.mypostcard.com/b2b/admin/) and create your first campaign to use it through [Braze webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks).

### Step 1: Create your Braze webhook template

Create a MyPostcard webhook template to use in future campaigns or Canvases by navigating to **Templates** > **Webhook Templates** in the Braze platform.

{% alert note %}
[구형 탐색]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/)로 이동하는 경우, **참여** > **템플릿 & 미디어** > **웹훅 템플릿**로 가십시오.
{% endalert %}

If you would like to create a one-off MyPostcard webhook campaign or use an existing template, select **Webhook** in Braze when creating a new campaign. Fill out the following fields:

| Field         | Description                                               |
|---------------|-----------------------------------------------------------|
| **Webhook URL** | The webhook URL as shown in the B2B Admin Tool.             |
| **Request Body** | Raw Text (JSON format found in the B2B Admin Tool).        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Request method and headers

MyPostcard requires an HTTP method along with the following HTTP headers to be included in the template.

{% raw %}
<table>
  <thead>
    <tr>
      <th><strong>Field</strong></th>
      <th><strong>Details</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>HTTP Method</strong></td>
      <td><code>POST</code></td>
    </tr>
    <tr>
      <td><strong>Username</strong></td>
      <td><code>{{ '&lt;username&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>Password</strong></td>
      <td><code>{{ '&lt;password&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>Content-Type</strong></td>
      <td><code>application/json</code></td>
    </tr>
  </tbody>
</table>
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Request body

B2B 관리 도구에 표시되는 요청 본문을 복사한 다음 Liquid 개인화 태그를 사용하여 플레이스홀더를 콘텐츠로 채웁니다.

![작성 탭에는 JSON 본문과 웹훅 정보가 표시됩니다.]({% image_buster /assets/img/mypostcard/mypostcard_compose.jpg %})

### 2단계: Preview your request

Next, preview your request in the **Preview** panel or go to the **Test** tab, where you can choose a random user, an existing user, or create a custom user to test your webhook. 페이지에서 나가기 전에 템플릿을 저장하는 것을 잊지 마세요!

![다양한 필드를 사용하여 웹훅 탭을 테스트하여 구현을 검증합니다.]({% image_buster /assets/img/mypostcard/mypostcard_test.jpg %})

{% alert important %}
Remember to save your template before leaving the page! <br>Updated webhook templates can be found in the **Saved Webhook Templates** list when creating a new [webhook campaign]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}

