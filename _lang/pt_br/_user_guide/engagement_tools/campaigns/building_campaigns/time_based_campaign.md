---
nav_title: Funcionalidades Baseadas no Tempo para Campanhas
article_title: Funcionalidades Baseadas no Tempo para Campanhas
page_order: 2
tool: Campaigns
page_type: reference
description: "Este artigo de referência cobre funcionalidades baseadas em tempo para campanhas, como entrega programada, Intelligent Timing e entrega baseada em ação."

---
# Funcionalidades baseadas em tempo para campanhas

> Ao usar campanhas, você pode usar as opções de agendamento baseadas em tempo para alcançar seu público. Essas funcionalidades baseadas em tempo incluem campanhas que estão configuradas para entrega programada e entrega baseada em ação.

{% alert tip %}
Para saber mais sobre a entrega de campanhas, confira nosso curso do Braze Learning dedicado à [configuração de campanhas](https://learning.braze.com/campaign-setup-delivery-targeting-conversions).
{% endalert %}

## Entrega programada

Esta seção cobre opções de agendamento e entrega baseadas em tempo para campanhas de [entrega agendada]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/scheduled_delivery/).

### Enviar em um horário determinado

| Definição | Fuso horário |
| ---------- | --------- |
| Enviar mensagem em um horário designado, em uma data específica do calendário. | Fuso horário da empresa. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Uma campanha com a opção "Enviar em um horário determinado" selecionada para enviar uma vez a partir das 9h do dia 13 de julho de 2021.][2]

### Intelligent Timing

| Definição | Fuso horário |
| ---------- | --------- |
| Tempo ideal do usuário. Cada usuário receberá a campanha no momento em que é mais provável que se envolva. Para saber mais, confira [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/). | Se você selecionar um horário específico como seu [fallback]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#fallback-options), isso será enviado no fuso local do usuário. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Uma campanha com a opção "Intelligent Timing" selecionada para enviar uma vez no momento ideal em 13 de julho de 2021 com um horário de fallback personalizado de 9h para usuários sem dados suficientes em seus perfis para calcular um horário ideal.][3]

### Enviar campanha para os usuários no fuso local deles

| Definição | Fuso horário |
| ---------- | --------- |
| Permite que você entregue mensagens para um segmento com base no [fuso horário individual]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#when-does-braze-evaluate-users-for-local-time-zone-delivery) de um usuário. | Fuso local do usuário. Se o fuso horário de um usuário não estiver definido, ele voltará ao fuso horário da empresa. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Uma campanha com a opção "Enviar em um horário designado" selecionada para enviar uma vez a partir das 9h do dia 13 de julho de 2021 com a caixa de seleção "Enviar campanha para usuários no seu fuso local" selecionada.][4]

### Permitir que usuários se tornem reelegíveis para receber uma campanha

| Definição | Fuso horário |
| ---------- | --------- |
| Depois que um usuário recebe uma mensagem da campanha, especifique quando ele se tornará elegível novamente para receber a campanha. [Saiba mais]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/). | N/D |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Uma campanha com a caixa de seleção marcada "Permitir que os usuários se tornem re-elegíveis para receber a campanha" após uma semana.][5]

## entrega baseada em ação

Esta seção cobre a postergação do cronograma e as opções de entrega para campanhas de [entrega baseada em ação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/).

### Postergação de cronograma

{% alert important %}
Ao escolher a duração da postergação, lembre-se de que, se definir uma postergação maior do que a [duração da campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#step-4-assign-duration), os usuários não receberão a campanha.
{% endalert %}

#### Enviar campanha imediatamente

| Definição | Fuso horário |
| ---------- | --------- |
| Enviar mensagem imediatamente após o usuário realizar a ação-gatilho. | N/D |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Postergação de Agendamento definida para enviar a campanha imediatamente após o evento de gatilho ocorrer.][6]

#### Enviar campanha após X dias

| Definição | Fuso horário |
| ---------- | --------- |
| Enviar mensagem após uma postergação. Você pode especificar uma postergação em segundos, minutos, horas, dias ou semanas. Para [campanhas de mensagens no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about), você pode definir uma postergação de até duas horas apenas. | N/D |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Postergação de Agendamento definida para enviar a campanha um dia após o evento de gatilho ocorrer.][7]

#### Enviar campanha no próximo [dia da semana] às X horas

| Definição | Fuso horário |
| ---------- | --------- |
| Enviar mensagem no próximo dia da semana especificado, em um horário selecionado. | Selecione entre **o fuso local do usuário** ou **o horário da empresa** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Por exemplo, suponha que você selecione "Enviar no próximo sábado às 15h15". Se um usuário realizar o evento de gatilho em um sábado, ele receberá essa mensagem no próximo sábado em sete dias. Se eles entrarem na sexta-feira, o próximo sábado será em um dia.

![][8]

#### Enviar em X dias corridos no horário Y

| Definição | Fuso horário |
| ---------- | --------- |
| Envie mensagens em um número específico de dias em um horário especificado. | Selecione entre **fuso local do usuário** ou **horário da empresa** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

A Braze calcula a postergação como `day of the week` + `calendar days`, depois adiciona o `time`. Por exemplo, suponha que o usuário execute o evento de gatilho na segunda-feira às 21h, e a postergação do agendamento esteja definida para "Enviar campanha em 1 dia às 9h". Essa mensagem será entregue na terça-feira às 9h porque a Braze calcula a postergação como `Monday` + `1 calendar day` e depois adiciona `9 am`.

![][9]

### Horário de silêncio

| Definição | Fuso horário |
| ---------- | --------- |
| Impedir que mensagens sejam enviadas durante horas especificadas. Se uma mensagem for disparada durante o horário de silêncio, você pode escolher entre cancelar a mensagem ou enviá-la no próximo horário disponível (como enviar no final do seu horário de silêncio). | Fuso local do usuário. Se o fuso horário de um usuário não estiver definido, ele voltará ao fuso horário da empresa. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Uma campanha com horário de silêncio ativado. Neste exemplo, as mensagens não serão enviadas entre 12h e 8h no fuso local do usuário. Se uma mensagem for disparada durante o horário de silêncio, então a mensagem será enviada no próximo horário disponível.][10]

### Permitir que os usuários sejam re-elegíveis para receber a campanha

| Definição | Fuso horário |
| ---------- | --------- |
| Depois que um usuário é contatado por esta campanha, especifique quando ele se tornará [re-elegível]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) para receber a campanha novamente. | N/D |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Uma campanha com a caixa de seleção marcada "Permitir que os usuários se tornem re-elegíveis para receber a campanha" após uma semana.][5]

### Limitação global de frequência

| Definição | Fuso horário |
| ---------- | --------- |
| Limite quantas vezes cada usuário deve receber a campanha dentro de um determinado período de tempo, que pode ser medido em minutos, dias, semanas (7 dias) e meses. Para saber mais, consulte [limitação de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping). | Fuso local do usuário. Se o fuso horário de um usuário não estiver definido, ele voltará ao fuso horário da empresa. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Por padrão, o limite de frequência é desativado para novos canvas. A limitação de frequência é aplicada no nível da etapa, não no nível de entrada do canva.

O limite de frequência é baseado em dias de calendário, não em um período de 24 horas. Isso significa que você pode configurar uma regra de limitação de frequência para enviar no máximo uma campanha por dia, mas se um usuário receber uma mensagem às 23h no seu fuso local, ele ainda poderá receber outra mensagem uma hora depois (à meia-noite do dia seguinte). 

## Prazo para conversão

| Definição | Fuso horário |
| ---------- | --------- |
| A quantidade máxima de tempo que pode passar entre um usuário receber uma campanha e realizar a ação atribuída para que seja considerada uma conversão. Para saber mais, consulte [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/). | N/D |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }



[2]: {% image_buster /assets/img_archive/time_designated.png %}
[3]: {% image_buster /assets/img_archive/time_intelligent_timing.png %}
[4]: {% image_buster /assets/img_archive/time_local.png %}
[5]: {% image_buster /assets/img_archive/time_reeligibility.png %}
[6]: {% image_buster /assets/img_archive/time_delay_immediately.png %}
[7]: {% image_buster /assets/img_archive/time_delay_after.png %}
[8]: {% image_buster /assets/img_archive/time_delay_on_the_next.png %}
[9]: {% image_buster /assets/img_archive/time_delay_in.png %}
[10]: {% image_buster /assets/img_archive/time_quiet_hours.png %}
