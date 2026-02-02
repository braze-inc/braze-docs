---
nav_title: "사용자 전화번호"
article_title: WhatsApp 사용자 전화번호
page_order: 1.5
description: "이 참조 문서는 WhatsApp 전화번호 형식, 전화번호 가져오기 방법 및 사용자를 WhatsApp 구독 그룹에 추가하는 방법을 다룹니다."
page_type: reference
channel: 
  - WhatsApp
  
---

# 사용자 전화번호

> 이 기사에서는 사용자의 전화번호 또는 고객의 전화번호와 관련된 다양한 주제를 다룰 것입니다.

전화번호는 고객 프로필에 현지 형식으로 표시되지만, 번호를 가져오는 데 사용하는 형식은 아닙니다(`(724) 123 4567`).

## 전화번호 가져오기

CSV를 [업로드]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) 또는 [API를 통해]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) 전화번호를 가져와 사용자를 생성할 수 있습니다.

### 서식 지정

비-U.S 숫자를 [`E.164`](https://en.wikipedia.org/wiki/e.164) 형식으로 가져오는 것이 중요하며, “+” 및 국가 코드가 포함됩니다. 이 형식으로 제공되지 않은 모든 전화번호는 미국 번호로 해석됩니다.  

전화번호가 E.164 형식으로 강제 변환되었지만 유효성 검사를 통과하지 못하면 Braze는 이 번호로 WhatsApp 메시지를 보낼 수 없습니다. 전화번호 형식을 지정할 수 없는 사용자는 WhatsApp이 포함된 캔버스 단계에서 자동으로 종료됩니다.

모든 U.S. 숫자는 유효한 지역 코드가 있는 10자리 전화번호여야 합니다. `+` 및 국가 코드 없이 입력할 수 있으며, Braze는 모든 유효한 10자리 전화번호를 U.S 번호로 가정하고 매핑합니다.

모든 국제 번호는 `+`로 시작하고 그 뒤에 해당 국가 코드와 전화번호를 입력해야 합니다. (e.g `+442071838750`)

![]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

그러나 국가 또는 지역 번호가 다른 여러 지역으로 보내는 경우 정확성을 보장하기 위해 U.S.기반 전화번호라도 `E.164` 형식을 사용하는 것이 좋습니다.

다음 표에서 로컬 숫자 형식과 범용 `E.164` 형식의 차이점을 볼 수 있습니다:

| 국가 | 로컬 | 국가 코드 | `E.164` |
|---|---|---|---|
| USA | `4155552671` | 1 | `+14155552671` |
| 영국 | `02071838750` | 44 | `+442071838750` |
| 브라질 | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 reset-td-br-4}

### WhatsApp 구독 그룹에 사용자 추가

고객이 WhatsApp 메시지를 받으려면 유효한 전화번호를 가지고 구독 그룹에 가입해야 합니다. 자세한 내용은 [WhatsApp 구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/)을 참조하세요.


### 같은 전화번호를 사용하는 여러 사용자

여러 사용자가 단일 캠페인 또는 캔버스 단계의 세그먼트 내에서 동일한 전화번호를 가지고 있는 경우, Braze는 발송을 중복 제거하고 해당 전화번호로 하나의 메시지만 보냅니다. 


