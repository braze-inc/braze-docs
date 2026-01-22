---
page_order: 1
nav_title: 알아야 할 용어
article_title: 알아야 할 SMS 용어
alias: /sms_terms_to_know/

layout: glossary_page
glossary_top_header: "Terms to Know"
glossary_top_text: "SMS–everyone has it and knows what it is. What they don't know is the nuance. Check out the following terms to learn more about SMS ecosystems, technologies, and processes."
page_type: glossary
description: "이 용어집은 알아야 할 다양한 SMS 용어를 정의합니다."
channel: SMS 

glossaries:
  - name: SMS (단문 메시지 서비스)
    description: "1980년에 만들어진 메시징 채널로, 가장 오래된 문자 기술 중 하나입니다. 또한 모든 문자 채널 중에서 가장 널리 퍼져 있고 자주 사용되는 기술 중 하나입니다. 이 채널은 개인 전화번호를 사용하여 사용자와 고객에게 도달하는 보다 직접적인 방법입니다. 따라서 SMS는 다른 메시징 채널보다 더 많은 규칙과 규제가 있습니다."
  - name: 단축 코드
    description: 이는 발신자가 긴 번호(초당 하나의 메시지)보다 더 일관된 속도로 더 많은 메시지를 보낼 수 있게 해주는 짧고 기억하기 쉬운 5-6자리 시퀀스입니다.<br><br>짧은 코드 또는 긴 코드 중 하나가 필요합니다.
  - name: 긴 코드
    description: 이는 발신자가 초당 하나의 메시지 속도로 더 많은 메시지를 보낼 수 있게 해주는 표준 10자리 전화번호(대부분의 국가에서)입니다.<br><br>짧은 코드 또는 긴 코드 중 하나가 필요합니다.
  - name: 인코딩
    description: 무언가를 코드 형태로 변환하는 것입니다. SMS 콘텐츠는 GSM-7 또는 UCS-2로 인코딩될 수 있습니다.
  - name: GSM-7 인코딩 (모바일 통신을 위한 글로벌 시스템)
    description: "GSM-7은 대부분의 SMS 메시징에서 가장 많이 사용되는 인코딩 표준입니다. 그리스어와 영어 알파벳의 대부분과 일부 추가 문자를 사용합니다. GSM-7 인코딩 및 사용할 수 있는 문자 집합에 대해 더 알고 싶다면 <a href='https://en.wikipedia.org/wiki/GSM_03.38#GSM_7-bit_default_alphabet_and_extension_table_of_3GPP_TS_23.038_.2F_GSM_03.38' title=\"GSM 7비트 기본 알파벳 및 확장 표\">위키백과</a>에서 확인할 수 있습니다. 중국어, 한국어 또는 일본어와 같은 언어는 16비트 UCS-2 문자 인코딩을 사용하여 전송해야 합니다. <br> <br> 이 유형의 인코딩에 대한 세그먼트당 문자 제한은 128자로 추정할 수 있습니다."
  - name: UCS-2 인코딩 (유니버설 코드 문자 집합)
    description: "UCS-2 인코딩은 GSM-7을 사용하여 인코딩할 수 없거나 언어가 128자 이상으로 렌더링되어야 할 때 특히 사용되는 대체 인코딩 표준입니다. USC-2는 \"문자\" 대신 <a href='https://en.wikipedia.org/wiki/Code_point'>코드 포인트</a>로 측정하는 것이 더 좋습니다. 어쨌든 이 유형의 인코딩에 대한 세그먼트당 문자 제한은 67자로 추정할 수 있습니다."
  - name: SMS용 구독 그룹
    description: 구독 그룹은 특정 사용자 또는 고객의 구독 수준을 타겟팅할 수 있는 Braze 도구입니다. SMS용 구독 그룹은 메시지 서비스에 따라 내부적으로 구성되며 작업 공간 간에 공유할 수 없습니다.
  - name: 메시지 세그먼트
    description: "메시지 세그먼트는 단일 SMS 발송으로 전송될 최대 정의된 문자 수(160자는 GSM-7 인코딩, 67자는 UCS-2 인코딩)로 그룹화된 것입니다. GSM-7 인코딩을 사용하여 161자를 포함한 SMS를 발송하면 두 개(2)의 메시지 세그먼트가 전송된 것을 확인할 수 있습니다. 여러 메시지 세그먼트를 전송하면 추가 요금이 발생할 수 있습니다."
  - name: 메시지 서비스
    description: "Braze를 사용하여 SMS 메시지를 전송하는 데 사용되는 긴 코드, 짧은 코드 및 영숫자 ID의 모음입니다."
  - name: 키워드
    description: "사전 정의된 SMS 프로그램과 상호 작용하거나 특정 프로그램 또는 코드의 모든 프로그램에서 OPT-OUT 요청을 위해 짧은 코드 또는 긴 코드로 전송되는 짧은 단어입니다. 예를 들어, <code>STOP</code>입니다. 키워드는 <br> - 영숫자여야 합니다 <br> - 공백이 없어야 합니다 <br> - 10자 미만이어야 합니다. <br> <br> 특정 키워드와 짧은 코드 조합은 한 번에 하나의 활성 프로그램에서만 사용될 수 있습니다. 다른 프로그램에서 이미 사용 중인 키워드가 입력되면 유효성 검사 오류가 발생합니다. <br> <br> 모든 SMS 콘텐츠 제공자가 준수해야 하는 두 가지 필수 키워드 카테고리가 있습니다: <code>STOP</code> 및 <code>HELP</code>."
  - name: 필수 키워드 도움말
    description: "SMS 캠페인 관리자 플랫폼에서 생성된 각 프로그램에 대해 이 키워드에 대한 콘텐츠를 제공해야 하며, SMS 트래픽이 전송되고 수신되는 국가 또는 지역의 모범 사례 및 통신사 준수를 충족해야 합니다. 대부분의 경우, 이 콘텐츠는 SMS 프로그램에 대한 간단한 설명과 OPT-OUT 방법을 포함해야 합니다."
  - name: 글로벌 STOP 키워드
    description: "변형에는 <code>STOP</code>, <code>END</code>, <code>QUIT</code>, <code>UNSUBSCRIBE</code>, <code>CANCEL</code>, <code>STOPALL</code>이 포함됩니다. 이들은 <code>Global-Stop-Keywords</code>로 언급됩니다. 이 키워드 중 하나라도 짧은 코드나 긴 코드로 문자 메시지를 보내면, 해당 코드와 연결된 모든 활성 SMS 프로그램에서 모바일 번호(발신 모바일 전화번호)가 옵트아웃됩니다."
  - name: 바니티 코드
    description: 바니티 짧은 코드는 브랜드에 의해 특별히 선택된 5-6자리 전화번호입니다. 바니티 짧은 코드는 브랜드화되어 있으며 소비자가 기억하기 쉽습니다.
  - name: 공유 짧은 코드
    description: "공유 짧은 코드를 사용할 때, 모든 문자 메시지는 어떤 비즈니스나 조직이 보냈든 관계없이 소비자의 모바일 장치에 동일한 5-6자리 전화번호에서 도착합니다. 공유 짧은 코드는 상대적으로 저렴하고 즉시 사용할 수 있지만, 이는 귀하의 비즈니스가 전용 짧은 코드를 갖지 않으며, 귀하의 공유 짧은 코드에 대해 다른 비즈니스가 올바른 프로토콜을 따르는 것에 따라 달라질 수 있음을 의미합니다." 
  - name: 영숫자 발신자 ID
    description: 영숫자 발신자 ID를 사용하면 지원되는 국가에 일방적인 메시지를 보낼 때 회사 이름이나 브랜드를 발신자 ID로 설정할 수 있습니다.
  - name: 무료 전화번호
    description: "무료 전화번호 또는 프리폰 번호는 발신 전화 가입자에게 요금이 부과되지 않고 모든 수신 전화에 대해 요금이 부과되는 전화번호입니다. 미국과 캐나다의 무료 전화번호는 SMS 기능이 지원되며, 가입자는 수신 및 발신 문자에 대해 요금을 지불합니다.<br><br>무료 메시징은 고객 지원이나 판매와 같이 발신자와 수신자가 문자로 대화를 나누는 경우에 가장 잘 작동합니다."
  - name: 일방향 메시징
    description: 일방향 메시징은 고객에게 문자 메시지를 보내어 소통할 수 있게 해줍니다. 일방향 메시징은 긴 코드와 짧은 코드가 사용되지 않는 시장에서 알파벳 숫자 발신자 ID를 구현하는 경우 유용합니다. 
  - name: 양방향 메시징
    description: 양방향 메시징은 문자 메시지를 보내고 받으며 대화를 나눌 수 있게 해줍니다. 
---
