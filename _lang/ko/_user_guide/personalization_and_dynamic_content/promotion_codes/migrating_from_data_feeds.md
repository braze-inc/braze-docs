---
nav_title: 데이터 피드에서 프로모션 코드로 마이그레이션하기
article_title: 데이터 피드에서 프로모션 코드로 마이그레이션하기
page_order: 0
description: "이 참조 문서에서는 Data Feeds에서 프로모션 코드로 마이그레이션하는 방법에 대한 지침을 제공합니다."
---

# 데이터 피드에서 프로모션 코드로 마이그레이션하기

{% alert note %}
데이터 피드는 더 이상 사용되지 않습니다. Braze는 데이터 피드를 사용하는 고객에게 프로모션 코드 목록으로 이동할 것을 권장합니다.
{% endalert %}

> This page guides you through migrating from Data Feeds to promotion codes. This is a straightforward process that involves manually creating promotion code lists with the information from your Data Feeds and updating your message references accordingly.

## 특징 및 기능

프로모션 코드 목록과 데이터 피드에는 몇 가지 차이점이 있습니다.

| 기능          | 프로모션 코드 | Data Feeds   |
|------------------|-----------------|--------------|
| 설명     | 예             | 아니요           |
| 만료 날짜 | 예             | 아니요           |
| 생성 방법  | CSV 업로드하기 | 텍스트 붙여넣기 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 마이그레이션하는 방법

데이터 피드를 프로모션 코드 목록으로 바꾸려면 다음과 같이 하세요: 

1. **데이터 설정**으로 이동하여 **프로모션 코드 목록 생성**을 선택합니다.
2. [프로모션 코드 목록을 설정합니다]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes).
3. 이전에 데이터 피드를 참조했던 메시지로 이동하여 프로모션 코드 목록을 사용하도록 업데이트합니다.