---
nav_title: Ingestão de dados na nuvem
article_title: Ingestão de dados para nuvem da Braze
alias: /cloud_ingestion/
description: "Este artigo de referência cobre as fontes de Ingestão de Dados na Nuvem da Braze e recomendações de configuração de dados."
page_order: 0.1
toc_headers: h2
---

# Ingestão de dados para nuvem da Braze

> A Ingestão de Dados na Nuvem (CDI) do Braze permite que você configure uma conexão direta da sua solução de armazenamento de dados para sincronizar dados relevantes de usuários e outros dados não relacionados a usuários com o Braze. Esses dados podem ser usados para personalização ou segmentação para potencializar seus casos de uso de marketing. A integração flexível da Ingestão de Dados na Nuvem suporta estruturas de dados complexas, incluindo JSON aninhado e arrays de objetos.

## Como funciona?

Com a Braze Cloud Data Ingestion (CDI), você configura uma integração entre sua instância de data warehouse e o espaço de trabalho da Braze para sincronizar dados de forma recorrente. Esta sincronização é executada em um cronograma que você define, e cada integração pode ter um cronograma diferente. As sincronizações podem ocorrer com a frequência de 15 minutos ou tão raramente quanto uma vez por mês. Se precisar que as sincronizações ocorram com mais frequência do que 15 minutos, entre em contato com o gerente de sucesso do cliente ou considere o uso de chamadas de API REST para ingestão de dados em tempo real.

Quando uma sincronização é executada, o Braze se conecta diretamente à sua instância de data warehouse, recupera todos os novos dados da tabela especificada e atualiza os dados correspondentes em seu dashboard do Braze. Cada vez que a sincronização é executada, quaisquer dados atualizados são refletidos no Braze.

### Encontrando seu ID de integração

Você pode encontrar seu ID de integração na URL ao visualizar uma integração no dashboard do Braze. Navegue até **Configurações de Dados** > **Ingestão de Dados na Nuvem** e selecione uma integração. O ID de integração aparece na URL no formato `https://[instance].braze.com/integrations/cloud_data_ingestion/[integration_id]`. Por exemplo, se sua URL for `https://dashboard-01.braze.com/integrations/cloud_data_ingestion/abc123xyz`, seu ID de integração é `abc123xyz`. Você pode usar esse ID ao fazer chamadas de API para disparar sincronizações ou verificar o status da sincronização.

## Casos de uso

Com as capacidades de Ingestão de Dados na Nuvem do Braze, você pode:

- Crie em poucos minutos uma integração simples com a Braze diretamente do seu data warehouse ou solução de armazenamento de arquivos.
- Sincronizar de forma segura dados de usuários, incluindo atributos, eventos e compras do seu data warehouse para o Braze.
- Feche o ciclo de dados com o Braze combinando a Ingestão de Dados na Nuvem com Currents ou Compartilhamento de Dados do Snowflake.

Além disso, [Fontes Conectadas]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) são uma alternativa sem cópia. Você pode fazer com que o Braze consulte diretamente seu data warehouse ou solução de armazenamento de arquivos para construir segmentos de CDI — tudo isso sem copiar os dados subjacentes para o Braze.

## Fontes de dados suportadas

A Ingestão de Dados na Nuvem pode sincronizar dados de:

   - Amazon Redshift
   - Databricks 
   - Google BigQuery
   - Microsoft Fabric
   - Snowflake
   - Amazon S3

## Tipos de dados suportados 

A Ingestão de Dados na Nuvem suporta os seguintes tipos de dados:

### Dados de usuários
- Atributos do usuário, incluindo:
   - Atributos personalizados aninhados
   - Arrays de objetos
   - Status de inscrições
- Eventos personalizados
- Eventos de compra
- Solicitações de exclusão de usuários

### Objetos não relacionados a usuários
- Itens do catálogo

### Envio de mensagens sem cópia
- Fontes conectadas

## Identificadores de usuários para ingestão de dados

Ao sincronizar dados de usuários através da Ingestão de Dados na Nuvem, você pode identificar usuários usando um ou mais dos seguintes tipos de identificadores. Cada linha na sua tabela de origem deve conter um valor para apenas um tipo de identificador por vez, mas sua tabela pode incluir colunas para um, dois, três, quatro ou todos os cinco tipos de identificadores.

| Identificador | Descrição |
|------------|-------------|
| `EXTERNAL_ID` | O ID externo que identifica o perfil do usuário a ser criado ou atualizado. Esse valor deve corresponder ao valor `external_id` usado no Braze. |
| `ALIAS_NAME` e `ALIAS_LABEL` | Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador único, e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`. |
| `BRAZE_ID` | O identificador de usuário da Braze gerado pelo SDK da Braze. Novos usuários não podem ser criados usando um ID da Braze através da Ingestão de Dados na Nuvem. Para criar novos usuários, especifique um ID de usuário externo ou um alias de usuário. |
| `EMAIL` | O endereço de e-mail do usuário. Se múltiplos perfis com o mesmo endereço de e-mail existirem, o perfil mais recentemente atualizado é priorizado para atualizações. Se você incluir tanto e-mail quanto telefone, o e-mail é usado como o identificador principal. |
| `PHONE` | O número de telefone do usuário. Se múltiplos perfis com o mesmo número de telefone existirem, o perfil mais recentemente atualizado é priorizado para atualizações. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para informações detalhadas sobre como configurar tabelas com esses identificadores, consulte a documentação de [integrações do Data Warehouse]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/).

## Uso de ponto de dados

Para clientes com faturamento baseado em pontos de dados, o faturamento por pontos de dados para a Ingestão de Dados na Nuvem é equivalente ao faturamento por atualizações através do [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track). Consulte [pontos de dados]({{site.baseurl}}/user_guide/data/data_points/) para saber mais. 

{% alert important %}
A ingestão de dados na nuvem da Braze conta para o limite de frequência disponível, então se você estiver enviando dados usando outro método, o limite de frequência é combinado entre a API da Braze e a ingestão de dados na nuvem.
{% endalert %}

## Limitações do produto

| Limitação            | Descrição                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Número de integrações | Não há limite para quantas integrações você pode configurar. No entanto, você pode configurar apenas uma integração por tabela ou visualização.                                             |
| Número de linhas         | Por padrão, cada execução pode sincronizar até 500 milhões de linhas. Qualquer sincronização com mais de 500 milhões de novas linhas é interrompida. Se você precisar de um limite maior do que isso, entre em contato com seu gerente de sucesso do cliente da Braze ou com o Suporte da Braze. |
| Atributos por linha     | Cada linha deve conter um único ID de usuário e um objeto JSON com até 250 atributos. Cada chave no objeto JSON conta como um atributo (ou seja, um vetor conta como um atributo). |
| Tamanho da carga útil           | Cada linha pode conter uma carga útil de até 1 MB. Carga útil maior que 1 MB é rejeitada, e o erro "Carga útil foi maior que 1MB" é registrado no log de sincronização junto com o ID externo associado e a carga útil truncada. |
| Tipo de dados              | Você pode sincronizar atributos de usuário, eventos e compras através da Ingestão de Dados na Nuvem.                                                                                                  |
| região Braze           | Este produto está disponível em todas as regiões da Braze. Qualquer região da Braze pode se conectar a qualquer região de origem de dados.                                                                              |
| Região de origem       | A Braze se conecta ao seu data warehouse ou ambiente de nuvem em qualquer região ou provedor de nuvem.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
