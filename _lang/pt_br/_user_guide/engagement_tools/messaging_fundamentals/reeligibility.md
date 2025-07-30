---
nav_title: Reelegibilidade
article_title: Reelegibilidade
page_order: 8
page_type: reference
description: "Este artigo de referência define a reelegibilidade para campanhas e telas."
tool:
    - Campaigns
    - Canvas
toc_headers: h2
---

# Reelegibilidade para campanhas e Canvas

> Ao programar uma campanha recorrente ou disparada ou o Canva, você tem a opção de permitir que os usuários se tornem reelegíveis para ela. A reelegibilidade significa que os usuários podem entrar na campanha ou no Canva várias vezes com base no disparo.

## Como funciona?

Por padrão, o Braze envia uma mensagem a um usuário apenas uma vez, mesmo que ele se requalifique várias vezes, pois a reelegibilidade precisa ser ativada separadamente. Depois de ativada, os membros qualificados terão permissão para receber mensagens novamente depois de receberem a primeira instância da campanha ou do Canva. Você pode indicar a linha do tempo em que os usuários se tornariam elegíveis novamente.

## Ativação da reelegibilidade

{% tabs local %}
{% tab campanha %}
Para ativar a reelegibilidade para uma campanha, marque a caixa de seleção **Permitir que os usuários se tornem reelegíveis para receber a campanha** na seção **Controles de entrega**. O tempo máximo de reelegibilidade para uma campanha é de 720 dias.

Para campanhas de mensagens disparadas com a reelegibilidade ativada, os usuários que [não receberam a mensagem da campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#why-did-a-user-not-receive-my-triggered-campaign) (apesar de terem concluído o evento de gatilho) se qualificarão automaticamente para a mensagem na próxima vez que concluírem o evento de gatilho. Isso ocorre porque a reelegibilidade se baseia no recebimento de mensagens e não na entrada na campanha. Ao tornar os usuários novamente elegíveis para uma campanha de mensagens disparadas, você permite que eles realmente recebam (e não simplesmente disparem) a mensagem mais de uma vez.

Além disso, se estiver tentando enviar uma mensagem imediatamente com uma reelegibilidade de zero minutos, sempre tentaremos agendá-la imediatamente, independentemente de como o usuário tenha recebido versões anteriores da campanha ou do Canva.

#### Re-eligibilidade com campanhas acionadas por API

O número de vezes que um usuário recebe uma campanha acionada por API pode ser limitado usando as configurações de re-eligibilidade. Isso significa que o usuário receberá a campanha apenas uma vez ou uma vez em uma janela específica, independentemente de quantas vezes o disparo da API for acionado.

Por exemplo, digamos que você esteja usando uma campanha disparada pela API para enviar ao usuário uma campanha sobre um item que ele visualizou recentemente. Neste caso, você pode limitar a campanha para enviar no máximo uma mensagem por dia, independentemente de quantos itens eles visualizaram enquanto disparavam o gatilho da API para cada item. Por outro lado, se sua campanha acionada por API for transacional, você vai querer garantir que o usuário receba a campanha toda vez que fizer a transação, definindo a postergação para zero minutos.
{% endtab %}

{% tab canvas %}
Para ativar a reelegibilidade de um Canvas, selecione **Permitir que os usuários entrem novamente nesse Canvas** na seção **Controles de entrada**. É possível escolher entre permitir que os usuários entrem novamente após a duração máxima do Canva ou após uma janela especificada.

A reelegibilidade para as variantes do Canvas está vinculada à entrada no Canvas e não ao recebimento de mensagens. Os usuários que entrarem em um Canvas e não receberem nenhuma mensagem não poderão entrar novamente no Canvas, a menos que a reelegibilidade esteja ativada.

### Exemplo

Por exemplo, suponha que um usuário sem um endereço de e-mail entre em um Canva recorrente diário que contenha uma etapa da jornada do usuário. Essa etapa contém apenas uma mensagem de e-mail, portanto, o usuário não recebe o engajamento. Esse usuário não poderá entrar no Canvas novamente, a menos que o Canvas tenha a reelegibilidade ativada. 

Se tiver um Canvas recorrente ou disparado ativo sem reelegibilidade e quiser que os usuários entrem novamente no Canvas até receberem uma mensagem dele, considere a possibilidade de permitir que os usuários sejam reelegíveis para entrada adicionando um filtro aos critérios de entrada que exclua os clientes que receberam uma mensagem do Canvas.

Se a reelegibilidade para um Canvas for definida como mais curta do que a duração do Canvas, é possível que os usuários entrem no Canvas mais de uma vez, o que pode levar a um envio de mensagens enganosas para Canvas que usam mensagens no app com postergações particularmente longas. Como várias mensagens no app do Canvas podem ser disparadas pelo mesmo início de sessão, o usuário pode ter a experiência de receber a mesma mensagem repetidamente, se um componente específico for renderizado mais rapidamente do que outros.
{% endtab %}
{% endtabs %}

## Cálculos de postergação de reelegibilidade

A reelegibilidade para campanhas e Canvas é calculada em segundos, não em dias corridos. Isso significa que um dia conta como 24 horas (ou 86.400 segundos) a partir do momento em que o usuário recebe a mensagem, e não no próximo dia do calendário, à meia-noite. Da mesma forma, um mês conta exatamente 2.592.000 segundos, o que equivale a aproximadamente 30 dias.

### Exemplo

Considere o seguinte cenário:

* Uma campanha está configurada para ser enviada mensalmente no dia 15, com a reelegibilidade definida para 30 dias.
* Há menos de 30 dias entre 15 de fevereiro e 15 de março. 

Isso significa que os usuários que receberam a campanha em 15 de fevereiro não serão elegíveis para a campanha a ser enviada em 15 de março. Se a campanha estiver definida para ser enviada diariamente às 8h com reelegibilidade de 1 dia e houver uma latência no envio da mensagem, os usuários que receberam a campanha às 8h30 ainda não serão reelegíveis no dia seguinte às 8h.

## Testes multivariantes

Para testes multivariantes, o Braze determina a reelegibilidade de variantes para todas as campanhas, mensagens no app disparadas e Canvas usando as seguintes regras:

- Quando as porcentagens de variantes não são alteradas, cada usuário sempre entrará na mesma variante de uma campanha, mensagem no app disparada ou entrada do Canva toda vez que for reelegível.
- Se as porcentagens de variantes mudarem, os usuários poderão ser redistribuídos para outras variantes.
- Os grupos de controle permanecerão consistentes se a porcentagem de variantes permanecer inalterada, e nenhum usuário que tenha recebido mensagens anteriormente entrará no grupo de controle em um envio posterior, nem nenhum usuário do grupo de controle receberá uma mensagem.

