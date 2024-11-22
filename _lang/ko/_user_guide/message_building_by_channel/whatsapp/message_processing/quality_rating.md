---
nav_title: 품질 등급 및 메시지 제한
article_title: 품질 등급 및 메시지 제한 
description: "이 참고 문서에서는 메타가 WhatsApp 채널의 품질 등급 및 메시징 제한에 미치는 영향에 대해 설명합니다."
page_type: partner
search_tag: Partner
page_order: 
channel:
  - WhatsApp
---

# 품질 등급 및 메시징 제한

> 메타는 WhatsApp 채널을 사용하기 시작하는 순간부터 품질 등급 및 [메시지 제한](https://developers.facebook.com/docs/whatsapp/messaging-limits)에 영향을 미치며, WhatsApp 사용량에 따라 계속해서 영향을 미칩니다.

## 정의

| Word | 정의 |
| --- | --- |
| 품질 평가 | 지난 7일 동안 고객이 받은 최근 메시지를 기준으로 한 평점입니다. 이 등급은 전화번호 차단 사유 및 기타 신고 문제 등 고객의 피드백에 따라 결정됩니다. [품질 등급](https://www.facebook.com/business/help/896873687365001)에 대해 자세히 알아보려면 메타의 설명서를 참조하세요.|
| 메시징 제한 | 24시간 동안 각 전화번호로 시작할 수 있는 비즈니스 시작 대화의 최대 개수입니다. |
{: .reset-td-br-1 .reset-td-br-2 }

## 온보딩  

새 WhatsApp 비즈니스 계정이 생성되면 메타는 다양한 요소를 사용하여 초기 전송 한도를 결정합니다. 이 한도는 WhatsApp 비즈니스 관리자에서 확인할 수 있으며, 자세한 내용은 전화번호 인사이트 페이지에서 확인할 수 있습니다. 

[한도](https://developers.facebook.com/docs/whatsapp/messaging-limits#checking-your-limit) 및 [휴대폰 번호 요건](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) 확인에 대한 자세한 내용은 메타의 설명서를 참조하세요.

## 처리량

메타는 등록된 각 비즈니스 전화번호를 초당 80개의 메시지 처리량으로 시작합니다. 초당(MPS) 1,000개의 메시지로 자동 또는 요청에 따라 업그레이드할 수 있습니다. 정보. 

[처리량](https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput)에 대해 자세히 알아보려면 메타의 문서를 참조하세요.

## 템플릿 페이싱

최근에 생성된 마케팅 템플릿과 일시 중지된 마케팅 템플릿은 일시 중지 해제될 가능성이 있습니다. 메타의 페이싱 선택 기준은 주로 템플릿 품질 기록에 따라 결정됩니다. 최근에 만든 마케팅 템플릿 또는 최근에 일시 중지하지 않은 마케팅 템플릿을 사용하는 경우 지정되지 않은 임계값에 도달할 때까지 메시지가 정상적으로 전송됩니다. 이 임계값에 도달하면 해당 템플릿을 사용하는 후속 메시지는 고객 피드백을 위한 충분한 시간을 확보하기 위해 보류됩니다. 

[템플릿 페이싱](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#template-pacing)에 대해 자세히 알아보려면 메타 설명서를 참조하세요.