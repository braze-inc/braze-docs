---
nav_title: Onboarding
article_title: Onboarding
page_order: 5
page_type: reference
description: "Este artigo descreve como usar um modelo do Braze Canvas para criar jornadas de integração que promovam uma forte adoção inicial e incentivem relacionamentos duradouros com seus usuários."
tool: Canvas
---

# Onboarding

> Comece a jornada de seus usuários com este modelo de integração. Este modelo foi projetado para promover uma forte adoção inicial e incentivar relacionamentos duradouros com seus usuários. Ao aproveitar a comunicação personalizada e um conjunto estruturado de mensagens, é possível apresentar perfeitamente os usuários à sua marca e iniciar o começo de um relacionamento duradouro.

Neste artigo, vamos orientá-lo em um caso de uso do modelo **Onboarding**, que se destina ao estágio de consideração do ciclo de vida do usuário, para criar uma jornada de integração perfeita para novos usuários. Após este artigo, você terá personalizado esse modelo do Braze Canvas com mensagens personalizadas para esses novos usuários.

## Pré-requisitos

Antes de usar esse modelo, você precisa criar os seguintes [modelos de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template) para fazer referência no Canva:

- Um e-mail de boas-vindas para todos os usuários do seu app
- Um e-mail com dicas sobre como usar seu app
- Um e-mail de feedback que inclui uma pesquisa com o usuário

## Adaptar o modelo às suas necessidades

Digamos que estejamos trabalhando na PantsLabyrinth e nosso objetivo seja aumentar o engajamento do usuário, criar confiança e fidelidade com nossos usuários e incentivá-los a permanecer engajados. Para isso, queremos nos concentrar no envio de mensagens direcionadas a novos usuários que ainda não interagiram com o app.

Para acessar o modelo de integração, ao criar um novo Canvas, selecione **Usar um modelo do Canvas** > **Modelos do Braze**. Em seguida, ao lado de **Integração**, selecione **Aplicar modelo**. Vamos começar a personalizar esse modelo para se adequar ao nosso caso de uso.

### Etapa 1: Configurar os detalhes

Vamos ajustar os detalhes do Canva para refletir nosso objetivo.

1. Selecione **Editar** ao lado do nome do modelo.

![O título e a descrição atuais do Canva.]({% image_buster /assets/img/canvas_templates/onboarding_old_name_description.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Atualize o nome do Canvas para especificar que o Canvas é para integração de novos usuários.
3\. Atualize a descrição para especificar que o Canva mapeia uma jornada do usuário que promove a confiança e a fidelidade dos usuários.
4\. Adicione a tag **Integração** para que possamos filtrá-la na página inicial do Canva.

![O novo nome, a descrição e a tag do Canva.]({% image_buster /assets/img/canvas_templates/onboarding_new_name_description.png %}){: style="max-width:60%;"}

### Etapa 2: Atribua seus eventos de conversão

Em seguida, vamos atribuir nossos eventos de conversão. Os eventos de conversão são um tipo de métrica que pode ser usada para medir o sucesso do Canva. Para **Nome do evento personalizado**, selecione **Clique de e-mail** como o evento personalizado.

![Evento de conversão primária - Um evento com o tipo de conversão "Realiza evento personalizado" com o nome de evento personalizado "Envio de e-mail". Há um prazo de conversão de 4 dias.]({% image_buster /assets/img/canvas_templates/onboarding1.png %})

Isso significa que os novos usuários têm até quatro dias para clicar no e-mail de boas-vindas. Nesse caso, queremos que nossos novos usuários tenham um senso de urgência para se engajarem no PantsLabyrinth e assinarem uma entrega recorrente de roupas sazonais.

### Etapa 3: Definir uma programação de entrada

Como o objetivo é direcionar novos usuários do PantsLabyrinth, manteremos o Canva baseado em ações. Para **Iniciar sessão**, selecione **Iniciar sessão em qualquer app** para permitir que os usuários que iniciarem uma sessão em qualquer app entrem no Canva.

Em seguida, ajuste a **Entry Window (Janela de entrada)** para determinar quando os usuários podem entrar no Canva. Digamos que haja um lançamento de inscrição no PantsLabyrinth no final de outubro. É aqui que definiremos o horário de início como **2024/10/28 8:00 am**. Opcionalmente, também podemos permitir que os usuários insiram o Canva em seu fuso local.

![Uma janela de entrada com horário de início em 28 de outubro de 2024, às 8 horas. Os usuários digitarão essa mensagem em seu fuso local.]({% image_buster /assets/img/canvas_templates/onboarding4.png %})

### Etapa 4: Direcionamento para seu público

Ao direcionar o público certo, podemos nos engajar efetivamente com novos usuários. Por exemplo, esse modelo direciona todos os usuários que usaram um app pela primeira vez há menos de um dia, o que é preciso para o nosso caso de uso. Portanto, deixaremos essa seção como está.

### Etapa 5: Definir configurações de envio

Por padrão, esse Canva é enviado aos usuários inscritos ou com aceitação e segue as regras de limite de frequência. Manteremos essas configurações como estão.

### Etapa 6: Personalize sua tela

Agora, vamos criar o Canva personalizando as etapas do modelo.

#### Configure o e-mail de boas-vindas

1. Selecione a etapa da mensagem chamada "Welcome Email" (E-mail de boas-vindas).
2. Selecione **Editar mensagem** para substituir o e-mail do modelo pelo nosso e-mail de boas-vindas.
3. Selecione **Concluído**.

Agora, nossos usuários receberão esse e-mail de boas-vindas depois de iniciarem uma sessão em nosso app. Para não sobrecarregar os usuários com envios repetidos de mensagens, recomendamos usar a etapa de postergação como parte da jornada do usuário.

#### Personalizar a jornada do público

Na etapa da jornada do público denominada **Audience Split (Divisão do público)**, podemos personalizar o filtro para nossos usuários engajados. No modelo, o filtro é **Tem e-mail clicado para a etapa E-mail de boas-vindas**, o que significa que os usuários são divididos em dois grupos: usuários que clicaram no e-mail de boas-vindas e aqueles que não clicaram.

![Uma etapa de divisão de público com uma jornada para usuários engajados e outra para todos os outros.]({% image_buster /assets/img/canvas_templates/onboarding2.png %}){: style="max-width:70%;"}

Como varejista on-line de roupas, a PantsLabyrinth também tem um grupo ativo de usuários móveis. Portanto, em uma tela de integração separada, também podemos selecionar o seguinte filtro para identificar e dividir nossos usuários móveis nesses segmentos:

- **Clicou no cartão de conteúdo para a etapa Cartão de conteúdo de boas-vindas**
- **Restante do público**

#### Direcionamento para mais usuários com as jornadas do público

A partir do conjunto de usuários que não interagiram com nosso app, podemos direcionar ainda mais esses usuários editando a etapa "Check for Clicks" e a etapa "Winback Nudge".

### Etapa 7: Teste e inicie seu Canva

Depois de testar e revisar nosso Canvas para garantir que ele funcione conforme o esperado, selecione **Launch Canvas** para iniciar o Canvas. Agora, podemos oferecer aos nossos novos usuários uma experiência de integração personalizada para incentivar um relacionamento duradouro!

{% alert tip %}
Confira nossa [lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber o que considerar antes e depois de lançar um Canva.
{% endalert %}

