---
nav_title: Reelegibilidade
article_title: Reelegibilidade
page_order: 10
page_type: reference
description: "Este artigo de referência define a re-elegibilidade para campanhas e Canvases."
tool:
    - Campaigns
    - Canvas
toc_headers: h2
---

# Re-elegibilidade para campanhas e Canvas

> Quando você agenda uma campanha ou Canvas recorrente ou disparado, tem a opção de permitir que os usuários se tornem re-elegíveis para isso. Re-elegibilidade significa que os usuários podem entrar na campanha ou Canvas várias vezes com base no gatilho.

## Como funciona?

Por padrão, a Braze envia uma mensagem a um usuário apenas uma vez, mesmo que ele se requalifique várias vezes, pois a re-elegibilidade precisa ser ativada separadamente. Depois que for ativada, os membros qualificados poderão receber mensagens novamente após terem recebido a primeira instância da campanha ou Canvas. Você pode indicar a linha do tempo em que os usuários se tornariam elegíveis novamente.

## Ativando a re-elegibilidade

{% tabs local %}
{% tab campaign %}
Para ativar a reelegibilidade para uma campanha, marque a caixa de seleção **Permitir que os usuários se tornem reelegíveis para receber a campanha** na seção **Controles de entrega**. O tempo máximo de reelegibilidade para uma campanha é de 720 dias.

Para campanhas disparadas com a re-elegibilidade ativada, usuários que [não receberam realmente a mensagem da campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#why-did-a-user-not-receive-my-triggered-campaign) (apesar de terem completado o evento de gatilho) se qualificarão automaticamente para a mensagem na próxima vez que completarem o evento de gatilho. Isso ocorre porque a reelegibilidade se baseia no recebimento de mensagens e não na entrada na campanha. Ao tornar os usuários novamente elegíveis para uma campanha de mensagens disparadas, você permite que eles realmente recebam (e não simplesmente disparem) a mensagem mais de uma vez.

Além disso, se você estiver tentando enviar uma mensagem imediatamente com uma re-elegibilidade de zero minutos, sempre tentaremos agendá-la imediatamente, independentemente de como um usuário recebeu versões anteriores da campanha ou Canvas.

#### Re-eligibilidade com campanhas acionadas por API

O número de vezes que um usuário recebe uma campanha acionada por API pode ser limitado usando as configurações de re-eligibilidade. Isso significa que o usuário receberá a campanha apenas uma vez ou uma vez em uma janela específica, independentemente de quantas vezes o disparo da API for acionado.

Por exemplo, digamos que você esteja usando uma campanha disparada por API para enviar ao usuário uma campanha sobre um item que ele visualizou recentemente. Nesse caso, você pode limitar a campanha a enviar até uma mensagem por dia, independentemente de quantos itens ele visualizou, enquanto dispara o gatilho da API para cada item. Por outro lado, se sua campanha acionada por API for transacional, você vai querer garantir que o usuário receba a campanha toda vez que fizer a transação, definindo a postergação para zero minutos.
{% endtab %}

{% tab canvas %}

Para ativar a re-elegibilidade para um Canvas, selecione **Permitir que os usuários reentrem neste Canvas** na seção **Controles de Entrada**. Você pode escolher entre permitir que os usuários reentrem após a duração máxima do Canvas ou após uma janela especificada.

A reelegibilidade para as variantes do Canvas está vinculada à entrada no Canvas e não ao recebimento de mensagens. Os usuários que entrarem em um Canvas e não receberem nenhuma mensagem não poderão entrar novamente no Canvas, a menos que a reelegibilidade esteja ativada.

Observe que um usuário não precisa sair de um Canvas primeiro antes de reentrar se a re-elegibilidade estiver definida para zero segundos, o que significa que um usuário pode entrar no mesmo Canvas novamente. Como outro exemplo, se a duração do Canvas estiver definida para 7 dias e o período de re-elegibilidade estiver definido para 3 dias, um usuário pode reentrar no Canvas antes de completar sua primeira jornada através dele.

Você pode adicionar filtros adicionais para evitar que os usuários recebam o mesmo passo ou mensagem várias vezes. No entanto, quando um usuário reentra em um Canvas pela segunda vez, os passos recebidos anteriormente durante sua primeira vez no Canvas não são visíveis para o usuário. Isso significa que o usuário pode ainda receber a mesma mensagem novamente. Para evitar isso, você pode configurar o Canvas para impedir reentrada ou definir a re-elegibilidade para a duração máxima do Canvas.

Você também pode usar um [Passo de Atualização do Usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) para o usuário que recebe o passo registrar isso como um atributo personalizado, que pode ser usado para filtrar usuários que receberam o passo durante sua jornada no Canvas.

### Exemplo

Por exemplo, suponha que um usuário sem um endereço de e-mail entre em um Canva recorrente diário que contenha uma etapa da jornada do usuário. Esta etapa contém apenas uma mensagem de e-mail, então o usuário não obtém o engajamento. Este usuário não poderá entrar no canva novamente a menos que a re-elegibilidade do canva esteja ativada. 

Se tiver um Canvas recorrente ou disparado ativo sem reelegibilidade e quiser que os usuários entrem novamente no Canvas até receberem uma mensagem dele, considere a possibilidade de permitir que os usuários sejam reelegíveis para entrada adicionando um filtro aos critérios de entrada que exclua os clientes que receberam uma mensagem do Canvas.

Se a reelegibilidade para um Canvas for definida como mais curta do que a duração do Canvas, é possível que os usuários entrem no Canvas mais de uma vez, o que pode levar a um envio de mensagens enganosas para Canvas que usam mensagens no app com postergações particularmente longas. Como várias mensagens in-app do canva podem ser acionadas pelo mesmo início de sessão, o usuário pode potencialmente ter a experiência de receber a mesma mensagem repetidamente se um componente específico renderizar mais rápido que os outros.
{% endtab %}
{% endtabs %}

## Cálculos de postergação de reelegibilidade

A re-elegibilidade para campanhas e canvases é calculada em segundos, não em dias do calendário. Isso significa que um dia conta como 24 horas (ou 86.400 segundos) a partir do momento em que o usuário recebe a mensagem, e não no próximo dia do calendário, à meia-noite. Da mesma forma, um mês conta exatamente 2.592.000 segundos, o que equivale a aproximadamente 30 dias.

### Exemplo

Considere o seguinte cenário:

* Uma campanha está configurada para ser enviada mensalmente no dia 15, com a reelegibilidade definida para 30 dias.
* Há menos de 30 dias entre 15 de fevereiro e 15 de março. 

Isso significa que os usuários que receberam a campanha em 15 de fevereiro não serão elegíveis para a campanha a ser enviada em 15 de março. Se a campanha estiver configurada para enviar diariamente às 8 da manhã com re-elegibilidade de 1 dia, e houver uma latência no envio da mensagem, os usuários que receberam a campanha às 8:30 da manhã ainda não estarão re-elegíveis no dia seguinte às 8 da manhã.

## Testes multivariantes

Para testes multivariantes, a Braze determina a re-elegibilidade de variantes para todas as campanhas, mensagens in-app acionadas e canvases usando as seguintes regras:

- Quando as porcentagens de variantes não são alteradas, cada usuário sempre entrará na mesma variante de uma campanha, mensagem no app disparada ou entrada do Canva toda vez que for reelegível.
- Se as porcentagens de variantes mudarem, os usuários poderão ser redistribuídos para outras variantes.
- Os grupos de controle permanecerão consistentes se a porcentagem de variantes permanecer inalterada, e nenhum usuário que tenha recebido mensagens anteriormente entrará no grupo de controle em um envio posterior, nem nenhum usuário do grupo de controle receberá uma mensagem.
