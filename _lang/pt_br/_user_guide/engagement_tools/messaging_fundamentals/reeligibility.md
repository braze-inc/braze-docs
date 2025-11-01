---
nav_title: Re-eligibilidade
article_title: Re-eligibilidade
page_order: 8
page_type: reference
description: "Este artigo de referência define re-eligibilidade para campanhas e Canvas."
tool:
    - Campaigns
    - Canvas
toc_headers: h2
---

# Re-eligibilidade para campanhas e Canvas

> Quando você agenda uma campanha ou Canvas recorrente ou acionada, você tem a opção de permitir que os usuários se tornem re-eligíveis para isso. Re-eligibilidade significa que os usuários podem entrar na campanha ou Canvas várias vezes com base no gatilho.

## Como funciona

Por padrão, a Braze envia uma mensagem a um usuário apenas uma vez, mesmo que ele se requalifique várias vezes, pois a re-eligibilidade precisa ser ativada separadamente. Depois que for ativada, os membros qualificados poderão receber mensagens novamente após terem recebido a primeira instância da campanha ou Canvas. Você pode declarar o cronograma em que os usuários se tornariam re-eligíveis.

## Ativando a re-eligibilidade

{% tabs local %}
{% tab campaign %}
Para ativar a re-eligibilidade para uma campanha, selecione a caixa de seleção **Permitir que os usuários se tornem re-eligíveis para receber a campanha** na seção **Controles de Entrega**. O tempo máximo para re-eligibilidade para uma campanha é de 720 dias.

Para campanhas acionadas com re-eligibilidade ativada, os usuários que [não receberam realmente a mensagem da campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#why-did-a-user-not-receive-my-triggered-campaign) (apesar de completar o evento de gatilho) se qualificarão automaticamente para a mensagem na próxima vez que completarem o evento de gatilho. Isso ocorre porque a re-eligibilidade é baseada no recebimento da mensagem e não na entrada da campanha. Ao tornar os usuários re-eligíveis para uma campanha acionada, você está permitindo que eles realmente recebam (e não apenas acionem) a mensagem mais de uma vez.

Além disso, se você estiver tentando enviar uma mensagem imediatamente com uma re-eligibilidade de zero minutos, sempre tentaremos agendá-la imediatamente, independentemente de como um usuário recebeu versões anteriores da campanha ou Canvas.

#### Re-eligibilidade com campanhas acionadas por API

O número de vezes que um usuário recebe uma campanha acionada por API pode ser limitado usando configurações de re-eligibilidade. Isso significa que o usuário receberá a campanha apenas uma vez ou uma vez em uma determinada janela, independentemente de quantas vezes o gatilho da API for acionado.

Por exemplo, digamos que você esteja usando uma campanha acionada por API para enviar ao usuário uma campanha sobre um item que ele visualizou recentemente. Nesse caso, você pode limitar a campanha a enviar no máximo uma mensagem por dia, independentemente de quantos itens ele visualizou ao acionar o gatilho da API para cada item. Por outro lado, se sua campanha acionada por API for transacional, você vai querer garantir que o usuário receba a campanha toda vez que realizar a transação, definindo o atraso para zero minutos.
{% endtab %}

{% tab canvas %}

Para ativar a re-eligibilidade para um Canvas, selecione **Permitir que os usuários reentrem neste Canvas** na seção **Controles de Entrada**. Você pode escolher entre permitir que os usuários reentrem após a duração máxima do Canvas ou após uma janela especificada.

A re-eligibilidade para variantes de Canvas está ligada à entrada no Canvas, em vez do recebimento da mensagem. Usuários que entram em um Canvas e não recebem nenhuma mensagem não poderão reentrar no Canvas, a menos que a re-eligibilidade esteja ativada.

Observe que um usuário não precisa sair de um Canvas primeiro antes de reentrar se a re-eligibilidade estiver definida para zero segundos, o que significa que é possível para um usuário entrar no mesmo Canvas novamente. Você pode adicionar filtros adicionais para evitar que os usuários recebam o mesmo passo ou mensagem várias vezes. No entanto, quando um usuário reentra em um Canvas pela segunda vez, os passos recebidos anteriormente durante sua primeira vez no Canvas não são visíveis para o usuário. Isso significa que o usuário ainda pode receber a mesma mensagem novamente. Para evitar isso, você pode configurar o Canvas para impedir a reentrada ou definir a re-eligibilidade para a duração máxima do Canvas.

Você também pode usar um [Componente de Atualização do Usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) para o usuário que recebe o passo registrar isso como um atributo personalizado, que pode ser usado para filtrar usuários que receberam o passo durante sua jornada no Canvas.

### Exemplo

Por exemplo, suponha que um usuário sem endereço de e-mail entre em um Canvas recorrente diário que contém um passo na jornada do usuário. Esse passo contém apenas uma mensagem de e-mail, então o usuário não recebe o engajamento. Esse usuário não poderá entrar no Canvas novamente, a menos que a re-eligibilidade do Canvas esteja ativada. 

Se você tiver um Canvas recorrente ou acionado ativo sem re-eligibilidade, e gostaria que os usuários reentrassem no Canvas até receber uma mensagem dele, você pode considerar permitir que os usuários sejam re-eligíveis para entrada, adicionando um filtro aos critérios de entrada que exclui clientes que receberam uma mensagem do Canvas.

Se a re-eligibilidade para um Canvas estiver definida para um período mais curto do que a duração do Canvas, é possível que os usuários entrem no Canvas mais de uma vez, o que pode levar a comportamentos enganosos para Canvases que usam mensagens no aplicativo com atrasos particularmente longos. Como várias mensagens no aplicativo Canvas podem ser acionadas pelo mesmo início de sessão, o usuário pode potencialmente ter a experiência de receber a mesma mensagem repetidamente, se um componente específico renderizar mais rápido que os outros.
{% endtab %}
{% endtabs %}

## Cálculos de atraso de re-eligibilidade

A re-eligibilidade para campanhas e Canvases é calculada em segundos, não em dias do calendário. Isso significa que um dia conta como 24 horas (ou 86.400 segundos) a partir do momento em que um usuário recebe a mensagem, e não no próximo dia do calendário à meia-noite. Da mesma forma, um mês conta exatamente como 2.592.000 segundos, equivalente a aproximadamente 30 dias.

### Exemplo

Considere o seguinte cenário:

* Uma campanha está programada para ser enviada mensalmente no dia 15, com re-eligibilidade definida para 30 dias.
* Há menos de 30 dias entre 15 de fevereiro e 15 de março. 

Isso significa que os usuários que receberam a campanha em 15 de fevereiro não serão elegíveis para a campanha a ser enviada em 15 de março. Se a campanha estiver programada para ser enviada diariamente às 8h, com re-eligibilidade de 1 dia e houver uma latência no envio da mensagem, os usuários que receberam a campanha às 8h30 não estarão re-eligíveis ainda no dia seguinte às 8h.

## Teste multivariado

Para testes multivariados, a Braze determina a re-eligibilidade de variantes para todas as campanhas, mensagens acionadas no aplicativo e Canvases usando as seguintes regras:

- Quando as porcentagens de variantes não mudam, cada usuário sempre entrará na mesma variante de uma campanha, mensagem acionada no aplicativo ou entrada de Canvas toda vez que forem re-eligíveis.
- Se as porcentagens de variantes mudarem, os usuários podem ser redistribuídos para outras variantes.
- Os grupos de controle permanecerão consistentes se a porcentagem da variante não mudar, e nenhum usuário que recebeu mensagens anteriormente entrará no grupo de controle em um envio posterior, nem qualquer usuário no grupo de controle receberá uma mensagem.

