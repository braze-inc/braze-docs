---
nav_title: Perguntas frequentes
article_title: Perguntas frequentes sobre mensagens no app
page_order: 19
description: "Este artigo fornece respostas às perguntas mais frequentes sobre mensagens no app."
tool: in-app messages

---

# Perguntas frequentes

> Este artigo fornece respostas a algumas perguntas frequentes sobre mensagens no app.

### O que é uma mensagem no navegador e como ela difere de uma mensagem no app?

As mensagens no navegador são mensagens no app enviadas para navegadores da Internet. Para criar uma mensagem no navegador, certifique-se de selecionar **Navegador da Web** no campo **Enviar para ao** criar sua campanha de mensagens no app ou no Canvas. 

### Uma mensagem no app será exibida se um dispositivo estiver off-line?

Depende. Como as mensagens no app são entregues no início da sessão, o dispositivo pode baixar a carga útil antes de ficar off-line, e a mensagem no app ainda pode ser exibida enquanto estiver off-line. Se a carga útil não for baixada, a mensagem no app não será exibida.

### Se um usuário já tiver uma carga útil de mensagem no app em seu dispositivo e a expiração da mensagem for alterada, a expiração será atualizada no dispositivo?

Quando um usuário inicia uma sessão, o Braze verifica se foram feitas alterações em quaisquer mensagens no app para as quais ele seja elegível e as atualiza de acordo. Portanto, se a expiração tiver sido alterada e eles registrarem uma sessão, a mensagem no app será enviada ao dispositivo com as informações atualizadas.

### Como faço para configurar o Horário de silêncio para uma campanha de mensagens no app?

O recurso Horário de silêncio não está disponível para uso com campanhas de mensagens no app. Esse recurso é usado para impedir o envio de mensagens aos seus usuários durante horários específicos. Para campanhas de mensagens no app, seus usuários só receberão mensagens no app se estiverem ativos no aplicativo. 

Como solução alternativa para enviar mensagens no app durante um horário específico, use o seguinte exemplo de código Liquid. Isso permite que a mensagem seja abortada se a mensagem no app for exibida após as 19h59 ou antes das 8h no fuso horário especificado.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 19 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}
MESSAGE HERE
```
{% endraw %}

### Quando é calculada a elegibilidade para uma mensagem no app?

A elegibilidade para uma mensagem no app é calculada no momento da entrega. Se uma mensagem no app estiver programada para ser enviada às 7h, a elegibilidade será verificada para essa mensagem no app às 7h.

Quando a mensagem no app for exibida, a elegibilidade dependerá de quando a mensagem no app for baixada e disparada.

### O que são mensagens no app modeladas?

As mensagens no app serão entregues como modelos de mensagens no app quando a opção **Reavaliar elegibilidade da campanha antes de exibir** estiver selecionada ou se qualquer uma das seguintes Liquid tags existir na mensagem:

- `canvas_entry_properties`
- `connected_content`
- Variáveis de SMS, como {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Isso significa que, durante o início da sessão, o dispositivo receberá o disparo dessa mensagem no app, em vez da mensagem inteira. Quando o usuário dispara a mensagem no app, o dispositivo do usuário faz uma solicitação de rede para buscar a mensagem real.

{% alert note %}
A mensagem não será entregue se o dispositivo não tiver acesso à Internet. A mensagem pode não ser entregue se a lógica do Liquid demorar muito para ser resolvida.
{% endalert %}

### Por que minha campanha de mensagens no app arquivada ainda está fornecendo impressões de mensagens no app?

Isso pode ocorrer para usuários que atenderam aos critérios do segmento quando a campanha de mensagens no app estava ativa.

Para evitar isso, durante a configuração de sua campanha, selecione **Reavaliar elegibilidade da campanha antes de exibi-la**. 

### Como o Braze calcula a expiração de uma mensagem no app definida como "após 1 dia(s)"?

O Braze calcula o tempo de expiração de um dia como 24 horas após os usuários serem elegíveis para receber uma mensagem.