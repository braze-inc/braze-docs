---
nav_title: Facebook
article_title: Facebook 오디언스 내보내기
alias: /partners/facebook/
description: "이 참고 문서에서는 브랜드가 고객에게 다가가고 고객과 소통할 수 있는 선도적인 소셜 플랫폼인 Braze와 Facebook의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Facebook 오디언스 내보내기

> Braze와 Facebook 통합을 사용하면 Braze 세그먼트를 Facebook으로 수동으로 내보내 Facebook 맞춤 오디언스를 생성할 수 있습니다. 이 기능은 일회성 정적 오디언스 내보내기이며 새로운 Facebook 커스텀 오디언스만 생성합니다.

Facebook 커스텀 오디언스를 내보내는 일반적인 사용 사례로 다음이 포함됩니다.
- 생애주기 내 특정 시점에 사용자 리타겟팅
- 제외 타겟팅 목록 생성
- 새로운 사용자를 더 효율적으로 확보하기 위해 [유사 오디언스][4] 생성
<br><br>

{% alert note %}
Facebook 오디언스 내보내기는 **사용자 액세스 토큰**을 사용하여 요청에 권한을 부여합니다.<br><br>
[Facebook에 오디언스 동기화]({{site.baseurl}}/audience_sync_facebook/) 기능과 함께 이 기능을 사용하는 경우, Braze는 기본적으로 사용자가 이미 생성한 보다 안정적인 **시스템 사용자 토큰**을 사용하여 요청에 대한 권한을 부여합니다.
{% endalert %}

{% alert note %}
베타 버전의 Meta Work 계정 테스트에 참여 중인 경우, [Facebook 파트너 페이지]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync#step-1-connect-to-facebook)에서 계정 연결을 끊었다가 다시 연결해야 합니다.
{% endalert %}

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| [Facebook 비즈니스 관리자][1] | 브랜드의 Facebook 자산(예: 광고 계정, 페이지, 앱)을 관리할 수 있는 중앙 집중식 도구입니다. |
| [Facebook 광고 계정][2] | 브랜드의 비즈니스 관리자와 연결된 활성 Facebook 광고 계정으로, Braze 맞춤 오디언스와 함께 사용하려는 계정입니다.<br><br>Facebook 비즈니스 매니저 관리자가 Braze에서 사용하려는 Facebook 광고 계정에 대한 관리자 권한을 부여하고 광고 계정 이용약관에 동의했는지 확인합니다. 그렇지 않으면 Braze 내에서 Facebook 광고 계정에 액세스할 수 없습니다. |
| [Facebook 커스텀 오디언스 약관][3]| Braze와 함께 사용하려는 Facebook 광고 계정에 대해 Facebook의 맞춤 타겟 약관에 동의해야 합니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: Facebook에 연결

1. Braze 대시보드에서 **파트너 통합** > **기술 파트너**로 이동하여 **Facebook**을 선택합니다. 

{: start="2"}
2\. Facebook 오디언스 내보내기 모듈에서 **Facebook 연결**을 클릭합니다. <br><br>![Braze 플랫폼의 Facebook 기술 파트너 페이지.][6]{: style="max-width:70%;"}

{: start="3"}
3\. Facebook oAuth 대화 상자 창에서 Facebook 광고 계정에 커스텀 오디언스를 생성할 수 있도록 Braze에 권한을 부여합니다. <br><br>!["X로 연결"이라는 메시지가 표시되는 첫 번째 페이스북 대화상자(여기서 X는 페이스북 사용자 아이디)가 나타납니다.][8]{: style="max-width:30%;"}  ![광고 계정에 대한 광고 관리 권한을 묻는 두 번째 Facebook 대화 상자입니다.][7]{: style="max-width:40%;"}

{: start="4"}
4\. Braze를 Facebook 계정에 연결한 후, Braze 워크스페이스 내에서 동기화할 광고 계정을 선택합니다. <br><br>![Facebook에 연결할 수 있는 사용 가능한 광고 계정 목록입니다.][9]{: style="max-width:70%;"}<br><br> 연결하면 파트너 페이지로 돌아가서 어떤 계정이 연결되어 있는지 확인하고 기존 계정의 연결을 해제할 수 있습니다. <br><br> ![Facebook 기술 파트너 페이지의 업데이트된 버전으로 광고 계정이 성공적으로 연결되었음을 보여줍니다.][10]{: style="max-width:70%;"}<br>
<br> Facebook 연결은 Braze 워크스페이스 수준에서 적용됩니다. 페이스북 관리자가 사용자를 페이스북 비즈니스 관리자에서 삭제하거나 연결된 페이스북 계정에 대한 액세스 권한을 제거하면 Braze는 유효하지 않은 토큰을 감지합니다. 결과적으로 Facebook 오디언스 단계를 사용하는 활성 캔버스에 오류가 표시되고 Braze에서 사용자를 동기화할 수 없게 됩니다. 

{% alert important %}
이전에 [광고 관리](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) 및 [광고 관리 표준 액세스](https://developers.facebook.com/docs/marketing-api/access#standard)에 대한 Facebook 앱 검토 절차를 거친 고객의 경우, 시스템 사용자 토큰은 Facebook 오디언스 단계에서 계속 유효합니다. Facebook 파트너 페이지를 통해 Facebook 시스템 사용자 토큰을 수정하거나 취소할 수 없습니다. 대신 Facebook 계정을 연결하여 Braze 워크스페이스 내에서 Facebook 시스템 사용자 토큰을 대체할 수 있습니다. 

<br><br>새로운 Facebook oAuth 구성은 [세그먼트를 통한 Facebook 내보내기]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites)에도 적용됩니다.
{% endalert %}

### 2단계: Facebook으로 사용자 내보내기

Braze에서 Facebook 오디언스 내보내기는 **세그먼트** 페이지를 통해 액세스할 수 있습니다. 

1. **세그먼트** 페이지에서 내보내려는 세그먼트를 선택합니다.
2. **사용자 데이터를** 선택한 다음 **Facebook 오디언스로 내보내기를** 선택합니다. <br><br>!['사용자 데이터'가 선택된 세그먼트의 '세그먼트 세부 정보' 섹션에 'Facebook 오디언스로 내보내기'를 포함한 옵션 드롭다운이 표시됩니다.][11]

{: start="3"}
3\. 아직 Braze 내에서 Facebook을 활성화하지 않았다면 대시보드의 Facebook 기술 파트너 페이지로 이동하라는 프롬프트가 표시됩니다. **기술 파트너** > **Facebook을** 통해 이미 Facebook을 활성화한 경우, 내보낼 Facebook 광고 계정과 사용자 필드를 선택할 수 있습니다. <br><br> 내보낼 수 있는 사용자 필드는 세 가지가 있습니다:
- 기기 IDFA
- 전화번호 
- 이메일

{% alert note %}
한 번의 내보내기에서 하나의 사용자 필드만 선택할 수 있습니다. 데이터 유형을 두 개 이상 선택하면 Braze는 각각에 대해 별도의 커스텀 오디언스를 생성합니다.
{% endalert %}

{: start="4"}
4\. 사용자 필드를 선택한 후 **세그먼트 내보내기를** 선택합니다. CSV 내보내기와 마찬가지로 세그먼트의 Facebook으로 내보내기가 완료되면 이메일을 수신합니다.
5\. [Facebook 광고 매니저][13]에서 커스텀 오디언스를 확인합니다.

{% alert important %}
사용자 개인정보 보호 정책으로 인해 Facebook은 사용자가 다음 정보를 보도록 허용하지 않습니다.

- 사용자 지정 대상에 성공적으로 추가된 정확한 사용자 수입니다. [자세히 알아보기.](https://www.facebook.com/business/help/112061095610075)
- 커스텀 오디언스 크기. [자세히 알아보기.](https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923)
{% endalert %}

#### 대상 내보내기 구성

Facebook 오디언스를 구축할 때 선호도에 따라 특정 사용자를 포함하거나 제외할 수 있으며, [CCPA에](https://oag.ca.gov/privacy/ccpa) 따른 '판매 또는 공유 금지' 권한과 같은 개인정보 보호법을 준수하기 위해 특정 사용자를 포함하거나 제외할 수 있습니다. 마케터는 캔버스 진입 기준 내에서 사용자의 자격에 맞는 관련 필터를 구현해야 합니다. 아래에는 몇 가지 옵션이 나와 있습니다. 

- [Braze SDK를 통해 iOS IDFA]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection)를 수집한 경우, **광고 추적 사용** 필터를 사용할 수 있습니다. 값을 `true`로 선택하면 사용자가 옵트인한 오디언스 동기화 대상으로만 사용자를 보낼 수 있습니다. 

![][16]{: style="max-width:75%;"}

- 옵트인, 옵트아웃, `Do Not Sell Or Share` 또는 기타 관련 커스텀 속성을 수집하는 경우 캔버스 진입 기준에 필터로 포함해야 합니다: 

![항목 대상 그룹이 "opted_in_marketing"인 캔버스는 "true"와 같습니다.][15]{: style="max-width:75%;"}


#### 유사 오디언스

세그먼트를 Facebook 오디언스로 성공적으로 내보낸 후에는 Facebook [유사 오디언스][4]를 사용하여 추가 그룹을 생성할 수 있습니다. 이 기능은 선택한 오디언스의 인구 통계, 관심사 및 기타 속성을 살펴보고 유사한 속성을 가진 사람으로 구성된 새로운 오디언스를 생성합니다.

[1]: https://www.facebook.com/business/help/113163272211510?id=180505742745347
[2]: https://www.facebook.com/business/help/910137316041095?id=420299598837059
[3]: https://www.facebook.com/ads/manage/customaudiences/tos.php
[4]: https://www.facebook.com/business/help/164749007013531?id=401668390442328
[6]: {% image_buster /assets/img/fb/afb_1.png %}
[7]: {% image_buster /assets/img/fb/afb_2.png %}
[8]: {% image_buster /assets/img/fb/afb_3.png %}
[9]: {% image_buster /assets/img/fb/afb_4.png %}
[10]: {% image_buster /assets/img/fb/afb_5.png %}
[11]: {% image_buster /assets/img/fb/afb_6.png %}
[13]:https://www.facebook.com/ads/manager/audiences/manage/
[15]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
