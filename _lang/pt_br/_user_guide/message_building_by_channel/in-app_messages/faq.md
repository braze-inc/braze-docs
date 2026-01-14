---
nav_title: FAQ
article_title: FAQ de Mensagens no Aplicativo
page_order: 19
description: "Este artigo fornece respostas para perguntas frequentes sobre Mensagens no Aplicativo."
tool: in-app messages

---

# Perguntas frequentes

> Este artigo fornece respostas para algumas perguntas frequentes sobre mensagens no aplicativo.

### O que é uma mensagem no navegador e como ela difere de uma mensagem no aplicativo?

Mensagens no navegador são mensagens no aplicativo enviadas para navegadores da web. Para criar uma mensagem no navegador, certifique-se de selecionar **Web Browser** no campo **Send To** ao criar sua campanha de mensagem no aplicativo ou Canvas. 

### Uma mensagem no aplicativo será exibida se um dispositivo estiver offline?

Depende. Como as mensagens no aplicativo são entregues no início da sessão, o dispositivo pode baixar a carga útil antes de ficar offline, a mensagem no aplicativo ainda pode ser exibida enquanto estiver offline. Se a carga útil não for baixada, a mensagem no aplicativo não será exibida.

### Se um usuário já tiver uma carga útil de mensagem no aplicativo em seu dispositivo e a expiração da mensagem for alterada, a expiração será atualizada em seu dispositivo?

Quando um usuário inicia uma sessão, a Braze verifica se houve alterações em mensagens no aplicativo para as quais ele é elegível e as atualiza de acordo. Portanto, se a expiração foi alterada e ele registra uma sessão, a mensagem no aplicativo é enviada para o dispositivo com as informações atualizadas.

### Como configuro Horários Silenciosos para uma campanha de mensagem no aplicativo?

O recurso de Horários Silenciosos não está disponível para uso com campanhas de mensagens no aplicativo. Este recurso é usado para evitar que mensagens sejam enviadas aos seus usuários durante horas específicas. Para campanhas de mensagens no aplicativo, seus usuários só receberão mensagens no aplicativo se estiverem ativos dentro do aplicativo. 

Como uma solução alternativa para enviar mensagens no aplicativo durante um horário específico, use o seguinte código Liquid de exemplo. Isso permite que a mensagem seja abortada se a mensagem no aplicativo for exibida após as 19h59 ou antes das 8h no fuso horário especificado.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 19 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}
MESSAGE HERE
```
{% endraw %}

### Quando a elegibilidade para uma mensagem no aplicativo é calculada?

A elegibilidade para uma mensagem no aplicativo é calculada no momento da entrega. Se uma mensagem no aplicativo está programada para ser enviada às 7h, a elegibilidade é verificada para essa mensagem no aplicativo às 7h.

Uma vez que a mensagem no aplicativo é exibida, a elegibilidade dependerá de quando a mensagem no aplicativo é baixada e acionada.

### O que são mensagens no aplicativo com modelo?

As mensagens no aplicativo serão entregues como mensagens no aplicativo com modelo quando **Reavaliar a elegibilidade da campanha antes de exibir** for selecionado ou se qualquer uma das seguintes tags Liquid existir na mensagem:

- `canvas_entry_properties`
- `connected_content`
- Variáveis SMS como {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Isso significa que durante o início da sessão, o dispositivo receberá o gatilho daquela mensagem no aplicativo em vez da mensagem inteira. Quando o usuário aciona a mensagem no aplicativo, o dispositivo do usuário fará uma solicitação de rede para buscar a mensagem real.

{% alert note %}
A mensagem não será entregue se o dispositivo não tiver acesso à internet. A mensagem pode não ser entregue se a lógica Liquid demorar muito para ser resolvida.
{% endalert %}

### Por que minha campanha de mensagem no aplicativo arquivada ainda está entregando impressões de mensagens no aplicativo?

Isso pode ocorrer para usuários que atenderam aos critérios do segmento quando a campanha de mensagem no aplicativo estava ativa.

Para evitar isso, durante a configuração da sua campanha, selecione **Reavaliar a elegibilidade da campanha antes de exibir**. 

### Como a Braze calcula a expiração de uma mensagem no aplicativo definida para "após 1 dia(s)"?

A Braze calcula um tempo de expiração de um dia como 24 horas após os usuários serem elegíveis para receber uma mensagem.