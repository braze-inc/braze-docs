---
nav_title: Limite de frequência e limitação de frequência
article_title: Limite de frequência e limitação de frequência
page_order: 6
tool: Campaigns
page_type: reference
description: "Este artigo de referência discute o conceito de limite de taxa e limite de frequência em campanhas e como é possível gerenciar a pressão de marketing para melhorar a experiência do usuário."

---

# Limite de taxa e limite de frequência

> O limite de taxa e o limite de frequência podem ser usados em conjunto para garantir que os usuários recebam as mensagens de que precisam e nenhuma das que não precisam.

## Sobre o limite de frequência

O Braze permite que você controle a pressão do marketing limitando a frequência de suas campanhas, regulando a quantidade de tráfego de saída de sua plataforma. Você pode implementar dois tipos diferentes de limites de frequência para suas campanhas: 

1. [**Limite de frequência centrado no usuário:**](#user-centric-rate-limiting) Concentra-se em fornecer a melhor experiência para o usuário.
2. [**Limite de frequência da velocidade de entrega:**](#delivery-speed-rate-limiting) Leva em consideração a largura de banda de seus servidores.

O Braze tentará distribuir uniformemente os envios de mensagens ao longo do minuto, mas não pode garantir isso. Por exemplo, se você tiver uma campanha com um limite de frequência de 5.000 mensagens por minuto, tentaremos distribuir as 5.000 solicitações uniformemente ao longo do minuto (cerca de 84 mensagens por segundo), mas pode haver alguma variação na taxa por segundo.

### Limite de frequência centrado no usuário

À medida que você cria mais segmentos, haverá casos em que a associação desses segmentos se sobrepõe. Se estiver enviando campanhas para esses segmentos, queira mesmo ter certeza de que não está enviando mensagens com muita frequência para seus usuários. Se um usuário receber muitas mensagens em um curto período de tempo, ele se sentirá sobrecarregado e desativará as notificações por push ou desinstalará o app.

#### Filtros de segmentos relevantes

O Braze fornece os seguintes filtros para ajudá-lo a limitar a frequência com que seus usuários recebem mensagens:

- Última interação com mensagem
- Último recebimento de qualquer mensagem
- Último recebimento de campanha por push
- Última campanha de e-mail recebida
- Último SMS recebido

#### Implementação de filtros

Digamos que criamos um segmento chamado "Vitrine de filtros de redirecionamento" com um filtro "Usou esses apps pela última vez há mais de 7 dias" para direcionar os usuários. Esse seria um segmento de reengajamento padrão.

Se tiver outros segmentos mais direcionados recebendo notificações recentemente, talvez não queira que seus usuários sejam alvo de campanhas mais genéricas direcionadas a esse segmento. Ao anexar o filtro "Last Received Push Campaign" a esse segmento, o usuário garante que, se tiver recebido outra notificação nas últimas 24 horas, ele sairá desse segmento nas próximas 24 horas. Se eles ainda atenderem aos outros critérios do segmento 24 horas depois e não tiverem recebido mais notificações, eles voltarão ao segmento.

![Seção Segment Details (Detalhes do segmento) com o filtro de segmento "Last Received Any Message" (Última mensagem recebida) destacado.]({% image_buster /assets/img_archive/rate_limit_daily.png %})

Anexar esse filtro a todos os segmentos direcionados por campanhas faria com que seus usuários recebessem no máximo um push a cada 24 horas. Assim, é possível priorizar o envio de mensagens, garantindo que as mais importantes sejam entregues antes das menos importantes.

#### Definição de um limite máximo de usuários

Na etapa **Target Audiences (Públicos-alvo** ) do criador de sua campanha, também é possível limitar o número total de usuários que receberão sua mensagem. Isso serve como uma verificação independente dos filtros da campanha, permitindo que você segmente livremente os usuários sem se preocupar com o excesso de spam.

![Resumo do público com uma caixa de seleção marcada para limitar o número de pessoas que recebem a campanha.]({% image_buster /assets/img_archive/total_limit.png %})

Ao selecionar o limite máximo de usuários, é possível limitar a frequência com que os usuários recebem notificações por canal ou globalmente em todos os tipos de mensagens.

##### Limite máximo de usuários com otimizações

Se estiver usando uma otimização como Winning Variant ou Personalized Variant, a campanha consistirá em dois envios: o experimento inicial e o envio final. 

Para configurar um limite máximo de usuários nesse cenário, selecione **Limitar o número de pessoas que receberão esta campanha** e, em seguida, selecione **No total, esta campanha deve** e insira um limite de público. Seu limite de público será dividido de acordo com as porcentagens mostradas no painel **Testes A/B**. 

Se você selecionar **Sempre que a campanha for programada**, essas duas fases serão limitadas separadamente ao número definido. Normalmente, isso não é desejável.

#### Definição de um limite máximo de impressões

Para mensagens no app e cartões de conteúdo, é possível controlar a pressão de marketing definindo um número máximo de impressões que serão exibidas para sua base de usuários, após o qual o Braze não enviará mais mensagens para seus usuários. No entanto, é importante notar que esse limite não é exato. 

Os novos cartões de conteúdo e as regras de mensagens no app são enviados para um aplicativo no início da sessão, o que significa que o Braze pode enviar uma mensagem ao usuário antes que o limite seja atingido, mas, quando o usuário disparar a mensagem, o limite já terá sido atingido. Nessa situação, o dispositivo ainda exibirá a mensagem.

Por exemplo, digamos que você tenha um jogo com uma mensagem no app que dispara quando o usuário passa de um nível e você limita essa mensagem a 100 impressões. Até o momento, foram registradas 99 impressões. Alice e Bob abrem o jogo e a Braze informa a seus dispositivos que eles são elegíveis para receber a mensagem quando passam de um nível. Alice vence um nível primeiro e recebe a mensagem. Bob vence o próximo nível, mas como seu dispositivo não se comunicou com os servidores Braze desde o início da sessão, ele não sabe que a mensagem atingiu seu limite e também receberá a mensagem. No entanto, quando um limite de impressões for atingido, na próxima vez que qualquer dispositivo solicitar a lista de mensagens no app elegíveis, essa mensagem não será enviada e será removida desse dispositivo.

### Limite de frequência e Testes A/B

Ao usar o limite de frequência com um Testes A/B, o limite de frequência não é aplicado ao grupo de controle da mesma forma que o grupo de teste, o que é uma fonte potencial de viés de tempo. Para evitar esse viés, use janelas de conversão adequadas.

### Limite de frequência da velocidade de entrega

Caso preveja que grandes campanhas gerem um pico na atividade do usuário e sobrecarreguem seus servidores, é possível especificar um limite de frequência por minuto para o envio de mensagens, o que significa que o Braze não enviará mais do que sua configuração de limite de frequência em um minuto.

Ao direcionar os usuários durante a criação da campanha, é possível navegar até **Públicos-alvo** (para campanhas) ou **Configurações de envio** (para o Canva) para selecionar um limite de frequência (em vários incrementos, de 10 a 500.000 mensagens por minuto).

Observe que as campanhas sem limite de frequência podem exceder esses limites de entrega. No entanto, esteja ciente de que as mensagens serão abortadas se sofrerem uma postergação de 72 horas ou mais devido a um limite de frequência baixo. Se o limite de frequência for muito baixo, o criador da campanha receberá alertas no dashboard e por e-mail.

![Resumo do público com uma caixa de seleção marcada para limitar a taxa na qual a campanha será encerrada, e a taxa sendo 500.000 por minuto.]({% image_buster /assets/img_archive/per_minute_rate_limit.png %})

Como outro exemplo, se estiver tentando enviar 75.000 mensagens com um limite de frequência de 10.000 por minuto, a entrega será distribuída em 8 minutos. Sua campanha enviará não mais do que 10.000 mensagens em cada um dos primeiros sete minutos e 5.000 no último minuto.

Observe que as mensagens com limite de frequência podem não ser enviadas uniformemente ao longo de cada minuto. Usando o exemplo de um limite de frequência de 10.000 por minuto, isso significa que o Braze garante que não sejam enviadas mais de 10.000 mensagens por minuto. Isso pode significar que uma porcentagem maior das 10.000 mensagens é enviada no primeiro meio minuto em comparação com o último meio minuto. 

Além disso, observe que o limite de frequência é aplicado no início da tentativa de envio de mensagens. Quando há flutuações no tempo que leva para o envio ser concluído, o número de envios concluídos pode exceder ligeiramente o limite de frequência em alguns minutos. Com o passar do tempo, o número de envios por minuto atingirá a média de não mais do que o limite de frequência.

{% alert important %}
Tenha cuidado com a postergação de mensagens sensíveis ao tempo com essa forma de limite de frequência em relação ao número total de usuários em um segmento. Por exemplo, se o segmento contiver 30 milhões de usuários, mas definirmos o limite de frequência para 10.000 por minuto, uma grande parte da sua base de usuários não receberá a mensagem até o dia seguinte.
{% endalert %}

#### Campanhas de canal único

Ao enviar uma campanha de canal único com um limite de frequência, o limite de frequência é aplicado a todas as mensagens juntas.

#### Campanhas multicanais

Ao enviar uma campanha multicanais com um limite de frequência, cada canal é enviado independentemente dos outros. Como resultado, pode ocorrer o seguinte:

- O número total de mensagens enviadas por minuto pode ser maior do que o limite de frequência. 
    - Por exemplo, se sua campanha tiver um limite de frequência de 10.000 por minuto e usar e-mail e SMS, o Braze poderá enviar um máximo de 20.000 mensagens totais por minuto (10.000 por e-mail e 10.000 por SMS).
- Os usuários podem receber os diferentes canais em momentos diferentes, e não há previsão de qual canal eles receberão primeiro. 
    - Por exemplo, se você enviar uma campanha que contenha um e-mail e um SMS, poderá ter 10.000 usuários com números de telefone válidos e 50.000 usuários com endereços de e-mail válidos. Se você definir a campanha para enviar 100 mensagens por minuto (um limite de frequência lento para o tamanho da campanha), um usuário poderá receber o SMS no primeiro lote de envios e o e-mail no último lote de envios, quase nove horas depois.

#### Campanhas push multiplataforma

Para campanhas push veiculadas em várias plataformas, o limite de frequência selecionado será distribuído igualmente entre as plataformas. Uma campanha de mensagens push que aproveite o Android e o iOS com um limite de frequência de 10.000 por minuto distribuirá igualmente as 10.000 mensagens nas duas plataformas.

#### Limite de frequência da velocidade de entrega da tela {#canvas-delivery-speed}

Ao enviar uma tela com um limite de frequência de velocidade, o limite de frequência é compartilhado entre os canais. Isso significa que o número total de mensagens enviadas por minuto a partir do Canva não excederá o limite de frequência. Por exemplo, se seu Canvas tiver um limite de frequência de 10.000 por minuto e usar e-mail e SMS, o Braze enviará um total de 10.000 mensagens por minuto por e-mail e SMS.

#### Limite de frequência e novas tentativas do Connected Content

Quando a [repetição de Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries/) estiver ativada, o Braze tentará novamente as falhas de chamada, respeitando o limite de frequência que você definiu para cada reenvio. Vamos considerar o cenário de envio de 75.000 mensagens com um limite de frequência de 10.000 por minuto. Imagine que, no primeiro minuto, a chamada falhe ou esteja lenta e envie apenas 4.000 mensagens.

Em vez de tentar compensar a postergação e enviar as 6.000 mensagens restantes no segundo minuto ou adicioná-las às 10.000 que já estão definidas para envio, o Braze moverá essas 6.000 mensagens para o "final da fila" e adicionará um minuto, se necessário, ao total de minutos que levaria para enviar sua mensagem.

| Minuto | Sem falhas | 6.000 falhas no minuto 1 |
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

As solicitações de Connected Content não têm limite de frequência de forma independente e seguirão o limite de frequência do webhook. Isso significa que, se houver uma chamada de Connected Content para um endpoint exclusivo por webhook, você esperaria 5.000 webhooks e também 5.000 chamadas de Connected Content por minuto. Observe que o armazenamento em cache pode afetar isso e reduzir o número de chamadas ao Connected Content. Além disso, as novas tentativas podem aumentar as chamadas do Connected Content, portanto, recomendamos verificar se o ponto de extremidade do Connected Content pode lidar com alguma flutuação aqui.

## Sobre o limite de frequência

À medida que sua base de usuários continua a crescer e seu envio de mensagens é ampliado para incluir campanhas de ciclo de vida, disparadas, transacionais e de conversão, é importante evitar que suas notificações pareçam "spam" ou perturbadoras. Ao proporcionar maior controle sobre a experiência dos usuários, a capacitação de frequência ativa a criação das campanhas desejadas sem sobrecarregar o público.

### Visão geral dos recursos {#freq-cap-feat-over}

O limite de frequência é aplicado no nível de envio da campanha ou do componente do Canva e pode ser configurado para cada espaço de trabalho em **Configurações** > **Regras de limite de frequência**.

Por padrão, o limite de frequência é ativado quando novas campanhas são criadas. A partir daí, você pode escolher o seguinte:

- Qual canal de envio de mensagens você gostaria de capturar: push, e-mail, SMS, webhook, WhatsApp ou qualquer um desses cinco.
- Quantas vezes cada usuário deve receber uma campanha ou componente do Canva enviado por um canal em um determinado período de tempo.
- Quantas vezes cada usuário deve receber uma campanha ou componente do Canva enviado por [tag](#frequency-capping-by-tag) em um determinado período de tempo.

Esse período de tempo pode ser medido em minutos, dias ou semanas (sete dias), com uma duração máxima de 30 dias.

Cada linha de limites de frequência será conectada usando o operador `AND`, e você pode adicionar até 10 regras por espaço de trabalho. Além disso, você pode incluir vários limites para os mesmos tipos de mensagens. Por exemplo, você pode limitar os usuários a não mais do que um push por dia e a não mais do que três pushs por semana.

![Seção de limite de frequência com listas de campanhas e telas às quais as regras se aplicam e não se aplicam.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %})

#### Comportamento quando os usuários têm limite de frequência em uma etapa do Canva

Se um usuário do Canva estiver com a frequência limitada devido às configurações globais de limitação de frequência, o usuário avançará imediatamente para a próxima etapa do Canva. O usuário não sairá do Canva por causa do limite de frequência.

### Regras de entrega

Pode haver algumas campanhas, como mensagens transacionais, que você deseja que sempre cheguem ao usuário, mesmo que ele já tenha atingido seu limite de frequência. Por exemplo, um app de entrega pode querer enviar um e-mail ou push quando um item for entregue, independentemente de quantas campanhas o usuário tenha recebido.

Se quiser que uma campanha específica substitua as regras de limite de frequência, você poderá configurar isso no dashboard do Braze ao programar a entrega dessa campanha, alternando **o limite de frequência** para **OFF**. 

Depois disso, você será perguntado se ainda deseja que essa campanha conte para o seu limite de frequência. As mensagens que contam para o limite de frequência são incluídas nos cálculos do filtro do Canal inteligente. Ao enviar [campanhas de API]({{site.baseurl}}/developer_guide/rest_api/messaging/#messaging), que geralmente são transacionais, você poderá especificar que uma campanha deve ignorar as regras de limite de frequência [na solicitação de API]({{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns), definindo `override_messaging_limits` como `true`.

Por padrão, as novas campanhas e canvas que não obedecerem aos limites de frequência também não contarão para eles. Isso é configurável para cada campanha e Canva.

{% alert note %}
Esse comportamento altera o comportamento padrão quando você desativa o limite de frequência para uma campanha ou uma tela. As alterações são compatíveis com versões anteriores e não afetam as mensagens que estão ativas no momento.
{% endalert %}

![Seção Controles de entrega com o limite de frequência ativado.]({% image_buster /assets/img_archive/frequencycappingupdate.png %})

Diferentes canais em uma campanha multicanal contarão individualmente o limite de frequência. Por exemplo, se você criar uma campanha em vários canais com push e e-mail e tiver um limite de frequência configurado para esses dois canais, o push será contabilizado em uma campanha de push e a mensagem de e-mail será contabilizada em uma campanha de mensagem de e-mail. A campanha também contará para uma "campanha de qualquer tipo". Se os usuários estiverem limitados a uma campanha push e uma campanha de e-mail por dia e um usuário receber essa campanha multicanal, ele não será mais elegível para campanhas push ou de e-mail pelo resto do dia (a menos que uma campanha ignore as regras de limitação de frequência).

As mensagens no app e os cartões de conteúdo não são contados como ou para os limites de campanhas ou componentes do Canvas de qualquer tipo.

{% alert important %}
O limite de frequência global é programado com base no fuso horário do usuário e é calculado por dias do calendário, não por períodos de 24 horas. Por exemplo, se você configurar uma regra de limite de frequência de envio de no máximo uma campanha por dia, um usuário poderá receber uma mensagem às 23h em seu fuso local e será elegível para receber outra mensagem uma hora depois.
{% endalert %}

#### Casos de uso

{% tabs %}
{% tab Caso de uso 1 %}

Digamos que você defina uma regra de limite de frequência que solicite que o usuário não receba mais do que três campanhas de notificações por push ou componentes do Canvas por semana de todas as campanhas ou componentes do Canvas.

Se o seu usuário estiver programado para receber três notificações por push, duas mensagens no app e um cartão de conteúdo nesta semana, ele receberá todas essas mensagens.

{% endtab %}
{% tab Caso de uso 2 %}

Esse cenário usa as seguintes regras de limite de frequência:

**Quando ocorre o seguinte cenário:**

- Um usuário dispara a mesma campanha, `Campaign ABC`, três vezes ao longo de uma semana.
- Esse usuário dispara `Campaign ABC` uma vez na segunda-feira, uma vez na quarta-feira e uma vez na quinta-feira.

![Seção Limite de frequência com a regra de enviar não mais do que 2 campanhas de notificação por push/etapas do canva de todas as campanhas/etapas do canva para um usuário a cada 1 semana.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Então, o comportamento esperado é esse:**

- Esse usuário receberá os envios da campanha que foram disparados na segunda e na quarta-feira.
- Esse usuário não receberá o terceiro envio de campanha na quinta-feira porque já recebeu dois envios de campanha push naquela semana.

{% endtab %}
{% endtabs %}

### Limite de frequência por tag

[As regras de limite de frequência](#delivery-rules) podem ser aplicadas aos espaços de trabalho usando tags específicas que você aplicou às suas campanhas e Canvas, permitindo que você baseie essencialmente o limite de frequência em grupos com nomes personalizados.

Com o limite de frequência por tag, as regras podem ser definidas nas tags principais e aninhadas, de modo que o Braze levará em conta todas as tags. Por exemplo, se você optou por usar a tag principal A para o limite de frequência, também incluiremos informações em todas as tags aninhadas (por exemplo, as tags B e C) ao determinar o limite.

Você também pode combinar o limite de frequência regular com o limite de frequência por tags. Considere as seguintes regras:

1. Não mais do que três campanhas de notificação por push ou componentes do Canvas por semana em todas as etapas da campanha e do Canvas. <br>**E**
2. Não mais do que dois componentes de campanha de notificação por push ou do Canvas por semana com a tag `promotional`.

![Seção de limite de frequência com duas regras que limitam quantas campanhas/canvas de notificação por push podem ser enviadas a um usuário a cada 1 semana.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

Como resultado, seus usuários não receberão mais do que três envios de campanha por semana em todas as campanhas e etapas do Canva e não mais do que duas campanhas de notificação por push ou componentes do Canvas com a tag `promotional`.

{% alert important %}
Os canvas são marcados no nível dos canvas, em vez de serem marcados por componente. Portanto, cada componente do Canvas herdará todas as tags de nível do Canvas.
{% endalert %}

#### Regras conflitantes

Quando as regras entram em conflito, a regra de limitação de frequência mais restritiva e aplicável será aplicada aos seus usuários. Por exemplo, digamos que você tenha as seguintes regras:

1. Não mais do que uma campanha de notificação por push ou componente do Canvas por semana de todos os componentes de campanha e do Canvas. <br>**E**
2. Não mais do que três campanhas de notificação por push ou componentes do Canvas por semana com a tag `promotional`.

![Seção de limite de frequência com regras conflitantes para limitar quantas campanhas de notificação por push/etapas do canva são enviadas a um usuário a cada 1 semana.]({% image_buster /assets/img/global_rules.png %} "global rules")

Neste exemplo, seu usuário não receberá mais de uma campanha de notificação por push ou componentes do Canvas com a tag "promocional" em uma determinada semana, porque você especificou que os usuários não devem receber mais de uma campanha de notificação por push ou componente do Canvas de todas as campanhas e componentes do Canvas. Em outras palavras, a regra de frequência aplicável mais restritiva é a regra que será aplicada a um determinado usuário.

#### Contagem de tags

O limite de frequência por regras de tag é calculado no momento em que uma mensagem é enviada. Isso significa que o limite de frequência por tag só conta as tags que estão atualmente nas campanhas ou Canvas que um usuário recebeu no passado. Não são contadas as tags que estavam nas campanhas ou canvas durante o período em que foram enviadas, mas que já foram removidas. Ele contará se uma tag for adicionada posteriormente a uma mensagem que um usuário recebeu no passado, mas antes que a mensagem com a tag mais recente seja enviada.

##### Caso de uso

Considere as seguintes campanhas e o limite de frequência por regra de tag:

**Campanhas**:

- **A campanha A** é uma campanha push com a tag `promotional`. O envio está previsto para as 9 horas de segunda-feira.
- **A campanha B** é uma campanha push com a tag `promotional`. O envio está previsto para as 9 horas da manhã de quarta-feira.

**Limite de frequência por regra de tag:**

- Seu usuário não deve receber mais do que uma campanha de notificações por push por semana com a tag `promotional`.<br><br>

| Ação | Resultado |
|---|---|
| A tag `promotional` é removida da **Campanha A** após o usuário ter recebido a mensagem, mas antes do **envio da Campanha B.** | Seu usuário receberá **a Campanha B**.|
| A tag `promotional` foi removida por engano da **Campanha A** depois que seu usuário recebeu a mensagem. <br> A tag é adicionada novamente à **Campanha A** na terça-feira, antes do envio **da Campanha B**. | Seu usuário não receberá **a Campanha B**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Envio em grandes escalas {#sending-at-large-scales}

O limite de frequência por regras de tag pode não ser aplicado corretamente em grandes escalas, como 100 mensagens por canal de campanhas ou componentes do Canvas.

Por exemplo, se sua regra de limite de frequência por tag for:

> Não mais do que duas campanhas de envio de e-mail ou componentes do Canva com a tag `Promotional` para um usuário a cada semana.

Se você enviar ao usuário mais de 100 e-mails de campanhas e etapas do Canva com o limite de frequência ativado ao longo de uma semana, mais de dois e-mails poderão ser enviados ao usuário.

Como 100 mensagens por canal são mais mensagens do que a maioria das marcas envia para seus usuários, é improvável que você seja afetado por essa limitação. Para evitar essa limitação, você pode definir um limite para o número máximo de e-mails que deseja que os usuários recebam ao longo de uma semana.

Por exemplo, você pode configurar a seguinte regra:

> Não mais do que três campanhas de envio de e-mail ou componentes do Canvas por semana em todas as etapas da campanha e do Canvas.

Essa regra garantirá que nenhum usuário receba mais de 100 e-mails por semana porque, no máximo, os usuários receberão três e-mails por semana de campanhas ou componentes do Canvas com o limite de frequência ativado.

