---
nav_title: 바우처 및 프로모션 코드 목록
article_title: Voucherify 및 Braze 프로모션 코드 목록
page_order: 4
alias: /partners/voucherify/promotion/
description: "이 참고 문서에서는 Braze 프로모션 코드 스니펫을 사용하여 바우처파이 코드를 공유하는 방법에 대해 설명합니다."
page_type: partner
search_tag: Partner
---

# Voucherify 및 Braze 프로모션 코드 목록

> 연결된 콘텐츠 및 사용자 지정 속성 외에도 Braze 프로모션 코드 스니펫을 사용하여 바우처파이 코드를 공유할 수 있습니다. 먼저, Voucherify에서 코드를 내보내고, Braze로 코드를 가져온 다음, 이메일 코드 스니펫을 추가하여 프로모션 목록에서 코드를 가져옵니다. 

_This integration is maintained by Voucherify._

## 1단계: Voucherify에서 고유 코드 내보내기

Voucherify에서 Voucherify 캠페인으로 이동합니다. 그런 다음, **CSV로 내보내기**를 선택하고 CSV 파일을 편집하고 열의 이름을 제거하여 코드 목록만 남깁니다.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_export_codes.png %}){: style="margin-top:15px;"}

## 2단계: 프로모션 코드 목록 만들기

**데이터 설정** > **프로모션 코드**로 이동하여 **프로모션 코드 목록 생성**을 클릭합니다.

Voucherify 캠페인 이름을 사용하여 목록의 이름을 지정하고 데이터 일관성을 확인할 수 있습니다.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_code_list.png %}){: style="max-width:50%;"}

그런 다음 목록의 코드를 참조하는 코드 스니펫을 추가하면 메시지가 전송될 때 고유 코드로 채워집니다.

### 추가 설정

목록 만료 및 임계치 알림과 같은 코드에 대한 속성을 설정할 수도 있지만, 목록 설정과 관계없이 Voucherify는 코드 이면의 로직을 관리한다는 점에 유의하세요.

![목록 만료]({% image_buster /assets/img/voucherify/voucherify_promotion_list_expiration.png %})

## 3단계: CSV 파일 업로드

Voucherify 코드가 포함된 CSV 파일을 업로드합니다.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_import_codes.png %})

목록에 열 헤더가 아닌 코드만 포함되어 있는지 확인하고 **업로드 시작**을 클릭합니다. 가져오기가 완료되면 **목록 저장을** 클릭하여 목록 세부 정보를 확인합니다.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_upload_csv.png %}){: style="max-width:50%;"}

## 4단계: Braze 캠페인에서 코드 스니펫 사용

Braze 캠페인에서 목록의 코드를 사용하려면 스니펫을 복사하여 이메일 본문에 추가합니다.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_code_snippet.png %}){: style="max-width:50%;"}

코드 스니펫을 추가하여 목록에서 코드를 표시합니다.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_liquid_email.png %})

코드가 포함된 메시지가 전송된 후에는 동일한 코드가 다시는 사용되지 않습니다.

