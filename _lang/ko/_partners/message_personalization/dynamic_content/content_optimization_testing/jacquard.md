---
nav_title: Jacquard
article_title: Jacquard
alias: /partners/jacquard/
page_order: 1
description: "이 참조 문서에서는 웹훅을 통해 가입자의 클릭 추적 정보를 수집하기 위해 Braze 커런츠와 연결된 콘텐츠를 사용하는 Braze와 자카드 동적 최적화의 파트너십에 대해 설명합니다. Jacquard then ties those events back to your language variants for real-time language optimization."
page_type: partner
search_tag: Partner
---

# Jacquard Dynamic Optimisation

> [Jacquard](https://www.jacquard.com/) brings together artificial intelligence, computational linguistics, and a spirit of customer-centricity to help deploy brand language, at scale, across channels that are customized to your brand voice.

Jacquard X에서 제공하는 동적 최적화는 Braze 커런츠와 연결된 콘텐츠를 사용하여 웹훅을 통해 가입자로부터 클릭 추적 정보를 수집합니다. Jacquard then ties those events back to your language variants for real-time language optimization. 

## Prerequisites

| Requirement | Description |
|---|---|
| Jacquard account | A [Jacquard account](https://www.jacquard.com/) is required to take advantage of this partnership. |
| Jacquard connect server token | A long string of characters that will serve as your Braze campaign's password to access your Jacquard language.<br><br>You can request this from your Jacquard customer success manager if you haven't already been provided it. |
| Currents | In order to export data to Currents, you need to have [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) set up for your account. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Request Jacquard Amazon S3 credentials

You'll need Jacquard to set up a dedicated Amazon S3 bucket to receive your click tracking events from Braze. 이 프로세스를 시작하려면 Jacquard 고객 성공 매니저에게 문의하세요. When the bucket is created, you will be provided unique credentials to create your Current. 

### Step 2: Create Current

1. In Braze, select **Currents > Create New Current > Amazon S3 Data Export**. 
2. Next, name your Current and enter a contact email.
3. Add your Jacquard AWS access key ID and secret access key in the credentials box. Then, add "phrasee-braze-currents-exports" as the AWS S3 bucket name. 
4. Lastly, add the AWS S3 bucket folder you received from your Jacquard customer success manager. It will likely be your company's name.
5. Under **General Settings**, check the "Include events from anonymous users" box, and under **Manage Engagement Events** check "Email Click".
6. When you are finished, select **Launch Current**.

### Step 3: Request to remove personally identifiable information (PII).

다음으로, Braze 계정 팀에 연락하여 개인 식별자 정보가 Jacquard에 전송되지 않도록 하세요.

By default, the Current will include certain PII attributes like email and address. Jacquard cannot and will not receive PII, so it's critical you make a request to your Braze account team to turn this off for any event data passed along to Jacquard.

### Step 4: Jacquard X code snippets 

필요한 코드 스니펫은 Jacquard 계정 팀에 문의하세요.

이러한 스니펫은 [연결된 콘텐츠를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) 사용하며, 이메일에 배치된 후에는 언어와 추적 픽셀을 동적으로 가져와서 Jacquard X를 사용하여 실시간으로 언어를 최적화할 수 있습니다.


