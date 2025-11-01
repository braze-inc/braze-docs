---
nav_title: Extensões de segmento
article_title: Extensões de segmento
page_order: 6
page_type: reference
description: "Este artigo explica como configurar e usar uma extensão de segmento para aprimorar seus recursos de segmentação."
tool: Segments
---

# Extensões de segmento

> As Extensões de Segmento permitem criar segmentos muito precisos durante um período prolongado do histórico de um usuário. Por exemplo, usando as Extensões de Segmento, você pode segmentar usuários que compraram um determinado produto nos últimos dezesseis meses ou que gastaram uma certa quantia de dinheiro com o seu serviço. Refine esse público-alvo usando as propriedades do evento para tornar a segmentação ainda mais granular.

A segmentação do Braze permite que você segmente usuários com base em eventos personalizados ou comportamento de compra. O Segment Extensions aprimora essa capacidade, permitindo que você aproveite os dados históricos salvos no perfil do usuário. Usando as Extensões de Segmento, você pode identificar e alcançar os usuários que concluíram qualquer evento personalizado ou evento de compra qualquer número de vezes nos últimos dois anos (730 dias). 

## Por que usar Extensões de Segmento?

Os segmentos Braze oferecem ferramentas poderosas de segmentação para criar grupos dinâmicos de usuários. Para a maioria dos casos de uso, isso é suficiente para atingir seu público de forma eficaz. As Extensões de Segmento são projetadas para casos de uso avançado em que você precisa analisar comportamentos de até dois anos atrás ou aplicar lógica complexa, sem comprometer a retenção de dados ou o desempenho do sistema. Você pode usar consultas [SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments) (SQL Segment Extensions) ou dados de seu próprio [data warehouse]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments) para refinar ainda mais seu público.

Por exemplo, a segmentação padrão do Braze encontrará usuários que se encaixam em critérios específicos definidos por você, como a identificação de um usuário que comprou recentemente um de seus produtos. As Extensões de Segmento permitem que você vá mais fundo - como identificar usuários que compraram uma determinada cor de um produto específico pelo menos duas vezes entre 18 e 24 meses atrás. As Extensões de Segmento são um aprimoramento, não um requisito. Se você precisar de filtros mais avançados ou de uma janela de análise mais longa, eles são uma ótima ferramenta para ajudar a manter o uso de dados otimizado.

{% alert note %}
Há uma alocação padrão de 25 Extensões de Segmento ativas por espaço de trabalho em um determinado momento. Se precisar aumentar esse limite, entre em contato com o gerente de sucesso do cliente Braze para discutir seu caso de uso.
{% endalert %}

## Criação de uma extensão de segmento

Para criar uma extensão de segmento, você criará um filtro para refinar um segmento de seus usuários com base em propriedades de eventos personalizados. Ao criar uma extensão de segmento, você escolherá se o segmento será estático ou atualizado dinamicamente em um intervalo definido.

### Etapa 1: Navegue até Extensões de segmento

Vá para **Audience** > **Segment Extensions**( **Público** > **Extensões de segmento**).

Na tabela Segment Extensions (Extensões de segmento), selecione **Create New Extension (Criar nova extensão**) e, em seguida, selecione sua experiência de criação de Segment Extension (Extensão de segmento):

- **Extensão simples:** Crie uma extensão de segmento focada em um único evento usando um formulário guiado.
Melhor para quando você não quiser usar o SQL.
- **Comece com um modelo:** Crie um segmento SQL com um modelo personalizável usando dados do Snowflake.
- **Atualização incremental:** Escreva um segmento SQL do Snowflake que atualize automaticamente os últimos dois dias de dados ou atualize manualmente conforme necessário. Melhor para equilibrar precisão e custo-benefício.
- **Atualização completa:** Escreva um segmento SQL com dados do Snowflake ou qualquer [fonte conectada ao CDI]({{site.baseurl}}/cdi_segment_extensions/) que recalcule todo o público após a atualização manual. Ideal para quando você precisa de uma visão completa e atualizada do seu público.

Tabela com diferentes experiências de criação de Extensão de Segmento para selecionar.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%"}

Se você selecionar uma experiência que use SQL, consulte [Extensões do segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) para obter mais informações. Se você selecionar **Extensão simples**, continue na etapa 2.

#### Uso de crédito SQL

Os seguintes tipos de extensão de segmento consomem créditos SQL:

- Extensões de segmento SQL (atualização incremental e completa)
- Segmentos do catálogo
- Segmentos do CDI 
    - Os créditos são consumidos em seu próprio data warehouse

### Etapa 2: Nomeie sua extensão de segmento

Nomeie sua extensão de segmento descrevendo o tipo de usuários que pretende filtrar. Isso garantirá que essa extensão possa ser descoberta com facilidade e precisão ao aplicá-la como um filtro em seu segmento.

Extensão de segmento denominada "Extensão para compradores on-line - 90 dias".]({% image_buster /assets/img/segment/segment_extension2.png %})

### Etapa 3: Escolha seus critérios

Selecione entre compra, engajamento por mensagem ou critérios de eventos personalizados para segmentação. Depois de selecionar os critérios de tipo de evento desejados, escolha o item comprado, a interação de mensagem ou o evento personalizado específico que deseja direcionar para a sua lista de usuários. Em seguida, escolha quantas vezes (mais do que, menos do que ou igual a) o usuário precisaria ter concluído o evento e o período de tempo - para Extensões de Segmento especificamente, você pode voltar até os últimos 730 dias (2 anos).

A segmentação baseada em dados de eventos de mais de 730 dias pode ser feita usando outros filtros localizados em **Segments (Segmentos**). Ao escolher o período de tempo, você pode especificar um intervalo de datas relativo para selecionar o número X de dias anteriores, uma data de início, uma data de término ou um intervalo de datas exato (data A a data B).

Critérios de segmentação para usuários que realizaram um evento personalizado mais de duas vezes no intervalo de datas de 1º de março de 2025 a 31 de março de 2025.]({% image_buster /assets/img/segment/segment_extension1.png %})

#### Segmentação de propriedades de eventos

Para aumentar a precisão do direcionamento, marque a caixa de seleção **Add Property Filters (Adicionar filtros de propriedade** ). Isso permitirá que você faça uma busca detalhada com base nas propriedades específicas de sua compra ou evento personalizado. Oferecemos suporte à segmentação de propriedades de eventos com base em objetos de cadeia de caracteres, numéricos, booleanos e de tempo.

Para propriedades de cadeia de caracteres, você pode inserir vários valores de uma vez. No exemplo abaixo, esse filtro procura usuários com um status igual a qualquer um dos seguintes: ouro, prata ou bronze.

\![Segmentação baseada em propriedades de cadeia de caracteres.]({% image_buster /assets/img/segment/property5.png %})

\![Segmentação baseada em propriedades numéricas.]({% image_buster /assets/img/segment/property2.png %})

\![Segmentação baseada em propriedades booleanas.]({% image_buster /assets/img/segment/property3.png %})

\![Segmentação baseada em objetos de data e hora.]({% image_buster /assets/img/segment/property4.png %})

Também oferecemos suporte à segmentação com base em [propriedades de eventos aninhados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

\![Segmentação baseada em propriedades de eventos aninhados.]({% image_buster /assets/img/segment/nested_segment_extensions.png %})

As Extensões de Segmento dependem do armazenamento de longo prazo das propriedades do evento e não têm um limite de armazenamento de propriedades com registro de data e hora. Você pode analisar as propriedades de eventos rastreadas nos últimos dois anos. O uso de propriedades de eventos nas Extensões de Segmento não afeta o uso do ponto de dados.

{% alert note %}
Você não precisa do Segment Extensions para usar propriedades de eventos ou atributos personalizados aninhados em seu segmento. As Extensões de segmento apenas estendem a janela histórica usada para criar um segmento padrão. Você pode criar um [segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/) padrão em tempo real que use propriedades de eventos dos últimos 30 dias ou use atributos personalizados aninhados. Da mesma forma, você pode [programar sua mensagem]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) para ser acionada em tempo real com base em uma propriedade de evento - sem necessidade de Segment Extension.
{% endalert %}

### Etapa 4: Designar configurações de atualização (opcional)

{% multi_lang_include segments.md section='Refresh settings' %}

### Etapa 5: Salvar sua extensão de segmento

Depois de selecionar **Save (Salvar)**, sua Segment Extension (Extensão de segmento) começará a ser processada. O tempo necessário para gerar sua extensão de segmento depende de quantos usuários você tem, quantos eventos personalizados ou eventos de compra você está capturando e quantos dias você está olhando para trás no histórico.

Enquanto sua extensão de segmento estiver sendo processada, você verá uma pequena animação ao lado do nome da extensão de segmento e a palavra "Processing" (Processando) na coluna **Last Processed (Último** processamento) na lista Segment Extension (Extensão de segmento). Observe que não será possível editar uma extensão de segmento enquanto ela estiver sendo processada.

Página "["Extensões de segmento"] com duas extensões ativas.]({% image_buster /assets/img/segment/segment_extension5.png %})

Quando uma Extensão de Segmento estiver sendo processada, o Braze continuará a usar o histórico de versões do segmento padrão de antes do início do processamento para fins de segmentação de público. O processamento ocorre sempre que ocorre um salvamento ou atualização e envolve a consulta e a atualização de perfis de usuários - em outras palavras, a associação do seu segmento padrão não é atualizada instantaneamente. Isso significa que, a menos que a ação de um usuário seja executada antes do início do processamento da atualização, não podemos garantir que o usuário será incluído na extensão de segmento quando essa atualização específica for concluída. Por outro lado, os usuários que estavam na extensão de segmento antes da atualização e que não atendem mais aos critérios continuarão a corresponder ao seu segmento de surdos até que o processo de atualização seja concluído e as atualizações sejam aplicadas.

### Etapa 6: Use sua extensão em um segmento

Depois de criar uma extensão de segmento, você pode usá-la como um filtro ao criar um segmento ou definir um público-alvo para uma campanha ou Canvas. Comece escolhendo **Braze Segment Extension** na lista de filtros na seção **User Attributes (Atributos do usuário** ).

Seção "Filtros" com um menu suspenso de filtros mostrando "Extensões do Braze Segment".]({% image_buster /assets/img/segment/segment_extension7.png %})

Na lista de filtros Extensão de Segmento Braze, selecione a Extensão de Segmento que você deseja incluir ou excluir nesse segmento.

Um filtro "Braze Segment Extensions" que inclui um segmento "1 clique de e-mail nos últimos 56 dias".]({% image_buster /assets/img/segment/segment_extension6.png %})

Para visualizar os critérios de extensão de segmento, selecione **View Extension Details (Exibir detalhes da extensão** ) para mostrar os detalhes em uma nova janela.

Extensão para "1 clique em e-mail nos últimos 56 dias".]({% image_buster /assets/img/segment/segment_extension8.png %}){: style="max-width:70%;"}

Agora você pode prosseguir normalmente com a [criação do seu segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

## Perguntas frequentes

### Posso criar uma extensão de segmento que use vários eventos personalizados?

Sim. Você pode adicionar vários eventos ou fazer referência a várias tabelas do Snowflake ao usar o [SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). 

Ao usar Extensões de segmento de **extensão simples**, você pode selecionar um evento personalizado, um evento de compra ou uma interação de canal. No entanto, você pode combinar várias Extensões de Segmento com um E ou OU ao criar o segmento padrão.

### Posso arquivar Extensões de Segmento se elas existirem em uma campanha ativa?

Não. Antes de arquivar uma extensão de segmento, você precisa removê-la de todas as mensagens ativas.

### Posso usar matrizes nas Extensões de Segmento?

Sim. Para usar matrizes, acrescente colchetes (`[]`) ao nome da propriedade. Se sua propriedade for `location_code`, você digitará `location_code[]`. 

O Braze usa o site `[]` para percorrer matrizes e verificar se algum item da matriz percorrida corresponde à propriedade do evento. Por exemplo, você pode criar uma extensão de segmento de usuários que correspondam a pelo menos um valor de uma propriedade de matriz.

### Como o Braze calcula o período de tempo para um período de tempo relativo de "últimos __ dias"?

Quando o Segment Extensions calcula o período de tempo relativo ("últimos X dias"), a hora de início é definida como meia-noite UTC. Por exemplo, para uma extensão de segmento que é atualizada em 2024-09-16 21:00 UTC e especifica 10 dias, a hora de início é definida como 2024-09-06 00:00 UTC, e não 2024-09-06 21:00 UTC. 

No entanto, você pode especificar os fusos horários usando segmentos SQL para identificar os usuários que realizaram o evento personalizado há 10 dias, com base na meia-noite no horário da empresa, ou os usuários que realizaram o evento há 10 dias, com base na hora atual.

