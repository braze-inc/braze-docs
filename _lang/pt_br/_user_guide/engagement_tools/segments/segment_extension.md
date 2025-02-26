---
nav_title: Extensões de segmento
article_title: Extensões de segmento
page_order: 3.1

page_type: tutorial
description: "Este artigo de instruções irá guiá-lo sobre como configurar e usar uma extensão de segmento para aprimorar suas capacidades de segmentação."
tool: Segments
---

# Extensões de segmento

> A segmentação do Braze permite que você direcione os usuários com base no evento personalizado ou no comportamento de compra armazenado durante a vida útil desse perfil de usuário. Exemplos incluem encontrar usuários que realizaram ou não um determinado evento personalizado desde um momento específico, ou segmentar usuários com base em quais produtos eles já compraram ou quanto dinheiro gastaram com seu serviço.

Extensões de segmento são definições de público que permitem usar propriedades de eventos aninhados ou criar agregações em janela de propriedades de eventos personalizados e de compra nos últimos 2 anos (730 dias). Por exemplo, a segmentação da Braze permite encontrar usuários que compraram um produto específico em sua vida. Com extensões de segmento, você pode refinar ainda mais esse público para usuários que compraram uma cor específica de um produto específico pelo menos duas vezes nos últimos 2 anos. Ao criar uma extensão de segmento, você também pode especificar que o público seja estático ou regenerado diariamente.

O uso de propriedades de eventos aninhados para [entrega baseada em ação][19] não requer extensões de segmento, pois o processamento de eventos ocorre em tempo real. Atributos personalizados aninhados, da mesma forma, não exigem o uso de extensões de segmento.

{% alert important %}
Há uma alocação padrão de 25 extensões de segmento ativas por espaço de trabalho em um determinado momento. Se você precisar aumentar esse limite, entre em contato com seu gerente de sucesso do cliente da Braze para discutir seu caso de uso.
{% endalert %}

## Etapa 1: Navegue para extensões de segmento

Acesse **Público** > **Extensões de segmento**.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), poderá encontrar essa página em **Engajamento** > **Segmentos** > **Extensões de segmento**.
{% endalert %}

Na tabela de extensões de segmento, clique em **Criar nova extensão**, depois selecione sua experiência de criação de extensão de segmento:

- **Extensão simples:** Crie uma extensão de segmento focada em um único evento usando um formulário guiado.
Melhor para quando você não quer usar SQL.
- **Comece com um modelo:** Crie um segmento SQL com um modelo personalizável usando dados do Snowflake.
- **Atualização incremental:** Formule um segmento do Snowflake SQL que recarregue automaticamente os 2 últimos dias de dados ou faça um recarregamento manual conforme necessário. Ideal para equilibrar precisão e custo-benefício.
- **Atualização completa:** Formule um segmento do Snowflake SQL que recalcule todo o público com atualização manual. Ideal para quando você precisa ter uma visão completa e atualizada do seu público.

![][20]{: style="max-width:50%"}

Se você selecionar uma experiência que usa SQL, consulte [extensões de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) para mais informações.

Se você selecionar **Extensão simples**, continue com as etapas abaixo.

## Etapa 2: Nomeie sua extensão de segmento

Nomeie sua extensão de segmento descrevendo o tipo de usuários que você pretende filtrar. Isso garantirá que esta extensão possa ser facilmente e precisamente descoberta ao aplicá-la como um filtro em seu segmento.

![extensão de segmento nomeada "Extensão de Compradores Online - 90 Dias" com a caixa de seleção "Regenerar Extensão Diariamente" selecionada.][2]

## Etapa 3: Escolha seus critérios

Selecione entre critérios de compra, engajamento com mensagem ou evento personalizado para direcionamento. Depois de selecionar os critérios do tipo de evento desejado, escolha qual item comprado, interação de mensagem ou evento personalizado específico você gostaria de direcionar para sua lista de usuários. Em seguida, escolha quantas vezes (mais que, menos que ou igual a) o usuário precisaria ter concluído o evento e o período de tempo—para extensões de segmento especificamente, você pode voltar até os últimos 730 dias (2 anos).

A segmentação baseada em dados de eventos de mais de 730 dias pode ser feita usando outros filtros localizados em **Segmentos**. Ao escolher seu período de tempo, você pode especificar um intervalo de datas relativo (como os últimos X dias), uma data de início, uma data de término ou um intervalo de datas exato (data A a data B).

![][3]

### Segmentação de propriedade de evento

Para aumentar a precisão do direcionamento, selecione a caixa de seleção **Adicionar Filtros de Propriedade**. Isso permitirá que você se aprofunde com base nas propriedades específicas da sua compra ou evento personalizado. Apoiamos a segmentação de propriedades de eventos com base em string, numérico, booleano e objetos de tempo.

Para propriedades de string, você pode inserir vários valores de uma vez. No exemplo abaixo, este filtro procura usuários com status igual a qualquer um dos seguintes: ouro, prata ou bronze.

![Segmentando com base nas propriedades da string.][13.5]

![Segmentação com base em propriedades numéricas.][13]

![Segmentando com base em propriedades booleanas.][14]

![Segmentando com base em objetos datetime.][15]

Também suportamos segmentação com base em [propriedades de eventos aninhados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/nested_objects/).

![Segmentação com base em propriedades de eventos aninhados.][18]

As extensões de segmento dependem do armazenamento de longo prazo das propriedades do evento e não têm um limite de armazenamento de propriedades com carimbo de data/hora. Você pode olhar para trás nas propriedades de eventos rastreadas nos últimos dois anos.

{% alert note %}
O uso de propriedades de eventos dentro de extensões de segmento não impacta o uso de pontos de dados.
{% endalert %}

## Etapa 4: Designar configurações de atualização (opcional)

Se não precisar que sua extensão seja atualizada regularmente, você poderá salvá-la sem usar as configurações de atualização, e o Braze gerará sua extensão de segmento com base na associação do usuário naquele momento. Use o comportamento padrão se quiser gerar o público apenas uma vez e depois direcioná-lo com uma campanha única.

Seu segmento sempre começará a ser processado após o salvamento inicial. Sempre que seu segmento for atualizado, o Braze executará novamente o segmento e atualizará a associação do segmento para refletir os usuários em seu segmento no momento da atualização. Isso pode ajudar suas campanhas recorrentes a alcançar os usuários mais relevantes.

### Configuração de uma atualização recorrente

Para configurar uma agenda recorrente, selecione **Atualizar configurações** no canto superior direito de sua extensão específica. A opção de designar configurações de atualização está disponível para todos os tipos de extensões de segmento, incluindo segmentos SQL, segmentos CDI e extensões de segmento simples baseadas em formulário.

{% alert important %}
As configurações de atualização são automaticamente desativadas para extensões de segmento não utilizadas. A Braze define extensões não utilizadas como aquelas que atendem aos seguintes critérios:

- Não utilizada em nenhuma campanha ativa, canva ou segmento
- Não utilizada em nenhuma campanha inativa, canva ou segmento inativo (rascunho, interrompida ou arquivada)
- Sem modificação há mais de 7 dias

A Braze notificará o contato da empresa e quem criou a extensão quando essa configuração for desativada. A opção de regenerar extensões diariamente pode ser ativada novamente a qualquer momento.
{% endalert %}

#### Seleção de suas configurações de atualização

![Configurações de intervalo de atualização com uma frequência de atualização semanal, horário de início às 10h e segunda-feira selecionada como dia.][21]{: style="max-width:60%;"}

No painel **Refresh Settings (Configurações de atualização)**, você pode selecionar a frequência com que essa extensão de segmento será atualizada: por hora, diariamente, semanalmente ou mensalmente. Também será necessário selecionar o horário específico (que está no fuso horário da sua empresa) em que a atualização ocorrerá, como, por exemplo:

- Se você tiver uma campanha de envio de e-mail que é enviada todas as segundas-feiras às 11 horas, horário da empresa, e quiser garantir que seu segmento seja atualizado logo antes do envio, deverá escolher uma agenda de atualização semanal às 10 horas das segundas-feiras.
- Se quiser que seu segmento seja atualizado todos os dias, selecione a frequência de atualização diária e, em seguida, escolha a hora do dia para atualizar.

{% alert note %}
A capacidade de definir um cronograma de atualização por hora não está disponível para extensões de segmento baseadas em formulário (mas você pode definir cronogramas diários, semanais ou mensais).
{% endalert %}

### Consumo de crédito e custos adicionais

Como as atualizações executam novamente a consulta de seu segmento, cada atualização para segmentos SQL consumirá créditos de segmento SQL e cada atualização para segmentos CDI incorrerá em um custo em seu data warehouse de terceiros.

{% alert note %}
Os segmentos podem levar até 60 minutos para serem atualizados devido ao tempo de processamento dos dados. Os segmentos que estão atualmente em processo de atualização terão o status "Processing" (Processando) na lista de extensões de segmento. Isso tem algumas implicações:

- Para concluir o processamento de seu segmento antes de um horário específico, escolha um horário de atualização que seja 60 minutos antes. 
- Somente uma atualização pode ocorrer de cada vez em uma extensão de segmento específica. Se houver um conflito em que uma nova atualização seja iniciada quando uma atualização existente já tiver começado a ser processada, o Braze cancelará a nova solicitação de atualização e continuará o processamento em andamento.
{% endalert %}

## Etapa 5: Salve sua extensão de segmento

Depois de clicar em **Salvar**, sua extensão começará a processar. O tempo necessário para gerar sua extensão depende de quantos usuários você tem, quantos eventos personalizados ou eventos de compra você está capturando e quantos dias você está olhando para trás na história.

Enquanto sua extensão está processando, você verá uma pequena animação ao lado do nome da extensão e a palavra "Processando" na coluna **Último Processado** na lista de extensões. Observe que você não poderá editar uma extensão enquanto ela estiver em processamento.

![][5]

## Etapa 6: Use sua extensão em um segmento

Depois de criar uma extensão, você pode usá-la como um filtro ao criar um segmento ou definir um público para uma campanha ou canva. Comece escolhendo **extensão de segmento Braze** da lista de filtros na seção **Atributos do Usuário**.

![][6]

Na lista de filtros da extensão de segmento do Braze, escolha a extensão que deseja incluir ou excluir neste segmento.

![][7]

Para visualizar os critérios de extensão, clique em **Ver Detalhes da Extensão** para mostrar os detalhes em um popup modal.

![][8]{: style="max-width:70%;"}

Agora você pode prosseguir como de costume com [a criação do seu segmento][11]].

[2]: {% image_buster /assets/img/segment/segment_extension2.png %}
[3]: {% image_buster /assets/img/segment/segment_extension1.png %}
[5]: {% image_buster /assets/img/segment/segment_extension5.png %}
[6]: {% image_buster /assets/img/segment/segment_extension7.png %}
[7]: {% image_buster /assets/img/segment/segment_extension6.png %}
[8]: {% image_buster /assets/img/segment/segment_extension8.png %}
[10]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/
[11]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/
[12]: {% image_buster /assets/img/segment/property1.png %}
[13]: {% image_buster /assets/img/segment/property2.png %}
[13,5]: {% image_buster /assets/img/segment/property5.png %}
[14]: {% image_buster /assets/img/segment/property3.png %}
[15]: {% image_buster /assets/img/segment/property4.png %}
[16]: {% image_buster /assets/img/Shopify/arrow.jpeg %}
[17]: {% image_buster /assets/img/segment/segment_extension9.png %}
[18]: {% image_buster /assets/img/segment/nested_segment_extensions.png %}
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/
[20]: {% image_buster /assets/img/segment/segment_extension_modal.png %}
[21]: {% image_buster /assets/img/segment/segment_interval_settings.png %}
