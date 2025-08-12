---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
description: "Este artigo de referência descreve a parceria entre a Braze e o Snowflake, um data warehouse de nuvem SQL criado especificamente para todos os seus dados e usuários."
page_type: partner
search_tag: Partner

---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Snowflake

> O [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) é um data warehouse de nuvem SQL criado para fins específicos e disponibilizado como software como serviço (SaaS). O Snowflake fornece um data warehouse mais rápido, mais fácil de usar e muito mais flexível do que as ofertas tradicionais. Com a arquitetura exclusiva e patenteada da Snowflake, é fácil reunir todos os seus dados, executar análises rápidas e obter insights orientados por dados para todos os seus usuários.

Campanhas de marketing personalizadas e relevantes exigem acesso aos dados no momento. É por isso que a Braze fez uma parceria com o Snowflake para lançar o compartilhamento de dados. Essa oferta conjunta ativa os profissionais de marketing a desbloquear o potencial de seus dados de engajamento de clientes e campanhas mais rápido do que nunca.

A [integração da Braze e da Snowflake](https://www.braze.com/perspectives/article/snowflake-partner-announcement) aproveita a troca de dados da Snowflake para criar uma presença, encontrar novos clientes e expandir o alcance por meio da crescente base de clientes da Snowflake.

{% alert tip %}
**Que tal obter acesso aos dados no nível do Snowflake sem precisar de uma conta no Snowflake?**<br>Confira [Contas de leitor do Snowflake]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts). Com as Contas de Leitor, o Braze criará e compartilhará seus dados em uma conta e lhe fornecerá credenciais para registrar e acessar seus dados. Isso fará com que todo o compartilhamento de dados e o faturamento do uso sejam gerenciados inteiramente pela Braze.
{% endalert %}

## O que é compartilhamento de dados?

A funcionalidade de [compartilhamento seguro de dados](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html) do Snowflake permite que o Braze lhe dê acesso seguro aos dados em nosso portal Snowflake sem se preocupar com o atrito ou a lentidão do fluxo de trabalho, os pontos de falha e os custos desnecessários que acompanham os relacionamentos típicos com os provedores de dados. O compartilhamento de dados pode ser configurado por meio da integração a seguir ou por meio das [contas de leitor da Snowflake]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts).

- **Reduzir o tempo para obter insights**<br>Diga adeus aos processos de ETL que levam semanas para serem desenvolvidos. As arquiteturas exclusivas do Braze e do Snowflake tornam todos os dados de engajamento do cliente e de campanha imediatamente acessíveis e consultáveis a partir do momento em que chegam ao lago de dados. Nenhum dado é copiado ou movido, portanto, você pode oferecer experiências ao cliente com base apenas nas informações mais relevantes e atualizadas.
- **Quebre os silos de dados**<br>Crie uma visão holística de seus clientes em todos os canais e plataformas. O compartilhamento de dados torna mais fácil do que nunca unir os dados de engajamento de clientes da Braze com todos os outros dados do Snowflake, criando insights mais ricos em uma única fonte confiável da verdade.
- **Veja como está o seu engajamento**<br>Otimize suas estratégias de engajamento do cliente com o Braze Benchmarks. Essa ferramenta interativa, desenvolvida pela Braze e pela Snowflake, permite comparar os dados de engajamento da sua marca com os benchmarks dos canais, do setor e das plataformas de dispositivos.

Com o compartilhamento de dados, nenhum dado real é copiado ou transferido entre as contas. Todo o compartilhamento é realizado por meio da camada de serviços e do armazenamento de metadados exclusivos do Snowflake. Esse é um conceito importante porque os dados compartilhados não ocupam nenhum espaço de armazenamento em uma conta de consumidor e, portanto, não contribuem para as cobranças mensais de armazenamento de dados do consumidor. Os **únicos** encargos para os consumidores são os recursos de computação (como os data warehouses virtuais) usados para consultar os dados compartilhados.

Além disso, usando os recursos integrados de funções e permissões do Snowflake, o acesso aos dados compartilhados do Braze pode ser controlado e governado usando os controles de acesso já existentes para a sua conta do Snowflake e os dados nela contidos. O acesso pode ser restrito e monitorado da mesma forma que seus próprios dados.

Para saber mais sobre o compartilhamento de dados do Snowflake, consulte [Introdução ao compartilhamento seguro de dados](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work).

## Pré-requisitos

Antes de poder usar esse recurso, você precisará concluir o seguinte:

| Requisito | Descrição |
| ----------- | ----------- |
| Acesso ao Braze | Para acessar esse recurso no Braze, você precisará entrar em contato com sua conta Braze ou com o gerente de sucesso do cliente. |
| Conta Snowflake | Uma conta Snowflake com permissões `admin`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Configuração do compartilhamento seguro de dados

No Snowflake, o compartilhamento de dados ocorre entre um [provedor de dados](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) e um [consumidor de dados](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers). Nesse contexto, sua conta Braze é o provedor de dados porque cria e envia o compartilhamento de dados, ao passo que sua conta Snowflake é o consumidor de dados porque usa o compartilhamento de dados para criar um banco de dados. Para obter mais detalhes, consulte [Snowflake: Consumo de dados compartilhados](https://docs.snowflake.com/en/user-guide/data-share-consumers).

### Etapa 1: Enviar o compartilhamento de dados do Braze

1. No Braze, acesse **Partner Integrations** > **Data Sharing (** **Integrações com parceiros** > **Compartilhamento de dados**).
2. Insira os detalhes de sua conta Snowflake e o local. Para obter o localizador de sua conta, execute `SELECT CURRENT_ACCOUNT()` na conta de destinos.
3. Se estiver usando um compartilhamento CRR, especifique o provedor de nuvem e a região.
4. Quando terminar, selecione **Create Datashare**. Isso enviará o compartilhamento de dados para sua conta do Snowflake.

### Etapa 2: Criar o banco de dados no Snowflake

1. Após alguns minutos, você deverá receber o compartilhamento de dados de entrada em sua conta do Snowflake.
2. Usando o compartilhamento de dados de entrada, crie um banco de dados para visualizar e consultar as tabelas. Por exemplo:
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
3. Conceda privilégios para consultar o novo banco de dados.

{% alert warning %}
Se você excluir e recriar um compartilhamento no dashboard do Braze, deverá remover o banco de dados criado anteriormente e recriá-lo usando `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` para consultar o compartilhamento de entrada.
{% endalert %}

## Uso e visualização

Depois que o compartilhamento de dados for provisionado, será necessário criar um banco de dados a partir do compartilhamento de dados recebido, fazendo com que todas as tabelas compartilhadas apareçam na sua instância do Snowflake e possam ser consultadas como qualquer outro dado armazenado na sua instância. No entanto, lembre-se de que os dados compartilhados são somente de leitura e só podem ser consultados, mas não modificados ou excluídos de forma alguma.

Semelhante ao Currents, você pode usar o compartilhamento seguro de dados do Snowflake para:

- Criar relatórios complexos
- Realizar modelagem de atribuição
- Compartilhamento seguro dentro de sua própria empresa
- Mapear dados brutos de eventos ou de usuários para um CRM (como o Salesforce)
- E mais

[Baixe os esquemas de tabela brutos aqui.]({% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %})

### Esquema de ID de usuário

Note as seguintes diferenças entre as convenções de nomenclatura da Braze e do Snowflake para IDs de usuário.

| Esquema do Braze | Esquema de Snowflake | Descrição |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | O identificador exclusivo que é atribuído automaticamente pelo Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | O identificador exclusivo do perfil de um usuário que é definido pelo cliente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Informações importantes e limitações

### Alterações interruptivas e não interruptivas

#### Alterações não interruptivas

Alterações não interruptivas podem ocorrer a qualquer momento e geralmente trazem novas funcionalidades. Exemplos de alterações não interruptivas:
- Adição de uma nova tabela ou visualização
- Adição de uma coluna a uma tabela ou exibição existente

{% alert important %}
Como as novas colunas são consideradas não interruptivas, a Braze recomenda enfaticamente listar de modo explícito as colunas de interesse em cada consulta, em vez de usar consultas `SELECT *`. Como alternativa, talvez você queira criar exibições que nomeiem explicitamente as colunas e, em seguida, consultar essas exibições em vez das tabelas diretamente.
{% endalert %}

#### Mudanças significativas

Quando possível, as mudanças interruptivas serão precedidas de um anúncio e de um período de migração. Exemplos de mudanças significativas incluem:
- Remoção de uma tabela ou exibição
- Remoção de uma coluna de uma tabela ou exibição existente
- Alteração do tipo ou da capacidade de anulação de uma coluna existente

### Regiões do Snowflake

A Braze hospeda todos os dados de nível de usuário nas regiões AWS US East-1 e EU-Central (Frankfurt) do Snowflake. Para usuários fora dessas regiões, a Braze pode fornecer compartilhamento de dados para clientes conjuntos que hospedem sua infraestrutura do Snowflake em qualquer região do AWS, Azure ou GCP.

### Retenção de dados

#### Política de retenção

Todos os dados com mais de dois anos serão arquivados e transferidos para o armazenamento de longo prazo. Como parte do processo de arquivamento, todos os eventos são anônimos e todos os campos sensíveis de informações de identificação pessoal (IPI) são removidos (isso inclui campos de IPI opcionais, como `properties`). Os dados arquivados ainda contêm o campo `user_id`, que permite a análise de dados por usuário em todos os dados de eventos.

Você poderá consultar os dois anos mais recentes de dados de cada evento na visualização correspondente do site `USERS_*_SHARED`. Além disso, cada evento terá uma visualização `USERS_*_SHARED_ALL` que pode ser consultada para retornar dados anônimos e não anônimos.

#### Dados históricos

O arquivo de dados históricos de eventos no Snowflake remonta a abril de 2019. Nos primeiros meses em que o Braze armazenou dados no Snowflake, foram feitas alterações no produto que podem ter resultado em alguns desses dados com aparência ligeiramente diferente ou com alguns valores nulos (já que não estávamos passando dados para todos os campos disponíveis no momento). É melhor presumir que os resultados que incluam dados anteriores a agosto de 2019 poderão ser ligeiramente diferentes das expectativas.

### Conformidade com o Regulamento Geral sobre a Proteção de Dados (GDPR)

Quase todos os registros de eventos armazenados pelo Braze incluem alguns campos que representam informações de identificação pessoal (IPI) dos usuários. Alguns eventos podem incluir endereço de e-mail, número de telefone, ID do dispositivo, idioma, gênero e local. Se a solicitação de esquecimento de um usuário for enviada ao Braze, anularemos esses campos de IPI para qualquer evento pertencente a esses usuários. Dessa forma, não removemos o registro histórico do evento, mas agora o evento jamais poderá ser vinculado a um indivíduo específico.

### Velocidade, performance e custo das consultas

A velocidade, o desempenho e o custo de qualquer consulta executada nos dados são determinados pelo tamanho do data warehouse que você usa para consultar os dados. Em alguns casos, dependendo da quantidade de dados que estiver acessando para análise de dados, talvez seja necessário usar um tamanho de warehouse maior para que a consulta seja bem-sucedida. A Snowflake tem excelentes recursos disponíveis sobre a melhor forma de determinar o tamanho a ser usado, incluindo [Visão geral dos armazéns](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) e [Considerações sobre o armazém](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html)

> Para obter um conjunto de exemplos de consultas a serem consultadas ao configurar o Snowflake, confira nossos exemplos [de consultas]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/sample_queries/) e de [configuração do pipeline de eventos ETL]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/etl_pipline_setup/).

