---
nav_title: Ingestão de dados na nuvem
article_title: Ingestão de dados para nuvem da Braze
alias: /cloud_ingestion/
description: "Este artigo de referência cobre as fontes de Ingestão de Dados na Nuvem da Braze e recomendações de configuração de dados."
page_order: 0.1
toc_headers: h2
---

# Ingestão de dados para nuvem da Braze

> O Braze Cloud Data Ingestion (CDI) permite que você configure uma conexão direta a partir da sua solução de armazenamento de dados para sincronizar dados de usuários relevantes e outros dados de não usuários com o Braze. Esses dados podem então ser usados para personalização ou segmentação para potencializar seus casos de uso de marketing. A integração flexível do Cloud Data Ingestion suporta estruturas de dados complexas, incluindo JSON aninhado e vetores de objetos.

## Como funciona?

Com a Braze Cloud Data Ingestion (CDI), você configura uma integração entre sua instância de data warehouse e o espaço de trabalho da Braze para sincronizar dados de forma recorrente. Esta sincronização é executada em um cronograma que você define, e cada integração pode ter um cronograma diferente. As sincronizações podem ocorrer com a frequência de 15 minutos ou tão raramente quanto uma vez por mês. Se precisar que as sincronizações ocorram com mais frequência do que 15 minutos, entre em contato com o gerente de sucesso do cliente ou considere o uso de chamadas de API REST para ingestão de dados em tempo real.

Quando uma sincronização é executada, o Braze se conecta diretamente à sua instância de data warehouse, recupera todos os novos dados da tabela especificada e atualiza os dados correspondentes em seu dashboard do Braze. Cada vez que a sincronização é executada, todos os dados atualizados são refletidos no Braze.

### Como encontrar seu ID de integração

Você pode encontrar seu ID de integração no URL ao visualizar uma integração no dashboard do Braze. Navegue até **Configurações de dados** > **Ingestão de dados na nuvem** e selecione uma integração. O ID de integração aparece no URL no formato `https://[instance].braze.com/integrations/cloud_data_ingestion/[integration_id]`. Por exemplo, se seu URL for `https://dashboard-01.braze.com/integrations/cloud_data_ingestion/abc123xyz`, seu ID de integração será `abc123xyz`. Você pode usar esse ID ao fazer chamadas de API para disparar sincronizações ou verificar o status da sincronização.

## Casos de uso

Com os recursos de ingestão de dados do Braze Cloud, você pode:

- Crie em poucos minutos uma integração simples com a Braze diretamente do seu data warehouse ou solução de armazenamento de arquivos.
- Sincronize com segurança os dados de usuários, incluindo atribuições, eventos e compras do seu data warehouse com o Braze.
- Feche o ciclo de dados com o Braze combinando a ingestão de dados na nuvem com o compartilhamento de dados do Currents ou do Snowflake.

Além disso, o [Connected Sources]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) é uma alternativa de cópia zero. Você pode fazer com que o Braze consulte diretamente seu data warehouse ou solução de armazenamento de arquivos para construir segmentos CDI - tudo sem copiar os dados subjacentes para o Braze.

## Fontes de dados suportadas

A ingestão de dados na nuvem pode sincronizar dados de:

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

### Objetos de não usuários
- Itens do catálogo

### Envio de mensagens sem cópia
- Fontes conectadas

## Identificadores de usuários para ingestão de dados

Ao sincronizar os dados de usuários por meio da ingestão de dados na nuvem, é possível identificar os usuários usando um ou mais dos seguintes tipos de identificadores. Cada linha em sua tabela de origem deve conter um valor para apenas um tipo de identificador por vez, mas sua tabela pode incluir colunas para um, dois, três, quatro ou todos os cinco tipos de identificadores.

| Identificador | Descrição |
|------------|-------------|
| `EXTERNAL_ID` | A ID externa que identifica o perfil de usuário a ser criado ou atualizado. Esse valor deve corresponder ao valor `external_id` usado no Braze. |
| `ALIAS_NAME` e `ALIAS_LABEL` | Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`. |
| `BRAZE_ID` | O identificador de usuário do Braze gerado pelo SDK do Braze. Novos usuários não podem ser criados usando um Braze ID por meio da ingestão de dados na nuvem. Para criar novos usuários, especifique um ID de usuário externo ou um alias de usuário. |
| `EMAIL` | O endereço de e-mail do usuário. Se houver vários perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente terá prioridade para atualizações. Se você incluir e-mail e telefone, o e-mail será usado como o identificador principal. |
| `PHONE` | O número de telefone do usuário. Se houver vários perfis com o mesmo número de telefone, o perfil atualizado mais recentemente terá prioridade nas atualizações. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para obter informações detalhadas sobre a configuração de tabelas com esses identificadores, consulte a documentação [de integrações do Data Warehouse]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/).

## Uso de ponto de dados

Para clientes com faturamento baseado em pontos de dados, o faturamento por ponto de dados para o Cloud Data Ingestion é equivalente ao faturamento por atualizações por meio do [ponto de extremidade`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track). Consulte [pontos de dados]({{site.baseurl}}/user_guide/data/data_points/) para saber mais. 

{% alert important %}
A ingestão de dados na nuvem da Braze conta para o limite de frequência disponível, então se você estiver enviando dados usando outro método, o limite de frequência é combinado entre a API da Braze e a ingestão de dados na nuvem.
{% endalert %}

## Limitações do produto

| Limitação            | Descrição                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Número de integrações | Não há limite para quantas integrações você pode configurar. No entanto, você pode configurar apenas uma integração por tabela ou visualização.                                             |
| Número de linhas         | Por padrão, cada execução pode sincronizar até 500 milhões de linhas. Todas as sincronizações com mais de 500 milhões de novas linhas são interrompidas. Se precisar de um limite maior do que esse, entre em contato com o gerente de sucesso do cliente Braze ou com o suporte da Braze. |
| Atributos por linha     | Cada linha deve conter um único ID de usuário e um objeto JSON com até 250 atributos. Cada chave no objeto JSON conta como um atributo (ou seja, um vetor conta como um atributo). |
| Tamanho da carga útil           | Cada linha pode conter uma carga útil de até 1 MB. Cargas úteis maiores que 1 MB são rejeitadas, e o erro "Carga útil maior que 1 MB" é registrado no log de sincronização junto com a ID externa associada e a carga útil truncada. |
| Tipo de dados              | Você pode sincronizar atributos de usuário, eventos e compras através da Ingestão de Dados na Nuvem.                                                                                                  |
| região Braze           | Este produto está disponível em todas as regiões da Braze. Qualquer região da Braze pode se conectar a qualquer região de origem de dados.                                                                              |
| Região de origem       | O Braze se conecta ao seu data warehouse ou ambiente de nuvem em qualquer região ou provedor de nuvem.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
