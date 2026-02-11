---
nav_title: Unique Discount Codes 
article_title: 고유 할인 코드 보내기
alias: /shopify_discount_codes/
page_order: 7
description: "This reference article covers a community-submitted use case of using Braze promotion codes with the Shopify Bulk Discount Code Bot to send unique discount codes through your campaigns and Canvases."
---

# Shopify를 통해 고유 할인 코드 보내기

> This community-submitted use case shows how to use Braze [promotion codes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/) with the Shopify Bulk Discount Code Bot to generate unique discount codes for your campaigns and Canvases. Unique discount codes help avoid the exploitation of generic promotion codes.

{% alert important %}
This is a community-submitted integration and isn’t directly supported by Braze. The Bulk Discount Code Bot is directly supported by Shopify. Only Braze promotion codes are supported by Braze.
{% endalert %}

## 요구 사항

| Requirement | Description |
| --- | --- |
| Set up a Shopify store | Confirm you've already [set up a Shopify store with Braze]({{site.baseurl}}/shopify_overview/). |
| Install the Bulk Discount Code Bot app | Download the [Bulk Discount Code Bot](https://apps.shopify.com/bulk-discount-generator) app in the Shopify app store. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Generating unique discount codes

### Step 1: Configure your discount codes

Use the Bulk Discount Code Bot to configure your discount codes based on the number of codes to generate, code length, discount value, and more.

![할인 세트의 구성 옵션][1]

### 2단계: Export your codes

Find your discount set in the Bulk Discount Code Bot's search bar, then select **Export Codes** > **Download Codes** to download a CSV file to your Downloads folder.

![할인 세트가 표시된 드롭다운과 선택할 수 있는 버튼 행이 있는 검색창.{: style="max-width:70%;"}

In the CSV file, delete row 1 to remove the column header “Promo”. This will prevent "Promo" from becoming a discount code in Braze.

![CSV 파일에서 행 헤더 "Promo" 제거를 보여주는 순서도.][3]{: style="max-width:60%;"}

### 3단계: Add your discount codes to Braze

In Braze, go to **Data Settings** > **Promotion Codes** > **Create Promotion Code List** and [configure your discount codes list]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/#creating-a-promotion-code-list). Make sure you match the expiration date that was configured by the Bulk Discounts Code Bot.

Then, upload your CSV file and select **Save List**.

### Step 4: Add your discount codes to a Braze campaign or Canvas step

If you want to use your unique discount codes in a single-send campaign, or you don't mind users receiving multiple unique codes across different campaigns or Canvas steps, copy the code's Liquid snippet from the promotion codes list you saved.

![버튼이 있는 Liquid 코드 스니펫은 이를 복사합니다.][4]{: style="max-width:60%;"}

Paste the Liquid snippet into a campaign or Canvas step. 

![Liquid 스니펫이 캔버스 단계에 추가되는 것을 보여주는 GIF][5].

캠페인이나 캔버스에서 할인 코드가 몇 번이나 참조되더라도 사용자에게 하나의 고유 할인 코드를 받도록 하려면 첫 번째 메시지 단계 바로 앞에 '프로모션 코드'와 같은 커스텀 속성에 할인 코드를 할당하는 [사용자 업데이트]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) 단계를 만드세요.

{% alert tip %}
You can also [create a custom attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) by going to **Data Settings** > **Custom Attributes**.
{% endalert %}

In the User Update step, do the following for each field:
- **Attribute Name:** Select **Promo Code**.
- **Action:** Select **Update**.
- **Key Value:** Paste the Liquid code snippet.

![Liquid 스니펫으로 "프로모션 코드" 속성을 업데이트하는 사용자 업데이트 단계입니다.][6].

Now, you can add the custom attribute {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %} to any message, and the discount code will be templated in.

## Discount code behavior

{% details Multichannel campaign or Canvas step %}

When a discount code snippet is used in a multichannel campaign or Canvas step, users always receive a unique code. If a user is eligible to receive a code through more than one channel, they'll receive the same code through each channel. In other words, an eligible user would only receive one code across all the messages sent by that campaign or Canvas step.

{% enddetails %}

{% details Different Canvas steps or separate campaigns %}

When a discount code is referenced by multiple steps in the same Canvas or by separate campaigns, an eligible user will receive multiple unique promotion codes (one code for each Canvas step or campaign).

{% enddetails %}

[1]: {% image_buster /assets/img/Shopify/configure_discount_codes.png %}
[2]: {% image_buster /assets/img/Shopify/export_discount_codes.png %}
[3]: {% image_buster /assets/img/Shopify/edited_codes_csv.png %}
[4]: {% image_buster /assets/img/Shopify/liquid_code_snippet.png %}
[5]: {% image_buster /assets/img/Shopify/liquid_promo_code.gif %}
[6]: {% image_buster /assets/img/Shopify/user_update_step.png %}