---
nav_title: Data Points
page_order: 4
---

# Data Points

Data points are Braze's way was of defining a pricing structure, based on pieces of information logged against user profiles. See [Consumption Count](#consumption-count) below to see what data counts toward your data point allocation.


## Consumption Count


{% tabs %}
{% tab General %}

### General

|Data Type | Data Point | Does it count towards consumption? |
|---|---|---|
|Profile Data | First Name | Yes |
|Profile Data | Last Name | Yes |
|Profile Data | User ID | Yes |
|Profile Data | Email Address | Yes |
|Profile Data | Gender | Yes |
|Profile Data | Age Group | Yes |
|Profile Data | Country | Yes |
|Profile Data | City | Yes |
|Profile Data | Language | Yes |
|Profile Data | Most Recent Device Locale | Yes |
|Profile Data | Time Zone | Yes |
|Profile Data | Date of Birth (DOB) | Yes |
|Profile Data | Bio | Yes |
|Profile Data | Phone Number  | Yes |
|Profile Data | Avatar Image URL | Yes |
|App Usage Data |Session Start | Yes |
|App Usage Data |Session End | Yes |
|Custom Attributes | All Custom Attributes | Yes |
|Recent Devices | Number of Devices | No |
|Recent Devices | Most Recent Watch | No |
|Recent Devices | App Version | No |
|Recent Devices | Device | No |
|Recent Devices | Device OS | No |
|Custom Events | All Custom Events | Yes |
|Purchases | All Purchases | Yes |
|Amplitude Cohort Assignment | All Assignments | No |
|Mixpanel Cohort Assignment | All Assignments | No |

  {% endtab %}
{% tab Location %}

### Location

|Data Type | Data Point | Does it count towards consumption? |
|---|---|---|
|Most Recent Location | All Most Recent Locations | Yes |

  {% endtab %}
{% tab Engagement %}

### Engagement

|Data Type | Data Point | Does it count towards consumption? |
|---|---|---|
|Contact Settings | First Name | No |
|Contact Settings | Last Name | No |
|Contact Settings | User ID | No |
|Campaigns Received | Email Address | No |
|Segments | Gender | No |
|Communication Stats | Age Group | No |
|Communication Stats | Country | No |
|Communication Stats | City | No |
|Communication Stats | Language | No |
|Communication Stats | Most Recent Device Locale | No |
|Communication Stats | Most Recent Device Locale | No |
|News Feed Cards Clicked | News Feed Cards Clicked | No |
|Install Attribution | Install Source | No |
|Install Attribution | Campaign | No |
|Install Attribution | Ad Group | No |
|Install Attribution | Ad | No |
|Miscellaneous | Random Bucket Number | No |
|Canvas Messages Received | Canvas Messages Received | No |

 {% endtab %}
{% tab Social %}

### Social

|Data Type | Data Point | Does it count towards consumption? |
|---|---|---|
|Twitter | Username | Yes |
|Twitter | Followers | No |
|Twitter | Following | No |
|Twitter | Number of Tweets | No |
|Facebook | Likes | No |

 {% endtab %}
{% endtabs %}


## Data Point Management & Usage

You can view your Data Points Usage on the __Subscriptions and Usage__ section in any of the tabs. Just go to your name in the top-right corner, click the drop down, and select __Subscriptions and Usage__.

{% alert tip %}
To prevent using up your allocated data points, we recommend setting up a program that will to prevent sending the same, unchanging data from your app to Braze over and over.

__Only update your deltas (changing data)!__
{% endalert %}
