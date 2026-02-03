---
nav_title: Limite de taxa e limite de frequência
article_title: Limite de frequência e limitação de frequência
page_order: 6
tool: Campaigns
page_type: reference
description: "Este artigo de referência discute o conceito de limite de taxa e limite de frequência em campanhas e como é possível gerenciar a pressão de marketing para melhorar a experiência do usuário."

---

# Limite de taxa e limite de frequência

> A limitação de taxa e o controle de frequência podem ser usados juntos para garantir que seus usuários recebam as mensagens de que precisam.

## Sobre o limite de frequência

O Braze permite que você controle a pressão do marketing limitando a frequência de suas campanhas, regulando a quantidade de tráfego de saída de sua plataforma. Você pode implementar dois tipos diferentes de limites de frequência para suas campanhas: 

1. [**Limite de frequência centrado no usuário:**](#user-centric-rate-limiting) Concentra-se em fornecer a melhor experiência para o usuário.
2. [**Limite de frequência da velocidade de entrega:**](#delivery-speed-rate-limiting) Leva em consideração a largura de banda de seus servidores.

A Braze tentará distribuir uniformemente o envio de mensagens ao longo do minuto, mas não pode garantir isso. Por exemplo, se você tiver uma campanha com um limite de taxa de 5.000 mensagens por minuto, tentaremos distribuir os 5.000 pedidos uniformemente ao longo do minuto (cerca de 84 mensagens por segundo), mas pode haver alguma variação na taxa por segundo.

### Limite de frequência centrado no usuário

À medida que você cria mais segmentos, haverá casos em que a associação desses segmentos se sobrepõe. Se estiver enviando campanhas para esses segmentos, queira mesmo ter certeza de que não está enviando mensagens com muita frequência para seus usuários. Se um usuário receber muitas mensagens em um curto período de tempo, ele se sentirá sobrecarregado e desativará as notificações por push ou desinstalará o app.

#### Filtros de segmentos relevantes

A Braze fornece os seguintes filtros para ajudar a limitar a taxa com que seus usuários recebem mensagens:

- Última interação com mensagem
- Último recebimento de qualquer mensagem
- Último push recebido
- Último recebimento de e-mail
- Último SMS recebido

#### Implementação de filtros

Vamos supor que criamos um segmento chamado "Demonstração de Filtro de Redirecionamento" com um filtro "Último app usado há mais de 7 dias" para segmentar usuários. Esse seria um segmento de reengajamento padrão.

Se você tiver outros segmentos mais direcionados recebendo notificações recentemente, pode não querer que seus usuários sejam segmentados por campanhas mais genéricas direcionadas a esse segmento. Ao adicionar o filtro "Último Push Recebido" a esse segmento, o usuário garantiu que, se tiver recebido outra notificação nas últimas 24 horas, ele sairá desse segmento pelas próximas 24 horas. Se eles ainda atenderem aos outros critérios do segmento 24 horas depois e não tiverem recebido mais notificações, eles voltarão ao segmento.

![Um segmento chamado "Demonstração de Filtro de Redirecionamento" com o grupo de filtros "Último app usado há mais de 7 dias".]({% image_buster /assets/img_archive/rate_limit_daily.png %}){: style="max-width:80%;"} 

Anexar esse filtro a todos os segmentos direcionados por campanhas faria com que seus usuários recebessem no máximo um push a cada 24 horas. Assim, é possível priorizar o envio de mensagens, garantindo que as mais importantes sejam entregues antes das menos importantes.

#### Definição de um limite máximo de usuários

Na etapa **Públicos Alvo** do seu criador de campanha, você também pode limitar o número total de usuários que receberão sua mensagem. Isso serve como uma verificação que é independente dos filtros da sua campanha.

![Resumo do Público com uma caixa de seleção selecionada para limitar o número de pessoas que recebem a campanha.]({% image_buster /assets/img_archive/total_limit.png %}){: style="max-width:50%;"} 

Ao selecionar o limite máximo de usuários, você pode limitar o volume de mensagens enviadas por canal ou globalmente em todos os tipos de mensagens.

##### Limite máximo de usuários com otimizações

Se estiver usando uma otimização como Winning Variant ou Personalized Variant, a campanha consistirá em dois envios: o experimento inicial e o envio final. 

Para configurar um limite máximo de usuários nesse cenário, selecione **Limitar o número de pessoas que receberão esta campanha** e, em seguida, selecione **No total, esta campanha deve** e insira um limite de público. Seu limite de público será dividido de acordo com as porcentagens mostradas no painel **Testes A/B**. 

Se você selecionar **Sempre que a campanha for programada**, essas duas fases serão limitadas separadamente ao número definido. Normalmente, isso não é desejável.

#### Definindo um limite máximo de impressões em campanhas

Para mensagens no app, você pode controlar a pressão de marketing definindo um número máximo de impressões que serão exibidas para sua base de usuários, após o qual a Braze não enviará mais mensagens para seus usuários. No entanto, é importante notar que esse limite não é exato. 

As regras de mensagens no app são enviadas para um app no início da sessão, o que significa que a Braze pode enviar uma mensagem ao usuário antes que o limite seja atingido, mas, quando o usuário aciona a mensagem, o limite já foi atingido. Nessa situação, o dispositivo ainda exibirá a mensagem.

Por exemplo, digamos que você tenha um jogo com uma mensagem no app que dispara quando o usuário passa de um nível e você limita essa mensagem a 100 impressões. Até o momento, foram registradas 99 impressões. Alice e Bob abrem o jogo, e a Braze informa seus dispositivos que eles são elegíveis para receber a mensagem quando eles completam um nível. Alice vence um nível primeiro e recebe a mensagem. Bob completa o nível a seguir, mas como seu dispositivo não se comunicou com os servidores da Braze desde que sua sessão começou, seu dispositivo não está ciente de que a mensagem atingiu seu limite, e ele também recebe a mensagem. No entanto, quando um limite de impressões é atingido, na próxima vez que qualquer dispositivo solicitar a lista de mensagens no app elegíveis, o sistema não envia essa mensagem e remove a mensagem daquele dispositivo.

### Limite de frequência e Testes A/B

Ao usar o limite de frequência com um Testes A/B, o limite de frequência não é aplicado ao grupo de controle da mesma forma que o grupo de teste, o que é uma fonte potencial de viés de tempo. Para evitar esse viés, use janelas de conversão adequadas.

### Limite de frequência da velocidade de entrega

Se você antecipar grandes campanhas gerando um aumento na atividade do usuário e sobrecarregando seus servidores, pode especificar um limite de taxa por minuto para o envio de mensagens, o que significa que a Braze não envia mais do que sua configuração de limite de taxa dentro de um minuto.

Ao direcionar os usuários durante a criação da campanha, é possível navegar até **Públicos-alvo** (para campanhas) ou **Configurações de envio** (para o Canva) para selecionar um limite de frequência (em vários incrementos, de 10 a 500.000 mensagens por minuto).

Observe que as campanhas sem limite de frequência podem exceder esses limites de entrega. No entanto, esteja ciente de que as mensagens serão abortadas se sofrerem uma postergação de 72 horas ou mais devido a um limite de frequência baixo. Se o limite de frequência for muito baixo, o criador da campanha receberá alertas no dashboard e por e-mail.

#### Exemplo

Se você está tentando enviar 75.000 mensagens com um limite de 10.000 por minuto, a entrega será distribuída ao longo de oito minutos. Sua campanha enviará não mais do que 10.000 mensagens em cada um dos primeiros sete minutos e 5.000 no último minuto.

#### Número de envios

Observe que as mensagens com limite de frequência podem não ser enviadas uniformemente ao longo de cada minuto. Usando o exemplo de um limite de frequência de 10.000 por minuto, isso significa que o Braze garante que não sejam enviadas mais de 10.000 mensagens por minuto. Isso pode significar que uma porcentagem maior das 10.000 mensagens é enviada no primeiro meio minuto em comparação com o último meio minuto.

O limite de frequência é aplicado no início da tentativa de envio da mensagem. Quando há flutuações no tempo que leva para a entrega ser concluída, o número de envios concluídos pode ligeiramente exceder o limite de frequência por alguns minutos. Com o passar do tempo, o número de envios por minuto atingirá a média de não mais do que o limite de frequência.

{% alert important %}
Cuidado ao atrasar mensagens sensíveis ao tempo com essa forma de limitação de frequência em relação ao número total de usuários em um segmento. Por exemplo, se o segmento contém 30 milhões de usuários, mas definimos o limite de frequência para 10.000 por minuto, uma grande parte da sua base de usuários não receberá a mensagem até o dia seguinte.
{% endalert %}

#### Campanhas multicanal e Canvases

Ao definir um limite de velocidade de entrega para uma campanha multicanal ou Canvas, você pode optar por definir um limite de frequência compartilhado ou um limite baseado em canal.

Quando uma campanha multicanal ou Canvas usa um limite de frequência compartilhado, isso significa que o número total de mensagens enviadas por minuto da campanha ou Canvas não excede o limite de frequência. Por exemplo, se seu Canvas tem um limite de 500.000 por minuto e contém etapas de mensagens de e-mail e SMS, a Braze envia um total de 500.000 mensagens por minuto entre e-mail e SMS.

![A opção de limitar a taxa na qual a campanha envia, selecionada com 500.000 mensagens por minuto.]({% image_buster /assets/img_archive/multichannel_campaigns_rate_limit.png %}){: style="max-width:50%;"} 

Quando uma campanha multicanal ou Canvas usa limitação de frequência baseada em canal, o limite de frequência se aplicará a cada um dos canais selecionados. Por exemplo, você pode definir sua campanha ou Canvas para enviar um máximo de 5.000 webhooks e 2.500 mensagens SMS por minuto na campanha ou Canvas.

![Limites de frequência separados para dois canais, webhook e SMS/MMS/RCS, com 5.000 e 2.500 mensagens por minuto, respectivamente.]({% image_buster /assets/img_archive/channel_rate_limits.png %}){: style="max-width:70%;"}

##### Notificações por push

Para campanhas ou Canvases com plataformas de push (como Android, iOS, Web Push ou Kindle), você pode selecionar **Notificações por push** para impor um limite de frequência que é compartilhado entre todas as plataformas de push em sua campanha ou Canvas.

![O menu suspenso de canais com opções para plataformas de push e notificações por push.]({% image_buster /assets/img_archive/push_notifications_rate_limit.png %}){: style="max-width:30%;"} 

{% alert note %}
Se você selecionar um limite para notificações por push, não poderá definir limites de frequência individuais para canais de push. Da mesma forma, se você selecionar limites para canais de push individuais, não poderá definir limites de notificações por push compartilhados.
{% endalert %}

{% alert important %}
**Atualizações na interface de limitação de frequência**<br>
A Braze atualizou a interface de limitação de frequência para fornecer mais transparência e controle sobre como os limites de frequência se aplicam a campanhas multicanal e Canvases.<br><br>

- **Campanhas e Canvases existentes:** Todas as campanhas e Canvases existentes foram migrados para esta interface. O comportamento de entrega permanece o mesmo. O dashboard exibe se a campanha usa lógica compartilhada ou por canal.<br>
- **Novas campanhas e Canvases:** Para todas as novas campanhas e Canvases, há um controle manual para escolher sua lógica de limite de frequência preferida. Certifique-se de selecionar o comportamento de limitação de frequência que se alinha ao seu comportamento pretendido ao definir ou atualizar um limite de frequência de campanha ou Canvas.
{% endalert %}

##### Considerações sobre limitação de frequência

Algumas notas a serem lembradas ao configurar limites de frequência e qual comportamento você deve esperar:

- Envios de SMS estão sujeitos a um limite de frequência de 50.000 por grupo de inscrições. Alguns provedores de SMS podem impor outros limites.
- As seguintes mensagens não serão limitadas ou contadas para o limite de frequência:
    - Envios de teste
    - Grupos de sementes
    - Cartões de Conteúdo configurados para criar "na primeira impressão" (Isso será controlado pela taxa de impressões do app. Consulte [Criação de Cartão]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences) para mais informações sobre as diferenças entre as opções de Criação de Cartão.)
- Limites de velocidade de taxa de entrega não são suportados para os seguintes:
    - Respostas automáticas de SMS
    - Mensagens com SLA (como [e-mail de transação]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign))
    - Mensagem no app
    - Feature Flag
    - Banners

#### Limite de frequência e novas tentativas do Connected Content

Quando o [Tentativa de Conteúdo Conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries/) está ativado, a Braze tentará novamente falhas de chamada respeitando o limite de frequência que você definiu para cada reenvio. Vamos considerar o cenário de enviar 75.000 mensagens com um limite de 10.000 por minuto. Imagine que no primeiro minuto, a chamada falha ou é lenta e envia apenas 4.000 mensagens.

Em vez de tentar compensar a postergação e enviar as 6.000 mensagens restantes no segundo minuto ou adicioná-las às 10.000 que já estão programadas para envio, a Braze moverá essas 6.000 mensagens para o "final da fila" e adicionará um minuto, se necessário, ao total de minutos que levaria para enviar sua mensagem.

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

As solicitações de Conteúdo Conectado não têm limite de frequência de forma independente e seguirão o limite de frequência do webhook. Isso significa que se houver uma chamada de Conteúdo Conectado para um endpoint único por webhook, você esperaria 5.000 webhooks e também 5.000 chamadas de Conteúdo Conectado por minuto. Note que o cache pode afetar isso e reduzir o número de chamadas de Conteúdo Conectado. Além disso, as tentativas podem aumentar as chamadas de Conteúdo Conectado, então recomendamos verificar se o endpoint de Conteúdo Conectado pode lidar com alguma flutuação aqui.

## Sobre o limite de frequência

À medida que sua base de usuários continua a crescer e seu envio de mensagens é ampliado para incluir campanhas de ciclo de vida, disparadas, transacionais e de conversão, é importante evitar que suas notificações pareçam "spam" ou perturbadoras. Ao proporcionar maior controle sobre a experiência dos usuários, a capacitação de frequência ativa a criação das campanhas desejadas sem sobrecarregar o público.

### Visão geral dos recursos {#freq-cap-feat-over}

O limite de frequência é aplicado no nível de envio da campanha ou do componente do Canva e pode ser configurado para cada espaço de trabalho em **Configurações** > **Regras de limite de frequência**.

Por padrão, o limite de frequência é ativado quando novas campanhas são criadas. A partir daí, você pode escolher o seguinte:

- O canal de envio de mensagens que você gostaria de limitar: push, e-mail, SMS, webhook, WhatsApp, LINE ou qualquer um desses canais.
- Quantas vezes cada usuário deve receber uma campanha ou componente do Canvas enviado de um canal dentro de um determinado período de tempo.
- Quantas vezes cada usuário deve receber uma campanha ou componente do Canvas enviado por [tag](#frequency-capping-by-tag) dentro de um determinado período de tempo.

Esse período de tempo pode ser medido em minutos, dias ou semanas (sete dias), com uma duração máxima de 30 dias.

Cada linha de limites de frequência é conectada usando o operador `AND`, e você pode adicionar até 10 regras por espaço de trabalho. Você pode incluir múltiplos limites para os mesmos tipos de mensagens. Por exemplo, você pode limitar os usuários a não mais do que um push por dia e a não mais do que três pushs por semana. Note que mensagens abortadas não contam para o limite de frequência.

![Seção de limites de frequência com listas de campanhas e Canvases às quais as regras se aplicarão e não se aplicarão.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %}){: style="max-width:90%;"} 

#### Comportamento quando os usuários estão com limite de frequência em uma etapa do Canvas

Se um usuário do Canvas estiver com limite de frequência devido às configurações globais de limite de frequência, então o usuário avançará imediatamente para a próxima etapa do Canvas. O usuário não sairá do Canvas por causa do limite de frequência.

### Regras de entrega

Pode haver algumas campanhas, como mensagens transacionais, que você deseja que sempre cheguem ao usuário, mesmo que ele já tenha atingido seu limite de frequência. Por exemplo, um aplicativo de entrega pode desejar enviar um e-mail ou push quando um item é entregue, independentemente de quantas campanhas o usuário recebeu.

Se quiser que uma campanha específica substitua as regras de limite de frequência, você poderá configurar isso no dashboard do Braze ao programar a entrega dessa campanha, alternando **o limite de frequência** para **OFF**. 

Depois disso, você será perguntado se ainda deseja que essa campanha conte para o seu limite de frequência. As mensagens que contam para o limite de frequência são incluídas nos cálculos do filtro do Canal inteligente. 

Ao enviar [campanhas de API]({{site.baseurl}}/developer_guide/rest_api/messaging/#messaging), que muitas vezes são transacionais, você terá a capacidade de especificar que uma campanha deve ignorar as regras de limite de frequência definindo `override_frequency_capping` para `true` na solicitação da API.

Por padrão, as novas campanhas e canvas que não obedecerem aos limites de frequência também não contarão para eles. Isso é configurável para cada campanha e Canva.

{% alert note %}
Esse comportamento altera o comportamento padrão quando você desativa o limite de frequência para uma campanha ou uma tela. As alterações são compatíveis com versões anteriores e não afetam as mensagens que estão ativas no momento.
{% endalert %}

![Seção de Controles de Entrega com Limite de Frequência ativado.]({% image_buster /assets/img_archive/frequencycappingupdate.png %}){: style="max-width:90%;"} 

Canais diferentes dentro de uma campanha multicanal contam individualmente para o limite de frequência. Por exemplo, se você criar uma campanha multicanal com push e e-mail e tiver o limite de frequência configurado para ambos os canais, então o push conta como uma campanha de push, e a mensagem de e-mail conta como uma campanha de mensagem de e-mail. A campanha também conta como uma "campanha de qualquer tipo." Se os usuários estão limitados a uma campanha de push e uma campanha de e-mail por dia, e um usuário recebe esta campanha multicanal, então eles não estão mais elegíveis para campanhas de push ou e-mail pelo resto do dia (a menos que uma campanha ignore as regras de limite de frequência).

As mensagens no app e os cartões de conteúdo não são contados como ou para os limites de campanhas ou componentes do Canvas de qualquer tipo.

{% alert important %}
O limite de frequência global é programado com base no fuso horário do usuário e é calculado por dias do calendário, não por períodos de 24 horas. Por exemplo, se você configurar uma regra de limite de frequência de envio de no máximo uma campanha por dia, um usuário poderá receber uma mensagem às 23h em seu fuso local e será elegível para receber outra mensagem uma hora depois.
{% endalert %}

#### Casos de uso

{% tabs %}
{% tab Use case 1 %}

Vamos supor que você defina uma regra de limite de frequência para que seus usuários recebam no máximo três campanhas de notificação por push ou etapas do Canvas por semana de todas as campanhas ou etapas do Canvas.

Se o seu usuário estiver programado para receber três notificações por push, duas mensagens no app e um cartão de conteúdo nesta semana, ele receberá todas essas mensagens.

{% endtab %}
{% tab Use case 2 %}

Este cenário usa uma regra de limite de frequência para que os usuários recebam no máximo duas campanhas de notificação por push ou etapas do Canvas por semana de todas as campanhas ou etapas do Canvas.

**Quando o seguinte cenário ocorre:**

- Um usuário aciona a mesma campanha `Campaign ABC` três vezes ao longo de uma semana.
- Esse usuário dispara `Campaign ABC` uma vez na segunda-feira, uma vez na quarta-feira e uma vez na quinta-feira.

![Seção de Limite de Frequência com a regra de enviar no máximo 2 campanhas de notificação por push/etapas do Canvas de todas as campanhas/etapas do Canvas para um usuário a cada 1 semana.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Então, o comportamento esperado é esse:**

- Esse usuário receberá os envios da campanha que foram disparados na segunda e na quarta-feira.
- Esse usuário não receberá o terceiro envio de campanha na quinta-feira porque já recebeu dois envios de campanha push naquela semana.

{% endtab %}
{% endtabs %}

### Limite de frequência por tag

[As regras de limite de frequência](#delivery-rules) podem ser aplicadas aos espaços de trabalho usando tags específicas que você aplicou às suas campanhas e Canvas, permitindo que você baseie essencialmente o limite de frequência em grupos com nomes personalizados.

Com o limite de frequência por tag, as regras podem ser definidas nas tags principais e aninhadas, de modo que o Braze levará em conta todas as tags. Por exemplo, se você selecionou usar a tag principal A como o limite de frequência, também incluiremos informações em todas as tags aninhadas (por exemplo, tags B e C) ao determinar o limite.

Você também pode combinar o limite de frequência regular com o limite de frequência por tags. Considere as seguintes regras:

1. Não mais do que três campanhas de notificação por push ou componentes do Canvas por semana de todas as campanhas e etapas do Canvas. <br>**E**
2. Não mais do que duas campanhas de notificação por push ou componentes do Canvas por semana com a tag `promotional`.

![Seção Frequency Capping (Limite de frequência) com duas regras que limitam quantas campanhas/canvas de notificação por push podem ser enviadas a um usuário a cada 1 semana.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

Como resultado, seus usuários não receberão mais do que três envios de campanha por semana em todas as campanhas e etapas do Canva e não mais do que duas campanhas de notificação por push ou componentes do Canvas com a tag `promotional`.

{% alert important %}
Os canvas são marcados no nível dos canvas, em vez de serem marcados por componente. Assim, cada componente do Canvas herdará todas as tags de nível Canvas.
{% endalert %}

#### Regras conflitantes

Quando as regras entram em conflito, a regra de limite de frequência mais restritiva e aplicável é aplicada aos seus usuários. Por exemplo, digamos que você tenha as seguintes regras:

1. Não mais do que uma campanha de notificação por push ou componente do Canvas por semana de todas as campanhas e componentes do Canvas. <br>**E**
2. Não mais do que três campanhas de notificação por push ou componentes do Canvas por semana com a tag `promotional`.

![Seção de limite de frequência com regras conflitantes para limitar quantas campanhas de notificação por push/etapas do canva são enviadas a um usuário a cada 1 semana.]({% image_buster /assets/img/global_rules.png %} "global rules")

Neste exemplo, seu usuário não receberá mais de uma campanha de notificação por push ou componentes do Canvas com a tag "promocional" em uma determinada semana, porque você especificou que os usuários não devem receber mais de uma campanha de notificação por push ou componente do Canvas de todas as campanhas e componentes do Canvas. Em outras palavras, a regra de frequência aplicável mais restritiva é a regra que será aplicada a um determinado usuário.

#### Contagem de tags

O limite de frequência por regras de tag é calculado no momento em que uma mensagem é enviada. Isso significa que o limite de frequência por tag só conta as tags que estão atualmente nas campanhas ou Canvas que um usuário recebeu no passado. Não conta as tags que estavam nas campanhas ou Canvases durante o tempo em que foram enviadas, mas que desde então foram removidas. Conta se uma tag for adicionada posteriormente a uma mensagem que um usuário recebeu no passado, mas antes da nova mensagem marcada ser enviada.

##### Caso de uso

Considere as seguintes campanhas e o limite de frequência por regra de tag:

**Campanhas**:

- **A campanha A** é uma campanha push com a tag `promotional`. Está programado para ser enviado às 9h na segunda-feira.
- **A campanha B** é uma campanha push com a tag `promotional`. Está programado para ser enviado às 9h na quarta-feira.

**Limite de frequência por regra de tag:**

- Seu usuário não deve receber mais do que uma campanha de notificações por push por semana com a tag `promotional`.<br><br>

| Ação | Resultado |
|---|---|
| A tag `promotional` é removida da **Campanha A** após o usuário ter recebido a mensagem, mas antes do **envio da Campanha B.** | Seu usuário recebe **Campanha B**.|
| A tag `promotional` foi removida por engano da **Campanha A** depois que seu usuário recebeu a mensagem. <br> A tag é adicionada novamente à **Campanha A** na terça-feira, antes do envio **da Campanha B**. | Seu usuário não recebe **Campanha B**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Envio em grandes escalas {#sending-at-large-scales}

O limite de frequência por regras de tag pode não ser aplicado corretamente em grandes escalas, como 100 mensagens por canal de campanhas ou componentes do Canvas.

Por exemplo, se sua regra de limite de frequência por tag for:

> Não mais do que duas campanhas de envio de e-mail ou componentes do Canva com a tag `Promotional` para um usuário a cada semana.

Se você enviar ao usuário mais de 100 e-mails de campanhas e etapas do Canva com o limite de frequência ativado ao longo de uma semana, mais de dois e-mails poderão ser enviados ao usuário.

Como 100 mensagens por canal são mais mensagens do que a maioria das marcas envia para seus usuários, é improvável que seja impactado por essa limitação. Para evitar essa limitação, você pode definir um limite para o número máximo de e-mails que deseja que os usuários recebam ao longo de uma semana.

Por exemplo, você pode configurar a seguinte regra:

> Não mais do que três campanhas de e-mail ou componentes de canva por semana de todas as campanhas e etapas de canva.

Esta regra determina que nenhum usuário receba mais de 100 e-mails por semana porque, no máximo, os usuários recebem três e-mails por semana de campanhas ou componentes de canva com limitação de frequência ativada.

