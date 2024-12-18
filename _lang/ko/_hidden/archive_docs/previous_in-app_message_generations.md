---
nav_title: 이전 세대
article_title: 이전 인앱 메시지 생성
page_order: 20
page_type: reference
description: "이 문서에서는 Braze의 인앱 메시지에 대한 이전 정보를 검토합니다."
channel: in-app messages
noindex: true
hidden : true
---

# 이전 인앱 메시지 생성

{% alert important %}
이 페이지에서는 인앱 메시지와 관련된 이전 정보를 검토합니다. 현재 인앱 메시지 생성에 대한 최신 정보를 확인하려면 현재 [인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) 설명서를 참조하세요.
{% endalert %}

## 유니버설

인앱 메시지와 관련된 이전 정보를 검토합니다. 현재 인앱 메시지 생성에 대한 최신 정보를 확인하려면 [인앱 메시지 개요 설명서]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/)를 참조하세요.

{% details 전체 화면 %}
가장 매력적이지만 사용자의 화면 전체를 덮기 때문에 가장 방해가 되는 광고이기도 합니다. 크고 풍부한 이미지를 표시하는 데 적합하며 중요한 새 기능이나 만료되는 프로모션과 같은 매우 중요한 정보를 전달하는 데 유용할 수 있습니다. 사용자 경험을 방해할 수 있으므로 최우선 순위 콘텐츠에만 제한적으로 사용하세요.

![전체 화면 메시지]({% image_buster /assets/img_archive/braze_fullscreen.png %}){: style="max-width:80%;"}

**사용자 지정 가능한 기능**

- 헤더 및 본문 텍스트
- 큰 이미지
- 별도의 클릭 동작 및 딥 링크가 있는 최대 2개의 클릭 유도 문안 버튼
- 헤더와 본문 텍스트, 버튼 및 배경의 색상이 다릅니다.
- 키-값 쌍

{% enddetails %}
{% details  모달 %}
이러한 메시지는 사용자가 여전히 앱 UI의 일부를 볼 수 있으므로 전체 화면 메시지만큼 방해가 되지 않습니다. 모달 메시지에는 여전히 버튼과 이미지가 포함되어 있으므로 보다 인터랙티브하고 시각적인 캠페인을 원한다면 슬라이드업보다 모달 메시지가 더 나은 옵션이 될 수 있습니다. 앱 업데이트, 긴급하지 않은 거래 및 이벤트와 같이 우선순위가 중간 정도인 콘텐츠에 적합합니다.

![모달 메시지]({% image_buster /assets/img_archive/braze_modal.png %}){: style="max-width:80%;"}

**사용자 지정 가능한 기능**

- 헤더 및 본문 텍스트
- 이미지 또는 사용자 지정 가능한 배지 아이콘
- 별도의 클릭 동작 및 딥 링크가 있는 최대 2개의 클릭 유도 문안 버튼
- 헤더와 본문 텍스트, 버튼 및 배경의 색상이 다릅니다.
- 키-값 쌍

{% enddetails %}

{% details 전통적인 슬라이드업 %}
색상과 배지 아이콘을 어떻게 사용하느냐에 따라 주의를 끌 수 있지만, 가장 방해가 적은 메시지 유형입니다. 앱 경험을 일시 중지하지 않고 지속적인 탐색을 허용하므로 신규 사용자를 온보딩하고 특정 인앱 기능으로 안내할 때 사용할 수 있는 메시지 형식일 수 있습니다.

![슬라이드업 메시지]({% image_buster /assets/img_archive/stopwatch_slideup_IAM.gif %}){: style="max-width:50%;"}

**사용자 지정 가능한 기능**

- 본문 텍스트
- 이미지 또는 사용자 지정 가능한 배지 아이콘
- 슬라이드업 배경, 텍스트 및 아이콘의 색상 변경
- 메시지 닫기 동작
- 슬라이드업 위치(앱 화면 상단 또는 하단)
- 키-값 쌍

{% enddetails %}

<br>

## 웹

이렇게 하면 더욱 커스텀된 인앱 메시지에 대한 이전 정보를 검토할 수 있습니다. 현재 인앱 메시지 생성에 대한 최신 정보를 확인하려면 [사용자 지정 설명서]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/)를 참조하세요.

{% details 이메일 캡처 메시지 %}
이메일 캡처 메시지를 사용하면 사이트 사용자에게 이메일 주소를 제출하도록 쉽게 유도할 수 있으며, 이후에는 모든 메시징 캠페인에서 사용할 수 있도록 Braze 시스템 내에서 해당 이메일 주소를 사용할 수 있습니다.

![이메일 캡처 메시지]({% image_buster /assets/img_archive/web-email-capture.png %}){: style="max-width:60%;"}

>  웹 SDK를 통해 이메일 인앱 메시지 캡처를 활성화하려면 `allowUserSuppliedJavascript` 초기화 옵션을 Braze에 제공해야 합니다(예: `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`). 이는 보안상의 이유로, HTML 인앱 메시지는 JavaScript를 실행할 수 있으므로 사이트 관리자가 이를 활성화해야 합니다.

**사용자 지정 가능한 기능**

- 헤더, 본문 및 제출 버튼 텍스트
- 선택적 이미지
- 선택 사항인 '서비스 약관' 링크
- 헤더와 본문 텍스트, 버튼 및 배경의 색상이 다릅니다.
- 키-값 쌍

{% enddetails %}

{% details 사용자 지정 HTML 메시지 %}

Braze의 기본 인앱 메시지는 다양한 방식으로 맞춤 설정할 수 있지만, HTML, CSS 및 JavaScript를 사용하여 디자인하고 구축한 메시지를 사용하면 캠페인의 모양과 느낌을 더욱 효과적으로 제어할 수 있습니다. 몇 가지 간단한 구성으로 필요에 따라 맞춤 기능과 브랜딩을 사용할 수 있습니다. HTML 인앱 메시지를 사용하면 메시지의 모양과 느낌을 더 잘 제어할 수 있으며, HTML5에서 지원되는 모든 것은 Braze에서도 지원됩니다.

**JavaScript Bridge(appboyBridge)**

HTML 인앱 메시지는 사용자가 링크가 있는 요소를 클릭하거나 다른 방식으로 콘텐츠에 참여할 때 사용자 지정 Braze 액션을 트리거할 수 있도록 Braze 웹 SDK에 대한 JavaScript "브릿지" 인터페이스를 지원합니다. Braze의 HTML 인앱 메시지에서 지원되는 자바스크립트 메서드는 다음과 같습니다:

{% multi_lang_include archive/appboyBridge.md platform="web" %}

또한 분석 추적 기술을 위해 HTML의 `<a>` 또는 `<button>` 요소는 인앱 메시지와 연결된 캠페인에 "클릭" 액션을 자동으로 기록합니다. '본문 클릭' 대신 '버튼 클릭'을 기록하려면 링크의 href(예: `<a href="http://mysite.com?abButtonId=0">click me</a>`)에 abButtonId의 쿼리 문자열 값을 제공하거나 HTML 요소에 id(예: `<a id="0" href="http://mysite.com">click me</a>`)를 제공하세요. 현재 허용되는 버튼 ID는 "0"과 "1"뿐입니다. 버튼 ID가 0인 링크는 대시보드에서 "버튼 1"로 표시되고, 버튼 ID가 1인 링크는 "버튼 2"로 표시됩니다.

>  웹 SDK를 통해 HTML 인앱 메시지를 활성화하려면 Braze에 `allowUserSuppliedJavascript` 초기화 옵션을 제공해야 합니다(예: `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`). 이는 보안상의 이유로, HTML 인앱 메시지는 JavaScript를 실행할 수 있으므로 사이트 관리자가 이를 활성화해야 합니다.

{% enddetails %}

{% details HTML 인앱 메시지 템플릿 %}

시작하는 데 도움이 되는 HTML5 인앱 메시지 템플릿 세트를 준비했습니다. 이러한 템플릿을 사용하고 필요에 맞게 사용자 지정하는 방법에 대한 자세한 지침이 포함된 [GitHub 리포지토리](https://github.com/braze-inc/in-app-message-templates)를 확인하세요.

**사용자 지정 가능한 기능**

- 글꼴
- 스타일
- 이미지 + 동영상
- 클릭 시 동작
- 인터랙티브 구성 요소

{% enddetails %}

<br>

## 사양

여기에서는 인앱 메시지 크리에이티브 사양에 대한 이전 정보를 검토합니다. 현재 인앱 메시지 생성에 대한 최신 정보를 확인하려면 [크리에이티브 사양 설명서]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/)를 참조하세요.

### 문자 및 이미지 제한

다음 테이블에 나열된 모든 인앱 메시지 유형에 대해 다음과 같은 추가 지침이 적용됩니다:

- **권장 이미지 크기:** 500 KB 
- **최대 이미지 크기:** 5MB
- **지원되는 파일 형식:** PNG, JPEG, GIF

| 유형                               | 화면 비율 | 최대 문자 수 |
| :--------------------------------- | :----------: | :-----------------: |
| 세로 전체 화면(이미지 전용)  |    10:16     |         240         |
| 세로 전체 화면(텍스트 포함)   |     5:4      |         240         |
| 가로 전체 화면(텍스트 포함)  |     16:5     |         240         |
| 가로 전체 화면(이미지 전용) |    16:10     |         240         |
| 슬라이드업                            |     1:1      |         140         |
| 모달(이미지 전용)                 |     1:1      |         140         |
| 모달(텍스트 포함)                  |    29:10     |         140         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 인앱 메시지 파일 크기를 작게 유지

Braze는 여러 가지 이유로 이미지와 HTML 에셋의 압축을 가능한 작게 유지하는 것을 권장합니다:

- HTML 및 이미지 메시지 페이로드가 작을수록 다운로드 속도가 빨라지고 고객에게 더 빠르고 안정적으로 표시됩니다.
- HTML 및 이미지 메시지 페이로드가 작아지면 고객의 데이터 비용도 절감할 수 있습니다. Braze 인앱 메시지는 세션 시작 시 백그라운드에서 다운로드되어 사용자가 선택한 기준에 따라 실시간으로 트리거될 수 있습니다. 결과적으로 1MB씩 10개의 HTML 인앱 메시지가 있는 경우, 고객이 모든 메시지를 트리거하지 않더라도 모두 10MB의 데이터 요금이 부과됩니다. 인앱 메시지가 캐시되고 세션에서 세션으로 다시 다운로드되지 않더라도 시간이 지남에 따라 빠르게 누적될 수 있습니다.

파일 크기를 줄이는 데 도움이 되는 전략은 다음과 같습니다:

- HTML 에셋 ZIP 폴더에 글꼴 파일을 포함하지 않고 애플리케이션이나 웹사이트에 포함된 참조 글꼴을 사용하여 HTML 인앱 메시지를 사용자 지정할 수 있습니다.
- HTML 에셋 ZIP에 불필요하거나 중복되는 CSS 또는 JavaScript가 포함되어 있지 않은지 확인하세요.
- 모든 이미지에 [ImageOptim][25]을 사용하면 품질 저하 없이 이미지를 가능한 최소 크기로 압축할 수 있습니다.

### iPhone 5 사양

![iPhone 5 사양][18]

### iPhone 6 사양

![iPhone 6 사양][19]


[18]: {% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_05.png %}

[19]: {% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_06.png %}

[25]: https://imageoptim.com/
