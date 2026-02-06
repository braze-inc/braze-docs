---
nav_title: Solução de problemas
article_title: Solução de problemas em telas
page_order: 11
page_type: reference
description: "Esta página fornece etapas de solução de problemas para Canvas."
tool: Canvas
---

# Solução de problemas em telas

> Esta página o ajuda a solucionar problemas com suas Canvas.

## Por que um usuário não recebeu uma etapa do Canva disparada?

Primeiro, confirme se o evento personalizado está sendo passado para o Braze. Acesse **Análise de dados** > **Relatório de eventos personalizados** e, em seguida, selecione o respectivo evento personalizado e o intervalo de datas. Se o evento não for exibido, confirme se ele foi configurado corretamente e se o usuário executou a ação correta.

Se o evento personalizado for exibido, solucione o problema da seguinte forma:

- Verifique o download do perfil do usuário para confirmar se ele disparou o evento e quando o fez. Se o evento foi disparado, compare o registro de data e hora de quando o evento foi disparado com a hora em que o Canva foi TTL. O evento pode ter sido disparado antes da ativação do Canva.
- Revise os changelogs do Canva e de todos os segmentos usados no direcionamento para determinar se o usuário estava no segmento quando o evento personalizado foi disparado. Se não estivessem no segmento, não teriam recebido a etapa do canva.
- Verifique se o usuário foi inserido em um grupo de controle por meio de segmentação e, consequentemente, impedido de receber a etapa do Canva.
- Se houver uma postergação programada, verifique se o evento personalizado do usuário foi disparado antes da postergação. Se o evento fosse disparado antes da postergação, eles não teriam recebido a etapa do Canva.

{% alert note %}
As mensagens no app só podem ser disparadas por eventos enviados pelo SDK, não pela API REST.
{% endalert %}

## Por que meu Canva não está sendo enviado como esperado?

Os canvas são robustos e complexos e sabemos que você dedica tempo e cuidado ao criá-los. Portanto, se achar que seu Canvas não está sendo enviado da maneira desejada, recomendamos verificar a programação, o público e as configurações de entrada do Canvas e revisar as etapas de [criação de um Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).

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

## Por que o meu público não se dividiu igualmente entre o grupo de controle e o grupo variante?

Ao criar o Canva, talvez você esperasse que o público se dividisse igualmente entre o grupo de controle e o grupo de variantes, como no [caso de uso](#use-case) a seguir. Vamos discutir por que isso acontece e como corrigi-lo!

O grupo que um usuário ingressa depende de suas configurações. Isso pode ser o grupo de controle ou o grupo variante. Um usuário entrará em um Canvas quando se encaixar em todos os critérios definidos na [etapa de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=entry%20schedule#step-12-determine-your-canvas-entry-schedule). Ao configurar sua canva, você define qual porcentagem de usuários entrará em cada variante e no grupo de controle.

Se o seu grupo de controle for grande em comparação com o seu grupo variante (e essa não for a sua intenção), recomendamos o seguinte:
1. Defina seu filtro de público-alvo de entrada **como Foreground Push Enabled**.
2. Defina o filtro de público-alvo de entrada para **Status da inscrição push**, **Status da inscrição por e-mail** ou ambos como **Aceitação** ou **Inscrição**.

Ao criar um Canvas com um grupo de controle, confirme se todos os usuários do público de entrada podem receber mensagens no Canvas (por exemplo, se o Canvas contém mensagens push e de e-mail).

### Caso de uso

Vamos imaginar o seguinte cenário:
- Uma canva tem uma única variante e um grupo de controle.
- A primeira etapa da variante é uma notificação por push.
- 90% dos usuários foram selecionados para entrar na variante, e 10% para entrar no grupo de controle.

![Exemplo de canvas com 90% de variante e 10% de grupo de controle.]({% image_buster /assets/img_archive/trouble15.png %})

Neste cenário, 90% dos usuários que entrarem no canva entrarão na variante. 

Se olharmos para os usuários ativos, veremos que, embora contenha 29,8 mil usuários, apenas 64% deles têm a capacitação ativada:

![Segmento com o filtro "Push Enabled" (Capacitação ativada por push) definido como "true" (verdadeiro) e usuários estimados em 29,8 mil.]({% image_buster /assets/img_archive/trouble16.png %})

Isso significa que, embora tenhamos especificado que 90% dos usuários entrem na variante, nem todos esses usuários conseguem receber uma notificação por push. Esses usuários que não conseguem receber uma notificação por push ainda entrarão na variante, independentemente.