---
nav_title: "Compartilhamento de dados"
article_title: Compartilhamento de dados do Snowflake
page_order: 0
description: "Este artigo de referência aborda a integração de Compartilhamento Seguro de Dados do Snowflake, que permite acessar dados de engajamento e campanhas da Braze diretamente na sua instância do Snowflake."
page_type: partner
search_tag: Partner

---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Compartilhamento de dados do Snowflake

> O [Compartilhamento Seguro de Dados](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html) do Snowflake permite que a Braze forneça acesso seguro aos dados no nosso portal Snowflake sem se preocupar com atritos no fluxo de trabalho, lentidão, pontos de falha e custos desnecessários que acompanham os relacionamentos típicos com provedores de dados. O compartilhamento de dados pode ser configurado por meio da integração a seguir ou por meio das [Contas de Leitor do Snowflake]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts).

{% alert tip %}
**Quer ter acesso a dados no nível do Snowflake sem precisar de uma conta do Snowflake?**<br>Confira as [Contas de Leitor do Snowflake]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts). Com as Contas de Leitor, a Braze criará e compartilhará seus dados em uma conta e fornecerá credenciais para que você faça login e acesse seus dados. Isso fará com que todo o compartilhamento de dados e a cobrança de uso sejam gerenciados inteiramente pela Braze.
{% endalert %}

## Sobre o Compartilhamento Seguro de Dados

Com o compartilhamento de dados, nenhum dado real é copiado ou transferido entre contas. Todo o compartilhamento é realizado por meio da camada de serviços e do armazenamento de metadados exclusivos do Snowflake. Esse é um conceito importante porque os dados compartilhados não ocupam nenhum espaço de armazenamento na sua conta e, portanto, não contribuem para as cobranças mensais de armazenamento de dados. Os **únicos** custos são pelos recursos computacionais (como warehouses virtuais) usados para consultar os dados compartilhados.

Além disso, usando os recursos integrados de funções e permissões do Snowflake, o acesso aos dados compartilhados pela Braze pode ser controlado e governado usando os controles de acesso já existentes na sua conta do Snowflake e nos dados contidos nela. O acesso pode ser restringido e monitorado da mesma forma que seus próprios dados.

- **Reduza o tempo para obter insights**<br>Diga adeus aos processos de ETL que levam semanas para serem construídos. As arquiteturas exclusivas da Braze e do Snowflake tornam todos os dados de engajamento de clientes e campanhas imediatamente acessíveis e consultáveis a partir do momento em que chegam ao data lake. Nenhum dado é copiado ou movido, então você pode oferecer experiências ao cliente com base apenas nas informações mais relevantes e atualizadas.
- **Elimine silos de dados**<br>Crie uma visão holística dos seus clientes em todos os canais e plataformas. O compartilhamento de dados torna mais fácil do que nunca unir seus dados de engajamento de clientes da Braze com todos os outros dados do Snowflake, criando insights mais ricos em uma única fonte confiável de verdade.
- **Veja como seu engajamento se compara**<br>Otimize suas estratégias de engajamento de clientes com o Braze Benchmarks. Essa ferramenta interativa, desenvolvida pela Braze e pelo Snowflake, permite comparar os dados de engajamento da sua marca com benchmarks de canais, setores e plataformas de dispositivos.

Para saber mais sobre o compartilhamento de dados do Snowflake, consulte [Introdução ao Compartilhamento Seguro de Dados](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work).

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Acesso à Braze | Fale com sua conta da Braze ou gerente de sucesso do cliente para configurar o Compartilhamento de Dados. |
| Conta do Snowflake | Uma conta do Snowflake com permissões de `admin`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Configurando o Compartilhamento Seguro de Dados

No Snowflake, o compartilhamento de dados acontece entre um [provedor de dados](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) e um [consumidor de dados](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers). Nesse contexto, sua conta da Braze é o provedor de dados porque cria e envia o datashare&#8212;enquanto sua conta do Snowflake é o consumidor de dados porque usa o datashare para criar um banco de dados. Para mais detalhes, consulte [Snowflake: Consumindo Dados Compartilhados](https://docs.snowflake.com/en/user-guide/data-share-consumers).

### Etapa 1: Enviar o datashare a partir da Braze

1. Na Braze, acesse **Integrações com Parceiros** > **Compartilhamento de Dados**.
2. Insira os detalhes e o localizador da sua conta do Snowflake. Para obter o localizador da sua conta, execute `SELECT CURRENT_ACCOUNT()` na conta de destino.
3. Se estiver usando um compartilhamento CRR, especifique o provedor de nuvem e a região.
4. Quando terminar, selecione **Criar Datashare**. Isso enviará o datashare para sua conta do Snowflake.

### Etapa 2: Criar o banco de dados no Snowflake

1. Após alguns minutos, você deverá receber o datashare de entrada na sua conta do Snowflake.
2. Usando o datashare de entrada, crie um banco de dados para visualizar e consultar as tabelas. Por exemplo:
    {% raw %}
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
    {% endraw %}
3. Conceda privilégios para consultar o novo banco de dados.

{% alert warning %}
Se você excluir e recriar um compartilhamento no dashboard da Braze, será necessário descartar o banco de dados criado anteriormente e recriá-lo usando `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` para consultar o compartilhamento de entrada.
Se você tiver múltiplos espaços de trabalho compartilhando dados para a mesma conta do Snowflake, consulte as [Perguntas frequentes sobre Compartilhamento de Dados do Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs/) para orientações sobre como gerenciar configurações com múltiplos espaços de trabalho.
{% endalert %}

## Uso e visualização

Após o compartilhamento de dados ser provisionado, crie um banco de dados a partir do compartilhamento de dados recebido, fazendo com que todas as tabelas compartilhadas apareçam na sua instância do Snowflake e possam ser consultadas como qualquer outro dado armazenado na sua instância. No entanto, tenha em mente que os dados compartilhados são somente leitura e só podem ser consultados, mas não modificados ou excluídos de nenhuma forma.

Assim como o Currents, você pode usar o Compartilhamento Seguro de Dados do Snowflake para:

- Criar relatórios complexos
- Realizar modelagem de atribuição
- Compartilhamento seguro dentro da sua própria empresa
- Mapear dados brutos de eventos ou de usuários para um CRM (como o Salesforce)
- E muito mais

[Baixe os esquemas de tabelas brutas aqui.]({% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %})

### Esquema de ID do usuário

Observe as seguintes diferenças entre as convenções de nomenclatura da Braze e do Snowflake para IDs de usuários.

| Esquema da Braze | Esquema do Snowflake | Descrição |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | O identificador único que é atribuído automaticamente pela Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | O identificador único do perfil de um usuário que é definido pelo cliente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Informações importantes e limitações

### Alterações com e sem quebra de compatibilidade

#### Alterações sem quebra de compatibilidade

Alterações sem quebra de compatibilidade podem acontecer a qualquer momento e geralmente fornecem funcionalidades adicionais. Exemplos de alterações sem quebra de compatibilidade:
- Adicionar uma nova tabela ou view
- Adicionar uma coluna a uma tabela ou view existente

{% alert important %}
Como novas colunas são consideradas alterações sem quebra de compatibilidade, a Braze recomenda fortemente listar explicitamente as colunas de interesse em cada consulta em vez de usar consultas `SELECT *`. Alternativamente, você pode criar views que nomeiem explicitamente as colunas e depois consultar essas views em vez das tabelas diretamente.
{% endalert %}

#### Alterações com quebra de compatibilidade

Quando possível, alterações com quebra de compatibilidade serão precedidas por um anúncio e um período de migração. Exemplos de alterações com quebra de compatibilidade incluem:
- Remover uma tabela ou view
- Remover uma coluna de uma tabela ou view existente
- Alterar o tipo ou a nulabilidade de uma coluna existente

### Regiões do Snowflake

Atualmente, a Braze hospeda todos os dados em nível de usuário nestas regiões AWS do Snowflake:

 - US East-1
 - EU-Central (Frankfurt)
 - AP-Southeast-2 (Sydney)
 - AP-Southeast-3 (Jakarta)
 
Para usuários fora dessas regiões, a Braze pode fornecer compartilhamento de dados para clientes em comum que hospedam sua infraestrutura do Snowflake em qualquer região da AWS, Azure ou GCP.

### Retenção de dados

#### Política de retenção

Quaisquer dados com mais de dois anos serão arquivados e movidos para armazenamento de longo prazo. Como parte do processo de arquivamento, todos os eventos são anonimizados e quaisquer campos sensíveis de informações pessoais identificáveis (IPI) são removidos (isso inclui campos opcionalmente IPI como `properties`). Os dados arquivados ainda contêm o campo `user_id`, o que permite análises por usuário em todos os dados de eventos.

Você poderá consultar os dois anos mais recentes de dados para cada evento na view `USERS_*_SHARED` correspondente. Além disso, cada evento terá uma view `USERS_*_SHARED_ALL` que pode ser consultada para retornar dados anonimizados e não anonimizados.

#### Dados históricos

O arquivo de dados históricos de eventos no Snowflake remonta a abril de 2019. Nos primeiros meses em que a Braze armazenou dados no Snowflake, foram feitas alterações no produto que podem ter resultado em alguns desses dados parecendo ligeiramente diferentes ou tendo alguns valores nulos (já que não estávamos passando dados para todos os campos disponíveis naquela época). É melhor considerar que quaisquer resultados que incluam dados anteriores a agosto de 2019 podem parecer ligeiramente diferentes do esperado.

### Conformidade com o Regulamento Geral de Proteção de Dados (GDPR)

{% include partners/snowflake_pii_gdpr.md %}

### Velocidade, performance e custo das consultas

A velocidade, a performance e o custo de qualquer consulta executada sobre os dados são determinados pelo tamanho do warehouse que você usa para consultar os dados. Em alguns casos, dependendo da quantidade de dados que você está acessando para análise de dados, pode ser necessário usar um warehouse de tamanho maior para que a consulta seja bem-sucedida. O Snowflake possui excelentes recursos disponíveis sobre como determinar o melhor tamanho a ser usado, incluindo [Visão geral de warehouses](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) e [Considerações sobre warehouses](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html).

{% alert tip %}
Para um conjunto de consultas de exemplo como referência ao configurar o Snowflake, confira nossos exemplos de [consultas de amostra]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/sample_queries/) e [configuração de pipeline de eventos ETL]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/etl_pipline_setup/).
{% endalert %}