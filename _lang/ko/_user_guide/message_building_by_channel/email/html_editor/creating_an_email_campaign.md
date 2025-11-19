---
nav_title: 이메일 만들기
article_title: 커스텀 HTML로 이메일 만들기
page_order: 1
description: "이 참고 문서에서는 Braze 플랫폼을 사용하여 이메일을 작성하는 방법을 설명합니다. 메시지 작성기, 콘텐츠 미리보기, 캠페인 또는 캔버스 예약 방법에 대한 모범 사례가 포함되어 있습니다."
tool:
  - Campaigns
channel:
  - email
search_rank: 1  
---

# 커스텀 HTML로 이메일 만들기

> 이메일 메시지는 사용자에게 원하는 방식으로 콘텐츠를 전달하는 데 유용합니다. 또한 앱을 삭제한 사용자의 재참여를 유도할 수 있는 훌륭한 툴이기도 합니다. 커스텀된 맞춤형 이메일 메시지를 보내면 사용자 경험을 향상시키고 사용자가 앱에서 최대한의 가치를 얻을 수 있습니다. 

이메일 캠페인의 예시를 보려면 [사례 연구를](https://www.braze.com/customers) 확인하세요. 

{% alert tip %}
이메일 캠페인을 처음 만드는 경우, 다음 Braze 학습 과정을 확인해 보시기 바랍니다:<br><br>
- [이메일 옵트인 및 권한](https://learning.braze.com/messaging-channels-email)
- [프로젝트: 기본 이메일 마케팅 프로그램 구축하기](https://learning.braze.com/project-build-a-basic-email-marketing-program)
{% endalert %}

## 1단계: 메시지 구축 위치 선택하기

메시지를 캠페인으로 보내야 할지 캔버스로 보내야 할지 잘 모르시겠어요? 캠페인은 단일의 간단한 메시징 캠페인에 적합하며, 캔버스는 여러 단계의 사용자 여정에 적합합니다.

{% tabs %}
{% tab Campaign %}

1. **메시징** > **캠페인으로** 이동하여 **캠페인 만들기를** 선택합니다.
2. **이메일을** 선택하거나 여러 채널을 타겟팅하는 캠페인의 경우 **멀티채널을** 선택합니다.
3. 캠페인 이름을 명확하고 의미 있는 것으로 정하세요.
4. 필요에 따라 [팀과]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) [태그를]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) 추가합니다.
   * 태그를 사용하면 캠페인을 더 쉽게 찾고 보고서를 구축할 수 있습니다. 예를 들어 [보고서 빌더를]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) 사용할 때 특정 태그를 기준으로 필터링할 수 있습니다.
5. 캠페인에 필요한 만큼 배리언트를 추가하고 이름을 지정하세요. 이 주제에 대한 자세한 내용은 [다변량 및 A/B 테스트를]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) 참조하세요.

{% alert tip %}
캠페인의 모든 메시지가 비슷하거나 콘텐츠가 동일한 경우 배리언트를 추가하기 전에 메시지를 작성하세요. 그런 다음 **배리언트 추가** 드롭다운에서 **배리언트에서 복사를** 선택할 수 있습니다.
{% endalert %}
{% endtab %}
{% tab Canvas %}

1. 캔버스 작성기를 사용하여 캔버스를 [만듭니다]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
2. 캔버스를 설정한 후 캔버스 빌더에서 단계를 추가합니다. 단계에 명확하고 의미 있는 이름을 붙이세요.
3. [단계 일정을]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) 선택하고 필요에 따라 지연을 지정합니다.
4. 필요에 따라 이 단계에서 오디언스를 필터링합니다. 세그먼트를 지정하고 필터를 추가하여 이 단계의 수신자를 더욱 세분화할 수 있습니다. 오디언스 옵션은 지연 후 메시징이 전송될 때 확인됩니다.
5. [진행 방식을]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) 선택하세요.
6. 메시지와 페어링할 다른 메시징 채널을 선택합니다.
{% endtab %}
{% endtabs %}

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='email html editor' %}

## 2단계: 편집 환경 선택하기 {#step-2-choose-your-template-and-compose-your-email}

Braze는 이메일 캠페인을 만들 때 [드래그 앤 드롭 편집기와]({{site.baseurl}}/dnd/) 표준 HTML 편집기 두 가지 편집 환경을 제공합니다. 원하는 편집 환경에 적합한 타일을 선택합니다. 

드래그 앤 드롭 편집기, HTML 편집기 또는 템플릿 중에서 이메일 편집 환경을 선택합니다.]({% image_buster /assets/img_archive/choose_email_creation.png %}){: style="max-width:75%" }

그런 다음 기존 [이메일 템플릿을]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template) 선택하거나 파일에서 [템플릿을 업로드하거나]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/) (HTML 편집기만 해당) 빈 템플릿을 사용할 수 있습니다. 

{% alert tip %}
이메일 캠페인당 하나의 편집 환경을 선택하는 것이 좋습니다. 예를 들어, 편집기 간에 전환하지 않고 하나의 이메일 캠페인에서 **HTML 클래식** 또는 **블록 편집기** 중 하나를 선택합니다.
{% endalert %}

## 3단계: 이메일 작성

템플릿을 선택하면 전체 화면 편집기로 바로 이동하여 이메일 초안을 작성하고, 전송 정보를 변경하고, 전달 가능성 또는 법률 준수에 대한 경고를 확인할 수 있는 이메일 개요가 표시됩니다. 작성하는 동안 HTML, 클래식, 일반 텍스트 및 [AMP]({{site.baseurl}}/user_guide/message_building_by_channel/email/amphtml/) 탭 간에 전환할 수 있습니다. 

'HTML에서 재생성' 버튼을 클릭합니다.]({% image_buster /assets/img_archive/regenerate_from_html.png %}){: style="max-width:30%;float:right;margin-left:15px;border:none;" }

이메일의 일반 텍스트 버전은 일반 텍스트 버전으로 편집이 감지될 때까지 항상 HTML 버전에서 자동으로 업데이트됩니다. 편집이 감지되면 덮어쓰지 말아야 할 내용을 의도적으로 변경한 것으로 간주하므로 Braze는 더 이상 일반 텍스트를 업데이트하지 않습니다. 일반 **텍스트** 탭에서 일반 텍스트가 동기화되지 않는 경우에만 표시되는 **HTML에서 재생성** 아이콘을 선택하여 자동 동기화로 되돌릴 수 있습니다.

{% alert tip %}
대부분의 받은편지함은 자바스크립트를 지원하지 않으므로 이메일에 정확한 미리보기로 모션을 추가하려면 자바스크립트가 필요한 요소 대신 GIF를 사용하세요.
{% endalert %}

이메일 배리언트 패널에서 이메일을 작성할 수 있습니다.]({% image_buster /assets/img/email.png %}){: style="max-width:75%" }

{% alert important %}
Braze는 속성으로 참조된 HTML 이벤트 핸들러를 자동으로 제거합니다. 이렇게 하면 HTML이 수정되므로 완료된 후 이메일을 다시 확인하는 것이 좋습니다. [HTML 핸들러에](https://www.w3schools.com/tags/ref_eventattributes.asp) 대해 자세히 알아보세요.
{% endalert %}

{% alert tip %}
멋진 카피를 만드는 데 도움이 필요하신가요? [AI 카피라이팅 도]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/)우미를 사용해 보세요. 제품 이름이나 설명을 입력하면 AI가 메시징에 사용할 수 있는 사람과 유사한 마케팅 문구를 생성합니다.

이메일 작성기의 본문 탭에 있는 AI 카피라이터 실행 버튼을 클릭합니다.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_email.png %}){: style="max-width:80%"}
{% endalert %}

아랍어 및 히브리어와 같은 언어에 대한 오른쪽에서 왼쪽으로 메시지를 작성하는 데 도움이 필요하신가요? 모범 사례는 [오른쪽에서 왼쪽으로 메시지 만들기를]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) 참조하세요.

### 3a단계: 전송 정보 추가

이메일 메시지 디자인 및 구축을 완료했다면 이제 **전송 설정** 섹션에서 전송 정보를 추가할 차례입니다.

1. **정보 보내기에서** **발신자 표시 이름 + 주소로** 이메일을 선택합니다. **표시 이름 + 주소에서 커스텀을** 선택하여 커스텀할 수도 있습니다.
2. **회신할 주소로** 이메일을 선택합니다. **답장 받는 사람 주소 사용자 지정을** 선택하여 커스텀할 수도 있습니다.
3. 다음으로, 이메일을 **BCC 주소로** 선택하여 이 주소에 이메일을 표시합니다.
4. 이메일에 제목란을 추가합니다. 선택적으로 프리헤더와 프리헤더 뒤에 공백을 추가할 수도 있습니다.

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

오른쪽 패널의 미리보기가 추가한 전송 정보로 채워집니다. 이 정보는 **설정** > **이메일 환경설정** > **보내기 구성으로** 이동하여 업데이트할 수도 있습니다.

#### 진행 중

**전송 설정** > **고급에서** 인라인 CSS를 켜고 이메일 헤더 및 이메일 엑스트라에 대한 개인화를 추가하여 다른 이메일 서비스 제공업체에 추가 데이터를 다시 보낼 수 있습니다.

##### 이메일 헤더

이메일 헤더를 추가하려면 **새 헤더 추가를** 선택합니다. 이메일 헤더에는 전송되는 이메일에 대한 정보가 포함되어 있습니다. 이러한 [키-값 페어에는]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) 일반적으로 발신자, 수신자, 인증 프로토콜 및 이메일 라우팅 정보에 대한 정보가 포함됩니다. Braze는 이메일이 받은편지함 제공업체에 제대로 전달될 수 있도록 RFC에서 요구하는 필수 헤더 정보를 자동으로 추가합니다.

Braze를 사용하면 필요에 따라 이메일 헤더를 유연하게 추가하여 고급 사용 사례를 진행할 수 있습니다. 전송 중에 Braze 플랫폼이 덮어쓰는 몇 가지 예약 필드가 있습니다. 

다음 키는 사용하지 마세요:

<style>
#reserved-fields td {
    word-break: break-word;
    width: 33%;
}
</style>

<table id="reserved-fields">
<thead>
  <tr>
    <th>예약 필드</th>
    <th></th>
    <th></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>BCC</td>
    <td>dkim-signature</td>
    <td>회신 대상</td>
  </tr>
  <tr>
    <td>CC</td>
    <td>에서</td>
    <td>제목</td>
  </tr>
  <tr>
    <td>콘텐츠 전송 인코딩</td>
    <td>MIME 버전</td>
    <td>To</td>
  </tr>
  <tr>
    <td>콘텐츠 유형</td>
    <td>수신됨</td>
    <td>X-SG-EID</td>
  </tr>
  <tr>
    <td>DKIM-서명</td>
    <td>받은</td>
    <td>x-sg-ID</td>
  </tr>
</tbody>
</table>

##### 이메일 추가 추가하기

이메일 추가 기능을 사용하면 다른 이메일 서비스 제공업체에 추가 데이터를 다시 보낼 수 있습니다. 이는 진행 중인 사용 사례에만 적용되므로 회사에서 이미 이 기능을 설정한 경우에만 이메일 추가 기능을 사용해야 합니다.

이메일 추가 **정보를** 추가하려면 **전송 정보로** 이동하여 **새 추가 정보 추가를** 선택합니다.

{% alert warning %}
추가된 총 키-값 쌍은 1KB를 초과하지 않아야 합니다. 그렇지 않으면 메시징이 중단됩니다.
{% endalert %}

이메일 추가 값은 커런츠 또는 Snowflake에 게시되지 않습니다. 추가 메타데이터나 동적 값을 커런츠 또는 Snowflake에 보내려면 대신 [`message_extras`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/) 대신

### 3b단계: 메시지 미리보기 및 테스트하기

완벽한 이메일 작성을 완료한 후에는 발송하기 전에 테스트해야 합니다. 개요 화면 하단에서 **미리보기 및 테스트를** 선택합니다. 

여기에서 고객의 받은편지함에 이메일이 어떻게 표시될지 미리 볼 수 있습니다. **사용자로 미리 보기를** 선택하면 임의의 사용자로 이메일을 미리 보거나 특정 사용자를 선택하거나 커스텀 사용자를 만들 수 있습니다. 이를 통해 연결된 콘텐츠 및 개인화 호출이 정상적으로 작동하는지 테스트할 수 있습니다. 

그런 다음 **미리 보기 링크를 복사하여** 임의의 사용자에게 이메일이 어떻게 표시되는지 보여주는 공유 가능한 미리 보기 링크를 생성하고 복사할 수 있습니다. 링크는 7일 동안 지속되며 그 후 다시 생성해야 합니다.

또한 데스크톱, 모바일, 일반 텍스트 보기 간에 전환하여 메시징이 다양한 상황에서 어떻게 표시되는지 확인할 수 있습니다.

{% alert tip %}
다크 모드 사용자에게 이메일이 어떻게 보이는지 궁금하신가요? **미리보기 및 테스트** 섹션에 있는 **다크 모드 미리보기** 토글을 선택합니다(드래그 앤 드롭 편집기만 해당).
{% endalert %}

최종 확인이 완료되면 **테스트 전송을** 선택하고 본인 또는 콘텐츠 테스터 그룹에게 테스트 메시지를 보내 다양한 기기와 이메일 클라이언트에서 이메일이 제대로 표시되는지 확인합니다.

이메일 작성 시 테스트 보내기 옵션과 이메일 미리보기 예시를 확인하세요.]({% image_buster /assets/img_archive/newEmailTest.png %})

이메일에 문제가 있거나 변경하려는 사항이 있으면 **이메일 편집을** 선택하여 편집기로 돌아갑니다.

{% alert tip %}
미리 보기 텍스트를 지원하는 이메일 클라이언트는 항상 사용 가능한 모든 미리 보기 텍스트 공간을 채울 수 있는 충분한 문자를 가져옵니다. 그러나 이로 인해 미리보기 텍스트가 불완전하거나 최적화되지 않은 상황에 처할 수 있습니다.
<br><br>이를 방지하려면 원하는 미리보기 텍스트 뒤에 공백을 만들어 이메일 클라이언트가 다른 방해가 되는 텍스트나 문자를 봉투 콘텐츠로 끌어들이지 않도록 할 수 있습니다. 이렇게 하려면 표시하려는 미리보기 텍스트 뒤에 너비가 0인 비접속자(`&zwnj;`)와 끊어지지 않는 공백(`&nbsp;`)을 추가합니다. <br><br>프리헤더 섹션의 미리보기 텍스트 끝에 다음 HTML 편집기용 코드를 추가하면 원하는 공백을 추가할 수 있습니다:<br><br>

```html
<div style="display: none; max-height: 0px; overflow: hidden;">&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>
```
드래그 앤 드롭 편집기의 경우 **전송 설정** 섹션의 프리헤더에 `<div>` 서식 없이 너비가 0인 비조인자(`&zwnj;`)만 직접 추가합니다.

{% endalert %}

### 3c단계: 이메일 오류 확인

편집기는 메시지를 보내기 전에 메시지에서 발견한 문제를 알려줍니다. 다음은 편집기에서 설명하는 오류 목록입니다:

- **표시 이름과** **헤더를** 함께 지정하지 않은 **경우** 
- **보낸** 사람 및 **받는 사람** 주소가 잘못되었습니다.
- 중복 **헤더** 키
- Liquid 구문 문제
- 이메일 본문이 400KB를 초과하는 경우(본문은 [102KB보다 작게]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#email-size) 작성할 것을 적극 권장)
- **본문** 또는 **제목이** 비어 있는 이메일
- 탈퇴 링크가 없는 이메일
- 보내는 이메일이 허용 목록에 없습니다(전달 가능성을 보장하기 위해 전송이 매우 제한됩니다).

## 4단계: 나머지 캠페인 또는 캔버스 구축하기

{% tabs %}
{% tab Campaign %}
이제 나머지 캠페인을 구축하세요! 다음 섹션에서 도구를 사용하여 이메일 캠페인을 구축하는 방법에 대한 자세한 내용을 확인하세요.

#### 전달 일정 또는 트리거 선택

이메일은 예약된 시간, 동작 또는 API 트리거에 따라 전달될 수 있습니다. 자세한 내용은 [캠페인 예약하기를]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/) 참조하세요.

{% alert note %}
API 트리거 캠페인의 경우 트리거 동작이 **캠페인과 상호** 작용으로 설정된 경우 상호 작용으로 **수신** 옵션을 선택하면 메시지가 반송되거나 전달되지 않더라도 Braze에서 선택한 캠페인을 보낸 것으로 표시하는 즉시 새 캠페인이 트리거됩니다.
{% endalert %}

캠페인 기간을 설정하고, [방해금지 시간을]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) 지정하고, [최대 게재빈도 제한]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) 규칙을 설정할 수도 있습니다.

#### 타겟팅할 사용자 선택하기

다음으로 세그먼트 또는 필터를 선택하여 오디언스 범위를 좁혀 [사용자를 타겟팅해야]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) 합니다. 이메일을 통해 도달할 수 있는 세그먼트 내 사용자 수를 포함하여 현재 해당 세그먼트 인구가 어떻게 보이는지 자동으로 미리 볼 수 있습니다. 정확한 세그먼트 멤버십은 항상 메시지 전송 직전에 계산된다는 점에 유의하세요.

{% multi_lang_include target_audiences.md %}

또한 이메일에 가입하고 옵트인한 사용자 등 특정 [가입 상태를]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) 가진 사용자에게만 캠페인을 보내도록 선택할 수도 있습니다.

선택적으로 메시지 세그먼트 내에서 지정된 수의 사용자로만 전달을 제한하거나 캠페인이 반복될 때 사용자가 동일한 메시지를 두 번 수신하도록 허용할 수도 있습니다.

##### 이메일과 푸시를 활용한 멀티채널 캠페인

이메일과 푸시 채널을 모두 타겟팅하는 멀티 채널 메시징 캠페인의 경우 명시적으로 옵트인한 사용자만 메시지를 받도록 캠페인을 제한할 수 있습니다(가입하거나 탈퇴한 사용자 제외). 예를 들어 옵트인 상태가 서로 다른 세 명의 사용자가 있다고 가정해 보겠습니다:

- **사용자 A는** 이메일에 가입하고 푸시 인에이블먼트가 되어 있습니다. 이 사용자는 이메일을 수신하지 않지만 푸시는 받게 됩니다.
- **사용자 B는** 이메일에 옵트인되어 있지만 푸시 인에이블먼트가 되어 있지 않습니다. 이 사용자는 이메일은 수신하지만 푸시는 받지 않습니다.
- **사용자 C는** 이메일에 옵트인되어 있으며 푸시 인에이블먼트가 설정되어 있습니다. 이 사용자는 이메일과 푸시를 모두 받게 됩니다.

이렇게 하려면 **오디언스 요약에서**'옵트인한 사용자에게만' 이 캠페인을 보내도록 선택합니다. 이 옵션을 선택하면 옵트인한 사용자만 이메일을 수신하도록 설정되며, Braze는 기본값으로 푸시를 인에이블먼트한 사용자에게만 푸시를 보냅니다.

{% alert important %}
이 구성에서는 오디언스를 단일 채널(예: `Foreground Push Enabled = True` 또는 `Email Subscription = Opted-In`)로 제한하는 필터를 **타겟 오디언스** 단계에 포함하지 마세요.
{% endalert %}

#### 전환 이벤트 선택하기

Braze를 사용하면 사용자가 캠페인을 수신한 후 특정 액션, [전환 이벤트를]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) 얼마나 자주 수행하는지 추적할 수 있습니다. 다음 작업 중 하나를 전환 이벤트로 지정할 수 있습니다:

- 앱 열기
- 구매(일반 구매 또는 특정 품목일 수 있음)
- 특정 커스텀 이벤트 수행
- 이메일 열기

사용자가 지정된 작업을 수행하면 전환이 카운트되는 기간을 최대 30일까지 허용할 수 있습니다. Braze는 캠페인의 열기 및 클릭을 자동으로 추적하지만, [지능형 선택을]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) 활용하기 위해 사용자가 이메일 주소를 열거나 클릭할 때로 전환 이벤트를 설정할 수 있습니다.
{% endtab %}

{% tab Canvas %}
아직 완료하지 않았다면 캔버스 구성 요소의 나머지 섹션을 완료하세요. 나머지 캔버스를 구축하고, 다변량 테스트 및 지능형 선택을 구현하는 방법 등에 대한 자세한 내용은 캔버스 설명서의 캔버스 [구축]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) 단계를 참조하세요.
{% endtab %}
{% endtabs %}

## 5단계: 검토 및 배포

마지막 섹션에서는 방금 디자인한 캠페인에 대한 요약이 제공됩니다. 관련 세부 정보를 모두 확인한 후 **캠페인 시작을** 선택합니다. 이제 모든 데이터가 들어올 때까지 기다릴 시간입니다! 

이메일 캠페인 결과에 액세스하는 방법을 알아보려면 [이메일 보고를]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/) 확인하세요.

