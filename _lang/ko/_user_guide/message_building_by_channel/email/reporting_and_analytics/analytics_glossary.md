---
nav_title: 이메일 애널리틱스 용어집
article_title: 이메일 애널리틱스 용어집 
page_order: 0
layout: glossary_page
glossary_top_header: "Email analytics glossary"
glossary_top_text: "These are terms you'll find in the analytics section of your email campaign or Canvas, post-launch. Search for the metrics you need in this glossary. <br><br> This glossary does not necessarily include metrics you might see in Currents or in other downloaded reports outside of your Braze account."

description: "이 용어집에는 출시 후 이메일 캠페인 또는 Canvas의 분석 섹션에서 찾을 수 있는 용어가 포함되어 있습니다. 이 용어집에는 전류 메트릭이 포함되어 있지 않습니다."
channel:
  - email

glossaries:
  - name: "변형"
    description: 크리에이터가 정의한 대로 다른 캠페인의 변형입니다.
    calculation: Count
  - name: "이메일 가능"
    description: 이메일 주소가 기록되어 있고 명시적으로 옵트인 또는 구독을 신청한 사용자.
    calculation: Count
  - name: "오디언스 %"
    description: 특정 이형 상품을 받은 사용자의 비율입니다.
    calculation: Number of Recipients in Variant / Unique Recipients
  - name: "고유 수신자"
    description: 일일 고유 수신자 수. 하루에 특정 메시지를 받은 사용자 수입니다. 이 번호는 Braze에서 받은 번호입니다.
    calculation: Count
  - name: "전송 또는 메시지 보내기"
    description: 이메일 캠페인에서 보낸 총 메시지 수입니다. 이 번호는 Braze에서 받은 번호입니다. 예약된 캠페인을 시작하면 이 지표에는 전송률 제한으로 인해 아직 발송되지 않았는지 여부와 관계없이 발송된 모든 메시지가 포함됩니다.
    calculation: Count
  - name: "전달 수"
    description: 이메일 가능 상대방과 성공적으로 주고받은 총 메시지(보내기) 수입니다.
    calculation: Sends - Bounces
  - name: "배달 %"
    description: 이메일 가능 상대방과 성공적으로 주고받은 총 메시지(보내기) 수입니다.
    calculation: (Sends - Bounces) / (Sends)
  - name: "반송 수"
    description: "이메일을 보낼 수 있는 사용자가 사용했거나 받지 못한 전송 서비스에서 전송에 실패했거나 '반송' 또는 '미수신'으로 지정된 메시지의 총 수입니다. 이는 유효한 푸시 토큰이 없거나 이메일 주소가 잘못되었거나 비활성화되었거나 캠페인이 시작된 후 사용자가 구독을 취소했기 때문에 발생할 수 있습니다. <br><br> <b>하드 바운스</b>: 하드 반송은 수신자의 주소가 유효하지 않아 발신자에게 반송된 이메일 메시지입니다. 도메인 이름이 존재하지 않거나 수신자를 알 수 없기 때문에 하드 바운스가 발생할 수 있습니다. 이메일이 하드 반송된 경우 해당 이메일 주소에 대한 향후 요청이 중지됩니다. <br><br><b>소프트 바운스</b>: 소프트 반송은 수신자의 메일 서버까지 도달했지만 수신자에게 전달되지 않고 반송되는 이메일 메시지를 말합니다. 소프트 반송은 수신자의 받은 편지함이 꽉 찼거나 서버가 다운되었거나 메시지가 수신자의 받은 편지함에 비해 너무 커서 발생할 수 있습니다. 이메일이 소프트 반송된 경우 일반적으로 72시간 이내에 재시도하지만 재시도 시도 횟수는 수신자마다 다릅니다. <br><br> <a href='/docs/user_guide/administrative/app_settings/developer_console/message_activity_log_tab/#message-activity-log-tab'>메시지 활동 로그에서</a> 하드 바운스 및 소프트 바운스를 추적할 수도 있습니다. <br><br><i> SendGrid를 사용하는 고객의 이메일 반송은 하드 반송, 스팸, 유효하지 않은 주소로 전송된 이메일로 구성됩니다. </i>"
    calculation: Count
  - name: "이탈률 또는 이탈률"
    description: "이메일을 보낼 수 있는 사용자가 사용했거나 받지 못한 전송 서비스에서 전송에 실패했거나 '반송' 또는 '미수신'으로 지정된 메시지의 비율입니다. 이는 유효한 푸시 토큰이 없거나 이메일 주소가 잘못되었거나 비활성화되었거나 캠페인이 시작된 후 사용자가 구독을 취소했기 때문에 발생할 수 있습니다. <br> <i> SendGrid를 사용하는 고객의 이메일 반송은 하드 반송, 스팸(`spam_report_drops`), 유효하지 않은 주소로 전송된 이메일(`invalid_emails`)로 구성됩니다. </i>"
    calculation: Bounces / Sends
  - name: "스팸"
    description: "\"스팸\"으로 표시된 총 전달된 이메일 수입니다. Braze는 이메일을 스팸으로 표시한 사용자의 구독을 자동으로 취소하며, 해당 사용자는 향후 이메일의 타겟이 되지 않습니다."
    calculation: (Marked as Spam) / (Sends)
  - name: "스팸 % 또는 스팸 비율"
    description: "전달된 이메일 중 \"스팸\"으로 표시되거나 기타 방식으로 지정된 이메일의 비율입니다. Braze는 이메일을 스팸으로 표시한 사용자의 구독을 자동으로 취소하며, 해당 사용자는 향후 이메일의 타겟이 되지 않습니다."
    calculation: (Marked as Spam) / (Sends)
  - name: "고유 열람"
    description: 단일 사용자 또는 컴퓨터가 한 번 이상 열어본 배달된 이메일의 총 개수입니다. 이메일의 경우 7일 동안 추적됩니다.
    calculation: (Unique Opens) / (Deliveries)
  - name: "고유 오픈 % 또는 고유 오픈율"
    description: 한 명의 사용자가 한 번 이상 열어본 배달된 이메일의 비율입니다. 이메일의 경우 7일 동안 추적됩니다.
    calculation: (Unique Opens) / (Deliveries)
  - name: "고유 클릭 수"
    description: "메시지 내에서 한 번 이상 클릭한 수신자의 고유한 수입니다. 이는 이메일의 경우 7일 동안 추적되며 <a href='/docs/help/help_articles/data/dispatch_id/'>dispatch_id로</a> 측정됩니다."
    calculation: Count
  - name: "고유 클릭 수 % 또는 클릭률"
    description: 메시지 내에서 한 번 이상 클릭한 수신자의 고유한 수입니다. 이메일의 경우 7일 동안 추적됩니다.
    calculation: Unique Clicks / Deliveries
  - name: "구독 취소 또는 구독 취소"
    description: 수신 거부로 이어진 메시지 수입니다. 구독 취소는 사용자가 Braze 구독 취소 링크를 클릭하면 발생합니다.
    calculation: Count
  - name: "구독 취소자 % 또는 구독 취소율"
    description: 수신 거부로 이어진 메시지 전달 건수의 백분율입니다. 구독 취소는 사용자가 Braze 구독 취소 링크를 클릭하면 발생합니다.
    calculation: Unsubscribes / Deliveries
  - name: "매출"
    description: "설정된 <a href='/docs/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#primary-conversion-event'>기본 전환 기간</a> 내에 캠페인 수신자로부터 발생한 총 수익(달러)입니다."
    calculation: Count
  - name: "기본 전환(A) 또는 기본 전환 이벤트"
    description: Braze 캠페인에서 수신한 메시지와 상호작용하거나 메시지를 본 후 정의된 이벤트가 발생한 횟수입니다. 이 정의된 이벤트는 캠페인을 구축할 때 마케터가 결정합니다.
    calculation: Count
  - name: "기본 전환(A) 또는 기본 전환 이벤트"
    description: Braze 캠페인에서 수신한 메시지와 상호 작용하거나 메시지를 본 후 정의된 이벤트가 발생한 횟수의 백분율입니다. 이 정의된 이벤트는 캠페인을 구축할 때 마케터가 결정합니다.
    calculation: "Primary Conversions / Unique Recipients"
  - name: "신뢰도"
    description: 특정 변형 메시지가 대조 그룹보다 성능이 우수하다는 신뢰도의 백분율입니다.
  - name: "기계 열람"
    description: "iOS 15용 Apple의 메일 개인정보 보호(MPP)의 영향을 받는 '열기'의 비율을 포함합니다. 예를 들어 사용자가 Apple 기기에서 메일 앱을 사용하여 이메일을 열면 <i>컴퓨터가 열림으로</i> 기록됩니다. 이 지표는 SendGrid의 경우 2021년 11월 11일부터, SparkPost의 경우 2021년 12월 2일부터 추적됩니다."
    calculation: Count
  - name: "기타 열람 수"
    description: "<i>컴퓨터에서 열림으로</i> 확인되지 않은 이메일을 포함합니다. 예를 들어 사용자가 다른 플랫폼(예: 휴대폰의 Gmail 앱, 데스크톱 브라우저의 Gmail)에서 이메일을 열면 <i>기타 열림으로</i> 기록됩니다. <i>컴퓨터 열기</i> 횟수가 기록되기 전에 사용자가 이메일을 열 수도 있습니다(예: <i>기타 열기</i> 횟수에 대한 열기 횟수). 사용자가 Apple Mail이 아닌 받은 편지함에서 컴퓨터 열기 이벤트가 발생한 후 이메일을 한 번 이상 여는 경우, 사용자가 이메일을 여는 횟수는 <i>기타 열기</i> 횟수에 대해 계산되고 <i>고유 열기</i> 횟수에 대해서는 한 번만 계산됩니다."
    calculation: Count
  - name: "열람률 클릭"
    description: 한 번 이상 클릭한 고유한 이메일 중 열린 이메일의 비율입니다.
    calculation: Unique Clicks / Unique Opens

---
