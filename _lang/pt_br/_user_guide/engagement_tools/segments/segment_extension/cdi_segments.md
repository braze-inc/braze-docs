---
nav_title: Extensões do segmento CDI
article_title: Extensões do segmento CDI
page_order: 0
page_type: reference
alias: /cdi_segment_extensions/
tool: 
- Segments
description: "Este artigo explica como configurar a segmentação por local, permitindo que você segmente os usuários por local."

---

# Extensões do segmento CDI

> Com o Braze [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/) (CDI), você pode configurar uma conexão direta do seu data warehouse ou sistema de armazenamento de arquivos com o Braze para sincronizar dados relevantes de usuários ou catálogos de forma recorrente.

{% alert warning %}
As CDI Segment Extensions consultam seu data warehouse diretamente, portanto, você incorrerá em todos os custos associados à execução dessas consultas em seu data warehouse. As CDI Segment Extensions não consomem [créditos de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#monitoring-your-sql-segments-usage), não contam para o limite de Segment Extension e não registram pontos de dados.
{% endalert %}

## Pré-requisitos

Para usar os dados do data warehouse para segmentação no espaço de trabalho do Braze, você precisará criar uma [fonte conectada]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/) e, em seguida, criar um segmento CDI nas [Extensões de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). As CDI Segment Extensions permitem que você escreva SQL que consulta diretamente seu próprio data warehouse usando dados disponibilizados por meio de suas conexões CDI e crie um grupo de usuários que pode ser direcionado no Braze.

## Criação de um segmento CDI

### Etapa 1: Configure sua fonte

Antes de criar sua primeira extensão de segmento CDI, configure uma nova fonte conectada com seu data warehouse seguindo as etapas em [Fontes conectadas]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/).

### Etapa 2: Criar um segmento

Primeiro, crie uma nova [extensão de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) e, em seguida, selecione **Full refresh (Atualização completa**).

\![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:60%;"}

Para sua fonte de dados, selecione **Tabelas de dados CDI**.

\![]({% image_buster /assets/img/segment/cdi_data_tables.png %}){: style="max-width:60%;"}

Como parte da configuração do CDI, você pode selecionar diferentes conexões para usar nas extensões de segmento do CDI. Cada conexão tem um conjunto específico de tabelas de dados. Sua equipe de desenvolvimento pode configurar suas conexões e tabelas de dados durante a configuração do CDI.

Para visualizar as tabelas de dados disponíveis, incluindo seus esquemas e quaisquer descrições disponíveis, selecione **Reference (Referência**). Quando estiver pronto, selecione uma conexão.

\![]({% image_buster /assets/img/segment/connection_schema_with_descriptions.png %}){: style="max-width:100%;"}

Em seguida, escreva o SQL para seu segmento usando [a sintaxe do Braze SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#writing-sql).

Lembre-se de que todas as CDI Segment Extensions devem usar `external_user_id` como a coluna selecionada, e sua `external_user_id` deve corresponder à definida no Braze para os usuários. Se os resultados da consulta incluírem usuários que não existem no Braze, esses usuários serão ignorados. O Braze não criará novos usuários com base na saída de sua extensão de segmento CDI.

{% alert tip %}
Para saber como você pode visualizar suas Extensões de Segmento, gerenciar suas Extensões de Segmento e executar atualizações automáticas de associação, consulte [Extensões de Segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/).
{% endalert %}

Por fim, você pode [usar essa extensão de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#step-5-use-your-extension-in-a-segment) em um segmento do Braze para enviar uma campanha ou um Canvas para esse público.

## Considerações

- Uma extensão de segmento pode fazer referência a dados de apenas uma conexão, não de várias.    
- Uma extensão de segmento pode usar uma das seguintes opções como fonte de dados: Dados do CDI ou dados do Braze Snowflake (Currents). Não é possível misturar fontes de dados em uma extensão de segmento, mas você pode criar várias extensões de segmento para referenciar juntas em um segmento.

## Solução de problemas

- Sua consulta poderá atingir o tempo máximo de execução, que é configurado para cada sincronização de conexão na página **Ingestão de dados na nuvem**. O tempo máximo de execução permitido é de 60 minutos.
- Certifique-se de que seu SQL esteja escrito usando a sintaxe apropriada para seu data warehouse. 
