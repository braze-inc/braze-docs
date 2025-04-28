---
nav_title: Critérios de saída 
article_title: Critérios de saída 
page_order: 4.1
alias: /exit_criteria/
page_type: reference
description: "Este artigo de referência aborda o recurso critérios de saída do Canvas Flow."
tool: Canvas
---

# Critérios de saída

> Ao adicionar [eventos de exceção]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events) diretamente às regras de entrada do Canvas, seus usuários podem sair do Canvas assim que o evento ocorrer no final da etapa do canva. Isso ajuda a obter uma abordagem mais direcionada para o envio de mensagens do Canva para seu público.

Na etapa do **público-alvo** do construtor do Canvas, é possível configurar critérios de saída para identificar quais usuários você deseja que saiam do Canvas. Adicione seu evento de exceção e selecione **Add Trigger (Adicionar gatilho)**. 

Também é possível incluir segmentos e filtros nos critérios de saída, o que significa que os usuários que corresponderem ao segmento ou ao filtro sairão do Canva e não receberão mais nenhum envio de mensagens. Se a primeira etapa de um canva for uma etapa de Postergação com uma postergação de cinco dias, os critérios de saída serão aplicados no final dessa etapa. Portanto, se um usuário atender aos critérios de saída, ele sairá ao final dos cinco dias.

{% alert note %}
Atualmente, não há suporte para atribuições de matriz como critérios de saída em eventos de exceção.
{% endalert %}

## Eventos de exceção

Outros eventos de exceção incluem:
- Fazer uma compra
- Iniciar uma sessão
- Realização de um evento personalizado
- Realização de um evento de conversão
- Adição de um endereço de e-mail
- Alteração de um valor de atributo personalizado
- Atualização do status de uma inscrição
- Atualização do status de um grupo de inscrições
- Interagindo com uma campanha
- Inserção de um local
- Como disparar um geofence
- Envio de mensagens SMS de entrada
- Envio de mensagens de entrada do WhatsApp
- Envio de mensagens de entrada LINE
- Execução de um evento de atualização de carrinho
- Performance de um evento de checkout concluído
- Performance de um evento de checkout iniciado

## Caso de uso

Digamos que você queira direcionar os usuários que ainda não fizeram nenhuma compra na sua empresa. Primeiro, selecione **Make Purchase (Fazer compra)** como o evento de exceção. Em seguida, selecione **Add Trigger (Adicionar disparo)**. Quando o Canva for lançado, seu público excluirá os usuários que fizeram compras com as seguintes configurações de **Critérios de saída**. 

No exemplo a seguir, esse critério de saída também é aplicado ao segmento "Used in last day" (Usado no último dia) para qualquer usuário que tenha feito exatamente uma compra.

![Configurações de critérios de saída com "Faz alguma compra" como o evento de exceção, portanto, se um usuário fizer uma compra, ele sairá desse canva.][1]

[1]: {% image_buster /assets/img_archive/exit_criteria_example.png %} 
