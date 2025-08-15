---
nav_title: 테스트 메시지 보내기
article_title: 테스트 메시지 보내기
page_order: 0
tool: 
  - Campaigns
page_type: reference
description: "이 참고 문서에서는 다양한 Braze 채널에서 테스트 메시지를 보내는 방법과 커스텀 이벤트 속성정보 또는 사용자 속성을 통합하는 방법에 대해 설명합니다."

---

# 테스트 메시지 보내기

> 사용자에게 메시징 캠페인을 보내기 전에 모범 사례로, 메시징 캠페인이 제대로 표시되고 의도한 대로 작동하는지 테스트하는 것이 좋습니다. Braze 대시보드의 도구를 사용하여 테스트 메시지를 생성하고 선택한 기기 또는 팀원에게 보낼 수 있습니다.

{% alert important %}
캠페인이 삭제되지 않도록 테스트 후 캠페인 초안을 저장해야 합니다. 메시지를 초안으로 저장하지 않고 테스트 메시지를 보낼 수 있습니다.
{% endalert %}

## 1단계: 테스트 사용자 식별

메시징 캠페인을 테스트하기 전에 테스트 사용자를 식별하는 것이 중요합니다. 이러한 사용자는 기존 사용자 ID 또는 이메일 주소이거나 메시징 캠페인 테스트 전용으로 사용되는 새 사용자일 수 있습니다. 

### 선택 사항: 콘텐츠 테스트 그룹 만들기

A convenient way to organize your test users is by creating a [Content Test Group]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/), which includes a group of users that will receive test messages from campaigns. 캠페인의 **테스트 대상자** 아래의 **콘텐츠 테스트 그룹 추가** 필드에 이 테스트 그룹을 추가하고 개별 테스트 사용자를 만들거나 추가하지 않고도 테스트를 시작할 수 있습니다.

## 2단계: 채널별 테스트 메시지 보내기

테스트 메시지를 보내는 단계는 각 채널의 다음 섹션을 참조하세요.

{% tabs %}
{% tab 이메일 %}

1. 이메일 메시지 초안을 작성합니다.
2. **미리보기 및 테스트**를 클릭합니다.
3. **테스트 보내기** 탭을 선택하고 **개별 사용자 추가** 필드에 이메일 주소 또는 사용자 ID를 추가합니다. 
4. **테스트 보내기**를 클릭하여 초안 이메일을 받은편지함으로 보냅니다.

![테스트 이메일]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

{% endtab %}
{% tab 푸시 %}

#### 모바일 푸시

1. 모바일 푸시 초안을 작성하세요.
2. **설정** 탭을 선택하고 **개별 사용자 추가** 필드에 이메일 주소 또는 사용자 아이디를 추가합니다.
3. **테스트 보내기**를 클릭하여 작성된 메시지를 기기로 보냅니다.

![테스트 푸시]({% image_buster /assets/img_archive/testpush.png %})

#### 웹 푸시

1. 웹 푸시를 만듭니다.
2. **테스트** 탭을 선택합니다. 
3. **나에게 테스트 발송**를 확인합니다.
4. **테스트 보내기를** 클릭하여 웹 푸시를 웹 브라우저로 전송합니다.

![웹 푸시 테스트]({% image_buster /assets/img_archive/testwebpush.png %})

Braze 대시보드에서 이미 푸시 메시지를 수락한 경우, 화면 모서리에 푸시가 표시됩니다. 그렇지 않으면 메시지가 표시되면 **허용**을 클릭합니다.

{% endtab %}
{% tab 인앱 메시지 %}

앱과 테스트 디바이스에 푸시 알림을 설정한 경우 앱에 테스트 인앱 메시지를 전송하여 실시간으로 어떤 모습인지 확인할 수 있습니다. 

1. 인앱 메시지 초안을 작성하세요.
2. **테스트** 탭을 선택하고 **개별 사용자 추가** 필드에 이메일 주소 또는 사용자 ID를 추가합니다. 
3. **테스트 보내기**를 클릭하여 푸시 메시지를 기기로 전송합니다.

디바이스 화면 상단에 테스트 푸시 메시지가 표시됩니다.

![앱에서 테스트]({% image_buster /assets/img_archive/test-in-app.png %})

푸시 메시지를 직접 클릭하고 열면 앱으로 이동하여 인앱 메시지 테스트를 확인할 수 있습니다. 이 인앱 메시지 테스트 기능은 사용자가 테스트 푸시 알림을 클릭하여 인앱 메시지를 트리거하는 데 의존한다는 점에 유의하세요. 따라서 테스트 푸시 알림을 성공적으로 전달하려면 사용자가 해당 앱에서 푸시 알림을 수신할 수 있는 자격이 있어야 합니다.

#### 문제 해결

* 인앱 메시지 캠페인이 푸시 캠페인에 의해 트리거되지 않는 경우, 인앱 캠페인 세그먼테이션을 확인하여 사용자가 푸시 메시지를 받기 **전에** 타겟 오디언스를 충족하는지 확인하세요.
* Android 및 iOS에서 테스트 전송의 경우, **푸시 권한 요청** 온클릭 동작을 사용하는 인앱 메시지가 일부 디바이스에서 표시되지 않을 수 있습니다. 해결 방법:
  * **Android:** 기기는 Android 13 및 Android SDK 버전 21.0.0을 사용 중이어야 합니다. 또 다른 이유는 인앱 메시지가 표시되는 기기에 이미 시스템 수준의 프롬프트가 있기 때문일 수 있습니다. **다시 묻지 않음**을 선택했을 수 있으므로 다시 테스트하기 전에 앱을 다시 설치하여 알림 권한을 재설정해야 할 수 있습니다.
  * **iOS:** 개발자 팀에서 앱의 푸시 알림 구현을 검토하고 푸시 권한을 요청하는 코드를 수동으로 제거할 것을 권장합니다. 자세한 내용은 [푸시 프라이머 인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)를 참조하세요.
* 액션 기반 인앱 메시지 캠페인을 전달하려면 커스텀 이벤트가 REST API가 아닌 Braze SDK를 통해 로깅되어야 사용자가 적격 인앱 메시지를 기기로 직접 수신할 수 있습니다. 사용자는 세션 중에 이벤트를 수행하면 인앱 메시지를 받을 수 있습니다.

{% endtab %}
{% tab 콘텐츠 카드 %}

콘텐츠 카드를 만든 후 테스트 콘텐츠 카드를 앱에 전송하여 실시간으로 어떻게 표시되는지 확인할 수 있습니다.

1. 콘텐츠 카드 초안을 작성합니다.
2. **테스트** 탭을 선택하고 이 테스트 메시지를 수신할 콘텐츠 테스트 그룹 또는 개별 사용자를 하나 이상 선택합니다. 
3. **테스트 보내기**를 클릭하여 콘텐츠 카드를 앱으로 전송합니다.

![콘텐츠 카드 테스트]({% image_buster /assets/img/contentcard_test.png %})

{% endtab %}
{% tab SMS/MMS %}

SMS 또는 MMS 메시지를 작성한 후 휴대폰으로 테스트 메시지를 전송하여 실시간으로 어떻게 표시되는지 확인할 수 있습니다. 

1. SMS 또는 MMS 메시지 초안을 작성합니다.
2. **테스트** 탭을 선택하고 이 테스트 메시지를 수신할 콘텐츠 테스트 그룹 또는 개별 사용자를 하나 이상 선택합니다. 
3. 테스트 메시지를 보내려면 테스트 **보내기**를 클릭합니다.

![콘텐츠 카드 테스트]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab 웹훅 %}

웹훅을 만든 후 테스트 전송을 수행하여 웹훅 응답을 확인할 수 있습니다. **테스트** 탭을 선택하고 **테스트 발송**을 선택하여 제공된 웹훅 URL로 테스트 전송을 보냅니다. 개별 사용자를 선택하여 특정 사용자로 응답을 미리 볼 수도 있습니다. 

![콘텐츠 카드 테스트]({% image_buster /assets/img/webhook_test.png %})

{% endtab %}
{% tab 뉴스 피드 %}

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

테스트 뉴스피드 카드를 보내려면 테스트 세그먼트를 설정한 후 테스트 캠페인을 보내야 합니다.

##### 1단계: 지정된 테스트 세그먼트 만들기

테스트 세그먼트를 설정한 후에는 이러한 메시징 채널을 사용할 수 있습니다. 이 과정은 몇 가지 간단한 단계를 거치며, 올바르게 구성한 경우 한 번만 수행하면 됩니다.

1. **세그먼트** 페이지로 이동하여 [새 세그먼트를 만듭니다]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/). 
2. **필터 추가** 아래의 드롭다운 메뉴를 클릭하고 목록 하단에서 테스트 필터를 찾습니다. <br><br>![필터 테스트]({% image_buster /assets/img_archive/testmessages1.png %})<br><br>
3. Use the testing filters to select users with specific email addresses or external [user IDs]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=swift).<br><br>![필터 옵션 테스트]({% image_buster /assets/img_archive/testmessages2.png %})
<br><br>이러한 필터에는 다음과 같은 옵션이 있습니다:
- **동등함**: 제공한 이메일 또는 사용자 아이디와 정확히 일치하는 것을 찾습니다. 단일 이메일 또는 사용자 ID와 연결된 기기로만 테스트 캠페인을 보내려는 경우 이 옵션을 사용합니다.
- **동등하지 않음**: 특정 이메일 또는 사용자 ID를 테스트 캠페인에서 제외합니다.
- **일치**: 입력한 검색어의 일부와 일치하는 이메일 주소 또는 사용자 아이디를 가진 사용자를 찾습니다. 이를 사용하여 "@yourcompany.com" 주소를 가진 사용자만 찾아서 팀원 모두에게 메시지를 보낼 수 있습니다.
<br><br>
이러한 필터를 함께 사용하여 테스트 사용자 목록의 범위를 좁힐 수도 있습니다. 예를 들어 테스트 세그먼트에는 `matches` "@braze.com"이라는 이메일 주소 필터와 `does not equal` "sales@braze.com"이라는 또 다른 필터가 포함될 수 있습니다. `matches` 옵션을 사용하고 이메일 주소를 "|" 문자로 구분하여 여러 개의 특정 이메일을 선택할 수도 있습니다(예: `matches` "email1@braze.com|email2@braze.com").
<br><br>
4. 테스트 세그먼트에 테스트 필터를 추가합니다.
5. 세그먼트 편집기 상단의 **미리 보기**를 클릭하거나 해당 세그먼트의 사용자 데이터를 CSV로 내보내서 의도한 사용자만 선택했는지 확인합니다.
6. **사용자 데이터** 드롭다운을 클릭하고 **모든 사용자 데이터 CSV 내보내기**를 선택하여 세그먼트 사용자 데이터를 내보냅니다. 

![테스트 세그먼트 확인]({% image_buster /assets/img_archive/testmessages3.png %})

> 세그먼트의 사용자 데이터를 CSV로 내보내면 해당 세그먼트에 속하는 사람을 가장 정확하게 파악할 수 있습니다. **미리보기** 탭은 세그먼트에 있는 사용자의 샘플일 뿐이므로 의도한 모든 구성원을 선택하지 않은 것처럼 보일 수 있습니다. 자세한 내용은 [세그먼트 데이터 보기 및 이해][7]를 참조하세요.

테스트 메시지를 수신하려는 사용자만 타겟팅하고 있는지 확인한 후 테스트하려는 기존 캠페인에서 이 세그먼트를 선택하거나 세그먼트 메뉴에서 **캠페인 시작** 버튼을 클릭할 수 있습니다.

##### 2단계: 테스트 캠페인 보내기

테스트 뉴스피드 카드를 보내려면 이전에 만든 테스트 세그먼트를 타겟팅해야 합니다. 멀티채널 캠페인을 생성하고 일반적인 단계를 따라 시작하세요. **타겟 사용자** 단계에 도달하면 다음 이미지와 같이 테스트 세그먼트를 선택합니다.

![테스트 세그먼트]({% image_buster /assets/img_archive/test_segment.png %})

캠페인 확인을 완료하고 캠페인을 실행하여 뉴스피드 카드를 테스트합니다.

> 하나의 캠페인을 사용하여 자신에게 테스트 메시지를 두 번 이상 보내려면 캠페인 작성기의 **일정** 부분에서 '사용자가 캠페인을 다시 받을 수 있도록 허용'이라는 제목의 확인란을 선택합니다.

{% endtab %}
{% endtabs %}

## 개인화된 캠페인 테스트 

사용자 데이터를 채우거나 사용자 지정 이벤트 속성을 사용하는 캠페인을 테스트하는 경우 추가 또는 다른 단계를 수행해야 합니다.

### 사용자 속성으로 맞춤화된 캠페인 테스트

메시지에서 [개인화][26]를 사용하는 경우 캠페인을 제대로 미리 보고 사용자 데이터가 콘텐츠를 제대로 채우고 있는지 확인하기 위해 추가 단계를 수행해야 합니다.

테스트 메시지를 보낼 때 **기존 사용자 선택** 또는 **사용자 지정 사용자로** 미리 보기 옵션 중 하나를 선택해야 합니다.

![개인화된 메시지 테스트][23]{: style="max-width:70%;" }

#### 기존 사용자 선택하기

기존 사용자를 선택하는 경우 검색 필드에 특정 사용자 ID 또는 이메일을 입력합니다. 그런 다음 대시보드 미리 보기를 사용하여 해당 사용자에게 메시지가 어떻게 표시되는지 확인하고 해당 사용자에게 표시되는 내용을 반영한 테스트 메시지를 장치로 보냅니다.

![사용자 선택][24]

#### 사용자 지정 사용자 선택하기

사용자 지정 사용자로 미리 보는 경우 사용자의 이름 및 사용자 지정 속성 등 개인화에 사용할 수 있는 다양한 필드에 대한 텍스트를 입력합니다. 다시 한 번 자신의 이메일 주소를 입력하여 기기로 테스트를 보낼 수 있습니다.

![사용자 지정 사용자][25]

### 사용자 지정 이벤트 속성으로 개인화된 캠페인 테스트

커스텀 이벤트 속성정보][19]로 개인화된 캠페인을 테스트하는 것은 설명한 다른 유형의 캠페인을 테스트하는 것과 약간 다릅니다. 사용자 지정 이벤트 속성을 사용하여 개인화된 캠페인을 테스트하는 가장 강력한 방법은 다음을 수행하여 캠페인을 직접 트리거하는 것입니다:

1. 이벤트 속성과 관련된 사본을 작성합니다. ![속성을 사용하여 테스트 메시지 작성][15]
2. 이벤트 발생 시 [실행 기반 전달][21]을 사용하여 캠페인을 전달합니다.

{% alert note %}
iOS 푸시 캠페인을 테스트하는 경우, iOS는 현재 열려 있는 앱에 대한 푸시 알림을 제공하지 않으므로 앱을 종료할 시간을 확보하기 위해 지연 시간을 1분으로 설정해야 합니다. 다른 유형의 캠페인은 즉시 전달되도록 설정할 수 있습니다.
{% endalert %}

![메시지 전달 테스트][16]

{: start="3"}
3\. 테스트 필터를 사용하거나 자신의 이메일 주소를 타겟팅하여 테스트할 때와 마찬가지로 사용자를 타겟팅하고 캠페인 생성을 완료합니다. 

![메시지 타겟팅 테스트][17]

{: start="4"}
4\. 앱으로 이동하여 사용자 지정 이벤트를 완료합니다.

캠페인이 트리거되고 이벤트 속성으로 맞춤 설정된 메시지가 표시됩니다.

![테스트 메시지 예제][18]

또는 사용자 지정 사용자 아이디를 저장하는 경우 자신에게 사용자 지정 테스트 메시지를 전송하여 캠페인을 테스트할 수도 있습니다.

1. 캠페인에 사용할 카피를 작성합니다.
2. **테스트** 탭을 선택하고 **커스텀 사용자**를 선택합니다. 
3. 페이지 하단에 사용자 지정 이벤트 속성을 추가하고 상단 상자에 사용자 아이디 또는 이메일 주소를 추가합니다.
4. **테스트 보내기를** 클릭하면 숙소와 맞춤 설정된 메시지를 받을 수 있습니다.

![사용자 지정 사용자를 사용한 테스트][22]

[7]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#user-preview
[13]: {% image_buster /assets/img_archive/test-push-for-in-app.png %}
[15]: {% image_buster /assets/img_archive/testeventproperties-compose.png %}
[16]: {% image_buster /assets/img_archive/testeventproperties-delivery.png %}
[17]: {% image_buster /assets/img_archive/testeventproperties-target.png %}
[18]: {% image_buster /assets/img_archive/testeventproperties-message.PNG %}
[19]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#custom-event-properties
[20]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[21]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/
[22]: {% image_buster /assets/img_archive/testeventproperties-customuser.png %}
[23]: {% image_buster /assets/img_archive/personalized_testing.png %}
[24]: {% image_buster /assets/img_archive/personalized_testing_select.png %}
[25]: {% image_buster /assets/img_archive/personalized_testing_custom.png %}
[26]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/
