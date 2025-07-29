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



Se você selecionar uma experiência que usa SQL, consulte [extensões de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) para mais informações.

Se você selecionar **Extensão simples**, continue com as etapas abaixo.

### Etapa 2: Nomeie sua extensão de segmento

Nomeie sua extensão de segmento descrevendo o tipo de usuários que você pretende filtrar. Isso garantirá que esta extensão possa ser facilmente e precisamente descoberta ao aplicá-la como um filtro em seu segmento.



### Etapa 3: Escolha seus critérios

Selecione entre critérios de compra, engajamento com mensagem ou evento personalizado para direcionamento. Depois de selecionar os critérios do tipo de evento desejado, escolha qual item comprado, interação de mensagem ou evento personalizado específico você gostaria de direcionar para sua lista de usuários. Em seguida, escolha quantas vezes (mais que, menos que ou igual a) o usuário precisaria ter concluído o evento e o período de tempo—para extensões de segmento especificamente, você pode voltar até os últimos 730 dias (2 anos).

A segmentação baseada em dados de eventos de mais de 730 dias pode ser feita usando outros filtros localizados em **Segmentos**. 



#### Segmentação de propriedade de evento

Para aumentar a precisão do direcionamento, selecione a caixa de seleção **Adicionar Filtros de Propriedade**. Isso permitirá que você se aprofunde com base nas propriedades específicas da sua compra ou evento personalizado. Apoiamos a segmentação de propriedades de eventos com base em string, numérico, booleano e objetos de tempo.

Para propriedades de string, você pode inserir vários valores de uma vez. No exemplo abaixo, este filtro procura usuários com status igual a qualquer um dos seguintes: ouro, prata ou bronze.









Também suportamos segmentação com base em [propriedades de eventos aninhados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).



As extensões de segmento dependem do armazenamento de longo prazo das propriedades do evento e não têm um limite de armazenamento de propriedades com carimbo de data/hora. Você pode olhar para trás nas propriedades de eventos rastreadas nos últimos dois anos. O uso de propriedades de eventos dentro de extensões de segmento não impacta o uso de pontos de dados.

{% alert note %}
Você não precisa de extensões de segmento para usar propriedades de evento ou atributos personalizados aninhados em seu segmento. As extensões de segmento apenas estendem a janela histórica usada para criar um segmento. Você pode criar um [segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/) em tempo real que use propriedades de eventos dos últimos 30 dias ou use atributos personalizados aninhados. Da mesma forma, você pode [programar sua mensagem]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) para ser disparada em tempo real com base em uma propriedade de evento – sem necessidade de extensão de segmento.
{% endalert %}

### Etapa 4: Designar configurações de atualização (opcional)



### Etapa 5: Salve sua extensão de segmento

 O tempo necessário para gerar sua extensão depende de quantos usuários você tem, quantos eventos personalizados ou eventos de compra você está capturando e quantos dias você está olhando para trás na história.

Enquanto sua extensão está processando, você verá uma pequena animação ao lado do nome da extensão e a palavra "Processando" na coluna **Último Processado** na lista de extensões. Observe que você não poderá editar uma extensão enquanto ela estiver em processamento.



   

### Etapa 6: Use sua extensão em um segmento

 Comece escolhendo **extensão de segmento Braze** da lista de filtros na seção **Atributos do Usuário**.



Na lista de filtros da extensão de segmento do Braze, escolha a extensão que deseja incluir ou excluir neste segmento.









## Perguntas frequentes

### Posso criar uma extensão de segmento que use vários eventos personalizados?

Sim. Você pode adicionar vários eventos ou fazer referência a várias tabelas do Snowflake ao usar [as extensões de segmento do SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). 

Ao usar extensões de segmento **de extensão simples**, você pode selecionar um evento personalizado, um evento de compra ou uma interação de canal. No entanto, você pode combinar várias extensões de segmento com um AND ou OR ao criar o segmento.

### Posso arquivar extensões de segmento se elas existirem em uma campanha ativa?

Não. Antes de arquivar uma extensão de segmento, você precisa removê-la de todos os envios de mensagens ativos.

### 

Sim.   

 

### 

  



