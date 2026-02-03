---
nav_title: 코드를 생성하세요
article_title: 프로모션 코드를 생성하세요
page_order: 0.1
description: "캠페인과 캔버스에서 프로모션 코드를 생성하는 방법을 배우세요."
---

# 프로모션 코드를 생성하세요

> 캠페인과 캔버스에서 프로모션 코드를 생성하는 방법을 배우세요.

## 프로모션 코드 목록 생성 {#create}

### 1단계: 새 목록 생성

대시보드에서 **데이터 설정** > **프로모션 코드**로 이동한 다음 **프로모션 코드 목록 생성**을 선택하세요.

![프로모션 코드를 생성하는 버튼입니다.]({% image_buster /assets/img/promocodes/promocode1.png %})

### 2단계: 세부 정보 입력

1. 프로모션 코드 목록의 이름을 지정하고 선택 사항인 설명을 추가합니다.
2. 다음으로 프로모션 코드에 대한 코드 스니펫을 생성합니다. 

코드 조각을 만들 때 고려해야 할 몇 가지 세부 사항은 다음과 같습니다:

- 저장한 후에는 코드 스니펫을 편집할 수 없습니다.
- 스니펫은 대소문자를 구분합니다. 예를 들어, 시스템은 "Birthday_promo"과 "birthday_promo"를 두 개의 다른 스니펫으로 인식합니다.
- Liquid에서 스니펫 이름을 사용하여 이 프로모션 코드 세트를 참조하세요.
- 코드 스니펫이 다른 목록에서 이미 사용되고 있지 않은지 확인하세요.

![코드 스니펫 "spring25"가 있는 "SpringSale2025"라는 이름의 프로모션 코드 목록입니다.]({% image_buster /assets/img/promocodes/promocode3.png %}){: style="max-width:80%"}

### 3단계: 프로모션 코드 옵션 선택

각 프로모션 코드 목록에는 생성 시 설정되는 해당 만료 날짜와 시간이 있습니다. 최대 만료 기간은 목록을 생성하거나 편집하는 날로부터 6개월입니다.

해당 기간 내에 만료일을 반복해서 변경하고 업데이트할 수 있습니다. 이 만료 날짜는 이 목록에 추가된 모든 코드에 적용됩니다. 만료되면, 코드는 Braze 시스템에서 삭제되며, 해당 목록의 코드 스니펫을 호출하는 메시지는 전송되지 않습니다.

![모든 남은 코드가 2025년 4월 30일 오전 12시에 만료되는 목록 만료 설정입니다.]({% image_buster /assets/img/promocodes/promocode4.png %}){: style="max-width:80%"}

임계값 알림을 선택 사항으로 설정하고 사용자 지정할 수도 있습니다. 설정된 경우, 이러한 알림은 목록에 있는 프로모션 코드가 부족하거나 프로모션 코드 목록이 만료에 가까워질 때 지정된 수신자에게 이메일을 보냅니다. 수신자는 하루에 한 번 알림을 받습니다.

![프로모션 코드 목록이 5일 후에 만료될 때 "marketing@abc.com"에게 알리기 위한 임계값 알림의 예입니다.]({% image_buster /assets/img/promocodes/promocode5.png %}){: style="max-width:80%"}

### 4단계: 프로모션 코드 업로드

Braze doesn't manage code creation or redemption, meaning you must generate your promotion codes to a CSV file and upload them to Braze. 

CSV 파일이 다음 가이드라인을 따르고 있는지 확인하세요:

- 프로모션 코드에 대한 열이 포함되어 있습니다.
- 행당 하나의 프로모션 코드가 있습니다.

You can use our built-in integration with [Voucherify]({{site.baseurl}}/partners/ecommerce/loyalty/voucherify/) or [Talon.One]({{site.baseurl}}/partners/ecommerce/loyalty/talonone/) to create and export promotion codes.

{% alert important %}
최대 파일 크기는 100MB, 최대 목록 크기는 사용하지 않은 코드의 20밀리미터입니다. 잘못된 파일이 업로드된 경우, 이전 파일을 대체할 새 파일을 업로드하세요.
{% endalert %}

1. 업로드가 완료되면 **목록 저장을** 선택하여 방금 입력한 모든 세부 정보와 코드를 저장합니다.

!["springsale"라는 이름의 CSV 파일이 성공적으로 업로드되었습니다.]({% image_buster /assets/img/promocodes/promocode7.png %})

{:start="2"}
2\. 저장 선택 후, **Import History**에 새로운 행이 나타납니다.
3\. 가져오기가 완료되었는지 확인하기 위해 표를 새로 고치려면 표 상단에서 <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **동기화를** 선택합니다.

![업로드 중인 프로모션 코드.]({% image_buster /assets/img/promocodes/promocode8.png %})

{% alert note %}
더 큰 파일은 가져오는 데 몇 분이 걸립니다. 기다리는 동안 페이지에서 나가서 가져오기가 진행되는 동안 다른 작업을 할 수 있습니다. 가져오기가 완료되면, 테이블의 상태가 **Complete**로 변경됩니다.
{% endalert %}

## 프로모션 코드 목록 업데이트

목록을 업데이트하려면 기존 목록 중 하나를 선택합니다. 이름, 설명, 목록 만료 및 임계값 알림을 변경할 수 있습니다. 새 파일을 업로드하고 **목록 업데이트**를 선택하여 목록에 코드를 더 추가할 수도 있습니다. 목록의 모든 코드는 가져온 날짜와 관계없이 동일한 만료일을 가집니다.

{% alert important %}
프로모션 코드는 삭제할 수 없습니다.
{% endalert %}

### 잘못된 프로모션 코드 목록 수정하기 

잘못된 프로모션 코드가 포함된 CSV 파일을 업로드하고 **Save list**를 선택한 경우, 다음 방법 중 하나로 해결할 수 있습니다:

- 전체 목록 폐기하기: 현재 프로모션 코드 목록을 캠페인, 캔버스 또는 템플릿에서 사용 중지합니다. 그런 다음, 올바른 코드가 포함된 CSV 파일을 업로드하고 메시징에 사용합니다.
- 잘못된 코드 사용하기: 잘못된 프로모션 코드 목록에서 프로모션 코드를 플레이스홀더로 보내는 캠페인을 생성하여 모든 잘못된 코드가 사용될 때까지 기다립니다. 그런 다음, 동일한 목록에 올바른 프로모션 코드를 업로드합니다.
