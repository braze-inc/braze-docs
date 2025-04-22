---
nav_title: 인앱 메시지
article_title: 캔버스의 인앱 메시지
alias: "/canvas_in-app_messages/"
page_order: 2
page_type: reference
description: "This reference article describes features and nuances specific to in-app messages that you can add to your Canvas to show rich messaging."
tool: Canvas
channel: in-app messages

---

# 캔버스의 인앱 메시지

> You can add in-app messages as part of your Canvas journey to show rich messaging when your customer engages with your app.

## How it works

Before you can use in-app messages in your Canvas, be sure to have a [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) set up with delay and audience options.

 

## Adding an in-app message to your user journey

To add an in-app message to your Canvas, do the following:

1. Add a [Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) step to your user journey.
2. Select **In-App Message** for your **Messaging Channel**. 
3. Determine [when your message will expire](#in-app-message-expiration) and which [advancement behavior](#advancement-behavior-options) it will have.

## 



  

동작 트리거 항목이 있는 캔버스 단계의 경우 사용자는 세션 중간에 캔버스에 들어갈 수 있습니다. 

## 인앱 메시지 만료

  인앱 메시지가 전송된 후에는 한 번만 볼 수 있습니다.



| 옵션 | 설명 | 예시 |
|---|---|---|
|  |  |  그러면 2일(48시간) 동안 사용할 수 있으며, 이 이틀 동안 앱을 열면 인앱 메시지를 볼 수 있습니다. |
|  |  |  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 사용 사례



{% tabs %}
  {% tab 프로모션 %}

프로모션, 쿠폰, 세일은 만료일이 정해져 있는 경우가 많습니다. 다음 캔버스는 사용자가 사용할 수 있고 구매에 영향을 줄 수 있는 프로모션이 있음을 가장 적절한 타이밍에 사용자에게 알려야 합니다. 

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table class="tg">
<thead>
  <tr>
    <th>캔버스 단계</th>
    <th>지연</th>
    <th>오디언스</th>
    <th>채널</th>
    <th>만료</th>
    <th>진행</th>
    <th>세부 정보</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1일차: 50% 할인</td>
    <td>없음</td>
    <td>항목 전체</td>
    <td>푸시</td>
    <td>N/A</td>
    <td>지연 후 오디언스 진행</td>
    <td>사용자에게 프로모션에 대해 알리는 초기 푸시입니다. 이는 사용자가 프로모션의 혜택을 누리기 위해 앱으로 이동하도록 유도하기 위한 것입니다.</td>
  </tr>
  <tr>
    <td>인앱: 50% 할인</td>
    <td>없음</td>
    <td>항목 전체</td>
    <td>인앱 메시지</td>
    <td><b>만료일:</b> 2019/02/28 11:15 AM 회사 시간</td>
    <td>인앱 메시지 보기</td>
    <td>이제 사용자가 앱을 열면 이전 푸시 메시지 때문인지 여부와 관계없이 이 메시지를 받게 됩니다.</td>
  </tr>
  <tr>
    <td>50% 할인 알림</td>
    <td>사용자가 이전 단계를 받은 날로부터 1일 후</td>
    <td>항목 전체 <br><br><b>필터:</b> 1주일 이상 전에 마지막으로 구매한 내역</td>
    <td>인앱 메시지</td>
    <td><b>만료일:</b> 2019/02/28 11:15 AM 회사 시간</td>
    <td>없음(캔버스의 마지막 메시지)</td>
    <td>사용자가 이전 단계에서 인앱 메시지를 받았지만 앱에 있음에도 불구하고 구매를 하지 않은 경우입니다. <br><br>이 메시지는 사용자가 프로모션을 사용하여 구매하도록 유도하기 위한 것입니다.</td>
  </tr>
</tbody>
</table>



  {% endtab %}
  {% tab 사용자 온보딩 %}

사용자에 대한 첫인상은 아마도 가장 중요한 첫인상일 것입니다. 이는 향후 앱 방문의 성패를 좌우할 수 있습니다. 사용자와의 첫 커뮤니케이션은 적절한 타이밍에 이루어져야 하며, 앱 사용을 촉진하기 위해 앱에 자주 방문하도록 유도해야 합니다.

<table class="tg">
<thead>
  <tr>
    <th>캔버스 단계</th>
    <th>지연</th>
    <th>오디언스</th>
    <th>채널</th>
    <th>만료</th>
    <th>진행</th>
    <th>세부 정보</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>환영 이메일</td>
    <td>없음</td>
    <td>항목 전체</td>
    <td>이메일</td>
    <td>N/A</td>
    <td>지연 후 심화 오디언스</td>
    <td>프로젝트, 멤버십 또는 기타 온보딩 프로그램에 사용자를 환영하는 초기 이메일입니다. <br><br>이는 사용자를 앱으로 유도하여 온보딩을 시작하도록 하기 위한 것입니다.</td>
  </tr>
  <tr>
    <td>3~6일차 인앱 메시지</td>
    <td>사용자가 이전 단계를 받은 날로부터 3일 후</td>
    <td>항목 전체</td>
    <td>인앱 메시지</td>
    <td><b>만료:</b> 단계를 사용할 수 있게 된 후 3일 후</td>
    <td>인앱 메시지 라이브</td>
    <td>사용자가 이메일에 따라 조치를 취하고 앱으로 이동한 경우 원하는 인앱 메시지를 수신하여 온보딩을 계속 진행하거나 온보딩과 관련된 요구 사항을 상기시킵니다.</td>
  </tr>
  <tr>
    <td>5일차 푸시 </td>
    <td>사용자가 이전 단계를 받은 날로부터 2일 후</td>
    <td>항목 전체</td>
    <td>푸시</td>
    <td>N/A</td>
    <td>발송 메시지</td>
    <td>사용자가 인앱 메시지를 수신한 후에는 온보딩을 계속 진행하기 위한 후속 푸시를 받게 됩니다.</td>
  </tr>
</tbody>
</table>

 

  {% endtab %}
{% endtabs %}


## 인앱 메시지 우선순위 지정

 이 경우 Braze는 다음과 같은 우선 순위에 따라 표시되는 인앱 메시지를 결정합니다. 

 기본적으로 캔버스 배리언트의 이전 단계는 이후 단계보다 먼저 표시하도록 설정되어 있습니다. 



### 

  

## 

  

 





You can no longer create or duplicate Canvases using the original editor. 이 섹션은 인앱 메시지가 있는 단계의 진행 동작이 어떻게 작동하는지 이해할 때 참조할 수 있습니다.

원본 편집기에서 만든 캔버스는 캔버스 구성 요소를 통해 발전하는 기준인 진행 동작을 지정해야 합니다.  캔버스 플로우 워크플로우의 인앱 메시지의 경우, 이 옵션은 항상 오디언스에게 즉시 전달되도록 설정됩니다.

인앱 메시지가 있는 캔버스 단계에서는 실행 기반 전달을 사용할 수 없습니다. 인앱 메시지가 포함된 캔버스 단계는 예약해야 합니다. 대신 캔버스 구성 요소에서 예약된 메시지가 사용자에게 전송된 후 사용자가 앱을 처음 열 때(시작 세션에 의해 트리거됨) 캔버스 인앱 메시지가 표시됩니다.

하나의 캔버스 내에 여러 개의 인앱 메시지가 있는 경우, 사용자는 각각의 개별 메시지를 수신하기 위해 여러 세션을 시작해야 합니다.

{% alert important %}
**인앱 메시지 라이브 시 미리** 알림을 선택하면 사용자가 다음 단계로 이동하더라도 인앱 메시지가 만료될 때까지 해당 메시지를 사용할 수 있습니다. 캔버스의 다음 단계가 전달될 때 인앱 메시지가 실시간으로 표시되지 않도록 하려면 만료 시간을 후속 단계의 지연 시간보다 짧게 설정하세요.
{% endalert %}

#### 여러 채널이 있는 단계 {#steps-multiple-channels}

인앱 메시지와 다른 채널이 있는 단계에는 다음과 같은 발전 옵션이 있습니다:

| 옵션 | 설명 |
|---|---|---|
| 메시지 전송 시 진행 | 사용자에게 이메일, 웹훅 또는 푸시 알림을 보내거나 인앱 메시지를 확인해야 캔버스에서 다음 단계로 진행할 수 있습니다.  <br> <br>  인앱 메시지가 만료되고 사용자가 이메일, 웹훅 또는 푸시를 받지 못했거나 인앱 메시지를 확인하지 않은 경우 캔버스를 종료하고 다음 단계로 진행하지 않습니다. |
| 즉시 오디언스 진행 | 해당 단계의 모든 오디언스는 표시된 메시지를 보았는지 여부에 관계없이 지연 시간이 경과한 후 다음 단계로 이동합니다. <br> <br> 사용자가 다음 단계로 진행하려면 해당 단계의 세그먼트 및 필터 기준과 일치해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
**전체 오디언스**를 선택하면 사용자가 다음 단계로 이동한 경우에도 인앱 메시지가 만료될 때까지 사용할 수 있습니다. 캔버스의 다음 단계가 전달될 때 인앱 메시지가 실시간으로 표시되지 않도록 하려면 만료 시간을 후속 단계의 지연 시간보다 짧게 설정하세요.
{% endalert %}

{% enddetails %}

## 



-  
-  
-  

   





- 
- 
- 
- 
- 

## 캔버스의 사용자 지정 이벤트 속성

 

## 



- 
- 
-  
