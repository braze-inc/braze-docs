---
nav_title: 커스텀 속성이 있는 배포판
article_title: Voucherify에서 커스텀 속성과 함께 배포
page_order: 3
alias: /partners/voucherify/custom_attributes/
description: "이 참조 문서에서는 Voucherify와 Braze 통합을 간략히 설명합니다. Braze 통합을 통해 Braze 메시지에서 Voucherify 코드를 보낼 수 있습니다."
page_type: partner
search_tag: Partner
---

# 커스텀 속성이 있는 배포판

> Braze 통합을 통해 Braze 메시지에서 Voucherify 코드를 보낼 수 있습니다. 이 참조 문서에서는 Voucherify 배포에서 Braze 커스텀 속성을 사용하는 방법을 다룹니다.

{% alert tip %}
Voucherify 배포에서 Braze 커스텀 속성을 사용하기 전에, Braze 사용자를 Voucherify 대시보드에 추가해야 합니다. Braze 연결된 콘텐츠를 사용하여 사용자를 동기화하거나 CSV 또는 API를 통해 고객을 가져올 수 있습니다. [Voucherify](https://support.voucherify.io/article/67-how-to-import-my-customers)를 방문하여 자세히 알아보세요.
{% endalert %}

Braze 커스텀 속성은 Braze의 사용자 프로필에 Voucherify 코드를 커스텀 속성으로 할당할 수 있게 해줍니다. 고유한 쿠폰, 기프트 카드, 로열티 카드 및 추천 코드를 사용할 수 있습니다. 먼저 Voucherify를 Braze와 연결하고, Voucherify에서 배포를 생성한 다음, Braze에서 캠페인을 생성하고, 메시지 템플릿에 커스텀 속성 스니펫을 추가합니다.

## 1단계: Voucherify 계정을 Braze에 연결하기

먼저, Voucherify 계정을 Braze와 연결하세요.

1. Braze 계정에서 REST API 키를 복사하세요.
2. Voucherify 대시보드의 **Integrations** 디렉토리로 이동하여 Braze를 찾아 **Connect.**를 선택하세요.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_integrations.png %}){: style="margin-top:15px;margin-left:25px;margin-bottom:15px;"}
    
3. Braze API 키를 붙여넣고 **연결**을 선택하세요:  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_enter_API_key.png %}){: style="max-width:60%;margin-top:15px;margin-left:25px;margin-bottom:15px;"}


## 2단계: 코드 분포

연결되면 Braze의 고객 프로필에 있는 커스텀 속성에 코드를 할당하는 새로운 Voucherify [배포](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work)를 시작할 수 있습니다. 나중에 Braze 캠페인에서 코드가 포함된 수신 속성을 사용할 수 있습니다.

배포를 설정하기 전에 Braze 사용자를 Voucherify 대시보드에 추가해야 합니다. [Voucherify](https://support.voucherify.io/article/67-how-to-import-my-customers)를 방문하여 자세히 알아보세요.

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_distribution.png %})

코드를 Braze에 배포할 수 있는 두 가지 모드가 있습니다:

- **수동 모드**
- 사용자가 취한 조치에 따라 코드 전달을 트리거하는 **자동화된 워크플로**를 정의합니다.

수동 모드와 자동 모드 모두에서 Voucherify는 고유 코드를 해당 속성과 함께 전송하고 이를 사용자 프로필의 Braze 커스텀 속성에 할당합니다.

![필드를 커스텀 속성에 매핑]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_fields_mapping.png %})

{% tabs %}
{% tab 수동 배포 %}

수동 모드는 선택한 오디언스에게 코드를 할당하는 일회성 작업입니다. 대시보드에서 **배포**로 이동하여 플러스를 사용하여 배포 매니저를 실행하고 **수동 메시지**를 선택하십시오.

1.  배포판의 이름을 지정하십시오.

    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_name_distribution.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}<br>  
    
    고유 코드 **(1)**의 출처가 될 캠페인을 선택하고 사용자 세그먼트 또는 단일 고객을 수신자로 선택하십시오 **(2)**. [Voucherify](https://support.voucherify.io/article/51-customer-segments)에 방문하여 고객 세그먼트에 대해 자세히 알아보세요.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_name_distribution_choose_segment.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  

2.  다음으로, 마케팅 권한을 추가합니다. 오디언스에게서 권한을 수집하지 않으면 동의 확인을 비활성화합니다.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_consents.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  
    
3.  Braze를 채널로 선택하고 고객 프로필에 추가할 커스텀 필드를 매핑합니다. 게시된 바우처의 코드를 나타내는 필드를 추가해야 합니다. 나머지 필드는 선택 사항입니다.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_channel.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  
    
4.  완료되면 분포 요약을 볼 수 있습니다. **저장 및 전송**을 클릭하여 Braze에서 고객 프로필로 코드를 전달합니다.  

_모든 수동 배포는 10분 지연 후에 전송됩니다._

{% endtab %}
{% tab 자동 워크플로 %}

Voucherify는 다음 트리거에 응답하여 Braze에 코드를 자동으로 푸시할 수 있습니다:

- **특정 Voucherify 세그먼트에 진입하거나 해당 세그먼트를 떠난 고객**
- **성공적인 코드 게시** – 메시지는 코드가 캠페인에서 고객에게 Voucherify에 게시(할당)될 때 전송됩니다.
- **주문 상태 changed** (order created, order updated, order has been paid, order canceled)
- **기프트 크레딧 추가됨** – 고객의 카드에 기프트 카드 크레딧이 추가될 때 메시지가 전송됩니다.
- **로열티 포인트 추가됨** – 고객 프로필에 로열티 포인트가 추가될 때 메시지가 전송됩니다.
- **바우처 사용됨** – 바우처를 성공적으로 사용한 고객에게 메시지가 전송됩니다.
- **바우처 사용 롤백** – 사용이 성공적으로 롤백된 고객에게 메시지가 전송됩니다.
- **리워드 사용** – 고객이 로열티 또는 추천 리워드를 사용할 때 메시지가 전송됩니다.
- **커스텀 이벤트가 고객을 위해 기록되었습니다** \- 이 메시지는 Voucherify가 특정 커스텀 이벤트를 기록할 때 트리거됩니다.

Braze 및 Voucherify와 함께 자동 워크플로를 설정하려면 [배포 튜토리얼을 참조](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work)하세요.

{% endtab %}
{% endtabs %}

## 3단계: 귀하의 Braze 캠페인에서 Voucherify 커스텀 속성을 사용하십시오

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_code.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

코드가 포함된 커스텀 속성이 Braze의 고객 커스텀 속성에 추가되면 캠페인에서 이를 사용할 수 있습니다.

메시지 본문을 편집하고 Voucherify 배포에 정의된 커스텀 속성을 추가하세요. {% raw %}`{{custom_attribute.${custom_attribute_with_code}}}`{% endraw %}를 배치하여 고유 코드를 표시합니다.

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_email_body.png %}){: style="max-width:75%;"}

준비가 되면 메시지 미리보기에서 코드를 볼 수 있습니다.

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_email_preview.png %})
