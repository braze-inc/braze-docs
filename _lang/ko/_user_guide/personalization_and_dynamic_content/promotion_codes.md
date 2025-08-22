---
nav_title: 프로모션 코드
article_title: 프로모션 코드
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "이 참조 문서에서는 프로모션 코드 목록을 생성하고 캠페인과 캔버스에 추가하는 방법을 설명합니다."
---

# 프로모션 코드

> This page covers how to create promotion code lists and add them to your campaigns and Canvases.

## How it works

프로모션 코드라고도 하는 프로모션 코드는 구매에 중점을 둔 상호 작용을 유도하여 사용자의 참여를 유지하는 좋은 방법입니다. 프로모션 코드 목록에서 가져오는 메시지를 만들 수 있습니다. 

Each promotion code has an expiration date of up to six months, and can be deleted before expiry by contacting [Support]({{site.baseurl}}/user_guide/administrative/access_braze/support/). 목록당 최대 2천만 개의 코드를 저장하고 관리할 수 있습니다. 프로모션 코드의 성과를 관리하고 분석하여 프로모션 전략과 메시지에 대한 타겟팅된 결정을 내릴 수 있습니다.

{% alert important %}
Promotion codes can't be sent in in-app messages in Canvas. If you're participarting in the [early access](#promotion-codes-iam-campaigns), promotion codes can be sent in in-app message campaigns.
{% endalert %}

## 프로모션 코드 목록 만들기

### 1단계: 프로모션 코드 섹션으로 이동

![Button to create a promotion code.]({% image_buster /assets/img/promocodes/promocode1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

1. 대시보드에서 **데이터 설정** > **프로모션 코드로** 이동합니다.
2. **프로모션 코드 목록 생성을** 선택합니다.

### 2단계: 프로모션 코드 이름 지정

1. 프로모션 코드 목록의 이름을 지정하고 선택 사항인 설명을 추가합니다.
2. 다음으로 프로모션 코드에 대한 코드 스니펫을 생성합니다. 

코드 조각을 만들 때 고려해야 할 몇 가지 세부 사항은 다음과 같습니다:

- 코드 스니펫은 일단 저장되면 편집할 수 없습니다.
- 스니펫은 대소문자를 구분합니다. 예를 들어, "Birthday_promo""와 "birthday_promo"은 서로 다른 두 개의 스니펫으로 인식됩니다.
- Liquid에서 스니펫 이름을 사용하여 이 프로모션 코드 세트를 참조하세요.
- 코드 스니펫이 다른 목록에서 이미 사용되고 있지 않은지 확인하세요.

![A promotion code list named "SpringSale2025" with the code snippet "spring25".]({% image_buster /assets/img/promocodes/promocode3.png %}){: style="max-width:80%"}

### 3단계: 프로모션 코드 옵션 선택

각 프로모션 코드 목록에는 생성 시 설정되는 해당 만료 날짜와 시간이 있습니다. 최대 만료 기간은 목록을 만들거나 수정한 날로부터 6개월 후까지입니다. 

해당 기간 내에 만료일을 반복해서 변경하고 업데이트할 수 있습니다. 이 만료 날짜는 이 목록에 추가된 모든 코드에 적용됩니다. 만료되면 해당 코드는 Braze 시스템에서 삭제되며 해당 목록의 코드 조각을 호출하는 모든 메시지는 전송되지 않습니다.

![List expiration settings that all remaining codes will expire on April 30, 2025 at 12 am.]({% image_buster /assets/img/promocodes/promocode4.png %}){: style="max-width:80%"}

임계값 알림을 선택 사항으로 설정하고 사용자 지정할 수도 있습니다. 이 알림을 설정하면 목록에 사용 가능한 프로모션 코드가 부족하거나 프로모션 코드 목록의 만료가 임박했을 때 지정된 수신자에게 이메일이 전송됩니다. 수신자에게는 하루에 한 번 알림이 전송됩니다.

![An example of a threshold alert to notify "marketing@abc.com" when the promotion code list expires in 5 days.]({% image_buster /assets/img/promocodes/promocode5.png %}){: style="max-width:80%"}

### 4단계: 프로모션 코드 업로드

Braze doesn't manage code creation or redemption, meaning you must generate your promotion codes to a CSV file and upload them to Braze. 

CSV 파일이 다음 가이드라인을 따르고 있는지 확인하세요:

- 프로모션 코드 열을 포함합니다.
- 행당 하나의 프로모션 코드가 있습니다.

You can use our built-in integration with [Voucherify]({{site.baseurl}}/partners/ecommerce/loyalty/voucherify/) or [Talon.One]({{site.baseurl}}/partners/ecommerce/loyalty/talonone/) to create and export promotion codes.

{% alert important %}
최대 파일 크기는 100MB, 최대 목록 크기는 사용하지 않은 코드의 20밀리미터입니다. 잘못된 파일이 업로드된 경우 새 파일을 업로드하면 이전 파일이 대체됩니다.
{% endalert %}

1. 업로드가 완료되면 **목록 저장을** 선택하여 방금 입력한 모든 세부 정보와 코드를 저장합니다.

![CSV file named "springsale" that was successfully uploaded.]({% image_buster /assets/img/promocodes/promocode7.png %})

{:start="2"}
2\. 저장을 선택하면 **가져오기 기록**에 새 행이 나타납니다.
3\. 가져오기가 완료되었는지 확인하기 위해 표를 새로 고치려면 표 상단에서 <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **동기화를** 선택합니다.

![Promotion codes in the process of being uploaded.]({% image_buster /assets/img/promocodes/promocode8.png %})

{% alert note %}
대용량 파일은 가져오는 데 몇 분 정도 걸립니다. 기다리는 동안 페이지에서 나가서 가져오기가 진행되는 동안 다른 작업을 할 수 있습니다. When the import finishes, the status will change to **Complete** in the table.
{% endalert %}

#### 프로모션 코드 목록 업데이트

목록을 업데이트하려면 기존 목록 중 하나를 선택합니다. 이름, 설명, 목록 만료 및 임계값 알림을 변경할 수 있습니다. 새 파일을 업로드하고 **목록 업데이트**를 선택하여 목록에 코드를 더 추가할 수도 있습니다.

목록의 모든 코드는 가져온 날짜와 관계없이 만료일이 동일합니다.

### 5단계: 프로모션 코드 사용

메시지로 프로모션 코드를 보내려면 다음과 같이 하세요:

1. 코드 조각 **복사를** 선택하여 프로모션 코드 목록을 생성할 때 설정한 코드 조각을 복사합니다.

![An option to copy the snippet to paste into your message.]({% image_buster /assets/img/promocodes/promocode9.png %}){: style="max-width:70%"}

{:start="2"}
2\. 거기에서 이 코드를 대시보드 내의 메시지에 붙여넣을 수 있습니다.

![An example message "Treat yourself to something nice this spring with our exclusive offer" followed by the code snippet.]({% image_buster /assets/img/promocodes/promocode10.png %}){: style="max-width:70%"}

[Liquid를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) 사용하면 업로드한 CSV 파일의 고유 프로모션 코드 중 하나를 메시지에 삽입할 수 있습니다. 해당 코드는 다른 메시지에서 동일한 코드를 보내지 않도록 Braze 백엔드에 전송된 것으로 표시됩니다.

#### 사용자에게 프로모션 코드 보내기

멀티채널 캠페인이나 캔버스 단계에서 코드 스니펫을 사용하면 각 사용자는 항상 고유한 코드를 받게 됩니다. 캔버스의 여러 단계에 대해 각 사용자는 여러 개의 프로모션 코드를 받습니다.

사용자가 두 개 이상의 채널을 통해 코드를 받을 수 있는 자격이 있는 경우 각 채널을 통해 동일한 코드를 받게 됩니다. 예를 들어 사용자가 두 개의 채널을 통해 두 개의 메시지를 수신하는 경우 하나의 코드만 수신하게 됩니다. 보고 목적으로도 동일하게 적용되며, 하나의 코드가 전송되고 사용자는 두 채널을 통해 이 코드를 받게 됩니다. 예를 들어, 멀티채널 캔버스 단계의 경우 사용자는 하나의 코드만 사용합니다.

{% alert important %}
프로모션 코드를 가져오는 캠페인에서 테스트 또는 실시간 메시지를 보낼 때 사용 가능한 프로모션 코드가 남아 있지 않으면 메시지가 전송되지 않습니다.
{% endalert %}

#### 프로모션 코드가 포함된 테스트 메시지 보내기

테스트 전송 및 시드 그룹 이메일 전송은 별도의 요청이 없는 한 프로모션 코드를 소진합니다. 테스트 전송 및 시드 그룹 이메일 전송 중에 프로모션 코드가 사용되지 않도록 이 기능 동작을 업데이트하려면 Braze 계정 관리자에게 문의하세요.

## 사용된 코드 수 확인

**프로모션 코드** 페이지의 프로모션 코드 목록의 **남은** 열에서 남은 코드 수를 확인할 수 있습니다.

![An example of a promotion code with unused codes.]({% image_buster /assets/img/promocodes/promocode11.png %})

이 코드 수는 기존 프로모션 코드 목록 페이지를 다시 방문할 때도 확인할 수 있습니다. 사용하지 않는 코드를 CSV 파일로 내보낼 수도 있습니다. 

![A promotion code named "Black Friday Sale" with 992 remaining codes.]({% image_buster /assets/img/promocodes/promocode12.png %}){: style="max-width:70%"}

### Using promotion codes in in-app message campaigns {#promotion-codes-iam-campaigns}

{% alert important %}
Using promotion codes in in-app message campaigns is currently in early access. Contact your Braze account manager if you're interested in participating in this early access.
{% endalert %}

After creating an [in-app message campaign]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages), you can insert a [promotion code list snippet]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) into your in-app message message body. 

Promotion codes in in-app messages will be deducted and used only when a user triggers the display of the in-app message.

## 멀티채널 및 단일 채널 전송

멀티채널 및 단일 전송 캠페인과 캔버스의 경우, 메시지의 리퀴드에 참조된 모든 프로모션 코드가 메시지 전송 **전에** 사용되지 않도록 차감되어 다음과 같은 상황이 발생합니다:

- 멀티채널 메시지에서 동일한 프로모션 코드가 여러 채널에 걸쳐 사용됩니다.
- 메시지가 실패하거나 중단된 경우에는 추가 프로모션 코드가 사용되지 않습니다.

사용자가 Liquid 조건부 논리 태그로 분할된 하나의 메시지에서 참조되는 두 개의 프로모션 코드 목록이 있는 경우, 사용자가 어떤 조건부 흐름을 따르는지에 관계없이 모든 프로모션 코드가 차감됩니다.

사용자가 새 캔버스 단계에 들어가거나 캔버스에 다시 들어가서 해당 사용자에게 보내는 메시지에 프로모션 코드 리퀴드 스니펫이 다시 적용되면 새 프로모션 코드가 사용됩니다.

### 사용 사례

다음 예의 경우 프로모션 코드 목록 `vip-deal` 및 `regular-deal` 모두 차감됩니다. 여기 Liquid가 있습니다.

{% raw %}
```
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %} 
```
{% endraw %}

Braze는 예상 사용량보다 더 많은 프로모션 코드를 업로드할 것을 권장합니다. 프로모션 코드 목록이 만료되거나 프로모션 코드가 부족하면 후속 메시지가 중단됩니다.

{% alert tip %}
**다음은 Braze에서 프로모션 코드가 어떻게 사용되는지에 대한 비유입니다.** <br><br>메시지를 보내는 것이 우체국에서 편지를 보내는 것과 같다고 상상해 보세요. 편지를 점원에게 전달하면 편지에 쿠폰이 포함되어 있어야 한다는 것을 점원이 확인합니다. 점원은 더미에서 첫 번째 쿠폰을 꺼내 봉투에 넣습니다. 점원이 편지를 보냈지만 어떤 이유에서인지 편지가 우편물에서 분실되었습니다(쿠폰도 분실되었습니다). <br><br>이 시나리오에서 Braze는 우체국 직원이고 프로모션 코드는 쿠폰입니다. 웹훅 결과에 관계없이 프로모션 코드 스택에서 가져온 후에는 다시 가져올 수 없습니다.
{% endalert %}

## 자주 묻는 질문

### 프로모션 코드와 함께 사용할 수 있는 메시징 채널은 무엇인가요?

프로모션 코드는 현재 이메일, 모바일 푸시, 웹 푸시, 콘텐츠 카드, 웹훅, SMS 및 WhatsApp에서 지원됩니다. Braze 거래 이메일 캠페인과 인앱 메시지는 현재 프로모션 코드를 지원하지 않습니다.

### 테스트 전송 및 시드 전송으로 프로모션 코드가 소진되나요?

기본적으로 테스트 전송 및 시드 그룹 이메일 전송에는 사용자별, 테스트 전송당 프로모션 코드가 사용됩니다. 그러나 테스트 중에는 프로모션 코드를 사용하지 않도록 Braze 계정 관리자에게 연락하여 이 동작을 업데이트할 수 있습니다.

### 멀티채널 캠페인 또는 캔버스 단계에서 프로모션 코드는 어떻게 작동하나요?

프로모션 코드는 메시지가 전송되기 전에 차감됩니다. 캠페인 또는 캔버스에서 보내는 메시징 채널에서 방해금지 시간, 사용량 제한, 최대 게재빈도 설정, 종료 기준 등의 이유로 프로모션 코드가 사용될 수 있습니다. 단, 메시지 채널 중 하나라도 전송되는 경우 하나의 프로모션 코드가 사용됩니다.

### 내 메시지에 동일한 프로모션 코드 목록을 참조하는 리퀴드 스니펫이 여러 개 있으면 어떻게 되나요?

메시지의 모든 Liquid 스니펫 인스턴스에 대해 동일한 프로모션 코드가 템플릿화됩니다.

### 프로모션 코드 목록이 만료되었거나 비어 있으면 어떻게 되나요?

만료된 코드는 6개월 후에 삭제됩니다.

메시지에 비어 있거나 만료된 목록의 프로모션 코드가 포함되어 있어야 하는 경우 메시지가 취소됩니다. 

메시지에 조건부로 프로모션 코드를 삽입하는 Liquid 로직이 포함된 경우, 메시지에 프로모션 코드가 포함되어 있어야 하는 경우에만 메시지가 취소됩니다. 메시지에 프로모션 코드가 포함되어 있지 않아야 하는 경우 메시지가 정상적으로 전송됩니다.

### 후속 메시지에 사용할 수 있도록 프로모션 코드를 사용자 프로필에 저장하려면 어떻게 해야 하나요?

이후 메시지에서 동일한 프로모션 코드를 참조하려면 코드를 사용자 프로필에 사용자 지정 속성으로 저장해야 합니다. 이는 동일한 캠페인 또는 캔버스 메시지 단계에 [Braze-to-Braze 웹훅을]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/) 연결하여 수행할 수 있습니다.

