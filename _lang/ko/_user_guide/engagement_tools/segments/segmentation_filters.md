---
page_order: 2
nav_title: 세분화 필터
article_title: 세분화 필터
layout: glossary_page
glossary_top_header: "세분화 필터"
glossary_top_text: "Braze SDK는 특정 기능 및 속성을 기반으로 사용자를 세분화하고 타겟팅할 수 있는 강력한 필터 모음을 제공합니다. 필터 카테고리별로 이러한 필터를 검색하거나 범위를 좁힐 수 있습니다.<br><br>사용자를 세분화하는 데 사용할 수 있는 다양한 커스텀 속성 데이터 유형에 대해 알아보려면 <a href=\"/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types\">커스텀 속성 데이터 유형</a>을 참조하세요."

page_type: glossary
tool: Segments
description: "이 용어집에는 사용자를 세분화하고 타겟팅하는 데 사용할 수 있는 필터가 나열되어 있습니다."
search_rank: 2
glossary_tag_name: 필터 카테고리
glossary_filter_text: "카테고리를 선택하여 용어집을 좁히세요:"

# channel to icon/fa or image mapping
# NOTE: glossary_tags names must match the "tags" under each glossary entry exactly (filter/checkbox logic). Do not translate.
glossary_tags:
  - name: Segment or CSV membership
  - name: Custom attribute
  - name: Custom events
  - name: Sessions
  - name: Retargeting
  - name: Channel subscription behavior
  - name: Purchase behavior
  - name: eCommerce
  - name: Demographic attributes
  - name: App
  - name: Uninstall
  - name: Devices
  - name: Location
  - name: Cohort membership
  - name: Install attribution
  - name: Intelligence and predictive
  - name: Social activity
  - name: Other Filters
  - name: Advertising use cases
  - name: User Attributes

glossaries:
  - name: Segment Membership
    description: 세그먼트, 캠페인 등 필터가 사용되는 모든 곳에서 세그먼트 멤버십을 기준으로 필터링하고 하나의 캠페인 내에서 여러 개의 서로 다른 세그먼트를 타겟팅할 수 있습니다. <br><br>이 필터를 이미 사용 중인 세그먼트는 다른 세그먼트에 추가로 포함하거나 중첩할 수 없습니다. 이렇게 하면 세그먼트 A가 세그먼트 B를 포함하고, 세그먼트 B가 다시 세그먼트 A를 포함하려는 순환이 발생할 수 있기 때문입니다. 이런 상황이 발생하면 세그먼트가 계속 자기 자신을 참조하게 되어 실제로 누가 해당 세그먼트에 속하는지 계산할 수 없게 됩니다. 또한 이렇게 세그먼트를 중첩하면 복잡성이 증가하고 속도가 느려질 수 있습니다. 대신 동일한 필터를 사용하여 포함하려는 세그먼트를 다시 만드세요.
    tags:
      - Segment or CSV membership
  - name: Braze Segment Extensions
    description: Braze 대시보드에서 세그먼트 확장을 생성한 후, 해당 확장을 세그먼트에 포함하거나 제외하도록 선택할 수 있습니다.
    tags:
      - Segment or CSV membership
  - name: Updated/Imported from CSV
    description: CSV 업로드에 포함되었는지 여부에 따라 사용자를 세분화합니다.
    tags:
      - Segment or CSV membership
  - name: Custom Attributes
    description: "사용자가 커스텀으로 기록된 속성 값과 일치하는지 여부를 결정합니다. <br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Custom attribute
  - name: Created At
    description: 사용자 프로필이 생성된 시점을 기준으로 사용자를 세분화합니다. 사용자가 CSV 또는 API를 통해 추가된 경우 이 필터는 추가된 날짜를 반영합니다. 사용자가 CSV 또는 API로 추가되지 않았고 SDK에서 첫 번째 세션이 추적된 경우 이 필터는 해당 첫 번째 세션의 날짜를 반영합니다.
    tags:
      - Other Filters
  - name: Created From
    description: "사용자 프로필이 생성된 위치를 기준으로 사용자를 세분화합니다.<br><br>지원되는 값은 다음과 같습니다:<br>- SDK (<code>sdk</code>): Braze SDK를 통해 생성된 사용자 프로필.<br>- REST API (<code>rest</code>): Braze REST API를 통해 생성된 사용자 프로필.<br>- 푸시 토큰 가져오기 (<code>pti</code>): 푸시 토큰 가져오기를 통해 생성된 사용자 프로필.<br>- CSV (<code>csv</code>): CSV 가져오기를 통해 생성된 사용자 프로필.<br>- 데모 (<code>demo</code>): 데모 데이터를 통해 생성된 사용자 프로필.<br>- SMS (<code>sms</code>): SMS를 통해 생성된 사용자 프로필.<br>- Shopify (<code>shopify</code>): Shopify를 통해 생성된 사용자 프로필.<br>- WhatsApp (<code>whats_app</code>): WhatsApp을 통해 생성된 사용자 프로필.<br>- 제공업체 이벤트 (<code>provider_event</code>): 제공업체 이벤트를 통해 생성된 사용자 프로필.<br>- 제공업체 동기화 (<code>provider_sync</code>): 제공업체 동기화를 통해 생성된 사용자 프로필.<br>- 랜딩 페이지 (<code>landing_page</code>): 랜딩 페이지를 통해 생성된 사용자 프로필."
    tags:
      - Other Filters
  - name: Nested Custom Attributes
    description: "커스텀 속성의 등록정보입니다.<br><br>중첩된 시간 커스텀 속성을 필터링할 때 \"연중일\" 또는 \"시간\"을 기준으로 필터링하도록 선택할 수 있습니다. \"연중일\"은 비교를 위해 월과 일만 확인합니다. \"시간\"은 연도를 포함한 전체 타임스탬프를 비교합니다."
    tags:
      - Custom attribute
  - name: Day of Recurring Event
    description: "이 필터는 데이터 유형이 \"날짜\"인 커스텀 속성의 월과 일을 확인하지만 연도는 확인하지 않습니다. 이 필터는 연례 이벤트에 유용합니다.<br><br>시간대&#58;<br>이 필터는 메시지가 로컬 시간 예약 옵션을 사용하여 전송되는 한 사용자가 있는 모든 시간대에 맞게 조정됩니다. 그렇지 않으면 회사의 시간대를 사용합니다."
    tags:
      - Custom attribute
  - name: Custom Event
    description: "사용자가 특별히 기록된 이벤트를 수행했는지 여부를 확인합니다.<br><br> 예시:<br>activity_name 이벤트 속성정보로 완료된 활동.<br><br>시간대:<br>UTC - 캘린더 일 = 1 캘린더 일은 24-48시간의 사용자 기록을 봅니다"
    tags:
      - Custom events
  - name: First Did Custom Event
    description: "사용자가 특별히 기록된 이벤트를 수행한 가장 이른 시간을 확인합니다. (24시간 기간) <br><br>예시:<br> 처음 유기한 장바구니가 1일 미만 전<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Custom events
  - name: Last Did Custom Event
    description: "사용자가 특별히 기록된 이벤트를 수행한 가장 최근 시간을 확인합니다. 이 필터는 0.25시간과 같은 소수점을 지원합니다. (24시간 기간) <br><br>예시:<br> 마지막으로 유기한 장바구니가 1일 미만 전<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Custom events
  - name: X Custom Event In Y Days
    description: "사용자가 1~30일 사이의 마지막 지정된 캘린더 일수 동안 0~50회 사이에 특별히 기록된 이벤트를 수행했는지 여부를 확인합니다. (캘린더 일 = 1 캘린더 일은 24-48시간의 사용자 기록을 봅니다)<br> <a href=\"/docs/x-in-y-behavior/\"> 여기에서 X-in-Y 동작에 대해 자세히 알아보세요.</a> <br><br>예시:<br>지난 1 캘린더 일 동안 유기한 장바구니가 정확히 0번<br><br>시간대:<br>UTC - 모든 시간대를 고려하기 위해 1 캘린더 일은 세그먼트가 평가되는 시간에 따라 24-48시간의 사용자 기록을 보고, 2 캘린더 일은 48-72시간의 사용자 기록을 봅니다."
    tags:
      - Custom events
  - name: X Custom Event Property In Y Days
    description: "사용자가 1~30일 사이의 마지막 지정된 캘린더 일수 동안 0~50회 사이에 특정 등록정보와 관련하여 특별히 기록된 이벤트를 수행했는지 여부를 결정합니다. (캘린더 일 = 1 캘린더 일은 24-48시간의 사용자 기록을 봅니다)<br><a href=\"/docs/x-in-y-behavior/\">여기에서 X-in-Y 동작에 대해 자세히 알아보세요.</a> <br><br>예시:<br> 지난 1 캘린더 일 동안 \"event_name\" 등록정보를 가진 즐겨찾기에 정확히 0번 추가됨<br><br>시간대:<br>UTC - 모든 시간대를 고려하기 위해 1 캘린더 일은 세그먼트가 평가되는 시간에 따라 24-48시간의 사용자 기록을 보고, 2 캘린더 일은 48-72시간의 사용자 기록을 봅니다."
    tags:
      - Custom events
  - name: Email Address
    description: "테스트를 위해 개별 이메일 주소로 캠페인 수신자를 지정할 수 있습니다. 또한 필터 내에서 '이메일 주소가 비어 있지 않음' 지정자를 사용하여 모든 사용자(탈퇴한 사용자 포함)에게 트랜잭션 이메일을 전송하는 데 사용할 수 있으므로 옵트인 상태와 관계없이 이메일 전달을 극대화할 수 있습니다. <br><br>이 필터는 사용자 프로필에 이메일 주소가 있는지 여부만 확인하지만, <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-available\">이메일 사용 가능</a> 필터는 추가 기준을 확인합니다."
    tags:
      - Other Filters
  - name: External User ID
    description: 테스트를 위해 개별 사용자 ID로 캠페인 수신자를 지정할 수 있습니다.
    tags:
      - Other Filters
  - name: "Random Bucket #"
    description: 무작위로 할당된 숫자(0~9999 포함)로 사용자를 세분화합니다. A/B 및 다변량 테스트를 위해 균일하게 분산된 진정한 무작위 사용자 세그먼트를 생성할 수 있습니다.
    tags:
      - Other Filters
  - name: Session Count
    description: 워크스페이스 내 앱에서 사용자가 가진 세션 수에 따라 사용자를 세분화합니다.
    tags:
      - Sessions
  - name: Session Count For App
    description: 특정 지정된 앱에서 가진 세션 수에 따라 사용자를 세분화합니다.
    tags:
      - Sessions
  - name: X Sessions In Last Y Days
    description: "사용자가 지난 1일에서 30일 사이의 지정된 캘린더 일수 동안 앱에서 가진 세션 수(0에서 50 사이)를 기준으로 사용자를 세분화합니다. <br> <a href=\"/docs/x-in-y-behavior/\">여기에서 X-in-Y 동작에 대해 자세히 알아보세요.</a>"
    tags:
      - Sessions
  - name: First Used App
    description: "사용자가 앱을 연 가장 이른 기록 시간을 기준으로 사용자를 세분화합니다. <em>이것은 Braze SDK가 통합된 버전의 앱을 사용하여 가진 첫 번째 세션을 캡처합니다.</em> (24시간 기간)<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Sessions
  - name: First Used Specific App
    description: "사용자가 워크스페이스 내에서 앱을 연 가장 이른 기록 시간을 기준으로 사용자를 세분화합니다. (24시간 기간)<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Sessions
  - name: Last Used App
    description: "사용자가 앱을 연 가장 최근 시간을 기준으로 사용자를 세분화합니다. (24시간 기간)<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Sessions
  - name: Last Used Specific App
    description: "사용자가 특정 지정된 앱을 가장 최근에 연 시간을 기준으로 사용자를 세분화합니다. (24시간 기간)<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Sessions
  - name: Median Session Duration
    description: 앱 내 세션의 중간 길이를 기준으로 사용자를 세분화합니다.
    tags:
      - Sessions
  - name: Received Message from Campaign
    description: "특정 캠페인을 수신했는지 여부에 따라 사용자를 세분화합니다. 이 필터는 메시지를 명시적으로 전송받은 사용자만 캡처하며, 중복 메시지를 받은 동일한 이메일 또는 전화번호를 가진 다른 사용자는 포함되지 않습니다. 중복 사용자를 캡처하려면 <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">캠페인 또는 태그가 있는 캔버스에서 받은 메시지</a>를 사용하세요.<br><br> 콘텐츠 카드, 배너 및 인앱 메시지의 경우, 카드 또는 인앱 메시지가 전송되는 시점이 아니라 사용자가 노출을 기록하는 시점입니다.<br><br>푸시 및 웹훅의 경우 사용자에게 메시지가 전송되는 시점입니다.<br><br> WhatsApp의 경우, 메시지가 사용자의 기기로 전달되는 시점이 아니라 마지막 메시지 API 요청이 WhatsApp으로 전송되는 시점입니다. <br><br>이메일의 경우, 이메일 요청이 이메일 서비스 제공업체에 전송되는 시점입니다(실제로 전달되는지 여부와 관계없이).<br><br>SMS의 경우 마지막 메시지가 SMS 제공업체에 전달된 시점입니다. 메시지가 사용자의 기기에 전달되었다는 보장은 없습니다."
    tags:
      - Retargeting
  - name: Received Campaign Variant
    description: "사용자가 수신한 다변량 캠페인의 배리언트를 기준으로 사용자를 세분화합니다. 이 필터는 메시지를 명시적으로 전송받은 사용자만 캡처하며, 중복 메시지를 받은 동일한 이메일 또는 전화번호를 가진 다른 사용자는 포함되지 않습니다. 중복 사용자를 캡처하려면 <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">캠페인 또는 태그가 있는 캔버스에서 받은 메시지</a>를 사용하세요.<br><br> 콘텐츠 카드, 배너 및 인앱 메시지의 경우, 카드 또는 인앱 메시지가 전송되는 시점이 아니라 사용자가 노출을 기록하는 시점입니다.<br><br>푸시 및 웹훅의 경우 사용자에게 메시지가 전송되는 시점입니다.<br><br> WhatsApp의 경우, 메시지가 사용자의 기기로 전달되는 시점이 아니라 마지막 메시지 API 요청이 WhatsApp으로 전송되는 시점입니다. <br><br>이메일의 경우, 이메일 요청이 이메일 서비스 제공업체에 전송되는 시점입니다(실제로 전달되는지 여부와 관계없이).<br><br>SMS의 경우 마지막 메시지가 SMS 제공업체에 전달된 시점입니다. 메시지가 사용자의 기기에 전달되었다는 보장은 없습니다."
    tags:
      - Retargeting
  - name: Received Message from Canvas Step
    description: "특정 캔버스 구성요소를 받았는지 여부에 따라 사용자를 세분화합니다. 이 필터는 메시지를 명시적으로 전송받은 사용자만 캡처하며, 중복 메시지를 받은 동일한 이메일 또는 전화번호를 가진 다른 사용자는 포함되지 않습니다. 중복 사용자를 캡처하려면 <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">캠페인 또는 태그가 있는 캔버스에서 받은 메시지</a>를 사용하세요.<br><br> 콘텐츠 카드 및 인앱 메시지의 경우, 카드 또는 인앱 메시지가 전송되는 시점이 아니라 사용자가 노출을 기록하는 시점입니다.<br><br>푸시 및 웹훅의 경우 사용자에게 메시지가 전송되는 시점입니다.<br><br> WhatsApp의 경우, 메시지가 사용자의 기기로 전달되는 시점이 아니라 마지막 메시지 API 요청이 WhatsApp으로 전송되는 시점입니다. <br><br>이메일의 경우, 이메일 요청이 이메일 서비스 제공업체에 전송되는 시점입니다(실제로 전달되는지 여부와 관계없이).<br><br>SMS의 경우 마지막 메시지가 SMS 제공업체에 전달된 시점입니다. 메시지가 사용자의 기기에 전달되었다는 보장은 없습니다."
    tags:
      - Retargeting
  - name: Last Received Message from Specific Canvas Step
    description: "특정 캔버스 구성요소를 받은 시점을 기준으로 사용자를 세분화합니다. 이 필터는 메시지를 명시적으로 전송받은 사용자만 캡처하며, 중복 메시지를 받은 동일한 이메일 또는 전화번호를 가진 다른 사용자는 포함되지 않습니다. 중복 사용자를 캡처하려면 <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">캠페인 또는 태그가 있는 캔버스에서 받은 메시지</a>를 사용하세요. 이 필터는 사용자가 다른 캔버스 구성요소를 받은 시기는 고려하지 않습니다."
    tags:
      - Retargeting
  - name: Last Received Message from Specific Campaign
    description: "특정 캠페인을 수신한 시점을 기준으로 사용자를 세분화합니다. 이 필터는 메시지를 명시적으로 전송받은 사용자만 캡처하며, 중복 메시지를 받은 동일한 이메일 또는 전화번호를 가진 다른 사용자는 포함되지 않습니다. 중복 사용자를 캡처하려면 <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">캠페인 또는 태그가 있는 캔버스에서 받은 메시지</a>를 사용하세요. 이 필터는 사용자가 다른 캠페인을 수신한 시기는 고려하지 않습니다."
    tags:
      - Retargeting
  - name: Received Message from Campaign or Canvas with Tag
    description: "특정 캠페인 또는 특정 태그가 포함된 캔버스를 수신했는지 여부에 따라 사용자를 세분화합니다. \"캠페인에서 받은 메시지\" 및 \"캔버스 단계에서 받은 메시지\"와 달리, 이 필터는 중복 메시지를 받은 동일한 이메일 또는 전화번호를 가진 모든 사용자를 캡처합니다.<br><br> 콘텐츠 카드, 배너(캠페인만 해당) 및 인앱 메시지의 경우, 카드 또는 인앱 메시지가 전송되는 시점이 아니라 사용자가 노출을 기록하는 시점입니다.<br><br>푸시 및 웹훅의 경우 사용자에게 메시지가 전송되는 시점입니다.<br><br> WhatsApp의 경우, 메시지가 사용자의 기기로 전달되는 시점이 아니라 마지막 메시지 API 요청이 WhatsApp으로 전송되는 시점입니다. <br><br>이메일의 경우, 이메일 요청이 이메일 서비스 제공업체에 전송되는 시점입니다(실제로 전달되는지 여부와 관계없이). 여러 사용자가 동일한 이메일 주소를 공유하는 경우:<br>- 최초 전송 시에는 특정 타겟 사용자의 프로필만 업데이트됩니다. <br>- 이메일이 전달되거나 사용자가 이메일 또는 이메일의 링크를 열면, 해당 이메일 주소를 공유하는 모든 사용자가 메시지를 받은 것으로 나타납니다.<br><br>SMS의 경우 마지막 메시지가 SMS 제공업체에 전달된 시점입니다. 메시지가 사용자의 기기에 전달되었다는 보장은 없습니다."
    tags:
      - Retargeting
  - name: Last Received Message from Campaign or Canvas With Tag
    description: 특정 캠페인이나 특정 태그가 포함된 캔버스를 수신한 시점을 기준으로 사용자를 세분화합니다. 이 필터는 사용자가 다른 캠페인이나 캔버스를 수신한 시기는 고려하지 않습니다. (24시간 기간)
    tags:
      - Retargeting
  - name: Has Never Received a Message from Campaign or Canvas Step
    description: 캠페인 또는 캔버스 구성요소를 수신한 적이 있는지 여부에 따라 사용자를 세분화합니다.
    tags:
      - Retargeting
  - name: Last Received Email
    description: "사용자가 마지막으로 이메일 메시지를 받은 시간을 기준으로 사용자를 세분화합니다. (24시간 기간)<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Retargeting
  - name: Last Received Push
    description: "사용자가 마지막으로 푸시 알림을 수신한 시간을 기준으로 사용자를 세분화합니다. (24시간 기간)<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Retargeting
  - name: Last In App Message Impression
    description: 사용자가 마지막으로 인앱 메시지를 본 시간을 기준으로 사용자를 세분화합니다.
    tags:
      - Retargeting
  - name: Last Received SMS
    description: "마지막 메시지가 SMS 제공업체에 전달된 시간을 기준으로 사용자를 세분화합니다. 메시지가 사용자의 기기에 전달되었다는 보장은 없습니다. (24시간 기간)<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Retargeting
  - name: Last Received Webhook
    description: "Braze가 해당 사용자에 대해 마지막으로 웹훅을 보낸 시간을 기준으로 사용자를 세분화합니다. (24시간 기간)<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Retargeting
  - name: Last Received WhatsApp
    description: "사용자가 마지막으로 WhatsApp 메시지를 받은 시간을 기준으로 사용자를 세분화합니다. 이는 메시지가 사용자의 기기로 전달되는 시점이 아니라 마지막 메시지 API 요청이 WhatsApp으로 전송되는 시점입니다. (24시간 기간)<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Retargeting
  - name: Live Activities Push to Start Registered for App
    description: 특정 앱에 대한 iOS 푸시 알림을 통해 Live Activity를 시작하도록 등록된 사용자를 세분화합니다.
    tags:
      - Devices
  - name: Clicked/Opened Campaign
    description: "특정 캠페인과의 상호작용을 기준으로 필터링합니다. 이메일 메시징의 경우 열기 이벤트에는 기계적 열기와 비기계적 열기가 모두 포함됩니다.<br><br> 이메일의 경우 '모든 이메일 열기(기계적 열기)' 및 '모든 이메일 열기(기타 열기)'로 필터링하는 옵션도 포함되어 있습니다. 탈퇴 링크 및 환경설정 센터 클릭은 이 필터에 포함되지 않습니다. 여러 사용자가 동일한 이메일 주소를 공유하는 경우:<br>- 이메일을 열거나 클릭하면 같은 이메일 주소를 가진 다른 모든 사용자도 프로필이 업데이트됩니다. <br>- 메시지가 전송된 후 열기 또는 클릭 전에 원래 사용자가 이메일 주소를 변경하면 원래 사용자 대신 해당 이메일 주소를 가진 나머지 모든 사용자에게 열기 또는 클릭이 적용됩니다.<br><br>SMS의 경우 상호작용은 다음과 같이 정의됩니다:<br>- 사용자가 마지막으로 특정 키워드 카테고리와 일치하는 답장 SMS를 보냈습니다. 이는 이 전화번호를 사용하는 모든 사용자가 가장 최근에 받은 캠페인에 기여됩니다. 캠페인은 지난 4시간 이내에 수신된 것이어야 합니다.<br>- 사용자가 특정 캠페인에서 사용자 클릭 추적이 켜져 있는 SMS 메시지의 단축 링크를 마지막으로 선택했습니다."
    tags:
      - Retargeting
  - name: Clicked/Opened Campaign or Canvas With Tag
    description: "특정 태그가 있는 특정 캠페인과의 상호작용을 기준으로 필터링합니다. 이메일 메시징의 경우 열기 이벤트에는 기계적 열기와 비기계적 열기가 모두 포함됩니다.<br><br> 이메일의 경우 '모든 이메일 열기(기계적 열기)' 및 '모든 이메일 열기(기타 열기)'를 기준으로 필터링하는 옵션이 포함됩니다. 여러 사용자가 동일한 이메일 주소를 공유하는 경우:<br>- 이메일을 열거나 클릭하면 같은 이메일 주소를 가진 다른 모든 사용자도 프로필이 업데이트됩니다. <br>- 메시지가 전송된 후 열기 또는 클릭 전에 원래 사용자가 이메일 주소를 변경하면 원래 사용자 대신 해당 이메일 주소를 가진 나머지 모든 사용자에게 열기 또는 클릭이 적용됩니다.<br><br>SMS의 경우 상호작용은 다음과 같이 정의됩니다:<br>- 사용자가 마지막으로 특정 키워드 카테고리와 일치하는 답장 SMS를 보냈습니다. 이는 이 전화번호를 사용하는 모든 사용자가 가장 최근에 받은 캠페인에 기여됩니다. 캠페인은 지난 4시간 이내에 수신된 것이어야 합니다.<br>- 사용자가 태그가 있는 특정 캠페인 또는 캔버스 단계에서 사용자 클릭 추적이 켜져 있는 SMS 메시지의 단축 링크를 마지막으로 선택한 경우."
    tags:
      - Retargeting
  - name: Clicked/Opened Step
    description: "특정 캔버스 구성요소와의 상호작용을 기준으로 필터링합니다. 이메일 메시징의 경우 열기 이벤트에는 기계적 열기와 비기계적 열기가 모두 포함됩니다.<br><br>이메일의 경우 '모든 이메일 열기(기계적 열기)' 및 '모든 이메일 열기(기타 열기)'를 기준으로 필터링하는 옵션이 포함됩니다.<br><br>SMS의 경우 상호작용은 다음과 같이 정의됩니다:<br>- 사용자가 마지막으로 특정 키워드 카테고리와 일치하는 답장 SMS를 보냈습니다. 이는 이 전화번호를 사용하는 모든 사용자가 가장 최근에 받은 캠페인에 기여됩니다. 캠페인은 지난 4시간 이내에 수신된 것이어야 합니다. <br>- 사용자가 지정된 캔버스 단계에서 사용자 클릭 추적이 켜져 있는 SMS 메시지의 단축 링크를 마지막으로 선택했습니다."
    tags:
      - Retargeting
  - name: Clicked Alias in Campaign
    description: "특정 캠페인에서 특정 별칭을 클릭했는지 여부에 따라 사용자를 필터링합니다. 이는 이메일 메시지에만 적용됩니다. <br><br> 여러 사용자가 동일한 이메일 주소를 공유하는 경우:<br>- 이메일을 열거나 클릭하면 같은 이메일 주소를 가진 다른 모든 사용자도 프로필이 업데이트됩니다. <br>- 메시지가 전송된 후 열기 또는 클릭 전에 원래 사용자가 이메일 주소를 변경하면 원래 사용자 대신 해당 이메일 주소를 가진 나머지 모든 사용자에게 열기 또는 클릭이 적용됩니다."
    tags:
      - Retargeting
  - name: Clicked Alias in Canvas Step
    description: "특정 캔버스에서 특정 별칭을 클릭했는지 여부에 따라 사용자를 필터링합니다. 이는 이메일 메시지에만 적용됩니다. <br><br> 여러 사용자가 동일한 이메일 주소를 공유하는 경우:<br>- 이메일을 열거나 클릭하면 같은 이메일 주소를 가진 다른 모든 사용자도 프로필이 업데이트됩니다. <br>- 메시지가 전송된 후 열기 또는 클릭 전에 원래 사용자가 이메일 주소를 변경하면 원래 사용자 대신 해당 이메일 주소를 가진 나머지 모든 사용자에게 열기 또는 클릭이 적용됩니다."
    tags:
      - Retargeting
  - name: Clicked Alias in Any Campaign or Canvas Step
    description: "캠페인 또는 캔버스에서 특정 별칭을 클릭했는지 여부에 따라 사용자를 필터링합니다. 이는 이메일 메시지에만 적용됩니다. <br><br> 여러 사용자가 동일한 이메일 주소를 공유하는 경우:<br>- 이메일을 열거나 클릭하면 같은 이메일 주소를 가진 다른 모든 사용자도 프로필이 업데이트됩니다. <br>- 메시지가 전송된 후 열기 또는 클릭 전에 원래 사용자가 이메일 주소를 변경하면 원래 사용자 대신 해당 이메일 주소를 가진 나머지 모든 사용자에게 열기 또는 클릭이 적용됩니다."
    tags:
      - Retargeting
  - name: Hard Bounced
    description: 이메일 주소가 하드바운스되었는지 여부(예: 이메일 주소가 유효하지 않은 경우)에 따라 사용자를 세분화합니다.
    tags:
      - Retargeting
  - name: Soft Bounced
    description: Y일 동안 X번 소프트바운스된 사용자를 세분화합니다. 세그먼트 필터는 30일까지만 조회할 수 있지만 세그먼트 확장을 사용하면 더 오래 조회할 수 있습니다.<br><br>이 필터는 커런츠의 소프트바운스 이벤트와는 다르게 작동합니다. 소프트바운스 세그먼트 필터는 72시간의 재시도 기간 동안 전달에 성공하지 못한 경우 소프트바운스로 계산합니다. 커런츠에서는 재시도에 실패할 때마다 소프트바운스 이벤트로 전송됩니다.
    tags:
      - Retargeting
  - name: Has Marked You As Spam
    description: 사용자가 메시지를 스팸으로 표시했는지 여부에 따라 사용자를 세분화합니다.
    tags:
      - Retargeting
  - name: Invalid Phone Number
    description: 전화번호가 유효하지 않은지 여부에 따라 사용자를 세분화합니다.
    tags:
      - Retargeting
  - name: Last Sent Specific SMS Inbound Keyword Category
    description: 특정 키워드 카테고리 내의 특정 구독 그룹에 마지막으로 SMS를 보낸 시점을 기준으로 사용자를 세분화합니다.
    tags:
      - Retargeting
  - name: Converted From Campaign
    description: 특정 캠페인에서 전환했는지 여부에 따라 사용자를 세분화합니다. 이 필터에는 대조군에 속한 사용자는 포함되지 않습니다.
    tags:
      - Retargeting
  - name: Converted From Canvas
    description: 특정 캔버스에서 전환했는지 여부에 따라 사용자를 세분화합니다. 이 필터에는 대조군에 속한 사용자는 포함되지 않습니다.
    tags:
      - Retargeting
  - name: In Campaign Control Group
    description: 특정 다변량 캠페인의 대조군에 속했는지 여부에 따라 사용자를 세분화합니다.
    tags:
      - Retargeting
  - name: In Canvas Control Group
    description: "특정 캔버스의 대조군에 속했는지 여부에 따라 사용자를 세분화합니다. 이 필터는 캔버스에 진입한 사용자만 평가하므로, 진입하지 않은 사용자는 결과에서 완전히 제외됩니다.<br><br>예를 들어, 캔버스의 대조군에 포함되지 않은 사용자를 필터링하면 캔버스에 진입하고 비대조 배리언트에 할당된 사용자만 반환됩니다. 캔버스에 진입하지 않은 사용자는 포함되지 않습니다. 캔버스 진입 여부에 관계없이 모든 사용자를 포함하려면 <code>Entered Canvas Variation</code> 필터를 대신 사용하세요."
    tags:
      - Retargeting
  - name: Last Enrolled in Any Control Group
    description: "캠페인에서 마지막으로 대조군에 속했던 시간을 기준으로 사용자를 세분화합니다. <br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Retargeting
  - name: Entered Canvas Variation
    description: "특정 캔버스의 변형 경로에 진입했는지 여부에 따라 사용자를 세분화합니다. 이 필터는 모든 사용자를 평가합니다.<br><br>예를 들어, 캔버스 변형 대조군에 진입하지 않은 사용자를 필터링하면 캔버스에 진입했는지 여부에 관계없이 대조군에 포함되지 않은 모든 사용자를 반환합니다."
    tags:
      - Retargeting
  - name: Last Received Any Message
    description: "마지막으로 수신한 메시지를 확인하여 사용자를 세분화합니다. (24시간 기간)<br><br> 콘텐츠 카드, 배너 및 인앱 메시지의 경우, 카드 또는 인앱 메시지가 마지막으로 전송된 시점이 아니라 사용자가 마지막으로 노출을 기록한 시점입니다.<br><br>푸시 및 웹훅의 경우 사용자에게 메시지가 전송된 시점입니다.<br><br> WhatsApp의 경우, 메시지가 사용자의 기기로 전달된 시점이 아니라 마지막 메시지 API 요청이 WhatsApp으로 전송된 시점입니다. <br><br>이메일의 경우, 이메일 요청이 이메일 서비스 제공업체에 전송되는 시점입니다(실제로 전달되는지 여부와 관계없이). 여러 사용자가 동일한 이메일 주소를 공유하는 경우:<br>- 최초 전송 시에는 특정 타겟 사용자의 프로필만 업데이트됩니다. <br>- 이메일이 전달되거나 사용자가 이메일 또는 이메일의 링크를 열면, 해당 이메일 주소를 공유하는 모든 사용자가 메시지를 받은 것으로 나타납니다.<br><br>SMS의 경우 마지막 메시지가 SMS 제공업체에 전달된 시점입니다. 메시지가 사용자의 기기에 전달되었다는 보장은 없습니다.<br><br>예시:<br>마지막으로 받은 메시지 1일 전 미만 = 24시간 전 미만<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Retargeting
  - name: Last Engaged With Message
    description: "사용자가 메시징 채널(배너, 콘텐츠 카드, 이메일, 인앱, SMS, 푸시, WhatsApp) 중 하나를 마지막으로 클릭하거나 연 시간을 기준으로 사용자를 세분화합니다. 이메일 메시징의 경우 열기 이벤트에는 기계적 열기와 비기계적 열기가 모두 포함됩니다. (24시간 기간)<br><br>이메일의 경우, 이메일 요청이 이메일 서비스 제공업체에 전송되는 시점입니다(실제로 전달되는지 여부와 관계없이). 여기에는 '모든 이메일 열기(기계적 열기)' 및 '모든 이메일 열기(기타 열기)'로 필터링하는 옵션도 포함되어 있습니다. 여러 사용자가 동일한 이메일 주소를 공유하는 경우:<br>- 최초 전송 시에는 특정 타겟 사용자의 프로필만 업데이트됩니다. <br>- 이메일이 전달되거나 사용자가 이메일 또는 이메일의 링크를 열면, 해당 이메일 주소를 공유하는 모든 사용자가 메시지를 받은 것으로 나타납니다.<br><br>SMS의 경우, 사용자 클릭 추적이 켜져 있는 메시지에서 사용자가 마지막으로 단축 링크를 선택한 시점을 의미합니다.<br><br>시간대:<br>회사 표준 시간대"
    tags:
      - Retargeting
  - name: Clicked card
    description: "특정 콘텐츠 카드를 클릭했는지 여부에 따라 사용자를 세분화합니다. 이 필터는 \"클릭/열린 캠페인\", \"클릭/열린 캠페인 또는 태그가 있는 캔버스\", \"클릭/열린 단계\"의 하위 필터로 사용할 수 있습니다."
    tags:
      - Retargeting
  - name: Feature Flags
    description: "현재 특정 <a href=\"/docs/developer_guide/feature_flags/\">기능 플래그</a>가 활성화된 사용자 세그먼트입니다."
    tags:
      - Retargeting
  - name: Subscription Group
    description: 이메일, SMS/MMS 또는 WhatsApp의 구독 그룹별로 사용자를 세분화합니다. 아카이브된 그룹은 표시되지 않으며 사용할 수 없습니다.
    tags:
      - Channel subscription behavior
  - name: Email Available
    description: "유효한 이메일 주소가 있는지 여부와 이메일에 가입되었거나 옵트인되었는지 여부에 따라 사용자를 세분화합니다. 이 필터는 사용자가 이메일을 탈퇴했는지, Braze가 하드바운스를 받았는지, 이메일이 스팸으로 표시되었는지 등 세 가지 기준을 확인합니다. 이 기준 중 하나라도 충족되거나 사용자의 이메일이 존재하지 않으면 사용자는 포함되지 않습니다.<br><br>이메일 사용 가능 여부가 <code>false</code>인 사용자는 캠페인 오디언스에서 제외되며 이메일을 받지 않습니다. 전송 설정이 모든 사용자(탈퇴한 사용자 포함)에게 전송하도록 구성되어 있더라도 마찬가지입니다.<br><br>옵트인 상태가 중요한 이메일의 경우 <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-address\">이메일 주소</a> 대신 이메일 사용 가능 여부를 사용하세요. 추가 기준은 이메일을 받을 자격이 있는 사용자를 타겟팅하는 데 도움이 됩니다."
    tags:
      - Channel subscription behavior
  - name: Email Opt In Date
    description: 사용자가 이메일 수신에 옵트인한 날짜에 따라 사용자를 세분화합니다.
    tags:
      - Channel subscription behavior
  - name: Email Subscription Status
    description: 이메일 구독 상태에 따라 사용자를 세분화합니다.
    tags:
      - Channel subscription behavior
  - name: Email Unsubscribed Date
    description: 사용자가 향후 이메일 수신을 탈퇴한 날짜를 기준으로 사용자를 세분화합니다.
    tags:
      - Channel subscription behavior
  - name: Foreground Push Enabled
    description: "임시 푸시 권한이 있거나 포그라운드 푸시를 사용하도록 설정된 사용자를 세분화합니다. 구체적으로 이 수에는 다음이 포함됩니다:<br>1. 푸시 권한이 잠정적으로 승인된 iOS 사용자. <br>2. 모든 앱에 대해 포그라운드 푸시가 활성화되어 있고 푸시 구독 상태가 탈퇴되지 않은 사용자입니다. 이러한 사용자의 경우 이 카운트에는 포그라운드 푸시만 포함됩니다.<br><br>포그라운드 푸시 활성화에는 탈퇴한 사용자가 포함되지 않습니다. <br><br>이 필터로 세분화한 후, <em>도달 가능한 사용자</em>라는 하단 패널에서 Android, iOS 및 웹에서 해당 세그먼트에 포함된 사용자의 세부 정보를 볼 수 있습니다."
    tags:
      - Channel subscription behavior
  - name: Foreground Push Enabled for App
    description: 사용자가 기기에서 앱에 푸시를 사용하도록 설정했는지 여부에 따라 세분화합니다. 앱에 대해 포그라운드 푸시가 활성화된 사용자입니다. 이는 푸시 구독 상태를 고려하지 않습니다. 이 수에는 포그라운드 및 백그라운드 푸시 토큰을 잠정적으로 승인한 사용자가 포함됩니다.
    tags:
      - Channel subscription behavior
  - name: Background or Foreground Push Enabled
    description: 푸시 토큰이 있고 탈퇴하지 않은 사용자를 기준으로 세분화합니다. 모든 앱에 대해 백그라운드 또는 포그라운드 푸시가 활성화된 사용자입니다.
    tags:
      - Channel subscription behavior
  - name: Push Opt In Date
    description: 사용자가 푸시를 옵트인한 날짜를 기준으로 사용자를 세분화합니다.
    tags:
      - Channel subscription behavior
  - name: Push Subscription Status
    description: "푸시 <a href=\"/docs/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-subscription-state\">구독 상태</a>에 따라 사용자를 세분화합니다."
    tags:
      - Channel subscription behavior
  - name: Push Unsubscribed Date
    description: 사용자가 향후 푸시 알림을 탈퇴한 날짜를 기준으로 사용자를 세분화합니다.
    tags:
      - Channel subscription behavior
  - name: Purchased Product
    description: 앱에서 구매한 제품별로 사용자를 세분화합니다.
    tags:
      - Purchase behavior
  - name: Total Number of Purchases
    description: 앱에서 구매한 횟수에 따라 사용자를 세분화합니다.
    tags:
      - Purchase behavior
  - name: X Product Purchased In Y Days
    description: 특정 제품을 구매한 횟수별로 사용자를 필터링합니다.
    tags:
      - Purchase behavior
  - name: X Purchases in Last Y Days
    description: "사용자가 1~30일 사이의 지정된 마지막 캘린더 일수 동안 구매한 횟수(0~50회)로 사용자를 세분화합니다. <br> <a href=\"/docs/x-in-y-behavior/\">여기에서 X-in-Y 동작에 대해 자세히 알아보세요.</a>"
    tags:
      - Purchase behavior
  - name: X Purchase Property In Y Days
    description: "1일에서 30일 사이의 지정된 마지막 캘린더 일수 동안 특정 구매 등록정보와 관련하여 구매가 이루어진 횟수에 따라 사용자를 세분화합니다. <br> <a href=\"/docs/x-in-y-behavior/\">여기에서 X-in-Y 동작에 대해 자세히 알아보세요.</a>"
    tags:
      - Purchase behavior
  - name: First Made Purchase
    description: 사용자가 앱에서 가장 먼저 구매한 시점을 기준으로 사용자를 세분화합니다.
    tags:
      - Purchase behavior
  - name: First Purchase For App
    description: 사용자가 앱에서 구매한 가장 이른 시점을 기준으로 사용자를 세분화합니다.
    tags:
      - Purchase behavior
  - name: Last Made Purchase
    description: 마지막으로 구매한 시간별로 사용자를 필터링합니다.
    tags:
      - Purchase behavior
  - name: Last Purchased Product
    description: 특정 제품을 마지막으로 구매한 시점을 기준으로 사용자를 필터링합니다.
    tags:
      - Purchase behavior
  - name: Money Spent
    description: 앱에서 지출한 금액에 따라 사용자를 세분화합니다.
    tags:
      - Purchase behavior
  - name: X Money Spent in Y Days
    description: "사용자가 1~30일 사이의 지정된 마지막 캘린더 일수 동안 앱에서 지출한 금액에 따라 사용자를 세분화합니다. 이 금액은 마지막 50건의 구매 합계만 포함됩니다. <br> <a href=\"/docs/x-in-y-behavior/\">여기에서 X-in-Y 동작에 대해 자세히 알아보세요.</a>"
    tags:
      - Purchase behavior
  - name: Last order placed (last 730 days)
    description: "사용자가 마지막으로 주문한 시점에 따라 세분화하며, 이는 주문 완료에 대한 <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">eCommerce 추천 이벤트</a>에 기반합니다(eCommerce 이벤트를 추적하지 않는 워크스페이스는 이 필터에 대한 데이터가 없습니다). 사용자는 이 필터에 대해 하루에 한 번 평가되며, 최대 조회 기간은 지난 2년입니다.<br><br>이 필터는 베타 버전입니다. 이 필터 사용에 관심이 있으시면 Braze 계정 매니저에게 문의하세요."
    tags:
      - eCommerce
  - name: Total orders count (last 730 days)
    description: "사용자의 지난 2년 동안의 총 주문 수에 따라 사용자를 세분화하며, 이는 주문 완료에 대한 <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">eCommerce 추천 이벤트</a>에 기반합니다(eCommerce 이벤트를 추적하지 않는 워크스페이스는 이 필터에 대한 데이터가 없습니다). 이 수치는 취소된 주문을 제외하며, 취소된 주문은 주문 취소에 대한 <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">eCommerce 추천 이벤트</a>를 사용하여 추적해야 합니다. 사용자는 이 필터에 대해 하루에 한 번 평가됩니다.<br><br>이 필터는 베타 버전입니다. 이 필터 사용에 관심이 있으시면 Braze 계정 매니저에게 문의하세요."
    tags:
      - eCommerce
  - name: Total orders count
    description: "사용자의 전체 생애주기 동안의 총 주문 수에 따라 사용자를 세분화하며, 이는 주문 완료에 대한 <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">eCommerce 추천 이벤트</a>에 기반합니다(eCommerce 이벤트를 추적하지 않는 워크스페이스는 이 필터에 대한 데이터가 없습니다). 이 수치는 취소된 주문을 제외하며, 취소된 주문은 주문 취소에 대한 <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">eCommerce 추천 이벤트</a>를 사용하여 추적해야 합니다. 사용자는 이 필터에 대해 실시간으로 평가됩니다.<br><br>이 필터는 베타 버전입니다. 이 필터 사용에 관심이 있으시면 Braze 계정 매니저에게 문의하세요."
    tags:
      - eCommerce
  - name: Total canceled orders count (last 730 days)
    description: "사용자가 지난 2년 동안 취소한 주문의 총 수에 따라 사용자를 세분화하며, 이는 주문 완료에 대한 <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">eCommerce 추천 이벤트</a>에 기반합니다(eCommerce 이벤트를 추적하지 않는 워크스페이스는 이 필터에 대한 데이터가 없습니다). 사용자는 이 필터에 대해 하루에 한 번 평가됩니다.<br><br>이 필터는 베타 버전입니다. 이 필터 사용에 관심이 있으시면 Braze 계정 매니저에게 문의하세요."
    tags:
      - eCommerce
  - name: Customer lifetime value (last 730 days)
    description: "사용자가 브랜드와의 구매 이력에서 생성할 것으로 예상되는 총 매출에 따라 사용자를 세분화합니다. 계산은 지난 730일을 고려하며 평균 주문 가치(AOV)에 총 주문 수를 곱한 후 사용자의 활성 구매 기간(첫 주문과 가장 최근 주문 사이의 기간)을 반영합니다. 이 필터는 <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">eCommerce 추천 이벤트</a>에서 추적된 데이터를 사용합니다(eCommerce 이벤트를 추적하지 않는 워크스페이스는 이 필터에 대한 데이터가 없습니다). 사용자는 이 필터에 대해 하루에 한 번 평가됩니다.<br><br>이 필터는 베타 버전입니다. 이 필터 사용에 관심이 있으시면 Braze 계정 매니저에게 문의하세요."
    tags:
      - eCommerce
  - name: Total refund value (last 730 days)
    description: "사용자가 지난 2년 동안 받은 환불의 가치를 기준으로 사용자를 세분화하며, 이는 주문 환불에 대한 <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">eCommerce 추천 이벤트</a>에 기반합니다(eCommerce 이벤트를 추적하지 않는 워크스페이스는 이 필터에 대한 데이터가 없습니다). 사용자는 이 필터에 대해 하루에 한 번 평가됩니다.<br><br>이 필터는 베타 버전입니다. 이 필터 사용에 관심이 있으시면 Braze 계정 매니저에게 문의하세요."
    tags:
      - eCommerce
  - name: Total refund value
    description: "사용자의 전체 생애주기 동안 부여된 환불의 총 가치를 기준으로 사용자를 세분화하며, 이는 주문 환불에 대한 <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">eCommerce 추천 이벤트</a>에 기반합니다(eCommerce 이벤트를 추적하지 않는 워크스페이스는 이 필터에 대한 데이터가 없습니다). 사용자는 이 필터에 대해 실시간으로 평가됩니다.<br><br>이 필터는 베타 버전입니다. 이 필터 사용에 관심이 있으시면 Braze 계정 매니저에게 문의하세요."
    tags:
      - eCommerce
  - name: Total revenue (last 730 days)
    description: "사용자의 지난 2년 동안의 주문에서 발생한 총 매출을 기준으로 사용자를 세분화하며, 주문 완료 eCommerce 이벤트와 관련된 매출에서 주문 환불에 대한 <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">eCommerce 추천 이벤트</a>와 관련된 매출을 빼서 계산합니다(eCommerce 이벤트를 추적하지 않는 워크스페이스는 이 필터에 대한 데이터가 없습니다). 사용자는 이 필터에 대해 하루에 한 번 평가됩니다.<br><br>이 필터는 베타 버전입니다. 이 필터 사용에 관심이 있으시면 Braze 계정 매니저에게 문의하세요."
    tags:
      - eCommerce
  - name: Total revenue
    description: "사용자의 전체 생애주기 동안의 주문에서 발생한 총 매출을 기준으로 사용자를 세분화하며, 주문 완료 eCommerce 이벤트와 관련된 매출에서 주문 환불에 대한 <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">eCommerce 추천 이벤트</a>와 관련된 매출을 빼서 계산합니다(eCommerce 이벤트를 추적하지 않는 워크스페이스는 이 필터에 대한 데이터가 없습니다). 사용자는 이 필터에 대해 실시간으로 평가됩니다.<br><br>이 필터는 베타 버전입니다. 이 필터 사용에 관심이 있으시면 Braze 계정 매니저에게 문의하세요."
    tags:
      - eCommerce
  - name: Average order value (last 730 days)
    description: "사용자의 지난 2년 동안의 주문의 평균(산술 평균) 가치를 기준으로 사용자를 세분화하며, 이는 주문 완료에 대한 <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">eCommerce 추천 이벤트</a>에 기반합니다(eCommerce 이벤트를 추적하지 않는 워크스페이스는 이 필터에 대한 데이터가 없습니다). 사용자는 이 필터에 대해 하루에 한 번 평가됩니다.<br><br>이 필터는 베타 버전입니다. 이 필터 사용에 관심이 있으시면 Braze 계정 매니저에게 문의하세요."
    tags:
      - eCommerce
  - name: Country
    description: 마지막으로 표시된 국가 위치에 따라 사용자를 세분화합니다.
    tags:
      - Demographic attributes
  - name: City
    description: 마지막으로 표시된 도시 위치를 기준으로 사용자를 세분화합니다.
    tags:
      - Demographic attributes
  - name: Language
    description: 선호하는 언어별로 사용자를 세분화합니다.
    tags:
      - Demographic attributes
  - name: Age
    description: 앱 내에서 사용자가 지정한 연령에 따라 사용자를 세분화합니다.
    tags:
      - Demographic attributes
  - name: Birthday
    description: "앱 내에서 사용자가 지정한 생일에 따라 사용자를 세분화합니다. <br> 2월 29일에 생일이 있는 사용자는 3월 1일을 포함하는 세그먼트에 포함됩니다.<br><br>12월 또는 1월 생일을 타겟팅하려면 타겟팅하려는 연도의 12개월 범위 내에서만 필터 로직을 삽입하세요. 즉, 전년도 12월로 되돌아가거나 다음 해 1월로 앞당기는 로직을 삽입하지 마세요. 예를 들어 12월 생일을 타겟팅하려면 \"12월 31일\", \"12월 31일 이전\" 또는 \"11월 30일 이후\"로 필터링할 수 있습니다."
    tags:
      - Demographic attributes
  - name: Gender
    description: 앱 내에서 사용자가 지정한 성별에 따라 사용자를 세분화합니다.
    tags:
      - Demographic attributes
  - name: Unformatted Phone Number
    description: 형식화되지 않은 전화번호를 기준으로 사용자를 세분화합니다. 괄호, 대시 또는 기타 기호를 포함하지 않습니다.
    tags:
      - Demographic attributes
  - name: First Name
    description: 앱 내에서 사용자가 지정한 이름(성이 아닌 이름)에 따라 사용자를 세분화합니다.
    tags:
      - Demographic attributes
  - name: Last Name
    description: 앱 내에서 사용자가 지정한 성에 따라 사용자를 세분화합니다.
    tags:
      - Demographic attributes
  - name: Has App
    description: 사용자가 앱을 설치한 적이 있는지 여부에 따라 세분화합니다. 현재 앱이 설치된 사용자와 과거에 앱을 삭제한 사용자가 포함됩니다. 일반적으로 이 필터에 포함되려면 사용자가 앱을 열어야 합니다(세션 시작). 그러나 사용자를 Braze로 가져와 앱과 수동으로 연결한 경우와 같이 몇 가지 예외가 있습니다.
    tags:
      - App
  - name: Most Recent App Version Name
    description: "사용자 앱의 최근 이름을 기준으로 세분화합니다.<br><br>\"미만\" 또는 \"이하\"를 사용할 때, 주 앱 버전이 존재하지 않으면 이 필터는 `true`를 반환합니다. 사용자가 앱 버전보다 오래되었기 때문입니다. 이는 사용자의 마지막 주 앱 버전이 존재하지 않으면 자동으로 필터에 일치함을 의미합니다."
    tags:
      - App
  - name: Most Recent App Version Number
    description: "사용자 앱의 최근 앱 버전 번호로 세분화합니다.<br><br>\"미만\" 또는 \"이하\"를 사용할 때, 주 앱 버전이 존재하지 않으면 이 필터는 `true`를 반환합니다. 사용자가 앱 버전보다 오래되었기 때문입니다. 이는 사용자의 마지막 주 앱 버전이 존재하지 않으면 자동으로 필터에 일치함을 의미합니다.<br><br>현재 앱 버전이 채워지는 데 시간이 걸릴 수 있습니다. 사용자 프로필의 앱 버전은 SDK에 의해 정보가 캡처될 때 업데이트되며, 이는 사용자가 앱을 열 때에 의존합니다. 사용자가 앱을 열지 않으면 현재 버전이 업데이트되지 않습니다. 이 필터는 소급 적용되지 않습니다. 현재 및 미래 버전에는 \"초과\" 또는 \"같음\"을 사용하는 것이 좋지만, 과거 버전 필터를 사용하면 예기치 않은 동작이 발생할 수 있습니다."
    tags:
      - App
  - name: Uninstalled
    description: 앱을 삭제했고 다시 설치하지 않은 사용자를 기준으로 세분화합니다.
    tags:
      - Uninstall
  - name: Device Carrier
    description: 기기 통신사별로 사용자를 세분화합니다.
    tags:
      - Devices
  - name: Device Count
    description: 앱을 사용한 기기 수에 따라 사용자를 세분화합니다.
    tags:
      - Devices
  - name: Device Model
    description: 휴대폰 모델 버전별로 사용자를 세분화합니다.
    tags:
      - Devices
  - name: Device OS
    description: "지정된 운영체제를 사용하는 기기를 하나 이상 보유한 사용자를 세분화합니다. 운영체제 범위에 따라 사용자를 세분화하려면 <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#device-os-version-number\">기기 OS 버전 번호</a> 필터를 사용하세요."
    tags:
      - Devices
  - name: Device OS Version Number
    description: 지정된 범위 내의 운영체제 버전을 가진 하나 이상의 기기를 보유한 사용자를 세분화합니다. 예를 들어, iOS 운영체제 버전이 26.0 이상인 사용자를 타겟팅할 수 있습니다.
    tags:
      - Devices
  - name: Most Recent Device Locale
    description: "가장 최근에 사용한 기기의 <a href=\"/docs/user_guide/engagement_tools/campaigns/ideas_and_strategies/localizing_a_campaign/\">로캘 정보</a>를 기준으로 사용자를 세분화합니다."
    tags:
      - Devices
  - name: Most Recent Watch Model
    description: 가장 최근 스마트워치 모델별로 사용자를 세분화합니다.
    tags:
      - Devices
  - name: Provisionally Authorized on iOS
    description: 특정 앱에 대해 iOS 12에서 잠정적으로 승인된 사용자를 찾을 수 있습니다.
    tags:
      - Devices
  - name: Web Browser
    description: 웹사이트에 액세스할 때 사용하는 웹 브라우저를 기준으로 사용자를 세분화합니다.
    tags:
      - Devices
  - name: Device IDFA
    description: 테스트를 위해 IDFA별로 캠페인 수신자를 지정할 수 있습니다.
    tags:
      - Advertising use cases
  - name: Device IDFV
    description: 테스트를 위해 IDFV별로 캠페인 수신자를 지정할 수 있습니다.
    tags:
      - Advertising use cases
  - name: Device Google Ad ID
    description: Google 광고 ID를 기준으로 사용자를 세분화합니다.
    tags:
      - Advertising use cases
  - name: Device Roku Ad ID
    description: Roku 광고 ID를 기준으로 사용자를 세분화합니다.
    tags:
      - Advertising use cases
  - name: Device Windows Ad ID
    description: Windows 광고 ID를 기준으로 사용자를 세분화합니다.
    tags:
      - Advertising use cases
  - name: Ad Tracking Enabled
    description: 사용자가 광고 추적에 옵트인했는지 여부에 따라 필터링할 수 있습니다. 광고 추적은 Apple이 모든 iOS 기기에 할당하는 IDFA 또는 "광고주 식별자"와 관련이 있으며, SDK로 설정할 수 있습니다. 이 식별자를 통해 광고주는 사용자를 추적하고 타겟팅 광고를 게재할 수 있습니다.
    tags:
      - Advertising use cases
  - name: Most Recent Location
    description: 마지막으로 앱을 사용한 기록된 위치를 기준으로 사용자를 세분화합니다.
    tags:
      - Location
  - name: Location Available
    description: "사용자의 위치 보고 여부에 따라 사용자를 세분화합니다. 이 필터를 사용하려면 앱에 <a href=\"/docs/search/?query=location%20tracking\">위치 추적 기능이 통합</a>되어 있어야 합니다."
    tags:
      - Location
  - name: Amplitude Cohorts
    description: Amplitude를 사용하는 고객은 Amplitude에서 코호트를 선택하고 가져와서 세그먼트를 보완할 수 있습니다.
    tags:
      - Cohort membership
  - name: Census Cohorts
    description: Census를 사용하는 고객은 Census에서 코호트를 선택하고 가져와서 세그먼트를 보완할 수 있습니다.
    tags:
      - Cohort membership
  - name: Heap Cohorts
    description: Heap을 사용하는 고객은 Heap에서 코호트를 선택하고 가져와서 세그먼트를 보완할 수 있습니다.
    tags:
      - Cohort membership
  - name: Hightouch Cohorts
    description: Hightouch를 사용하는 고객은 Hightouch에서 코호트를 선택하고 가져와서 세그먼트를 보완할 수 있습니다.
    tags:
      - Cohort membership
  - name: Kubit Cohorts
    description: Kubit을 사용하는 고객은 Kubit에서 코호트를 선택하고 가져와서 세그먼트를 보완할 수 있습니다.
    tags:
      - Cohort membership
  - name: Mixpanel Cohorts
    description: Mixpanel을 사용하는 고객은 Mixpanel에서 코호트를 선택하고 가져와서 세그먼트를 보완할 수 있습니다.
    tags:
      - Cohort membership
  - name: Segment Cohorts
    description: Segment를 사용하는 고객은 Segment에서 코호트를 선택하고 가져와서 세그먼트를 보완할 수 있습니다.
    tags:
      - Cohort membership
  - name: Tinyclues Cohorts
    description: Tinyclues를 사용하는 고객은 Tinyclues에서 코호트를 선택하고 가져와서 세그먼트를 보완할 수 있습니다.
    tags:
      - Cohort membership
  - name: Install Attribution Ad
    description: 설치 경로가 된 광고에 따라 사용자를 세분화합니다.
    tags:
      - User Attributes
  - name: Install Attribution Adgroup
    description: 설치 경로가 된 광고 그룹을 기준으로 사용자를 세분화합니다.
    tags:
      - Install attribution
  - name: Install Attribution Campaign
    description: 설치 경로가 된 광고 캠페인별로 사용자를 세분화합니다.
    tags:
      - Install attribution
  - name: Install Attribution Source
    description: 설치 경로가 된 소스를 기준으로 사용자를 세분화합니다.
    tags:
      - Install attribution
  - name: Churn Risk Category
    description: 특정 예측에 따라 고객이탈 위험 카테고리별로 사용자를 세분화합니다.
    tags:
      - Intelligence and predictive
  - name: Churn Risk Score
    description: 특정 예측에 따라 고객이탈 위험 점수별로 사용자를 세분화합니다.
    tags:
      - Intelligence and predictive
  - name: Event Likelihood Category
    description: 특정 예측에 따라 이벤트 수행 가능성별로 사용자를 세분화합니다.
    tags:
      - Intelligence and predictive
  - name: Event Likelihood Score
    description: 특정 예측에 따라 이벤트 수행 가능성 점수별로 사용자를 세분화합니다.
    tags:
      - Intelligence and predictive
  - name: Intelligent Channel
    description: 지난 3개월 동안 가장 활발하게 활동한 채널별로 사용자를 세분화합니다.
    tags:
      - Intelligence and predictive
  - name: Message Open Likelihood
    description: "지정된 채널에서 <a href=\"/docs/user_guide/brazeai/intelligence/intelligent_channel/#individual-channels\">메시지를 열 가능성</a>에 따라 0~100% 척도로 사용자를 필터링합니다. 채널의 가능성을 측정할 수 있는 충분한 데이터가 없는 사용자는 \"비어 있음\"을 사용하여 선택할 수 있습니다.<br><br>이메일의 경우, 기계적 열기는 가능성 계산에서 제외됩니다."
    tags:
      - Intelligence and predictive
  - name: Number of Facebook Friends Using App
    description: 같은 앱을 사용하는 Facebook 친구 수에 따라 사용자를 세분화합니다.
    tags:
      - Social activity
  - name: Connected Facebook
    description: 앱이 Facebook에 연결되었는지 여부에 따라 사용자를 세분화합니다.
    tags:
      - Social activity
  - name: Connected Twitter
    description: 앱이 X(구 Twitter)에 연결되었는지 여부에 따라 사용자를 세분화합니다.
    tags:
      - Social activity
  - name: Number of Twitter Followers
    description: 사용자가 보유한 X(구 Twitter) 팔로워 수에 따라 사용자를 세분화합니다.
    tags:
      - Social activity
  - name: Phone Number
    description: "E.164 형식의 전화번호 필드를 기준으로 사용자를 세분화합니다.<br><br> 전화번호가 Braze에 전송되면, Braze는 SMS 및 WhatsApp 채널을 통해 전송하는 데 사용되는 <a href=\"/docs/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers\">e.164 형식</a>으로 강제 변환하려고 시도합니다. 전화번호의 형식이 올바르지 않으면 강제 변환 프로세스가 실패하여 사용자 프로필에 형식화되지 않은 전화번호가 있지만 발신 전화번호는 없는 결과가 발생할 수 있습니다. 이 세그먼트 필터는 e.164 형식의 전화번호(사용 가능한 경우)로 사용자를 반환합니다.<br><br>활용 사례:<br> - 이 필터를 사용하면 SMS 또는 WhatsApp 메시지를 보낼 때 가장 정확한 타겟 오디언스 규모를 파악할 수 있습니다.  <br>- 이 필터와 함께 정규표현식(정규식)을 사용하여 특정 국가 코드가 있는 전화번호로 세분화합니다. <br>- 이 필터를 사용하여 e.164 강제 변환 프로세스에 실패한 전화번호로 사용자를 세분화합니다."
    tags:
      - Other Filters
---