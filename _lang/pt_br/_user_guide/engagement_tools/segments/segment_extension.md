---
nav_title: extensões de segmento
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

Os Braze segments oferecem ferramentas poderosas de direcionamento para criar grupos dinâmicos de usuários. Para a maioria dos casos de uso, isso é suficiente para alcançar seu público de forma eficaz. As extensões de segmento são projetadas para casos de uso avançado em que é necessário analisar comportamentos de até dois anos atrás ou aplicar lógica complexa, sem comprometer a retenção de dados ou a performance do sistema. Você pode usar [SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments) consultas (Extensões de Segmento SQL) ou dados do seu próprio [data warehouse]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments) para refinar ainda mais seu público.

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
- **Atualização completa:** Escreva um segmento SQL com dados do Snowflake ou qualquer [fonte conectada ao CDI]({{site.baseurl}}/cdi_segment_extensions/) que recalcula todo o público após a atualização manual. Ideal para quando você precisa ter uma visão completa e atualizada do seu público.

![Tabela com diferentes experiências de criação de Extensão de Segmento para selecionar.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%"}

Se você selecionar uma experiência que usa SQL, consulte [Extensões de Segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) para mais informações. Se você selecionar **Extensão simples**, continue para a etapa 2.

#### Uso de crédito SQL

Os seguintes tipos de Extensão de Segmento consomem créditos SQL:

- Extensões de Segmento SQL (tanto incremental quanto atualização completa)
- Segmentos do catálogo
- Segmentos do CDI 
    - Os créditos são consumidos dentro do seu próprio data warehouse

### Etapa 2: Nomeie sua extensão de segmento

Nomeie sua extensão de segmento descrevendo o tipo de usuários que você pretende filtrar. Isso garantirá que esta extensão possa ser facilmente e precisamente descoberta ao aplicá-la como um filtro em seu segmento.

![Extensão de Segmento chamada "Extensão de Compradores Online - 90 Dias".]({% image_buster /assets/img/segment/segment_extension2.png %})

### Etapa 3: Escolha seus critérios

Selecione entre critérios de compra, engajamento com mensagem ou evento personalizado para direcionamento. Depois de selecionar os critérios do tipo de evento desejado, escolha qual item comprado, interação de mensagem ou evento personalizado específico você gostaria de direcionar para sua lista de usuários. Em seguida, escolha quantas vezes (mais que, menos que ou igual a) o usuário precisaria ter concluído o evento e o período de tempo—para extensões de segmento especificamente, você pode voltar até os últimos 730 dias (2 anos).

A segmentação baseada em dados de eventos de mais de 730 dias pode ser feita usando outros filtros localizados em **Segmentos**. Ao escolher seu período de tempo, você pode especificar um intervalo de datas relativo para selecionar os últimos X dias, uma data de início, uma data de término ou um intervalo de datas exato (data A até data B).

![Critérios de segmentação para usuários que realizaram um evento personalizado mais de 2 vezes no intervalo de datas de 1º de março de 2025 a 31 de março de 2025.]({% image_buster /assets/img/segment/segment_extension1.png %})

#### Segmentação de propriedade de evento

Para aumentar a precisão do direcionamento, selecione a caixa de seleção **Adicionar Filtros de Propriedade**. Isso permitirá que você se aprofunde com base nas propriedades específicas da sua compra ou evento personalizado. Apoiamos a segmentação de propriedades de eventos com base em string, numérico, booleano e objetos de tempo.

Para propriedades de string, você pode inserir vários valores de uma vez. No exemplo abaixo, este filtro procura usuários com status igual a qualquer um dos seguintes: ouro, prata ou bronze.

![Segmentação com base em propriedades de string.]({% image_buster /assets/img/segment/property5.png %})

![Segmentação com base em propriedades numéricas.]({% image_buster /assets/img/segment/property2.png %})

![Segmentando com base em propriedades booleanas.]({% image_buster /assets/img/segment/property3.png %})

![Segmentando com base em objetos datetime.]({% image_buster /assets/img/segment/property4.png %})

Também suportamos segmentação com base em [propriedades de eventos aninhados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

![Segmentação com base em propriedades de eventos aninhados.]({% image_buster /assets/img/segment/nested_segment_extensions.png %})

As extensões de segmento dependem do armazenamento de longo prazo das propriedades do evento e não têm um limite de armazenamento de propriedades com carimbo de data/hora. Você pode olhar para trás nas propriedades de eventos rastreadas nos últimos dois anos. O uso de propriedades de eventos dentro de extensões de segmento não impacta o uso de pontos de dados.

{% alert note %}
Você não precisa de extensões de segmento para usar propriedades de evento ou atributos personalizados aninhados em seu segmento. As Extensões de Segmento apenas estendem a janela histórica usada para criar um segmento padrão. Você pode criar um [segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/) padrão em tempo real que usa propriedades de eventos dos últimos 30 dias ou usa atributos personalizados aninhados. Da mesma forma, você pode [programar sua mensagem]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) para ser disparada em tempo real com base em uma propriedade de evento – sem necessidade de extensão de segmento.
{% endalert %}

### Etapa 4: Designar configurações de atualização (opcional)

{% multi_lang_include segments.md section='Refresh settings' %}

### Etapa 5: Salve sua extensão de segmento

Após selecionar **Salvar**, sua Extensão de Segmento começará a processar. O tempo que leva para gerar sua Extensão de Segmento depende de quantos usuários você tem, quantos eventos personalizados ou eventos de compra você está capturando e quantos dias você está analisando no histórico.

Enquanto sua Extensão de Segmento estiver processando, você verá uma pequena animação ao lado do nome da Extensão de Segmento e a palavra "Processando" na coluna **Último Processado** na lista de Extensões de Segmento. Observe que você não poderá editar uma Extensão de Segmento enquanto ela estiver processando.

!["Extensões de Segmento" página com duas extensões ativas.]({% image_buster /assets/img/segment/segment_extension5.png %})

Quando uma Extensão de Segmento está processando, a Braze continuará a usar o histórico de versões do segmento padrão de antes do início do processamento para fins de segmentação de público. O processamento ocorre cada vez que um salvamento ou atualização acontece, e envolve consultar e atualizar perfis de usuários—em outras palavras, a associação do seu segmento padrão não é atualizada instantaneamente. Isso significa que, a menos que uma ação do usuário seja realizada antes do início do processamento da atualização, não podemos garantir que o usuário será incluído na Extensão de Segmento uma vez que essa atualização específica esteja completa. Por outro lado, os usuários que estavam na Extensão de Segmento antes da atualização e que não atendem mais aos critérios continuarão a corresponder ao seu segmento padrão até que o processo de atualização esteja completo e as atualizações sejam aplicadas.

### Etapa 6: Use sua extensão em um segmento

Depois de criar uma Extensão de Segmento, você pode usá-la como um filtro ao criar um segmento ou definindo um público para uma campanha ou Canvas. Comece escolhendo **extensão de segmento Braze** da lista de filtros na seção **Atributos do Usuário**.

!["Seção de Filtros" com um menu suspenso de filtro mostrando "Extensões de Segmento Braze".]({% image_buster /assets/img/segment/segment_extension7.png %})

Na lista de filtros de Extensão de Segmento da Braze, escolha a Extensão de Segmento que deseja incluir ou excluir neste segmento.

![Um filtro "Extensões de Segmento Braze" que inclui um segmento "1 clique de e-mail nos últimos 56 dias".]({% image_buster /assets/img/segment/segment_extension6.png %})

Para visualizar os critérios da Extensão de Segmento, selecione **Ver Detalhes da Extensão** para mostrar os detalhes em uma nova janela.

![Extensão para "1 clique de e-mail nos últimos 56 dias".]({% image_buster /assets/img/segment/segment_extension8.png %}){: style="max-width:70%;"}

Agora você pode prosseguir como de costume com [criando seu segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

## Perguntas frequentes

### Posso criar uma Extensão de Segmento que use múltiplos eventos personalizados?

Sim. Você pode adicionar múltiplos eventos ou referenciar múltiplas tabelas Snowflake ao usar [Extensões de Segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). 

Ao usar **Extensão simples** Extensões de Segmento, você pode selecionar um evento personalizado, um evento de compra ou uma interação de canal. No entanto, você pode combinar múltiplas Extensões de Segmento com um AND ou OR ao criar o segmento padrão.

### Posso arquivar Extensões de Segmento se elas existirem em uma campanha ativa?

Não. Antes de arquivar uma Extensão de Segmento, você precisa removê-la de todas as mensagens ativas.

### Posso usar arrays em Extensões de Segmento?

Sim. Para usar arrays, anexe colchetes (`[]`) ao nome da sua propriedade. Se sua propriedade for `location_code`, você deve inserir `location_code[]`. 

Braze usa `[]` para percorrer arrays e verificar se algum item no array percorrido corresponde à propriedade do evento. Por exemplo, você poderia criar uma Extensão de Segmento de usuários que correspondem a pelo menos um valor de uma propriedade de array.

### Como o Braze calcula o período de tempo para um período de tempo relativo de "últimos __ dias"?

Quando as Extensões de Segmento calculam o período de tempo relativo ("últimos X dias"), o horário de início é definido para a meia-noite UTC. Por exemplo, para uma Extensão de Segmento que se atualiza em 2024-09-16 21:00 UTC e especifica 10 dias, o horário de início é definido para 2024-09-06 00:00 UTC, não 2024-09-06 21:00 UTC. 

No entanto, você pode especificar os fusos horários usando segmentos SQL para identificar usuários que realizaram o evento personalizado há 10 dias com base na meia-noite no horário da empresa, ou usuários que realizaram o evento há 10 dias com base no horário atual.

