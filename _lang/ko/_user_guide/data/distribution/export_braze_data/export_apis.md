---
nav_title: API 내보내기
article_title: API 내보내기
page_order: 8
page_type: reference
description: "이 참조 문서에서는 대시보드에서 직접 CSV 파일을 내보내는 것보다 프로그래밍 방식으로 대시보드 데이터의 JSON 파일을 내보내는 이유를 설명합니다."
platform: API

---

# API 내보내기

> 이 페이지에서는 프로그래밍 방식으로 대시보드 데이터의 JSON 파일을 내보낼 수 있는 Braze 내보내기 API를 다룹니다. 내보내기에 대한 지침과 샘플 코드를 포함하여 액세스할 수 있는 데이터 목록은 [엔드포인트 내]({{site.baseurl}}/api/endpoints/export/) 보내기를 참조하세요.

## CVS 다운로드 대신 내보내기 API를 사용해야 하는 경우

대시보드에서 직접 CSV를 내보내는 것보다 이 방법을 선호하는 데에는 몇 가지 이유가 있습니다:

 - 파일이 매우 큽니다. 대시보드에서 최대 500,000개의 행이 포함된 CSV를 내보낼 수 있습니다. 사용자 수가 50만 명이 넘는 세그먼트의 데이터를 내보내려면 내보낼 수 있는 양에 제한이 없는 내보내기 API를 사용해야 합니다.
 -  프로그래밍 방식으로 데이터와 상호 작용하고 싶습니다.

{% alert tip %}
CSV 및 API 내보내기에 대한 도움말은 [내보내기 문제 해결을]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/) 참조하세요.
{% endalert %}

