---
nav_title: 전달 가능성 센터
article_title: 전달 가능성 센터
page_order: 4
description: "이 참조 기사는 마케터가 이메일 발송 도메인과 IP 평판을 보고 이메일 전달 가능성을 이해할 수 있도록 하는 기능인 전달 가능성 센터를 설정하는 방법을 다룹니다."
channel:
  - email

---

# 전달 가능성 센터

> 전달 가능성 센터는 [Gmail Postmaster Tools](https://www.gmail.com/postmaster/)의 사용을 지원하여 발송된 이메일에 대한 데이터를 추적하고 발송 도메인에 대한 데이터를 수집함으로써 이메일 성과에 대한 더 많은 통찰력을 제공합니다.

이메일 전달 가능성은 캠페인 성공의 핵심입니다. Braze 대시보드에서 전달 가능성 센터를 사용하면 **IP 평판** 또는 **전달 오류**로 도메인을 보고 이메일 전달 가능성과 관련된 잠재적인 문제를 발견하고 해결할 수 있습니다. 

전달 가능성 센터에 접근하려면 "캠페인, 캔버스, 카드, 세그먼트, 미디어 라이브러리 접근" 및 "사용 데이터 보기" [사용자 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)이 필요합니다.

## Google Postmaster 계정 설정하기

전달 가능성 센터에 연결하기 전에 Google Postmaster Tools 계정을 설정해야 합니다. 작업용 또는 개인 Gmail 계정을 사용하여 Google Postmaster를 설정할 수 있습니다. 

1. [Google Postmaster Tools 대시보드](https://postmaster.google.com/managedomains?pli=1)로 이동합니다.
2. 오른쪽 하단에서 <i class="fas fa-plus-circle"></i> 더하기 아이콘을 선택합니다.
3. 이메일을 인증하기 위해 루트 도메인 또는 서브도메인을 입력합니다. 루트 도메인을 추가하고 확인하는 경우, 이는 서브도메인에 대해 하류에서 확인이 적용될 수 있도록 합니다. 예를 들어, `braze.com`을 확인하면 나중에 `demo.braze.com` 및 기타 서브도메인을 개별적으로 확인할 필요 없이 추가할 수 있습니다.
4. Google은 도메인의 DNS에 직접 추가할 수 있는 TXT 레코드를 생성합니다. 이는 일반적으로 DNS를 관리하는 사람이 소유합니다. 특정 DNS를 업데이트하는 방법에 대한 정보와 지침은 [도메인 확인하기 (호스트별 단계)](https://support.google.com/a/topic/1409901)를 확인하세요.
5. **다음**을 선택합니다. <br>\![이메일을 인증하기 위한 예시 도메인 "demo.braze.com".]({% image_buster /assets/img_archive/domain_authentication.png %})
6. TXT 레코드가 DNS에 추가된 후, Google Postmaster Tools 대시보드로 돌아가서 **확인**을 선택합니다. 이 단계는 도메인을 소유하고 있음을 확인하므로 Postmaster 계정에서 Gmail 배달 가능성 메트릭에 접근할 수 있습니다. <br> \![도메인 "demo.braze.com" 소유권을 확인하는 프롬프트입니다.]({% image_buster /assets/img_archive/domain_verification.png %})

{% alert tip %}
TXT 레코드가 Braze를 통해 사용하는 하위 도메인이 아닌 상위 도메인에 연결되어 있는지 확인하세요.
{% endalert %}

{% alert note %}
하위 도메인이 Google Postmaster의 배달 가능성 센터에 포함되지 않은 경우, 이는 상위 도메인만 Google Postmaster에 추가한 결과일 수 있습니다. 상위 도메인이 Google Postmaster에서 확인된 후, 하위 도메인을 추가할 수 있으며, 이는 자동으로 확인됩니다. 이 프로세스는 Google이 하위 도메인 수준의 메트릭을 보고할 수 있게 하며, 이는 Braze 배달 가능성 센터로 가져올 수 있습니다.
{% endalert %}

## Google Postmaster 통합

배달 가능성 센터를 설정하기 전에 도메인이 [Gmail Postmaster Tools](https://support.google.com/mail/answer/9981691?hl=en)에 [추가되었는지](https://support.google.com/mail/answer/9981691?hl=en) 확인하세요.

Google Postmaster와 통합하고 배달 가능성 센터를 설정하려면 다음 단계를 따르세요:

1. **Analytics** > **Email Performance**로 이동하세요.
2. **배달 가능성 센터** 탭을 선택하세요. <br>\![Google Postmaster와 연결되지 않은 배달 가능성 센터입니다.]({% image_buster /assets/img_archive/deliverability_center1.png %})
3. **Google Postmaster와 연결**을 선택하세요. 
4. Google 계정을 선택한 후 **허용**을 선택하여 Braze가 Postmaster Tools에 등록된 도메인의 이메일 트래픽 메트릭을 볼 수 있도록 허용하세요. 

확인된 도메인이 배달 가능성 센터에 표시됩니다. 

\![중간 및 낮은 평판을 가진 Google Postmaster의 두 개의 확인된 도메인입니다.]({% image_buster /assets/img_archive/deliverability_center2.png %})

Braze 대시보드에서 **파트너 통합** > **기술 파트너** > **Google Postmaster**로 이동하여 Google Postmaster에 접근할 수 있습니다. 통합 후, Braze는 지난 30일 동안의 평판 및 오류 데이터를 가져옵니다. 데이터는 즉시 사용 가능하지 않을 수 있으며, 채워지는 데 몇 분이 걸릴 수 있습니다.

### 지표 및 정의

다음 지표 및 정의는 Google Postmaster Tools에 적용됩니다.

#### IP 평판 

IP 평판에 대한 평가를 이해하는 데 도움이 되도록 이 표를 참조하십시오:

| 평판 등급 | 정의 |
| ----- | ---------- |
| 높음 | 스팸 버튼을 클릭하는 사용자와 같은 낮은 스팸 불만을 생성하는 좋은 실적을 가지고 있습니다. |
| 중간/공정 | 긍정적인 참여를 생성하는 것으로 알려져 있지만 가끔 스팸 불만을 받습니다. 이 도메인에서 발송되는 대부분의 이메일은 스팸 불만이 증가하지 않는 한 받은 편지함으로 전송됩니다. |
| 낮음 | 정기적으로 높은 비율의 스팸 불만을 받는 것으로 알려져 있습니다. 이 발신자에게서 오는 이메일은 스팸 폴더로 필터링될 가능성이 높습니다. |
| 나쁨 | 높은 비율의 스팸 불만을 받는 이력이 있습니다. 이 도메인에서 오는 이메일은 거의 항상 연결 시 거부되거나 스팸 폴더로 필터링됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 도메인 평판 

다음 표를 사용하여 도메인 평판 등급을 모니터링하고 이해하여 스팸 폴더로 필터링되는 것을 피하는 데 도움을 주십시오.

| 평판 등급 | 정의 |
| ----- | ---------- |
| 높음 | 스팸 불만이 매우 낮은 좋은 실적을 보유하고 있습니다. Gmail의 발신자 가이드라인을 준수합니다. 이메일이 스팸 폴더로 필터링되는 경우는 드뭅니다. 매우 낮은 스팸 비율에 대한 좋은 실적을 보유하고 있습니다. [Gmail의 발신자 가이드라인](https://developers.google.com/gmail/markup/registering-with-google)을 준수합니다. |
| 중간/공정 | 긍정적인 참여를 생성하는 것으로 알려져 있지만 가끔 낮은 양의 스팸 불만을 받기도 했습니다. 이 도메인에서 발송된 이메일의 대부분은 수신함에 도달합니다(스팸 수준이 눈에 띄게 증가하지 않는 한). |
| 낮음 | 정기적으로 스팸 불만을 받는 것으로 알려져 있습니다. 이 발신자에게서 오는 이메일은 스팸 폴더로 필터링될 가능성이 높습니다. |
| 나쁨 | 높은 비율의 스팸 불만을 받는 이력이 있습니다. 이 도메인에서 오는 이메일은 거의 항상 연결 시 거부되거나 스팸 폴더로 필터링됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 인증

인증 대시보드를 사용하여 발신자 정책 프레임워크(SPF), 도메인키 식별 메일(DKIM), 도메인 기반 메시지 인증, 보고 및 준수(DMARC)를 통과한 이메일의 비율을 검토합니다.

| 그래프 유형 | 정의 |
| ----- | ---------- |
| SPF | SPF를 통과한 이메일의 비율과 SPF를 시도한 도메인에서의 모든 이메일을 보여줍니다. 이는 스푸핑된 메일을 제외합니다. |
| DKIM | DKIM을 통과한 이메일의 비율과 DKIM을 시도한 도메인에서의 모든 이메일을 보여줍니다. |
| DMARC | SPF 또는 DKIM을 통과한 도메인에서 수신된 모든 이메일에 대한 DMARC 정렬을 통과한 이메일의 비율을 보여줍니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 암호화

이 표를 참조하여 수신 및 발신 트래픽의 몇 퍼센트가 암호화되어 있는지 이해합니다.

| 용어 | 정의 |
| ----- | ---------- |
| TLS 수신 | 도메인에서 수신한 모든 메일에 대해 TLS를 통과한 수신 메일의 비율을 보여줍니다. |
| TLS 발신 | 도메인으로 전송된 모든 메일에 대해 TLS를 통해 수락된 발신 메일의 비율을 보여줍니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

전달 가능성을 개선하기 위한 더 많은 아이디어는 [전달 가능성 함정 및 스팸 트랩]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/deliverability_pitfalls_and_spam_traps/#deliverability-pitfalls-and-spam-traps)을 읽어보세요. 이메일 캠페인을 보내기 전에 확인해야 할 사항에 대한 [이메일 모범 사례]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/)를 참조하세요.

## Microsoft 스마트 네트워크 데이터 서비스(SNDS) 설정하기

Microsoft가 주요 메일박스 제공업체인 경우 이 통합을 사용하여 Microsoft 평판 데이터를 액세스하고 볼 수 있습니다. 이렇게 하면 IP의 상태를 모니터링하여 이메일이 어떻게 수신되고 있는지 판단하는 데 도움이 됩니다.

{% alert important %}
전달 가능성 센터에서 데이터를 볼 수 없는 경우, IP 주소 목록과 함께 [지원]({{site.baseurl}}/user_guide/administrative/access_braze/support/)에 문의하세요.
{% endalert %}

\![Microsoft SNDS의 결과 예시로, 샘플 IP, 수신자, RCPT 명령, 데이터 명령, 필터 결과, 불만 비율, 트랩 메시지 기간 시작 및 종료, 스팸 트랩 적중을 포함합니다.]({% image_buster /assets/img_archive/deliverability_center_msnds.png %})

### 지표 및 정의

다음 메트릭은 Microsoft SNDS에 적용됩니다.

#### 수신자

이 메트릭은 IP에 의해 전송된 메시지의 수신자 수를 나타냅니다.

#### DATA 명령

이 메트릭은 IP에 의해 전송된 DATA 명령의 수를 추적합니다. DATA 명령은 메일을 전송하는 데 사용되는 SMTP 프로토콜의 일부입니다.

#### 필터 결과

이 표를 참조하여 필터 결과를 이해하십시오 

| 결과 | 정의 |
| ----- | ---------- |
| 녹색 | 주어진 기간의 최대 10%까지 Microsoft의 스팸 필터에 의해 스팸으로 판단되었습니다. |
| 노란색 | 주어진 기간의 10%에서 90% 사이에 Microsoft의 스팸 필터에 의해 스팸으로 판단되었습니다. |
| 빨간색 | 주어진 기간의 90% 이상 Microsoft의 스팸 필터에 의해 스팸으로 판단되었습니다.| 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 불만 비율

이는 활동 기간 동안 IP에서 수신된 메시지에 대해 Hotmail 또는 Windows Live 사용자가 불만을 제기한 시간의 비율입니다. 사용자는 웹 사용자 인터페이스를 통해 거의 모든 메시지를 정크로 신고할 수 있는 옵션이 있습니다. 

불만 비율을 계산하려면 불만 수를 메시지 수신자 수로 나누십시오.  

| 결과 | 정의 |
| ----- | ---------- |
| 0.3% 미만 | 이상적인 불만 비율입니다. |
| 0.3% 초과 | 가입 프로세스를 검토하고 구독 취소 링크가 작동하는지 확인하십시오. 또한, 메일이 청중에게 더 잘 개인화될 수 있는지 고려하십시오. |
| 100% 초과 | SNDS는 불만이 보고된 날짜에 대한 불만을 표시하며, 불만이 제기된 메일이 배달된 날짜에 대해 소급하여 표시하지 않습니다. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 스팸 트랩 적중

스팸 트랩 히트는 "트랩 계정"으로 전송된 메시지의 수로, 이는 Outlook.com에 의해 유지되는 계정으로 어떤 메일도 요청하지 않습니다. 이러한 트랩 계정으로 전송된 메시지는 스팸으로 간주될 가능성이 높으므로, 이 메트릭을 모니터링하여 낮게 유지하는 것이 중요합니다. 낮은 스팸 트랩 히트는 메시지가 이러한 계정으로 전송되지 않고 실제 계정으로 전송되고 있음을 의미합니다.

{% alert tip %}
Braze에서 확인된 도메인 중 하나와 관련된 기록을 찾고 있다면, Deliverability Center가 Google Postmaster 또는 Microsoft SNDS의 데이터를 나열하므로, 두 플랫폼 중 하나가 Braze와 공유할 데이터가 없을 가능성이 높습니다. 대안으로, 일관된 이메일 배달을 유지하는 것을 제안합니다. 이는 더 높은 평판으로 이어질 수 있습니다.
{% endalert %}


