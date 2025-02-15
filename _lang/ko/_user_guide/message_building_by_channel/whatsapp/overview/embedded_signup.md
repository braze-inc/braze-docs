---
nav_title: 임베디드 가입
article_title: WhatsApp 임베디드 가입
page_order: 0
description: "이 참고 문서에서는 Braze의 WhatsApp 임베드된 가입 워크플로우에 대한 단계별 안내를 제공합니다."
page_type: reference
channel:
  - WhatsApp
---

# WhatsApp 임베디드 가입

> 이 참고 문서에서는 Braze의 WhatsApp 임베드된 가입 워크플로우에 대한 단계별 안내를 제공합니다.

WhatsApp 임베디드 가입 워크플로우는 [WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/)을 Braze 워크스페이스에 처음 통합할 때와 기존 WhatsApp 통합에 [WhatsApp 비즈니스 계정을 추가할]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups/) 때 액세스할 수 있습니다.

## 워크플로에 액세스하기

**파트너 통합** > **기술 파트너로** 이동한 다음 **WhatsApp**을 검색하여 선택합니다. 다음 선택은 사용 사례에 따라 다릅니다:

- WhatsApp을 워크스페이스에 통합하는 경우 **통합 시작**을 선택합니다. <br><br>![][10]{: style="max-width:80%;"}<br><br>
- 기존 WhatsApp 통합 서비스에 WhatsApp 비즈니스 계정을 추가하는 경우에는 **WhatsApp 비즈니스 계정 추가**를 선택합니다. <br><br>![][11]{: style="max-width:80%;"}

여기서부터의 워크플로우는 두 사용 사례 모두 동일합니다.

## WhatsApp 임베디드 가입 워크플로

1. 메타(Facebook) 로그인 창에서 다른 **계정으로 로그인** 또는 **계속**을 선택합니다. <br><br>![메타 로그인 창.][1]{: style="max-width:60%;"}<br><br>
2. Braze와 공유할 권한을 읽은 다음 **시작하기**를 선택합니다. <br><br>![통합을 위해 Braze와 공유할 권한 목록입니다.][2]{: style="max-width:50%;"}<br><br>
3. **비즈니스** 포트폴리오 드롭다운에서 비즈니스 포트폴리오를 선택한 후 **다음을** 선택합니다. 이것은 WhatsApp 비즈니스 계정에 연결되므로 예상 비즈니스 포트폴리오가 표시되지 않으면 권한을 확인하세요.<br><br>![비즈니스 포트폴리오 이름 등 비즈니스 정보를 입력할 수 있는 필드가 있는 창입니다.][3]{: style="max-width:50%;"}<br><br>
4. 드롭다운 필드에서 다음을 선택한 후 **다음**을 선택합니다.
- **WhatsApp 비즈니스 계정을 선택합니다**: WhatsApp 비즈니스 계정 만들기
- **WhatsApp 비즈니스 프로필을 만들거나 선택합니다**: 새 WhatsApp 비즈니스 프로필 만들기 <br><br>![WhatsApp 비즈니스 계정 및 프로필을 선택하거나 생성할지 여부를 지정하는 필드입니다.][4]{: style="max-width:50%;"}<br><br>
5. 다음을 입력한 후 **다음을** 선택합니다.
- WhatsApp 비즈니스 계정 이름
- WhatsApp 비즈니스 표시 이름
- 카테고리 <br><br>![필드에 새 WhatsApp 비즈니스 계정에 대한 세부 정보를 입력합니다.][5]{: style="max-width:50%;"}<br><br>
6. 휴대폰 번호를 입력하고 **문자 메시지** 또는 **전화 통화** 중 하나를 선택합니다. 이 번호는 다른 WhatsApp 계정에 등록되어 있지 않아야 하는 등 WhatsApp 전화번호의 모든 요구 사항을 준수해야 합니다. <br><br>![필드에 전화번호를 추가합니다.][6]{: style="max-width:50%;"}<br><br>
7. 2단계 인증 코드를 입력한 후 **다음**을 선택합니다. <br><br>![2단계 인증 코드의 입력 필드입니다.][7]{: style="max-width:50%;"}<br><br>
8. WhatsApp 비즈니스 계정에 부여되는 권한을 검토한 후 **계속**을 선택합니다. <br><br>![WhatsApp 비즈니스 계정에서 요청한 권한 목록입니다.][8]{: style="max-width:50%;"}<br><br>
9. 완료되었습니다! <br><br>![창에 사람들에게 메시지를 보낼 준비가 되었다는 메시지가 표시됩니다.][9]{: style="max-width:50%;"}

[1]: {% image_buster /assets/img/whatsapp/login_screen.png %}
[2]: {% image_buster /assets/img/whatsapp/get_started.png %}
[3]: {% image_buster /assets/img/whatsapp/business_info.png %}
[4]: {% image_buster /assets/img/whatsapp/create_select_waba.png %}
[5]: {% image_buster /assets/img/whatsapp/waba_details.png %}
[6]: {% image_buster /assets/img/whatsapp/add_phone_number.png %}
[7]: {% image_buster /assets/img/whatsapp/two_factor.png %}
[8]: {% image_buster /assets/img/whatsapp/permissions.png %}
[9]: {% image_buster /assets/img/whatsapp/finish.png %}
[10]: {% image_buster /assets/img/whatsapp/whatsapp1.png %}
[11]: {% image_buster /assets/img/whatsapp/multiple_wabas.png %} 