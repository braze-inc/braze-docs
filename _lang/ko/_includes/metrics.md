{% if include.metric == "AMP Clicks" %}
<i>AMP 클릭</i> 수는 이메일의 HTML, 일반 텍스트 및 AMP HTML 버전을 합산한 총 클릭 수입니다.
{% endif %}

{% if include.metric == "AMP Opens" %}
<i>AMP 열람</i>은 AMP HTML 이메일 및 AMP HTML 버전의 이메일에서 열람한 총 횟수입니다.
{% endif %}

{% if include.metric == "Audience" %}
<i>오디언스</i>는 특정 메시지를 수신한 사용자의 비율입니다. 이 숫자는 Braze에서 받았습니다.
{% endif %}

{% if include.metric == "Bounces" %}
<i>반송</i>은 의도한 수신자에게 성공적으로 전달되지 못한 총 메시지 수입니다.
{% endif %}

{% if include.metric == "Estimated Real Opens" %}
<i>예상 실제 열람</i>은 기계 열람이 존재하지 않을 경우 얼마나 많은 고유 열람이 있을지에 대한 추정치이며, 독점적인 Braze 통계 모델의 결과입니다.
{% endif %}

{% if include.metric == "Help" %}
<i>도움말</i>은 사용자가 <a href="https://braze.com/docs/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">도움말 키워드</a>를 사용하여 메시지에 답장하고 도움말 자동 응답이 발송된 경우입니다.
{% endif %}

{% if include.metric == "Hard Bounce" %}
<i>하드바운스</i>는 영구적인 전달 오류로 인해 이메일이 수신자에게 전달되지 못하는 경우를 말합니다. 도메인 이름이 존재하지 않거나 수신자를 알 수 없기 때문에 하드 바운스가 발생할 수 있습니다.
{% endif %}

{% if include.metric == "Soft Bounce" %}
<i>소프트 반송</i>은 수신자의 이메일 주소가 유효함에도 불구하고 일시적인 전송 오류로 인해 이메일이 수신자에게 전달되지 못하는 경우를 말합니다. 소프트바운스는 수신자의 받은편지함이 꽉 찼거나 서버가 다운되었거나 메시지가 수신자의 받은 편지함에 비해 너무 커서 발생할 수 있습니다.
{% endif %}

{% if include.metric == "Deferral" %}
<i>연기란</i> 이메일이 즉시 전달되지 않았지만, 특정 캠페인에 대한 시도가 중지되기 전에 전달 성공 가능성을 극대화하기 위해 일시적인 전달 실패 후 최대 72시간 동안 이메일을 재시도하는 것을 말합니다.
{% endif %}

{% if include.metric == "Body Click" %}
푸시 스토리 알림은 알림을 클릭하면 <i>본문 클릭을</i> 기록합니다. 메시지가 확장되거나 실행 버튼 클릭에 대해 기록되지 않습니다.
{% endif %}

{% if include.metric == "Body Clicks" %}
<i>본문 클릭</i>은 사용자가 버튼(버튼 1, 버튼 2)이 없고 기존 편집기로 작성된 메시지를 클릭하는 경우와 HTML 편집기 또는 끌어서 놓기 편집기를 사용하여 작성된 메시지를 클릭하는 경우에 발생합니다. <code>brazeBridge.logClick()</code> 이는 인수가 없습니다.
{% endif %}

{% if include.metric == "Button 1 Clicks" %}
<i>버튼 1 클릭</i> 수는 메시지의 버튼 1을 클릭한 총 횟수입니다.
{% endif %}

{% if include.metric == "Button 2 Clicks" %}
<i>버튼 2 클릭</i> 수는 메시지의 버튼 2를 클릭한 총 횟수입니다.
{% endif %}

{% if include.metric == "Choices Submitted" %}
<i>제출된 선택</i> 항목은 사용자가 <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>간편 설문조사</a>의 설문조사 문제 페이지에서 제출 버튼을 클릭할 때 선택한 총 선택 항목 수입니다.
{% endif %}

{% if include.metric == "Click-to-Open Rate" %}
<i>클릭 후 열람율</i>은 단일 사용자 또는 컴퓨터가 한 번 이상 열어본 전달된 이메일의 비율이며 <a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>보고서 빌더</a>에서만 사용할 수 있습니다.
{% endif %}

{% if include.metric == "Close Message" %}
<i>메시지 닫기</i> 횟수는 메시지의 닫기 버튼을 클릭한 총 횟수입니다. 이는 기존 에디터가 아닌 드래그 앤 드롭 에디터에서 만든 인앱 메시지에만 존재합니다.
{% endif %}

{% if include.metric == "Confirmed Deliveries" %}
<i>전달 확인</i>은 이동통신사가 메시지가 대상 전화 번호로 전달되었음을 확인한 경우입니다.
{% endif %}

{% if include.metric == "Confidence" %}
<i>신뢰도</i>는 메시지의 특정 배리언트가 대조군보다 성능이 우수하다는 신뢰도의 백분율입니다.
{% endif %}

{% if include.metric == "Confirmation Page Button" %}
<i>확인 페이지 버튼</i>은 <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>간단한 설문조사</a>의 확인 페이지에서 클릭한 클릭 유도 문안 버튼의 총 클릭 수입니다.
{% endif %}

{% if include.metric == "Confirmation Page Dismissals" %}
<i>확인 페이지 삭제</i>는 <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>간단한 설문조사</a>의 확인 페이지에서 닫기(X) 버튼을 클릭한 총 횟수입니다.
{% endif %}

{% if include.metric == "Conversion Rate" %}
<i>전환율</i>은 메시지의 모든 수신자 대비 정의된 이벤트가 발생한 횟수의 백분율입니다. 이 정의된 이벤트는 캠페인을 구축할 때 결정됩니다.
{% endif %}

{% if include.metric == "Conversion Window" %}
<i>전환 기간</i>이란 메시지를 수신한 후 사용자 행동을 추적하여 전환 이벤트에 기여한 기간(일수)입니다. 이 기간 이후에 발생하는 전환은 전환 이벤트로 인해 발생한 것이 아닙니다.
{% endif %}

{% if include.metric == "Conversions (B, C, D)" %}
<i>전환(B, C, D)</i> 은 기본 전환 이벤트 이후에 추가된 추가 전환 이벤트입니다. Braze 캠페인에서 수신한 메시지와 상호작용하거나 메시지를 본 후 정의된 이벤트가 발생한 횟수입니다.
{% endif %}

{% if include.metric == "Total Conversions" %}
<i>총 전환</i> 수는 사용자가 인앱 메시지 캠페인을 본 후 특정 전환 이벤트를 완료한 총 횟수입니다.
{% endif %}

{% if include.metric == "Deliveries" %}
<i>전달</i>은 수신 서버가 수락한 총 메시지 요청 수입니다. 이것은 메시지가 기기에 전달되었다는 것을 의미하지 않으며, 메시지가 서버에 의해 수락되었다는 것만을 의미합니다.
{% endif %}

{% if include.metric == "Deliveries %" %}
<i>전달 %</i>는 이메일 가능 상대방과 성공적으로 주고받은 총 메시지 수(전송)의 백분율입니다.
{% endif %}

{% if include.metric == "Delivery Failures" %}
<i>전송 실패</i>는 대기줄이 넘쳐서 SMS를 보낼 수 없는 경우(긴 코드 또는 짧은 코드가 처리할 수 있는 속도보다 높은 속도로 SMS를 전송하는 경우)를 말합니다.
{% endif %}

{% if include.metric == "Delivery Failures RCS" %}
<i>배달 실패는</i> 대기열이 넘쳐서 RCS를 전송할 수 없는 경우(RCS 인증 발신자가 처리할 수 있는 속도보다 높은 속도로 RCS를 전송하는 경우)입니다.
{% endif %}

{% if include.metric == "Failed Delivery Rate" %}
<i>배달 실패율은</i> 메시지를 보낼 수 없어 실패한 전송의 백분율입니다. 이는 대기열 오버플로, 계정 일시 정지, MMS의 경우 미디어 오류 등 다양한 이유로 발생할 수 있습니다.
{% endif %}

{% if include.metric == "Direct Opens" %}
<i>직접 열기는</i> 알림을 직접 눌러 앱이나 웹사이트를 연 총 사용자 수입니다.
{% endif %}

{% if include.metric == "Emailable" %}
<i>이메일 가능</i> 수는 이메일 주소가 기록되어 있고 명시적으로 옵트인 또는 구독을 신청한 총 사용자 수입니다.
{% endif %}

{% if include.metric == "Errors" %}
<i>오류</i>는 웹훅 이벤트가 반환한 오류의 수(전송 프로세스 중에 증가)입니다.
{% endif %}

{% if include.metric == "Failures" %}
<i>실패</i>는 인터넷 서비스 공급자가 하드바운스를 반환하여 WhatsApp 메시지를 보낼 수 없는 경우입니다. 하드 바운스는 영구적인 전달 가능성 실패를 의미합니다.
{% endif %}

{% if include.metric == "Influenced Opens" %}
<i>영향받은 열람</i>은 푸시 알림이 전송된 후 푸시를 직접 실행하지 않고 앱을 실행한 사용자의 총 수(및 백분율)입니다.
{% endif %}

{% if include.metric == "Lifetime Revenue" %}
<i>생애주기 매출</i>은 <code>PurchaseEvents</code> 지금까지 받은 가격 총 가치(USD)입니다.
{% endif %}

{% if include.metric == "Lifetime Value Per User" %}
<i>사용자당 평생 가치는</i> <i>평생 수익을</i> 총 <i>사용자</i> 수로 나눈 값입니다(홈 페이지에 있음).
{% endif %}

{% if include.metric == "Average Daily Revenue" %}
<i>일일 평균 수익은</i> 해당 일의 캠페인과 캔버스 수익의 합계를 평균한 값입니다.
{% endif %}

{% if include.metric == "Daily Purchases" %}
<i>일일 구매</i>는 총 고유 구매 평균입니다. <code>PurchaseEvents</code> 특정 기간을 따릅니다.
{% endif %}

{% if include.metric == "Daily Revenue Per User" %}
<i>사용자당 일일 매출</i>은 일일 활성 사용자당 평균 일일 매출입니다.
{% endif %}

{% if include.metric == "Machine Opens" %}
<i>기계 열람</i>에는 iOS 15용 Apple의 메일 개인정보 보호(MPP)의 영향을 받는 '열람'의 비율이 포함됩니다. 예를 들어 사용자가 Apple 기기에서 메일 앱을 사용하여 이메일을 열면 <i>컴퓨터가 열림</i>으로 기록됩니다.
{% endif %}

{% if include.metric == "Other Opens" %}
<i>기타 열람</i>에는 <i>기계 열람</i>으로 식별되지 않은 이메일이 포함됩니다. 예를 들어 사용자가 다른 플랫폼(예: 휴대폰의 Gmail 앱, 데스크톱 브라우저의 Gmail)에서 이메일을 열면 <i>기타 열림</i>으로 기록됩니다.
{% endif %}

{% if include.metric == "Opens" %}
<i>열람</i>은 <i>직접 열람</i>과 <i>영향받은 열람</i>을 모두 포함하는 인스턴스로, Braze SDK가 독점 알고리즘을 사용하여 푸시 알림으로 인해 사용자가 앱을 열었다고 판단한 경우입니다.
{% endif %}

{% if include.metric == "Opt-Out" %}
<i>옵트아웃은</i> 사용자가 <a href="https://braze.com/docs/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">옵트아웃 키워드를</a> 사용하여 메시지에 답장을 보낸 후 SMS 또는 RCS 프로그램에서 수신 거부된 경우입니다.
{% endif %}

{% if include.metric == "Pending Retry" %}
<i>보류 중인 재시도</i>는 수신 서버에서 일시적으로 거부되었지만 이메일 서비스 공급자(ESP)가 재전송을 시도한 요청의 수입니다. 이메일 서비스 공급자는 타임아웃 기간에 도달할 때까지 전달을 재시도합니다(일반적으로 72시간 후).
{% endif %}

{% if include.metric == "Primary Conversions (A) or Primary Conversion Event" %}
<i>주요 전환(A)</i> 또는 <i>주요 전환 이벤트</i>는 Braze 캠페인에서 수신한 메시지와 상호 작용하거나 메시지를 본 후 정의된 이벤트가 발생한 횟수입니다. 이 정의된 이벤트는 캠페인을 구축할 때 사용자가 결정합니다.
{% endif %}

{% if include.metric == "Reads" %}
<i>읽기는</i> 사용자가 메시지를 읽은 경우입니다. 사용자의 읽음 확인이 Braze에서 읽음을 추적하려면 "켜짐" 상태여야 합니다.
{% endif %}

{% if include.metric == "Read Rate" %}
<i>읽음률은</i> 읽음으로 이어진 전송의 백분율입니다. 이 기능은 읽음 확인을 켠 사용자에게만 제공됩니다.
{% endif %}

{% if include.metric == "Received" %}
<i>수신</i>은 채널별로 다르게 정의되며 사용자가 메시지를 보거나, 사용자가 정의된 트리거 동작을 수행하거나, 메시지가 메시지 공급자에게 전송될 때일 수 있습니다.
{% endif %}

{% if include.metric == "Rejections" %}
<i>거부란</i> 이동통신사에 의해 SMS 또는 RCS가 거부된 경우를 말합니다. 이것은 여러 가지 이유로 발생할 수 있습니다. 여기에는 통신사 콘텐츠 필터링, 대상 기기의 가용성, 전화번호가 더 이상 서비스되지 않음 등이 포함됩니다.
{% endif %}

{% if include.metric == "Revenue" %}
<i>매출</i>은 설정된 <a href='/docs/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events'>주요 전환 기간</a> 내에 캠페인 수신자로부터 발생한 총 수익(달러)입니다.
{% endif %}

{% if include.metric == "Messages Sent" %}
<i>보낸 메시지</i> 수는 캠페인에서 보낸 총 메시지 수입니다. 예약된 캠페인을 시작한 후, 이 측정기준에는 전송된 모든 메시지가 포함되며, 사용량 제한조치로 인해 아직 전송되지 않은 메시지도 포함됩니다. 이는 메시지가 디바이스에 수신 또는 전달되었음을 의미하는 것이 아니라 메시지가 전송되었다는 의미입니다.
{% endif %}

{% if include.metric == "Sent" %}
<i>전송은</i> 캠페인 또는 캔버스 단계가 시작되거나 트리거되어 Braze에서 SMS 또는 RCS가 전송될 때마다 발생합니다. 오류로 인해 SMS 또는 RCS가 사용자의 디바이스에 도달하지 못했을 수 있습니다.
{% endif %}

{% if include.metric == "Sends" %}
<i>전송</i> 수는 캠페인에서 보낸 총 메시지 수입니다. 예약된 캠페인을 시작한 후, 이 측정기준에는 전송된 모든 메시지가 포함되며, 사용량 제한조치로 인해 아직 전송되지 않은 메시지도 포함됩니다. 이는 메시지가 디바이스에 수신 또는 전달되었음을 의미하는 것이 아니라 메시지가 전송되었다는 의미입니다.
{% endif %}

{% if include.metric == "Sends to Carrier" %}
<i>전송을 캐리어로</i>는 더 이상 사용되지 않지만, 이미 사용 중인 사용자에게는 계속 지원됩니다. 배송업체에서 배송 또는 거부가 확인되지 않은 <i>배송 확인</i>, 배송 <i>거부</i> 및 <i>발송의</i> 합계입니다. 일부 배송업체는 배송 확인을 제공하지 않거나 전송 시 확인을 제공할 수 없기 때문에 배송업체가 배송 확인을 제공하지 않거나 거부한 경우도 포함됩니다.
{% endif %}

{% if include.metric == "Sends to Carrier Rate" %}
<i>이동 통신사로 전송 비율은</i> 전송된 전체 메시지 중 <i>이동 통신사로 전송으로</i> 분류된 메시지의 비율입니다. 일부 배송업체는 배송 확인을 제공하지 않거나 전송 시 확인을 제공할 수 없기 때문에 배송업체가 배송을 제공하지 않거나 확인을 거부하는 경우도 포함됩니다. 이 메트릭은 더 이상 사용되지 않지만 이미 해당 메트릭을 보유한 사용자에게는 계속 지원됩니다.
{% endif %}

{% if include.metric == "Spam" %}
<i>스팸은</i> 수신자가 '스팸'으로 표시한 총 전달된 이메일 수입니다. Braze는 이러한 사용자의 구독 상태를 변경하지 않지만, '수신 거부 포함 모든 사용자에게 보내기'로 구성된 트랜잭션 이메일을 보내지 않는 한 향후 이메일에서 해당 사용자는 자동으로 제외됩니다.
{% endif %}

{% if include.metric == "Survey Page Dismissals" %}
설문조사 <i>페이지</i> 종료 횟수는 <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>간단한 설문조사</a>의 설문조사 문제 페이지에서 닫기(X) 버튼을 클릭한 총 횟수입니다.
{% endif %}

{% if include.metric == "Survey Submissions" %}
설문조사 <i>제출</i>은 <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>간단한 설문조사</a>의 제출 버튼을 클릭한 총 횟수입니다.
{% endif %}

{% if include.metric == "Total Clicks" %}
<i>총 클릭</i> 수는 전달된 메시지의 링크를 클릭한 고유 수신자 수입니다.
{% endif %}

{% if include.metric == "Total Dismissals" %}
<i>총 닫기</i> 횟수는 캠페인에서 콘텐츠 카드가 닫기된 횟수입니다.
{% endif %}

{% if include.metric == "Total Impressions" %}
<i>총 노출</i> 횟수는 이전 상호 작용과 관계없이 메시지가 로드되어 사용자 화면에 표시된 횟수입니다(예: 사용자에게 메시지가 두 번 표시된 경우 두 번 계산됨).
{% endif %}

{% if include.metric == "Total Opens" %}
<i>총 열람</i> 건수는 열람한 총 메시지 수입니다.
{% endif %}

{% if include.metric == "Total Revenue" %}
<i>총 매출</i>은 설정된 주요 전환 기간 내에 캠페인 수신자로부터 발생한 총 매출(달러)입니다.
{% endif %}

{% if include.metric == "Unique Clicks" %}
<i>고유 클릭</i> 수는 메시지 내의 링크를 한 번 이상 클릭한 수신자의 고유한 수이며 <a href='https://braze.com/docs/help/help_articles/data/dispatch_id/'>dispatch_id로</a> 측정됩니다.
{% endif %}

<!-- Pull channels like Banners that don't have a Dispatch ID-->
{% if include.metric == "Unique Clicks No Dispatch ID" %}
<i>고유 클릭</i>는 메시지 내의 링크를 최소한 한 번 클릭한 수신자의 고유한 수입니다.
{% endif %}

{% if include.metric == "Unique Dismissals" %}
<i>고유 해지</i> 횟수는 캠페인에서 콘텐츠 카드를 해지한 고유 수신자 수입니다. 사용자가 캠페인에서 콘텐츠 카드를 여러 번 해제하는 것은 하나의 고유한 해제를 나타냅니다.
{% endif %}

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

{% if include.metric == "Unique Impressions" %}
<i>고유 노출</i> 수는 특정 캠페인에서 메시지를 수신하고 조회한 총 사용자 수입니다.
{% endif %}

{% if include.metric == "Unique Recipients" %}
<i>고유 수신자는</i> 일일 고유 수신자 수 또는 하루에 새 메시지를 받은 사용자의 수입니다. 사용자에 대해 이 횟수가 두 번 이상 증가하려면 사용자가 다른 날에 새 메시지를 수신해야 합니다.
{% endif %}

{% if include.metric == "Unique Opens" %}
<i>고유 열람</i> 건수는 한 명의 사용자가 한 번 이상 열어본 총 전달 메시지 수이며 7일 동안 추적됩니다.
{% endif %}

{% if include.metric == "Unsubscribers or Unsub" %}
<i>수신 거부자</i> 또는 수신 <i>취소</i>는 수신 거부로 이어진 메시지 수입니다. 구독 취소는 사용자가 Braze 구독 취소 링크를 클릭하면 발생합니다.
{% endif %}

{% if include.metric == "Unsubscribes" %}
<i>구독 취소</i>는 Braze에서 제공한 구독 취소 URL을 클릭한 결과 구독 상태가 구독 취소로 변경된 수신자 수입니다.
{% endif %}

{% if include.metric == "Variation" %}
<i>배리언트</i>는 크리에이터가 정의한 대로 다른 캠페인의 배리언트 수입니다.
{% endif %}
