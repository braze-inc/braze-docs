---
nav_title: 전달 가능성 센터
article_title: 전달 가능성 센터
page_order: 4
description: "이 참조 문서에서는 마케터가 이메일 전송 도메인 및 IP 평판을 확인하고 이메일 전달 가능성을 파악할 수 있는 기능인 전달 센터를 설정하는 방법에 대해 설명합니다."
channel:
  - email

---

# 전달 가능성 센터

> The Deliverability Center provides more insight into your email performance by supporting the use of [Gmail Postmaster Tools](https://www.gmail.com/postmaster/) to track data on emails sent and gather data about your sending domain.

이메일 전달 가능성은 캠페인 성공의 핵심입니다. Braze 대시보드의 배달 가능성 센터를 사용하면 **IP 평판** 또는 **배달 오류별로** 도메인을 확인하여 이메일 배달 가능성과 관련된 잠재적인 문제를 발견하고 해결할 수 있습니다. 

전달 가능성 센터에 액세스하려면 "캠페인, 캔버스, 카드, 세그먼트, 미디어 라이브러리 액세스" 및 "사용 데이터 보기" [사용자 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)이 필요합니다.

## Google 포스트마스터 계정 설정하기

전달 가능성 센터에 연결하기 전에 Google Postmaster 도구 계정을 설정해야 합니다. 업무용 또는 개인용 Gmail 계정을 사용하여 Google Postmaster를 설정할 수 있습니다. 

1. [Google Postmaster 툴 대시보드](https://postmaster.google.com/managedomains?pli=1)로 이동합니다.
2. 오른쪽 하단에서 <i class="fas fa-plus-circle"></i> 더하기 아이콘을 선택합니다.
3. 루트 도메인 또는 하위 도메인을 입력하여 이메일을 인증합니다. 루트 도메인을 추가하고 확인하는 경우 하위 도메인에 대한 확인을 다운스트림에 적용할 수 있습니다. 예를 들어 `braze.com` 을 인증하면 나중에 `demo.braze.com` 및 기타 하위 도메인을 개별적으로 인증할 필요 없이 추가할 수 있습니다.
4. Google은 도메인의 DNS에 직접 추가할 수 있는 TXT 레코드를 생성합니다. 일반적으로 DNS를 관리하는 사람이 소유합니다. 특정 DNS를 업데이트하는 방법에 대한 정보와 지침은 [도메인 확인(호스트별 단계)](https://support.google.com/a/topic/1409901)을 참조하세요.
5. **다음**을 선택합니다. <br>![An example domain "demo.braze.com" to authenticate an email.]({% image_buster /assets/img_archive/domain_authentication.png %})
6. TXT 레코드가 DNS에 추가되면 Google Postmaster 툴 대시보드로 돌아가서 **확인**을 선택합니다. 이 단계를 통해 도메인을 소유하고 있음을 확인하면 Postmaster 계정에서 Gmail 전달 가능성 측정지표에 액세스할 수 있습니다. <br> ![A prompt to verify ownership of the domain "demo.braze.com".]({% image_buster /assets/img_archive/domain_verification.png %})

{% alert tip %}
TXT 레코드가 Braze를 통해 사용 중인 하위 도메인이 아닌 상위 도메인에 연결되어 있는지 확인하세요.
{% endalert %}

{% alert note %}
하위 도메인이 Google Postmaster용 전달 가능성 센터에 포함되지 않는 경우, 이는 상위 도메인만 Google Postmaster에 추가했기 때문일 수 있습니다. Google 포스트마스터에서 상위 도메인이 확인되면 하위 도메인을 추가할 수 있으며, 이 도메인은 자동으로 확인됩니다. 이 프로세스를 통해 Google은 하위 도메인 수준의 측정기준을 다시 보고할 수 있으며, 이를 Braze 전달 가능성 센터로 가져올 수 있습니다.
{% endalert %}

## Google 포스트마스터 통합

Before setting up your Deliverability Center, check that your domains have been [added to the Gmail Postmaster Tools](https://support.google.com/mail/answer/9981691?hl=en).

다음 단계에 따라 Google Postmaster와 통합하고 전달 가능성 센터를 설정하세요.

1. **분석** > **이메일 성능**으로 이동합니다.
2. **배송 센터** 탭을 선택합니다. <br>![A Deliverability Center with Google Postmaster unconnected.]({% image_buster /assets/img_archive/deliverability_center1.png %})
3. **Google 포스트마스터와 연결을** 선택합니다. 
4. Google 계정을 선택한 다음 **허용을** 선택하여 Braze가 포스트마스터 도구에 등록된 도메인에 대한 이메일 트래픽 지표를 볼 수 있도록 허용합니다. 

확인된 도메인은 배달 가능성 센터에 표시됩니다. 

![Two verified domains for Google Postmaster with a medium and low reputation.]({% image_buster /assets/img_archive/deliverability_center2.png %})

Braze 대시보드에서 **파트너 통합** > **기술 파트너** > **Google 포스트마스터로** 이동하여 Google 포스트마스터에 액세스할 수도 있습니다. 통합 후 Braze는 지난 30일 동안의 평판 및 오류 데이터를 가져옵니다. 데이터를 즉시 사용할 수 없으며 데이터를 채우는 데 몇 분 정도 걸릴 수 있습니다.

### 메트릭 및 정의

다음 측정기준 및 정의가 Google Postmaster 도구에 적용됩니다.

#### IP 평판 

IP 평판에 대한 등급을 이해하는 데 도움이 되는 표를 참조하세요:

| 평판 평가 | 정의 |
| ----- | ---------- |
| 높음 | 스팸 불만(예: 사용자가 '스팸' 버튼을 클릭하는 등) 발생률이 낮아야 합니다. |
| 중간/공평 | 긍정적인 참여를 유도하는 것으로 알려져 있지만 때때로 스팸 불만이 접수되기도 합니다. 스팸 불만이 증가하는 경우를 제외하고 이 도메인에서 보낸 대부분의 이메일은 받은 편지함으로 전송됩니다. |
| 낮음 | 스팸 불만 접수율이 정기적으로 높은 것으로 알려져 있습니다. 이 발신자가 보낸 이메일은 스팸 폴더로 필터링될 가능성이 높습니다. |
| 나쁨 | 스팸 불만 접수율이 높은 이력이 있습니다. 이 도메인에서 보낸 이메일은 거의 항상 연결 시 거부되거나 스팸 폴더로 필터링됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 도메인 평판 

다음 표를 참조하여 도메인 평판 등급을 모니터링하고 이해하면 스팸 폴더로 필터링되는 것을 방지하는 데 도움이 됩니다.

| 평판 평가 | 정의 |
| ----- | ---------- |
| 높음 | 스팸 불만 신고가 매우 낮은 좋은 실적을 보유하고 있습니다. Gmail의 발신자 가이드라인을 준수합니다. 이메일이 스팸 폴더로 필터링되는 경우는 거의 없습니다. 스팸 비율이 매우 낮은 좋은 실적을 보유하고 있습니다. Complies with [Gmail's sender guidelines](https://developers.google.com/gmail/markup/registering-with-google). |
| 중간/공평 | 긍정적인 인게이지먼트를 유도하는 것으로 알려져 있지만 가끔 스팸 불만이 제기되는 경우가 있습니다. 이 도메인에서 보낸 대부분의 이메일은 받은 편지함에 도착합니다(스팸 수준이 눈에 띄게 증가한 경우 제외). |
| 낮음 | 스팸 신고가 정기적으로 접수되는 것으로 알려져 있습니다. 이 발신자가 보낸 이메일은 스팸 폴더로 필터링될 가능성이 높습니다. |
| 나쁨 | 스팸 불만 접수율이 높은 이력이 있습니다. 이 도메인에서 보낸 이메일은 거의 항상 연결 시 거부되거나 스팸 폴더로 필터링됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 인증

인증 대시보드를 사용하여 발신자 정책 프레임워크(SPF), 도메인 키 식별 메일(DKIM) 및 도메인 기반 메시지 인증, 보고 및 적합성(DMARC)을 통과한 이메일의 비율을 검토하세요.

| 그래프 유형 | 정의 |
| ----- | ---------- |
| SPF | SPF를 시도한 도메인의 모든 이메일 대비 SPF를 통과한 이메일의 비율을 표시합니다. 여기에는 스푸핑된 메일은 제외됩니다. |
| DKIM | DKIM을 시도한 도메인의 모든 이메일 대비 DKIM을 통과한 이메일의 비율을 표시합니다. |
| DMARC | 도메인에서 수신된 모든 이메일 중 SPF 또는 DKIM을 통과한 이메일 대비 DMARC 정렬을 통과한 이메일의 비율을 표시합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 암호화

이 표를 참조하여 인바운드 및 아웃바운드 트래픽의 몇 퍼센트가 암호화되는지 파악하세요.

| 기간 | 정의 |
| ----- | ---------- |
| TLS 인바운드 | 해당 도메인에서 수신된 모든 메일 대비 TLS를 통과한 수신 메일(Gmail로)의 비율을 표시합니다. |
| TLS 아웃바운드 | 해당 도메인으로 전송된 모든 메일 대비 TLS를 통해 수락된 발신 메일(Gmail에서 보낸 메일)의 비율을 표시합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For more ideas on improving deliverability, read [Deliverability pitfalls and spam traps]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/deliverability_pitfalls_and_spam_traps/#deliverability-pitfalls-and-spam-traps). Be sure to reference our [Email best practices]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/) for things you should check for before sending an email campaign.

## Microsoft SNDS(스마트 네트워크 데이터 서비스) 설정하기

Microsoft가 기본 사서함 제공업체인 경우 이 통합 기능을 사용하여 Microsoft 평판 데이터에 액세스하고 볼 수 있습니다. 이렇게 하면 IP 상태를 모니터링하여 이메일이 어떻게 수신되는지 확인할 수 있습니다.

{% alert important %}
전달 가능성에 센터에 데이터가 표시되지 않으면 [지원팀]({{site.baseurl}}/user_guide/administrative/access_braze/support/)에 IP 주소 목록과 함께 문의하세요.
{% endalert %}

![An example of results from Microsoft SNDS, including sample IPs, recipients, RCPT commands, data commands, filter result, complaint rate, trap message period start and end, and spam trap hits.]({% image_buster /assets/img_archive/deliverability_center_msnds.png %})

### 메트릭 및 정의

다음 메트릭은 Microsoft SNDS에 적용됩니다.

#### 수신자

이 메트릭은 IP로 전송된 메시지의 수신자 수를 나타냅니다.

#### 데이터 명령

이 측정기준은 IP가 전송한 데이터 명령의 수를 추적합니다. DATA 명령은 메일을 보내는 데 사용되는 SMTP 프로토콜의 일부입니다.

#### 필터 결과

필터 결과를 이해하려면 다음 표를 참조하세요. 

| 결과 | 정의 |
| ----- | ---------- |
| 녹색 | 주어진 기간의 최대 10%까지 Microsoft의 스팸 필터에 의해 스팸으로 판단됩니다. |
| 노란색 | 주어진 기간의 10%에서 90% 사이에서 Microsoft의 스팸 필터에 의해 스팸으로 판정된 메일입니다. |
| 빨간색 | Microsoft의 스팸 필터에 의해 주어진 기간의 최대 90% 이상에서 스팸으로 판단됩니다.| 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 불만율

활동 기간 동안 Hotmail 또는 Windows Live 사용자가 IP로부터 수신한 메시지에 대해 불만을 제기하는 비율입니다. 사용자는 웹 사용자 인터페이스를 통해 거의 모든 메시지를 스팸으로 신고할 수 있습니다. 

불만 비율을 계산하려면 불만 건수를 메시지 수신자 수로 나눕니다.  

| 결과 | 정의 |
| ----- | ---------- |
| 0.3% 미만 | 이상적인 불만 비율. |
| 0.3% 이상 | 가입 절차를 검토하고 수신 거부 링크가 제대로 작동하는지 확인하세요. 또한 메일을 오디언스에게 더 잘 맞춤화할 수 있는지 고려하세요. |
| 100% 이상 | SNDS는 불만 사항이 신고된 날의 불만 사항을 표시하며, 불만 사항이 접수된 메일이 배달된 날로 소급하여 표시하지 않는다는 점에 유의하세요. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 스팸 트랩 적중률

스팸 트랩 적중률은 Outlook.com에서 관리하며 메일을 요청하지 않는 계정인 "트랩 계정"으로 전송된 메시지 수입니다. It's likely that any messages sent to these trap accounts are considered spam, so it's important to monitor this metric to make sure that it's low. Low spam trap hits means the messages aren't sent to these accounts and are being sent to actual accounts instead.

{% alert tip %}
Braze에서 확인된 도메인 중 하나와 관련된 레코드를 찾고 있는 경우, 배달 가능성 센터에 Google Postmaster 또는 Microsoft SNDS의 데이터가 나열되어 있으므로 두 플랫폼 모두 Braze와 공유할 데이터가 없을 가능성이 높다는 점에 유의하세요. 또는 평판이 높아질 수 있으므로 일관성 있는 이메일 전송을 유지하는 것이 좋습니다.
{% endalert %}


