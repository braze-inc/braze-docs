---
page_order: 2
nav_title: 세분화 필터
article_title: 세분화 필터
layout: glossary_page
glossary_top_header: "Segmentation Filters"
glossary_top_text: The Braze SDK provides you with a powerful arsenal of filters to segment and target your users based off of specific features and attributes. You can search or narrow these filters by filter category.<br><br>To learn about the different custom attribute data types you can use to segment users, view <a href="/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types">Custom attribute data types</a>.

page_type: glossary
tool: Segments
description: "이 용어집에는 사용자를 세분화하고 타겟팅하는 데 사용할 수 있는 필터가 나열되어 있습니다."
search_rank: 2
glossary_tag_name: Filter Category
glossary_filter_text: "Select a category to narrow the glossary:"

# channel to icon/fa or image mapping
glossary_tags:
  - name: 세그먼트 또는 CSV 멤버십
  - name: 커스텀 속성
  - name: 커스텀 이벤트
  - name: 세션
  - name: 리타겟팅
  - name: 채널 구독 동작
  - name: 구매 행동
  - name: 인구 통계학적 속성
  - name: 앱
  - name: 제거
  - name: 기기
  - name: 위치
  - name: 코호트 멤버십
  - name: 설치 경로 속성
  - name: 인텔리전스 및 예측
  - name: 사회 활동
  - name: 기타 필터

glossaries:
  - name: 세그먼트 멤버십
    description: "세그먼트, 캠페인 등 필터가 사용되는 모든 곳에서 세그먼트 멤버십을 기준으로 필터링하고 하나의 캠페인 내에서 여러 개의 서로 다른 세그먼트를 타겟팅할 수 있습니다. <br><br>이미 이 필터를 사용하고 있는 세그먼트는 다른 세그먼트에 더 이상 포함하거나 중첩할 수 없는데, 이는 세그먼트 A가 세그먼트 B를 포함하면 다시 세그먼트 A를 포함하려고 하는 사이클이 발생할 수 있기 때문입니다. 그렇게 되면 세그먼트가 계속 자신을 참조하게 되어 실제로 누가 그 세그먼트에 속해 있는지 계산할 수 없게 됩니다. 또한 이와 같이 세그먼트를 중첩하면 복잡성이 증가하여 속도가 느려질 수 있습니다. 대신 동일한 필터를 사용하여 포함하려는 세그먼트를 다시 만듭니다."
    tags:
      - Segment or CSV membership
  - name: Braze 세그먼트 확장
    description: Braze 대시보드에서 세그먼트 확장을 생성한 후 해당 확장을 세그먼트에 포함/제외하도록 선택할 수 있습니다.
    tags:
      - Segment or CSV membership
  - name: CSV에서 업데이트/가져오기
    description: CSV 업로드에 참여했는지 여부에 따라 사용자를 세그먼트화하세요.
    tags:
      - Segment or CSV membership
  - name: 커스텀 속성
    description: "사용자가 커스텀으로 기록된 속성 값과 일치하는지 여부를 결정합니다. <br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Custom attributes
  - name: 만든 곳
    description: 고객 프로필이 생성된 시점을 기준으로 사용자를 세그먼트화합니다. 사용자가 CSV 또는 API를 통해 추가된 경우 이 필터는 사용자가 추가된 날짜를 반영합니다. 사용자가 CSV 또는 API로 추가되지 않았고 소프트웨어 개발 키트에서 첫 번째 세션을 추적하는 경우 이 필터는 첫 번째 세션의 날짜를 반영합니다.
    tags:
      - Other Filters
  - name: 중첩 고객 속성
    description: "커스텀 속성의 속성입니다.<br><br>중첩된 시간 커스텀 속성을 필터링할 때 '요일' 또는 '시간'을 기준으로 필터링하도록 선택할 수 있습니다. '연도'는 비교를 위해 월과 일만 확인합니다. '시간'은 연도를 포함한 전체 타임스탬프를 비교합니다."
    tags:
      - Custom attributes
  - name: 반복 이벤트의 날
    description: "이 필터는 데이터 유형이 '날짜'인 커스텀 속성의 월과 일을 확인하지만 연도는 확인하지 않습니다. 이 필터는 연례 이벤트에 유용합니다.<br><br>시간대:<br>이 필터는 메시징이 현지 시간 예약 옵션을 사용하여 전송되는 경우 사용자가 어떤 시간대에 있는지에 따라 조정되며, 그렇지 않은 경우에는 회사 시간대를 사용합니다."
    tags:
      - Custom attributes
  - name: 커스텀 이벤트
    description: "사용자가 특별히 기록된 이벤트를 수행했는지 여부를 확인합니다.<br><br> 예시:<br>속성 activity_name으로 완료된 활동입니다.<br><br>시간대:<br>UTC - 캘린더 데이 = 1 캘린더 데이는 24-48시간의 사용자 기록을 확인합니다."
    tags:
      - Custom events
  - name: 커스텀 이벤트 최초 실시
    description: "사용자가 특별하게 기록된 이벤트를 수행한 가장 빠른 시간을 확인합니다. (24시간 기간) <br><br>예시:<br> 처음 유기한 장바구니 1일 전<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Custom events
  - name: 최근 수행한 커스텀 이벤트 
    description: "사용자가 특별하게 기록된 이벤트를 수행한 최근 시간을 확인합니다. 이 필터는 0.25시간과 같은 소수점을 지원합니다. (24시간 기간) <br><br>예시:<br> 마지막으로 유기한 장바구니 1일 미만 전<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Custom events
  - name: Y일 내 X 커스텀 이벤트
    description: "사용자가 1~30일 사이의 마지막 지정된 캘린더 일수 동안 0~50회 사이에 특별하게 기록된 이벤트를 수행했는지 여부를 결정합니다. (캘린더 데이 = 1 캘린더 데이는 24-48시간의 사용자 기록을 확인합니다.)<br> <a href=\"/docs/x-in-y-behavior/\"> 여기에서 X-in-Y 동작에 대해 자세히 알아보세요.</a> <br><br>예시:<br>지난 1일 동안 정확히 0번 버려진 장바구니 수<br><br>시간대:<br>UTC - 모든 시간대를 고려하기 위해 세그먼트가 평가되는 시간에 따라 캘린더 1일은 24-48시간의 사용자 기록을, 2일은 48-72시간의 사용자 기록을 살펴보는 식으로 계산합니다."
    tags:
      - Custom events
  - name: Y 일 동안의 커스텀 이벤트 속성정보 제공
    description: "사용자가 1~30일 사이의 마지막 지정된 캘린더 일수 동안 0~50회 사이에 특정 속성과 관련하여 특별히 기록된 이벤트를 수행했는지 여부를 결정합니다. (캘린더 데이 = 1 캘린더 데이는 24-48시간의 사용자 기록을 확인합니다.)<br><a href=\"/docs/x-in-y-behavior/\">여기에서 X-in-Y 동작에 대해 자세히 알아보세요.</a> <br><br>예시:<br> 지난 캘린더 1일 동안 정확히 0번 \"event_name\" 속성을 가진 즐겨찾기에 추가됨<br><br>시간대:<br>UTC - 모든 시간대를 고려하기 위해 세그먼트가 평가되는 시간에 따라 캘린더 1일은 24-48시간의 사용자 기록을, 2일은 48-72시간의 사용자 기록을 살펴보는 식으로 계산합니다."
    tags:
      - Custom events
  - name: 이메일 주소 
    description: "테스트를 위해 개별 이메일 주소로 캠페인 수신자를 지정할 수 있습니다. 또한 필터 내에서 \"이메일 주소가 비어 있지 않음\" 지정자를 사용하여 모든 사용자(탈퇴한 사용자 포함)에게 트랜잭션 이메일을 보낼 수 있으므로 옵트인 상태와 관계없이 이메일 전달을 최대화할 수 있습니다. <br><br>이 필터는 고객 프로필에 이메일 주소가 있는지 여부만 확인하는 반면, <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-available\">이메일 사용 가능</a> 필터는 추가 기준을 확인합니다."
    tags:
      - Other Filters
  - name: 외부 사용자 ID
    description: 테스트를 위해 개별 사용자 ID별로 캠페인 수신자를 지정할 수 있습니다.
    tags:
      - Other Filters
  - name: "랜덤 버킷 번호"
    description: 무작위로 할당된 숫자(0~9999 포함)로 사용자를 세그먼트화합니다. A/B 및 다변량 테스트를 위해 균일하게 분산된 진정한 무작위 사용자 세그먼트를 생성할 수 있습니다.
    tags:
      - Other Filters
  - name: 세션 수
    description: 워크스페이스 내 앱에서 사용자가 참여한 세션 수에 따라 사용자를 세그먼트화하세요.
    tags:
      - Sessions
  - name: 앱 세션 수
    description: 특정 앱에서 특정 세션에 참여한 횟수에 따라 사용자를 세그먼트화합니다.
    tags:
      - Sessions
  - name: 지난 Y일 동안의 X 세션
    description: "1~30일 사이의 지정된 마지막 캘린더 일수 동안 앱에 참여한 세션 수(0~50개)에 따라 사용자를 세그먼트화합니다. <br> <a href=\"/docs/x-in-y-behavior/\">여기에서 X-in-Y 동작에 대해 자세히 알아보세요.</a>"
    tags:
      - Sessions
  - name: 처음 사용한 앱
    description: "사용자가 앱을 가장 먼저 연 기록된 시간을 기준으로 사용자를 세그먼트화합니다. <em>이렇게 하면 Braze SDK가 통합된 앱 버전을 사용하는 첫 번째 세션이 캡처됩니다.</em> (24시간 기간)<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Sessions
  - name: 처음 사용한 특정 앱
    description: "워크스페이스 내에서 가장 먼저 앱을 연 기록된 시간을 기준으로 사용자를 세그먼트화하세요. (24시간 기간)<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Sessions
  - name: 마지막으로 사용한 앱
    description: "사용자가 앱을 가장 최근에 연 시간을 기준으로 사용자를 세그먼트화합니다. (24시간 기간)<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Sessions
  - name: 마지막으로 사용한 특정 앱
    description: "사용자가 특정 앱을 가장 최근에 연 시간으로 사용자를 세그먼트화합니다. (24시간 기간)<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Sessions
  - name: 평균 세션 시간
    description: 앱 내 세션의 평균 길이를 기준으로 사용자를 세그먼트화합니다.
    tags:
      - Sessions
  - name: 캠페인에서 메시지 받기
    description: "특정 캠페인을 수신했는지 여부에 따라 사용자를 세그먼트화합니다.<br><br> 콘텐츠 카드, 배너 및 인앱 메시지의 경우 사용자가 노출 횟수를 기록하는 시점이 아니라 카드 또는 인앱 메시지가 전송된 시점이 기준이 됩니다.<br><br>푸시 및 웹훅의 경우 메시지가 사용자에게 전송되는 시점입니다.<br><br> WhatsApp의 경우 메시징이 사용자의 기기에 전달되는 시점이 아니라 마지막 메시지 API 요청이 WhatsApp으로 전송되는 시점입니다. <br><br>이메일의 경우, 이메일 요청이 이메일 서비스 제공업체에 전송되는 시점입니다(실제로 전달되는지 여부와 무관함). 여러 사용자가 동일한 이메일 주소를 공유하는 경우:<br>- 최초 전송 시에는 특정 타겟팅된 사용자의 프로필만 업데이트됩니다. <br>- 이메일이 전달되거나 사용자가 이메일 또는 이메일의 링크를 열면 해당 이메일 주소를 공유하는 모든 사용자가 메시지를 받은 것으로 표시됩니다.<br><br>SMS의 경우 마지막 메시지가 SMS 제공업체에 전달된 시점입니다. 메시징이 사용자의 기기에 전달되었다는 것을 보장하지는 않습니다."
    tags:
      - Retargeting
  - name: 캠페인 배리언트 받기
    description: "사용자가 수신한 다변량 캠페인 배리언트를 기준으로 사용자를 세그먼트화합니다.<br><br> 콘텐츠 카드, 배너 및 인앱 메시지의 경우 사용자가 노출 횟수를 기록하는 시점이 아니라 카드 또는 인앱 메시지가 전송된 시점이 기준이 됩니다.<br><br>푸시 및 웹훅의 경우 메시지가 사용자에게 전송되는 시점입니다.<br><br> WhatsApp의 경우 메시징이 사용자의 기기에 전달되는 시점이 아니라 마지막 메시지 API 요청이 WhatsApp으로 전송되는 시점입니다. <br><br>이메일의 경우, 이메일 요청이 이메일 서비스 제공업체에 전송되는 시점입니다(실제로 전달되는지 여부와 무관함). 여러 사용자가 동일한 이메일 주소를 공유하는 경우:<br>- 최초 전송 시에는 특정 타겟팅된 사용자의 프로필만 업데이트됩니다. <br>- 이메일이 전달되거나 사용자가 이메일 또는 이메일의 링크를 열면 해당 이메일 주소를 공유하는 모든 사용자가 메시지를 받은 것으로 표시됩니다.<br><br>SMS의 경우 마지막 메시지가 SMS 제공업체에 전달된 시점입니다. 메시징이 사용자의 기기에 전달되었다는 것을 보장하지는 않습니다."
    tags:
      - Retargeting
  - name: 캔버스 단계에서 메시지 받기
    description: "특정 캔버스 컴포넌트를 받았는지 여부에 따라 사용자를 세그먼트화합니다.<br><br> 콘텐츠 카드 및 인앱 메시지의 경우 사용자가 노출 횟수를 기록하는 시점이 아니라 카드 또는 인앱 메시지가 전송되는 시점입니다.<br><br>푸시 및 웹훅의 경우 메시지가 사용자에게 전송되는 시점입니다.<br><br> WhatsApp의 경우 메시징이 사용자의 기기에 전달되는 시점이 아니라 마지막 메시지 API 요청이 WhatsApp으로 전송되는 시점입니다. <br><br>이메일의 경우, 이메일 요청이 이메일 서비스 제공업체에 전송되는 시점입니다(실제로 전달되는지 여부와 무관함). 여러 사용자가 동일한 이메일 주소를 공유하는 경우:<br>- 최초 전송 시에는 특정 타겟팅된 사용자의 프로필만 업데이트됩니다. <br>- 이메일이 전달되거나 사용자가 이메일 또는 이메일의 링크를 열면 해당 이메일 주소를 공유하는 모든 사용자가 메시지를 받은 것으로 표시됩니다.<br><br>SMS의 경우 마지막 메시지가 SMS 제공업체에 전달된 시점입니다. 메시징이 사용자의 기기에 전달되었다는 것을 보장하지는 않습니다."
    tags:
      - Retargeting
  - name: 특정 캔버스 단계에서 마지막으로 수신한 메시지
    description: 특정 캔버스 컴포넌트를 받은 시점을 기준으로 사용자를 세그먼트화합니다. 이 필터는 사용자가 다른 캔버스 컴포넌트를 받은 시기는 고려하지 않습니다.
    tags:
      - Retargeting
  - name: 특정 캠페인에서 마지막으로 수신한 메시지
    description: 특정 캠페인을 수신했는지 여부에 따라 사용자를 세그먼트화합니다. 이 필터는 사용자가 다른 캠페인을 수신한 시기는 고려하지 않습니다.
    tags:
      - Retargeting
  - name: 태그가 있는 캠페인 또는 캔버스에서 메시지 수신
    description: "특정 캠페인 또는 특정 태그가 있는 캔버스를 수신했는지 여부에 따라 사용자를 세그먼트화합니다.<br><br> 콘텐츠 카드, 배너(캠페인만 해당) 및 인앱 메시지의 경우 카드 또는 인앱 메시지가 전송된 시점이 아니라 사용자가 노출 횟수를 기록한 시점을 기준으로 합니다.<br><br>푸시 및 웹훅의 경우 메시지가 사용자에게 전송되는 시점입니다.<br><br> WhatsApp의 경우 메시징이 사용자의 기기에 전달되는 시점이 아니라 마지막 메시지 API 요청이 WhatsApp으로 전송되는 시점입니다. <br><br>이메일의 경우, 이메일 요청이 이메일 서비스 제공업체에 전송되는 시점입니다(실제로 전달되는지 여부와 무관함). 여러 사용자가 동일한 이메일 주소를 공유하는 경우:<br>- 최초 전송 시에는 특정 타겟팅된 사용자의 프로필만 업데이트됩니다. <br>- 이메일이 전달되거나 사용자가 이메일 또는 이메일의 링크를 열면 해당 이메일 주소를 공유하는 모든 사용자가 메시지를 받은 것으로 표시됩니다.<br><br>SMS의 경우 마지막 메시지가 SMS 제공업체에 전달된 시점입니다. 메시징이 사용자의 기기에 전달되었다는 것을 보장하지는 않습니다."
    tags:
      - Retargeting
  - name: 태그가 있는 캠페인 또는 캔버스에서 마지막으로 받은 메시지
    description: 특정 캠페인이나 특정 태그가 있는 캔버스를 수신한 시점을 기준으로 사용자를 세그먼트화합니다. 이 필터는 사용자가 다른 캠페인이나 캔버스를 받은 시기는 고려하지 않습니다. (24시간 기간)
    tags:
      - Retargeting
  - name: 캠페인 또는 캔버스 단계에서 메시지를 받은 적이 없음
    description: 캠페인 또는 캔버스 컴포넌트를 수신했는지 여부에 따라 사용자를 세그먼트화합니다.
    tags:
      - Retargeting
  - name: 마지막으로 받은 이메일
    description: "사용자가 마지막으로 이메일 메시지를 받은 시간을 기준으로 사용자를 세그먼트화합니다. (24시간 기간)<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Retargeting
  - name: 마지막으로 받은 푸시
    description: "사용자가 마지막으로 푸시 알림을 받은 시간을 기준으로 사용자를 세그먼트화합니다. (24시간 기간)<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Retargeting
  - name: 마지막 인앱 메시지 노출 횟수
    description: 사용자가 마지막으로 인앱 메시지를 본 시간을 기준으로 사용자를 세분화합니다.
    tags:
      - Retargeting
  - name: 마지막으로 수신한 SMS
    description: "마지막 메시지가 SMS 제공업체에 전달된 시간을 기준으로 사용자를 세그먼트화합니다. 메시징이 사용자의 기기에 전달되었다는 것을 보장하지는 않습니다. (24시간 기간)<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Retargeting
  - name: 마지막으로 수신한 웹훅
    description: "해당 사용자에 대해 마지막으로 Braze가 웹훅을 보낸 시간을 기준으로 사용자를 세그먼트화합니다. (24시간 기간)<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Retargeting
  - name: 마지막으로 받은 WhatsApp
    description: "사용자가 마지막으로 WhatsApp 메시지를 받은 시간을 기준으로 사용자를 세그먼트화합니다. 이는 메시징이 사용자의 기기에 전달되는 시점이 아니라 마지막 메시지 API 요청이 WhatsApp으로 전송되는 시점입니다. (24시간 기간)<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Retargeting
  - name: 클릭/열린 캠페인
    description: "특정 캠페인과의 상호작용을 기준으로 필터링합니다. 이메일 메시징의 경우 열기 이벤트에는 컴퓨터 열기와 컴퓨터 외 열기 모두 포함됩니다.<br><br> 이메일의 경우 '모든 이메일 열기(컴퓨터 열기)' 및 '모든 이메일 열기(기타 열기)'로 필터링하는 옵션도 포함되어 있습니다. 여러 사용자가 동일한 이메일 주소를 공유하는 경우:<br>- 이메일을 열거나 클릭하면 같은 이메일 주소를 가진 다른 모든 사용자의 프로필도 업데이트됩니다. <br>- 메시징이 전송된 후 열기 또는 클릭 전에 원래 사용자가 이메일 주소를 변경하면 원래 사용자 대신 해당 이메일 주소를 가진 나머지 모든 사용자에게 열기 또는 클릭이 적용됩니다.<br><br>SMS의 경우 상호 작용은 다음과 같이 정의됩니다:<br>- 사용자가 마지막으로 특정 키워드 카테고리와 일치하는 답장 SMS를 보냈습니다. 이는 이 전화번호를 사용하는 모든 사용자가 가장 최근에 받은 캠페인의 기여도에 기인합니다. 캠페인은 지난 4시간 이내에 접수된 것이어야 합니다.<br>- 사용자가 특정 캠페인에서 사용자 클릭 추적이 켜져 있는 SMS 메시지에서 단축 링크를 마지막으로 선택했습니다."
    tags:
      - Retargeting
  - name: 클릭/열린 캠페인 또는 태그가 있는 캔버스
    description: "특정 태그가 있는 특정 캠페인과의 상호작용을 기준으로 필터링합니다. 이메일 메시징의 경우 열기 이벤트에는 컴퓨터 열기와 컴퓨터 외 열기 모두 포함됩니다.<br><br> 이메일의 경우 '모든 이메일 열기(컴퓨터 열기)' 및 '모든 이메일 열기(기타 열기)'를 기준으로 필터링하는 옵션이 포함되어 있습니다. 여러 사용자가 동일한 이메일 주소를 공유하는 경우:<br>- 이메일을 열거나 클릭하면 같은 이메일 주소를 가진 다른 모든 사용자의 프로필도 업데이트됩니다. <br>- 메시징이 전송된 후 열기 또는 클릭 전에 원래 사용자가 이메일 주소를 변경하면 원래 사용자 대신 해당 이메일 주소를 가진 나머지 모든 사용자에게 열기 또는 클릭이 적용됩니다.<br><br>SMS의 경우 상호 작용은 다음과 같이 정의됩니다:<br>- 사용자가 마지막으로 특정 키워드 카테고리와 일치하는 답장 SMS를 보냈습니다. 이는 이 전화번호를 사용하는 모든 사용자가 가장 최근에 받은 캠페인의 기여도에 기인합니다. 캠페인은 지난 4시간 이내에 접수된 것이어야 합니다.<br>- 사용자 클릭 추적이 켜져 있는 SMS 메시지에서 사용자가 태그가 있는 특정 캠페인 또는 캔버스 단계에서 단축 링크를 마지막으로 선택한 경우."
    tags:
      - Retargeting
  - name: 클릭/열기 단계
    description: "특정 캔버스 컴포넌트와의 상호작용을 기준으로 필터링합니다. 이메일 메시징의 경우 열기 이벤트에는 컴퓨터 열기와 컴퓨터 외 열기 모두 포함됩니다.<br><br>이메일의 경우 '모든 이메일 열기(컴퓨터 열기)' 및 '모든 이메일 열기(기타 열기)'를 기준으로 필터링하는 옵션이 포함되어 있습니다.<br><br>SMS의 경우 상호 작용은 다음과 같이 정의됩니다:<br>- 사용자가 마지막으로 특정 키워드 카테고리와 일치하는 답장 SMS를 보냈습니다. 이는 이 전화번호를 사용하는 모든 사용자가 가장 최근에 받은 캠페인의 기여도에 기인합니다. 캠페인은 지난 4시간 이내에 접수된 것이어야 합니다. <br>- 사용자가 특정 캔버스 단계에서 사용자 클릭 추적이 켜져 있는 SMS 메시지에서 단축 링크를 마지막으로 선택했습니다."
    tags:
      - Retargeting
  - name: 캠페인에서 별칭 클릭
    description: "특정 캠페인에서 특정 별칭을 클릭했는지 여부에 따라 사용자를 필터링하세요. 이는 이메일 메시징에만 적용됩니다. <br><br> 여러 사용자가 동일한 이메일 주소를 공유하는 경우:<br>- 이메일을 열거나 클릭하면 같은 이메일 주소를 가진 다른 모든 사용자의 프로필도 업데이트됩니다. <br>- 메시징이 전송된 후 열기 또는 클릭 전에 원래 사용자가 이메일 주소를 변경하면 원래 사용자 대신 해당 이메일 주소를 가진 나머지 모든 사용자에게 열기 또는 클릭이 적용됩니다."
    tags:
      - Retargeting
  - name: 캔버스 단계에서 별칭 클릭
    description: "특정 캔버스에서 특정 별칭을 클릭했는지 여부에 따라 사용자를 필터링하세요. 이는 이메일 메시징에만 적용됩니다. <br><br> 여러 사용자가 동일한 이메일 주소를 공유하는 경우:<br>- 이메일을 열거나 클릭하면 같은 이메일 주소를 가진 다른 모든 사용자의 프로필도 업데이트됩니다. <br>- 메시징이 전송된 후 열기 또는 클릭 전에 원래 사용자가 이메일 주소를 변경하면 원래 사용자 대신 해당 이메일 주소를 가진 나머지 모든 사용자에게 열기 또는 클릭이 적용됩니다."
    tags:
      - Retargeting
  - name: 캠페인 또는 캔버스 단계에서 별칭 클릭
    description: "캠페인 또는 캔버스에서 특정 별칭을 클릭했는지 여부에 따라 사용자를 필터링하세요. 이는 이메일 메시징에만 적용됩니다. <br><br> 여러 사용자가 동일한 이메일 주소를 공유하는 경우:<br>- 이메일을 열거나 클릭하면 같은 이메일 주소를 가진 다른 모든 사용자의 프로필도 업데이트됩니다. <br>- 메시징이 전송된 후 열기 또는 클릭 전에 원래 사용자가 이메일 주소를 변경하면 원래 사용자 대신 해당 이메일 주소를 가진 나머지 모든 사용자에게 열기 또는 클릭이 적용됩니다."
    tags:
      - Retargeting
  - name: 하드 바운스
    description: "이메일 주소가 하드 바운스되었는지 여부(예: 이메일 주소가 유효하지 않은 경우)에 따라 사용자를 세그먼트화하세요."
    tags:
      - Retargeting
  - name: 소프트 바운스
    description: Y일 동안 소프트 바운스 횟수별로 사용자를 세분화하세요. 세그먼트 필터는 30일만 되돌아볼 수 있지만 세그먼트 확장을 사용하면 더 오래 되돌아볼 수 있습니다.<br><br>이 필터는 커런츠의 소프트 바운스 이벤트와 다르게 작동합니다. 소프트 바운스 세그먼트 필터는 72시간의 재시도 기간 동안 전달에 성공하지 못한 경우 소프트 바운스를 계산합니다. 커런츠에서는 실패한 모든 재시도가 소프트 바운스 이벤트로 전송됩니다. 
    tags:
      - Retargeting
  - name: 스팸으로 표시됨
    description: 사용자가 메시지를 스팸으로 표시했는지 여부에 따라 사용자를 세분화합니다.
    tags:
      - Retargeting
  - name: 잘못된 전화 번호 
    description: 전화번호가 유효하지 않은지 여부에 따라 사용자를 세그먼트화합니다.
    tags:
      - Retargeting
  - name: 마지막으로 전송된 특정 SMS 인바운드 키워드 카테고리
    description: 특정 키워드 카테고리 내의 특정 구독 그룹에 마지막으로 SMS를 보낸 시점을 기준으로 사용자를 세그먼트화합니다. 
    tags:
      - Retargeting
  - name: 캠페인에서 전환됨
    description: 특정 캠페인에서 전환했는지 여부에 따라 사용자를 세그먼트화합니다. 이 필터에는 대조군에 속한 사용자는 포함되지 않습니다.
    tags:
      - Retargeting
  - name: 캔버스에서 변환됨
    description: 특정 캔버스에서 전환했는지 여부에 따라 사용자를 세그먼트화합니다. 이 필터에는 대조군에 속한 사용자는 포함되지 않습니다.
    tags:
      - Retargeting
  - name: 캠페인 대조군에서
    description: 특정 다변량 캠페인의 대조군에 속했는지 여부에 따라 사용자를 세그먼트화합니다.
    tags:
      - Retargeting
  - name: 캔버스 대조군에서
    description: 특정 캔버스에 대한 대조군에 속했는지 여부에 따라 사용자를 세그먼트화합니다. 이 필터는 캔버스에 입장한 사용자만 평가합니다.<br><br>예를 들어 캔버스의 대조군에 속하지 않는 사용자를 필터링하면 캔버스에 들어왔지만 대조군에 속하지 않는 모든 사용자를 받게 됩니다.
    tags:
      - Retargeting
  - name: 대조군에 마지막으로 등록한 경우
    description: "캠페인에서 마지막으로 대조군에 속했던 시간별로 사용자를 세그먼트화합니다. <br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Retargeting
  - name: 입력된 캔버스 변형
    description: 특정 캔버스의 변형 경로를 입력했는지 여부에 따라 사용자를 세그먼트화합니다. 이 필터는 모든 사용자를 평가합니다.<br><br>예를 들어 캔버스 변형 대조군에 들어가지 않은 사용자를 필터링하면 캔버스 입력 여부와 관계없이 대조군에 속하지 않은 모든 사용자를 받게 됩니다.
    tags:
      - Retargeting
  - name: 마지막으로 수신한 모든 메시지
    description: "마지막으로 수신한 메시지를 확인하여 사용자를 세그먼트화합니다. (24시간 기간)<br><br> 콘텐츠 카드, 배너 및 인앱 메시지의 경우 사용자가 마지막으로 노출 횟수를 기록한 시점이 아니라 카드 또는 인앱 메시지가 마지막으로 전송된 시점이 기준이 됩니다.<br><br>푸시 및 웹훅의 경우 사용자에게 메시지가 전송된 때입니다.<br><br> WhatsApp의 경우 메시징이 사용자의 기기에 전달된 시점이 아니라 마지막 메시지 API 요청이 WhatsApp에 전송된 시점이 기준이 됩니다. <br><br>이메일의 경우, 이메일 요청이 이메일 서비스 제공업체에 전송되는 시점입니다(실제로 전달되는지 여부와 무관함). 여러 사용자가 동일한 이메일 주소를 공유하는 경우:<br>- 최초 전송 시에는 특정 타겟팅된 사용자의 프로필만 업데이트됩니다. <br>- 이메일이 전달되거나 사용자가 이메일 또는 이메일의 링크를 열면 해당 이메일 주소를 공유하는 모든 사용자가 메시지를 받은 것으로 표시됩니다.<br><br>SMS의 경우 마지막 메시지가 SMS 제공업체에 전달된 시점입니다. 메시징이 사용자의 기기에 전달되었다는 것을 보장하지는 않습니다.<br><br>예시:<br>마지막으로 받은 메시지 1일 전 미만 = 24시간 전 미만<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Retargeting
  - name: 마지막으로 메시징에 참여한 시간
    description: "메시징 채널(배너, 콘텐츠 카드, 이메일, 인앱, SMS, 푸시, WhatsApp) 중 하나를 마지막으로 클릭하거나 열어본 시간별로 사용자를 세분화합니다. 이메일 메시징의 경우 열기 이벤트에는 컴퓨터 열기와 컴퓨터 외 열기 모두 포함됩니다. (24시간 기간)<br><br>이메일의 경우, 이메일 요청이 이메일 서비스 제공업체에 전송되는 시점입니다(실제로 전달되는지 여부와 무관함). 여기에는 '모든 이메일 열기(컴퓨터 열기)' 및 '모든 이메일 열기(기타 열기)'로 필터링하는 옵션도 포함되어 있습니다. 여러 사용자가 동일한 이메일 주소를 공유하는 경우:<br>- 최초 전송 시에는 특정 타겟팅된 사용자의 프로필만 업데이트됩니다. <br>- 이메일이 전달되거나 사용자가 이메일 또는 이메일의 링크를 열면 해당 이메일 주소를 공유하는 모든 사용자가 메시지를 받은 것으로 표시됩니다.<br><br>SMS의 경우, 사용자 클릭 추적이 켜져 있는 메시지에서 사용자가 마지막으로 단축 링크를 선택한 때입니다.<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Retargeting
  - name: 클릭한 카드 
    description: "특정 콘텐츠 카드를 클릭했는지 여부에 따라 사용자를 세그먼트화합니다. 이 필터는 '클릭/열린 캠페인', '클릭/열린 캠페인 또는 태그가 있는 캔버스', '클릭/열린 단계'의 하위 필터로 사용할 수 있습니다."
    tags:
      - Retargeting
  - name: 기능 플래그
    description: "현재 특정 <a href=\"/docs/developer_guide/feature_flags/\">기능 플래그가</a> 인에이블된 사용자 세그먼트입니다."
    tags:
      - Retargeting
  - name: 구독 그룹
    description: "이메일, SMS/MMS 또는 WhatsApp의 구독 그룹별로 사용자를 세그먼트화하세요. 보관된 그룹은 표시되지 않으며 사용할 수 없습니다."
    tags:
      - Channel subscription behavior
  - name: 이메일 사용 가능
    description: "유효한 이메일 주소가 있는지 여부와 이메일에 가입했는지 또는 옵트인했는지 여부에 따라 사용자를 세그먼트화합니다. 이 필터는 사용자가 이메일에서 탈퇴했는지, Braze가 하드 바운스를 받았는지, 이메일이 스팸으로 표시되었는지 등 세 가지 기준을 확인합니다. 이러한 기준 중 하나라도 충족되지 않거나 사용자에 대한 이메일이 존재하지 않는 경우 해당 사용자는 포함되지 않습니다.<br><br>트랜잭션 이메일을 보내는 경우 '이메일 사용 가능'이 <code>거짓인</code> 사용자는 오디언스 계산에 포함되지 않지만 여전히 메시지를 받을 수 있습니다. 그러나 오디언스 계산에는 가입하거나 옵트인한 사용자만 포함됩니다. <br><br>옵트인 상태가 중요한 이메일의 경우 <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-address\">이메일 주소</a> 필터 대신 '이메일 사용 가능' 필터를 사용하는 것이 좋으며, 추가 기준을 사용하면 메시지를 실제로 보고 싶어하는 사용자를 타겟팅하는 데 도움이 될 수 있습니다."
    tags:
      - Channel subscription behavior
  - name: 이메일 옵트인 날짜
    description: 사용자가 이메일을 옵트인한 날짜를 기준으로 사용자를 세그먼트화합니다.
    tags:
      - Channel subscription behavior
  - name: 이메일 구독 상태
    description: 이메일 구독 상태에 따라 사용자를 세그먼트화하세요.
    tags:
      - Channel subscription behavior
  - name: 이메일 탈퇴 날짜 
    description: 향후 이메일에서 탈퇴한 날짜를 기준으로 사용자를 세그먼트화합니다.
    tags:
      - Channel subscription behavior
  - name: 포 그라운드 푸시 인에이블먼트
    description: "임시 푸시 권한이 있거나 포그라운드 푸시가 인에이블된 사용자를 세그먼트화합니다. 구체적으로 이 수에는 다음이 포함됩니다:<br>푸시 권한이 잠정적으로 승인된 iOS 사용자. <br>2. 포그라운드 푸시가 인에이블먼트되어 있고 푸시 구독 상태가 탈퇴되지 않은 사용자(모든 앱에 대해). 이러한 사용자의 경우 이 카운트에는 포그라운드 푸시만 포함됩니다.<br><br>포그라운드 푸시 인에이블먼트에는 탈퇴한 사용자는 포함되지 않습니다. <br><br>이 필터를 사용하여 세그먼트를 세분화하면 하단 패널에서 <em>도달 가능한 사용자라는</em> 이름으로 해당 세그먼트에 속한 Android, iOS 및 웹 사용자에 대한 분석을 볼 수 있습니다."
    tags:
      - Channel subscription behavior
  - name: 앱에 포그라운드 푸시 인에이블먼트 사용
    description: 사용자가 기기에서 앱에 푸시 인에이블먼트가 설정되어 있는지 여부에 따라 세그먼트화합니다. 앱에 대해 포그라운드 푸시 인에이블먼트된 사용자. 여기에는 푸시 구독 상태가 고려되지 않습니다. 이 수에는 포그라운드 및 백그라운드 푸시 토큰을 잠정적으로 승인한 사용자가 포함됩니다.
    tags:
      - Channel subscription behavior
  - name: 백그라운드 또는 포그라운드 푸시 인에이블먼트
    description: 사용자가 푸시 토큰을 보유하고 있고 탈퇴하지 않았는지 여부에 따라 세그먼트화합니다. 앱에 대해 백그라운드 또는 포그라운드 푸시 인에이블먼트된 사용자입니다.
    tags:
      - Channel subscription behavior
  - name: 푸시 옵트인 날짜
    description: 사용자가 푸시를 옵트인한 날짜를 기준으로 사용자를 세그먼트화합니다.
    tags:
      - Channel subscription behavior
  - name: 푸시 구독 상태
    description: "푸시를 위해 <a href=\"/docs/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-subscription-state\">구독 상태에</a> 따라 사용자를 세그먼트화합니다."
    tags:
      - Channel subscription behavior
  - name: 푸시 탈퇴 날짜
    description: 향후 푸시 알림을 탈퇴한 날짜를 기준으로 사용자를 세그먼트화합니다.
    tags:
      - Channel subscription behavior
  - name: 구매한 제품
    description: 앱에서 구매한 제품별로 사용자를 세그먼트화하세요.
    tags:
      - Purchase behavior
  - name: 총 구매 횟수
    description: 앱에서 구매한 횟수에 따라 사용자를 세그먼트화하세요.
    tags:
      - Purchase behavior
  - name: Y일 동안 구매한 X 제품 수
    description: 특정 제품을 구매한 시간별로 사용자를 필터링하세요.
    tags:
      - Purchase behavior
  - name: 지난 Y일 동안의 X 구매
    description: "1~30일 사이의 지정된 마지막 캘린더 일수 동안 구매를 한 횟수(0~50)로 사용자를 세그먼트화합니다. <br> <a href=\"/docs/x-in-y-behavior/\">여기에서 X-in-Y 동작에 대해 자세히 알아보세요.</a>"
    tags:
      - Purchase behavior
  - name: Y일 내 X 구매 속성정보
    description: "1~30일 사이의 지정된 마지막 캘린더 일수 동안 특정 구매 속성정보와 관련하여 구매가 이루어진 횟수에 따라 사용자를 세그먼트화합니다. <br> <a href=\"/docs/x-in-y-behavior/\">여기에서 X-in-Y 동작에 대해 자세히 알아보세요.</a>"
    tags:
      - Purchase behavior
  - name: 첫 구매
    description: 사용자가 앱에서 가장 먼저 구매한 시점을 기준으로 사용자를 세그먼트화합니다.
    tags:
      - Purchase behavior
  - name: 앱 첫 구매
    description: 사용자가 앱에서 가장 먼저 구매한 시점을 기준으로 사용자를 세그먼트화합니다.
    tags:
      - Purchase behavior
  - name: 마지막 구매
    description: 마지막으로 구매한 시간별로 사용자를 필터링합니다.
    tags: 
      - Purchase behavior
  - name: 마지막으로 구매한 제품
    description: 특정 제품을 마지막으로 구매한 시점을 기준으로 사용자를 필터링하세요.
    tags:
      - Purchase behavior
  - name: 지출한 돈
    description: 앱에서 지출한 금액에 따라 사용자를 세그먼트화하세요.
    tags:
      - Purchase behavior
  - name: Y일 동안 지출한 X 금액
    description: "사용자가 지난 1~30일 사이의 지정된 캘린더 일수 동안 앱에서 지출한 금액에 따라 사용자를 세그먼트화합니다. 이 금액에는 최근 50회 구매 금액의 합계만 포함됩니다. <br> <a href=\"/docs/x-in-y-behavior/\">여기에서 X-in-Y 동작에 대해 자세히 알아보세요.</a>"
    tags:
      - Purchase behavior
  - name: 국가
    description: 마지막으로 표시된 국가 위치에 따라 사용자를 세그먼트화합니다.
    tags:
      - Demographic attributes
  - name: 도시
    description: 마지막으로 표시된 도시 위치를 기준으로 사용자를 세그먼트화합니다.
    tags:
      - Demographic attributes
  - name: 언어
    description: 선호하는 언어별로 사용자를 세그먼트화하세요.
    tags:
      - Demographic attributes
  - name: 나이
    description: 앱 내에서 사용자가 지정한 연령에 따라 사용자를 세그먼트화합니다.
    tags:
      - Demographic attributes
  - name: 생일
    description: "앱 내에서 사용자가 지정한 생일에 따라 사용자를 세그먼트화합니다. <br> 2월 29일이 생일인 사용자는 3월 1일을 포함한 세그먼트에 포함됩니다.<br><br>12월 또는 1월 생일을 타겟팅하려면 타겟팅하려는 연도의 12개월 범위 내에서만 필터 로직을 삽입하세요. 즉, 전년도 캘린더의 12월로 돌아가거나 내년 1월로 앞당기는 로직을 삽입하지 마세요. 예를 들어 12월 생일을 타겟팅하려면 '12월 31일', '12월 31일 이전' 또는 '11월 30일 이후'로 필터링할 수 있습니다."
    tags:
      - Demographic attributes
  - name: 성별
    description: 앱 내에서 사용자가 지정한 대로 사용자를 성별에 따라 세그먼트화합니다.
    tags:
      - Demographic attributes
  - name: 형식화되지 않은 전화 번호
    description: "형식화되지 않은 전화번호를 기준으로 사용자를 세그먼트화합니다. 괄호, 대시 또는 기타 기호를 포함하지 않습니다."
    tags:
      - Demographic attributes
  - name: 이름
    description: 앱 내에서 사용자가 지정한 이름에 따라 사용자를 세그먼트화합니다.
    tags:
      - Demographic attributes
  - name: 성
    description: 앱 내에서 사용자가 지정한 대로 성을 기준으로 사용자를 세그먼트화합니다.
    tags:
      - Demographic attributes
  - name: 앱 있음
    description: 사용자가 앱을 설치했는지 여부에 따라 세그먼트를 세분화합니다. 여기에는 현재 앱을 설치한 사용자와 과거에 앱을 삭제한 사용자가 포함됩니다. 일반적으로 이 필터에 포함되려면 사용자가 앱을 열어야 합니다(세션 시작). 그러나 사용자를 Braze로 가져와 앱에 수동으로 연결한 경우와 같은 몇 가지 예외가 있습니다.
    tags:
      - App
  - name: 가장 최근 앱 버전 이름
    description: "사용자 앱의 최근 이름으로 세그먼트를 세분화합니다.<br><br>\"보다 작음\" 또는 \"보다 작거나 같음\"을 사용할 때 기본 앱 버전이 존재하지 않으면 사용자가 앱 버전보다 오래되었기 때문에 이 필터는 'true'를 반환합니다. 즉, 사용자의 마지막 기본 앱 버전이 존재하지 않으면 자동으로 필터와 일치합니다."
    tags:
      - App 
  - name: 가장 최근 앱 버전 번호
    description: "사용자 앱의 최근 앱 버전 번호로 세그먼트화합니다.<br><br>\"보다 작음\" 또는 \"보다 작거나 같음\"을 사용할 때 기본 앱 버전이 존재하지 않으면 사용자가 앱 버전보다 오래되었기 때문에 이 필터는 'true'를 반환합니다. 즉, 사용자의 마지막 기본 앱 버전이 존재하지 않으면 자동으로 필터와 일치합니다.<br><br>현재 앱 버전이 업데이트되는 데 시간이 걸릴 수 있습니다. 고객 프로필의 앱 버전은 사용자가 앱을 여는 시점에 따라 소프트웨어 개발 키트에 의해 정보가 캡처되면 업데이트됩니다. 사용자가 앱을 열지 않으면 현재 버전이 업데이트되지 않습니다. 이러한 필터는 소급 적용되지 않습니다. 현재 버전과 향후 버전에 \"보다 큼\" 또는 \"같음\"을 사용하는 것이 좋지만 과거 버전 필터를 사용하면 예기치 않은 동작이 발생할 수 있습니다."
    tags:
      - App 
  - name: 제거됨
    description: "앱을 삭제했는지, 다시 설치했는지 여부에 따라 사용자를 세그먼트화합니다."
    tags:
      - Uninstall 
  - name: 기기 사업자
    description: 사용자를 기기 통신사별로 세그먼트화하세요.
    tags:
      - Devices
  - name: 기기 수
    description: 앱을 사용한 기기 수에 따라 사용자를 세그먼트화하세요.
    tags:
      - Devices
  - name: 기기 모델
    description: 휴대폰 모델 버전별로 사용자를 세그먼트화하세요.
    tags:
      - Devices
  - name: 기기 OS
    description: 지정된 운영 체제를 사용하는 기기를 하나 이상 보유한 사용자를 세그먼트화합니다.
    tags:
      - Devices
  - name: 최신 기기 로캘
    description: "가장 최근에 사용한 기기의 <a href=\"/docs/user_guide/engagement_tools/campaigns/ideas_and_strategies/localizing_a_campaign/\">로캘 정보에</a> 따라 사용자를 세그먼트화합니다."
    tags:
      - Devices      
  - name: 최신 시계 모델
    description: 가장 최근 스마트워치 모델별로 사용자를 세그먼트화합니다.
    tags:
      - Devices    
  - name: iOS에서 잠정 승인됨
    description: 특정 앱에 대해 iOS 12에서 잠정적으로 승인된 사용자를 찾을 수 있습니다.
    tags:
      - Devices   
  - name: 웹 브라우저
    description: 웹사이트에 액세스하는 데 사용하는 웹 브라우저를 기준으로 사용자를 세그먼트화합니다.
    tags:
      - Devices
  - name: 기기 IDFA
    description: IDFA별로 캠페인 수신자를 지정하여 테스트할 수 있습니다.
    tags:
      - Advertising use cases
  - name: 기기 IDFV
    description: 테스트를 위해 IDFV별로 캠페인 수신자를 지정할 수 있습니다.
    tags:
      - Advertising use cases 
  - name: 기기 Google 광고 ID
    description: Google 광고 ID를 기준으로 사용자를 세그먼트화합니다.
    tags:
      - Advertising use cases
  - name: 기기 Roku 광고 ID
    description: Roku 광고 ID를 기준으로 사용자를 세그먼트화합니다.
    tags:
      - Advertising use cases
  - name: 기기 윈도우 광고 ID
    description: Windows 광고 ID를 기준으로 사용자를 세그먼트화합니다.
    tags:
      - Advertising use cases  
  - name: 광고 추적 활성화됨
    description: "사용자가 광고 추적에 옵트인했는지 여부에 따라 필터링할 수 있습니다. 광고 추적은 Apple이 모든 iOS 기기에 할당하는 IDFA 또는 '광고주 식별자'와 관련이 있으며, 이는 SDK로 설정할 수 있습니다. 이 식별자를 통해 광고주는 사용자를 추적하고 타겟팅 광고를 게재할 수 있습니다."
    tags:
      - Advertising use cases
  - name: 가장 최근 위치
    description: 마지막으로 앱을 사용한 기록된 위치를 기준으로 사용자를 세그먼트화합니다.
    tags:
      - Location
  - name: 사용 가능한 위치
    description: "위치를 신고했는지 여부에 따라 사용자를 세그먼트화합니다. 이 필터를 사용하려면 앱에 <a href=\"/docs/search/?query=location%20tracking\">위치 추적 기능이 통합되어</a> 있어야 합니다."
    tags:
      - Location
  - name: Amplitude 코호트
    description: Amplitude를 사용하는 클라이언트는 Amplitude에서 코호트를 선택하고 가져와서 세그먼트를 보완할 수 있습니다.
    tags:
      - Cohort membership
  - name: Census 코호트
    description: Census를 사용하는 클라이언트는 Census에서 코호트를 선택하고 가져와서 세그먼트를 보완할 수 있습니다.
    tags:
      - Cohort membership
  - name: 힙 코호트
    description: Heap을 사용하는 클라이언트는 Heap에서 코호트를 선택하고 가져와서 세그먼트를 보완할 수 있습니다.
    tags:
      - Cohort membership
  - name: Hightouch 코호트
    description: Hightouch를 사용하는 클라이언트는 Hightouch에서 코호트를 선택하고 가져와서 세그먼트를 보완할 수 있습니다.
    tags:
      - Cohort membership
  - name: Kubit 코호트
    description: Kubit을 사용하는 클라이언트는 Kubit에서 코호트를 선택하고 가져와서 세그먼트를 보완할 수 있습니다.
    tags:
      - Cohort membership
  - name: Mixpanel 코호트
    description: Mixpanel을 사용하는 클라이언트는 Mixpanel에서 코호트를 선택하고 가져와서 세그먼트를 보완할 수 있습니다.
    tags:
      - Cohort membership
  - name: 세그먼트 코호트
    description: 세그먼트를 사용하는 클라이언트는 세그먼트에서 코호트를 선택하여 가져와서 세그먼트를 보완할 수 있습니다.
    tags:
      - Cohort membership
  - name: Tinyclues 코호트
    description: Tinyclues를 사용하는 클라이언트는 Tinyclues에서 코호트를 선택하고 가져와서 세그먼트를 보완할 수 있습니다.
    tags:
      - Cohort membership
  - name: 설치 경로 광고 설치
    description: 설치 기여도가 높은 광고에 따라 사용자를 세그먼트화합니다.
    tags:
      - User Attributes
  - name: 기여도 애드그룹 설치 경로
    description: 사용자의 설치 경로가 기여한 광고 그룹별로 사용자를 세그먼트화합니다.
    tags:
      - Install Attribution
  - name: 설치 경로 기여도 캠페인
    description: 설치 기여도가 높은 광고 캠페인을 기준으로 사용자를 세그먼트화합니다.
    tags:
      - Install Attribution
  - name: 설치 기여도 소스
    description: 설치 기여도가 높은 소스를 기준으로 사용자를 세그먼트화합니다.
    tags:
      - Install Attribution
  - name: 고객이탈 위험 카테고리
    description:  특정 예측에 따라 이탈 위험 범주별로 사용자를 세그먼트화하세요.
    tags:
      - Intelligence and predictive
  - name: 고객이탈 위험 점수
    description: 특정 예측에 따라 이탈 위험 점수에 따라 사용자를 세그먼트화하세요.
    tags:
      - Intelligence and predictive
  - name: 이벤트 가능성 카테고리
    description: 특정 예측에 따라 이벤트 수행 가능성에 따라 사용자를 세그먼트화하세요.
    tags:
      - Intelligence and predictive
  - name: 이벤트 가능성 점수
    description: 특정 예측에 따라 이벤트 수행 가능성에 따라 사용자를 세그먼트화하세요.
    tags:
      - Intelligence and predictive
  - name: 인텔리전트 채널
    description: 지난 3개월 동안 가장 활발하게 활동한 채널을 기준으로 사용자를 세그먼트화하세요.
    tags:
      - Intelligence and predictive
  - name: 메시지 열기 가능성
    description: "지정된 채널에서 메시지를 열 가능성에 따라 0~100% 범위에서 사용자를 필터링합니다. 채널의 가능성을 측정할 수 있는 충분한 데이터가 없는 사용자는 \"비어 있음\"을 사용하여 선택할 수 있습니다."
    tags:
      - Intelligence and predictive
  - name: 앱을 사용하는 Facebook 친구 수
    description: 같은 앱을 사용하는 Facebook 친구 수에 따라 사용자를 세그먼트화합니다.
    tags:
      - Social activity
  - name: 연결된 Facebook
    description: 앱을 Facebook에 연결했는지 여부에 따라 사용자를 세그먼트화합니다.
    tags:
      - Social activity
  - name: 연결된 트위터
    description: 앱이 X(이전의 트위터)에 연결되었는지 여부에 따라 사용자를 세그먼트화합니다.
    tags:
      - Social activity
  - name: 트위터 팔로워 수
    description: 사용자가 보유한 팔로워 수 X(이전의 트위터) 수에 따라 사용자를 세그먼트화합니다.
    tags:
      - Social activity
  - name: 전화번호
    description: "E.164 형식의 전화번호 필드를 기준으로 사용자를 세그먼트화합니다.<br><br> 전화번호가 Braze로 전송되면 Braze는 SMS 및 WhatsApp 채널에서 전송하는 데 사용되는 <a href=\"/docs/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers\">e.164 형식으로</a> 강제로 전송하려고 시도합니다. 번호의 형식이 제대로 지정되지 않은 경우 강제 프로세스가 실패하여 고객 프로필에 형식이 지정되지 않은 전화번호가 있지만 발신 전화번호가 없는 결과가 발생할 수 있습니다. 이 세그먼트 필터는 e.164 형식의 전화번호(사용 가능한 경우)로 사용자를 반환합니다.<br><br>사용 사례:<br> - 이 필터를 사용하면 SMS 또는 WhatsApp 메시지를 보낼 때 가장 정확한 타겟팅 대상자 규모를 파악할 수 있습니다.  <br>- 이 필터와 함께 정규표현식(정규식)을 사용하여 특정 국가 코드가 있는 전화번호로 세그먼트화할 수 있습니다. <br>- 이 필터를 사용하여 e.164 강제 프로세스에 실패한 전화번호를 기준으로 사용자를 세그먼트화할 수 있습니다."
    tags:
      - Other filters
---
