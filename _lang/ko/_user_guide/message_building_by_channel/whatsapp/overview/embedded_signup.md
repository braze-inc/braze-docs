---
nav_title: 임베디드 가입
article_title: WhatsApp 임베디드 가입
page_order: 0
description: "이 참조 문서는 Braze에서 WhatsApp 임베디드 가입 워크플로우에 대한 단계별 안내를 제공합니다."
page_type: reference
channel:
  - WhatsApp
---

# WhatsApp 임베디드 가입

> 이 참조 문서는 Braze에서 WhatsApp 임베디드 가입 워크플로우에 대한 단계별 안내를 제공합니다.

WhatsApp 임베디드 가입 워크플로우는 처음 [WhatsApp 통합]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/)을 Braze 작업 공간에 추가할 때와 기존 WhatsApp 통합에 [WhatsApp 비즈니스 계정]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups/)을 추가할 때 접근할 수 있습니다.

{% alert note %}
여러 [WhatsApp 비즈니스 계정](({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups/))을 Braze 작업 공간에 추가할 수 있습니다. 그러나 각 특정 WhatsApp 비즈니스 계정은 오직 하나의 Braze 작업 공간에만 추가될 수 있습니다.
{% endalert %}

## 워크플로우 접근하기

**파트너 통합** > **기술 파트너**로 이동한 다음, **WhatsApp**을 검색하고 선택합니다. 다음 선택은 사용 사례에 따라 다릅니다:

- 작업 공간에 WhatsApp을 통합하는 경우, **통합 시작**을 선택합니다. <br><br>\![WhatsApp 파트너 페이지와 통합 시작 버튼.]({% image_buster /assets/img/whatsapp/whatsapp1.png %}){: style="max-width:80%;"}<br><br>
- 기존 WhatsApp 통합에 WhatsApp 비즈니스 계정을 추가하는 경우, **WhatsApp 비즈니스 계정 추가**을 선택합니다. <br><br>\!["WhatsApp 메시징 통합"과 WhatsApp 비즈니스 계정 또는 구독 그룹 및 번호 추가 옵션.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %}){: style="max-width:80%;"}

여기서의 워크플로우는 두 사용 사례 모두에 대해 동일합니다.

## WhatsApp 임베디드 가입 워크플로우

1. 메타(페이스북) 로그인 창에서 **로그인** 또는 **계속**을 선택합니다. <br><br>\![메타 로그인 창.]({% image_buster /assets/img/whatsapp/login_screen.png %}){: style="max-width:60%;"}<br><br>
2. Braze와 공유할 권한을 읽고, **시작하기**를 선택하세요. <br><br>\![Braze와의 통합을 위해 공유할 권한 목록.]({% image_buster /assets/img/whatsapp/get_started.png %}){: style="max-width:50%;"}<br><br>
3. **비즈니스 포트폴리오** 드롭다운에서 비즈니스 포트폴리오를 선택한 후 **다음**을 선택하세요. 이것은 귀하의 WhatsApp 비즈니스 계정에 연결되므로, 예상하는 비즈니스 포트폴리오가 보이지 않으면 권한을 확인하세요.<br><br>\![비즈니스 포트폴리오 이름을 포함하여 비즈니스 정보를 입력할 필드가 있는 창.]({% image_buster /assets/img/whatsapp/business_info.png %}){: style="max-width:50%;"}<br><br>
4. 드롭다운 필드에 대해 다음을 선택한 후 **다음**을 선택하세요.
- **WhatsApp 비즈니스 계정 선택**: WhatsApp 비즈니스 계정 만들기
- **WhatsApp 비즈니스 프로필 만들기 또는 선택하기**: 새 WhatsApp 비즈니스 프로필 만들기 <br><br>\![WhatsApp 비즈니스 계정 및 프로필을 선택하거나 만드는지 지정할 필드.]({% image_buster /assets/img/whatsapp/create_select_waba.png %}){: style="max-width:50%;"}<br><br>
5. 다음을 제공한 후 **다음**을 선택하세요.
- WhatsApp 비즈니스 계정 이름
- WhatsApp 비즈니스 표시 이름
- 카테고리 <br><br>\![새 WhatsApp 비즈니스 계정에 대한 세부정보를 제공할 필드.]({% image_buster /assets/img/whatsapp/waba_details.png %}){: style="max-width:50%;"}<br><br>
6. 전화번호를 입력하고 **문자 메시지** 또는 **전화 통화** 중 하나를 선택하세요. 이 번호는 WhatsApp 전화번호의 모든 요구 사항을 따라야 하며, 다른 WhatsApp 계정에 등록되어 있지 않아야 합니다. <br><br>\![전화번호를 추가할 필드.]({% image_buster /assets/img/whatsapp/add_phone_number.png %}){: style="max-width:50%;"}<br><br>
7. 이중 인증 코드를 입력한 후 **다음**을 선택하세요. <br><br>\![2단계 인증 코드 입력 필드.]({% image_buster /assets/img/whatsapp/two_factor.png %}){: style="max-width:50%;"}<br><br>
8. 귀하의 WhatsApp 비즈니스 계정이 받을 권한을 검토한 후, **계속**을 선택하십시오. <br><br>\![WhatsApp 비즈니스 계정에서 요청한 권한 목록.]({% image_buster /assets/img/whatsapp/permissions.png %}){: style="max-width:50%;"}<br><br>
9. 완료되었습니다! <br><br>\![사람들에게 메시지를 보낼 준비가 되었다고 말하는 창.]({% image_buster /assets/img/whatsapp/finish.png %}){: style="max-width:50%;"}

