---
nav_title: 메시지 유형
article_title: 라인 메시지 유형
page_order: 0
description: "이 기사는 다양한 유형의 LINE 메시지를 다룹니다."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/message_types/
---

# LINE 메시지 유형

> 이 기사에서는 작성할 수 있는 LINE 메시지 유형과 그 측면 및 제한 사항을 다룹니다.

LINE 메시지를 작성할 때, 메시지 유형을 작성기 안으로 드래그 앤 드롭한 다음, 이를 사용자 정의할 수 있습니다.

![Message types panel with message types to drag into the composer editor, including text, image, rich message, and card-based message.]({% image_buster /assets/img/line/line_message_types.png %}){: style="max-width:40%;"}

## 텍스트

LINE 텍스트 메시지는 최대 5,000자까지 포함할 수 있으며 이모지와 Liquid 개인화를 포함할 수 있습니다.

사용 사례에는 다음이 포함됩니다:
- 한정 기간 동안 재고 정리를 위한 프로모션을 발표합니다.
- 생일 축하 메시지를 개인화된 프로모션 카드로 보내세요.
- 다가오는 이벤트에 대한 빠른 업데이트를 공유하세요.

![A text message reminding the user not to forget about a Black Friday party and the potential to save up to 80% before midnight.]({% image_buster /assets/img/line/line_text_message.png %}){: style="max-width:40%;"}

## 이미지

LINE 이미지 메시지는 미디어 라이브러리, URL 또는 Liquid를 통해 추가할 수 있습니다. 이 이미지는 독립적이며 클릭 가능한 링크가 포함되어 있지 않습니다.

사용 사례에는 다음이 포함됩니다:
- 사용자들이 비행기 티켓 구매를 고려하도록 영감을 주기 위해 휴가 여행지를 선보입니다.
- 시즌 종료 프로모션을 강조하여 사용자들이 내년 겨울 옷을 좋은 가격에 미리 준비하도록 유도하세요.
- 상점 전체 연례 세일을 위한 시각적 카운트다운을 시작하세요.

![An image message promoting a toaster sale.]({% image_buster /assets/img/line/line_image_message.png %}){: style="max-width:40%;"}

### URL 이미지

사용 사례에 통합된 URL 이미지를 사용하십시오:
- 이미지 소스 속성에 Liquid를 포함하여 Liquid 동적 이미지를 만듭니다. 예를 들어, 이미지 URL로를 삽입하여 이미지에 사용자의 이름을 포함할 수 있습니다.
- 연결된 콘텐츠는 웹 서버 또는 공개적으로 접근 가능한 API에서 이미지를 직접 가져오는 것입니다.
- CSV 파일 및 API 엔드포인트에서 가져온 이미지를 통해 브레이즈 카탈로그를 액세스합니다.

| **사양** | 추천 속성 |
|--------------------------|----------------------------|
| 이미지 파일 URL 길이 | 최대 2,000자  |
| 이미지 형식          | PNG, JPEG             |
| 파일 크기     |  최대 10MB |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 부유한 메시지 (이미지 맵)

라인 리치 메시지는 이미지로, 이미지의 특정 영역을 선택하여 열 수 있는 하나 이상의 링크를 포함합니다. 이미지에 링크가 매핑되는 방식을 선택할 수 있는 다양한 메시지 템플릿을 선택하세요.

사용 사례에는 다음이 포함됩니다:
- 신규 도착한 핸드백의 그리드를 표시하고 각 가방의 해당 제품 페이지에 대한 링크를 제공합니다.
- 항목을 선택하여 콤보 주문을 시작하는 대화형 메뉴를 제공합니다.
- 사용자가 그리드 사각형을 선택하여 선택할 수 있는 여러 프로모션을 배치합니다.

![A six-square rich message with a photo of a black-and-white grid that users can tap to receive a random offer.]({% image_buster /assets/img/line/line_rich_message.png %})

### 이미지 맵 

| **사양** | 추천 속성 |
|--------------------------|----------------------------|
| 이미지 파일 URL 길이 | 최대 2,000자  |
| 이미지 형식          | PNG (투명 가능), JPEG             |
| 종횡비          | 1:1 (너비:높이)
| 파일 크기     |  최대 10MB |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### URI 링크 

| **사양** | 추천 속성 |
|--------------------------|----------------------------|
| 문자 수      | 1,000 최대 |
| 계획              | HTTP, HTTPS, LINE, tel |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 텍스트 

400자까지 포함할 수 있는 풍부한 메시지입니다.

## 카드 기반 (캐러셀)

LINE 카드 기반 메시지는 사용자가 캐러셀처럼 여러 메시지를 스크롤하고, 카드나 카드의 버튼을 선택하여 자신에게 가장 관련 있는 메시지에 대해 행동을 취할 수 있게 합니다.

사용 사례에는 다음이 포함됩니다:
- 특정 메뉴 항목에 대한 프로모션 표시
- 이번 시즌의 베스트셀러 재킷을 강조하세요.
- 요리 도구와 기구의 샘플을 키트에 포함된 것들로 제시합니다.

![A card-based message with at least two cards that promote sandwiches in the composer editor.]({% image_buster /assets/img/line/line_card_message.png %})

### 메시지

| **사양** | 추천 속성 |
|--------------------------|----------------------------|
| 열                  | 10 최대 |
| 종횡비             | 사각형 1.51:1 <br> 정사각형 1:1  |
| 제목                    | 최대 40자
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


### 이미지

| **사양** | 추천 속성 |
|--------------------------|----------------------------|
| 이미지 URL                 | 최대 2,000자 |
| 이미지 형식              | JPEG 또는 PNG |
| 폭                     | 1,024 픽셀  |
| 파일 크기                 | 1MB |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


### 텍스트

| **사양** | 추천 속성 |
|-------------------------|----------------------------|
| 문자              | 120 최대 (이미지나 제목 없음) <br> 60 최대 (이미지 또는 제목이 있는 메시지)  |
| 행동                 | 최대 3 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


