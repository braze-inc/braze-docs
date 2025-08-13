---
nav_title: OneTrust
article_title: OneTrust
description: "이 참조 문서에서는 데이터 개인정보 보호 및 보안 소프트웨어 제공업체인 Braze와 OneTrust 간의 파트너십에 대해 설명하며, 이를 통해 OneTrust 워크플로 빌더를 사용하여 제품에 대한 보안 워크플로를 만들 수 있습니다."
alias: /partners/onetrust/
page_type: partner
search_tag: Partner

---

# OneTrust

> [OneTrust](https://www.onetrust.com/)는 개인정보 보호 및 보안 소프트웨어 제공업체로, 신뢰 환경을 더 잘 이해하는 데 필요한 가시성, 강력한 인사이트를 활용할 수 있는 조치, 경쟁에서 우위를 점할 수 있는 자동화를 제공합니다. 

_이 통합은 OneTrust에서 유지 관리합니다._

## 통합 정보

Braze와 OneTrust의 통합을 통해 OneTrust 워크플로 빌더를 사용하여 제품에 대한 보안 워크플로를 만들 수 있습니다.
## 필수 조건

| 요구 사항 | 설명 |
|---|---|
| OneTrust 계정 | 이 파트너십을 활용하려면 [OneTrust](https://www.onetrust.com/) 계정이 필요합니다. |
| Braze API 키 | OneTrust 동작이 사용할 엔드포인트에 필요한 권한이 있는 Braze REST API 키.<br><br>Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| 브레이즈 인스턴스 | Braze 인스턴스는 Braze 온보딩 매니저로부터 가져오거나 [API 개요 페이지]({{site.baseurl}}/api/basics/#endpoints)에서 찾을 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

다음 통합에서는 사용자 동의 업데이트 워크플로와 사용자 삭제 워크플로를 생성하는 방법에 대한 안내를 제공합니다. 추가적으로 지원되는 Braze 엔드포인트에 대한 자세한 내용은 [기타 지원되는 작업](#Other-supported-actions)을 참조하세요.

### OneTrust에 Braze 자격 증명 추가하기

OneTrust **통합** 메뉴에서 **자격증명** > **새로 추가** 버튼으로 이동하여 **시스템 선택** 화면을 불러옵니다. 여기에서 **Braze**를 찾은 후 **다음** 버튼을 클릭합니다.

**자격증명 세부 정보 입력** 화면의 메시지에 따라 다음 정보를 입력합니다. 완료되면 자격 증명을 저장합니다.
  - 자격증명 이름
  - 커넥터 유형을 **웹 앱으로** 설정
  - 호스트 이름: `<your-braze-instance-url>`
  - **요청 헤더**:
    - **권한 부여**: Bearer
    - **Content-Type**: application/json
  - 토큰: `<your-braze-api-key>`

### Braze를 시스템으로 추가

#### 1단계: 워크플로 만들기

{% tabs %}
{% tab 사용자 동의 업데이트 %}
1. OneTrust 통합 메뉴에서 **갤러리** > **Braze** > **추가**로 이동하여 새 워크플로를 생성합니다.![]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. 워크플로 모달에서 이름과 알림 이메일을 입력합니다. **만들기** 버튼을 클릭합니다. 생성 시 워크플로 빌더로 이동합니다. 삭제 요청을 처리하는 데 사용할 수 있는 API 호출 및 작업으로 Braze 워크플로우가 시드됩니다. <br><br>
3. 워크플로 빌더에서 워크플로에서 트리거할 작업을 선택합니다.<br>![]({% image_buster /assets/img/onetrust/onetrust2.png %})

{% endtab %}
{% tab 사용자 삭제 %}

1. OneTrust 통합 메뉴에서 **갤러리** > **Braze** > **추가**로 이동하여 새 워크플로를 생성합니다.![]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. 워크플로 모달에서 이름과 알림 이메일을 입력합니다. **만들기** 버튼을 클릭합니다. 생성 시 워크플로 빌더로 이동합니다. 삭제 요청을 처리하는 데 사용할 수 있는 API 호출 및 작업으로 Braze 워크플로우가 시드됩니다. <br><br>
3. 워크플로 빌더에서 워크플로에서 트리거할 작업을 선택합니다.<br>![]({% image_buster /assets/img/onetrust/onetrust8.png %})
{% endtab %}
{% endtabs %}

#### 2단계: 작업 선택
{% tabs %}
{% tab 사용자 동의 업데이트 %}

1. 완료되면 **완료**를 클릭하고 **작업 추가**를 선택합니다. 선택하는 작업은 업데이트되는 기본 설정 유형과 선호하는 엔드포인트에 따라 달라집니다.
- 사용자의 글로벌 가입 환경설정을 업데이트하려면 **POST 사용자 추적 - 속성** 작업을 선택합니다.
- 사용자의 구독 그룹 환경설정을 업데이트하려면 **POST 사용자 추적 - 속성** 작업 또는 **POST 사용자 구독 그룹 상태 설정** 작업을 선택합니다.<br>![]({% image_buster /assets/img/onetrust/onetrust4.png %})<br><br>
2. 원하는 작업을 선택하고 이전에 생성한 Braze 자격 증명을 선택한 후 **다음**을 클릭합니다.<br>![]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% tab 사용자 삭제 %}

1. 완료되면 **완료**를 클릭하고 **작업 추가**를 선택합니다.
- Braze에서 사용자를 삭제하려면 **POST 사용자 삭제 작업**을 선택합니다.
<br>![]({% image_buster /assets/img/onetrust/onetrust9.png %})<br><br>
2. 원하는 작업을 선택하고 이전에 생성한 Braze 자격 증명을 선택한 후 **다음**을 클릭합니다.<br>![]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% endtabs %}
#### 3단계: 업데이트 요청 본문
{% tabs %}
{% tab 사용자 동의 업데이트 %}

1. 필요한 동적 값을 포함하도록 본문을 업데이트합니다. 작업 본문이 [`/users/track` 엔드포인트](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/) 및 [`/subscription/status/set` 엔드포인트](https://www.braze.com/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)와 일치하는지 확인합니다.
2. 조직의 필요에 맞게 추가 매개변수 또는 조건부 논리를 사용하여 워크플로를 사용자 지정하세요.
3. 편집이 완료되면 **마침**을 클릭한 다음, **활성화**를 클릭하여 워크플로를 활성화합니다.

{% alert note %}
OneTrust 워크플로를 사용하여 Braze에서 구독 그룹 환경설정을 업데이트하는 경우 `subscription_group_id`는 구독 그룹을 생성할 때 Braze에서 설정한 ID와 일치해야 합니다. Braze 대시보드에서 **구독** 그룹 페이지로 이동하여 구독 그룹의 `subscription_group_id` 에 액세스할 수 있습니다.
{% endalert %}

![]({% image_buster /assets/img/onetrust/onetrust6.png %})

{% endtab %}
{% tab 사용자 삭제 %}

1. 필요한 동적 값을 포함하도록 본문을 업데이트합니다. 작업 본문이 [`/users/delete` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)와 일치하는지 확인합니다
2. 편집이 완료되면 **마침**을 선택한 다음, **활성화**를 클릭하여 워크플로를 활성화합니다.

![]({% image_buster /assets/img/onetrust/onetrust10.png %})

#### 데이터 주체 요청 워크플로 업데이트
1. **개인정보 보호 권한 자동화** 메뉴에서 **워크플로**를 선택합니다. 
2. Braze 통합으로 업데이트하려는 워크플로를 선택합니다. 
3. **편집** 버튼을 선택하여 편집을 활성화합니다.
4. 그런 다음, Braze 통합을 추가할 워크플로 단계를 선택하고 **연결 추가**를 클릭합니다.
5. 이전에 생성한 Braze 워크플로를 시스템 하위 작업으로 추가합니다.

{% endtab %}
{% endtabs %}

## 기타 지원되는 작업

**POST 사용자 추적 - 속성**, **POST 사용자 구독 그룹 상태 설정**, **POST 사용자 삭제** 작업 외에도 Braze는 커스텀 워크플로를 생성하는 데 사용할 수 있고 기존 워크플로 내에서 하위 작업으로 사용할 수 있는 다른 엔드포인트를 지원합니다. 

지원되는 작업의 전체 목록을 보려면 다음을 수행합니다.
1. OneTrust의 **통합** 메뉴에서 **시스템**을 클릭합니다. 
2. **Braze** 시스템을 선택합니다.
3. **작업** 탭으로 이동합니다.

![][7]


[1]: {% image_buster /assets/img/onetrust/onetrust.png %}
[2]: {% image_buster /assets/img/onetrust/onetrust2.png %}
[3]: {% image_buster /assets/img/onetrust/onetrust3.png %}
[4]: {% image_buster /assets/img/onetrust/onetrust4.png %}
[5]: {% image_buster /assets/img/onetrust/onetrust5.png %}
[6]: {% image_buster /assets/img/onetrust/onetrust6.png %}
[7]: {% image_buster /assets/img/onetrust/onetrust7.png %}
[8]: {% image_buster /assets/img/onetrust/onetrust8.png %}
[9]: {% image_buster /assets/img/onetrust/onetrust9.png %}
[10]: {% image_buster /assets/img/onetrust/onetrust10.png %}
