---
nav_title: Lista de verificação pré e pós-lançamento
article_title: Lista de verificação pré e pós-lançamento
page_order: 2
description: "Este artigo fornece uma diretriz sobre o que deve ser verificado antes e depois de lançar um Canvas."
tool: Canvas

---

# Lista de verificação pré e pós-lançamento

> Este artigo fornece uma diretriz sobre o que deve ser verificado antes e depois de lançar um Canvas.

## Coisas a considerar antes do lançamento

Antes de lançar um Canvas, há vários detalhes que você pode verificar para garantir que suas mensagens e horários de envio estejam alinhados com as preferências do seu público. Os itens a serem considerados incluem variações nos fusos horários, configurações de entrada e outros. Usando essa lista de verificação como guia, ajuste essas áreas com base no seu caso de uso para ajudar a contribuir para o sucesso do seu Canvas. 

### Revisar as configurações de fuso horário

Se você estiver inserindo usuários de acordo com o fuso horário local usando uma programação de entrada agendada, deverá iniciar o Canvas pelo menos 24 horas antes da data em que deseja que os usuários entrem no Canvas. Por exemplo, aqui está um Canvas que não deixou tempo suficiente entre o lançamento e o horário de entrada programado. Nesse cenário, pode haver alguns usuários que não entrarão no seu Canvas, pois o horário de entrada programado já passou em determinados fusos horários. 

{% alert tip %}
Você verá um alerta se não tiver programado um buffer suficiente. Uma solução rápida é ajustar o tempo de envio para garantir que os usuários possam permanecer no segmento-alvo por 24 horas completas.
{% endalert %}

\![Um Canvas programado para entrar nos usuários de uma só vez a partir das 10 horas do dia 30 de abril de 2025, em seu horário local.]({% image_buster /assets/img_archive/canvas_checklist1.png %}){: style="max-width:75%;"}

### Considere o uso de expressões regulares para filtros de público-alvo

Depois de configurar os detalhes preliminares de quando seus usuários devem entrar em um Canvas, é recomendável verificar seus segmentos ou filtros na etapa **Público-alvo** da criação de um Canvas. Nessa etapa, você também pode revisar o resumo da **população-alvo** para ver como o público-alvo foi configurado. 

Aqui, considere o uso de uma expressão regular para segmentos ou filtros nas etapas de Caminhos do público-alvo e configurações de validação de entrega nas etapas de Divisão de mensagens e decisões. Uma [expressão regular]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/) (também chamada de regex) é uma cadeia de caracteres, o que significa que ela reconhece padrões e leva em conta caracteres, em vez de coisas como capitalização. Isso significa que, se você estiver usando "Equals / Does Not Equal", poderá estar limitando o tamanho do seu público devido a erros simples de sintaxe.

Se você perceber que seu público-alvo é menor do que o esperado, tente usar "Matches Regex" ou "Does Not Match Regex" em vez de "Equals" ou "Does Not Equal". Isso pode levar em conta os usuários ausentes e atingir um público maior. 

### Identificar configurações de entrada e condições de corrida

Uma condição de corrida pode ocorrer quando você usa os mesmos critérios de entrada nas configurações de **Entry Schedule** e **Target Audience**. 

Se estiver usando uma entrada baseada em ação, verifique se não usou aqui a mesma ação de acionamento do seu público-alvo. Pode ocorrer uma condição de corrida na qual o usuário não está no público no momento em que executa o evento de acionamento, o que significa que ele não entrará no Canvas.

{% alert tip %}
Confira as [práticas recomendadas]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#scenario-3-matching-action-based-triggers-and-audience-filters) para evitar essa condição de corrida ao configurar um Canvas baseado em ação com o mesmo acionador que o filtro de público-alvo.
{% endalert %}

### Verifique as propriedades de entrada do Canvas e as propriedades do evento

Embora o nome seja semelhante, [as propriedades de entrada do Canvas e as propriedades de evento]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) funcionam de forma diferente em seus fluxos de trabalho do Canvas. As propriedades de entrada do Canvas estão vinculadas às suas configurações de entrada e podem ser referenciadas em qualquer componente de mensagem em seu Canvas. As propriedades de entrada do Canvas são propriedades do evento ou da chamada de API que aciona a entrada de um usuário em um Canvas, usando configurações de entrada baseadas em ação ou acionadas por API.

As propriedades de eventos, por outro lado, só podem ser referenciadas na primeira etapa de Mensagem após uma etapa de Caminhos de Ação. As propriedades de evento são propriedades de um evento personalizado ou evento de compra que o usuário realizou durante a janela de avaliação de uma etapa dos Caminhos de Ação e que aciona sua progressão em um dos caminhos de ação definidos.

Verifique se há alguma etapa da mensagem na visualização da mensagem que faça referência às propriedades de entrada do Canvas ou às propriedades do evento.

### Revisar as etapas da mensagem para o avanço do usuário

Por padrão, os usuários avançarão por todas as etapas da mensagem, independentemente de terem recebido ou não a mensagem. Se quiser avançar os usuários que receberão uma determinada mensagem, poderá fazê-lo adicionando uma etapa de divisão de decisão diretamente após o componente Mensagem. Adicione o filtro "Mensagem recebida da etapa do Canvas" como filtro adicional e, em seguida, selecione a etapa Canvas e Mensagem.

Para etapas de mensagens com mensagens in-app, talvez você queira usar um componente Caminhos de ação em vez do componente Divisão de decisão. Isso permitirá que você avance os usuários com base no fato de eles terem visualizado sua mensagem in-app. Defina um grupo de ações adicionando o filtro "Interact with Step" (Interagir com a etapa) e selecione **View in app message (Exibir na mensagem do aplicativo**). Em seguida, defina a janela de avaliação da etapa como a janela de expiração da mensagem in-app.

Para um componente Message em mensagens multicanal, recomendamos o seguinte:
* Inclua uma etapa de atraso entre as etapas de divisão de mensagem e decisão e defina o atraso para pelo menos cinco segundos
* Se o componente incluir o Intelligent Timing, defina o atraso para 24 horas
* Se o componente incluir limitação de taxa, divida suas mensagens em várias etapas de mensagem de canal único e conecte-as. Em seguida, conecte a etapa Decision Split diretamente após a última etapa Message para verificar se um usuário recebeu alguma das mensagens. Você também pode usar esse método como alternativa para uma etapa de mensagem multicanal com Intelligent Timing.

## Coisas a considerar após o lançamento

Você lançou seu Canvas! E agora? Use esta lista de verificação para ver como você pode revisar e ajustar seu Canvas em caso de discrepâncias após o lançamento com base nesses cenários.

### Muitas entradas, mas poucos envios

Por exemplo, digamos que você tenha notado uma disparidade entre o número de mensagens enviadas e o total de entradas. Você pode identificar e descobrir áreas para ajustar seu Canvas verificando essas áreas-chave.

#### Público de entrada

Se estiver usando uma campanha de envio programado, verifique novamente seu público-alvo revisando sua população-alvo. Como estão os números nos canais e como isso se relaciona com os canais que você usou em seu Canvas? Se os números mais baixos corresponderem aos canais que você usou em seu Canvas, talvez você tenha encontrado o problema.

#### Primeiro componente do Canvas

Revise todos os filtros de público-alvo, acionadores de ação ou segmentos usados nos componentes iniciais de seu Canvas. Há algum erro de ortografia ou condições muito rígidas que estejam impedindo que seu Canvas comece bem? Você está usando "Equals" quando deveria estar usando "Matches Regex"?

#### Grupo de controle de tela 

Analise a distribuição de usuários entre suas variantes e seu grupo de controle. O grupo de controle é maior do que você pretendia? Se for o caso, você pode editar essa configuração. Se **a Seleção Inteligente** estiver ativada e o grupo de controle estiver ganhando, considere interromper o Canvas e tentar uma nova abordagem.

### Um público total vazio

Se você não estiver vendo nenhum dado de entrada para o seu Canvas, o motivo pelo qual os usuários podem não estar entrando no Canvas pode ser devido a condições raciais e filtros restritivos de segmentação de público.

Se estiver usando a entrada baseada em ação em seu cronograma de entrada, verifique se não usou a mesma ação de acionamento aqui que em seu **Target Audience**. Pode ocorrer uma condição de corrida na qual o usuário não está no público no momento em que executa o evento de acionamento, o que significa que ele não entrará no Canvas.

Além disso, verifique se o segmento selecionado tem usuários nele, revisando a tabela **Target Population (População-alvo** ) nas configurações de **Target Audience (Público-alvo** ). Se esse número for baixo, veja como ajustar suas configurações de entrada ou revise os segmentos ou filtros selecionados para verificar se há erros.

### Queda inesperada entre os degraus

Outra maneira aparente de identificar áreas de ajuste para seu Canvas pode ocorrer quando há uma grande queda de uma etapa do Canvas para a seguinte. Nesse caso, verifique se os filtros de público-alvo e os eventos de exceção não contêm erros de ortografia ou de capitalização. E, como sempre, verifique se os seus filtros de público-alvo não são tão rígidos a ponto de impedir que a maioria dos seus usuários entre no Canvas. 

Em seguida, é importante identificar essas configurações que podem afetar quando e se as mensagens são enviadas aos seus usuários:
- [Cronograma inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)
- Horário de silêncio
- Validações de entrega

Em geral, escolha Intelligent Timing ou Quiet Hours para o Canvas, e não ambos. A mesma sugestão se aplica ao uso do Intelligent Timing ou [da limitação de taxa]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/), não de ambos. Para obter mais informações sobre a melhor forma de usar o Intelligence Suite, leia nossos [casos de uso do Intelligent Suite]({{site.baseurl}}/user_guide/brazeai/intelligence/#use-cases).

### Volumes suspeitos de envio entre caminhos

Quando o volume de envios entre dois ou mais caminhos (Caminhos de público-alvo ou Caminhos de ação) não é o esperado, essa pode ser uma oportunidade para verificar seus segmentos, filtros ou ações de acionamento. Além disso, certifique-se de identificar e remover todos os filtros sobrepostos.

