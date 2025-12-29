---
nav_title: Limitação de taxa e limitação de frequência
article_title: Limitação de taxa e limitação de frequência
page_order: 6
tool: Campaigns
page_type: reference
description: "Este artigo de referência discute o conceito de limitação de taxa e limite de frequência em campanhas e como você pode gerenciar a pressão de marketing para melhorar a experiência do usuário."

---

# Limitação de taxa e limitação de frequência

> A limitação de taxa e o limite de frequência podem ser usados em conjunto para garantir que seus usuários recebam as mensagens de que precisam e nenhuma das que não precisam.

## Sobre limitação de taxa

O Braze permite que você controle a pressão do marketing limitando a taxa de suas campanhas, regulando a quantidade de tráfego de saída de sua plataforma. Você pode implementar dois tipos diferentes de limitação de taxa para suas campanhas: 

1. [**Limitação de taxa centrada no usuário:**](#user-centric-rate-limiting) Concentra-se em fornecer a melhor experiência para o usuário.
2. [**Limitação da taxa de velocidade de entrega:**](#delivery-speed-rate-limiting) Leva em consideração a largura de banda de seus servidores.

O Braze tentará distribuir uniformemente os envios de mensagens ao longo do minuto, mas não pode garantir isso. Por exemplo, se você tiver uma campanha com um limite de taxa de 5.000 mensagens por minuto, tentaremos distribuir as 5.000 solicitações uniformemente ao longo do minuto (cerca de 84 mensagens por segundo), mas poderá haver alguma variação na taxa por segundo.

### Limitação de taxa centrada no usuário

À medida que você cria mais segmentos, haverá casos em que a associação desses segmentos se sobrepõe. Se estiver enviando campanhas para esses segmentos, é preciso ter certeza de que não está enviando mensagens aos usuários com muita frequência. Se um usuário receber muitas mensagens em um curto período de tempo, ele se sentirá sobrecarregado e desativará as notificações por push ou desinstalará o aplicativo.

#### Filtros de segmentos relevantes

O Braze fornece os seguintes filtros para ajudá-lo a limitar a taxa de recebimento de mensagens pelos seus usuários:

- Último engajamento com mensagem
- Última mensagem recebida
- Campanha Last Received Push
- Última campanha de e-mail recebida
- Último SMS recebido

#### Implementação de filtros

Digamos que tenhamos criado um segmento chamado "Retargeting Filter Showcase" com um filtro "Last used these apps more than 7 days ago" para segmentar os usuários. Esse seria um segmento de reengajamento padrão.

Se você tiver outros segmentos mais direcionados recebendo notificações recentemente, talvez não queira que seus usuários sejam alvo de campanhas mais genéricas direcionadas a esse segmento. Ao anexar o filtro "Last Received Push Campaign" a esse segmento, o usuário garante que, se tiver recebido outra notificação nas últimas 24 horas, ele sairá desse segmento nas próximas 24 horas. Se eles ainda atenderem aos outros critérios do segmento 24 horas depois e não tiverem recebido mais notificações, eles voltarão ao segmento.

\![Seção Segment Details (Detalhes do segmento) com o filtro de segmento "Last Received Any Message" (Última mensagem recebida) destacado.]({% image_buster /assets/img_archive/rate_limit_daily.png %})

Anexar esse filtro a todos os segmentos direcionados por campanhas faria com que seus usuários recebessem no máximo um push a cada 24 horas. Assim, você pode priorizar suas mensagens, garantindo que as mais importantes sejam entregues antes das menos importantes.

#### Definição de um limite máximo de usuários

Na etapa **Target Audiences (Públicos-alvo** ) do compositor da campanha, você também pode limitar o número total de usuários que receberão sua mensagem. Isso serve como uma verificação independente dos filtros da campanha, permitindo segmentar livremente os usuários sem se preocupar com o excesso de spam.

Resumo do público-alvo com uma caixa de seleção marcada para limitar o número de pessoas que recebem a campanha.]({% image_buster /assets/img_archive/total_limit.png %})

Ao selecionar o limite máximo de usuários, é possível limitar a taxa na qual os usuários recebem notificações por canal ou globalmente em todos os tipos de mensagens.

##### Limite máximo de usuários com otimizações

Se estiver usando uma otimização como Winning Variant ou Personalized Variant, a campanha consistirá em dois envios: o experimento inicial e o envio final. 

Para configurar um limite máximo de usuários nesse cenário, selecione **Limitar o número de pessoas que receberão esta campanha** e, em seguida, selecione **No total, esta campanha deve** e insira um limite de público. Seu limite de público-alvo será dividido de acordo com as porcentagens mostradas no painel **Teste A/B**. 

Se você selecionar **Sempre que a campanha for programada**, essas duas fases serão limitadas separadamente ao número definido. Normalmente, isso não é desejável.

#### Definição de um limite máximo de impressão

Para mensagens in-app e Content Cards, você pode controlar a pressão de marketing definindo um número máximo de impressões que serão exibidas à sua base de usuários, após o qual o Braze não enviará mais mensagens aos seus usuários. No entanto, é importante observar que esse limite não é exato. 

Os novos cartões de conteúdo e as regras de mensagens no aplicativo são enviados para um aplicativo no início da sessão, o que significa que o Braze pode enviar uma mensagem ao usuário antes que o limite seja atingido, mas quando o usuário acionar a mensagem, o limite já terá sido atingido. Nessa situação, o dispositivo ainda exibirá a mensagem.

Por exemplo, digamos que você tenha um jogo com uma mensagem in-app que é acionada quando um usuário vence um nível e você limita essa mensagem a 100 impressões. Foram registradas 99 impressões até o momento. Alice e Bob abrem o jogo e o Braze informa a seus dispositivos que eles estão qualificados para receber a mensagem quando passam de um nível. Alice vence um nível primeiro e recebe a mensagem. Bob vence o próximo nível, mas como seu dispositivo não se comunicou com os servidores Braze desde o início da sessão, ele não sabe que a mensagem atingiu seu limite e também receberá a mensagem. No entanto, quando um limite de impressões for atingido, na próxima vez que qualquer dispositivo solicitar a lista de mensagens in-app qualificadas, essa mensagem não será enviada e será removida desse dispositivo.

### Limitação de taxas e testes A/B

Ao usar a limitação de taxa com um teste A/B, o limite de taxa não é aplicado ao grupo de controle da mesma forma que o grupo de teste, o que é uma possível fonte de viés de tempo. Para evitar esse viés, use janelas de conversão adequadas.

### Limitação da taxa de velocidade de entrega

Se você prevê que grandes campanhas gerem um pico na atividade do usuário e sobrecarreguem seus servidores, é possível especificar um limite de taxa por minuto para o envio de mensagens, o que significa que o Braze não enviará mais do que sua configuração de taxa limitada em um minuto.

Ao segmentar os usuários durante a criação da campanha, você pode navegar até **Públicos-alvo** (para campanhas) ou **Configurações de envio** (para Canvas) para selecionar um limite de taxa (em vários incrementos, de 10 a 500.000 mensagens por minuto).

Observe que as campanhas não limitadas por taxa podem exceder esses limites de entrega. No entanto, esteja ciente de que as mensagens serão abortadas se forem atrasadas 72 horas ou mais devido a um limite de taxa baixo. Se o limite da taxa for muito baixo, o criador da campanha receberá alertas no painel e por e-mail.

\![Resumo do público-alvo com uma caixa de seleção marcada para limitar a taxa na qual a campanha será encerrada e a taxa sendo 500.000 por minuto.]({% image_buster /assets/img_archive/per_minute_rate_limit.png %})

#### Exemplo

Se você estiver tentando enviar 75.000 mensagens com um limite de taxa de 10.000 por minuto, a entrega será distribuída em oito minutos. Sua campanha entregará não mais do que 10.000 mensagens em cada um dos primeiros sete minutos e 5.000 no último minuto.

#### Número de envios

Observe que as mensagens com taxa limitada podem não ser enviadas uniformemente ao longo de cada minuto. Usando o exemplo de um limite de taxa de 10.000 por minuto, isso significa que o Braze garante que não sejam enviadas mais de 10.000 mensagens por minuto. Isso pode significar que uma porcentagem maior das 10.000 mensagens é enviada no primeiro meio minuto em comparação com o último meio minuto.

O limite de taxa é aplicado no início da tentativa de envio da mensagem. Quando há flutuações no tempo que leva para o envio ser concluído, o número de envios concluídos pode exceder ligeiramente o limite de taxa em alguns minutos. Com o passar do tempo, o número de envios por minuto atingirá a média de não mais do que o limite da taxa.

{% alert important %}
Tenha cuidado para não atrasar mensagens sensíveis ao tempo com essa forma de limitação de taxa em relação ao número total de usuários em um segmento. Por exemplo, se o segmento contiver 30 milhões de usuários, mas definirmos o limite de taxa para 10.000 por minuto, uma grande parte da sua base de usuários não receberá a mensagem até o dia seguinte.
{% endalert %}

#### Campanhas de canal único

Ao enviar uma campanha de canal único com um limite de taxa de velocidade, o limite de taxa é aplicado a todas as mensagens juntas.

#### Campanhas multicanais

Ao enviar uma campanha multicanal com um limite de taxa de velocidade, cada canal é enviado independentemente dos outros. Como resultado, pode ocorrer o seguinte:

- O número total de mensagens enviadas por minuto pode ser maior do que o limite da taxa. 
    - Por exemplo, se sua campanha tiver um limite de taxa de 10.000 por minuto e usar e-mail e SMS, o Braze poderá enviar um máximo de 20.000 mensagens totais por minuto (10.000 por e-mail e 10.000 por SMS).
- Os usuários podem receber os diferentes canais em horários diferentes, e não é previsível qual canal eles receberão primeiro. 
    - Por exemplo, se você enviar uma campanha que contenha um e-mail e um SMS, poderá ter 10.000 usuários com números de telefone válidos e 50.000 usuários com endereços de e-mail válidos. Se você definir a campanha para enviar 100 mensagens por minuto (um limite de taxa lento para o tamanho da campanha), um usuário poderá receber o SMS no primeiro lote de envios e o e-mail no último lote de envios, quase nove horas depois.

#### Campanhas push multiplataforma

Para campanhas push veiculadas em várias plataformas, o limite de taxa selecionado será distribuído igualmente entre as plataformas. Uma campanha push que utiliza Android e iOS com um limite de 10.000 mensagens por minuto distribuirá igualmente as 10.000 mensagens entre as duas plataformas.

#### Limitação da taxa de velocidade de entrega da tela {#canvas-delivery-speed}

Ao enviar um Canvas com um limite de taxa de velocidade, o limite de taxa é compartilhado entre os canais. Isso significa que o número total de mensagens enviadas por minuto a partir do Canvas não excederá o limite de taxa. Por exemplo, se o seu Canvas tiver um limite de taxa de 10.000 por minuto e usar e-mail e SMS, o Braze enviará um total de 10.000 mensagens por minuto por e-mail e SMS.

#### Limitação de taxa e novas tentativas de Connected Content

Quando a [repetição de Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries/) estiver ativada, o Braze tentará novamente as falhas de chamada, respeitando o limite de taxa que você definiu para cada reenvio. Vamos considerar o cenário de envio de 75.000 mensagens com um limite de taxa de 10.000 por minuto. Imagine que, no primeiro minuto, a chamada falhe ou esteja lenta e envie apenas 4.000 mensagens.

Em vez de tentar compensar o atraso e enviar as 6.000 mensagens restantes no segundo minuto ou adicioná-las às 10.000 que já estão definidas para envio, o Braze moverá essas 6.000 mensagens para o "final da fila" e adicionará um minuto, se necessário, ao total de minutos que levaria para enviar sua mensagem.

| Minuto | Sem falhas | 6.000 Falhas no minuto 1 |
|--------|------------|---------------------------|
| 1      | 10,000     | 4,000                     |
| 2      | 10,000     | 10,000                    |
| 3      | 10,000     | 10,000                    |
| 4      | 10,000     | 10,000                    |
| 5      | 10,000     | 10,000                    |
| 6      | 10,000     | 10,000                    |
| 7      | 10,000     | 10,000                    |
| 8      | 5,000      | 10,000                    |
| 9      | 0          | 6,000                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

As solicitações de Connected Content não são limitadas por taxa de forma independente e seguirão o limite de taxa do webhook. Isso significa que, se houver uma chamada de Connected Content para um endpoint exclusivo por webhook, você esperaria 5.000 webhooks e também 5.000 chamadas de Connected Content por minuto. Observe que o armazenamento em cache pode afetar isso e reduzir o número de chamadas ao Connected Content. Além disso, as novas tentativas podem aumentar as chamadas do Connected Content, portanto, recomendamos verificar se o ponto de extremidade do Connected Content pode lidar com alguma flutuação aqui.

## Sobre o limite de frequência

À medida que sua base de usuários continua a crescer e suas mensagens são ampliadas para incluir campanhas de ciclo de vida, acionadas, transacionais e de conversão, é importante evitar que suas notificações pareçam "spam" ou perturbadoras. Ao proporcionar maior controle sobre a experiência dos usuários, o limite de frequência permite criar as campanhas desejadas sem sobrecarregar o público.

### Visão geral dos recursos {#freq-cap-feat-over}

O limite de frequência é aplicado no nível de envio da campanha ou do componente do Canvas e pode ser configurado para cada espaço de trabalho em **Configurações** > **Regras de limite de frequência**.

Por padrão, o limite de frequência é ativado quando novas campanhas são criadas. A partir daí, você pode escolher o seguinte:

- Qual canal de mensagens você gostaria de capturar: push, e-mail, SMS, webhook, WhatsApp ou qualquer um desses cinco.
- Quantas vezes cada usuário deve receber uma campanha ou componente do Canvas enviado de um canal dentro de um determinado período de tempo.
- Quantas vezes cada usuário deve receber uma campanha ou componente do Canvas enviado por [tag](#frequency-capping-by-tag) em um determinado período de tempo.

Esse período de tempo pode ser medido em minutos, dias ou semanas (sete dias), com uma duração máxima de 30 dias.

Cada linha de limites de frequência será conectada usando o operador `AND`, e você pode adicionar até 10 regras por espaço de trabalho. Além disso, você pode incluir vários limites para os mesmos tipos de mensagem. Por exemplo, você pode limitar os usuários a não mais do que um envio por dia e a não mais do que três envios por semana.

Seção de limite de frequência com listas de campanhas e telas às quais as regras se aplicam e não se aplicam.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %})

#### Comportamento quando os usuários têm limite de frequência em uma etapa do Canvas

Se um usuário do Canvas tiver limite de frequência devido às configurações globais de limite de frequência, ele avançará imediatamente para a próxima etapa do Canvas. O usuário não sairá do Canvas por causa do limite de frequência.

### Regras de entrega

Pode haver algumas campanhas, como mensagens transacionais, que você deseja que sempre cheguem ao usuário, mesmo que ele já tenha atingido seu limite de frequência. Por exemplo, um aplicativo de entrega pode querer enviar um e-mail ou um push quando um item for entregue, independentemente de quantas campanhas o usuário tenha recebido.

Se quiser que uma determinada campanha substitua as regras de limite de frequência, você poderá configurar isso no painel do Braze ao programar a entrega dessa campanha, alternando o **limite de frequência** para **OFF**. 

Depois disso, você será perguntado se ainda deseja que essa campanha conte para o seu limite de frequência. As mensagens que contam para o limite de frequência são incluídas nos cálculos do filtro Intelligent Channel. Ao enviar [campanhas de API]({{site.baseurl}}/developer_guide/rest_api/messaging/#messaging), que geralmente são transacionais, você poderá especificar que uma campanha deve ignorar as regras de limite de frequência [na solicitação de API]({{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns), definindo `override_messaging_limits` como `true`.

Por padrão, as novas campanhas e Canvases que não obedecerem aos limites de frequência também não contarão para eles. Isso é configurável para cada campanha e Canvas.

{% alert note %}
Esse comportamento altera o comportamento padrão quando você desativa o limite de frequência para uma campanha ou Canvas. As alterações são compatíveis com versões anteriores e não afetam as mensagens que estão ativas no momento.
{% endalert %}

Seção de controles de entrega com o limite de frequência ativado.]({% image_buster /assets/img_archive/frequencycappingupdate.png %})

Canais diferentes em uma campanha multicanal contarão individualmente o limite de frequência. Por exemplo, se você criar uma campanha multicanal com push e e-mail e tiver um limite de frequência configurado para esses dois canais, o push será contabilizado em uma campanha de push e a mensagem de e-mail será contabilizada em uma campanha de mensagem de e-mail. A campanha também contará para uma "campanha de qualquer tipo". Se os usuários estiverem limitados a uma campanha push e uma campanha de e-mail por dia e um usuário receber essa campanha multicanal, ele não estará mais qualificado para campanhas push ou de e-mail pelo resto do dia (a menos que uma campanha ignore as regras de limitação de frequência).

As mensagens no aplicativo e os cartões de conteúdo não são contados como ou para os limites de campanhas ou componentes do Canvas de qualquer tipo.

{% alert important %}
O limite de frequência global é programado com base no fuso horário do usuário e é calculado por dias do calendário, não por períodos de 24 horas. Por exemplo, se você configurar uma regra de limite de frequência para enviar no máximo uma campanha por dia, um usuário poderá receber uma mensagem às 23h em seu fuso horário local e estará qualificado para receber outra mensagem uma hora depois.
{% endalert %}

#### Casos de uso

{% tabs %}
{% tab Use case 1 %}

Digamos que você defina uma regra de limite de frequência que solicite que o usuário não receba mais do que três campanhas de notificação por push ou componentes do Canvas por semana de todos os componentes da campanha ou do Canvas.

Se o seu usuário estiver programado para receber três notificações por push, duas mensagens no aplicativo e um Content Card esta semana, ele receberá todas essas mensagens.

{% endtab %}
{% tab Use case 2 %}

Esse cenário usa as seguintes regras de limite de frequência:

**Quando ocorre o seguinte cenário:**

- Um usuário aciona a mesma campanha, `Campaign ABC`, três vezes ao longo de uma semana.
- Esse usuário aciona o `Campaign ABC` uma vez na segunda-feira, uma vez na quarta-feira e uma vez na quinta-feira.

Seção de limite de frequência com a regra de enviar não mais do que 2 campanhas de notificação por push/etapas de tela de todas as campanhas/etapas de tela para um usuário a cada 1 semana.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Então, o comportamento esperado é esse:**

- Esse usuário receberá os envios da campanha que foram acionados na segunda e na quarta-feira.
- Esse usuário não receberá o terceiro envio de campanha na quinta-feira porque já recebeu dois envios de campanha push naquela semana.

{% endtab %}
{% endtabs %}

### Limite de frequência por tag

[As regras de limite de frequência](#delivery-rules) podem ser aplicadas aos espaços de trabalho usando tags específicas que você aplicou às suas campanhas e Canvases, permitindo que você baseie seu limite de frequência em grupos com nomes personalizados.

Com o limite de frequência por tag, as regras podem ser definidas nas tags principais e aninhadas, de modo que o Braze levará em conta todas as tags. Por exemplo, se você optou por usar a tag principal A para o limite de frequência, também incluiremos informações em todas as tags aninhadas (por exemplo, tags B e C) ao determinar o limite.

Você também pode combinar o limite de frequência regular com o limite de frequência por tags. Considere as seguintes regras:

1. Não mais do que três campanhas de notificação por push ou componentes do Canvas por semana em todas as etapas da campanha e do Canvas. <br>**E**
2. Não mais do que dois componentes de campanha de notificação por push ou do Canvas por semana com a tag `promotional`.

Seção Frequency Capping (Limite de frequência) com duas regras que limitam quantas campanhas de notificação push/Canvases podem ser enviadas a um usuário a cada 1 semana.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

Como resultado, seus usuários não receberão mais do que três envios de campanha por semana em todas as campanhas e etapas do Canvas e não mais do que duas campanhas de notificação por push ou componentes do Canvas com a tag `promotional`.

{% alert important %}
As telas são marcadas no nível da tela, em vez de serem marcadas por componente. Portanto, cada componente do Canvas herdará todas as tags de nível do Canvas.
{% endalert %}

#### Regras conflitantes

Quando as regras entram em conflito, a regra de limitação de frequência mais restritiva e aplicável será aplicada aos seus usuários. Por exemplo, digamos que você tenha as seguintes regras:

1. Não mais do que uma campanha de notificação por push ou componente do Canvas por semana de todos os componentes de campanha e do Canvas. <br>**E**
2. Não mais do que três campanhas de notificação por push ou componentes do Canvas por semana com a tag `promotional`.

Seção de limite de frequência com regras conflitantes para limitar quantas campanhas de notificação por push/etapas de tela são enviadas a um usuário a cada 1 semana.]({% image_buster /assets/img/global_rules.png %} "global rules")

Neste exemplo, seu usuário não receberá mais de uma campanha de notificação por push ou componentes do Canvas com a tag "promocional" em uma determinada semana, porque você especificou que os usuários não devem receber mais de uma campanha de notificação por push ou componente do Canvas de todas as campanhas e componentes do Canvas. Em outras palavras, a regra de frequência aplicável mais restritiva é a regra que será aplicada a um determinado usuário.

#### Contagem de etiquetas

O limite de frequência por regras de tag é calculado no momento em que uma mensagem é enviada. Isso significa que o limite de frequência por tag só conta as tags que estão atualmente nas campanhas ou Canvases que um usuário recebeu no passado. Ele não conta as tags que estavam nas campanhas ou telas durante o período em que foram enviadas, mas que já foram removidas. Ele contará se uma tag for adicionada posteriormente a uma mensagem que um usuário recebeu no passado, mas antes que a mensagem com a tag mais recente seja enviada.

##### Caso de uso

Considere as seguintes campanhas e o limite de frequência por regra de tag:

**Campanhas**:

- **A campanha A** é uma campanha push marcada como `promotional`. O envio está previsto para as 9 horas da manhã de segunda-feira.
- **A campanha B** é uma campanha de incentivo marcada como `promotional`. O envio está previsto para as 9 horas da manhã de quarta-feira.

**Limite de frequência por regra de etiqueta:**

- Seu usuário não deve receber mais do que uma campanha de notificação por push por semana com a tag `promotional`.<br><br>

| Ação | Resultado |
|---|---|
| A tag `promotional` é removida da **Campanha A** após o usuário ter recebido a mensagem, mas antes do **envio da Campanha B.** | Seu usuário receberá **a Campanha B**.|
| A tag `promotional` foi removida por engano da **Campanha A** depois que seu usuário recebeu a mensagem. <br> A tag é adicionada novamente à **Campanha A** na terça-feira, antes do envio **da Campanha B**. | Seu usuário não receberá **a Campanha B**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Envio em grandes escalas {#sending-at-large-scales}

O limite de frequência por regras de tag pode não ser aplicado corretamente em grandes escalas, como 100 mensagens por canal de campanhas ou componentes do Canvas.

Por exemplo, se sua regra de limitação de frequência por tag for:

> Não mais do que duas campanhas de e-mail ou componentes do Canvas com a tag `Promotional` para um usuário a cada semana.

Se você enviar ao usuário mais de 100 e-mails de campanhas e etapas do Canvas com o limite de frequência ativado ao longo de uma semana, mais de dois e-mails poderão ser enviados ao usuário.

Como 100 mensagens por canal são mais mensagens do que a maioria das marcas envia para seus usuários, é improvável que você seja afetado por essa limitação. Para evitar essa limitação, você pode definir um limite para o número máximo de e-mails que deseja que seus usuários recebam ao longo de uma semana.

Por exemplo, você pode configurar a seguinte regra:

> Não mais do que três campanhas de e-mail ou componentes do Canvas por semana em todas as etapas da campanha e do Canvas.

Essa regra garantirá que nenhum usuário receba mais de 100 e-mails por semana porque, no máximo, os usuários receberão três e-mails por semana de campanhas ou componentes do Canvas com o limite de frequência ativado.

