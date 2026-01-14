---
nav_title: "푸시 알림 유형"
article_title: 푸시 알림 유형
page_order: 1
page_type: glossary
description: "이 용어집에는 Braze를 사용하여 보낼 수 있는 다양한 유형의 푸시 알림이 나열되어 있습니다."
channel: push

layout: glossary_page
glossary_top_header: "Types of push notifications"
glossary_top_text: "There are many types of push notifications you can use to interact with your customers. These can be narrowed by channel and used to meet the needs of many different users. You can configure most of these settings in your Push campaigns, but there are notes in the following descriptions that will indicate whether any backend configurations are needed and what those might be."

glossary_tag_name: Channels
glossary_filter_text: "Select any of the following channels to narrow Push Type options."

# category to icon/fa or image mapping
glossary_tags:
  - name: iOS
  - name: Android
  - name: 웹

glossaries:
  - name: "정기 푸시"
    description: "모든 것을 아우르는 푸시 메시지. 이러한 알림은 사용자의 기기에 알림 소리와 메시지로 표시되며, 알림 표시줄이나 스택에 슬라이드되거나 표시됩니다."
    tags:
      - iOS
      - Android
      - Web
  - name: "웹 푸시"
    description: "이러한 푸시 메시지는 웹 앱 또는 브라우저에 표시됩니다. 고객에게 연락하려면 여전히 허가가 필요합니다. 사용자가 숨겨진 브라우저를 사용하는 경우 웹 푸시가 작동하지 않습니다."
    tags:
      - Web
  - name: "푸시 프라이머 캠페인"
    description: "인앱 메시지 캠페인은 사용자로부터 명시적인 푸시 옵트인 또는 옵트아웃 신호를 얻는 데 사용됩니다. 프라이머를 통해 기기 설정을 통해 푸시 알림을 끌 가능성이 있는 사용자에게 알림을 보내지 않도록 할 수 있습니다. iOS의 경우, 사용자가 명시적으로 iOS의 기본 푸시 안내에 옵트인하지 않으면 포그라운드 푸시 알림(예: 기기 깨우기 알림)이 인에이블먼트되지 않으므로 푸시 캠페인이 적절합니다."
    tags:
      - iOS
      - Android
      - Web
  - name: "푸시 스토리"
    description: "푸시 스토리는 캐러셀 형태의 시각적 여정을 통해 사용자를 안내하는 몰입형 메시지입니다. 모바일 기기에서만 사용할 수 있습니다."
    tags:
      - iOS
      - Android
  - name: "실행 버튼으로 푸시하기"
    description: "푸시 실행 버튼은 사용자에게 옵션을 제공하고 여러 가지 콜투액션을 제공할 수 있는 메시지입니다."
    tags:
      - iOS
      - Android
      - Web
  - name: "리치 푸시 알림"
    description: "리치 푸시 알림은 단순한 아이콘과 콜투액션 텍스트를 뛰어넘는 몰입형 이미지와 창의적인 콘텐츠가 포함된 알림입니다."
    tags:
      - iOS
      - Android
  - name: "iOS용 임시 푸시 알림"
    description: "iOS 12에서 Apple이 도입한 임시 승인은 iOS 앱 설치 시 자동으로 발생하므로 브랜드가 사용자에게 푸시 알림을 표시하지 않고도 무음 알림을 보낼 수 있습니다. 무음 푸시가 전송되어 기기의 알림 트레이에서 확인되면 사용자에게 푸시 알림을 허용하거나 중단할 수 있는 옵션이 제공됩니다."
    tags:
      - iOS
  - name: "HTML 푸시 알림"
    description: "HTML 푸시 알림은 HTML로 하드 코딩된 푸시 메시지로, Braze에서 제공하는 사전 설정된 푸시 템플릿을 사용하지 않습니다. HTML 푸시 알림을 만들 수 있는 옵션을 사용하면 푸시 메시지의 모양을 원하는 대로 자유롭게 설정할 수 있고 일관성 있는 브랜딩을 할 수 있습니다."
    tags:
      - Android
  - name: "알림 ID 및 채널 ID"
    description: "알림 ID와 채널 ID를 사용하면 사용자가 이미 받았지만 열지 않은 푸시 알림을 교체하거나 업데이트할 수 있습니다."
    tags:
      - iOS
      - Android
  - name: "백그라운드 또는 무음 푸시 알림"
    description: "기기에서 렌더링되지 않는 푸시 알림. 일반적으로 백그라운드 프로세스 및 제거 추적을 위해 앱으로 정보 패킷을 보내는 데 사용됩니다. 백그라운드 또는 무음 푸시를 보내려면 백그라운드 인에이블먼트 푸시 토큰이 필요합니다."
    tags:
      - iOS
      - Android
      - Web
  - name: "웨어러블 푸시 알림"
    description: "이러한 푸시 알림을 통해 브랜드는 Apple Watch와 같은 웨어러블 기기에 직접 메시지를 보낼 수 있습니다."
    tags:
      - iOS

---
