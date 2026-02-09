---
nav_title: Criar um modelo do Canvas
article_title: Criar um modelo de tela
alias: "/canvas_templates/"
page_order: 0.5
description: "Este artigo de referência aborda como criar um modelo para o Canva."
page_type: reference
---

# Criar um modelo do Canvas

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
Se estiver usando a navegação mais antiga, poderá encontrar essa página em **Engajamento** > **Modelos & Media** > Canvas Templates.
{% endalert %}

### Etapa 2: Criar um novo modelo

Selecione **Criar modelo** e comece a configurar os detalhes do Canva. Você pode começar dando um nome ao seu modelo do Canva.

![Um exemplo de modelo de canva chamado "Modelo de canva de venda anual" com a descrição "Use para a promoção anual de primavera".]({% image_buster /assets/img/canvas_template_example.png %})

### Etapa 3: Personalize seu modelo

Em seguida, personalize seu modelo configurando [o Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2-set-up-your-canvas). É possível decidir quando os usuários devem entrar no Canvas, determinar quais usuários podem entrar nesse Canvas, ajustar as configurações de envio e criar a jornada do usuário para o modelo.

### Etapa 4: Salve seu modelo

Depois de terminar de personalizar seu modelo, selecione o botão **Salvar modelo**. Na página **do modelo do Canvas**, você pode visualizar os detalhes do modelo do Canvas selecionando <i class="fas fa-list"></i> **Detalhes do modelo**. 

## Uso de modelos do Canvas

Há duas maneiras de usar seu modelo ao criar um canva:

- **Do envio de mensagens**: Acesse **Envio de mensagens** > **Canva**. Selecione o botão **Create Canvas** e **Use a Canvas Template**.
- **Dos modelos**: Acesse **Modelos** > **Modelos de tela** e localize o modelo desejado. Em seguida, selecione o menu <i class="fas fa-ellipsis-vertical"></i> seguido de **Apply template (Aplicar modelo**). Isso levará você a um novo canva com o modelo aplicado no criador de canvas.

### Modelos de Braze disponíveis

Para obter uma lista dos modelos disponíveis do Canvas, consulte [Modelos do Canvas]({{site.baseurl}}/canvas_templates/templates/). Para obter detalhes sobre o uso dos modelos do eCommerce Canva, consulte [Como usar os eventos recomendados para comércio eletrônico]({{site.baseurl}}/ecommerce_use_cases/).

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

