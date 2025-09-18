---
nav_title: NiftyImages
article_title: NiftyImages
description: "NiftyImages와 Braze를 통합하는 방법을 알아보세요."
alias: /partners/niftyimages/
page_type: partner
search_tag: Partner
---

# NiftyImages

> [NiftyImages](https://niftyimages.com)는 마케터가 관련성 높은 최신 이메일 커뮤니케이션을 보다 효율적으로 전송하는 동시에 인게이지먼트와 매출을 높일 수 있도록 지원하는 실시간 이메일 개인화 소프트웨어입니다. 마케터가 쉽고 빠르게 이메일에 동적 콘텐츠를 추가할 수 있는 사용자 친화적인 셀프 서비스 도구입니다.

_이 통합은 NiftyImages에서 유지 관리합니다._

## 전제 조건

NiftyImages는 통합할 필요 없이 기본 Braze 플랫폼에서 작동합니다. 시작하려면 [NiftyImages 계정](https://niftyimages.com/Signup)만 있으면 됩니다.

## 지원되는 기능

Braze에서 NiftyImages를 활용하면 기존 Braze 개인화 태그를 NiftyImages URL에 매핑하여 이메일 캠페인을 위한 동적이고 개인화된 이미지를 만들 수 있습니다.

- **개인정보 보호:** 모든 데이터는 NiftyImages가 아닌 Braze에 저장됩니다.
- **개인화된 이미지:** Braze 병합 태그를 사용하여 이미지를 맞춤 설정할 수 있습니다.
- **차트 및 그래프:** 사용자 지정 가능한 차트와 그래프를 통해 티어 레벨, 고객 상태, 지출 금액, 포인트 등을 표시하세요.
- **맵:** 사용자가 이메일을 여는 가장 가까운 위치를 사용하여 맵 이미지를 표시합니다.
- **사용자 지정 카운트다운 타이머:** 생일, 평가판 만료일, 마지막 구매 날짜, 연체된 청구서 또는 마지막 로그인 날짜에 대한 날짜 데이터베이스 변수를 사용하여 고유한 타이머를 표시합니다.
- **실시간 콘텐츠:** 제품 추천, 장바구니 유기, 가격 인하, 재고 수준, 날씨 등을 실시간 이미지로 표시합니다.
- **실시간 투표:** 실시간 투표를 표시하여 인게이지먼트를 촉진하고 관심 수준에 대한 인사이트를 확보합니다.
- **규칙 기반 로직:** 사용자 데이터, 인구 통계, 행동, 위치, 시간, 요일, 여는 기기, 운영 체제 등을 기반으로 동적 이미지를 표시합니다.

예를 들어 다음은 고객의 이름을 사용하여 NiftyImages에서 생성한 커스텀 이미지입니다.

![ALT_TEXT.]({% image_buster /assets/img/niftyimages/1.png %}){: style="max-width:70%;"}

## NiftyImage 생성

### 1단계: 병합 태그 만들기

NiftyImages에서 병합 태그를 선택한 다음 기본값을 입력합니다. 완료했으면 **다음**을 선택합니다.

![대체 텍스트]({% image_buster /assets/img/niftyimages/2.png %}){: style="max-width:70%;"}

선택적으로 데이터 유형을 입력한 후 **다음**을 선택합니다.

![대체 텍스트]({% image_buster /assets/img/niftyimages/3.png %})
{: style="max-width:70%;"}

원하는 경우 나중에 사용할 수 있도록 태그를 저장하도록 선택할 수 있습니다. 완료했으면 **저장을** 선택하여 병합 태그를 만듭니다.

![대체 텍스트]({% image_buster /assets/img/niftyimages/4.png %}){: style="max-width:70%;"}

### 2단계: 이미지 사용자 지정

이미지의 글꼴, 글꼴 크기, 위치, 색상, 레이어링 등을 사용자 지정할 수 있습니다. 완료되면 이미지 URL을 복사합니다.

![대체 텍스트]({% image_buster /assets/img/niftyimages/5.png %})

### 3단계: Braze에 이미지 URL 추가

Braze에서 캠페인 또는 캔버스를 연 다음 NiftyImage URL을 붙여넣습니다. 선택 사항으로 변경 사항을 미리 보고 Liquid 태그를 확인할 수 있습니다.


![대체 텍스트]({% image_buster /assets/img/niftyimages/6.png %})
