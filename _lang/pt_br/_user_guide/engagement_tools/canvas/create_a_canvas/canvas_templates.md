---
nav_title: Criação de um modelo do Canvas
article_title: Criação de um modelo de tela
alias: "/canvas_templates/"
page_order: 0.5
description: "Este artigo de referência aborda como criar um modelo para o Canvas."
page_type: reference
---

# Criação de um modelo do Canvas

> Este artigo de referência aborda como criar e gerenciar modelos para o Canvas. O uso de modelos pode refinar suas mensagens, criando uma estrutura consistente que pode ser facilmente personalizada para atender às suas metas específicas em todos os Canvases.

{% alert tip %}
Economize tempo e agilize a criação de seu Canvas usando [os modelos do Braze Canvas](#available-braze-templates)! Navegue em nossa biblioteca de modelos pré-criados para encontrar um que se adapte ao seu caso de uso e personalize-o para atender às suas necessidades específicas.
{% endalert %}

## Método 1: Criar a partir de um Canvas existente

### Etapa 1: Selecione seu Canvas existente

No painel de controle do Braze, acesse **Messaging** > **Canvas** e selecione um Canvas existente que você deseja usar como modelo.

### Etapa 2: Crie seu modelo

No editor do Canvas, selecione **Editar Canvas** ou **Editar rascunho**, dependendo se o Canvas está ativo ou em um rascunho. Expanda o menu suspenso **Salvar como rascunho** no rodapé e selecione **Salvar como modelo**.

\![]({% image_buster /assets/img/save_canvas_as_template.png %})

### Etapa 3: Salvar seu modelo

Em seguida, dê um nome ao seu modelo e adicione todas as tags relevantes. Em seguida, selecione **Salvar**. Seu modelo agora está pronto para ser usado na criação de um Canvas, o que lhe dá uma vantagem inicial com as configurações e etapas básicas já definidas.

## Método 2: Criar por meio do editor de modelos do Canvas

### Etapa 1: Vá para o editor de modelos do Canvas

No painel de controle do Braze, vá para **Templates** > **Canvas Templates**.

{% alert note %}
Se você estiver usando a navegação mais antiga, poderá encontrar essa página em **Engagement** > **Templates & Media** > **Canvas Templates**.
{% endalert %}

### Etapa 2: Criar um novo modelo

Selecione **Criar modelo** e comece a configurar os detalhes do Canvas. Você pode começar dando um nome ao seu modelo do Canvas.

\![Um exemplo de modelo de tela chamado "Modelo de tela de venda anual" com a descrição "Use para a promoção anual de primavera".]({% image_buster /assets/img/canvas_template_example.png %})

### Etapa 3: Personalize seu modelo

Em seguida, personalize seu modelo configurando [o Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2-set-up-your-canvas). Você pode decidir quando os usuários devem entrar no Canvas, determinar quais usuários podem entrar nesse Canvas, ajustar as configurações de envio e criar a jornada do usuário para o modelo.

### Etapa 4: Salvar seu modelo

Depois de terminar de personalizar o modelo, selecione o botão **Salvar modelo**. Na página **do modelo** do Canvas, você pode visualizar os detalhes do modelo do Canvas selecionando <i class="fas fa-list"></i> **Detalhes do modelo**. 

## Uso de modelos do Canvas

Há duas maneiras de usar seu modelo ao compor um Canvas:

- **De Mensagens**: Vá para **Mensagens** > **Canvas**. Selecione o botão **Create Canvas (Criar tela)** e **Use a Canvas Template (Usar um modelo de tela)**.
- **Dos modelos**: Vá para **Templates** > **Canvas Templates** e localize o modelo desejado. Em seguida, selecione o menu <i class="fas fa-ellipsis-vertical"></i> seguido de **Apply template (Aplicar modelo)**. Isso o levará a um novo Canvas com o modelo aplicado no compositor do Canvas.

### Modelos de brasagem disponíveis

O Braze tem uma seleção de modelos de Canvas disponíveis para você consultar e usar como práticas recomendadas para casos de uso comuns. Embora esses modelos não possam ser editados, você pode visualizá-los em **Templates** > **Braze templates** ou usá-los em seus Canvases.

Modelos do Braze na seção de modelos do Canvas com seis modelos disponíveis.]({% image_buster /assets/img/braze_canvas_templates.png %})

Selecione um dos modelos disponíveis a seguir para fazer referência ou usar como seu Canvas.

{% tabs %}
{% tab Abandoned Intent %}

Interaja com os usuários em tempo real para incentivá-los a concluir suas compras.

Considere o seguinte ao usar esse modelo:

- Adicionar um público específico. Atualmente, os caminhos do público-alvo são acionados com base em "Made Any Purchase", mas você pode adaptar isso a produtos específicos que deseja segmentar.
- Esse modelo pressupõe que você tenha uma jornada pós-compra separada, portanto, fazer uma compra fará com que os usuários saiam do Canvas.
- Preencha os detalhes na etapa Audience Sync.

{% endtab %}
{% tab Back In Stock %}

Impulsione as compras notificando seus usuários quando um item estiver de volta ao estoque com mensagens personalizadas. Considere o seguinte ao usar esse modelo:

- Em **Entry Schedule**, selecione um catálogo para usar. Isso permite que você acesse dados, como produtos, descontos e promoções, para direcionar ainda mais seus usuários.
- Em **Target Audience**, adicione um segmento para direcionar os usuários que indicaram interesse em um determinado item.
- Nas etapas de Mensagem em todo o Canvas, atualize o Liquid para fazer referência ao seu catálogo.

{% endtab %}
{% tab Feature Adoption %}

Envie mensagens personalizadas em tempo hábil para destacar os benefícios e as dicas de uso. Considere o seguinte ao usar esse modelo:

- Excluir usuários que já tenham usado o produto. Por exemplo, em **Target Audience**, adicione um filtro em 
-  Para usar a etapa Caminho do experimento, defina um evento de conversão. Esse evento deve ser o evento que sinaliza a adoção do recurso.
- Configure a etapa Action Path no modelo com eventos personalizados para "Activated Feature" (Recurso ativado) e "Taken Tour" (Passeio realizado).
- Configure os atributos personalizados na etapa de mensagem denominada "Pesquisa de feedback" para capturar o sentimento do feedback.

{% endtab %}
{% tab Lapsed User %}

Traga os usuários de volta ao seu aplicativo com incentivos baseados em seus envolvimentos anteriores. Considere o seguinte ao usar esse modelo:

- Em **Basics**, selecione um aplicativo específico para o qual rastrear conversões.
- No editor do Canvas, adicione aplicativos específicos para as etapas dos Caminhos de Ação.
- Configure a etapa Audience Sync com os parceiros e públicos para seu caso de uso.

{% endtab %}
{% tab Onboarding %}

Crie jornadas de integração que promovam uma forte adoção inicial e incentivem relacionamentos duradouros com seus usuários. Considere o seguinte ao usar esse modelo:

- Na etapa Audience Paths (Caminhos do público) denominada "Audience Split" (Divisão do público), considere a possibilidade de personalizar as principais ações para usuários engajados. No modelo, o filtro de segmento é "Has clicked email for step Welcome Email".

{% endtab %}
{% tab Post-Purchase Feedback %}

Orquestre experiências personalizadas que lhe permitam responder ao feedback e criar um relacionamento com seus usuários. Considere o seguinte ao usar esse modelo:

- Na primeira etapa do editor do Canvas:
    - Especifique os atributos personalizados na mensagem in-app para indicar o sentimento do feedback com base na opção de pesquisa selecionada. 
    - Especifique atributos nos links de cada call-to-action para capturar a opção selecionada. Esses atributos são referenciados no caminho do público-alvo subsequente.
- Personalize o Audience Path com os atributos da primeira etapa deste modelo.
- Configure a etapa Audience Sync denominada "Ad Retargeting".

{% endtab %}
{% endtabs %}

{% alert tip %}
Para obter um guia passo a passo sobre como criar um exemplo de tela usando esses modelos do Braze, consulte [Usando modelos do Braze]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates).
{% endalert %}

## Gerenciando modelos do Canvas

Os modelos do Canvas podem ser duplicados e arquivados, de forma semelhante a um Canvas real. Para editar um modelo do Canvas, selecione o modelo e, em seguida, **<i class="fas fa-pencil-alt"></i>Edit**.

No nível do espaço de trabalho, é possível atualizar as permissões de usuário para permitir ou limitar o acesso para criar, editar, visualizar ou arquivar modelos do Canvas.

### Permissões para equipes e espaços de trabalho

Para permitir que apenas determinados usuários acessem e usem modelos específicos do Canvas, [adicione uma equipe]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) aos modelos e atribua permissões de "Access Campaigns, Canvases, Content Cards, Content Blocks, Feature Flags, Segments, Media Library e Preference Center" no nível da equipe.

Se você atribuir qualquer uma das seguintes permissões no nível da equipe, mas não no nível do espaço de trabalho, só poderá fazer o seguinte atribuído à sua equipe:

- Criar e editar modelos do Canvas
- Exibir modelos do Canvas
- Arquivar modelos do Canvas

Se as permissões forem concedidas no nível do espaço de trabalho e das equipes, as permissões no nível do espaço de trabalho serão priorizadas.

## Perguntas frequentes

### Posso salvar uma etapa incompleta em um modelo do Canvas?

Sim, você pode salvar etapas incompletas como um modelo do Canvas. No entanto, quando o modelo for usado, haverá um erro no botão **Salvar modelo** que indica o que é necessário para iniciar o Canvas.

### Posso salvar minhas configurações do Canvas builder como um modelo ou só posso salvar as etapas? 

Sim, você pode salvar as configurações no construtor do Canvas em um modelo do Canvas. Por exemplo, se você planeja usar uma combinação de segmentos e filtros com frequência, pode salvar essas configurações **do Target Audience** como parte do modelo do Canvas.

