---
nav_title: Modelos de canva
article_title: Modelos de canva
alias: "/canvas_templates/templates/"
page_order: 0
description: "Este artigo de referência aborda como criar modelos disponíveis do Canvas."
page_type: reference
---

# Modelos de canva

> O Braze tem uma seleção de modelos de canvas disponíveis para você usar como referência e como práticas recomendadas para casos de uso comuns. Embora esses modelos não possam ser editados, você pode visualizá-los em **Templates** > **Braze templates** ou usá-los em suas Canvas.

![Modelos do Braze na seção de modelos do Canvas com treze modelos disponíveis.]({% image_buster /assets/img/braze_canvas_templates.png %})

Selecione um dos modelos disponíveis a seguir para fazer referência ou usar como seu Canva.

## Modelos padrão do Canva

{% tabs %}
{% tab Abandoned Intent %}

### Intenção abandonada

Engajamento com os usuários em tempo real para incentivá-los a concluir suas compras.

Considere o seguinte ao usar este modelo:

- Adicione um público específico. Atualmente, as jornadas do público são disparadas com base em "Made Any Purchase", mas você pode adaptar isso a produtos específicos que deseja direcionar.
- Esse modelo pressupõe que você tenha uma jornada pós-compra separada, portanto, fazer uma compra fará com que os usuários saiam do Canva.
- Preencha os detalhes na etapa Audience Sync.

{% endtab %}
{% tab Back In Stock %}

### De volta ao estoque

Impulsione as compras notificando seus usuários quando um item estiver de volta ao estoque com envio de mensagens personalizadas. Considere o seguinte ao usar este modelo:

- Em **Entry Schedule**, selecione um catálogo para usar. Isso permite acessar dados, como produtos, descontos e promoções, para direcionar ainda mais seus usuários.
- Em **Target Audience (Público alvo)**, adicione um segmento para direcionar os usuários que indicaram interesse em um determinado item.
- Nas etapas de mensagens em todo o Canva, atualize o Liquid para fazer referência ao seu catálogo.

{% endtab %}
{% tab Feature Adoption %}

### Adoção de recursos

Envie mensagens personalizadas em tempo hábil para destacar os benefícios e as dicas de uso. Considere o seguinte ao usar este modelo:

- Excluir usuários que já adotaram o recurso. Por exemplo, em **Público-alvo**, adicione um filtro para um evento personalizado, como "Recurso ativado", que já tenha ocorrido.
- Para usar a etapa da jornada experimental, defina um evento de conversão. Esse evento deve ser o evento que sinaliza a adoção do recurso.
- Configure a etapa da jornada de ação no modelo com eventos personalizados para "Recurso ativado" e "Tour realizado".
- Configure os atributos personalizados na etapa de mensagens denominada "Pesquisa de feedback" para capturar o sentimento do feedback.

{% endtab %}
{% tab Lapsed User %}

### Usuário desistente

Traga os usuários de volta ao seu app com incentivos baseados em seus engajamentos anteriores. Considere o seguinte ao usar este modelo:

- Em **Basics**, selecione um app específico para rastrear conversões.
- No editor do Canva, adicione aplicativos específicos para as etapas das jornadas de ação.
- Configure a etapa Audience Sync com os parceiros e públicos para seu caso de uso.

{% endtab %}
{% tab Onboarding %}

### Onboarding

Crie jornadas de integração que promovam uma forte adoção inicial e incentivem relacionamentos duradouros com seus usuários. Considere o seguinte ao usar este modelo:

- Na etapa Jornadas do público denominada "Audience Split" (Divisão do público), considere a possibilidade de personalizar as principais ações para usuários engajados. No modelo, o filtro de segmento é "Has clicked e-mail for step Welcome Email".

{% endtab %}
{% tab Post-Purchase Feedback %}

### Feedback pós-compra

Orquestre experiências personalizadas que lhe permitam responder ao feedback e construir relacionamentos com seus usuários. Considere o seguinte ao usar este modelo:

- Na primeira etapa do editor do Canva:
    - Especifique os atributos personalizados na mensagem no app para indicar o sentimento do feedback com base na opção de pesquisa selecionada. 
    - Especifique atribuições nos links de cada call-to-action para capturar a opção selecionada. Essas atribuições são referenciadas na jornada do público subsequente.
- Personalize a jornada do público com os atributos da primeira etapa deste modelo.
- Configure a etapa do Audience Sync chamada "Ad Redirecionamento".

{% endtab %}
{% endtabs %}

{% alert tip %}
Para obter um guia passo a passo sobre como criar um exemplo de tela usando esses modelos do Braze, consulte [Usando modelos do Braze]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates).
{% endalert %}

## Modelos de canvas para comércio eletrônico

Os modelos do eCommerce Canva são adaptados especificamente para profissionais de marketing de comércio eletrônico, facilitando a implementação de estratégias essenciais.

{% multi_lang_include canvas/ecommerce_templates.md %}