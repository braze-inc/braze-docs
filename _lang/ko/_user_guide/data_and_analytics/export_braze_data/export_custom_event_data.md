---
nav_title: 내보내기 커스텀 이벤트 집계
article_title: 내보내기 커스텀 이벤트 집계
page_order: 6
page_type: reference
description: "이 참조 문서는 커스텀 이벤트 데이터 집계를 내보내는 방법을 다룹니다."
tool: Reports

---

# 커스텀 이벤트 집계 내보내기

> 대시보드의 **커스텀 이벤트** 보고서 페이지를 통해 시간 경과에 따른 하나 이상의 커스텀 이벤트 발생을 확인할 수 있습니다. 사용자 정의 이벤트 또는 시간별 사용자 정의 이벤트에 대한 자세한 통계를 보면 특정 세그먼트별로 데이터를 볼 수 있는 옵션도 있습니다.

**커스텀 이벤트 보고서**는 **분석**에서 찾을 수 있습니다.

{% alert note %}
[이전 탐색<2>을 사용하는 경우 **커스텀 이벤트** 보고서 페이지를 **데이터<4> 아래에서 찾을 수 있습니다.
{% endalert %}

![커스텀 이벤트][14]

다음 CSV를 내보낼 수 있습니다:

- 날짜별 커스텀 이벤트
    - (Optional) 커스텀 이벤트 for Different Segments
- 시간대별 사용자 지정 이벤트
    - (Optional) 커스텀 이벤트 for Different Segments
- MAU당 사용자 지정 이벤트
- 다른 세그먼트를 위한 커스텀 이벤트
- KPI 공식당 커스텀 이벤트
    - (Optional) 커스텀 이벤트 for Different Segments

{% alert tip %}
CSV 및 API 내보내기에 대한 도움말은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/) 문서를 참조하세요.
{% endalert %}

[14]: {% image_buster /assets/img_archive/Export_events.png %}
