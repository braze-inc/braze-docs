---
nav_title: Adoção de Recursos
article_title: Adoção de Recursos
page_order: 3
page_type: reference
description: "Este artigo descreve como usar um modelo de canva Braze para enviar mensagens personalizadas em tempo hábil para destacar os benefícios e dicas de uso."
tool: Canvas
---

# Adoção de recursos

> Este modelo é projetado para impulsionar o uso de seus novos recursos, produtos existentes, ofertas adicionais ou qualquer outra área que você gostaria que seus clientes experimentassem. Ao aproveitar a comunicação personalizada e um conjunto estruturado de mensagens, você pode apresentar novas funcionalidades aos usuários de forma fluida e obter feedback valioso deles. 

Neste artigo, vamos guiá-lo por um caso de uso para o Modelo de **Adoção de Funcionalidades**, que é destinado às etapas de retenção e fidelidade do ciclo de vida do usuário. Após este artigo, você terá personalizado uma jornada do usuário que incentiva os usuários a utilizarem novos recursos e coleta o sentimento do usuário.

## Pré-requisitos

Para usar com sucesso este modelo, você precisará de um [evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) que faça referência a quando os usuários usaram o recurso.

## Adaptar o modelo às suas necessidades

Vamos supor que você trabalhe na Calorie Rocket, um app de entrega de comida, que recentemente lançou o Cruise Control, um recurso para agendar entregas de comida recorrentes, e você quer incentivar mais usuários a adotar esse novo recurso. No nosso exemplo, usaremos o evento personalizado `scheduled_delivery` para rastrear quando os usuários tentaram o recurso de Controle de Cruzeiro.

Para acessar o modelo de volta ao estoque, ao criar um novo canva, selecione **Usar um modelo de canva** > **Modelos de Braze**. Em seguida, ao lado de **Adoção de Recursos**, selecione **Aplicar Modelo**. Agora, podemos examinar o modelo para adequá-lo às nossas necessidades.

### Etapa 1: Configurar os detalhes

Vamos ajustar os detalhes do Canva para refletir nosso objetivo.

1. Selecione **Editar** ao lado do nome do modelo.

![O título e a descrição atuais do Canva.]({% image_buster /assets/img/canvas_templates/feature_adoption/select_edit_details.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Atualize o canva para especificar que o canva é para direcionamento de usuários para coletar feedback dos usuários.
3\. Atualize a descrição para especificar que o canva é para incentivar os usuários a enviar feedback e acompanhar o sentimento dos usuários em relação ao novo recurso de Controle de Cruzeiro.
4\. Adicione a tag **Feature adoption** para que possamos filtrá-la na página inicial do canva.

![O novo nome e descrição para o canva. A nova descrição afirma: Uma adoção de canva para rastrear a adoção e o sentimento do usuário para o Controle de Cruzeiro, uma funcionalidade para agendar entregas de alimentos recorrentes.]({% image_buster /assets/img/canvas_templates/feature_adoption/enter_new_canvas_name.png %}){: style="max-width:60%;"}

### Etapa 2: Atribuir um evento de conversão

Em seguida, vamos adicionar um evento de conversão para nosso canva para sinalizar a adoção de recursos. Isso nos permitirá personalizar a jornada experimental em nossa experiência do usuário mais tarde.

1. Em **atribuir Eventos de Conversão**, selecione **Adicionar Evento de Conversão**.
2. Em **Evento de Conversão Primária - A**, selecione **Executa Evento Personalizado** como o **tipo de evento de conversão**.
3. Selecione nosso evento personalizado `scheduled_delivery`.
4. Manteremos o prazo de conversão em três dias.

![A janela de evento de conversão no canva.]({% image_buster /assets/img/canvas_templates/feature_adoption/assign_conversion_event_cruise_control.png %}){: style="max-width:90%;"}

### Etapa 3: Ajustar o cronograma de entrada

Nosso objetivo é incentivar nossos usuários a adotarem o Controle de Cruzeiro, mas não queremos que nosso envio de mensagens seja muito frequente. Então, manteremos este canva como uma entrega agendada e faremos os seguintes ajustes na seção **Opções Baseadas em Tempo**.

1. Atualizar **Frequência de Entrada** para **Semanal**.
2. Mantenha a recorrência como está.
3. Selecione **Mon** para direcionar usuários no início da semana.
4. Selecione o horário de início para o canva.
5. Atualize os **parâmetros de término** para encerrar o canva no último dia do ano.

Vamos manter a opção de permitir que os usuários entrem no canva em seu fuso local.

### Etapa 4: Selecione o público-alvo

Agora, vamos definir nosso público-alvo atualizando os seguintes detalhes no modelo:

1. Selecione o segmento **Todos os Usuários**.
2. Remova os filtros adicionais do modelo. 
3. Crie este filtro usando nosso evento personalizado: `Has scheduled_delivery for exactly 0 times`. Isso nos permite excluir usuários que já usaram o recurso de entrar em nosso canva.

![O segmento para todos os usuários que não usaram o Cruise Control.]({% image_buster /assets/img/canvas_templates/feature_adoption/cruise_control_segment.png %}){: style="max-width:90%;"}

{: start="4"}
4\. Tendo em mente que o Calorie Rocket anteriormente permitiu que alguns usuários testassem em beta a nova funcionalidade Controle de Cruzeiro, atualizaremos os critérios de saída para excluir esses usuários de entrar no canva.

### Etapa 5: Selecione suas configurações de envio

Manteremos as configurações de inscrição padrão, então enviaremos apenas para usuários que se inscreveram ou optaram por receber mensagens ou notificações, e pularemos as outras configurações (limitação de frequência, horário de silêncio e grupos de semente).

### Etapa 6: Personalize sua tela

#### Construa a jornada de Ação

Em seguida, vamos construir a primeira etapa da jornada de Ação, que tem como objetivo indicar se nossos usuários têm interesse no novo recurso. Faremos os seguintes ajustes no modelo:

1. Como a funcionalidade de Controle de Cruzeiro só está disponível após um pedido ter sido adicionado a um carrinho, nomearemos o primeiro grupo de ações **Adicionado ao carrinho** e selecionaremos `added_to_cart` para o evento personalizado.

![O nome do grupo de ações definido como "Adicionado ao carrinho" e o "Executar Evento Personalizado" definido como "adicionado_ao_carrinho".]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_added_to_cart.png %}){: style="max-width:60%;"}

{: start="2"}
2\. Mantenha o segundo grupo de ações **Taken Tour** como está, pois queremos avaliar se os usuários fizeram um tour pelo app, e se o fizeram, então avançarão para a segunda jornada.
3\. Para a Ação subsequente Jornada chamada **Assess Usage**, substitua **Used Feature >3x** por **Viewed Cruise Control settings**.
4\. Selecione o **Executar Evento Personalizado** dropdown, em seguida selecione `scheduled_delivery` para o evento personalizado.

![O nome do grupo de ações definido como 'Recurso Usado >3x' e o 'Executar Evento Personalizado' definido como 'entrega_agendada'.]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_assess_usage.png %}){: style="max-width:60%;"}

#### Configurar pesquisa de feedback

Em seguida, iremos acessar a etapa da Mensagem chamada **Feedback Survey** para incluir nossa pesquisa de feedback para que nossos usuários possam preencher após usar o Cruise Control pela primeira vez. As opções de resposta da nossa pesquisa para nossos usuários são:

- **Amei!**
- **Não é para mim.**

1. Para as duas opções da pesquisa, selecione **Feedback de Experiência** como nosso atributo personalizado para capturar e rastrear feedback sobre o Controle de Cruzeiro. Este atributo personalizado terá dois valores para representar as respostas da pesquisa (`good` e `bad`).
2. Atualize os valores dos atributos para corresponder às opções da pesquisa. Isso nos permitirá acompanhar a resposta de um usuário.

### Etapa 7: Teste e inicie seu Canva

Depois de testar e revisar nosso Canvas para garantir que ele funcione conforme o esperado, selecione **Launch Canvas** para iniciar o Canvas. Agora, podemos direcionar os usuários com uma jornada personalizada para incentivá-los a adotar nosso novo recurso Controle de Cruzeiro.

{% alert tip %}
Confira nossa [lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber o que considerar antes e depois de lançar um Canva.
{% endalert %}
