---
nav_title: 사용량 분석 내보내기
article_title: 사용량 분석 내보내기
page_order: 3

page_type: reference
description: "이 참조 문서에서는 높은 수준의 앱 사용 데이터를 내보내는 방법에 대해 설명합니다."
tool: 
  - Reports

---

# 사용량 분석 내보내기

> 이 페이지에서는 대시보드의 **홈** 페이지에 앱 사용에 대한 개략적인 데이터와 날짜별 다양한 KPI에 대한 자세한 통계가 포함되어 있습니다.

이 페이지에서 데이터의 CSV를 내보내려면 다음과 같이 하세요:

1. 데이터를 볼 기간과 앱을 설정합니다. 기본적으로 대시보드에는 모든 앱의 최근 30일간의 데이터가 표시됩니다.

![Time period and app fields on the Home dashboard.]({% image_buster /assets/img_archive/home_dashboard_select_date.png %}){: style="max-width:60%;"}

{:start="2"}
2\. **시간 경과에 따른 성능** 그래프까지 아래로 스크롤합니다.
3\. **통계** 대상 필드에서 내보내려는 데이터를 선택합니다. 내보낼 수 있는 [데이터를](#available-data) 확인하세요.

![Performance Over Time graph on the Home dashboard.]({% image_buster /assets/img_archive/home_dashboard_export.png %})

{:start="4"}
4\. 선택 <i class="fas fa-bars" title="차트 컨텍스트 메뉴"></i> 을 선택한 다음 내보내기 옵션을 선택합니다.

## 사용 가능한 데이터

다음 데이터가 포함된 CSV를 내보낼 수 있습니다:

- 날짜별 세션 수
    - (선택 사항) 세그먼트별 세션 수
    - (선택 사항) 앱 버전별 세션 수
- 날짜별 DAU
    - (선택 사항) 다양한 세그먼트에 대한 DAU
- 날짜별 이메일 통계
    - 전송된 이메일 수
    - 전달된 이메일 수
    - 열람된 이메일 수
    - 이메일 클릭 수
    - 이메일 반송 횟수
    - 스팸으로 신고된 이메일 수
- 날짜별 인앱 메시지
    - 전송된 인앱 메시지 수
    - 인앱 메시지 노출 수
    - 열린 인앱 메시지 수
- 날짜별 MAU
- 날짜별 신규 사용자 수
- 날짜별 푸시 알림
    - (선택 사항) 다양한 앱 플랫폼에 대한 푸시 알림
    - 푸시 알림 전송 횟수
    - 총 열람 수
    - 직접 열람 수
    - 반송 수
- 시간별 세션 수
- 날짜별 MAU당 세션 수
- 날짜별 고착도

{% alert tip %}
CSV 및 API 내보내기에 대한 도움말은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/) 도움말 문서를 참조하세요.
{% endalert %}

