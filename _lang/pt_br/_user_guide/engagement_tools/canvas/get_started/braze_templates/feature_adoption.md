---
nav_title: Adoção de recursos
article_title: Adoção de recursos
page_order: 3
page_type: reference
description: "Este artigo descreve como usar um modelo do Braze Canvas para enviar mensagens personalizadas em tempo hábil para destacar os benefícios e as dicas de uso."
tool: Canvas
---

# Adoção de recursos

> Esse modelo foi projetado para impulsionar o uso de seus novos recursos, produtos existentes, ofertas adicionais ou qualquer outra área que você gostaria que seus clientes experimentassem. Ao aproveitar a comunicação personalizada e um conjunto estruturado de mensagens, é possível apresentar novos recursos aos usuários e obter feedback valioso deles. 

Neste artigo, vamos orientá-lo em um caso de uso do modelo **Adoção de recursos**, que se destina aos estágios de retenção e fidelidade do ciclo de vida do usuário. Após este artigo, você terá personalizado uma jornada de usuário que incentiva os usuários a usar novos recursos e coleta o sentimento do usuário.

## Pré-requisitos

Para usar esse modelo com êxito, você precisará de um [evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) que faça referência a quando os usuários usaram o recurso.

## Adaptar o modelo às suas necessidades

Digamos que você trabalhe na Calorie Rocket, um aplicativo de entrega de alimentos, que lançou recentemente o Cruise Control, um recurso para agendar entregas recorrentes de alimentos, e você quer incentivar mais usuários a adotar esse novo recurso. Em nosso exemplo, usaremos o evento personalizado `scheduled_delivery` para rastrear quando os usuários experimentaram o recurso Cruise Control.

Para acessar o modelo em estoque, ao criar um novo Canvas, selecione **Usar um modelo de Canvas** > **Modelos de brasagem**. Em seguida, ao lado de **Feature Adoption**, selecione **Apply Template (Aplicar modelo**). Agora, podemos examinar o modelo para adequá-lo às nossas necessidades.

### Etapa 1: Configurar os detalhes

Vamos ajustar os detalhes do Canvas para refletir nosso objetivo.

1. Selecione **Editar** ao lado do nome do modelo.

\![O título e a descrição atuais do Canvas.]({% image_buster /assets/img/canvas_templates/feature_adoption/select_edit_details.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Atualize o nome do Canvas para especificar que o Canvas é para direcionar usuários para coletar feedback do usuário.
3\. Atualize a descrição para especificar que o Canvas serve para incentivar os usuários a enviar feedback e acompanhar a opinião dos usuários sobre o novo recurso Cruise Control.
4\. Adicione a tag **Feature adoption** para que possamos filtrá-la na página inicial do Canvas.

\![O novo nome e a descrição do Canvas. A nova descrição indica: Um Canvas de adoção de recursos para rastrear a adoção e o sentimento dos usuários em relação ao Cruise Control, um recurso para agendar entregas recorrentes de alimentos.]({% image_buster /assets/img/canvas_templates/feature_adoption/enter_new_canvas_name.png %}){: style="max-width:60%;"}

### Etapa 2: Atribuir um evento de conversão

Em seguida, vamos adicionar um evento de conversão ao nosso Canvas para sinalizar a adoção do recurso. Isso nos permitirá personalizar o Caminho do Experimento em nossa jornada do usuário posteriormente.

1. Em **Assign Conversion Events (Atribuir eventos de conversão**), selecione **Add Conversion Event (Adicionar evento de conversão**).
2. Em **Primary Conversion Event - A**, selecione **Performs Custom Event** como o **tipo de evento de conversão**.
3. Selecione nosso evento personalizado `scheduled_delivery`.
4. Manteremos o prazo de conversão em três dias.

\![A janela do evento de conversão no Canvas.]({% image_buster /assets/img/canvas_templates/feature_adoption/assign_conversion_event_cruise_control.png %}){: style="max-width:90%;"}

### Etapa 3: Adaptar o cronograma de entrada

Nosso objetivo é incentivar nossos usuários a adotar o Cruise Control, mas não queremos que nossas mensagens sejam muito frequentes. Portanto, manteremos esse Canvas como uma entrega programada e faremos os seguintes ajustes na seção **Time-Based Options**.

1. Atualize **a frequência de entrada** para **semanal**.
2. Mantenha a recorrência como está.
3. Selecione **Mon** para segmentar os usuários no início da semana.
4. Selecione o horário de início do nosso Canvas.
5. Atualize os **parâmetros de término** para encerrar o Canvas no último dia do ano.

Manteremos a opção de permitir que os usuários insiram o Canvas em seu fuso horário local.

### Etapa 4: Selecione o público-alvo

Agora, vamos configurar nosso público-alvo atualizando os seguintes detalhes no modelo:

1. Selecione o segmento **Todos os usuários**.
2. Remova os filtros adicionais do modelo. 
3. Crie esse filtro usando nosso evento personalizado: `Has scheduled_delivery for exactly 0 times`. Isso nos permite excluir usuários que já usaram o recurso de entrar em nosso Canvas.

\![O segmento para todos os usuários que não usaram o Cruise Control.]({% image_buster /assets/img/canvas_templates/feature_adoption/cruise_control_segment.png %}){: style="max-width:90%;"}

{: start="4"}
4\. Tendo em mente que o Calorie Rocket permitiu anteriormente que alguns usuários fizessem o teste beta do novo recurso Cruise Control, atualizaremos os critérios de saída para excluir esses usuários do Canvas.

### Etapa 5: Selecione suas configurações de envio

Manteremos as configurações de assinatura padrão, para que enviemos apenas aos usuários que se inscreveram ou optaram por receber mensagens ou notificações, e ignoraremos as outras configurações (limite de frequência, horas de silêncio e grupos de sementes).

### Etapa 6: Personalize seu Canvas

#### Crie o caminho da ação

Em seguida, vamos criar a primeira etapa do Caminho de Ação, que tem como objetivo indicar se os usuários têm interesse no novo recurso. Faremos os seguintes ajustes no modelo:

1. Como o recurso Cruise Control só está disponível depois que um pedido é adicionado a um carrinho, nomearemos o primeiro grupo de ações como **Added to cart (Adicionado ao carrinho** ) e selecionaremos `added_to_cart` para o evento personalizado.

\![O nome do grupo de ação definido como "Added to cart" (Adicionado ao carrinho) e "Perform Custom Event" (Executar evento personalizado) definido como "added_to_cart".]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_added_to_cart.png %}){: style="max-width:60%;"}

{: start="2"}
2\. Mantenha o segundo grupo de ações **Taken Tour** como está, pois queremos avaliar se os usuários fizeram um tour pelo aplicativo e, se tiverem feito, eles avançarão para o segundo caminho.
3\. Para o Caminho de ação subsequente denominado **Avaliar uso**, substitua **Recurso usado >3x** por **Configurações de controle de cruzeiro visualizadas**.
4\. Selecione o menu suspenso **Perform Custom Event (Executar evento personalizado** ) e, em seguida, selecione `scheduled_delivery` para o evento personalizado.

\![O nome do grupo de ação definido como "Recurso usado >3x" e a opção "Executar evento personalizado" definida como 'scheduled_delivery'.]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_assess_usage.png %}){: style="max-width:60%;"}

#### Configure a pesquisa de feedback

Em seguida, iremos para a etapa Message (Mensagem) chamada **Feedback Survey (Pesquisa de feedback** ) para incluir nossa pesquisa de feedback para os usuários preencherem depois de usar o Cruise Control pela primeira vez. As opções de resposta da pesquisa para nossos usuários são:

- **Adorei!**
- **Não para mim.**

1. Para as duas opções de pesquisa, selecione **Experience Feedback** como nosso atributo personalizado para capturar e rastrear o feedback sobre o Cruise Control. Esse atributo personalizado terá dois valores para representar as respostas da pesquisa (`good` e `bad`).
2. Atualize os valores dos atributos para que correspondam às opções da pesquisa. Isso nos permitirá rastrear a resposta de um usuário.

### Etapa 7: Teste e inicie seu Canvas

Depois de testar e revisar nosso Canvas para garantir que ele funcione conforme o esperado, selecione **Launch Canvas** para iniciar o Canvas. Agora, podemos direcionar os usuários com uma jornada de usuário personalizada para incentivá-los a adotar nosso novo recurso Cruise Control.

{% alert tip %}
Confira nossa [lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber o que considerar antes e depois de lançar um Canvas.
{% endalert %}
