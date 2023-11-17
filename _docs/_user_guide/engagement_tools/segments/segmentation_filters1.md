---
nav_title: "Segmentation Filters tabs"
article_title: Segmentation filters tabs
page_order: 0
description: 
page_type: reference
---

# Filter categories

The Braze SDK provides you with a powerful arsenal of filters to segment and target your users based off of specific features and attributes. As you can see, you can search or narrow these filters by filter category.

{% tabs %}
{% tab Segment or CSV membership %}
## Segment or CSV membership

User membership in other segments, Segment Extension, or imported CSV.

| Filter name | Description 
|---|---
| Segment membership | 
| Braze Segment Extensions |
| Updated/imported from CSV | 
{: .reset-td-br-1 .reset-td-br-2 }

 {% endtab %}
 {% tab Custom attributes  %}

## Custom attributes

User characteristics that your company has set up.

| Filter name | Description 
|---|---
| Custom attributes |
| Nested custom attributes |
| Day of recurring event |
{: .reset-td-br-1 .reset-td-br-2 }

{% endtab %}
{% tab Custom events %}

## Custom events

User actions that your company has set up.

| Filter name | Description 
|---|---
| Custom events |
| First did custom event |
| Last did custom event |
| X custom event in Y days |
| X custom event property in Y days |
{: .reset-td-br-1 .reset-td-br-2 }

{% endtab %}
{% tab Sessions %}

## Sessions

Session count, first and last session, and median session duration.

### Session count

| Filter name | Description 
|---|---
| Session count overall | 
| Session count for app |
| X sessions in last Y days |
{: .reset-td-br-1 .reset-td-br-2 }

### First session

| Filter name | Description 
|---|---
| First used app |
| First used specific app |

### Last session

| Filter name | Description 
|---|---
| Last used app | 
| Last used specific app |
{: .reset-td-br-1 .reset-td-br-2 }

### Median session

| Filter name | Description 
|---|---
| Median session duration |
{: .reset-td-br-1 .reset-td-br-2 }

{% endtab %}
{% tab Retargeting %}

## Retargeting

Past interactions with messages and channels.

### Received campaign/Canvas

| Filter name | Description 
|---|---
| Received message from campaign | 
| Received campaign variant |
| Received message from Canvas step |
| Last received message from specific campaign | 
| Last received message from specific Canvas step | 
| Received message from campaign or Canvas with tag | 
| Last received message from campaign or Canvas with tag | 
| Has never received a message from campaign or Canvas step |
{: .reset-td-br-1 .reset-td-br-2 }

### Last channel receipt/engagement

| Filter name | Description 
|---|---
| Last received email |
| Last received push | 
| Last in-app message impression | 
| Last received SMS/MMS | 
| Last received webhook | 
| Last received Whatsapp | 
| Last viewed News Feed |
| Last received any message |
| Last engaged with message |
{: .reset-td-br-1 .reset-td-br-2 }

### Clicked/opened campaign or Canvas

| Filter name | Description 
|---|---
| Clicked/Opened Campaign |
| Clicked/Opened Campaign or Canvas With Tag | 
| Clicked/Opened Step |
{: .reset-td-br-1 .reset-td-br-2 }

### Email

| Filter name | Description 
|---|---
| Clicked Alias in campaign | 
| Clicked Alias in Canvas step |
| Clicked Alias in any campaign or Canvas Step |
| Hard bounced |
| Has marked you as spam |
{: .reset-td-br-1 .reset-td-br-2 }

### SMS

| Filter name | Description 
|---|---
| Invalid phone number | 
| Last sent specific SMS Inbound Keyword category |
{: .reset-td-br-1 .reset-td-br-2 }

### Converted

| Filter name | Description 
|---|---
| Converted from Campaign | 
| Converted from Canvas | 
{: .reset-td-br-1 .reset-td-br-2 }

### Control group membership

| Filter name | Description 
|---|---
| In campaign control group |
| In Canvas control group | 
| Last enrolled in control group |
{: .reset-td-br-1 .reset-td-br-2 }

### Other

| Filter name | Description 
|---|---
| Entered Canvas Variation |
| Clicked card |
| Feature flags |
{: .reset-td-br-1 .reset-td-br-2 }

{% endtab %}
{% tab Channel subscription behavior %}

## Channel subscription behavior

User subscription behavior for specific messaging channels.

| Filter name | Description 
|---|---
| Subscription group | 
{: .reset-td-br-1 .reset-td-br-2 }

### Email

| Filter name | Description 
|---|---
| Email available |
| Email opt in date |
| Email subscription status |
| Email unsubscribed date |
{: .reset-td-br-1 .reset-td-br-2 }

### Push

| Filter name | Description 
|---|---
| Push enabled |
| Push enabled for app |
| Background push enabled |
| Push opt in date |
| Push subscription status |
| Push unsubscribed date |
{: .reset-td-br-1 .reset-td-br-2 }

{% endtab %}
{% tab Purchase behavior %}

## Purchase behavior

User actions for purchasing, purchasing specific products, and spending money.

### Number of purchases

| Filter name | Description 
|---|---
| Purchased product |
| Total number of purchases |
| X product purchased in Y days |
| X purchase property in Y days |
| X purchases in Y days |
{: .reset-td-br-1 .reset-td-br-2 }

### First purchase

| Filter name | Description 
|---|---
| First made purchase |
| First purchase for app |
| First purchased product |
{: .reset-td-br-1 .reset-td-br-2 }

### Last purchase

| Filter name | Description 
|---|---
| Last purchase for app |
| Last purchased product |
| Last purchased product |
{: .reset-td-br-1 .reset-td-br-2 }

### Spend

| Filter name | Description 
|---|---
| Money spent |
| X money spent in Y days |
{: .reset-td-br-1 .reset-td-br-2 }

{% endtab %}
{% tab Demographic attributes %}

## Demographic attributes

User demographic information including country, city, language, birthday, and more.

| Filter name | Description 
|---|---
| Country |
| City |
| Language |
| Age |
| Birthday |
| Gender |
| Phone number |
| First name |
| Last name |
{: .reset-td-br-1 .reset-td-br-2 }

{% endtab %}
{% tab App %}

## App

Usage behavior for specific apps and app versions.

| Filter name | Description 
|---|---
| Has app |
| Most recent app version name |
| Most recent app version number |
{: .reset-td-br-1 .reset-td-br-2 }

{% endtab %}
{% tab Uninstall %}

## Uninstall

App uninstall behavior and date.

| Filter name | Description 
|---|---
| Uninstalled |
| Uninstall date |
{: .reset-td-br-1 .reset-td-br-2 }

{% endtab %}
{% tab Devices %}

## Devices

User device information, including model, OS, ad tracking, and more.

| Filter name | Description 
|---|---
| Device carrier |
| Device count |
| Device model |
| Device OS |
| Most recent device locale |
| Most recent watch model |
| Provisionally authorized on iOS |
| Web browser (not sure about this one) |
{: .reset-td-br-1 .reset-td-br-2 }

### Advertising use cases

| Filter name | Description 
|---|---
| Ad tracking |
| Device IDFA |
| Device IDFV |
| Device Google Ad ID |
| Device Roku Ad ID |
| Device Windows Ad ID |
{: .reset-td-br-1 .reset-td-br-2 }

{% endtab %}
{% tab Location %}

## Location

User location data.

| Filter name | Description 
|---|---
| Most recent location |
| Location available |
{: .reset-td-br-1 .reset-td-br-2 }

{% endtab %}
{% tab Cohort membership %}

## Cohort membership

User membership in cohorts from Alloys integrations.

| Filter name | Description 
|---|---
| Amplitude cohorts |
| Census cohorts |
| Heap cohorts |
| Hightouch Cohorts |
| Kubit Cohorts |
| Mixpanel cohorts |
| Segment cohorts |
| Tinyclues cohorts |
{: .reset-td-br-1 .reset-td-br-2 }

{% endtab %}
{% tab Install attribution %}

## Install attribution

User install behavior attributed to specific ad sources. 

| Filter name | Description 
|---|---
| 
{: .reset-td-br-1 .reset-td-br-2 }

{% endtab %}
{% tab Intelligence and predictive %}

## Intelligence and predictive

Data that leverages AI features for predicted events, or for intelligent channel selection.

### Churn risk

| Filter name | Description 
|---|---
| Churn risk category |
| Churn risk score |
{: .reset-td-br-1 .reset-td-br-2 }

### Purchase likelihood

| Filter name | Description 
|---|---
| Purchase likelihood category |
| Purchase likelihood score |
{: .reset-td-br-1 .reset-td-br-2 }

### Other

| Filter name | Description 
|---|---
| Intelligent channel |
{: .reset-td-br-1 .reset-td-br-2 }

{% endtab %}
{% tab Social activity %}

## Social activity

Connection to Facebook and Twitter.

| Filter name | Description 
|---|---
| Number of Facebook Friends using app |
| Connected Facebook |
| Connected Twitter |
| Number of Twitter followers |
{: .reset-td-br-1 .reset-td-br-2 }

{% endtab %}
{% endtabs %}