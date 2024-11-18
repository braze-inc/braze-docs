---
nav_title: Como lidar com um grande grupo de controle
article_title: Como lidar com um grande grupo de controle
page_order: 2

page_type: solution
description: "Este artigo de ajuda descreve por que seu grupo de controle pode ser maior do que o esperado e orienta você nas etapas para corrigir isso."
tool: Canvas
---

# Lidando com um grande grupo de controle

Ao criar sua canva, você pode ter esperado que seu público se dividisse igualmente entre seu grupo de controle e seu grupo variante, como no seguinte [exemplo](#example). Podemos explicar por que isso acontece e como corrigir!

O grupo que um usuário ingressa depende de suas configurações. Isso pode ser o grupo de controle ou o grupo variante. Um usuário entrará em um canva quando atender a todos os seus critérios definidos na [Etapa][1]]. Ao configurar sua canva, você define qual porcentagem de usuários entrará em cada variante e no grupo de controle.

Se o seu grupo de controle for grande em comparação com o seu grupo variante (e essa não for a sua intenção), recomendamos o seguinte:
1. Defina seu filtro de público de entrada para "Push está habilitado".
2. Defina seu filtro de público de entrada para "Optou por participar ou está inscrito".

Ao criar uma canva com um grupo de controle, certifique-se de que todos os usuários no público de entrada possam receber mensagens dentro da canva (como a canva contém mensagens push e e-mail).

## Caso de uso

Vamos imaginar o seguinte cenário:
- Uma canva tem uma única variante e um grupo de controle.
- A primeira etapa da variante é uma notificação por push.
- 90% dos usuários foram selecionados para entrar na variante, e 10% para entrar no grupo de controle.

![Exemplo de canvas][41]

Neste cenário, 90% dos usuários que entrarem no canva entrarão na variante. 

Se olharmos para os usuários ativos, podemos ver que, embora sejam 39,8 mil usuários, apenas 73% deles estão com push habilitado:

![Público de entrada][42]

Isso significa que, embora tenhamos especificado que 90% dos usuários entrem na variante, nem todos esses usuários conseguem receber uma notificação por push. Esses usuários que não conseguem receber uma notificação por push ainda entrarão na variante, independentemente.

Ainda precisa de ajuda? Abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).

_Última atualização em 3 de dezembro de 2020_

[1]: {{site.baseurl }}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2-use-the-entry-wizard-to-set-up-your-canvas
[41]: {% image_buster /assets/img_archive/trouble15.png %}
[42]: {% image_buster /assets/img_archive/trouble16.png %}
