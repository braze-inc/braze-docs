---
nav_title: FAQ
article_title: WhatsApp FAQ
page_order: 80
description: "이 도움말에서는 WhatsApp 캠페인을 설정할 때 가장 자주 발생하는 몇 가지 질문에 대해 설명합니다."
page_type: FAQ
channel:
  - WhatsApp

---

# 자주 묻는 질문

> 이 페이지에서는 WhatsApp에 대한 가장 까다로운 질문에 대한 답변을 드리려고 합니다!<br><br>이 FAQ는 법률 자문을 제공하기 위한 것이 아니며, 법률 자문을 제공하는 것으로 의존해서는 안 됩니다. WhatsApp 채널의 사용에는 특정 Meta Platforms, Inc.의 요구사항이 적용됩니다. 모든 관련 요건과 특히 적용될 수 있는 법률을 준수하여 WhatsApp 채널을 사용하고 있는지 확인하려면 법률 고문의 조언을 구해야 합니다.

## 자주 묻는 질문 주제
- [WhatsApp 비즈니스 계정](#whatsapp-business-accounts)
- [WhatsApp 비즈니스 계정 전화번호](#whatsapp-business-account-phone-numbers)
- [옵트인 및 구독 관리](#opt-in-and-subscription-management) 
- [메시징 제한](#messaging-limits) 
- [WhatsApp 템플릿](#whatsapp-templates)
- [전달 가능성](#deliverability) 
- [기타](#miscellaneous)

### WhatsApp 비즈니스 계정 

#### WhatsApp 비즈니스 계정은 어떻게 만들 수 있나요? 
Braze 대시보드에 내장된 가입 절차를 통해 WhatsApp 비즈니스 계정(WABA)을 만드는 것을 권장합니다. 

#### 이미 메타 비즈니스 계정이 있습니다. WhatsApp 비즈니스 계정이 여전히 필요한가요? 
예, 여전히 WhatsApp 비즈니스 계정을 만들어야 합니다. [기본 Meta 비즈니스 계정 아래에 WABA를 중첩하는]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/) 것이 좋습니다. 

#### WhatsApp 비즈니스 계정에 액세스하려면 어떻게 해야 하나요? 
임베드된 가입 절차를 완료한 후, [WhatsApp 섹션으로](https://business.facebook.com/wa/manage/home) 이동하여 business.facebook.com에서 계정에 액세스할 수 있습니다. 

#### 여러 WABA를 Braze에 연결할 수 있나요? 
Yes, you can add up to 10 WhatsApp Business accounts per workspace, and each business account can be nested under a different Meta Business Manager.

![Diagram of the Braze and WhatsApp ecosystem, showing how workspaces and WhatsApp Business accounts connect to each other: you can connect one subscription group to one phone number, multiple WhatsApp Business accounts to one workspace, and one workspace to multiple Meta Business Portfolios.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %}) 

### WhatsApp 비즈니스 계정 전화번호 

#### WhatsApp 비즈니스 계정에 전화번호가 필요한가요? 
예, 액세스 권한이 있는 번호가 필요합니다. 내장된 가입 절차를 진행할 때 2단계 인증을 통해 휴대폰 번호를 인증하라는 메시지가 표시됩니다. 이 전화번호는 다른 WhatsApp 계정(비즈니스 또는 개인)에 사용할 수 없습니다.

#### WhatsApp에서 지원되는 전화번호 유형은 무엇인가요? 
자세한 내용은 [전화번호](https://developers.facebook.com/docs/whatsapp/phone-numbers)에 대한 Meta의 요구 사항을 참조하세요. 

#### 하나의 전화번호를 여러 WABA에서 사용할 수 있나요? 
아니요. 전화번호는 여러 WABA에서 공유할 수 없습니다. 

#### 특정 국가에 메시지를 보내려면 특정 유형의 전화번호가 필요한가요? 
아니요. WhatsApp을 사용하면 모든 국가의 지원되는 전화번호로 최종 사용자에게 메시지를 보낼 수 있습니다. 자세한 내용은 [전화번호](https://developers.facebook.com/docs/whatsapp/phone-numbers)에 대한 Meta의 요구 사항을 참조하세요. 

#### 특정 국가로 보내려면 국가별 전화번호를 사용해야 하나요?
아니요. WhatsApp을 사용하면 지원되는 모든 전화번호를 지원되는 모든 국가의 최종 사용자에게 보낼 수 있습니다.

### 옵트인 및 구독 관리 

#### WhatsApp에서 최종 사용자에게 마케팅 메시지를 보내려면 옵트인을 수집해야 하나요? 
예, WhatsApp에서는 기업이 최종 사용자에게 마케팅 메시지를 보내기 위해 [옵트인 동의를 수집해야](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) 합니다.

#### WhatsApp에서 최종 사용자에게 선제적으로 메시지를 보내 옵트인 동의를 받을 수 있나요? 
최종 사용자에게 선제적으로 메시지를 보내기로 선택한 경우, 비즈니스에서 처음 보내는 메시지는 사용자에게 비즈니스의 마케팅 메시지를 수신할 것인지 묻고 [옵트인 수락](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)을 위한 Meta의 요구 사항을 준수해야 합니다. WhatsApp은 채널에서 비즈니스 평판을 모니터링하므로 최종 사용자에게 명확히 밝히고 수신 의사를 표시한 메시지만 보내는 것이 좋습니다.
 
#### 옵트인을 수집할 때 최종 사용자의 전화번호를 수집해야 하나요? 
메시지를 보내려면 Braze 프로필에 최종 사용자의 전화번호가 있어야 합니다. 
- 이미 번호를 알고 있는 경우에는 옵트인할 때 번호를 수집할 필요가 없습니다. 
- 최종 사용자 번호가 없는 경우 옵트인 방법에 전화번호 캡처를 포함해야 합니다. 

#### 옵트인한 최종 사용자의 구독 상태를 업데이트하려면 어떻게 해야 하나요? 
WhatsApp 채널의 구독 관리는 다른 Braze 채널에서 작동하는 방식과 유사하게 작동합니다. 자세한 내용은 [사용자 구독 관리하기]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/)를 참조하세요.  

#### WhatsApp에서 마케팅 메시지 수신에 동의한 사용자 목록이 이미 있는 경우, Braze에서 해당 사용자의 구독 상태를 어떻게 업데이트하나요? 
[사용자 가져오기를]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#importing-custom-data) 통해 구독 상태를 업데이트할 수 있습니다. 

#### 옵트인 수집을 위해 어떤 방법을 사용해야 하나요? 
Braze는 규정 준수를 유지하기 위해 [Meta의 옵트인 방법에 대한 가이드라인](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)을 참조할 것을 권장합니다. Braze [채널 및 옵트인 아이디어와 제안](https://docs.google.com/document/d/1rNKnKN2oIn-e9bXdYEvnwdlzlCsEOKs-xREcdVvPBE8/edit)은 다음 리소스를 참조하세요.

#### WhatsApp에 이중 옵트인이 필요한가요? 
아니요, 이중 옵트인은 필요하지 않습니다. 

#### 사용자가 WhatsApp 메시지 수신을 거부하려면 어떻게 해야 하나요? 
사용자는 두 가지 방법으로 옵트아웃할 수 있습니다:
1. 특정 옵트아웃 단어가 포함된 인바운드 WhatsApp 메시지를 설정하고 웹훅을 사용하여 사용자 가입 상태를 업데이트합니다.
2. WhatsApp 템플릿 내에 옵트아웃 빠른 답장을 추가하고 해당 웹훅을 업데이트합니다. 

### 메시징 제한 

#### 메시징 제한이란 무엇인가요? 
메시징 제한은 WhatsApp 무결성 구축 개념입니다. 각 전화번호가 24시간 동안 시작할 수 있는 최대 비즈니스 개시 대화 수를 결정합니다. 메시징 한도 수준은 네 가지입니다: 1,000, 10,000, 100,000 및 무제한.

#### 메시징 한도를 늘리려면 어떻게 해야 하나요? 
다음 조건을 충족하는 경우 WhatsApp에서 메시징 한도를 늘립니다.
1. [전화 번호 상태는](https://www.facebook.com/business/help/896873687365001) **연결됨입니다**. 
2. [전화 번호 품질 등급이](https://www.facebook.com/business/help/896873687365001) **중간** 또는 **높음**
3. 지난 7일 동안 고유 사용자와 X회 이상 대화를 시작했으며, 여기서 X는 현재 메시징 한도를 2로 나눈 값입니다. 

따라서 10만 건에서 무제한으로 전환하려면 7일 동안 최소 50,000건의 비즈니스 시작 대화를 보내야 합니다. 

#### 내 메시징 제한을 늘리는 데 얼마나 걸리나요? 
이전 조건이 모두 충족되면 4일 안에 쪽지 한도를 1,000개에서 무제한으로 늘릴 수 있습니다. 

#### 현재 내 메시징 한도는 어디에서 확인할 수 있나요? 
**WhatsApp 관리자 > 개요 대시보드 > 인사이트** 탭에서 현재 메시지 한도를 확인할 수 있습니다. 

#### 이미 메시징 제한에 도달한 상태에서 메시지를 보내려고 하면 어떻게 되나요?
현재 제한이 허용하는 것보다 더 많은 고유 사용자에게 캠페인 또는 캔버스를 보내려고 하면 메시지 전송에 실패합니다. Braze는 최대 하루 동안 메시징 제한이 초과될 경우 계속해서 메시지 재전송을 시도합니다. 

#### 내 메시징 제한이 줄어들 수 있나요?
예, 휴대폰 번호 품질 등급이 너무 낮게 떨어지면 WhatsApp에서 메시징 제한을 줄일 위험이 있습니다. Braze는 휴대폰 번호 상태 및 메시징 한도 수준 업데이트 등 WhatsApp의 품질 관련 업데이트를 구독하고 알림을 받을 것을 권장합니다. WhatsApp 관리자 대시보드에서 바로 알림을 구독할 수 있습니다. 

#### 메타 처리량 제한이란 무엇인가요?
메타에는 WABA 메시징 제한과는 별도로 자체 처리량 제한이 있습니다. 클라우드 API가 지원하는 기본 제한은 초당 80개 메시지입니다. 캠페인이 이 한도를 초과할 것으로 예상되는 경우 한도 증액을 [요청](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/#throughput)할 수 있습니다. Meta는 캠페인 전송 최소 3일 전에 이 요청을 제출할 것을 권장합니다.

### WhatsApp 템플릿 

#### WhatsApp 템플릿이란 무엇인가요? 
WhatsApp은 모든 비즈니스 개시 메시지를 승인된 템플릿을 사용하여 시작하도록 요구합니다. 템플릿에는 메시지 사본과 함께 이미지, 클릭 유도 문안, 빠른 답장 버튼과 같은 선택적 리치 미디어가 포함되어 있습니다. WhatsApp이 템플릿을 승인하면, 해당 템플릿을 사용하여 Braze에서 WhatsApp 메시지를 작성할 수 있습니다. 

#### WhatsApp 템플릿은 어디에서 생성, 편집 및 관리하나요? 
WhatsApp 관리자에서 직접 템플릿을 생성, 편집, 관리하고 승인을 위해 제출할 수 있습니다. WABA가 Braze에 연결되면 대시보드에 상태 표시기와 함께 모든 템플릿을 볼 수 있습니다. 템플릿이 거부되면 WhatsApp 관리자를 통해 직접 다시 제출하게 됩니다. **템플릿은 Braze에서 직접 만들거나 편집할 수 없습니다.**

#### WhatsApp에서 템플릿 제출을 검토하는 데 얼마나 걸리나요? 
승인 프로세스는 최대 24시간이 소요될 수 있지만, 템플릿은 몇 시간 또는 몇 분 만에 처리되는 경우가 많습니다. 

#### 한 번에 몇 개의 템플릿을 만들 수 있나요? 
메시지 템플릿 한도는 비즈니스 인증 상태에 따라 다릅니다. **WhatsApp 관리자 > 메시지 템플릿** 페이지에서 한도를 확인할 수 있습니다. 

#### Braze에서 템플릿 카피와 리치 미디어를 개인화하려면 어떻게 하나요? 
WhatsApp에서는 메시지 템플릿에 가변 매개변수를 삽입할 수 있습니다. 메시지는 변수 매개변수로 시작하거나 끝낼 수 없습니다. 변수 매개변수는 Braze 플랫폼에서 Liquid 로직으로 채울 수 있습니다. 가변 매개변수에 대해 자세히 알아보려면 [Braze에서 WhatsApp 메시지 작성하기]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#step-2-compose-your-whatsapp-message)를 참조하세요. 

#### 템플릿이 거부되었습니다. Braze가 승인을 받는 데 도움을 줄 수 있나요? 
Braze 팀에는 템플릿 거부에 대한 가시성이 없습니다. 템플릿을 수정하고 다시 제출하려면 WhatsApp 비즈니스 관리자와 직접 협력해야 합니다. 필요한 경우 샘플 템플릿을 제공하세요. 템플릿이 메타의 [비즈니스](https://www.whatsapp.com/legal/business-policy/?fbclid=IwAR2qWg6yFKdyjDMxJkbNSM38FLGsxXxffC1qStY2gaHOyp-gl_8g72rZNIw) 또는 [커머스](https://www.whatsapp.com/legal/commerce-policy/?fbclid=IwAR3bzN3LTZ-7kO-wnO7X3smtPKGy0asxaFod-U1Ub8B9JUpnrfy1_y7LpAQ) 정책을 따르는지 다시 확인하세요.

#### Braze에서 리치 미디어를 타겟팅하거나 개인화할 수 있나요? 
미디어 라이브러리에서 이미지를 업로드할 수는 있지만 동적으로 타겟팅할 수는 없습니다. URL의 경우 링크의 마지막 부분은 Liquid를 사용하여 동적으로 채울 수 있습니다. 

### 전달 가능성 

#### 메시지가 전달되지 않는 이유는 무엇인가요? 
메시지가 전달되지 않는 이유는 네트워크 문제, 기기가 꺼져 있는 경우 등 여러 가지가 있습니다. 

#### 메시지가 전달되지 않으면 요금이 청구되나요? 
아니요. 메시지가 전달되지 않으면 요금이 청구되지 않습니다. 

#### 최종 사용자가 내 비즈니스를 차단하면 어떻게 되나요? 
최종 사용자가 비즈니스를 차단하면 이후 보내려는 메시지는 전달되지 않으며 요금이 청구되지 않습니다. 

#### 최종 사용자가 메시지를 신고하면 어떻게 되나요? 
최종 사용자가 메시지를 신고한 경우에도 이 사용자에게 후속 메시지를 보낼 수 있습니다. 그러나 신고는 채널의 품질 등급에 영향을 미칠 수 있습니다. 

#### 최종 사용자가 내 비즈니스를 차단하거나 신고하면 Braze에서 해당 사용자의 구독 상태가 업데이트되나요? 
아니요. 해당 사용자의 Braze 구독 상태는 업데이트되지 않습니다. 

### 기타

#### Braze는 WhatsApp의 챗봇 및 사람 지원 채팅과 같은 고객 지원 사용 사례를 지원하나요? 
Braze 내에서 또는 직접 통합을 통해 챗봇이나 사람 지원 채팅을 지원하지 않습니다. 

이미 WhatsApp을 고객 지원 채널로 사용하고 있는 경우에는 현재 설정을 유지하고 마케팅 메시징을 위해 Braze를 통해 새 WABA를 생성하는 것이 좋습니다. 이 WABA에는 새 전화번호가 필요합니다. 

#### Braze를 통해 고객 지원 메시지와 마케팅 메시지 간의 '격차'를 해소하려면 어떻게 해야 하나요? 
WhatsApp Liquid 속성을 사용하여 고객 지원 도구를 포함한 다른 플랫폼으로 인바운드 WhatsApp 메시지 콘텐츠(메시지 본문 및 미디어 URL 포함)를 Braze에서 다른 플랫폼으로 전달할 수 있습니다. 자세한 내용은 [지원되는 개인화 태그]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)를 참조하세요. 

예를 들어 사용자가 활발한 지원 대화 중임을 나타내는 정보를 Braze로 보내려면 커스텀 속성(예: "기존 지원 채팅 있음 = true/false")을 기록하고 이를 마케팅 캠페인의 세분화 기준으로 사용할 수 있습니다. 또한 두 채팅 스레드 간에 딥링크를 연결하여 사용자를 마케팅 스레드에서 지원 스레드로, 또는 그 반대로 연결할 수도 있습니다. 

#### Braze는 사용자 응답을 저장하나요? 
메시지는 처리할 수 있을 만큼만 저장됩니다. 사용자 메시지에 액세스하려면 커런트를 사용하세요. 

#### 사용자 전화번호는 Braze에 어떻게 저장해야 하나요? 
사용자 전화번호는 [E.164 형식으로]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/#formatting) 저장해야 합니다.

#### WhatsApp 템플릿에서 지원되는 리치 미디어의 종류는 무엇인가요? 
WhatsApp 템플릿에 이미지, 클릭 유도 문안(URL 또는 전화번호), 빠른 답장 버튼을 추가할 수 있습니다. WhatsApp에서 직접 템플릿을 만들 때 이러한 요소를 추가할 수 있습니다. 

#### 사용자 전화번호를 가져올 수 있나요? 
예. [사용자 전화번호를 가져올]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/) 수 있습니다. 

#### 비즈니스 인증이란 무엇인가요? 
비즈니스 인증은 브랜드가 합법적인 비즈니스인지 확인하는 데 사용되는 WhatsApp의 개념입니다. WhatsApp 관리자에서 완료할 수 있습니다. 메시징을 확장하려면 비즈니스 인증도 필요합니다. 비즈니스 인증이 없으면 고객은 24시간 동안 최대 250명의 고유 최종 사용자만 보낼 수 있습니다. 

#### 공식 비즈니스 계정이란 무엇인가요? 
OBA는 표시 이름 옆에 녹색 확인 표시가 표시되며 선택 사항입니다. 비즈니스 인증을 완료한 후 공식 비즈니스 계정을 신청할 수 있습니다. 비즈니스 인증과 공식 비즈니스 계정은 서로 다른 WhatsApp의 개념이라는 점에 유의하세요. 

#### Braze 대시보드에서 사용할 수 있는 지표에는 어떤 것이 있나요? 
Braze 대시보드에서 고유한 수신자, 전송, 배달, 읽음 및 실패를 확인할 수 있습니다. Braze에서 읽기를 추적하려면 최종 사용자의 읽기 영수증이 "켜짐"이어야 합니다. 다른 채널과 마찬가지로 전환 이벤트를 설정하여 캠페인 성과를 모니터링할 수도 있습니다. 

#### WhatsApp 대화란 무엇인가요? 
WhatsApp은 양방향 메시징에 중점을 둔 채널이므로 개별 메시지 수 대신 대화에 중점을 둡니다. 대화는 비즈니스와 최종 사용자 간에 24시간 진행되는 스레드입니다.

- **비즈니스에서 시작된 대화**: 승인된 템플릿 메시지를 최종 사용자에게 보내는 것으로 비즈니스가 시작되는 대화입니다. 비즈니스가 메시지를 보내는 즉시 24시간 창이 시작됩니다.
- **사용자 주도 대화**: 최종 사용자가 비즈니스에 메시지를 보내는 대화입니다. 비즈니스에서 응답으로 메시지를 보내면 24시간의 기간이 시작됩니다.

#### 전화번호 품질 등급에 영향을 미치는 요인은 무엇이며 품질 등급이 너무 낮게 떨어지면 어떻게 되나요? 
전화번호 품질 등급에 영향을 미치는 요인으로는 최종 사용자가 비즈니스를 차단하는 경우(및 비즈니스를 차단할 때 제공하는 이유), 최종 사용자가 비즈니스를 신고하는 경우 등이 있습니다. 

품질 등급이 낮으면 전화 번호 상태가 **연결됨**에서 **신고됨**으로 변경됩니다. 7일이 지나도 품질이 개선되지 않으면 상태가 **연결됨**으로 돌아갑니다. 그러나 메시징 한도는 다음 단계로 감소합니다. 예를 들어, 100,000개의 쪽지 한도가 있던 전화번호의 경우 이제 10,000개의 쪽지 한도가 있습니다.
