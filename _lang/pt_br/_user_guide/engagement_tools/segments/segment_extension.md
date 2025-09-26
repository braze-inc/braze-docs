---
nav_title: Extensões de segmento
article_title: Extensões de segmento
page_order: 6
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

![Tabela com diferentes experiências de criação de extensão de segmento para seleção.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%"}

Se você selecionar uma experiência que usa SQL, consulte [extensões de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) para mais informações.

Se você selecionar **Extensão simples**, continue com as etapas abaixo.

### Etapa 2: Nomeie sua extensão de segmento

Nomeie sua extensão de segmento descrevendo o tipo de usuários que você pretende filtrar. Isso garantirá que esta extensão possa ser facilmente e precisamente descoberta ao aplicá-la como um filtro em seu segmento.

![Extensão de segmento denominada "Extensão para compradores on-line - 90 dias".]({% image_buster /assets/img/segment/segment_extension2.png %})

### Etapa 3: Escolha seus critérios

Selecione entre critérios de compra, engajamento com mensagem ou evento personalizado para direcionamento. Depois de selecionar os critérios do tipo de evento desejado, escolha qual item comprado, interação de mensagem ou evento personalizado específico você gostaria de direcionar para sua lista de usuários. Em seguida, escolha quantas vezes (mais que, menos que ou igual a) o usuário precisaria ter concluído o evento e o período de tempo—para extensões de segmento especificamente, você pode voltar até os últimos 730 dias (2 anos).

A segmentação baseada em dados de eventos de mais de 730 dias pode ser feita usando outros filtros localizados em **Segmentos**. Ao escolher o período de tempo, você pode especificar um intervalo de datas relativo para selecionar o número X de dias anteriores, uma data de início, uma data de ponta a ponta ou um intervalo de datas exato (data A a data B).

![Critérios de segmentação para usuários que realizaram um evento personalizado mais de 2 vezes no intervalo de datas de 1º de março de 2025 a 31 de março de 2025.]({% image_buster /assets/img/segment/segment_extension1.png %})

#### Segmentação de propriedade de evento

Para aumentar a precisão do direcionamento, selecione a caixa de seleção **Adicionar Filtros de Propriedade**. Isso permitirá que você se aprofunde com base nas propriedades específicas da sua compra ou evento personalizado. Apoiamos a segmentação de propriedades de eventos com base em string, numérico, booleano e objetos de tempo.

Para propriedades de string, você pode inserir vários valores de uma vez. No exemplo abaixo, este filtro procura usuários com status igual a qualquer um dos seguintes: ouro, prata ou bronze.

![Segmentação baseada em propriedades de string.]({% image_buster /assets/img/segment/property5.png %})

![Segmentação baseada em propriedades numéricas.]({% image_buster /assets/img/segment/property2.png %})

![Segmentação baseada em propriedades booleanas.]({% image_buster /assets/img/segment/property3.png %})

![Segmentação baseada em objetos de data e hora.]({% image_buster /assets/img/segment/property4.png %})

Também suportamos segmentação com base em [propriedades de eventos aninhados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

![Segmentação baseada em propriedades de eventos aninhados.]({% image_buster /assets/img/segment/nested_segment_extensions.png %})

As extensões de segmento dependem do armazenamento de longo prazo das propriedades do evento e não têm um limite de armazenamento de propriedades com carimbo de data/hora. Você pode olhar para trás nas propriedades de eventos rastreadas nos últimos dois anos. O uso de propriedades de eventos dentro de extensões de segmento não impacta o uso de pontos de dados.

{% alert note %}
Você não precisa de extensões de segmento para usar propriedades de evento ou atributos personalizados aninhados em seu segmento. As extensões de segmento apenas estendem a janela histórica usada para criar um segmento. Você pode criar um [segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/) em tempo real que use propriedades de eventos dos últimos 30 dias ou use atributos personalizados aninhados. Da mesma forma, você pode [programar sua mensagem]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) para ser disparada em tempo real com base em uma propriedade de evento – sem necessidade de extensão de segmento.
{% endalert %}

### Etapa 4: Designar configurações de atualização (opcional)

{% multi_lang_include segments.md section='Refresh settings' %}

### Etapa 5: Salve sua extensão de segmento

Depois de selecionar **Save (Salvar)**, sua extensão começará a ser processada. O tempo necessário para gerar sua extensão depende de quantos usuários você tem, quantos eventos personalizados ou eventos de compra você está capturando e quantos dias você está olhando para trás na história.

Enquanto sua extensão está processando, você verá uma pequena animação ao lado do nome da extensão e a palavra "Processando" na coluna **Último Processado** na lista de extensões. Observe que você não poderá editar uma extensão enquanto ela estiver em processamento.

![Página "Extensões de segmento" com duas extensões ativas.]({% image_buster /assets/img/segment/segment_extension5.png %})

Quando uma extensão de segmento estiver sendo processada, o Braze continuará a usar o histórico da versão do segmento antes do início do processamento para fins de segmentação de público. O processamento ocorre cada vez que ocorre um salvamento ou atualização e envolve consultas e atualização de perfis de usuários - em outras palavras, a associação do seu segmento não é atualizada instantaneamente. Isso significa que, a menos que a ação de um usuário seja executada antes do início do processamento da atualização, não podemos garantir que o usuário será incluído na extensão de segmento quando essa atualização específica for concluída. Por outro lado, os usuários que estavam na extensão de segmento antes da atualização e que não atendem mais aos critérios continuarão a corresponder ao seu segmento até que o processo de atualização seja concluído e as atualizações sejam aplicadas.

### Etapa 6: Use sua extensão em um segmento

Depois de criar uma extensão, você pode usá-la como um filtro ao criar um segmento ou definir um público para uma campanha ou Canva. Comece escolhendo **extensão de segmento Braze** da lista de filtros na seção **Atributos do Usuário**.

![Seção "Filtros" com um menu suspenso de filtros mostrando "Extensões de segmento do Braze".]({% image_buster /assets/img/segment/segment_extension7.png %})

Na lista de filtros da extensão de segmento do Braze, escolha a extensão que deseja incluir ou excluir neste segmento.

![Um filtro "Braze Segment Extensions" que inclui um segmento "1 clique de e-mail nos últimos 56 dias".]({% image_buster /assets/img/segment/segment_extension6.png %})

Para visualizar os critérios da extensão, selecione **View Extension Details (Exibir detalhes da extensão** ) para mostrar os detalhes em uma nova janela.

![Extensão para "1 clique de e-mail nos últimos 56 dias".]({% image_buster /assets/img/segment/segment_extension8.png %}){: style="max-width:70%;"}

Agora você pode prosseguir normalmente com a [criação do seu segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

## Perguntas frequentes

### Posso criar uma extensão de segmento que use vários eventos personalizados?

Sim. Você pode adicionar vários eventos ou fazer referência a várias tabelas do Snowflake ao usar [as extensões de segmento do SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). 

Ao usar extensões de segmento de **extensão simples**, você pode selecionar um evento personalizado, um evento de compra ou uma interação de canal. No entanto, você pode combinar várias extensões de segmento com um AND ou OR ao criar o segmento.

### Posso arquivar extensões de segmento se elas existirem em uma campanha ativa?

Não. Antes de arquivar uma extensão de segmento, você precisa removê-la de todos os envios de mensagens ativos.

### Posso usar matrizes em extensões de segmento?

Sim. Para usar matrizes, acrescente colchetes (`[]`) ao nome da propriedade. Se sua propriedade for `location_code`, você digitará `location_code[]`. 

O Braze usa o site `[]` para percorrer matrizes e verificar se algum item da matriz percorrida corresponde à propriedade do evento. Por exemplo, você pode criar um segmento de usuários que correspondam a pelo menos um valor de uma propriedade de matriz.

### Como o Braze calcula o período de tempo para um período de tempo relativo de "últimos \__ dias"?

Quando as extensões de segmento calculam o período de tempo relativo ("últimos X dias"), a hora de início é definida como meia-noite UTC. Por exemplo, para uma extensão de segmento que é atualizada em 2024-09-16 21:00 UTC e especifica 10 dias, a hora de início é definida como 2024-09-06 00:00 UTC, e não 2024-09-06 21:00 UTC. 

No entanto, é possível especificar os fusos horários usando segmentos SQL para identificar os usuários que realizaram o evento personalizado há 10 dias, com base na meia-noite no horário da empresa, ou os usuários que realizaram o evento há 10 dias, com base na hora atual.

