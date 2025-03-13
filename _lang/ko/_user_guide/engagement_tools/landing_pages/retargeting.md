---
nav\_title: 사용자 리타겟팅 기사 _ 제목: 랜딩 페이지 설명을 통해 사용자를 리타겟팅합니다: "랜딩 페이지를 통해 양식을 제출한 사용자를 리타겟팅하는 방법을 알아보세요." page\_order: 3
---

# 랜딩 페이지를 통한 사용자 리타겟팅

> 전용 세그먼트를 만들거나 양식이 제출될 때 메시지를 트리거하여 랜딩 페이지를 통해 양식을 제출한 사용자를 리타겟팅하는 방법을 알아보세요.

## 필수 조건

시작하기 전에 [랜딩 페이지를]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/) 만들어야 합니다.

## 사용자 리타겟팅

Braze는 사용자가 랜딩 페이지 양식을 제출하는 시점을 자동으로 추적합니다. [랜딩 페이지 분석에서]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#viewing-analytics) 양식의 총 제출 횟수를 확인할 수 있습니다. 그러나 사용자별 리타겟팅의 경우 다음 방법 중 하나를 사용하여 랜딩 페이지 양식을 통해 사용자를 리타겟팅해야 합니다:

- **세그먼트 사용:** 새 세그먼트를 생성하여 랜딩 페이지 양식을 제출한 사용자와 제출하지 않은 사용자를 자동으로 식별할 수 있습니다.
- **메시지 트리거 사용:** 메시지 트리거를 설정하여 사용자가 양식을 제출한 후 자동으로 메시지를 보내거나 캔버스에 입력하도록 할 수 있습니다.

{% 탭 로컬 %} {% 탭 세그먼트 사용 %} [세그먼트를 만들]({{site.baseurl}}/docs/user_guide/engagement_tools/segments/creating_a_segment/) 때 '리타겟팅' 그룹에서 **랜딩 페이지에 제출된 양식을** 선택합니다.

\![필터 그룹을 '랜딩 페이지에 제출된 양식'으로 선택한 세그먼트 생성\]({% image\_buster /assets/img/랜딩\_페이지/segmentation\_selected.png %})

여기에서 랜딩 페이지에 대한 랜딩 페이지 양식을 제출했는지 여부에 따라 사용자를 세분화할 수 있습니다. {% 끝 탭 %}

{% 탭 메시지 트리거 사용 %} [캠페인]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) 또는 [캔버스에]({{site.baseurl}}/user_guide/engagement_tools/canvas/) 대한 전달 옵션을 선택할 때 **액션 기반 전달을** 선택한 다음 **제출된 랜딩 페이지 양식을** 선택합니다.

이 랜딩 페이지 양식을 통해 양식을 제출하는 모든 사용자는 선택한 메시징 채널을 통해 메시지를 받거나 선택한 캔버스에 입력됩니다.

\![메시징의 랜딩 페이지 트리거 동작\]({% image\_buster /assets/img/landing\_pages/trigger.png %}) {% endtab %} {% endtabs %}
