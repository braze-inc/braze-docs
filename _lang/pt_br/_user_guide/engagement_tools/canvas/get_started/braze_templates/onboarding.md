---
nav_title: Integração
article_title: Integração
page_order: 5
page_type: reference
description: "Este artigo descreve como usar um modelo de Canvas da Braze para criar jornadas de integração que promovem uma forte adoção inicial e incentivam relacionamentos duradouros com seus usuários."
tool: Canvas
---

# Integração

> Comece a jornada dos seus usuários com este modelo de integração. Este modelo é projetado para promover uma forte adoção inicial e incentivar relacionamentos duradouros com seus usuários. Ao aproveitar a comunicação personalizada e um conjunto estruturado de mensagens, você pode apresentar seus usuários à sua marca e iniciar o começo de um relacionamento duradouro.

Neste artigo, vamos guiá-lo por um caso de uso do modelo **Integração**, que é destinado à fase de consideração do ciclo de vida do usuário, para criar uma jornada de integração perfeita para novos usuários. Após este artigo, você terá personalizado este modelo de Canvas da Braze com mensagens personalizadas para esses novos usuários.

## Pré-requisitos

Antes de usar este modelo, você precisa criar os seguintes [modelos de email]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template) para referência no Canvas:

- Um email de boas-vindas para todos os usuários do seu aplicativo
- Um email com dicas sobre como usar seu aplicativo
- Um email de feedback que inclui uma pesquisa de usuário

## Personalizando o modelo para suas necessidades

Vamos supor que estamos trabalhando na PantsLabyrinth, e nosso objetivo é aumentar o engajamento do usuário, construir confiança e lealdade com nossos usuários e incentivá-los a permanecer engajados. Para isso, queremos nos concentrar em criar mensagens que visem novos usuários que ainda não interagiram com o aplicativo.

Para acessar o modelo de integração, ao criar um novo Canvas, selecione **Usar um modelo de Canvas** > **Modelos da Braze**. Em seguida, ao lado de **Integração**, selecione **Aplicar Modelo**. Vamos começar a personalizar este modelo para se adequar ao nosso caso de uso.

### Passo 1: Configure os detalhes

Vamos ajustar os detalhes do Canvas para refletir nosso objetivo.

1. Selecione **Editar** ao lado do nome do modelo.

\![O título e a descrição atuais do Canvas.]({% image_buster /assets/img/canvas_templates/onboarding_old_name_description.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Atualize o nome do Canvas para especificar que o Canvas é para a integração de novos usuários.
3\. Atualize a descrição para especificar que o Canvas mapeia uma jornada do usuário que promove confiança e lealdade com os usuários.
4\. Adicione a tag **Integração** para que possamos filtrá-la na página inicial do Canvas.

\![O novo nome, descrição e tag para o Canvas.]({% image_buster /assets/img/canvas_templates/onboarding_new_name_description.png %}){: style="max-width:60%;"}

### Passo 2: Atribua seus eventos de conversão

Em seguida, vamos atribuir nossos eventos de conversão. Eventos de conversão são um tipo de métrica que pode ser usada para medir o sucesso do Canvas. Para **Nome do evento personalizado**, selecione **Clique no Email** como o evento personalizado.

\![Evento de Conversão Primário - A com o tipo de conversão "Executa Evento Personalizado" com o nome do evento personalizado "Clique no Email". Há um prazo de conversão de 4 dias.]({% image_buster /assets/img/canvas_templates/onboarding1.png %})

Isso significa que novos usuários têm até quatro dias para clicar no email de boas-vindas. Neste caso, queremos que nossos novos usuários sintam um senso de urgência para se envolver com o PantsLabyrinth e assinar uma entrega recorrente de roupas sazonais.

### Passo 3: Defina um cronograma de entrada

Como o objetivo é direcionar novos usuários do PantsLabyrinth, manteremos o Canvas baseado em ações. Para **Iniciar Sessão**, selecione **Iniciar Sessão em Qualquer Aplicativo** para permitir que usuários que iniciam uma sessão em qualquer aplicativo entrem no Canvas.

Em seguida, ajuste a **Janela de Entrada** para determinar quando os usuários podem entrar no Canvas. Digamos que haverá um lançamento de assinatura do PantsLabyrinth no final de outubro. Aqui é onde definiremos o horário de início como **2024/10/28 8:00 am**. Opcionalmente, também podemos permitir que os usuários entrem no Canvas em seu fuso horário local.

\![Uma janela de entrada com o horário de início 28 de outubro de 2024 às 8 da manhã. Os usuários inserirãom essa mensagem em seu fuso horário local.]({% image_buster /assets/img/canvas_templates/onboarding4.png %})

### Passo 4: Direcione seu público

Ao direcionar o público certo, podemos nos envolver efetivamente com novos usuários. Por exemplo, este modelo direciona todos os usuários que usaram um aplicativo pela primeira vez há menos de um dia, o que é preciso para nosso caso de uso. Portanto, deixaremos esta seção como está.

### Passo 5: Defina as configurações de envio

Como padrão, este Canvas é enviado para usuários que estão inscritos ou optaram por participar e segue as regras de limitação de frequência. Manteremos essas configurações como estão.

### Passo 6: Personalize seu Canvas

Agora, vamos construir o Canvas personalizando as etapas do modelo.

#### Configure o e-mail de boas-vindas

1. Selecione a etapa Mensagem chamada "E-mail de Boas-Vindas".
2. Selecione **Editar mensagem** para substituir o e-mail do modelo pelo nosso e-mail de boas-vindas.
3. Selecione **Concluído**.

Agora, nossos usuários receberão este e-mail de boas-vindas após iniciarem uma sessão em nosso aplicativo. Para não sobrecarregar os usuários com mensagens repetidas, recomendamos usar a etapa de Atraso como parte da jornada do usuário.

#### Personalize o Caminho do Público

Na etapa Caminho do Público chamada **Corte de Público**, podemos personalizar o filtro para nossos usuários engajados. No modelo, o filtro é **Teve clique no e-mail para a etapa E-mail de Boas-Vindas**, o que significa que os usuários são divididos em dois grupos: usuários que clicaram no e-mail de boas-vindas e aqueles que não clicaram.

\![Uma etapa de Corte de Público com um caminho para usuários engajados e um caminho para todos os outros.]({% image_buster /assets/img/canvas_templates/onboarding2.png %}){: style="max-width:70%;"}

Como um varejista de roupas online, a PantsLabyrinth também possui um grupo ativo de usuários móveis. Portanto, em um Canvas de integração separado, também podemos selecionar o seguinte filtro para identificar e dividir nossos usuários móveis nesses segmentos:

- **Teve clique no cartão de conteúdo para a etapa Cartão de Conteúdo de Boas-Vindas**
- **Todos os Outros**

#### Alcance mais usuários com Caminhos de Público

Do conjunto de usuários que não interagiram com nosso aplicativo, podemos direcionar ainda mais esses usuários editando a etapa "Verificar Cliques" e a etapa "Empurrão de Retorno".

### Etapa 7: Teste e lance seu Canvas

Após testar e revisar nosso Canvas para garantir que funcione como esperado, selecione **Iniciar Canvas** para lançar o Canvas. Agora, podemos oferecer aos nossos novos usuários uma experiência de integração personalizada para incentivar um relacionamento duradouro!

{% alert tip %}
Confira nossa [Lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para coisas a considerar antes e depois de lançar um Canvas.
{% endalert %}

