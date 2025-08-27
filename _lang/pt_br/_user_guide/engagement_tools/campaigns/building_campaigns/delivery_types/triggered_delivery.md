---
nav_title: Entrega baseada em ação
article_title: Entrega baseada em ação
page_order: 1
page_type: reference
description: "Este artigo de referência descreve como disparar campanhas a serem enviadas depois que um usuário concluir um determinado evento."
tool: Campaigns

---

# Entrega baseada em ação

> As campanhas de entrega baseadas em ação ou campanhas disparadas por eventos são muito eficazes para mensagens transacionais ou baseadas em conquistas. Em vez de enviar sua campanha em determinados dias, é possível disparar o envio depois que um usuário concluir um determinado evento. 

## Configuração de uma campanha disparada

### Etapa 1: Selecione um evento de gatilho

Selecione um evento de gatilho. Isso pode incluir qualquer um dos seguintes itens:
- Fazer uma compra
- Iniciar uma sessão
- Realização de um evento personalizado
- Performar o evento de conversão primária da campanha
- Adição de um endereço de e-mail a um perfil de usuário
- Alteração de um valor de atributo personalizado
- Atualização do status de uma inscrição
- Atualização do status de um grupo de inscrições
- Interagir com outras campanhas
    - Ver mensagem no app
    - Clique na mensagem no app
    - Clique nos botões de mensagem no app
    - Clique no e-mail
    - Clique no alias no e-mail
    - Alias clicado em qualquer campanha ou etapa do Canva
    - Abrir e-mail
    - E-mail aberto (aberturas por máquina)
    - E-mail aberto (outras aberturas)
    - Abra diretamente a notificação por push
    - Clique no botão de notificação por push
    - Clique na página da story por push
    - Realizar evento de conversão
    - Receber e-mail
    - Receber SMS
    - Clique no link encurtado do SMS
    - Receba notificações por push
    - Receber webhook
    - Estão inscritos no grupo de controle
    - Exibir cartão de conteúdo
    - Clique no cartão de conteúdo
    - Descarte de cartão de conteúdo
- Inserção de um local
- Performar o evento de exceção para outra campanha
- Interagindo com uma etapa do Canva
- Como disparar um geofence
- Envio de mensagens SMS de entrada
- Envio de mensagens de entrada do WhatsApp

Você também pode filtrar ainda mais os eventos de disparo através das propriedades de evento personalizado do Braze, permitindo propriedades de evento personalizáveis para eventos personalizados e compras dentro do app. Esse recurso permite personalizar ainda mais os usuários que recebem uma mensagem com base nos atributos específicos do evento personalizado, permitindo maior personalização da campanha e coleta de dados mais sofisticada. 

Por exemplo, digamos que temos uma campanha com um evento personalizado de carrinho abandonado que é direcionado ainda mais pelo filtro de propriedade "valor do carrinho". Essa campanha atingirá apenas os usuários que deixaram entre US$ 100 e US$ 200 em mercadorias em seus carrinhos. 

![]({% image_buster /assets/img_archive/customEventProperties.png %})

{% alert note %}
O evento de gatilho "iniciar sessão" pode ser a primeira abertura de app do usuário se o segmento da sua campanha se aplicar a novos usuários. (por exemplo, se seu segmento consistir naqueles sem sessões).
{% endalert %}

Lembre-se de que ainda é possível enviar uma campanha disparada para um segmento específico de usuários, portanto, os usuários que não fazem parte do segmento não receberão a campanha, mesmo que concluam o evento de gatilho. Se você notar que os usuários não estão recebendo a campanha, mesmo tendo se qualificado para o segmento, veja nossa seção sobre por que um usuário pode não ter recebido uma campanha disparada.

Com relação ao evento de gatilho para quando um usuário adiciona um endereço de e-mail ao seu perfil, aplicam-se as seguintes regras:

- O evento de gatilho será disparado depois que o atributo do perfil do usuário for atualizado. Isso significa que a avaliação dos segmentos e filtros da campanha ocorrerá após qualquer atualização de atribuição. Isso é vantajoso porque ativa a capacitação para configurar filtros como "endereço de e-mail corresponde a gmail.com" para criar uma campanha disparada que envia apenas para usuários do Gmail e dispara assim que eles adicionam seu endereço de e-mail.
- O evento de gatilho será disparado quando um endereço de e-mail for adicionado a um perfil de usuário. Se você tiver vários perfis de usuário criados com o mesmo endereço de e-mail, a campanha poderá ser disparada várias vezes, uma vez para cada perfil de usuário.

Além disso, as mensagens no app disparadas ainda obedecem às regras de entrega de mensagens no app e aparecem no início de uma sessão do aplicativo.

![]({% image_buster /assets/img_archive/schedule_triggered1.png %})

### Etapa 2: Selecione a duração da postergação

Selecione o tempo de espera antes de enviar a campanha depois que os critérios do disparo forem atendidos. Se a duração da postergação escolhida for maior do que a duração do envio da mensagem, nenhum usuário receberá a campanha. 

Além disso, os usuários que concluírem o evento de gatilho após o lançamento da campanha serão os primeiros a começar a receber a mensagem após o término da postergação. Os usuários que tiverem concluído o evento de gatilho antes do lançamento da campanha não se qualificarão para receber a campanha.

![]({% image_buster /assets/img_archive/schedule_triggered22.png %})

Você também pode optar por enviar a campanha em um dia específico da semana (escolhendo "no próximo" e, em seguida, selecionando um dia) ou em um número específico de dias (selecionando "em") no futuro. Como alternativa, você pode optar por enviar sua mensagem usando o recurso [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) em vez de selecionar manualmente um horário de entrega.

![]({% image_buster /assets/img_archive/schedule_triggered7.png %})
![]({% image_buster /assets/img_archive/schedule_triggered8.png %})

### Etapa 3: Selecionar eventos de exceção

Selecione um evento de exceção que desqualificará os usuários para receberem essa campanha. Isso só pode ser feito se a mensagem disparada for enviada após uma postergação. Eventos de exceção podem ser fazer uma compra, iniciar uma sessão, realizar um dos eventos de conversão designados de uma campanha, ou realizar um evento personalizado. Se um usuário concluir o evento de gatilho, mas depois concluir o evento de exceção antes do envio das mensagens devido à postergação, ele não receberá a campanha. Os usuários que não receberem a campanha devido ao evento de exceção serão automaticamente elegíveis para recebê-la no futuro, na próxima vez que concluírem o evento de gatilho, mesmo que você não opte por tornar os usuários [novamente elegíveis]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/).

![]({% image_buster /assets/img_archive/schedule_triggered32.png %})

Você pode ler mais sobre como empregar eventos de exceção em nossa seção sobre [casos de uso]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#use-cases).

> Se você enviar uma campanha com um evento de disparo que corresponda ao evento de exceção, o Braze cancelará a campanha e reagendará automaticamente uma nova campanha com base no tempo de entrega da mensagem do evento de exceção. Por exemplo, se o seu primeiro evento de gatilho começar em cinco minutos e o evento de exceção começar em 10 minutos, você consideraria os 10 minutos do evento de exceção como o tempo de envio de mensagens da campanha oficial.

{% alert note %}
Não é possível fazer de um "início de sessão" tanto o evento de gatilho quanto o evento de exceção de uma campanha. No entanto, você sempre tem a opção de selecionar qualquer outro evento personalizado fora dessa opção.
{% endalert %}

### Etapa 4: Atribuir duração

Atribua a duração da campanha especificando uma hora de início e uma hora de término opcional.

![]({% image_buster /assets/img_archive/schedule_triggered43.png %})

Se um usuário concluir um evento de gatilho durante o período de tempo especificado, mas se qualificar para a mensagem fora do período de tempo devido a uma postergação programada, ele não receberá a campanha. Portanto, se você definir uma postergação maior do que o período de tempo da mensagem, nenhum usuário receberá sua campanha. Além disso, é possível optar por enviar a mensagem nos [fusos locais dos usuários]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/scheduled_delivery/#local-time-zone-campaigns).

### Etapa 5: Selecione o período

Selecione se o usuário receberá a campanha durante uma parte específica do dia. Se você der à mensagem um período de tempo e o usuário concluir o evento de gatilho fora do período de tempo ou se a postergação da mensagem fizer com que ele perca o período de tempo, então, por padrão, o usuário não receberá sua mensagem.

![]({% image_buster /assets/img_archive/schedule_triggered5.png %})

No caso de um usuário concluir o evento de gatilho dentro do período de tempo, mas a postergação da mensagem fizer com que o usuário saia do período de tempo, é possível marcar a caixa a seguir para que esses usuários ainda recebam a campanha.

![]({% image_buster /assets/img_archive/schedule_triggered_next_available.png %})

Se um usuário não receber a mensagem porque perdeu o prazo, ele ainda estará qualificado para recebê-la na próxima vez que concluir o evento de gatilho, mesmo que você não tenha optado por tornar os usuários [novamente elegíveis]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/). Se optar pela reelegibilidade dos usuários, eles poderão receber a campanha sempre que concluírem o evento de gatilho, desde que se qualifiquem durante o período de tempo especificado.

Se também tiver atribuído à campanha uma determinada duração, o usuário deverá se qualificar tanto na duração quanto na parte específica do dia para receber a mensagem.

### Etapa 6: Determinar a reelegibilidade

Determine se os usuários podem se tornar [novamente elegíveis]({% image_buster /assets/img_archive/ReEligible.png %}) para a campanha. Se você permitir que os usuários se tornem novamente elegíveis, poderá especificar uma postergação de tempo antes que o usuário possa receber a campanha novamente. Isso evitará que suas campanhas disparadas se tornem "spam".

![]({% image_buster /assets/img_archive/schedule_triggered6.png %})

## Casos de uso

As campanhas de mensagens disparadas são muito eficazes para mensagens transacionais ou baseadas em conquistas.

As campanhas de mensagens transacionais incluem mensagens enviadas depois que o usuário conclui uma compra ou adiciona um item ao carrinho. O último caso é um ótimo exemplo de uma campanha que se beneficiaria de um evento de exceção. Digamos que sua campanha lembre os usuários de itens no carrinho que eles não compraram. O evento de exceção, nesse caso, seria o usuário comprando os produtos em seu carrinho. Para campanhas baseadas em conquistas, é possível enviar uma mensagem 5 minutos depois que o usuário concluir uma conversão ou superar um nível de jogo.

Além disso, ao criar campanhas de mensagens de boas-vindas, é possível disparar mensagens a serem enviadas depois que o usuário se registrar ou configurar uma conta. O envio de mensagens em dias diferentes após o registro permitirá que você crie um processo de integração completo.

## Por que um usuário não recebeu minha campanha disparada?

Qualquer uma dessas coisas impedirá que um usuário que tenha concluído o evento de gatilho receba a campanha:

- O usuário concluiu o evento de exceção antes que a postergação tivesse se esgotado completamente.
- [A lógica do`abort_message` ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages) foi usada e a mensagem foi abortada com base na lógica ou nas regras do `abort_message`.
- A postergação fez com que o usuário se tornasse qualificado para receber a campanha após o término da duração.
- A postergação fez com que o usuário se qualificasse para receber a campanha fora da parte especificada do dia.
- O usuário já recebeu a campanha, e os usuários não se tornam elegíveis novamente.
- Embora os usuários sejam elegíveis novamente para receber a campanha, eles só podem dispará-la novamente após um determinado período de tempo, e esse período de tempo ainda não passou.

[A segmentação de]({{site.baseurl}}/user_guide/engagement_tools/segments/) uma campanha disparada com base nos dados de usuários registrados no momento do evento pode causar uma [condição de corrida]({{site.baseurl}}/help/best_practices/race_conditions/#race-conditions). Isso acontece quando a atribuição do usuário na qual a campanha é segmentada é alterada, mas a alteração não foi processada para o usuário quando a campanha é enviada. Como as campanhas verificam a associação ao segmento na entrada, isso pode fazer com que o usuário não receba a campanha.

Por exemplo, imagine que você queira enviar uma campanha disparada por evento para usuários do sexo masculino que acabaram de se registrar. Quando o usuário se registra, você grava um evento personalizado `registration` e, simultaneamente, define o atributo `gender` do usuário. O evento pode disparar a campanha antes que o Braze tenha processado o gênero do usuário, impedindo-o de receber a campanha.

Como prática recomendada, certifique-se de que a atribuição na qual a campanha é segmentada seja liberada para os servidores do Braze antes do evento. Se isso não for possível, a melhor maneira de garantir a entrega é usar as propriedades de evento personalizado para anexar as propriedades relevantes do usuário ao evento e aplicar um filtro de propriedade para a propriedade de evento específica em vez de um filtro de segmentação. No nosso exemplo, você adicionaria uma propriedade `gender` ao evento personalizado `registration` para garantir que o Braze tenha os dados de que você precisa quando sua campanha for disparada.

Além disso, se uma campanha for baseada em ação e tiver uma postergação, é possível marcar a opção **Reavaliar associação de segmento no momento do envio** para garantir que os usuários ainda façam parte do público-alvo quando a mensagem for enviada.

Se a sua campanha for disparada por um evento personalizado específico e você selecionar um segmento como público, os usuários deverão realizar o mesmo evento personalizado para serem incluídos no segmento. Isso significa que os usuários precisam fazer parte do público antes que uma campanha baseada em ação possa ser disparada. O fluxo de trabalho geral de uma campanha disparada é o seguinte:

1. **Participe do público:** Quando um usuário realiza o evento personalizado, ele é adicionado ao público-alvo da campanha.
2. **Disparar o e-mail:** Um usuário deve executar o evento personalizado novamente para disparar o e-mail, pois ele precisa fazer parte do público para que o e-mail possa ser enviado.

Recomendamos alterar o público-alvo para incluir todos os usuários ou verificar se os usuários que deverão realizar o evento já fazem parte do público da campanha para que a mensagem seja disparada.

![]({% image_buster /assets/img_archive/reevaluate_segment_membership.png %})

### Solução de problemas de eventos personalizados

Primeiro, confirme se o evento personalizado está sendo enviado para o Braze. Acesse Análise > Relatório de Eventos Personalizados, e então selecione o respectivo evento personalizado e intervalo de datas. Se o evento não for exibido, confirme se está configurado corretamente e se o usuário realizou a ação correta.

Se o evento personalizado for exibido, faça mais verificações fazendo o seguinte:

- Verifique o download do perfil do usuário para confirmar se eles dispararam o evento e quando o fizeram. Se o evento foi disparado, compare o timestamp de quando o evento foi disparado com o momento em que a campanha foi ao ar. O evento pode ter sido disparado antes da campanha ir ao ar.
- Revise os logs de alterações da campanha e quaisquer segmentos usados no direcionamento para determinar se o usuário estava no segmento quando seu evento personalizado foi disparado. Se eles não estavam no segmento, não teriam recebido a campanha.
- Verifique se o usuário foi inserido em um grupo de controle através da segmentação e, consequentemente, impedido de receber a campanha.
- Se houver um atraso programado, verifique se o evento personalizado do usuário foi disparado antes do atraso. Se o evento foi disparado antes do atraso, eles não teriam recebido a campanha.

{% alert note %}
Mensagens dentro do app só podem ser disparadas por eventos enviados através do SDK, não pela API REST.
{% endalert %}

