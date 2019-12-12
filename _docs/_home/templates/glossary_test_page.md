---
page_order: 2

nav_title: Glossary
layout: glossary_page
glossary_top_header: "Glossary Template"
glossary_top_text: "This is a test Glossary Page."

//Required
description: "This is the Google Search description. Characters past 160 get truncated, keep it brief." 
page_type: glossary
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
//Use if applicable
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

noindex = true 
//ATTENTION: remove noindex and this alert from template

glossary_tag_name: Tags
glossary_filter_text: "Select tags below to narrow the glossary:"

# channel to icon/fa or image mapping
glossary_tags:
  - name: Tag 1
  - name: Tag 2
  - name: Tag 3

glossaries:
  - name: Term 1
    image: /docs/assets/img_archive/weeklyreport.png
    description: Definition of Term 1.
    calculation: Calculation / Of Term 1
    tags:
      - All
  - name: Term 2
    description: Definition of Term 2.
    calculation: (Number of Terms) / (Unique Terms)
    tags:
      - Tag 1
  - name: Term 3
    description: Definition of Term 3.
    calculation: Count
    tags:
      - Tag 2
  - name: Term 4
    description: Definition of Term 4.
    calculation: Count
    tags:
      - Tag 1
      - Tag 3
---
