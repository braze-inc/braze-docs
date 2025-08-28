---
nav_title: Gmail 프로모션 설정
article_title: Gmail 프로모션 설정
page_order: 8
description: "이 참조 문서에서는 Braze를 사용하여 이메일 캠페인에서 Gmail 모바일 프로모션 카드를 빌드하는 방법을 설명합니다."
channel:
  - email

---

# Gmail 프로모션 설정

> The [Gmail mobile Promotions tab](https://developers.google.com/gmail/promotab/) allows marketers to send more information via annotations in a "card" rather than just the subject line or preheader information. Braze에는 이메일 캠페인에서 카드를 빌드하는 데 도움이 되는 내장 도구가 있습니다.

## 필수 조건

먼저, 도메인과 하위 도메인을 Google의 프로모션 탭 아웃리치 팀 <a href="mailto:p-promo-outreach@google.com">p-promo-outreach@google.com</a>에 전달하여 Gmail의 허용 목록에 추가하세요. 이를 통해 Gmail 프로모션 탭의 제품 캐러셀과 같은 풍부한 이미지를 보여주는 모든 기능을 사용할 수 있습니다.

## Braze로 카드를 만들기

이 단계를 따라 이메일 캠페인을 위한 Gmail 프로모션 카드를 구축하세요. 편집기에서 **콘텐츠** 섹션을 벗어나면 **Gmail 프로모션** 탭의 필드와 정보가 초기화됩니다. 프로모션 카드의 설정을 완료하고 생성된 HTML을 복사하여 HTML 코드를 잃지 않도록 하세요.

1. [Create your email campaign]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/), and select the **HTML Editor** as your editing experience.
2. HTML 편집기에서 **콘텐츠** 섹션으로 이동하여 **Gmail 프로모션** 탭을 선택합니다.
3. **기본 정보** 아래 필드를 작성한 다음 **HTML 코드 생성<2>를 클릭하십시오. 이것은 **HTML 코드 `<Head>`** 섹션에 복사하여 붙여넣기하여 Gmail 프로모 탭 카드의 스크립트를 생성하는 데 도움이 됩니다. <br> ![An example of how to build a card.]({% image_buster /assets/img/create-gmail-promo.png %})
4. 할인 혜택만, 프로모션 카드만 또는 둘 다 포함할지 선택하세요. <br> ![Options to include a discount offer and promotion cards.]({% image_buster /assets/img_archive/gmail_promo_discount.png %}){: style="max-width:70%;"}
5. 스크립트를 이메일 HTML의 `<head>` 요소에 복사하여 붙여넣으세요.

{% alert warning %}
프로모션 스크립트는 이메일이 Gmail 프로모션 탭에 도착한 경우에만 나타납니다. 현재 Gmail은 알고리즘을 사용하여 이메일이 어디에 도착할지 결정합니다. 그러나 사용자가 이메일을 프로모션으로 표시하면 Gmail의 알고리즘이 무시되고 이메일이 자동으로 프로모션 탭으로 이동합니다.
{% endalert %}

### 할인 혜택 포함

할인 혜택을 설정하면 할인의 유효 날짜를 지정할 수 있습니다. 할인 혜택을 결정한 후 시작 날짜와 시간을 선택하십시오. 할인 혜택을 특정 시간에 종료하거나, 종료하지 않도록 선택할 수 있습니다.

![Options to specify the offer value, code, and start date and time for a discount offer.]({% image_buster /assets/img/gmail_promo_discount_details.png %}){: style="max-width:70%;"}

### 제품 캐러셀 사용자 정의

제품 캐러셀의 프로모션 카드는 귀하의 제안에 이미지를 제공하는 데 유용합니다. 제품 캐러셀에서 변수를 커스텀하고 최대 10개의 이미지 미리보기를 포함할 수 있으며, 각 이미지는 고유합니다.

![An example of a product carousel from a company named Motto with the email heading "Our best selling socks are on sale", with three images of socks and their discounted prices.]({% image_buster /assets/img_archive/product_carousel.png %}){: style="max-width:40%;"}

| 사용자 정의 변수 | 설명 |
|---|---|
| 이미지 URL | 귀하의 이미지에 대한 URL. 제품 캐러셀의 각 이미지에는 고유한 URL이 있어야 하며 동일한 종횡비(4:5, 1:1, 1.91:1)를 사용해야 합니다. |
| 대상 URL | 프로모션 링크입니다. |
| 헤드라인 | (선택 사항) 프로모션에 대한 한두 문장 설명. 미리보기 이미지 아래에 표시됩니다. |
| 통화 | (optional) 가격의 통화. |
| 가격 | 프로모션의 가격. |
| 할인 가격 | 원래 가격에서 할인된 금액. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
제품 이미지를 미디어 라이브러리에 업로드한 후 URL을 적절한 필드에 복사하여 붙여넣는 것을 권장합니다. 정적 이미지 형식(PNG 및 JPEG)만 허용됩니다. 일부 이미지 형식(GIF)은 업로드되지만 예상대로 표시되지 않습니다.
{% endalert %}

### 모범 사례

In general, adhere to these [best practices recommended by Gmail](https://developers.google.com/gmail/promotab/best-practices). 

{% alert tip %}
이 스크립트 내에서 Liquid을 사용할 수 있지만 오류를 피하기 위해 가능한 한 메시징을 많이 테스트하는 것이 좋습니다.
{% endalert %}

#### 이미지 통합

Gmail은 이메일 메시지와 관련된 강력한 이미지로 더 나은 결과를 보았습니다. Gmail은 텍스트 전용 디자인 사용을 권장하지 않습니다. 이 공간은 시각적 언어를 미리 보기로 가져오는 것이며, 이는 이메일 마케팅에 필수적입니다. 잘린 텍스트가 포함된 이미지를 사용하거나 여러 캠페인에서 이미지를 반복 사용하지 마세요.

#### 제안을 설명하기

Gmail은 "1+1 구매 가능" 또는 "모든 반바지와 셔츠 할인"과 같은 문장이나 구를 사용하지 않는 것이 좋습니다. 이는 제목란과 경쟁하고 눈에 띄지 않게 되며, 잘리지 않을 수 있습니다. 이 공간은 고객과 메시징으로 소통하는 데만 사용해야 하므로 "지금 이 이메일을 열어보세요" 또는 "여기에서 거래를 클릭하세요"와 같은 언어는 피하세요. 제목란을 반복하지 않는 것이 좋습니다.

## 자주 묻는 질문

### 내 프로모션 메시지가 최종 사용자의 받은편지함에 프로모션 카드나 제품 캐러셀을 표시하지 않는 이유는 무엇입니까?

제품 캐러셀을 Gmail 프로모션 탭에 표시할지 여부를 결정하는 많은 요소가 있습니다.

모든 주석 이미지들은 여전히 품질 필터를 통과해야 합니다. 제품 캐러셀이 채워지려면 주석의 모든 이미지가 권장 이미지 종횡비, 고품질 또는 고해상도 클로즈업 제품 이미지여야 합니다. 이미지에는 텍스트가 거의 없거나 전혀 없어야 합니다(바람직함). 품질 필터는 부적절한 콘텐츠도 필터링하므로 이미지는 가족, 사용자 및 아동 친화적이어야 합니다.

게다가 Gmail은 사용자의 Gmail 프로모션 탭에 표시되는 제품 캐러셀 수에 밀도 제한을 두고 있습니다. 예를 들어, 사용자가 프로모션 이메일에서 제품 캐러셀을 사용하는 많은 브랜드를 구독하는 경우, Gmail은 결국 표시되는 제품 캐러셀의 수에 제한을 둡니다.

Google의 개인정보 보호 및 안전 규정으로 인해 주석이 있는 이메일은 주석이 작동하려면 널리 전송되어야 합니다. Google의 시스템이 이를 "대량 발송"으로 감지하도록 캠페인을 시작하고 최소 100명의 수신자에게 보내는 것이 좋습니다. 이미지 URL은 수신자에 따라 다르지 않을 수 있습니다.

### 프로모션 카드 또는 제품 캐러셀의 클릭은 어떻게 추적되나요?

Braze 또는 다른 ESP는 헤더 섹션의 링크에 링크 추적을 삽입할 수 없습니다. 이는 프로모션 카드 또는 제품 캐러셀에서 클릭을 추적할 수 없음을 의미합니다.

### 사용자가 제품 캐러셀을 받은 수를 확인할 수 있는 방법이 있습니까?

Gmail은 카드를 표시할 시기와 대상을 결정하므로 모든 수신자가 제품 캐러셀을 볼 수 있다는 보장은 없습니다.

