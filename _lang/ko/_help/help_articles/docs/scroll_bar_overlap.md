---
nav_title: 스크롤 막대 겹침
article_title: 스크롤 막대 겹침
page_order: 0

page_type: solution
description: "이 도움말 문서에서는 Mac 사용자에게 Braze 설명서 내에서 콘텐츠가 겹치는 스크롤 막대를 해결하는 방법을 안내합니다."
---

# 스크롤 막대 겹침

Mac을 사용 중인데 다음 예시와 같이 Braze Docs 내에서 스크롤 막대가 콘텐츠와 겹치는 현상이 발생하나요?

![스크롤 막대 겹침의 예]({% image_buster /assets/img/scroll-overlap.png %})

스크롤 막대가 다음 코드 블록과 겹치는지 확인합니다:

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.S3.integration.<integration-id>/event_type=<event-type>/date=<date>/<schema-id>/<zone>/dataexport.<cluster-identifier>.S3.integration.<integration-id>+<partition>+<offset>.avro
```

스크롤 막대가 코드 블록과 겹치는 경우 **일반 설정에서** **스크롤 막대 표시:** 설정을 **항상으로** 변경하는 것이 좋습니다. 이렇게 하면 문서에서 코드 블록과 같은 기능을 확장하여 스크롤 막대를 항상 표시하고 가독성을 방지할 수 있습니다.

![MacOS 일반 설정]({% image_buster /assets/img/general-on-mac.png %})

이제 업데이트된 스크롤 막대의 모습은 다음과 같습니다:

![겹치지 않는 고정 스크롤바의 예]({% image_buster /assets/img/scroll-bar-on.png %})

_마지막 업데이트: 2019년 3월 27일_

{% comment %}
문제를 일으킬 수 있는 한 줄의 긴 코드가 있는 곳에 삽입하세요:
_스크롤 막대 때문에 코드가 보이지 않나요? 이 문제를 해결하는 방법은 [여기에서]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/) 확인하세요._
{% endcomment %}

