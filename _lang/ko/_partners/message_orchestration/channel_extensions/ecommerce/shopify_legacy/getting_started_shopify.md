---
nav_title: 시작하기
article_title: "Shopify 시작하기"
description: "이 참조 문서에서는 Shopify 웹사이트에 Braze 웹 SDK를 구현하는 방법을 간략하게 설명합니다."
page_type: partner
search_tag: Partner
alias: /getting_started_shopify_legacy/
page_order: 1
---

# Shopify 시작하기

> 이 문서에서는 Shopify 웹사이트에 Braze 웹 SDK를 구현하는 방법을 간략하게 설명합니다. 구현 후에 Braze와의 Shopify 통합 설정을 완료하는 방법을 알아보려면 [Shopify 설정]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify)을 참조하세요.

## 통합 설정 체크리스트

1. [Braze 웹 SDK 구현](#implement-web-sdk)
2. [Braze에서 Shopify 설정]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify)
3. Shopify 통합 테스트

## Shopify 웹사이트에 웹 SDK 구현하기 {#implement-web-sdk}

[Braze 웹 SDK]({{site.baseurl}}/user_guide/getting_started/web_sdk/)는 Shopify 스토어 고객의 행동을 추적하는 데 사용되는 강력한 툴입니다. 웹 SDK를 사용하면 웹 또는 모바일 브라우저에서 세션 데이터를 수집하고, 사용자를 식별하며, 사용자 행동 데이터를 기록할 수 있습니다. 인브라우저 메시지와 같은 기본 메시징 채널을 잠금 해제할 수도 있습니다.

Shopify 통합은 강력한 기본 기능 세트를 제공하지만, [Shopify 통합에서 지원하지 않는 이벤트에]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/using_shopify/shopify_data_in_braze/) 대한 현장 추적을 추가하거나 [콘텐츠 카드]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards) 등의 채널을 추가하려는 사용 사례가 있는 경우 웹 SDK를 Shopify 사이트에 직접 구현해야 한다는 점에 유의하세요.

통합 온보딩을 시작하기 전에 팀과 함께 웹 SDK를 구현하는 경로에 대해 다음 사항을 검토하세요.

### 지원되는 기능

|아이콘| 정의 
|-------------|-------------
|<i aria-hidden="true" class="fas fa-check" title="지원됨"></i><span class="sr-only">지원됨</span> | 지원
|<i aria-hidden="true" class="fas fa-times" title="지원되지 않음"></i><span class="sr-only">지원됨</span> | 지원되지 않음
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

| 피처 | Shopify ScriptTag를 통한 웹 SDK | theme.liquid를 통해 직접 웹 SDK 통합 | Shopify Hydrogen을 통한 직접 웹 SDK 통합
|-------------|-------------|-------------|------------
| 기본 현장 추적      | <i class="fas fa-check" title="지원"></i> | <i class="fas fa-times" title="지원되지 않음"></i> | <i class="fas fa-times" title="지원되지 않음"></i>          
| 캡처 양식 사용자 조정(낮은 엔지니어링 리프트 필요)   | <i class="fas fa-check" title="지원"></i> | <i class="fas fa-check" title="지원"></i> | <i class="fas fa-times" title="지원되지 않음"></i> 
| 결제 사용자 조정     | <i class="fas fa-check" title="지원"></i>  | <i class="fas fa-times" title="지원되지 않음"></i>   | <i class="fas fa-times" title="지원되지 않음"></i>                                        
| 조회한 제품<br> 클릭한 제품<br> 방치된 장바구니   | <i class="fas fa-check" title="지원"></i> |<i class="fas fa-check" title="지원"></i> | <i class="fas fa-times" title="지원되지 않음"></i> 
| 중단된 결제<br> 생성된 주문<br> Braze 구매<br> 주문 결제<br> 부분 주문 처리된 주문<br> 주문 처리된 주문<br> 취소된 주문<br> 환불 생성<br> 고객 생성 및 업데이트 | <i class="fas fa-check" title="지원"></i> | <i class="fas fa-check" title="지원"></i> | <i class="fas fa-check" title="지원"></i>
| 기록 백필 | <i class="fas fa-check" title="지원"></i>  | <i class="fas fa-check" title="지원"></i>  | <i class="fas fa-check" title="지원"></i>  
| 카탈로그 동기화  |<i class="fas fa-check" title="지원"></i> |<i class="fas fa-check" title="지원"></i>  |<i class="fas fa-check" title="지원"></i>
| 이메일 및 SMS 구독자 수집    | <i class="fas fa-check" title="지원"></i>| <i class="fas fa-check" title="지원"></i>  | <i class="fas fa-check" title="지원"></i>     
| 기본 인앱 메시지 지원   | <i class="fas fa-check" title="지원"></i>  | <i class="fas fa-check" title="지원"></i>  | <i class="fas fa-times" title="지원되지 않음"></i>     
| 기본 콘텐츠 카드 지원   | <i class="fas fa-times" title="지원되지 않음"></i> | <i class="fas fa-times" title="지원되지 않음"></i> | <i class="fas fa-times" title="지원되지 않음"></i>   
| 기본 웹 푸시 지원     | <i class="fas fa-times" title="지원되지 않음"></i> | <i class="fas fa-times" title="지원되지 않음"></i> | <i class="fas fa-times" title="지원되지 않음"></i>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }    

{% tabs %}
{% tab Shopify ScriptTag %}

### Shopify ScriptTag를 통해 Braze 웹 SDK 구현하기

[Shopify ScriptTag는](https://shopify.dev/api/admin-rest/2021-10/resources/scripttag#top) 스토어 페이지 또는 결제의 주문 상태 페이지에 로드되는 원격 JavaScript 코드입니다. 스토어 페이지가 로드되면 Shopify는 사이트 페이지에 로드해야 하는 스크립트 태그가 있는지 확인합니다. 

Braze를 빠르게 시작하려는 경우 Braze가 Braze 웹 SDK용 사전 정의된 스크립트를 Shopify 스토어 사이트에 직접 로드하도록 허용하는 옵션이 있습니다.

{% alert important %}
이 통합 방법을 위한 Braze 웹 SDK의 사전 정의된 스크립트는 사용자 지정할 수 없습니다.
{% endalert %}

#### Shopify 통합과 함께 작동하는 방법

Shopify 사이트가 로드되면 Shopify는 페이지에 로드해야 하는 스크립트 태그가 있는지 확인합니다. 이 과정에서 Braze 웹 SDK 스크립트가 스토어 페이지 또는 결제의 주문 상태 페이지에 로드됩니다. 

또한 제품 보기, 제품 클릭, 장바구니 포기 이벤트를 선택한 경우 사전 정의된 스크립트를 추가하여 Shopify ScriptTag 또는 인앱 메시징을 채널로 사용할 수 있도록 합니다.  

#### 활성화 방법

통합의 일부로 Braze Web SDK 스크립트를 자동으로 활성화하려면 지원되는 Shopify ScriptTag 이벤트를 선택하거나 [Shopify 통합 설정]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/) 중에 인앱 메시징을 채널로 활성화합니다. 

Shopify 설정 작성기에서 별표(\*)로 표시된 이벤트는 웹 SDK에서 지원됩니다. 이러한 이벤트를 선택하거나 브라우저 내 메시징을 포함하면 Braze는 설정의 일부로 Shopify ScriptTag를 통해 웹 SDK 구현을 Shopify 스토어에 추가합니다.

#### Shopify 이메일 캡처 양식 및 사용자 조정 

캡처 양식은 고객 생애주기 초기에 식별 가능한 고객 정보를 확보하여 다운스트림 메시징 및 인게이지먼트를 유도합니다. 

웹 SDK는 `device_id`를 사용하여 Shopify 현장 행동 및 익명 사용자를 추적합니다. Braze Shopify ScriptTag 통합은 뉴스레터 신청과 같은 Shopify 이메일 캡처 양식의 이메일을 사용자의 `device_id` 에 할당합니다.

일반적인 이메일 캡처 양식은 다음과 같습니다: 
- 이메일 캡처 양식 
- 뉴스레터 신청 양식

사용자의 이메일과 `device_id`를 조정하는 두 가지 방법이 있습니다. 
- Braze 자동 이메일 캡처 스크립트 사용 
- `setEmail` 또는 `setPhoneNumber` 메서드 호출

##### 이메일 또는 전화 가입 캡처

Braze를 사용하면 [이메일과]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/#step-1-create-an-in-app-message-campaign) [SMS 및 WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture) 가입 양식을 사용하여 웹 SDK와 인앱 메시지를 활용할 수 있습니다. 

Shopify 이메일 또는 전화번호 캡처 또는 타사 캡처 양식을 사용하는 경우 Braze Web SDK에서 추적하는 사용자에 대해 직접 설정할 수 있습니다. 예를 들어 고객의 이메일 주소를 확보한 경우 다음과 같이 사용자 프로필에 설정할 수 있습니다:

{% raw %}
```javascript
braze.getUser().setEmail(<email address>);
```
{% endraw %}

이러한 값 설정에 대한 자세한 내용은 다음 자바스크립트 리소스를 참조하세요:

- 사용자 [이메일](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail) 설정
- 사용자 [휴대폰 번호](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setphonenumber) 설정

이메일이나 전화번호를 수집할 때 사용자의 구독 상태를 다음과 같이 설정할 수도 있습니다:

{% raw %}
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.SUBSCRIBED);
```
{% endraw %}

이러한 값 설정에 대한 자세한 내용은 다음 자바스크립트 리소스를 참조하세요:

- 사용자의 [이메일 알림 구독 유형](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype) 설정하기
- [구독 그룹에](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup) 사용자 추가하기

**서드파티 캡처 양식 구현 예제**

1. `theme.liquid` 에서 `head tag` 에 다음 스니펫을 복사합니다:

{% raw %}
```javascript
<script>
  const emailInputPoller = setInterval(()=>{
    if (document.getElementById('{FORM_ID}')) {
      document.getElementById('{FORM_ID}').addEventListener("submit",
        function() {  
          var email = document.getElementById('{INPUT_EMAIL_ID}').value
          braze.getUser().setEmail(email)
        }
      );
    }
    clearInterval(emailInputPoller)
  }, 2000)
</script>
```
{% endraw %}

{: start="2"}
2\. 스크립트가 먼저 로드되도록 먼저 `setInterval` 호출
3\. `{FORM_ID}` 을 캡처하려는 양식의 요소 ID로 바꿉니다.
(예: "ContactFooter").
4\. `{INPUT_EMAIL_ID}` 을 양식 내 이메일 입력 필드의 요소 ID로 바꿉니다.
5\. 양식이 제출되면 스크립트는 이메일 입력 값으로 `setEmail` 호출
6\. 스크립트가 로드된 후 한 번만 로드되도록 `clearInterval` 호출

{% alert note %}
현재 Braze 이메일 캡처 양식은 Shopify 고객을 생성하지 않습니다. 따라서 고객이 결제를 진행하거나 계정을 생성할 때까지 연결된 Shopify 사용자 프로필 없이 Braze 사용자 프로필을 보유할 수 있습니다.
{% endalert %}

#### 구현 후 예상되는 사항

**Braze 웹 SDK 초기화**

세션이 시작되면 웹 SDK가 초기화됩니다. Shopify 고객 ID, 이메일 또는 전화번호와 같은 다른 식별자는 Shopify 스토어의 게스트 방문자에게 쉽게 제공되지 않을 수 있으므로 Braze는 익명 사용자 데이터 추적을 위해 `device_id` 을 수집해야 합니다.

또한 결제 프로세스 후 고객이 이메일 주소나 전화번호와 같은 식별 가능한 정보를 제공하면 `device_id` 을 사용하여 사용자 데이터를 익명 사용자 프로필에 조정할 수 있습니다.

**Braze 웹 SDK 버전**

Shopify ScriptTag 통합을 통한 Braze 웹 SDK의 현재 버전은 v4.2입니다.

**월간 활성 사용자(MAU)**

웹 SDK는 Shopify 고객 및 게스트의 세션을 추적합니다. 결과적으로 이는 Braze 대시보드 보고 내에서 MAU 할당량에 포함되어 MAU로 누적됩니다. 익명 사용자도 MAU에 포함된다는 점을 명심해야 합니다. 모바일 디바이스의 경우 익명 사용자는 디바이스에 따라 다릅니다. 웹 사용자의 경우 익명 사용자는 브라우저 캐시에 의존합니다.

{% endtab %}

{% tab 테마 액체 %}

### Shopify 사이트 theme.liquid에 직접 웹 SDK 구현

Braze는 다음을 포함하여 웹 SDK를 구현하는 여러 방법을 제공합니다.
- Shopify `theme.liquid` 파일에 직접 웹 SDK 추가하기
- Google 태그 관리자 

Shopify 스토어에 이미 웹 SDK가 설치되어 있는 경우에도 온보딩 프로세스 내에서 Shopify ScriptTag 설정을 계속 진행할 수 있습니다. 

설치 프로세스 중에 Braze는 Shopify 스토어에서 웹 SDK 인스턴스를 이미 사용할 수 있는지 확인합니다. 기존 구현이 있는 경우, Braze는 웹 SDK를 활성화하기 위해 미리 정의된 스크립트를 로드하지 않습니다. 그런 다음, 필요한 스크립트를 추가하여 선택한 이벤트를 추적하거나 인브라우저 메시징을 활성화할 수 있도록 합니다.

#### 활성화 방법

웹 SDK를 수동으로 구현하려면 [초기 SDK 설정]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)을 참조하세요. Google Tag Manager를 통해 웹 SDK를 구현하려면 [웹용 Google Tag Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/web/google_tag_manager#google-tag-manager)를 참조하세요. 

어느 구현 경로를 사용하든 웹 SDK 통합에 다음이 포함되어 있는지 확인하지 않으면 Shopify 통합이 지원되지 않습니다: 
- 웹 SDK 버전 v4.0 이상
- 세션 시작 시 웹 SDK 초기화

#### Shopify 이메일 캡처 양식 및 사용자 조정 

캡처 양식은 고객 생애주기 초기에 식별 가능한 고객 정보를 확보하여 다운스트림 메시징 및 인게이지먼트를 유도합니다. 

웹 SDK는 `device_id`를 사용하여 Shopify 현장 행동 및 익명 사용자를 추적합니다. Braze Shopify ScriptTag 통합은 뉴스레터 신청과 같은 Shopify 이메일 캡처 양식의 이메일을 사용자의 `device_id` 에 할당합니다.

일반적인 이메일 캡처 양식은 다음과 같습니다: 
- 이메일 캡처 양식 
- 뉴스레터 신청 양식

사용자의 이메일과 `device_id`를 조정하는 두 가지 방법이 있습니다. 
- Braze 자동 이메일 캡처 스크립트 사용 
- `setEmail` 또는 `setPhoneNumber` 메서드 호출

##### 이메일 또는 전화 가입 캡처

Braze를 사용하면 [이메일과]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/#step-1-create-an-in-app-message-campaign) [SMS 및 WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture) 가입 양식을 사용하여 웹 SDK와 인앱 메시지를 활용할 수 있습니다. 

Shopify 이메일 또는 전화번호 캡처 또는 타사 캡처 양식을 사용하는 경우 Braze Web SDK에서 추적하는 사용자 개체에서 직접 설정할 수 있습니다. 예를 들어 고객의 이메일 주소를 확보한 경우 다음과 같이 사용자 프로필에 설정할 수 있습니다:

{% raw %}
```javascript
braze.getUser().setEmail(<email address>);
```
{% endraw %}

이러한 값 설정에 대한 자세한 내용은 다음 자바스크립트 리소스를 참조하세요:

- 사용자 [이메일](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail) 설정
- 사용자 [휴대폰 번호](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setphonenumber) 설정

이메일이나 전화번호를 수집할 때 사용자의 구독 상태를 이렇게 설정할 수도 있습니다:

{% raw %}
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.SUBSCRIBED);
```
{% endraw %}

이러한 값 설정에 대한 자세한 내용은 다음 자바스크립트 리소스를 참조하세요:

- 사용자의 [이메일 알림 구독 유형](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype) 설정하기
- [구독 그룹에](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup) 사용자 추가하기

**서드파티 캡처 양식 구현 예제**

1. `theme.liquid` 에서 `head tag` 에 다음 스니펫을 복사합니다:

{% raw %}
```javascript
<script>
  const emailInputPoller = setInterval(()=>{
    if (document.getElementById('{FORM_ID}')) {
      document.getElementById('{FORM_ID}').addEventListener("submit",
        function() {  
          var email = document.getElementById('{INPUT_EMAIL_ID}').value
          braze.getUser().setEmail(email)
        }
      );
    }
    clearInterval(emailInputPoller)
  }, 2000)
</script>
```
{% endraw %}

{: start="2"}
2\. 스크립트가 먼저 로드되도록 먼저 `setInterval` 호출
3\. `{FORM_ID}` 을 캡처하려는 양식의 요소 ID로 바꿉니다.
(예: "ContactFooter").
4\. `{INPUT_EMAIL_ID}` 을 양식 내 이메일 입력 필드의 요소 ID로 바꿉니다.
5\. 양식이 제출되면 스크립트는 이메일 입력 값으로 `setEmail` 호출
6\. 스크립트가 로드된 후 한 번만 로드되도록 `clearInterval` 호출

{% alert note %}
현재 Braze 이메일 캡처 양식은 Shopify 고객을 생성하지 않습니다. 따라서 고객이 결제를 진행하거나 계정을 생성할 때까지 연결된 Shopify 사용자 프로필 없이 Braze 사용자 프로필을 보유할 수 있습니다.
{% endalert %}

#### 통합 후 예상되는 사항

**Braze 웹 SDK 초기화**

세션이 시작되면 웹 SDK가 초기화됩니다. Shopify 고객 ID, 이메일 또는 전화번호와 같은 다른 식별자는 Shopify 스토어의 게스트 방문자에게 쉽게 제공되지 않을 수 있으므로 Braze는 익명 사용자 데이터 추적을 위해 `device_id` 을 수집해야 합니다.

또한 고객이 결제 프로세스 중 및 이후에 이메일이나 전화번호와 같은 식별 가능한 정보를 제공하면 `device_id` 을 통해 사용자 데이터를 익명 사용자 프로필과 조정할 수 있습니다.

**Braze 웹 SDK 버전**

현재 Braze Web SDK의 버전은 v4.0 이상이어야 합니다.

**월간 활성 사용자(MAU)**

웹 SDK는 Shopify 고객 및 게스트의 세션을 추적합니다. 결과적으로 이는 Braze 대시보드 보고 내에서 MAU 할당량에 포함되어 MAU로 누적됩니다. 익명 사용자도 MAU에 포함된다는 점을 명심해야 합니다. 모바일 디바이스의 경우 익명 사용자는 디바이스에 따라 다릅니다. 웹 사용자의 경우 익명 사용자는 브라우저 캐시에 의존합니다.

{% endtab %}
{% tab 헤드리스 Shopify 사이트 %}

### 헤드리스 Shopify 사이트에 직접 웹 SDK 구현 {#headless-site}

Braze Shopify ScriptTag 통합은 헤드리스 Shopify 사이트와 호환되지 않습니다. 따라서 제품 조회, 제품 클릭, 유기한 장바구니 이벤트에 대한 기본 지원을 받을 수 없으며 사전 정의된 스크립트를 통해 인앱 메시징을 활성화할 수 없습니다. 

#### 활성화 방법

웹 SDK를 헤드리스 Shopify 사이트에 직접 통합하려면 [웹용 초기 SDK 설정]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)을 참조하세요.

웹 SDK 통합에 다음이 포함되어 있는지 확인하세요: 
- 웹 SDK 버전은 v4.0 이상이어야 합니다.
- 세션 시작 시 웹 SDK 초기화

#### 사용자 조정을 위한 Shopify 양식 설정

eCommerce brands likely have experiences on their Shopify site to capture identifiable information from customers ahead of checkout, like email capture forms.

웹 SDK는 `device_id`를 사용하여 Shopify 현장 행동 및 익명 사용자를 추적합니다. 이메일 주소가 익명 사용자 프로필에 추가되었는지 확인하려면 뉴스레터 또는 이메일 캡처 양식에 다음을 추가합니다: 
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail) 
  - 이메일 캡처 또는 뉴스레터 신청
- [addAlias](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addalias) 
  - "alias_label": "shopify_email" 
  - "alias_name": "example@email.com"

사용자가 계정을 등록하거나 로그인할 때 외부 ID로 [사용자 프로필을 식별하고]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles) 싶을 수 있습니다. 사용자가 계정을 등록하고 로그인한 후 사용자가 계정을 만들거나 로그인하는 경우 외부 ID를 할당하는 [changeUser](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) 메서드를 추가합니다. 

{% alert note %}
사용자 프로필에 임시 별칭을 설정하면 나중에 사용자를 식별하기 위해 [사용자/병합 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) 엔드포인트에 요청을 진행할 수 있습니다.
{% endalert %}

#### 결제 사용자 조정 설정 {#headless-checkout}

중단된 결제 이벤트를 활성화하면 Braze는 Shopify 결제/생성 웹훅을 받게 됩니다. Braze는 이메일 주소, 전화 번호 또는 Shopify 고객 ID로 기존 사용자 프로필과 매칭을 시도합니다. 일치하는 항목이 없으면 Braze가 별칭 프로필을 생성합니다. 

현장에서 추적된 사용자 프로필이 Shopify 웹훅에서 생성된 Shopify 별칭 사용자 프로필과 병합되도록 하려면 아래 단계에 따라 [`/users/merge` 엔드포인트를]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) 사용할 수 있습니다. 

{% alert tip %}
`theme.liquid` 파일에 대한 SDK 또는 API 호출을 통해 커스텀 이벤트를 기록하여 `users/merge` 엔드포인트에 대한 요청이 포함된 캔버스를 트리거할 수 있습니다. 이러한 방법은 아래에 설명되어 있습니다.
{% endalert %}

고객이 Shopify 사이트를 방문하는 즉시 익명 사용자가 생성됩니다. 이 사용자에게는 자동으로 Braze `device_id`가 할당됩니다. 

1. 새 세션이 시작되면 사이트 방문자에게 고유한 [사용자 별칭]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification)을 무작위로 할당합니다.

2. 사용자가 사이트에서 작업을 수행하면 이를 [커스텀 이벤트]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)로 기록하거나 [사용자 속성을 캡처]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web)합니다. 사용자가 결제를 진행하여 Shopify 양식에 이메일을 입력하면 Shopify 고객 ID가 생성됩니다. 이메일, 전화 또는 Shopify 별칭이 기존 사용자와 일치하지 않는 경우 Braze는 Shopify 웹훅을 처리하고 새 사용자 프로필을 생성합니다.

{% raw %}
```javascript
{
  "user_alias": {
    "alias_name": 1234,
    "alias_label": "temp_user_id"
  }
}
```
{% endraw %}

{% subtabs %}
{% subtab API approach %}

{: start="3"}
3\. 사용자 프로필 중복을 방지하려면 Braze `device_id` 가 포함된 사용자 프로필을 Shopify 별칭 프로필이 포함된 사용자 프로필과 병합해야 합니다. 지연을 설정하고 `do_not_merge` 속성으로 사용자를 업데이트한 다음, [`/users/merge` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)에 대한 요청을 수행하는 API 트리거 캔버스를 생성할 수 있습니다. `merge_user` 같은 사용자 지정 이벤트를 기록하여 캔버스를 트리거할 수도 있습니다. 


{% endsubtab %}
{% subtab Non-API approach %}

{: start="3"}
3\. 사용자가 플로우를 종료하거나 결제를 완료하면 `merge_user` 와 같은 사용자 지정 이벤트를 기록하여 지연을 설정하는 캔버스를 트리거하고 `do_not_merge` 속성으로 사용자를 업데이트하고 [`/users/merge` 엔드포인트에]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) 요청할 수 있습니다.

{% endsubtab %}
{% endsubtabs %}

{: start="4"}
4\. 캔버스 진입 기준에서 식별되지 않은 고객 프로필(외부 ID가 없고 `do_not_merge`가 true가 아님)만 타겟팅합니다. <br><br>![`do_not_merge`를 필터로 사용하는 캔버스 작성기의 '오디언스 진입' 단계.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_entrycriteria.png %})

{: start="5"}
5\. 캔버스 진입 기준을 구성한 후 캔버스 흐름을 생성할 수 있습니다. 캔버스의 첫 번째 단계를 **지연** 단계로 설정하여 처리 중 발생할 수 있는 경합 조건을 방지하세요.<br><br>![캔버스 작성기의 지연 단계.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_delay.png %})

{: start="6"}
6\. 이러한 사용자는 다음 단계에서 병합되므로 **사용자 업데이트** 단계를 만들어 `do_not_merge` 사용자 지정 속성을 "true"로 업데이트할 수 있습니다. <br><br>![속성으로 `do_not_merge`가 선택된 캔버스 작성기의 사용자 업데이트 단계.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_userupdate.png %})

{: start="7"}
7\. 다음으로 웹훅을 사용하여 **메시지** 단계를 만듭니다.<br><br>![웹훅 메시징 채널이 있는 캔버스 작성기의 메시지 단계.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_webhook.png %}) 

{% raw %}
```javascript
{
  "merge_updates": [
    {
      "identifier_to_merge": {
           "user_alias": {
                "alias_label": "temp_user_id",
                "alias_name": "{{canvas_entry_properties.${temp_user_id}}}"
            }
      },
      "identifier_to_keep": {
           "user_alias": {
                "alias_label": "shopify_customer_id",
                "alias_name": "{{canvas_entry_properties.${shopify_customer_id}}}"
            }
      }
    }
  ]
}
```
{% endraw %}

{% alert tip %}
`merge_users` 동작에 대한 자세한 내용은 [POST를 참조하세요: 사용자 병합]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior).
{% endalert %}

{: start="8"}
8\. 사용자가 플로우를 종료하거나 결제를 완료하면 후속 Shopify 웹후크는 이메일 주소나 전화 번호 또는 Shopify 별칭을 사용하여 일치합니다.

{% endtab %}
{% endtabs %}
