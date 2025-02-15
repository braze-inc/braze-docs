---
nav_title: Funcionalidades baseadas no tempo
article_title: Funcionalidades baseadas em tempo para o Canva
page_order: 1
tools: Canvas
page_type: reference
description: "Este artigo de referência aborda definições, fusos horários e exemplos de funcionalidades baseadas em tempo para o canva."

---

# Funcionalidades baseadas em tempo para o Canva

> Este artigo de referência aborda as funcionalidades baseadas em tempo do canva para ajudar com estratégias, solução de problemas e para responder a perguntas comuns. 

## Postergação do cronograma

{% alert important %}
A partir de 28 de fevereiro de 2023, não será mais possível criar ou duplicar canvas usando o editor original. Esta seção está disponível para referência ao editar a programação de um canvas existente criado usando o fluxo de trabalho do canva original. Para funcionalidades baseadas em tempo do fluxo de trabalho do Canvas Flow, confira o [componente Postergação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/).
{% endalert %}

### Enviar imediatamente

| Definição |  Fuso horário |
| --- | --- |
| Envie a mensagem imediatamente após o usuário receber a etapa anterior ou, se esta for a primeira etapa, imediatamente após o usuário entrar no Canva. | N/D |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][1]

### Enviar após X dias

| Definição |  Fuso horário |
| --- | --- |
| Enviar mensagem após uma postergação. Você pode especificar uma postergação em segundos, minutos, horas, dias ou semanas.  | N/D |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][2]

### Enviar no próximo [dia da semana] no horário X

| Definição |  Fuso horário |
| --- | --- |
| Enviar mensagem no próximo dia da semana especificado, em um horário selecionado.  | Selecione entre **o fuso local do usuário** ou **o horário da empresa** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Por exemplo, suponha que você selecione "Send on the next Saturday at 3:15 pm" (Enviar no próximo sábado às 15h15). Se um usuário entrar no Canva em um sábado, ele receberá a mensagem no sábado seguinte, em sete dias. Se eles entrarem em uma sexta-feira, o próximo sábado será em um dia.

![][3]

### Enviar em X dias corridos no horário Y

| Definição |  Fuso horário |
| --- | --- |
| Envie mensagens em um número específico de dias em um horário especificado. | Selecione entre **o fuso local do usuário** ou **o horário da empresa** |

O canva calcula a postergação como `day of the week` + `calendar days` e, em seguida, adiciona o `time`. Por exemplo, suponha que um componente do canva seja enviado na segunda-feira às 21 horas e que a próxima etapa esteja programada para "Enviar em um dia às 9 horas". Essa mensagem será entregue na terça-feira às 9 horas, porque o canva calcula a postergação como `Monday` + `1 calendar day` e, em seguida, adiciona `9 am`.

![][4]

### Intelligent Timing

| Definição | Fuso horário |
| ---------- | ----- |
| [O Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) calcula o tempo de envio ideal com base em uma análise estatística das interações anteriores do usuário com o envio de mensagens (por canal) e com o app. | Se você selecionar **um horário específico** como [fallback]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#fallback-options), ele será enviado no fuso local do usuário. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][5]

## Limite global de frequência

| Definição | Fuso horário |
| --- | --- |
| Limite o número de vezes que cada usuário deve receber o Canva em um determinado período de tempo, que pode ser medido em minutos, dias, semanas (sete dias) e meses. | Fuso local do usuário. Se o fuso horário de um usuário não estiver definido, ele voltará ao fuso horário da empresa. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

[O limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping) é baseado em dias corridos, não em um período de 24 horas. Isso significa que você pode configurar uma regra de limitação de frequência para enviar no máximo uma campanha por dia, mas se um usuário receber uma mensagem às 23h no seu fuso local, ele ainda poderá receber outra mensagem uma hora depois (à meia-noite do dia seguinte).

![][6]

{% alert note %}
Se tiver as [permissões de usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) adequadas para aprovar Canvas, você verá uma [etapa**de Resumo**]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_approval/#using-approvals) no fluxo de trabalho.
{% endalert %}


[1]: {% image_buster /assets/img_archive/schedule_delay_immediately.png %}
[2]: {% image_buster /assets/img_archive/schedule_delay_after.png %}
[3]: {% image_buster /assets/img_archive/schedule_delay_next.png %}
[4]: {% image_buster /assets/img_archive/schedule_delay_in.png %}
[5]: {% image_buster /assets/img_archive/schedule_delay_intelligent.png %}
[6]: {% image_buster /assets/img_archive/schedule_frequency_capping.png %}
