---
nav_title: Facebook Lead Ads via Zapier
article_title: Facebook Lead Ads via Zapier
description: "이 참조 문서에서는 Zapier를 통해 Braze와 Facebook 리드 광고를 통합하여 Facebook에서 Braze로 리드 데이터를 자동으로 전송하여 실시간 참여와 개인화된 후속 조치를 가능하게 하는 방법에 대해 설명합니다."
alias: /partners/facebook_via_zapier/
page_type: partner
search_tag: Partner

---

# Zapier 통합을 통한 Facebook 리드 광고

> <a href="https://zapier.com/" target="_blank">Zapier를</a> 통한 Facebook 리드 광고 통합을 사용하면 Facebook에서 Braze로 리드를 가져오고 리드가 캡처되면 사용자 지정 이벤트를 추적할 수 있습니다. 

Facebook 리드 광고는 비즈니스가 Facebook에서 직접 리드 정보를 수집할 수 있는 광고 형식입니다. 이러한 광고는 리드 생성 프로세스를 쉽고 원활하게 진행할 수 있도록 설계되었습니다. Zapier와 Braze의 통합을 활용하면, Facebook에서 Braze로 리드 데이터를 자동 전송하여 실시간 인게이지먼트 및 개인화된 후속 작업을 수행할 수 있습니다. 

## 필수 조건

| 요구 사항 | 설명 |
|---|---|
| Zapier 계정 | 이 파트너십을 이용하려면 Zapier 계정이 필요합니다. 이 통합을 사용하려면 <a href="https://zapier.com/app/pricing/" target="_blank">프리미엄 Zapier 앱</a>을 사용해야 하므로 현재 Zapier 요금제에 프리미엄 앱에 대한 액세스 권한이 있는지 확인합니다. |
| <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862/" target="_blank">Facebook 리드 액세스</a> | Braze에서 사용하려는 광고 계정마다 Facebook 리드 액세스 권한이 필요합니다. |
| <a href="https://www.facebook.com/business/help/1710077379203657?id=180505742745347" target="_blank">Facebook 비즈니스 관리자</a> | 이 통합의 일환으로 브랜드의 Facebook 자산(예: 광고 계정, 페이지, 앱)을 관리하는 중앙 집중식 툴인 Facebook 비즈니스 매니저를 사용합니다. |
| <a href="https://www.facebook.com/business/help/195296697183682?id=829106167281625/" target="_blank">Facebook 광고 계정</a> | 브랜드의 비즈니스 매니저와 연결된 활성 Facebook 광고 계정이 필요합니다. <br><br>Braze에서 사용하려는 각 광고 계정에 대해 '광고 계정 관리' 권한이 있는지, 광고 계정 이용약관에 동의했는지 확인합니다. |
| <a href="https://www.facebook.com/business/help/183277585892925?id=420299598837059/" target="_blank">페이스북 페이지</a> | 브랜드의 비즈니스 매니저와 연결된 활성 Facebook 페이지가 필요합니다. <br><br>Braze에서 사용하려는 각 Facebook 페이지에 대해 '페이지 관리' 권한이 있는지 확인합니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL][1]을 알고 있는지 확인합니다. API 엔드포인트가 Braze 인스턴스의 대시보드 URL과 일치합니다. <br><br> 예를 들어 대시보드 URL이 `https://dashboard-03.braze.com`인 경우 엔드포인트는 `dashboard-03`입니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키가 있는지 확인합니다. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: 즉석 양식으로 리드 광고 캠페인 만들기

Facebook 광고 관리자에서 <a href="https://www.facebook.com/business/help/397336587121938?id=735435806665862&helpref=uf_permalink" target="_blank">Facebook 리드 캠페인과 Facebook 리드 광고 양식을</a> 만듭니다.

[`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)에 대한 요청을 수행할 때 이메일 주소 또는 전화번호를 사용하여 고객 프로필을 업데이트하거나 생성할 수 있습니다. 따라서 리드 광고 양식에 **이메일**이나 **전화**를 입력할 수 있는 **연락처 필드**를 포함하세요. 이름이나 성을 수집하는 경우에는 전체 이름을 사용하는 대신 양식에서 별도로 수집하세요.

### 2단계: 페이스북 계정을 Zapier에 연결 

#### 2a단계: Zapier에서 연결 방법 선택

Zapier에서 **앱으로** 이동하여 사용 가능한 Facebook 앱을 검색합니다. **Facebook 리드 광고** 또는 **Facebook 리드 광고(비즈니스 관리자용)**를 선택합니다.

Facebook 계정을 Zapier에 연결하는 이 두 가지 방법에 대한 자세한 내용은 다음을 참조하세요:

- <a href="https://help.zapier.com/hc/en-us/articles/8496123584781-How-to-get-started-with-Facebook-Lead-Ads-for-Business-Admins-on-Zapier#h_01HC9VZFZG0GR2KRYM5EQJN329" target="_blank">Facebook 리드 광고(비즈니스 관리자용)</a>
- <a href="https://help.zapier.com/hc/en-us/articles/8496061306253#h_01HC9VMZ2XP0017AR6SE7S30JG" target="_blank">Facebook 리드 광고</a>

![][2]{: style="max-width:80%;"}

#### 2b단계: Facebook 비즈니스 매니저에서 리드 액세스 권한에 Zapier 추가

Facebook 비즈니스 매니저의 왼쪽 메뉴에서 **연동** > **리드 액세스로** 이동합니다. Facebook 페이지를 선택한 다음 **CRM을** 클릭합니다. CRM 탭에서 **CRM 할당**을 선택하고 **Zapier**를 추가합니다.

![][3]{: style="max-width:80%;"}

Zapier를 CRM 통합으로 할당하는 단계는 Facebook <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862" target="_blank">설명서</a>를 참조하세요.

### 3단계: Zap 만들기

#### 3a단계: 트리거 만들기 

Facebook 계정을 연결한 후 Zap 생성을 진행할 수 있습니다. **트리거**의 경우 2단계에서 선택한 내용에 따라 **Facebook 리드 광고** 또는 **Facebook 리드 광고(비즈니스 관리자용)**를 선택합니다. 

![][4]{: style="max-width:80%;"}

**이벤트**의 경우 **새 리드** > **계속**을 선택합니다. 

![][5]{: style="max-width:80%;"}

Facebook 계정을 선택한 다음 **계속을** 클릭합니다. 

![][6]{: style="max-width:80%;"}

이전에 만든 Facebook 페이지와 인스턴트 양식을 선택한 다음 **계속을** 클릭합니다.

![][7]{: style="max-width:80%;"}

다음으로 이 트리거를 테스트합니다. 양식 출력의 유효성을 검사한 후 **선택한 레코드로 계속**을 선택합니다.

#### 3b단계: 액션 만들기

새 단계를 추가한 다음, **Zapier의 웹훅**을 선택합니다. 다음으로, **이벤트** 필드에 대한 **커스텀 요청**을 선택한 다음, **계속**을 클릭합니다. 

![][8]{: style="max-width:80%;"}

마지막으로 페이로드에 필드를 삽입하여 사용자 지정 요청을 설정합니다. 다음 코드 스니펫은 페이로드 예시를 보여줍니다. 

```
{
    "attributes": [
        {
            "email": "<insert_email_field>",
            "first_name": "<insert_first_name_field>",
            "last_name": "<insert_last_name_field>",
            "lead_form": "<insert_form_name_field>",
            "fb_campaign": "<insert_campaign_id_field>",
            "fb_ad_set": "<insert_campaign_id_field>",
            "fb_ad": "<insert_campaign_id_field>",
            "email_subscribe": "subscribed",
            "subscription_groups" : [{
                "subscription_group_id": "<subscription_group_id>",
                "subscription_state": "subscribed"
                }
            ]
        }
    ],
    "events": [
        {
            "email": "<insert_email_field>",
            "name": "<insert_custom_event_name>",
            "time": "<insert_timestamp_field>",
            "_update_existing_only": false
        }
    ]
}`
```

다음은 Zapier에서 이것이 어떻게 보이는지 보여주는 예시입니다:

![][9]{: style="max-width:80%;"}

웹훅을 구성한 후 **계속 및 테스트**를 선택합니다. 테스트가 성공하면 Zap을 게시할 수 있습니다.

### 4단계: Facebook 리드 광고 Zap 테스트

이 포괄적인 테스트를 수행하려면 Facebook 개발자 콘솔에서 Facebook의 리드 광고 테스트 툴을 사용합니다. 자세한 내용은 <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting/" target="_blank">테스트 및 문제 해결</a>을 참조하세요.

## 사용자 ID 관리

이 통합을 통해 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#example-request-for-updating-a-user-profile-by-phone-number)를 사용하여 이메일로 Facebook 리드에 기여할 수 있습니다.

* 이메일이 기존 사용자 프로필과 일치하는 경우, Braze는 Facebook 리드 데이터로 프로필을 업데이트합니다.
* 동일한 이메일을 사용하는 사용자 프로필이 여러 개 있는 경우, Braze는 가장 최근에 업데이트된 외부 ID를 사용하는 프로필에 우선순위를 부여하여 업데이트를 진행합니다.
* 외부 ID가 존재하지 않는 경우, Braze는 가장 최근에 업데이트된 프로필과 일치하는 이메일을 우선적으로 사용합니다.
* 제공된 이메일을 사용하는 프로필이 없는 경우 Braze에서 새 프로필을 생성하고, 새 별칭 고객 프로필이 생성합니다. 새로 생성한 별칭 고객 프로필을 식별하려면 [`/users/identify` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)를 사용합니다.

{% alert note %}
해당 필드를 사용할 수 있고 통합을 위해 원하는 기본 식별자를 사용할 수 있는 경우 전화번호 또는 외부 ID를 Braze에 요청할 때 사용할 수도 있습니다. 이렇게 하려면 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)에 표시된 대로 요청 페이로드를 수정합니다.
{% endalert %}

## 문제 해결

{% details 트리거와 작업을 성공적으로 테스트한 후에도 Zapier Zap을 게시할 수 없는 이유는 무엇인가요? %}
이 통합 기능을 사용하려면 프리미엄 앱을 지원하는 <a href="https://zapier.com/app/pricing/" target="_blank">Zapier 요금제</a>를 사용해야 합니다.
{% enddetails %}

{% details Facebook 리드가 Braze에 동기화되지 않는 이유는 무엇인가요? %}
1. Facebook 페이지, 광고 계정 및 리드 액세스 권한에 대한 관리자 액세스 권한이 있는지 확인합니다. 그런 다음 Zapier에서 계정을 다시 연결합니다.
2. Facebook에서 만든 인스턴트 양식이 트리거 단계에서 선택한 양식에 매핑되는지 확인합니다. 
3. **Facebook 비즈니스 매니저** > **통합** > **리드 액세스**로 이동하여 Zapier를 리드 액세스 권한을 할당했는지 확인합니다.
{% enddetails %}

{% details 동일한 이메일에 중복된 사용자 프로필이 표시되는 이유는 무엇인가요? %}
[고객 프로필 수명주기]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-profile-lifecycle)에 따라 Braze에서 고객 프로필을 생성하고 관리하는 고유한 방법이 있습니다.

내부 프로세스와 Braze 내에서 고객을 생성하도록 트리거하는 시점에 따라, 통합에 의해 생성되는 사용자 프로필과 시스템에서 사용자가 생성되는 시점의 경쟁 조건으로 인해 중복된 사용자 프로필이 발생할 수 있습니다. Braze에서 [고객 프로필을 병합]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)할 수 있습니다.
{% enddetails %}

{% details Zapier 계정이 없습니다. Facebook 리드 광고 웹훅을 Braze로 트리거하려면 어떻게 해야 하나요? %}
Zapier를 사용하지 않거나 사용할 계획이 없는 경우, Facebook에서 Braze로 직접 통합을 구축할 수 있습니다. 자세한 내용은 <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/" target="_blank">리드 광고 설명서</a>를 참조하세요.

Facebook에서 리드를 검색하려면 <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#webhooks" target="_blank">웹훅</a>을 사용합니다. Facebook에서 웹훅을 시작하려면 <a href="https://developers.facebook.com/docs/graph-api/webhooks/getting-started" target="_blank">웹훅 설명서</a>를 참조하세요.

Facebook에서 웹훅 URL을 설정한 후, 팀과 협력하여 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)로 데이터를 전달하는 최적의 경로를 결정합니다. Zapier 접근 방식과 마찬가지로 `users/track` 엔드포인트를 통해 [이메일로 요청하는]({{site.baseurl}}/api/endpoints/user_data/post_user_track#example-request-for-updating-a-user-profile-by-phone-number) 것이 좋습니다.
{% enddetails %}

{% alert tip %}
더 많은 문제 해결 팁은 Zapier의 <a href="https://help.zapier.com/hc/en-us/articles/8495982030861-Common-Problems-with-Facebook-Lead-Ads#h_01HC9V6Y652KQYYY96YG99T423" target="_blank">Facebook 리드 문제 해결 가이드</a>를 참조하세요.
{% endalert %}


[1]: {{site.baseurl}}/api/basics/#api-definitions
[2]: {% image_buster /assets/img/fb_lead_ads_zapier/integration1.png %}
[3]: {% image_buster /assets/img/fb_lead_ads_zapier/integration2.png %}
[4]: {% image_buster /assets/img/fb_lead_ads_zapier/create_zap1.png %}
[5]: {% image_buster /assets/img/fb_lead_ads_zapier/create_zap2.png %}
[6]: {% image_buster /assets/img/fb_lead_ads_zapier/create_zap3.png %}
[7]: {% image_buster /assets/img/fb_lead_ads_zapier/create_zap4.png %}
[8]: {% image_buster /assets/img/fb_lead_ads_zapier/create_zap5.png %}
[9]: {% image_buster /assets/img/fb_lead_ads_zapier/configuration_example.png %}