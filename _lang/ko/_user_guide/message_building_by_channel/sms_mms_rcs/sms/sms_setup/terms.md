---
page_order: 1
nav_title: 필수 용어
article_title: 알아두어야 할 SMS 약관
alias: /sms_terms_to_know/

layout: glossary_page
glossary_top_header: "Terms to Know"
glossary_top_text: "SMS–everyone has it and knows what it is. What they don't know is the nuance. Check out the following terms to learn more about SMS ecosystems, technologies, and processes."
page_type: glossary
description: "이 용어집에서는 알아야 할 다양한 SMS 용어를 정의합니다."
channel: SMS 

glossaries:
  - name: SMS(단문 메시지 서비스)
    description: "1980년에 만들어진 메시징 채널로, 가장 오래된 문자 메시지 기술 중 하나입니다. 또한 모든 문자 메시지 채널 중에서 가장 널리 퍼져 있고 사용 빈도가 높은 채널 중 하나입니다. 이 채널은 개인 전화번호를 활용하여 사용자와 고객에게 연락하기 때문에 대부분의 다른 메시징 채널보다 더 직접적으로 사용자에게 다가갈 수 있는 방법입니다. 따라서 SMS에는 다른 메시징 채널에 비해 더 많은 규칙과 규정이 적용됩니다."
  - name: 짧은 코드
    description: "이는 기억하기 쉬운 짧은 5~6자리 숫자로, 발신자가 긴 숫자(초당 한 개의 메시지)보다 더 많은 메시지를 일관된 속도로 보낼 수 있도록 해줍니다.<br><br>짧은 코드 또는 긴 코드가 필요합니다."
  - name: 긴 코드
    description: 이 번호는 발신자가 초당 한 개의 메시지 전송 속도로 더 많은 메시지를 보낼 수 있는 표준 10자리 전화번호(대부분의 국가에서 사용)입니다.<br><br>짧은 코드 또는 긴 코드가 필요합니다.
  - name: 인코딩
    description: 무엇이든 코드화된 형태로 변환하는 작업입니다. SMS 콘텐츠는 GSM-7 또는 UCS-2로 인코딩할 수 있습니다.
  - name: GSM-7 인코딩(모바일 통신을 위한 글로벌 시스템)
    description: "GSM-7은 대부분의 SMS 메시징에서 가장 많이 사용되는 인코딩 표준입니다. 대부분의 그리스어 및 영어 알파벳과 몇 가지 추가 문자를 사용합니다. <a href='https://en.wikipedia.org/wiki/GSM_03.38#GSM_7-bit_default_alphabet_and_extension_table_of_3GPP_TS_23.038_.2F_GSM_03.38' title=\"GSM 7\"></a> 인코딩 및 사용할 수 있는 문자 집합에 대한 자세한 내용은 <a href='https://en.wikipedia.org/wiki/GSM_03.38#GSM_7-bit_default_alphabet_and_extension_table_of_3GPP_TS_23.038_.2F_GSM_03.38' title=\"\">titleGSM 7비트 기본 알파벳 및 확장자 표위키백과에서title</a> 확인할 수 있습니다. 중국어, 한국어, 일본어와 같은 언어는 16비트 UCS-2 문자 인코딩을 사용하여 전송해야 합니다. <br> <br> 이 유형의 인코딩에 대한 세그먼트당 글자 수 제한은 128자로 예상할 수 있습니다."
  - name: UCS-2 인코딩(범용 코드 문자 집합)
    description: "UCS-2 인코딩은 특히 GSM-7을 사용하여 메시지를 인코딩할 수 없거나 언어가 128자 이상을 렌더링해야 하는 경우 대체 인코딩 표준입니다. USC-2는 '문자'가 아닌 <a href='https://en.wikipedia.org/wiki/Code_point'>코드 포인트로</a> 측정하는 것이 더 좋습니다. 어쨌든 이 유형의 인코딩에 대한 세그먼트당 글자 수 제한은 67자로 추정할 수 있습니다."
  - name: SMS 구독 그룹
    description: 구독 그룹은 사용자 또는 고객의 특정 구독 수준을 타겟팅할 수 있는 Braze 도구입니다. SMS용 구독 그룹은 메시지 서비스를 기반으로 내부적으로 구성되며 워크스페이스 간에 공유할 수 없습니다.
  - name: 메시지 세그먼트
    description: "메시지 세그먼트는 단일 SMS 발송으로 전송되는 최대 정의된 문자 수(GSM-7 인코딩의 경우 160자, UCS-2 인코딩의 경우 67자)로 구성된 그룹입니다. GSM-7 인코딩을 사용하여 161자로 된 SMS를 발송하면 전송된 메시지 세그먼트가 두(2) 개인 것을 확인할 수 있습니다. 여러 개의 메시지 세그먼트를 보내면 추가 요금이 부과될 수 있습니다."
  - name: 메시지 서비스
    description: "Braze로 SMS 메시지를 보내는 데 사용되는 긴 코드, 짧은 코드, 영숫자 ID의 모음입니다."
  - name: 키워드
    description: "미리 정의된 SMS 프로그램과 상호 작용하거나 특정 프로그램 또는 코드의 모든 프로그램에 대한 옵트아웃을 요청하기 위해 짧거나 긴 코드에 전송되는 짧은 단어입니다. 예를 들어 <code>STOP</code>. 키워드는 다음과 같아야 합니다. <br> - 영숫자이어야 합니다. <br> - 공백이 없습니다. <br> - 10자 미만이어야 합니다. <br> <br> 특정 키워드와 단축 코드 조합은 한 번에 하나의 활성 프로그램에서만 사용할 수 있습니다. 다른 프로그램에서 이미 사용 중인 키워드를 입력하면 유효성 검사 오류가 표시됩니다. <br> <br> 모든 SMS 콘텐츠 제공업체가 준수해야 하는 두 가지 필수 키워드 카테고리가 있습니다: <code>STOP</code> 그리고 <code>HELP</code>."
  - name: 필수 키워드 도움말
    description: "SMS 캠페인 매니저 플랫폼에서 생성되는 각 프로그램에 대해 이 키워드에 대한 콘텐츠를 제공해야 하며, SMS 트래픽이 송수신되는 국가 또는 지역별로 모범 사례 및 통신사 규정 준수를 충족해야 합니다. 대부분의 경우 이 콘텐츠에는 SMS 프로그램에 대한 간략한 설명과 수신 거부 방법이 포함되어야 합니다."
  - name: 글로벌 스톱 키워드
    description: "변형은 다음과 같습니다. <code>STOP</code>, <code>END</code>, <code>QUIT</code>, <code>UNSUBSCRIBE</code>, <code>CANCEL</code>, <code>STOPALL</code>. 이는 다음으로 참조됩니다 <code>Global-Stop-Keywords</code>. 이러한 키워드 중 하나라도 짧거나 긴 코드에 문자로 입력하면 해당 코드와 연결된 모든 활성 SMS 프로그램에서 해당 휴대폰 번호(발신 휴대폰 번호)가 수신 거부됩니다."
  - name: 베니티 코드
    description: 베니티 쇼트 코드는 브랜드에서 특별히 선택한 5~6자리 전화번호입니다. 베니티 쇼트 코드는 브랜드화되어 소비자가 기억하기 쉽습니다.
  - name: 공유 쇼트 코드
    description: "공유 단축 코드를 사용하면 어떤 기업이나 조직에서 문자 메시지를 보내든 상관없이 모든 문자 메시지가 동일한 5~6개의 전화번호를 통해 소비자의 모바일 디바이스에 도착합니다. 공유 단축 코드는 상대적으로 비용이 저렴하고 즉시 사용할 수 있지만, 비즈니스 전용 단축 코드가 없으며 공유 단축 코드를 사용하는 다른 비즈니스가 올바른 프로토콜을 따라야 한다는 것을 의미합니다." 
  - name: 영숫자 발신자 ID
    description: 영숫자 발신자 ID를 사용하면 지원되는 국가에 단방향 메시지를 보낼 때 영숫자를 사용하여 회사 이름이나 브랜드를 발신자 ID로 설정할 수 있습니다.
  - name: 무료 전화 번호
    description: "수신자 부담 전화 번호 또는 무료 전화 번호는 발신 전화 가입자에게 요금이 부과되지 않고 모든 수신 전화에 대해 요금이 청구되는 전화 번호입니다. 미국과 캐나다의 수신자 부담 무료 전화번호는 SMS를 지원하며, 가입자에게는 수신 및 발신 문자 요금이 부과됩니다.<br><br>수신자 부담 메시징은 고객 지원이나 영업과 같이 발신자와 수신자 모두 문자를 통해 대화하는 개인 대 개인 사용 사례에 가장 적합합니다."
  - name: 단방향 메시징
    description: 단방향 메시징을 사용하면 문자 메시지를 전송하여 고객과 소통할 수 있습니다. 단방향 메시징은 긴 코드와 짧은 코드를 사용할 수 없는 시장에서 영숫자 발신자 ID를 구현하는 경우에 유용합니다. 
  - name: 양방향 메시징
    description: 양방향 메시징을 사용하면 문자 메시지를 주고받으며 대화를 이어갈 수 있습니다. 
---
