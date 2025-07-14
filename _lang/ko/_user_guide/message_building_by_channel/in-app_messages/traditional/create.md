---
nav_title: 인앱 메시지 만들기
article_title: 인앱 메시지 만들기
page_order: 1
description: "이 참조 문서에서는 캠페인 또는 캔버스를 사용하여 Braze 플랫폼을 사용하여 인앱 메시지를 만드는 방법에 대해 설명합니다."
channel:
  - in-app messages
tool:
  - Campaigns
search_rank: 4.8
---

# 인앱 메시지 만들기

> 캠페인, 캔버스 또는 API 캠페인으로 Braze 플랫폼을 사용하여 인앱 메시지 또는 인브라우저 메시지를 만들 수 있습니다. 편리한 [인앱 메시지 준비 가이드]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/)를 사용하여 메시지를 계획하고 모든 자료를 미리 준비해 두는 것을 적극 권장합니다.

## 1단계: 메시지를 작성할 위치 선택 {#create-new-campaign-in-app}

메시지를 캠페인으로 보내야 할지 캔버스로 보내야 할지 잘 모르시겠어요? 캠페인은 단일의 간단한 메시징 캠페인에 적합하며, 캔버스는 여러 단계의 사용자 여정에 적합합니다.

{% tabs %}
{% tab 캠페인 %}

1. **메시징** > **캠페인**으로 이동하여 **캠페인 만들기**를 선택합니다.
2. **인앱 메시지**를 선택합니다. 멀티채널 캠페인에서는 인앱 메시지를 사용할 수 없습니다.
3. 캠페인의 이름을 명확하고 의미 있는 것으로 정하세요.
4. Add [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) and [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) as needed.
   * 태그를 사용하면 캠페인을 더 쉽게 찾고 보고서를 작성할 수 있습니다. For example, when using the [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), you can filter by particular tags.
5. 캠페인에 필요한 만큼 이형 상품을 추가하고 이름을 지정하세요. 추가된 각 배리언트에 대해 서로 다른 플랫폼, 메시지 유형 및 레이아웃을 선택할 수 있습니다. 이 주제에 대한 자세한 내용은 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)를 참조하세요.

{% alert tip %}
캠페인의 모든 메시지가 비슷하거나 콘텐츠가 동일한 경우, 변형을 추가하기 전에 메시지를 작성하세요. 그런 다음 **배리언트 상품 추가** 드롭다운에서 **배리언트 상품에서 복사**를 선택할 수 있습니다.
{% endalert %}

{% endtab %}
{% tab 캔버스 %}

1. 캔버스 작성기를 사용하여 [캔버스를 만듭니다]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
2. 캔버스를 설정한 후 캔버스 빌더에서 단계를 추가합니다. 단계에 명확하고 의미 있는 이름을 붙이세요.
3. [단계 스케줄]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay)을 선택하고 필요에 따라 지연을 지정합니다. 인앱 메시지가 포함된 단계는 액션 기반이 될 수 없습니다.
4. 필요에 따라 이 단계의 오디언스를 필터링합니다. 세그먼트를 지정하고 필터를 추가하여 이 단계의 수신자를 더욱 세분화할 수 있습니다. 오디언스 옵션은 지연 후 메시지가 발송되는 시점에 확인됩니다.
5. [진행 동작]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/)을 선택하세요.
6. 메시지와 페어링할 다른 메시징 채널을 선택합니다.

{% alert important %}
한 번에 여러 개의 인앱 메시지 배리언트를 사용할 수 없습니다.
{% endalert %}

You can find more Canvas-specific information in [In-app messages in Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/).

{% endtab %}
{% endtabs %}

## 2단계: 배달 플랫폼 지정

먼저 메시지를 수신할 플랫폼을 선택합니다. 이 선택을 사용하면 특정 앱 집합으로 캠페인 전송을 제한할 수 있습니다. 예를 들어, 사용자가 모바일 앱을 다운로드하도록 유도하는 인브라우저 메시지에 **웹 브라우저를** 선택하여 이미 앱을 다운로드한 후 메시지를 받지 않도록 할 수 있습니다. 플랫폼 선택은 각 변형에 따라 다르므로 플랫폼별로 메시지 참여도를 테스트해 볼 수 있습니다.

| 플랫폼                        | 메시지 전달        |
|---------------------------------|-------------------------|
| 모바일 앱                     | iOS 및 Android SDK      |
| 웹 브라우저                    | 웹 SDK                 |
| 모바일 앱 및 웹 브라우저 모두 | iOS, Android 및 웹 SDK |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 3단계: 메시지 유형 지정

발송 플랫폼을 선택한 후에는 메시지 유형, 레이아웃 및 이와 관련된 기타 옵션을 찾아봅니다. 이러한 각 메시지의 예상 동작 및 모양에 대한 자세한 내용은 [크리에이티브 세부 정보]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/) 페이지 또는 다음 표에서 링크된 메시지 유형을 클릭하여 확인하세요.

어떤 메시지 유형을 사용할지 결정할 때는 인앱 메시지 캠페인이 얼마나 방해가 되는지 고려해야 합니다. 이는 메시지가 차지하는 화면 공간과 이로 인해 고객의 앱 또는 사이트에서의 일반적인 경험을 얼마나 방해하는지 측정합니다. 전달하고자 하는 콘텐츠가 풍부할수록 메시지에 더 많은 신경을 써야 합니다.

![덜 방해되는 것부터 방해가 되는 것까지의 척도를 보여주는 그래픽으로, 슬라이더가 가장 방해가 적고 모달이 그 다음이며 전체 화면이 가장 방해가 됩니다]({% image_buster /assets/img_archive/iam_intrusive.png %}){: style="max-width:80%" }

### 메시지 유형

이러한 인앱 메시지는 모바일 앱과 웹 애플리케이션 모두에서 허용됩니다.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table class="tg">
<thead>
  <tr>
    <th>메시지 유형</th>
    <th>유형 설명</th>
    <th>사용 가능한 레이아웃</th>
    <th>기타 옵션</th>
    <th>권장 사용</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen'>전체 화면</a></td>
    <td>메시지 블록으로 화면 전체를 덮는 메시지.</td>
    <td>
      <ul>
      <li>이미지 및 텍스트</li>
      <li>이미지만</li>
      </ul>
    </td>
    <td>장치 방향 강제 적용(세로 또는 가로)</td>
    <td>크고 대담하게! 가장 중요한 캠페인, 중요한 알림 또는 대규모 프로모션과 같은 콘텐츠를 사용자에게 확실히 보여주고 싶을 때 사용합니다.<br><br>모바일 디바이스의 경우 디바이스의 방향이 메시지의 방향과 일치하지 않으면 세로 및 가로 메시지가 표시되지 않습니다.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal'>Modal</a></td>
    <td>화면 오버레이 및 메시지 블록으로 전체 화면을 덮는 메시지.</td>
    <td>
      <ul>
      <li>텍스트(선택 사항으로 이미지 포함)</li>
      <li>이미지만</li>
      </ul>
    </td>
    <td>N/A</td>
    <td>좋은 중간 지점입니다. 사용자에게 새로운 기능을 사용해 보도록 유도하거나 프로모션을 활용하는 등 사용자의 관심을 끌 수 있는 확실한 방법이 필요할 때 사용합니다.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup'>슬라이드업</a></td>
    <td>화면의 나머지 부분을 가리지 않고 지정된 위치에서 슬라이드하여 볼 수 있는 메시지입니다.</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>눈에 잘 띄지 않음 - 화면 공간을 가장 적게 차지합니다. 새로운 기능, 공지사항, 쿠키 사용 등과 같은 작은 정보 조각을 사용자에게 알릴 때 사용합니다.<br></td>
  </tr>
</tbody>
</table>

### 고급 메시지 유형

이러한 인앱 메시지는 필요에 따라 커스텀 설정할 수 있습니다.

<table class="tg">
<thead>
  <tr>
    <th>메시지 유형</th>
    <th>유형 설명</th>
    <th>사용 가능한 레이아웃</th>
    <th>요구 사항</th>
    <th>권장 사용</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages'>사용자 지정 HTML 메시지</a></td>
    <td>사용자 지정 코드(HTML, CSS 및/또는 JavaScript)에 정의된 대로 작동하는 사용자 지정 메시지입니다.</td>
    <td>N/A</td>
    <td><span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> 초기화 옵션을 <code>true</code> 설정해야 인앱 메시지가 작동합니다.</td>
    <td>IAM의 모든 장점을 원하지만 추가 기능이 필요하거나 외관을 "브랜드에 맞게" 유지하려는 경우 좋은 옵션입니다. 글꼴, 색상, 모양, 크기, 버튼 등 메시지의 모든 세부 사항을 변경할 수 있습니다. <br><br>사용 사례의 예로는 사용자에게 앱 피드백, 이메일 캡처 양식 또는 페이지 매김 메시지를 요청하는 것이 있습니다</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#email-capture-form'>이메일 수집 양식</a></td>
    <td>일반적으로 시청자의 이메일을 캡처하는 데 사용됩니다.</td>
    <td>N/A</td>
    <td><span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> 초기화 옵션을 <code>true</code> 설정해야 인앱 메시지가 작동합니다.</td>
    <td>사용자에게 이메일 주소를 제출하라는 메시지를 표시하는 경우.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css'>CSS를 사용한 웹 모달</a></td>
    <td>사용자 정의 가능한 CSS가 포함된 웹용 모달 메시지.</td>
    <td>
      <ul>
      <li>텍스트(선택 사항으로 이미지 포함)</li>
      <li>이미지만</li>
      </ul>
    </td>
    <td>CSS가 포함된 웹 모달은 웹 SDK에 고유하며 <b>웹 브라우저</b>를 선택한 후에만 사용할 수 있습니다.</td>
    <td>사용자 지정 CSS를 업로드하거나 작성하여 아름답고 다양한 스타일의 사용자 지정 메시지를 만들고 싶을 때입니다. </td>
  </tr>
</tbody>
</table>

{% alert important %}
Braze에서 코드에 닫기 또는 종료 버튼이 포함되어 있지 않다고 감지하면, 이를 추가하도록 요청할 것입니다. 편의를 위해 코드에 복사하여 붙여넣을 수 있는 스니펫을 제공했습니다: <br><br>`<a href= "appboy://close">X</a>`.
{% endalert %}

## 4단계: 인앱 메시지 작성

**작성** 탭에서는 메시지의 콘텐츠와 동작의 모든 측면을 편집할 수 있습니다.

![신규 고객을 환영하고 사용자 프로필을 설정하라는 메시지를 표시하는 브랜드의 인앱 메시지 예시입니다.][24]{: style="max-width:85%" }

**작성** 탭의 내용은 이전 단계에서 선택한 메시지 옵션에 따라 달라지지만 다음 옵션 중 하나를 포함할 수 있습니다:

### 언어

**언어 추가를** 선택하고 제공된 목록에서 원하는 언어를 선택합니다. 이렇게 하면 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic)가 메시지에 삽입됩니다. 콘텐츠를 작성하기 전에 언어를 선택하여 Liquid에서 원하는 위치에 텍스트를 채울 수 있도록 하는 것이 좋습니다. [사용 가능한 언어 전체 목록][18] 을 참조하세요.

### 이미지

메시지 유형에 따라 **이미지 업로드**, **배지 선택** 또는 **멋진 글꼴**을 사용할 수 있습니다. 이미지를 업로드하려면 **이미지 추가를** 클릭하거나 이미지 URL을 입력합니다. **이미지 추가**를 클릭하면 이전에 업로드한 이미지를 선택하거나 새 이미지를 추가할 수 있는 **미디어 라이브러리**가 열립니다. 메시지 유형과 플랫폼마다 권장 비율과 요구 사항이 다를 수 있으므로 이미지를 커미셔닝하거나 처음부터 만들기 전에 해당 사항을 확인하세요!

### 헤더 및 본문

원하는 것은 무엇이든 작성하세요! [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) 및 기타 유형의 개인화를 포함하는 옵션과 함께 완전 사용자 지정 사본(종종 사용자 지정 HTML 기능 포함)을 포함하세요. 메시지를 더 빨리 전달하고 고객의 클릭을 유도할수록 좋습니다! 명확하고 간결한 헤더와 메시지 콘텐츠를 권장합니다.

일부 메시지 유형은 헤더가 필요하지 않으므로 헤더를 요청하지 않습니다.

#### Tips 

##### Generating AI copy

멋진 카피를 만드는 데 도움이 필요하신가요? Try using the [AI copywriting assistant]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/). 제품 이름이나 설명을 입력하면 AI가 메시지에 사용할 수 있도록 사람과 유사한 마케팅 문구를 생성합니다.

![인앱 메시지 작성기의 메시지 필드에 있는 AI 카피라이터 실행 버튼입니다.(]({% image_buster /assets/img/ai_copywriter/ai_copywriter_iam.png %}){: style="max-width:60%"}

##### Creating right-to-left messages

Need help crafting right-to-left messages for languages like Arabic and Hebrew? Refer to [Creating right-to-left messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) for best practices.

### 버튼 텍스트 {#buttons}

메시지 유형에 사용할 수 있는 경우 텍스트 본문 아래에 최대 2개의 버튼을 표시할 수 있습니다. 사용자 지정 버튼 텍스트와 색상을 만들고 편집할 수 있습니다. 이메일 캡처 양식 내에 서비스 약관 링크를 추가할 수도 있습니다.

![인앱 메시지의 기본 및 보조 버튼]({% image_buster /assets/img/primary-secondary-buttons.png %}){: style="float:right;margin-left:15px;height:30%;width:30%"}

하나의 버튼만 사용하도록 선택하면 추가 버튼을 위한 공간을 남겨두는 대신 메시지 하단의 사용 가능한 공간을 차지하도록 버튼이 자동으로 조정됩니다.

#### 기본 버튼 선택

이러한 버튼에 자신만의 색상을 지정하려면 버튼 2를 사용하는 것이 더 좋습니다. 즉, 사용자가 한 버튼을 다른 버튼보다 더 많이 클릭하도록 하려면 해당 버튼이 오른쪽에 있는지 확인하세요. 특히 오른쪽 버튼은 나머지 메시지와 다소 대조적이거나 눈에 띄는 색상을 사용하는 경우 클릭 가능성이 더 높은 경우가 많습니다. 왼쪽의 버튼이 메시지와 시각적으로 더 잘 어우러질 때만 강조됩니다.

### 클릭 시 동작 {#button-actions}

고객이 인앱 메시지에서 버튼을 클릭하면 다음과 같은 작업을 수행할 수 있습니다. 

| 작업 | 설명 |
|---|---|
| 웹 URL로 리디렉션 | 네이티브가 아닌 웹 페이지를 엽니다. |
| [앱으로 딥링크]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | 앱의 기존 화면으로 딥링크를 연결합니다. |
| 메시지 닫기 | 현재 활성화된 메시지를 닫습니다. |
| 사용자 지정 이벤트 로그 | Choose a [custom event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) to trigger. 다른 인앱 메시지를 표시하거나 추가 메시지를 트리거하는 데 사용할 수 있습니다. |
| 사용자 지정 속성 로그 | Choose a [custom attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) to set for the current user. |
| 푸시 권한 요청 | 기본 푸시 권한을 표시합니다. Read more about [push priming]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/), as well as [best practices]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#best-practices) for priming users for push. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

참고: __푸시 권한 요청__, __커스텀 이벤트 로그__, __커스텀 속성 로그__ 옵션을 사용하려면 다음 SDK 최소 버전이 필요합니다:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

### iOS 기기 옵션

원하는 경우 인앱 메시지를 iOS 기기로만 보내도록 제한할 수 있습니다. 이렇게 하려면 **변경**을 클릭하고 **iOS 기기로만 보내기**를 선택합니다.

### 메시지 닫기

다음 옵션 중에서 선택합니다:
 
- **자동 해지:** 메시지가 화면에 표시되는 시간을 몇 초로 할지 선택합니다.
- **사용자가 스와이프하거나 터치할 때까지 기다립니다:** 해지 또는 닫기 옵션이 필요합니다.

### 슬라이드 위로 위치

이 설정은 슬라이드업 메시지 유형에만 적용됩니다. 슬라이드 업을 **앱 화면 하단** 또는 **앱 화면 상단**에서 표시할지 여부를 선택합니다.

### HTML 및 자산

이 설정은 사용자 지정 코드 메시지 유형에만 적용됩니다. 사용 가능한 공간에 HTML을 복사하여 붙여넣고 ZIP 파일을 사용하여 에셋을 업로드합니다.

### 이메일 수집 입력 안내

이 설정은 이메일 캡처 양식 메시지 유형에만 적용됩니다. 이메일 입력 필드의 자리 표시자 텍스트로 표시될 사용자 지정 사본을 입력합니다. 기본값은 "이메일 주소 입력"입니다.

## 5단계: 인앱 메시지 스타일 지정

**스타일** 탭에서는 메시지의 모든 시각적 측면을 조정할 수 있습니다. 이미지 또는 배지를 업로드하거나 미리 디자인된 배지 아이콘을 선택하세요. 팔레트에서 선택하거나 16진수, RGB 또는 HSB 코드를 입력하여 머리글과 본문 텍스트, 버튼 및 배경의 색상을 변경할 수 있습니다.

**스타일** 탭의 콘텐츠는 이전 단계에서 선택한 메시지 옵션에 따라 달라지지만 다음 옵션 중 하나를 포함할 수 있습니다:

| 서식 지정 | 입력 | 설명 |
|---|---|---|
|[색 프로필]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/color_profiles_and_css) | 앱 내 메시지 템플릿 갤러리에서 신청하세요. | **템플릿 적용을** 선택하고 갤러리에서 선택합니다. 그런 다음 **저장**을 선택합니다. |
|텍스트 정렬 | 왼쪽, 가운데 또는 오른쪽.  | 최신 Braze SDK 버전에서만 사용할 수 있습니다. |
|헤더 | HEX 색상 코드. | 원하는 HEX 색상이 표시됩니다. 색상의 불투명도를 선택할 수도 있습니다.  |
|텍스트 | HEX 색상 코드. | 원하는 HEX 색상이 표시됩니다. 색상의 불투명도를 선택할 수도 있습니다. |
|버튼 | HEX 색상 코드. | 원하는 HEX 색상이 표시됩니다. 색상의 불투명도를 선택할 수도 있습니다. 메시지의 닫기 버튼 배경은 물론 각 버튼의 배경, 텍스트 및 테두리의 색상을 선택할 수 있습니다. |
| 버튼 테두리 | HEX 색상 코드. | 신규! 이렇게 하면 기본 버튼과 보조 버튼을 서로 다르게 설정할 수 있습니다. 대비되는 색상으로 버튼의 윤곽선을 그리는 것이 좋습니다. |
|배경색 | HEX 색상 코드. | 원하는 HEX 색상이 표시됩니다. 색상의 불투명도를 선택할 수도 있습니다. 이 배경은 전체 메시지의 배경이며 텍스트 본문 뒤에 명확하게 표시됩니다. |
|화면 오버레이 | HEX 색상 코드. | 원하는 HEX 색상이 표시됩니다. 색상의 불투명도를 선택할 수도 있습니다. 최신 Braze SDK 버전에서만 사용할 수 있습니다. 전체 메시지를 둘러싼 프레임입니다. |
|셰브론 또는 기타 닫기 메시지 옵션 | HEX 색상 코드. | 원하는 HEX 색상이 표시됩니다. 색상의 불투명도를 선택할 수도 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

메시지를 보내기 전에 항상 [미리 보고 테스트하세요]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/).

{% alert important %}
일부 인앱 메시지 유형에는 ZIP 파일을 사용하여 사용자 지정 HTML(또는 CSS 또는 JavaScript) 및 에셋을 업로드하는 것 외에 스타일 지정 옵션이 없습니다. [CSS가 포함된 웹 모달을]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css) 사용하면 사용자 지정 CSS를 업로드하거나 작성하여 모든 기능을 갖춘 멋진 사용자 지정 스타일의 메시지를 만들 수 있습니다.
{% endalert %}

## 6단계: 추가 설정 구성(선택 사항)

### 키-값 쌍

[키-값 페어][19]를 추가하여 사용자 기기에 추가 커스텀 필드를 보낼 수 있습니다.

## 7단계: 나머지 캠페인 또는 캔버스 구축하기

{% tabs %}
{% tab 캠페인 %}

다음 섹션에서 인앱 메시지를 작성하기 위해 도구를 가장 효과적으로 사용하는 방법에 대한 자세한 지침을 확인하세요.

#### 트리거 선택

메시지를 트리거할 액션과 캠페인 또는 캔버스의 시작 및 종료 시간을 선택합니다.

{% alert important %}
사용자 지정 이벤트를 기반으로 인앱 메시지를 트리거하려는 경우, 해당 사용자 지정 이벤트는 SDK를 사용하여 전송해야 한다는 점에 유의하세요.
{% endalert %}

![트리거 액션이 "세션 시작"으로 설정된 액션 기반 캠페인.]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="max-width:80%"}

인앱 메시지 전달은 전적으로 다음 액션 트리거를 기반으로 합니다:

- 구매하기
- 앱/웹페이지 열기
- 사용자 지정 이벤트 수행하기(SDK를 사용하여 전송한 이벤트에서만 작동)
- 특정 푸시 메시지 열기
- 각 사용자의 현지 시간을 기준으로 특정 시간에 보낼 캠페인을 자동으로 예약할 수 있습니다.
- 매일, 매주(선택 사항으로 특정 요일) 또는 매월 반복되도록 메시지를 구성할 수도 있습니다.

시작 날짜와 시간은 반드시 선택해야 하지만 종료 날짜는 선택 사항입니다. 종료 날짜를 설정하면 지정된 날짜/시간 이후에는 특정 인앱 메시지가 기기에 표시되지 않습니다.

Refer to our developer documentation for [server-side event triggering]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web) and [local in-app message delivery]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#local-in-app-messages).

##### 온라인 트리거와 오프라인 트리거

인앱 메시지는 메시지와 트리거를 사용자의 디바이스로 전송하는 방식으로 작동합니다. 인앱 메시지가 기기에 표시된 후 트리거 조건이 충족될 때까지 기다립니다. 인앱 메시지가 이미 사용자의 기기에 캐시되어 있는 경우, Braze에 연결하지 않고도 오프라인(예: 비행기 모드)에서 인앱 메시지를 트리거할 수도 있습니다.

{% alert important %}
인앱 메시지가 중지된 후 메시지가 중지되기 전에 세션을 시작하고 트리거 이벤트를 수행한 경우 메시지가 계속 표시되는 사용자가 있을 수 있습니다. 이러한 사용자는 캠페인이 중지된 후에도 고유 노출로 계산됩니다.
{% endalert %}

#### 우선순위 선택

마지막으로 인앱 메시지가 트리거될 작업을 선택한 후에는 우선순위도 설정해야 합니다. 동일한 작업으로 인해 두 개의 메시지가 트리거되는 경우 우선순위가 높은 메시지가 우선순위가 낮은 메시지보다 먼저 사용자의 디바이스에 표시되도록 예약됩니다. 

다음 메시지 우선순위 중에서 선택할 수 있습니다:

- 낮은 우선순위(다른 메시지 다음에 표시됨)
- 중간 우선순위
- 높은 우선순위(다른 메시지보다 먼저 표시됨)

트리거된 메시지 우선순위의 높음, 중간, 낮음 옵션은 버킷이며, 따라서 여러 메시지의 우선순위가 동일하게 선택될 수 있습니다. 이러한 버킷 내에서 우선순위를 설정하려면 **정확한 우선순위 설정을** 클릭하고 캠페인을 끌어서 놓아 올바른 우선순위로 정렬할 수 있습니다.

![인앱 메시지 캠페인 및 캔버스에 대한 우선순위를 설정하는 방법의 예.]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

#### 타겟팅할 사용자 선택

다음으로 세그먼트 또는 필터를 선택하여 [사용자를 타겟팅하여]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) 오디언스의 범위를 좁혀야 합니다. 대략적인 세그먼트 인구가 현재 어떤 모습인지에 대한 스냅샷이 자동으로 제공됩니다. 정확한 세그먼트 멤버십은 항상 메시지가 전송되기 직전에 계산된다는 점에 유의하세요.

{% alert note %}
인앱 메시지 단계에서 지연이 발생하는 경우, 세그먼트 멤버십은 지연이 발생한 후에 평가됩니다. 사용자가 자격을 갖춘 경우, 인앱 메시지는 다음 사용 가능한 세션에서 동기화됩니다.
{% endalert %}

##### 캠페인 자격 및 리퀴드 재평가

일부 시나리오에서는 인앱 메시지를 표시할 때 사용자의 자격을 다시 평가해야 할 수도 있습니다. 자주 변경되는 사용자 지정 속성을 타겟팅하는 캠페인이나 마지막 순간에 프로필 변경 사항을 반영해야 하는 메시지를 예로 들 수 있습니다.

![타겟 사용자 단계의 오디언스 요약 섹션에서 "표시하기 전에 캠페인 자격 재평가" 옵션을 선택합니다.]({% image_buster /assets/img_archive/re-evaluate-iam-membership.png %})

**표시하기 전에 캠페인 자격 재평가**를 선택하면, 메시지를 보내기 전에 사용자가 여전히 이 메시지를 받을 자격이 있는지 확인하기 위해 Braze에 추가 요청이 이루어집니다. 또한 모든 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) 변수 또는 [연결된 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)는 메시지가 표시되기 전에 해당 순간에 템플릿이 지정됩니다.

이렇게 하면 만료되었거나 보관된 캠페인 내에서 인앱 메시지가 사용자에게 전송되지 않습니다. 사용자의 자격을 재평가하지 않으면 캠페인이 만료되거나 보관된 후에도 인앱 메시지가 SDK에 저장되어 사용자가 트리거하기를 기다리고 있기 때문에 사용자는 인앱 메시지를 받게 됩니다.

{% alert note %}
이 옵션을 활성화하면 추가된 자격 및 템플릿 요청으로 인해 사용자가 인앱 메시지를 트리거하는 시점과 메시지가 표시되는 시점 사이에 약간의 지연(100ms 미만)이 발생할 수 있습니다.
<br><br>
사용자가 오프라인 상태이거나 자격 및 Liquid 재평가가 필요하지 않은 경우 트리거할 수 있는 메시지에는 이 옵션을 사용하지 마세요.
{% endalert %}

#### 전환 이벤트 선택

Braze를 사용하면 사용자가 캠페인을 수신한 후 특정 행동, [전환 이벤트]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)를 얼마나 자주 수행하는지 추적할 수 있습니다. 사용자가 지정된 작업을 수행하면 최대 30일 동안 전환이 카운트되도록 허용하는 옵션이 있습니다.

{% endtab %}
{% tab 캔버스 %}

아직 완료하지 않았다면 캔버스 구성 요소의 나머지 섹션을 완료하세요. 캔버스의 나머지 부분을 구성하고, 다변량 테스트 및 지능형 선택을 구현하는 방법 등에 대한 자세한 내용은 캔버스 설명서의 [캔버스 구성]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) 단계를 참조하세요.

For information on Canvas-specific in-app messaging options, refer to [In-app messages in Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/).

{% endtab %}
{% endtabs %}

## 8단계: 검토 및 배포

캠페인 또는 캔버스의 마지막 제작을 완료한 후에는 세부 정보를 검토하고 [테스트한]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) 다음 전송하세요!

다음으로 [인앱 메시지 보고]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/)를 확인하여 메시징 캠페인의 결과에 액세스하는 방법을 알아보세요.

## 알아두어야 할 사항

### 활성 인앱 메시지 캠페인 한도

Braze는 안정성과 속도를 중시합니다. 필요한 데이터만 Braze에 전송하는 것을 권장하는 것처럼, 브랜드에 더 이상 가치를 제공하지 않는 캠페인도 해제하는 것을 권장합니다.

아직 활성 상태이지만 더 이상 메시지를 보내지 않거나 더 이상 필요하지 않은 액션 기반 인앱 메시지 캠페인을 처리하면 귀하와 다른 고객의 전반적인 Braze 서비스 성능이 느려집니다. 이렇게 많은 수의 유휴 캠페인을 처리하는 데 시간이 추가로 소요되면 인앱 메시지가 최종 사용자의 기기에 표시되는 데 시간이 더 오래 걸리고, 이는 최종사용자의 경험에 영향을 미칩니다.

{% alert important %}
작업 공간당 최대 200개의 활성 액션 기반 인앱 메시지 캠페인을 보유하여 메시지 전달 속도를 최적화하고 시간 초과를 방지할 수 있습니다. 캔버스에는 적용되지 않습니다.
{% endalert %}

200개에는 아직 종료 시간에 도달하지 않은 활성 인앱 메시지 캠페인과 종료 시간이 없는 캠페인이 포함됩니다. 종료 시간이 지난 활성 인앱 메시지 캠페인은 집계되지 않습니다. 평균적으로 Braze 고객은 한 번에 총 26개의 캠페인을 활성화하므로 이 제한이 영향을 미치지는 않을 것입니다.


[2]: {% image_buster /assets/img/iam-generations.gif %}
[16]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported
[19]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/
[24]: {% image_buster /assets/img_archive/iam_compose.png %}
[25]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[26]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
[27]: {% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}
