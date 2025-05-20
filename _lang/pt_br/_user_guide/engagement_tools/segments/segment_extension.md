---
nav_title: Extensões de segmento
article_title: Extensões de segmento
page_order: 3.1
page_type: reference
description: "Este artigo de instruções irá guiá-lo sobre como configurar e usar uma extensão de segmento para aprimorar suas capacidades de segmentação."
tool: Segments
---

# Extensões de segmento

> As extensões de segmento permitem criar segmentos muito precisos ao longo de um período extenso do histórico de um usuário. Por exemplo, usando as extensões de segmento, é possível direcionar os usuários que compraram um determinado produto nos últimos dezesseis meses ou que gastaram uma certa quantia de dinheiro com o seu serviço. Refine esse público usando as propriedades do evento para tornar o direcionamento ainda mais granular.

A segmentação do Braze permite o direcionamento de usuários com base em eventos personalizados ou comportamento de compra. As extensões de segmento aumentam essa capacidade, permitindo que você utilize dados históricos salvos no perfil do usuário. Usando extensões de segmento, é possível identificar e alcançar usuários que concluíram qualquer evento personalizado ou evento de compra qualquer número de vezes nos últimos dois anos (730 dias). 

## Por que usar extensões de segmento?

Os Braze segments oferecem ferramentas poderosas de direcionamento para criar grupos dinâmicos de usuários. Para a maioria dos casos de uso, isso é suficiente para alcançar seu público de forma eficaz. As extensões de segmento são projetadas para casos de uso avançado em que é necessário analisar comportamentos de até dois anos atrás ou aplicar lógica complexa, sem comprometer a retenção de dados ou a performance do sistema. Você pode usar consultas [de SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments) ou dados de seu próprio [data warehouse]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments) para refinar ainda mais seu público.

Por exemplo, a segmentação padrão do Braze encontrará usuários que se encaixam em critérios específicos definidos por você, como a identificação de um usuário que comprou recentemente um de seus produtos. As extensões de segmento permitem que você vá mais fundo - como identificar usuários que compraram uma determinada cor de um produto específico pelo menos duas vezes entre 18 e 24 meses atrás. As extensões de segmento são um aprimoramento, não um requisito. Se você precisar de filtros mais avançados ou de uma janela de análise mais longa, eles são uma ótima ferramenta para ajudar a manter o uso de dados otimizado.

{% alert note %}
Há uma alocação padrão de 25 extensões de segmento ativas por espaço de trabalho em um determinado momento. Se você precisar aumentar esse limite, entre em contato com seu gerente de sucesso do cliente da Braze para discutir seu caso de uso.
{% endalert %}

## Criação de uma extensão de segmento

Para criar uma extensão de segmento, você criará um filtro para refinar um segmento de seus usuários com base em propriedades de eventos personalizados. Ao criar uma extensão de segmento, você escolherá se o segmento será estático ou atualizado dinamicamente em um intervalo definido.

### Etapa 1: Navegue para extensões de segmento

Acesse **Público** > **Extensões de segmento**.

Na tabela Extensões de segmento, selecione **Criar nova extensão** e, em seguida, selecione sua experiência de criação de extensão de segmento:

- **Extensão simples:** Crie uma extensão de segmento focada em um único evento usando um formulário guiado.
Melhor para quando você não quer usar SQL.
- **Comece com um modelo:** Crie um segmento SQL com um modelo personalizável usando dados do Snowflake.
- **Atualização incremental:** Formule um segmento do Snowflake SQL que recarregue automaticamente os 2 últimos dias de dados ou faça um recarregamento manual conforme necessário. Ideal para equilibrar precisão e custo-benefício.
- **Atualização completa:** Formule um segmento do Snowflake SQL que recalcule todo o público com atualização manual. Ideal para quando você precisa ter uma visão completa e atualizada do seu público.

![Tabela com diferentes experiências de criação de extensão de segmento para selecionar.][20]{: style="max-width:50%"}

Se você selecionar uma experiência que usa SQL, consulte [extensões de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) para mais informações.

Se você selecionar **Extensão simples**, continue com as etapas abaixo.

### Etapa 2: Nomeie sua extensão de segmento

Nomeie sua extensão de segmento descrevendo o tipo de usuários que você pretende filtrar. Isso garantirá que esta extensão possa ser facilmente e precisamente descoberta ao aplicá-la como um filtro em seu segmento.

![extensão de segmento nomeada "Extensão de Compradores Online - 90 Dias" com a caixa de seleção "Regenerar Extensão Diariamente" selecionada.][2]

### Etapa 3: Escolha seus critérios

Selecione entre critérios de compra, engajamento com mensagem ou evento personalizado para direcionamento. Depois de selecionar os critérios do tipo de evento desejado, escolha qual item comprado, interação de mensagem ou evento personalizado específico você gostaria de direcionar para sua lista de usuários. Em seguida, escolha quantas vezes (mais que, menos que ou igual a) o usuário precisaria ter concluído o evento e o período de tempo—para extensões de segmento especificamente, você pode voltar até os últimos 730 dias (2 anos).

A segmentação baseada em dados de eventos de mais de 730 dias pode ser feita usando outros filtros localizados em **Segmentos**. Ao escolher seu período de tempo, você pode especificar um intervalo de datas relativo (como os últimos X dias), uma data de início, uma data de término ou um intervalo de datas exato (data A a data B).

![Critérios de segmentação para usuários que realizaram um evento personalizado, "# of aaa", mais de 0 vezes no intervalo de datas de 1º de agosto de 2023 a 10 de agosto de 2023.][3]

#### Segmentação de propriedade de evento

Para aumentar a precisão do direcionamento, selecione a caixa de seleção **Adicionar Filtros de Propriedade**. Isso permitirá que você se aprofunde com base nas propriedades específicas da sua compra ou evento personalizado. Apoiamos a segmentação de propriedades de eventos com base em string, numérico, booleano e objetos de tempo.

Para propriedades de string, você pode inserir vários valores de uma vez. No exemplo abaixo, este filtro procura usuários com status igual a qualquer um dos seguintes: ouro, prata ou bronze.

![Segmentando com base nas propriedades da string.][13.5]

![Segmentação com base em propriedades numéricas.][13]

![Segmentando com base em propriedades booleanas.][14]

![Segmentando com base em objetos datetime.][15]

Também suportamos segmentação com base em [propriedades de eventos aninhados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

![Segmentação com base em propriedades de eventos aninhados.][18]

As extensões de segmento dependem do armazenamento de longo prazo das propriedades do evento e não têm um limite de armazenamento de propriedades com carimbo de data/hora. Você pode olhar para trás nas propriedades de eventos rastreadas nos últimos dois anos. O uso de propriedades de eventos dentro de extensões de segmento não impacta o uso de pontos de dados.

{% alert note %}
Você não precisa de extensões de segmento para usar propriedades de evento ou atributos personalizados aninhados em seu segmento. As extensões de segmento apenas estendem a janela histórica usada para criar um segmento. Você pode criar um [segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/) em tempo real que use propriedades de eventos dos últimos 30 dias ou use atributos personalizados aninhados. Da mesma forma, você pode [programar sua mensagem]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) para ser disparada em tempo real com base em uma propriedade de evento – sem necessidade de extensão de segmento.
{% endalert %}

### Etapa 4: Designar configurações de atualização (opcional)

Se não precisar que sua extensão seja atualizada regularmente, você poderá salvá-la sem usar as configurações de atualização, e o Braze gerará sua extensão de segmento com base na associação do usuário naquele momento. Use o comportamento padrão se quiser gerar o público apenas uma vez e depois direcioná-lo com uma campanha única.

Seu segmento sempre começará a ser processado após o salvamento inicial. Sempre que seu segmento for atualizado, o Braze executará novamente o segmento e atualizará a associação do segmento para refletir os usuários em seu segmento no momento da atualização. Isso pode ajudar suas campanhas recorrentes a alcançar os usuários mais relevantes.

#### Configuração de uma atualização recorrente

Para configurar uma agenda recorrente, selecione **Atualizar configurações** no canto superior direito de sua extensão específica. A opção de designar configurações de atualização está disponível para todos os tipos de extensões de segmento, incluindo segmentos SQL, segmentos CDI e extensões de segmento simples baseadas em formulário.

{% alert important %}
Para otimizar seu gerenciamento de dados, as configurações de atualização são automaticamente desativadas para extensões de segmento não utilizadas. As extensões de segmento são consideradas não utilizadas quando são:

- Não usado em nenhuma campanha, tela ou segmento ativo ou inativo (rascunho, interrompido, arquivado); ou
- Sem modificação há mais de 7 dias

O Braze notificará o contato da empresa e o criador da extensão se essa configuração estiver desativada. A opção de regenerar extensões diariamente pode ser ativada novamente a qualquer momento.
{% endalert %}

#### Seleção de suas configurações de atualização

![Configurações de intervalo de atualização com uma frequência de atualização semanal, horário de início às 10h e segunda-feira selecionada como dia.][21]{: style="max-width:60%;"}

No painel **Refresh Settings (Configurações de atualização)**, você pode selecionar a frequência com que essa extensão de segmento será atualizada: por hora, diariamente, semanalmente ou mensalmente. Também será necessário selecionar o horário específico (que está no fuso horário da sua empresa) em que a atualização ocorrerá, como, por exemplo:

- Se você tiver uma campanha de envio de e-mail que é enviada todas as segundas-feiras às 11 horas, horário da empresa, e quiser garantir que seu segmento seja atualizado logo antes do envio, deverá escolher uma agenda de atualização semanal às 10 horas das segundas-feiras.
- Se quiser que seu segmento seja atualizado todos os dias, selecione a frequência de atualização diária e, em seguida, escolha a hora do dia para atualizar.

{% alert note %}
A capacidade de definir um cronograma de atualização por hora não está disponível para extensões de segmento baseadas em formulário (mas você pode definir cronogramas diários, semanais ou mensais).
{% endalert %}

#### Consumo de crédito e custos adicionais

Como as atualizações executam novamente a consulta de seu segmento, cada atualização para segmentos SQL consumirá créditos de segmento SQL e cada atualização para segmentos CDI incorrerá em um custo em seu data warehouse de terceiros.

{% alert note %}
Os segmentos podem levar até 60 minutos para serem atualizados devido ao tempo de processamento dos dados. Os segmentos que estão atualmente em processo de atualização terão o status "Processing" (Processando) na lista de extensões de segmento. Isso tem algumas implicações:

- Para concluir o processamento de seu segmento antes de um horário específico, escolha um horário de atualização que seja 60 minutos antes. 
- Somente uma atualização pode ocorrer de cada vez em uma extensão de segmento específica. Se houver um conflito em que uma nova atualização seja iniciada quando uma atualização existente já tiver começado a ser processada, o Braze cancelará a nova solicitação de atualização e continuará o processamento em andamento.
{% endalert %}

#### Critérios para desativar automaticamente extensões obsoletas

As atualizações programadas são automaticamente desativadas quando uma extensão de segmento se torna obsoleta. Uma extensão de segmento estará obsoleta se atender aos seguintes critérios:

- Não usado em nenhuma campanha ou tela ativa
- Não usado em nenhum segmento que esteja em uma campanha ativa ou canva
- Não usado em nenhum segmento que tenha [o rastreamento de dados]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking#segment-analytics-tracking) ativado
- Não é modificado há mais de sete dias
- Não foi adicionado a uma campanha ou Canva (incluindo rascunhos) ou segmento há mais de sete dias

Se a atualização programada estiver desativada para uma extensão de segmento, essa extensão terá uma notificação informando isso.

![Uma notificação informando que "As atualizações programadas foram desativadas para essa extensão porque ela não é usada em nenhuma campanha, canvas ou segmento ativo. A extensão do segmento foi desativada em 23 de fevereiro de 2025 às 12:00 AM."][1]

Quando estiver pronto para usar uma extensão de segmento desatualizada, [revise as configurações de atualização](#step-4-designate-refresh-settings-optional), selecione a programação de atualização que corresponda ao seu caso de uso e salve as modificações.

### Etapa 5: Salve sua extensão de segmento

Depois de selecionar **Salvar**, sua extensão começará a ser processada. O tempo necessário para gerar sua extensão depende de quantos usuários você tem, quantos eventos personalizados ou eventos de compra você está capturando e quantos dias você está olhando para trás na história.

Enquanto sua extensão está processando, você verá uma pequena animação ao lado do nome da extensão e a palavra "Processando" na coluna **Último Processado** na lista de extensões. Observe que você não poderá editar uma extensão enquanto ela estiver em processamento.

![Página "Extensões de segmento" com duas extensões ativas.][5]

### Etapa 6: Use sua extensão em um segmento

Depois de criar uma extensão, você pode usá-la como um filtro ao criar um segmento ou definir um público para uma campanha ou canva. Comece escolhendo **extensão de segmento Braze** da lista de filtros na seção **Atributos do Usuário**.

![Seção "Filtros" com um menu suspenso de filtros mostrando "Extensões de segmento Braze".][6]

Na lista de filtros da extensão de segmento do Braze, escolha a extensão que deseja incluir ou excluir neste segmento.

![Um filtro "Braze Segment Extensions" que inclui um segmento "Online Shoppers Ext...".][7]

Para visualizar os critérios da extensão, selecione **Exibir detalhes da extensão** para mostrar os detalhes em um modal pop-up.

![Detalhes da extensão para a "Extensão para compradores on-line - 90 dias".][8]{: style="max-width:70%;"}

Agora você pode prosseguir como de costume com [a criação do seu segmento][11]].

## Perguntas frequentes

### Posso criar uma extensão de segmento que use vários eventos personalizados?

Sim. Você pode adicionar vários eventos ou fazer referência a várias tabelas do Snowflake ao usar [as extensões de segmento do SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). 

Ao usar extensões de segmento **de extensão simples**, você pode selecionar um evento personalizado, um evento de compra ou uma interação de canal. No entanto, você pode combinar várias extensões de segmento com um AND ou OR ao criar o segmento.

### Posso arquivar extensões de segmento se elas existirem em uma campanha ativa?

Não. Antes de arquivar uma extensão de segmento, você precisa removê-la de todos os envios de mensagens ativos.

[1]: {% image_buster /assets/img/segment/segment_extension_disabled.png %}
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
[20]: {% image_buster /assets/img/segment/segment_extension_modal.png %}
[21]: {% image_buster /assets/img/segment/segment_interval_settings.png %}
