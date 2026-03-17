---
nav_title: Solução de problemas
article_title: Solução de problemas de Canvases
page_order: 11
page_type: reference
description: "Esta página fornece etapas de solução de problemas para Canvases."
tool: Canvas
---

# Solução de problemas de Canvases

> Esta página ajuda você a solucionar problemas com seus Canvases.

## Por que um usuário não recebeu uma etapa do Canvas acionada?

Primeiro, confirme se o evento personalizado está sendo enviado para a Braze. Acesse **análise de dados** > **Relatório de Eventos Personalizados**, e então selecione o evento personalizado e o intervalo de datas respectivos. Se o evento não for exibido, confirme se está configurado corretamente e se o usuário realizou a ação correta.

Se o evento personalizado for exibido, continue a solução de problemas fazendo o seguinte:

- Verifique o download do perfil do usuário para confirmar se eles acionaram o evento e quando o fizeram. Se o evento foi acionado, compare o timestamp de quando o evento foi acionado com o momento em que o Canvas foi ao ar. O evento pode ter sido acionado antes do Canvas ir ao ar.
- Revise os changelogs do Canvas e quaisquer segmentos usados no direcionamento para determinar se o usuário estava no segmento quando seu evento personalizado foi acionado. Se eles não estavam no segmento, não teriam recebido a etapa do Canvas.
- Verifique se o usuário foi inserido em um grupo de controle por meio de segmentação e, consequentemente, impedido de receber a etapa do Canvas.
- Se houver um atraso programado, verifique se o evento personalizado do usuário foi acionado antes do atraso. Se o evento foi acionado antes do atraso, eles não teriam recebido a etapa do Canvas.

{% alert note %}
Mensagens no aplicativo só podem ser acionadas por eventos enviados através do SDK, não pela API REST.
{% endalert %}

## Por que meu Canvas não está enviando como esperado?

Os canvas são robustos e complexos e sabemos que você dedica tempo e cuidado ao criá-los. Então, se você descobrir que seu Canvas não está enviando da maneira que você deseja, recomendamos verificar o cronograma do seu Canvas, o público de entrada e as configurações de entrada, e revisar as etapas para [criar um Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).

### Cronograma

- O Canva está [programado corretamente]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#entry-schedule-types)?
- Você selecionou a data e a hora corretas?
- Para a [entrega baseada em ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=action-based%20delivery#entry-schedule-types), os usuários executaram as ações especificadas desde o lançamento do Canva?

### Configurações de entrada

As [configurações de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=basics#selecting-entry-controls) são importantes para entender como as telas estão sendo enviadas. Verifique se você limitou o número de pessoas que potencialmente entrarão no Canva.

Os usuários também podem sair de um Canva se não forem mais elegíveis para receber mensagens. Por exemplo, se o Canvas contiver apenas notificações por push e um usuário optar pela aceitação do push após receber a primeira etapa do canva, esse usuário sairá do Canvas. Considere o uso de [diferentes etapas do Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/) para adicionar jornadas de usuário alternativas.

### Segmentação de seu público

Considere as seguintes perguntas para seu público-alvo:

- Você selecionou o segmento correto?
- Como o segmento é configurado?
- Você confirmou que o segmento contém algum usuário?
- Você adicionou algum filtro adicional que limitaria o número de usuários que entram no Canva?
- Os usuários se qualificam para receber a primeira etapa de suas variantes? Por exemplo, se a primeira etapa do seu Canva for uma notificação por push, mas o público de entrada estiver todo desabilitado para push, nenhum usuário receberá mensagens.

## Por que nenhum usuário entrou no meu Canvas programado diariamente no dia da mudança para o horário de verão?

Nos dias de transição para o horário de verão (DST), os Canvases programados diariamente podem ser executados até uma hora mais cedo ou mais tarde do que o habitual. Se seus critérios de entrada dependem de atributos personalizados ou eventos com timestamps que caem dentro de uma hora do horário de entrada programado, os usuários podem não se qualificar no dia do DST porque o atributo ou evento ainda não foi registrado.

Por exemplo, suponha que os usuários normalmente recebam uma atualização de atributo personalizado às 3:00 p.m. no fuso horário do seu Canvas e seu Canvas é executado diariamente às 3:30 p.m. nesse mesmo fuso horário. Em um dia de avanço de horário de verão, o Canvas pode avaliar os usuários até uma hora mais cedo do que o habitual em relação a essa atualização de atributo—antes que o atributo tenha sido registrado. Se a re-eligibilidade estiver desativada, os usuários que entraram em dias anteriores não podem reentrar, resultando em zero entradas para aquele dia.

Para evitar isso, certifique-se de que suas atualizações de atributo personalizado ou evento ocorram mais de uma hora antes do horário de entrada programado do Canvas.

## Por que meu público não se dividiu igualmente entre o grupo de controle e o grupo variante?

Ao criar seu Canvas, você pode ter esperado que seu público se dividisse igualmente entre seu grupo de controle e seu grupo variante, como no seguinte [caso de uso](#use-case). Vamos discutir por que isso acontece e como corrigir!

O grupo que um usuário ingressa depende de suas configurações. Isso pode ser o grupo de controle ou o grupo variante. Um usuário entrará em um Canvas quando atender a todos os seus critérios definidos na [Etapa de Entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=entry%20schedule#step-12-determine-your-canvas-entry-schedule). Ao configurar sua canva, você define qual porcentagem de usuários entrará em cada variante e no grupo de controle.

Se o seu grupo de controle for grande em comparação com o seu grupo variante (e essa não for a sua intenção), recomendamos o seguinte:
1. Defina seu filtro de público de entrada para **Push em Primeiro Plano Habilitado**.
2. Defina seu filtro de público de entrada para **Status de Inscrição Push**, **Status de Inscrição por E-mail**, ou ambos para **Optou por Receber** ou **Inscrito**.

Ao criar um Canvas com um grupo de controle, confirme que todos os usuários no público de entrada podem receber mensagens dentro do Canvas (como o Canvas contém mensagens push e de e-mail).

### Caso de uso

Vamos imaginar o seguinte cenário:
- Uma canva tem uma única variante e um grupo de controle.
- A primeira etapa da variante é uma notificação por push.
- 90% dos usuários foram selecionados para entrar na variante, e 10% para entrar no grupo de controle.

![Exemplo de Canvas com 90% variante e 10% grupo de controle.]({% image_buster /assets/img_archive/trouble15.png %})

Neste cenário, 90% dos usuários que entrarem no canva entrarão na variante. 

Se olharmos para os usuários ativos, podemos ver que, embora contenha 29,8 mil usuários, apenas 64% deles têm push habilitado:

![Segmento com o filtro "Push Habilitado" definido como "verdadeiro", e usuários estimados de 29,8 mil.]({% image_buster /assets/img_archive/trouble16.png %})

Isso significa que, embora tenhamos especificado que 90% dos usuários entrem na variante, nem todos esses usuários conseguem receber uma notificação por push. Esses usuários que não conseguem receber uma notificação por push ainda entrarão na variante, independentemente.