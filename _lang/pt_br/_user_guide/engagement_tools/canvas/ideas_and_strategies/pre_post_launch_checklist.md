---
nav_title: Lista de Verificação Pré e Pós-Lançamento
article_title: Lista de Verificação Pré e Pós-Lançamento
page_order: 2
description: "Este artigo fornece um guia para coisas a serem verificadas antes e depois de lançar um canva."
tool: Canvas

---

# Lista de verificação pré e pós-lançamento

> Este artigo fornece um guia para coisas a serem verificadas antes e depois de lançar um canva.

## Coisas a considerar antes do lançamento

Antes de lançar uma canva, há vários detalhes que você pode verificar para garantir que seu envio de mensagens e horários de envio estejam alinhados com as preferências do seu público. Coisas a considerar incluem quaisquer variações nos fusos horários, configurações de entrada e mais. Usando esta lista de verificação como guia, ajuste essas áreas com base no seu caso de uso para ajudar a contribuir para o sucesso do seu canva. 

{% alert important %}
A partir de 28 de fevereiro de 2023, você não poderá mais criar ou duplicar canvas usando a experiência original do canvas. A Braze recomenda que os clientes que usam a experiência original do Canvas migrem para o Canvas Flow. É uma experiência de edição aprimorada para melhor construir e gerenciar canvas. Saiba mais sobre a [clonagem de canvas no Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

### Revisar configurações de fuso horário

Se você estiver inserindo usuários de acordo com seu fuso local usando um cronograma de entrada agendada, deve lançar seu canva pelo menos 24 horas antes de quando quiser que os usuários entrem em seu canva. Por exemplo, aqui está uma canva que não deixou tempo suficiente entre o lançamento e o horário de entrada programado. Neste cenário, pode haver alguns usuários que não entrarão na sua canva, pois o horário de entrada agendado já passou em certos fusos horários. 

{% alert tip %}
Você verá um alerta se não tiver agendado um buffer suficiente. Uma solução rápida é ajustar o tempo de envio para garantir que os usuários possam permanecer no segmento alvo por um período completo de 24 horas.
{% endalert %}

![Uma tela programada para entrar nos usuários de uma só vez a partir das 10 horas do dia 30 de abril de 2025, em seu fuso local.]({% image_buster /assets/img_archive/canvas_checklist1.png %}){: style="max-width:75%;"}

### Considere usar expressões regulares para filtros de público

Depois de configurar os detalhes preliminares de quando seus usuários devem entrar em uma canva, é recomendável agora verificar seus segmentos ou filtros na **etapa de Público-alvo** de construção de uma canva. Nesta etapa, você também pode revisar o resumo do **público-alvo** para ver como seu público-alvo foi configurado. 

Aqui, considere usar uma expressão regular para segmentos ou filtros nas etapas de Caminhos do Público, configurações de validação de entrega na Mensagem e etapas de divisão de decisão também. Uma [expressão regular]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/) (também conhecida como regex) é uma string, o que significa que reconhece padrões e leva em consideração caracteres, em vez de coisas como capitalização. Isso significa que, se você estiver usando "Igual / Diferente", poderá estar limitando o tamanho do seu público devido a erros de sintaxe simples.

Se você notar que seu {target} público é menor do que o esperado, tente usar "Corresponde ao regex" ou "Não corresponde ao regex" em vez de "Igual" ou "Não igual". Isso pode explicar os usuários ausentes e atingir um público maior. 

### Identificar configurações de entrada e condições de corrida

Uma condição de corrida pode ocorrer quando você usou os mesmos critérios de entrada tanto nas suas configurações de **Programação de Entrada** quanto de **Público-Alvo**. 

Se você estiver usando entrada baseada em ação, verifique se não usou a mesma ação-gatilho aqui que no seu público-alvo. Uma condição de corrida pode ocorrer na qual o usuário não está no público no momento em que realiza o evento de gatilho, o que significa que ele não entrará no canva.

{% alert tip %}
Confira as [práticas recomendadas]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#scenario-3-matching-action-based-triggers-and-audience-filters) para evitar essa condição de corrida ao configurar um Canva baseado em ação com o mesmo disparo que o filtro de público.
{% endalert %}

### Verifique as propriedades de entrada da canva e as propriedades do evento

Embora semelhantes no nome, [as propriedades de entrada do Canva e as propriedades de evento]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) funcionam de maneira diferente dentro dos seus fluxos de trabalho do Canva. As propriedades de entrada da canva estão vinculadas às suas configurações de entrada e podem ser referenciadas em qualquer componente de mensagem ao longo da sua canva. As propriedades de entrada do canva são propriedades do evento ou chamada de API que aciona a entrada de um usuário em um canva, usando configurações de entrada baseadas em ação ou acionadas por API.

As propriedades do evento, por outro lado, só podem ser referenciadas na primeira etapa de mensagem após uma jornada de ação. As propriedades do evento são propriedades de um evento personalizado ou evento de compra que o usuário realizou durante a janela de avaliação de uma etapa de Jornadas de Ação, e que desencadeia sua progressão em uma das jornadas de ação definidas.

Verifique sua <b><i><u>}prévia<{biu} da mensagem para quaisquer etapas de Mensagem que referenciem propriedades de entrada do <b><i><u>}canva<{biu} ou propriedades de evento.

### Revisar etapas de mensagem para avanço do usuário

Por padrão, os usuários avançarão por todas as etapas de Mensagem, independentemente de terem recebido a mensagem. Se você deseja avançar os usuários que recebem uma mensagem específica, pode fazê-lo adicionando uma etapa de divisão de decisão diretamente após o seu componente de mensagem. Adicione o filtro "Recebeu mensagem de uma etapa de um canva" como filtro adicional, depois selecione o canva e a etapa da Mensagem.

Para etapas de Mensagem com envio de mensagens no app, você pode querer usar um componente de jornadas de ação em vez do componente de divisão de decisão. Isso permitirá que você avance os usuários com base em se eles visualizaram sua mensagem no app. Defina um grupo de ação adicionando o filtro "Interagir com a etapa" e selecione **Ver na mensagem do app**. Em seguida, defina a janela de avaliação da etapa para a janela de expiração da mensagem no app.

Para um componente de mensagem em envio de mensagens multicanal, recomendamos o seguinte:
* Inclua uma etapa de postergação entre suas etapas de mensagem e divisão de decisão, e defina a postergação para pelo menos cinco segundos
* Se o componente incluir Intelligent Timing, defina a postergação para 24 horas
* Se o componente incluir limitação de taxa, divida suas mensagens em várias etapas de Mensagem de canal único e conecte-as juntas. Em seguida, conecte a etapa de divisão de decisão diretamente após a última etapa de mensagem para verificar se um usuário recebeu alguma das mensagens. Você também pode usar este método como uma alternativa para uma etapa de Mensagem multi-canal com Intelligent Timing.

## Coisas a considerar após o lançamento

Você lançou seu canva! E agora? Use esta lista de verificação para ver como você pode revisar e ajustar sua canva no caso de discrepâncias após o lançamento com base nesses cenários.

### Muitas entradas, mas poucos envios

Por exemplo, digamos que você tenha notado uma disparidade entre o número de mensagens enviadas e o total de entradas. Você pode identificar e descobrir áreas para ajustar sua canva verificando essas áreas-chave.

#### Público de entrada

Se você estiver usando uma campanha de envio agendada, verifique novamente seu público-alvo revisando seu público-alvo. Como os números se comportam nos canais e como isso se relaciona com os canais que você usou na sua canva? Se os números mais baixos corresponderem aos canais que você usou na sua canva, você pode ter encontrado o problema.

#### Primeiro componente da canva

Revise quaisquer filtros de público, gatilhos de ação ou segmentos usados nos componentes iniciais do seu canva. Há algum erro de ortografia ou condições muito rigorosas que estão impedindo sua canva de começar bem? Você está usando "Equals" quando deveria estar usando "Matches regex"?

#### Grupo de controle do canva 

Revise a distribuição de usuários entre suas variantes e seu grupo de controle. O grupo de controle é maior do que você pretendia? Se for o caso, você pode editar esta configuração. Se você tiver **Seleção Inteligente** ativada, e o grupo de controle estiver ganhando, considere parar seu canva e tentar uma nova abordagem.

### Um público total vazio

Se não estiver vendo nenhum dado de entrada no seu Canvas, o motivo pelo qual os usuários podem não estar entrando no Canvas pode ser devido a condições de corrida e filtros de segmentação de público restritivos.

Se você estiver usando entrada baseada em ação em sua programação de entrada, verifique se não usou a mesma ação-gatilho aqui que em seu **público-alvo**. Uma condição de corrida pode ocorrer na qual o usuário não está no público no momento em que realiza o evento de gatilho, o que significa que ele não entrará no canva.

Além disso, verifique se o segmento selecionado possui usuários revisando a tabela de **público-alvo** nas configurações de **público-alvo**. Se este número for baixo, veja como você pode ajustar suas configurações de entrada ou revise seus segmentos ou filtros selecionados para quaisquer erros.

### Queda inesperada entre as etapas

Outra maneira aparente de identificar áreas de ajuste para o seu canva pode ocorrer quando há uma grande queda de uma etapa do canva para a próxima. Neste caso, verifique se seus filtros de público e eventos de exceção não contêm erros de ortografia ou capitalização. E como sempre, verifique se seus filtros de público não são tão rígidos a ponto de impedir que a maioria de seus usuários entre no canva. 

Em seguida, é importante identificar essas configurações que podem afetar quando e se as mensagens são enviadas aos seus usuários:
- [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)
- Horário de silêncio
- Validações de entrega

Em geral, escolha Intelligent Timing ou horário de silêncio para o seu canva, não ambos. A mesma sugestão se aplica ao uso de Intelligent Timing ou [limitação de taxa]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/), não ambos. Para saber mais sobre como usar melhor o Intelligence Suite, leia nossas [Perguntas frequentes sobre inteligência]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/).

### Volumes de envio suspeitos entre caminhos

Quando o volume de envios entre duas ou mais jornadas (sejam Jornadas de público ou Jornadas de ação) não é o que você espera, isso pode ser uma oportunidade para verificar seus segmentos, filtros ou ações de gatilho. Além disso, certifique-se de identificar e remover quaisquer filtros sobrepostos.

