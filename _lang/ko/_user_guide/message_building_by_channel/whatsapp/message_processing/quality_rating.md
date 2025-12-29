---
nav_title: 품질 등급 및 메시징 한도
article_title: 품질 등급 및 메시징 한도 
description: "이 참조 문서에서는 Meta가 WhatsApp 채널에 대한 품질 등급 및 메시징 한도에 어떤 영향을 미치는지 설명합니다."
page_type: partner
search_tag: Partner
page_order: 
channel:
  - WhatsApp
---

# 품질 등급 및 메시징 한도

> Meta는 WhatsApp 채널을 사용하기 시작하는 순간부터 귀하의 품질 등급 및 [메시징 한도](https://developers.facebook.com/docs/whatsapp/messaging-limits)에 영향을 미치며, 귀하의 WhatsApp 사용에 따라 계속해서 영향을 미칩니다.

## 정의

| 단어 | 정의 |
| --- | --- |
| 품질 등급 | 고객이 지난 7일 동안 받은 최근 메시지를 기반으로 한 등급입니다. 이 등급은 고객의 피드백에 따라 결정되며, 전화번호 차단 사유 및 기타 신고 문제와 같은 요소가 포함됩니다. Meta의 문서를 참조하여 [품질 등급에 대한 자세한 내용](https://www.facebook.com/business/help/896873687365001)을 알아보세요.|
| 메시징 한도 | 각 전화번호로 시작할 수 있는 비즈니스 주도 대화의 최대 수로, 24시간 주기 내에서 적용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 }

## 온보딩  

새 WhatsApp 비즈니스 계정이 생성되면, Meta는 초기 전송 한도를 결정하기 위해 다양한 요소를 사용합니다. WhatsApp 비즈니스 관리자에서 이 한도를 확인할 수 있으며, 전화번호 통찰력 페이지에서 추가 세부정보를 확인할 수 있습니다. 

Meta의 문서를 참조하여 [한도 확인](https://developers.facebook.com/docs/whatsapp/messaging-limits#checking-your-limit) 및 [전화번호 요구 사항](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)에 대한 자세한 내용을 알아보세요.

## 처리량

Meta는 등록된 각 비즈니스 전화번호에 대해 초당 80개의 메시지 처리량으로 시작합니다. 초당 1,000개의 메시지로 업그레이드가 자동으로 또는 요청에 따라 발생할 수 있습니다. 정보. 

당신의 [처리량](https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput)에 대해 더 알아보려면 Meta의 문서를 참조하세요.

## 템플릿 속도 조절

최근에 생성된 마케팅 템플릿과 일시 중지된 마케팅 템플릿이 다시 활성화되면 속도 조절의 대상이 될 수 있습니다. Meta의 속도 조절 선택 기준은 주로 템플릿 품질 이력에 의해 결정됩니다. 최근에 생성된 마케팅 템플릿이나 최근에 다시 활성화된 마케팅 템플릿을 사용할 때, 메시지는 특정 임계값에 도달할 때까지 정상적으로 전송됩니다. 이 임계값에 도달한 후, 해당 템플릿을 사용하는 후속 메시지는 고객 피드백을 받을 충분한 시간을 허용하기 위해 보류됩니다. 

당신의 [템플릿 속도 조절](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#template-pacing)에 대해 더 알아보려면 Meta의 문서를 참조하세요.