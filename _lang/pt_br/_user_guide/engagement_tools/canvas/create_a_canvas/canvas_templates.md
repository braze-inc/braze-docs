---
nav_title: Criando um modelo de tela
article_title: Criando um modelo de tela
alias: "/canvas_templates/"
page_order: 0.5
description: "Este artigo de referência aborda como criar um modelo para o Canva."
page_type: reference
---

# Criação de um modelo do Canvas

> Este artigo de referência aborda como criar e gerenciar modelos para o Canva. O uso de modelos pode refinar o envio de mensagens, criando uma estrutura consistente que pode ser facilmente personalizada para atender às suas metas específicas em todas as telas.

{% alert tip %}
Economize tempo e agilize sua criação de telas usando os [modelos do Braze Canvas](#available-braze-templates)! Navegue em nossa biblioteca de modelos pré-criados para encontrar um que se adapte ao seu caso de uso e personalize-o para atender às suas necessidades específicas.
{% endalert %}

## Método 1: Criar a partir de um Canvas existente

### Etapa 1: Selecione seu Canva existente

No dashboard do Braze, acesse **Envio de mensagens** > **Canvas** e selecione um Canvas existente que você deseja usar como modelo.

### Etapa 2: Crie seu modelo

No editor do Canvas, selecione **Editar Canvas** ou **Editar rascunho**, dependendo se o Canvas estiver ativo ou em um rascunho. Expanda o menu suspenso **Salvar como rascunho** no rodapé e selecione **Salvar como modelo**.

![]({% image_buster /assets/img/save_canvas_as_template.png %})

### Etapa 3: Salve seu modelo

Em seguida, dê um nome ao seu modelo e adicione as tags relevantes. Em seguida, selecione **Salvar**. Seu modelo agora está pronto para ser usado na criação de um Canvas, o que lhe dá uma vantagem inicial com as configurações e etapas básicas já definidas.

## Método 2: Criar por meio do editor de modelos do Canva

### Etapa 1: Acesse o editor de modelos do Canva

No dashboard da Braze, acesse **Modelos** > **Modelos de canvas**.

{% alert note %}
Se estiver usando a navegação mais antiga, poderá encontrar essa página em **Engajamento** > **Modelos e mídias** > **Modelos de canvas**.
{% endalert %}

### Etapa 2: Criar um novo modelo

Selecione **Criar modelo** e comece a configurar os detalhes do Canva. Você pode começar dando um nome ao seu modelo do Canva.

![Um exemplo de modelo de tela chamado "Annual sale Canvas template" (Modelo de tela de venda anual) com a descrição "Use for annual spring promotion" (Use para a promoção anual de primavera).]({% image_buster /assets/img/canvas_template_example.png %})

### Etapa 3: Personalize seu modelo

Em seguida, personalize seu modelo configurando [o Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2-set-up-your-canvas). É possível decidir quando os usuários devem entrar no Canvas, determinar quais usuários podem entrar nesse Canvas, ajustar as configurações de envio e criar a jornada do usuário para o modelo.

### Etapa 4: Salve seu modelo

Depois de terminar de personalizar seu modelo, selecione o botão **Salvar modelo**. Na página **do modelo do Canvas**, você pode visualizar os detalhes do modelo do Canvas selecionando <i class="fas fa-list"></i> **Detalhes do modelo**. 

## Uso de modelos do Canvas

Há duas maneiras de usar seu modelo ao criar um canva:

- **Do envio de mensagens**: Acesse **Envio de mensagens** > **Canva**. Selecione o botão **Create Canvas** e **Use a Canvas Template**.
- **Dos modelos**: Acesse **Modelos** > **Modelos de tela** e localize o modelo desejado. Em seguida, selecione o menu <i class="fas fa-ellipsis-vertical"></i> seguido de **Apply template (Aplicar modelo**). Isso levará você a um novo canva com o modelo aplicado no criador de canvas.

### Modelos de Braze disponíveis

O Braze tem uma seleção de modelos de canvas disponíveis para você usar como referência e como práticas recomendadas para casos de uso comuns. Embora esses modelos não possam ser editados, você pode visualizá-los em **Templates** > **Braze templates** ou usá-los em suas Canvas.

![Modelos do Braze na seção de modelos do Canvas com seis modelos disponíveis.]({% image_buster /assets/img/braze_canvas_templates.png %})

Selecione um dos modelos disponíveis a seguir para fazer referência ou usar como seu Canva.

{% tabs %}
{% tab Intenção abandonada %}

Engajamento com os usuários em tempo real para incentivá-los a concluir suas compras.

Considere o seguinte ao usar este modelo:

- Adicione um público específico. Atualmente, as jornadas do público são disparadas com base em "Made Any Purchase", mas você pode adaptar isso a produtos específicos que deseja direcionar.
- Esse modelo pressupõe que você tenha uma jornada pós-compra separada, portanto, fazer uma compra fará com que os usuários saiam do Canva.
- Preencha os detalhes na etapa Audience Sync.

{% endtab %}
{% tab De volta ao estoque %}

Impulsione as compras notificando seus usuários quando um item estiver de volta ao estoque com envio de mensagens personalizadas. Considere o seguinte ao usar este modelo:

- Em **Entry Schedule**, selecione um catálogo para usar. Isso permite acessar dados, como produtos, descontos e promoções, para direcionar ainda mais seus usuários.
- Em **Target Audience (Público alvo)**, adicione um segmento para direcionar os usuários que indicaram interesse em um determinado item.
- Nas etapas de mensagens em todo o Canva, atualize o Liquid para fazer referência ao seu catálogo.

{% endtab %}
{% tab Adoção de recursos %}

Envie mensagens personalizadas em tempo hábil para destacar os benefícios e as dicas de uso. Considere o seguinte ao usar este modelo:

- Excluir usuários que já tenham usado o produto. Por exemplo, em **Público-alvo**, adicione um filtro em 
-  Para usar a etapa da jornada experimental, defina um evento de conversão. Esse evento deve ser o evento que sinaliza a adoção do recurso.
- Configure a etapa da jornada de ação no modelo com eventos personalizados para "Recurso ativado" e "Tour realizado".
- Configure os atributos personalizados na etapa de mensagens denominada "Pesquisa de feedback" para capturar o sentimento do feedback.

{% endtab %}
{% tab Usuários inativos %}

Traga os usuários de volta ao seu app com incentivos baseados em seus engajamentos anteriores. Considere o seguinte ao usar este modelo:

- Em **Basics**, selecione um app específico para rastrear conversões.
- No editor do Canva, adicione aplicativos específicos para as etapas das jornadas de ação.
- Configure a etapa Audience Sync com os parceiros e públicos para seu caso de uso.

{% endtab %}
{% tab Integração %}

Crie jornadas de integração que promovam uma forte adoção inicial e incentivem relacionamentos duradouros com seus usuários. Considere o seguinte ao usar este modelo:

- Na etapa Jornadas do público denominada "Audience Split" (Divisão do público), considere a possibilidade de personalizar as principais ações para usuários engajados. No modelo, o filtro de segmento é "Has clicked e-mail for step Welcome Email".

{% endtab %}
{% tab Feedback pós-compra %}

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

## Gerenciando modelos do Canvas

Os modelos do Canvas podem ser duplicados e arquivados, de forma semelhante a um Canvas real. Para editar um modelo de canva, selecione o modelo e, em seguida, **<i class="fas fa-pencil-alt"></i>Editar**.

No nível do espaço de trabalho, é possível atualizar as permissões de usuário para permitir ou limitar o acesso para criar, editar, visualizar ou arquivar modelos do Canva.

### Permissões para equipes e espaços de trabalho

Para permitir que apenas determinados usuários acessem e usem modelos específicos do Canvas, [adicione uma equipe]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) aos modelos e atribua permissões de "Access Campaigns, Canvas, Content Cards, Content Blocks, Feature Flags, Segments, Media Library e Central de Preferências" no nível da equipe.

Se atribuir qualquer uma das seguintes permissões no nível da equipe, mas não no nível do espaço de trabalho, só poderá fazer o seguinte atribuído à sua equipe:

- Criar e editar modelos do Canvas
- Veja os modelos do Canvas
- Arquivar modelos do Canvas

Se as permissões forem concedidas no nível do espaço de trabalho e das equipes, as permissões no nível do espaço de trabalho serão priorizadas.

## Perguntas frequentes

### Posso salvar uma etapa incompleta em um modelo do Canva?

Sim, você pode salvar etapas incompletas como um modelo do Canva. Entretanto, quando o modelo for usado, haverá um erro no botão **Salvar modelo** que indica o que é necessário para iniciar o canva.

### Posso salvar minhas configurações do Construtor de canvas como um modelo ou só posso salvar etapas? 

Sim, você pode salvar as configurações no construtor do Canvas em um modelo do Canvas. Por exemplo, se você planeja usar uma combinação de segmentos e filtros com frequência, pode salvar essas configurações de **público-alvo** como parte do modelo do Canva.

