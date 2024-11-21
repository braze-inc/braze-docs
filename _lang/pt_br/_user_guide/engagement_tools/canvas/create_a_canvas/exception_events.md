---
nav_title: Eventos de exceção 
article_title: Eventos de exceção
page_order: 4
page_type: reference
description: "Este artigo de referência descreve os eventos de exceção e como eles afetam seus componentes do Canva."
tool: Canvas

---

# Eventos de exceção do Canva

{% alert important %}
A partir de 28 de fevereiro de 2023, não será mais possível criar ou duplicar canvas usando o editor original. Este artigo está disponível para referência ao configurar eventos de exceção para o fluxo de trabalho do canva original. <br><br> A Braze recomenda que os clientes que usam a experiência original do Canvas migrem para o Canvas Flow. É uma experiência de edição aprimorada para melhor construir e gerenciar canvas. Saiba mais sobre a [clonagem de canvas no Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

> Ao programar um componente para um Canvas usando o editor de Canvas original, você tem a opção de configurar um evento de exceção. Você pode adicionar um evento de exceção a um componente, desde que o público não seja imediatamente avançado. Os usuários que realizarem o evento de exceção não serão [avançados na etapa][2] e deixarão de fazer parte do seu público do Canva.

Os eventos de gatilho só serão disparados enquanto um usuário estiver esperando para receber o componente canva associado. Se um usuário executar a mesma ação em uma etapa anterior do Canva, o evento de exceção não será disparado.

{% alert important %}
No Canvas Flow, os eventos de exceção só são configurados usando [jornadas de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/). Por exemplo, você pode definir uma Jornada de ação e usar a jornada Todos os outros como exceção.
{% endalert %}

Os eventos de exceção para uma etapa baseada em ação funcionarão durante a postergação ou a janela da etapa. As etapas programadas não têm uma janela e, como resultado, o evento de exceção só funcionará se ocorrer durante a postergação.

Por exemplo, se você tiver um evento de exceção para "Carrinho abandonado" na terceira etapa do seu Canva, mas um usuário abandonar o carrinho enquanto estiver na segunda etapa, o evento de exceção não será disparado. Nesse exemplo, o evento de exceção só será disparado se o usuário abandonar o carrinho na terceira etapa do Canva. 

![][1]


[1]:{% image_buster /assets/img_archive/Canvas_Exception_Events.png %}
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/
