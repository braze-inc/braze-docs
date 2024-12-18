---
nav_title: 테스트 메시지 보내기
article_title: 테스트 메시지 보내기
page_order: 6
description: "이 참조 문서에서는 다양한 채널에 대한 테스트 메시지 보내기에 대해 설명합니다."

---

# 테스트 메시지 보내기

> 사용자에게 메시징 캠페인을 보내기 전에 메시징 캠페인이 제대로 표시되고 의도한 방식으로 작동하는지 테스트해 볼 수 있습니다. 대시보드의 툴을 사용하면 특정 기기 또는 팀원에게 테스트 메시지를 쉽게 작성하고 전송할 수 있습니다.

## 지정된 테스트 세그먼트 만들기 <a class="margin-fix" name="test-segment"></a>

테스트 세그먼트를 설정한 후에는 이를 사용하여 **모든** 메시징 채널을 테스트할 수 있습니다. 올바르게 구성한 경우 이 프로세스는 한 번만 수행하면 됩니다.

테스트 세그먼트를 설정하려면 대시보드의 **세그먼트** 페이지로 이동하여 새 세그먼트를 만듭니다. **필터 추가를** 클릭하여 드롭다운 메뉴 하단에 있는 테스트 필터 중 하나를 선택합니다.

![타겟팅 단계에서 사용 가능한 필터를 표시하는 Braze 테스트 캠페인.]({% image_buster /assets/img_archive/testmessages1.png %})

이러한 두 가지 테스트 필터를 사용하면 특정 이메일 주소 또는 외부 [사용자 ID를]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#setting-user-ids) 가진 사용자를 선택할 수 있습니다.

![테스트]({% image_buster /assets/img_archive/testmessages2.png %})라는 제목 아래에 여러 필터가 나열된 드롭다운 메뉴가 표시됩니다.

이메일 주소와 외부 사용자 아이디 필터에는 모두 세 가지 옵션이 있습니다:

  1) **'같음'** \- 제공한 이메일 또는 사용자 ID와 정확히 일치하는 항목을 찾습니다. 단일 이메일 또는 사용자 ID와 연결된 기기로만 테스트 캠페인을 보내려는 경우 이 옵션을 사용합니다.

  2) **"동일하지 않음"** \- 특정 이메일 또는 사용자 ID를 테스트 캠페인에서 제외하려는 경우 이 옵션을 사용합니다.

  3) **"일치"** \- 입력한 검색어의 일부와 일치하는 이메일 주소 또는 사용자 아이디를 가진 사용자를 찾습니다. 이 옵션을 사용하여 '@yourcompany.com' 주소를 사용하는 사용자만 찾아서 팀원 모두에게 메시지를 보낼 수 있습니다.

'일치' 옵션을 사용하고 이메일 주소를 | 문자로 구분하여(예: 'email1@braze.com | email2@braze.com' '일치') 여러 개의 특정 이메일을 선택할 수 있습니다.

이러한 필터를 함께 사용하여 테스트 사용자 목록을 좁힐 수도 있습니다. 예를 들어 테스트 세그먼트에 '@braze.com' '일치' 이메일 주소 필터 및 다른 'sales@braze.com' '같지 않음' 필터가 포함될 수 있습니다. 

테스트 세그먼트에 테스트 필터를 추가한 후에는 세그먼트 에디터 상단의 **미리 보기를** 클릭하여 의도한 사용자만 선택했는지 확인하거나 에디터 오른쪽 모서리에 있는 톱니바퀴 아이콘을 클릭하고 드롭다운 메뉴에서 **모든 사용자 데이터 CSV 내보내기를** 선택하여 해당 세그먼트의 사용자 데이터를 CSV로 내보내면 확인할 수 있습니다.

![브레이즈 캠페인의 세그먼트 세부 정보]({% image_buster /assets/img_archive/testmessages3.png %})

>  세그먼트의 사용자 데이터를 CSV로 내보내면 해당 세그먼트에 속하는 사람을 가장 정확하게 파악할 수 있습니다. **미리보기** 탭은 세그먼트에 있는 사용자의 샘플일 뿐이므로 의도한 모든 구성원을 선택하지 않은 것처럼 보일 수 있습니다.

## 테스트 푸시 알림 또는 인앱 메시지 보내기 <a class="margin-fix" name="push-inapp-test"></a>

테스트 푸시 알림 또는 인앱 메시지를 보내려면 이전에 생성한 테스트 세그먼트를 타겟팅해야 합니다. 캠페인을 생성하고 일반적인 단계를 따라 캠페인을 시작하세요. **타겟 사용자** 단계에 도달하면 드롭다운 메뉴에서 테스트 세그먼트를 선택합니다.

![타겟팅 단계에서 사용 가능한 세그먼트를 표시하는 Braze 테스트 캠페인.]({% image_buster /assets/img_archive/test_segment.png %})

캠페인 확인을 완료하고 캠페인을 실행하여 푸시 알림 및 인앱 메시지를 테스트합니다.

>  하나의 캠페인을 사용하여 자신에게 테스트 메시지를 두 번 이상 보내려는 경우 캠페인 작성기의 **일정** 부분에서 **사용자에게 캠페인을 수신할 수 있는 자격 다시 부여**를 선택해야 합니다.

## 테스트 이메일 메시지 보내기

이메일 메시지만 테스트하는 경우에는 반드시 테스트 세그먼트를 설정할 필요는 없습니다. 캠페인의 이메일 메시지를 작성하는 캠페인 작성기의 첫 번째 단계에서 **테스트 보내기를** 클릭하고 테스트 이메일을 보낼 이메일 주소를 입력합니다. 

![테스트 전송 탭이 선택된 Braze 캠페인]({% image_buster /assets/img_archive/testmessages45.png %})

{% alert tip %}
테스트 메시지에 [TEST(또는 SEED)]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#append-email-subject-lines) 추가를 사용하거나 사용하지 않도록 설정할 수도 있습니다.
{% endalert %}

## 명령줄에서 테스트하기

또는 명령줄을 통해 푸시 알림을 테스트하려면 각 플랫폼에서 다음 예제를 따르세요.

### cURL을 통해 iOS 앱으로 푸시 테스트하기

CURL 및 [메시징 API를]({{site.baseurl}}/api/endpoints/messaging/) 통해 터미널을 통해 단일 알림을 보낼 수 있습니다. 다음 필드를 테스트 케이스에 맞는 올바른 값으로 바꿔야 합니다:

- `YOUR_API_KEY` - **설정** > **API 키에서** 사용 가능
- `YOUR_EXTERNAL_USER_ID` - **사용자 검색** 페이지에서 사용 가능
- `YOUR_KEY1` (선택 사항)
- `YOUR_VALUE1` (선택 사항)

{% alert note %}
[이전 탐색을]({{site.baseurl}}/navigation) 사용하는 경우 이러한 페이지는 다른 위치에 있습니다: <br>- **API 키는** **개발자 콘솔** > **API 설정에서** 찾을 수 있습니다. <br>- **사용자 검색**은 **사용자** > **사용자 검색**에 있음
{% endalert %}

>  다음 예제에서는 `US-01` 인스턴스에서 고객에게 적합한 API 엔드포인트를 보여줍니다. 이 인스턴스를 사용하고 있지 않다면 [API 설명서를]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) 참조하여 요청할 엔드포인트를 확인하세요.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert": "Test push",
      "extra": { 
        "YOUR_KEY1" :"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

### cURL을 통해 Android 앱으로 푸시 테스트

터미널을 통해 cURL 및 [메시징 API를]({{site.baseurl}}/api/endpoints/messaging/) 통해 단일 알림을 보낼 수 있습니다. 다음 필드를 테스트 케이스에 맞는 올바른 값으로 바꿔야 합니다:

- `YOUR_API_KEY` ( **설정** > **API 키로** 이동합니다.)
- `YOUR_EXTERNAL_USER_ID` ( **사용자 검색** 페이지에서 프로필을 검색합니다.)
- `YOUR_KEY1` (선택 사항)
- `YOUR_VALUE1` (선택 사항)

>  다음 예제에서는 `US-01` 인스턴스에서 고객에게 적합한 API 엔드포인트를 보여줍니다. 이 인스턴스를 사용하고 있지 않다면 [API 설명서를]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) 참조하여 요청할 엔드포인트를 확인하세요.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

### cURL을 통해 Kindle 앱으로 푸시 테스트하기

터미널을 통해 cURL 및 [메시징 API를]({{site.baseurl}}/api/endpoints/messaging/) 통해 단일 알림을 보낼 수 있습니다. 다음 필드를 테스트 케이스에 맞는 올바른 값으로 바꿔야 합니다:

- `YOUR_API_KEY` - **개발자 콘솔** 페이지에서 사용 가능
- `YOUR_EXTERNAL_USER_ID` - **사용자 검색** 페이지에서 사용 가능
- `YOUR_KEY1` (선택 사항)
- `YOUR_VALUE1` (선택 사항)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "kindle_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

## 테스트 메시지의 제한 사항

테스트 메시지가 실제 사용자 집합을 대상으로 캠페인이나 캔버스를 실행하는 것과 기능적으로 완전히 동등하지 않은 몇 가지 상황이 있습니다. 이 경우 이 동작을 검증하려면 제한된 테스트 사용자 집합을 대상으로 캠페인 또는 캔버스를 실행해야 합니다.

- **테스트 메시지에서** Braze [환경설정 센터를]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) 확인하면 제출 버튼이 회색으로 표시됩니다.
- list-unsubscribe 헤더가 테스트 메시지 기능으로 보낸 이메일에 포함되지 않음
- 인앱 메시지 및 콘텐츠 카드의 경우 대상 사용자에게 대상 기기에 대한 푸시 토큰이 있어야 함

