---
nav_title: Entrega baseada em ações
article_title: Entrega baseada em ações
page_order: 1
page_type: reference
description: "Este artigo de referência descreve como acionar campanhas a serem enviadas depois que um usuário concluir um determinado evento."
tool: Campaigns

---

# Entrega baseada em ações

> Campanhas de entrega baseadas em ações ou campanhas acionadas por eventos são muito eficazes para mensagens transacionais ou baseadas em conquistas. Em vez de enviar sua campanha em determinados dias, você pode acioná-la para enviar depois que um usuário concluir um determinado evento. 

## Configuração de uma campanha acionada

### Etapa 1: Selecione um evento de acionamento

Selecione um evento de acionamento. Isso pode incluir qualquer um dos seguintes itens:
- Fazer uma compra
- Iniciar uma sessão
- Realização de um evento personalizado
- Realização do evento de conversão principal da campanha
- Adição de um endereço de e-mail a um perfil de usuário
- Alteração de um valor de atributo personalizado
- Atualização do status de uma assinatura
- Atualização do status de um grupo de assinaturas
- Interagir com outras campanhas
    - Exibir mensagem no aplicativo
    - Clique na mensagem no aplicativo
    - Clique nos botões de mensagem no aplicativo
    - Clique no e-mail
    - Clique no alias no e-mail
    - Alias clicado em qualquer campanha ou etapa do Canvas
    - Abrir e-mail
    - Abrir e-mail (abertura de máquina)
    - Abrir e-mail (outras aberturas)
    - Abrir diretamente a notificação por push
    - Clique no botão de notificação por push
    - Clique em empurrar a página da história
    - Realizar evento de conversão
    - Receber e-mail
    - Receber SMS
    - Clique no link encurtado do SMS
    - Receber notificação por push
    - Receber webhook
    - Estão inscritos no grupo de controle
    - Exibir cartão de conteúdo
    - Clique em Content Card
    - Dispensar cartão de conteúdo
- Inserção de um local
- Realização do evento de exceção para outra campanha
- Interagindo com uma etapa do Canvas
- Acionamento de uma geofence
- Envio de uma mensagem SMS de entrada
- Envio de uma mensagem de entrada do WhatsApp

Você também pode filtrar ainda mais os eventos de acionamento por meio das [propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) do Braze, permitindo propriedades de eventos personalizáveis para eventos personalizados e compras no aplicativo. Esse recurso permite personalizar ainda mais os usuários que receberão uma mensagem com base nos atributos específicos do evento personalizado, permitindo maior personalização da campanha e coleta de dados mais sofisticada. 

Por exemplo, digamos que temos uma campanha com um evento personalizado de carrinho abandonado que é direcionado ainda mais pelo filtro de propriedade "valor do carrinho". Essa campanha atingirá apenas os usuários que deixaram entre US$ 100 e US$ 200 em mercadorias em seus carrinhos. 

\![]({% image_buster /assets/img_archive/customEventProperties.png %})

{% alert note %}
O evento de disparo "iniciar sessão" pode ser a primeira abertura de aplicativo do usuário se o segmento da sua campanha se aplicar a novos usuários. (por exemplo, se seu segmento consistir naqueles sem sessões).
{% endalert %}

Lembre-se de que você ainda pode enviar uma campanha acionada para um segmento específico de usuários, de modo que os usuários que não fazem parte do segmento não receberão a campanha, mesmo que concluam o evento de acionamento. Se você perceber que os usuários não estão recebendo a campanha, embora tenham se qualificado para o segmento, consulte nossa seção sobre [por que um usuário pode não ter recebido uma campanha acionada]({{site.baseurl}}/help/help_articles/campaigns_and_canvas/not_triggering/).

Com relação ao evento de acionamento para quando um usuário adiciona um endereço de e-mail ao seu perfil, aplicam-se as seguintes regras:

- O evento de acionamento será disparado após a atualização do atributo do perfil do usuário. Isso significa que a avaliação dos segmentos e filtros da campanha ocorrerá após qualquer atualização de atributo. Isso é vantajoso porque permite que você configure filtros como "endereço de e-mail corresponde a gmail.com" para criar uma campanha de gatilho que só envia para usuários do Gmail e dispara assim que eles adicionam seu endereço de e-mail.
- O evento de acionamento será disparado quando um endereço de e-mail for adicionado a um perfil de usuário. Se você tiver vários perfis de usuário criados com o mesmo endereço de e-mail, a campanha poderá ser disparada várias vezes, uma vez para cada perfil de usuário.

Além disso, as mensagens in-app acionadas ainda obedecem às regras de entrega de mensagens in-app e aparecem no início de uma sessão do aplicativo.

\![]({% image_buster /assets/img_archive/schedule_triggered1.png %})

### Etapa 2: Selecione a duração do atraso

Selecione o tempo de espera antes de enviar a campanha depois que os critérios de acionamento forem atendidos. Se a duração do atraso escolhida for maior do que a duração do envio da mensagem, nenhum usuário receberá a campanha. 

Além disso, os usuários que concluírem o evento de acionamento após o lançamento da sua campanha serão os primeiros a começar a receber a mensagem depois que o atraso tiver passado. Os usuários que tiverem concluído o evento de acionamento antes do lançamento da campanha não se qualificarão para receber a campanha.

\![]({% image_buster /assets/img_archive/schedule_triggered22.png %})

Você também pode optar por enviar a campanha em um dia específico da semana (escolhendo "no próximo" e, em seguida, selecionando um dia) ou em um número específico de dias (selecionando "em") no futuro. Como alternativa, você pode optar por enviar sua mensagem usando o recurso [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) em vez de selecionar manualmente um horário de entrega.

\![]({% image_buster /assets/img_archive/schedule_triggered7.png %})
\![]({% image_buster /assets/img_archive/schedule_triggered8.png %})

### Etapa 3: Selecionar eventos de exceção

Selecione um evento de exceção que desqualificará os usuários para receberem essa campanha. Isso só pode ser feito se a mensagem acionada for enviada após um atraso de tempo. [Os eventos de exceção]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/#exception-events) podem ser fazer uma compra, iniciar uma sessão, realizar um dos [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events) designados de uma campanha ou realizar um evento personalizado. Se um usuário concluir o evento de acionamento, mas depois concluir o evento de exceção antes do envio da mensagem devido ao atraso, ele não receberá a campanha. Os usuários que não receberem a campanha devido ao evento de exceção estarão automaticamente qualificados para recebê-la no futuro, na próxima vez que concluírem o evento de acionamento, mesmo que você não opte por tornar os usuários [novamente elegíveis]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/).

\![]({% image_buster /assets/img_archive/schedule_triggered32.png %})

Você pode ler mais sobre como empregar eventos de exceção em nossa seção sobre [casos de uso]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#use-cases).

> Se você enviar uma campanha com um evento de acionamento que corresponda ao evento de exceção, o Braze cancelará a campanha e reagendará automaticamente uma nova campanha com base no tempo de entrega da mensagem do evento de exceção. Por exemplo, se o seu primeiro evento de acionamento começar em cinco minutos e o evento de exceção começar em 10 minutos, você consideraria os 10 minutos do evento de exceção como o tempo de entrega da mensagem da campanha oficial.

{% alert note %}
Não é possível fazer de um "início de sessão" tanto o evento de acionamento quanto o evento de exceção de uma campanha. No entanto, você sempre tem a opção de selecionar qualquer outro evento personalizado fora dessa opção.
{% endalert %}

### Etapa 4: Atribuir duração

Atribua a duração da campanha especificando uma hora de início e uma hora de término opcional.

\![]({% image_buster /assets/img_archive/schedule_triggered43.png %})

Se um usuário concluir um evento de acionamento durante o período de tempo especificado, mas se qualificar para a mensagem fora do período de tempo devido a um atraso programado, ele não receberá a campanha. Portanto, se você definir um atraso maior do que o período de tempo da mensagem, nenhum usuário receberá sua campanha. Além disso, você pode optar por enviar a mensagem nos [fusos horários locais]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/scheduled_delivery/#local-time-zone-campaigns) dos usuários.

### Etapa 5: Selecione o período de tempo

Selecione se o usuário receberá a campanha durante uma parte específica do dia. Se você der à mensagem um período de tempo e o usuário concluir o evento de acionamento fora do período de tempo ou se o atraso da mensagem fizer com que ele perca o período de tempo, então, por padrão, o usuário não receberá a mensagem.

\![]({% image_buster /assets/img_archive/schedule_triggered5.png %})

Caso um usuário conclua o evento de acionamento dentro do período de tempo, mas o atraso da mensagem faça com que o usuário saia do período de tempo, é possível marcar a caixa a seguir para que esses usuários ainda recebam a campanha.

\![]({% image_buster /assets/img_archive/schedule_triggered_next_available.png %})

Se um usuário não receber a mensagem porque perdeu o prazo, ele ainda estará qualificado para recebê-la na próxima vez que concluir o evento de acionamento, mesmo que você não tenha optado por tornar os usuários [novamente elegíveis]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/). Se você optar por tornar os usuários reelegíveis, eles poderão receber a campanha sempre que concluírem o evento de acionamento, desde que se qualifiquem durante o período de tempo especificado.

Se você também tiver atribuído à campanha uma determinada duração, o usuário deverá se qualificar dentro da duração e da parte específica do dia para receber a mensagem.

### Etapa 6: Determinar a reelegibilidade

Determine se os usuários podem se tornar [reelegíveis]({% image_buster /assets/img_archive/ReEligible.png %}) para a campanha. Se você permitir que os usuários se tornem reelegíveis, poderá especificar um atraso de tempo antes que o usuário possa receber a campanha novamente. Isso evitará que suas campanhas acionadas se tornem "spammy".

\![]({% image_buster /assets/img_archive/schedule_triggered6.png %})

## Casos de uso

As campanhas acionadas são muito eficazes para mensagens transacionais ou baseadas em conquistas.

As campanhas transacionais incluem mensagens enviadas depois que o usuário conclui uma compra ou adiciona um item ao carrinho. O último caso é um ótimo exemplo de uma campanha que se beneficiaria de um evento de exceção. Digamos que sua campanha lembre os usuários de itens no carrinho que eles não compraram. O evento de exceção, nesse caso, seria o usuário comprando os produtos em seu carrinho. Para campanhas baseadas em conquistas, você pode enviar uma mensagem 5 minutos depois que o usuário concluir uma conversão ou superar um nível de jogo.

Além disso, ao criar campanhas de boas-vindas, é possível acionar mensagens a serem enviadas depois que o usuário se registrar ou configurar uma conta. O escalonamento das mensagens a serem enviadas em dias diferentes após o registro permitirá que você crie um processo de integração completo.

## Por que um usuário não recebeu minha campanha acionada?

Qualquer uma dessas coisas impedirá que um usuário que tenha concluído o evento de acionamento receba a campanha:

- O usuário concluiu o evento de exceção antes que o tempo de atraso tivesse se esgotado completamente.
- [A lógica do`abort_message` ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages) líquido foi usada e a mensagem foi abortada com base na lógica ou nas regras do `abort_message`.
- O tempo de atraso fez com que o usuário se qualificasse para receber a campanha após o término da duração.
- O atraso fez com que o usuário se qualificasse para receber a campanha fora da parte especificada do dia.
- O usuário já recebeu a campanha, e os usuários não se tornam elegíveis novamente.
- Embora os usuários sejam reelegíveis para receber a campanha, eles só podem reativá-la após um determinado período de tempo, e esse período de tempo ainda não se esgotou.

[A segmentação de]({{site.baseurl}}/user_guide/engagement_tools/segments/) uma campanha acionada com base nos dados do usuário registrados no momento do evento pode causar uma [condição de corrida]({{site.baseurl}}/help/best_practices/race_conditions/#race-conditions). Isso acontece quando o atributo do usuário no qual a campanha é segmentada é alterado, mas a alteração não foi processada para o usuário quando a campanha é enviada. Como as campanhas verificam a associação ao segmento na entrada, isso pode fazer com que o usuário não receba a campanha.

Por exemplo, imagine que você queira enviar uma campanha acionada por evento para usuários do sexo masculino que acabaram de se registrar. Quando o usuário se registra, você grava um evento personalizado `registration` e, simultaneamente, define o atributo `gender` do usuário. O evento pode disparar a campanha antes que o Braze tenha processado o gênero do usuário, impedindo-o de receber a campanha.

Como prática recomendada, certifique-se de que o atributo no qual a campanha é segmentada seja transferido para os servidores do Braze antes do evento. Se isso não for possível, a melhor maneira de garantir a entrega é usar [propriedades de evento personalizadas]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) para anexar as propriedades relevantes do usuário ao evento e aplicar um filtro de propriedade para a propriedade específica do evento em vez de um filtro de segmentação. No nosso exemplo, você adicionaria uma propriedade `gender` ao evento personalizado `registration` para garantir que o Braze tenha os dados de que você precisa quando sua campanha for acionada.

Além disso, se uma campanha for baseada em ação e tiver um atraso, você poderá marcar a opção **Reavaliar associação de segmento no momento do envio** para garantir que os usuários ainda façam parte do público-alvo quando a mensagem for enviada.

Se a sua campanha for acionada por um evento personalizado específico e você selecionar um segmento como público-alvo, os usuários deverão executar o mesmo evento personalizado para serem incluídos no segmento. Isso significa que os usuários precisam fazer parte do público antes que uma campanha baseada em ação possa ser acionada. O fluxo de trabalho geral para uma campanha acionada é o seguinte:

1. **Junte-se ao público:** Quando um usuário realiza o evento personalizado, ele é adicionado ao público-alvo da campanha.
2. **Acionar o e-mail:** Um usuário deve executar o evento personalizado novamente para acionar o e-mail, pois ele precisa fazer parte do público-alvo para que o e-mail possa ser enviado.

Recomendamos alterar o público-alvo para incluir todos os usuários ou verificar se os usuários que devem realizar o evento já fazem parte do público da campanha para que a mensagem seja acionada.

\![]({% image_buster /assets/img_archive/reevaluate_segment_membership.png %})

### Solução de problemas de eventos personalizados

Primeiro, confirme se o evento personalizado está sendo passado para o Braze. Vá para **Analytics** > **Custom Events Report** e selecione o respectivo evento personalizado e o intervalo de datas. Se o evento não for exibido, confirme se ele foi configurado corretamente e se o usuário executou a ação correta.

Se o evento personalizado for exibido, solucione o problema da seguinte forma:

- Verifique o download do perfil do usuário para confirmar se ele acionou o evento e quando o fez. Se o evento foi acionado, compare o registro de data e hora de quando o evento foi acionado com a hora em que a campanha foi ao ar. O evento pode ter sido acionado antes de a campanha entrar no ar.
- Revise os registros de alterações da campanha e de todos os segmentos usados na segmentação para determinar se o usuário estava no segmento quando o evento personalizado foi acionado. Se eles não estivessem no segmento, não teriam recebido a campanha.
- Verifique se o usuário foi inserido em um grupo de controle por meio de segmentação e, consequentemente, impedido de receber a campanha.
- Se houver um atraso programado, verifique se o evento personalizado do usuário foi acionado antes do atraso. Se o evento fosse acionado antes do atraso, eles não teriam recebido a campanha.

{% alert note %}
As mensagens in-app só podem ser acionadas por eventos enviados pelo SDK, não pela API REST.
{% endalert %}

