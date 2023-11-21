---
nav_title: Managing pages
page_order: 1
noindex: true
---

# Managing pages

> TODO

New pages will be created within the `/_docs` folder in 1 of the main folders:
* `_developer_guide`: Developer Guide Documentation, REST API Documentation, Integration Guides.
* `_user_guide`: User Guide Documentation, Product Uses & Walkthroughs.
* `_partner`: Technology Partner Integration and Information Guides.
* `_help`: Help Articles, Troubleshooting, Best Practices, & More.

**_All file names and folders should all be lower case. Underscores (\_) should be used instead of spaces or special characters._**

## Adding a new page

While uncommon, if you would like to add a new page through the on-GitHub contribution method, listed below are the instructions and required YAML to do so.

If you would like to add a new page, navigate to the folder where you want your new file to sit. Select the Create new file button.

Name your file.

Then, add your `yaml` config to the top of the file. At least add the following:

```
---
nav_title: Title That Will Appear in the Navigation Bar
article_title: The title that will appear in the Braze search bar. This title is also what Algolia, our search engine provider, queries first. This is often just the same as the title of the article.
page_order: 0
description: "This is the Google Search description. Characters past 160 get truncated. Keep it brief." 
page_type: See List of Valid Page Types
tool:
  - dashboard
  - docs
  - canvas
  - campaigns
  - segments
  - templates
  - media
  - location 
  - currents
  - reports
platform: 
  - iOS
  - Android
  - Web
  - API
channel: 
  - content cards
  - email
  - news feed
  - in-app messages
  - push
  - sms
  - webhooks
---
```

Write your content as described above, then submit your changes.
