---
nav_title: Como o Braze usa as correntes
article_title: Como o Braze usa as correntes
page_order: 6
page_type: tutorial
description: "Este artigo de instruções da Currents o guiará pelo processo básico de configuração de entradas apropriadas para dados de eventos, bem como para transferi-los para um banco de dados e uma ferramenta de Business Intelligence (BI)."
tool: Currents
 
---

# Como o Braze usa as correntes

> O Braze usa o Currents! É isso mesmo, gostamos de nosso próprio produto o suficiente para usá-lo em conjunto com alguns de [nossos parceiros]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/).

Filtramos os dados de nossas campanhas de e-mail e push em uma ferramenta de insights de negócios, a Looker, mas é preciso percorrer um caminho interessante para chegar lá. Usamos uma versão ligeiramente invertida da metodologia Extrair, Transformar, Carregar (ETL) - apenas mudamos a ordem para Extrair, Carregar, Transformar (ELT)!

## Etapa 1: Dados de eventos agregados e de admissão

Depois de lançar campanhas usando qualquer uma de nossas ferramentas de engajamento (como campanhas ou Canvas), rastreamos os dados do evento usando nosso próprio sistema, bem como alguns de nossos parceiros de e-mail. Alguns desses dados são agregados e exibidos no painel, mas estamos interessados em nos aprofundar mais!

## Etapa 2: Enviar dados de eventos para um parceiro de armazenamento de dados

Configuramos o Currents para enviar dados de eventos do Braze para o Amazon S3 para armazenamento e extração. Agora, sabemos que você pode usar [o Athena](https://aws.amazon.com/athena/) para se sentar em cima do S3 e executar consultas. É uma ótima solução de curto prazo. Mas queríamos uma solução de longo prazo usando um banco de dados relacional e uma ferramenta de Business Intelligence/Analytics. (Recomendamos o mesmo para você).

Consideramos o S3 como nossas chaves do castelo! Isso abre as portas para muitas possibilidades de mover, girar e analisar nossos dados, transferindo-os para onde precisamos. No entanto, temos o cuidado de não transformar nossos dados no S3, pois temos uma estrutura muito específica para eles.

## Etapa 3: Transforme dados de eventos com um banco de dados relacional

No S3, escolhemos um depósito[(Snowflake Data Sharing](https://www.snowflake.com/try-the-data-warehouse-built-for-the-cloud/?&utm_medium=search&utm_source=adwords&utm_campaign=NA%20-%20Branded&utm_adgroup=NA%20-%20Branded%20Snowflake%20-%20Data&utm_term=%2Bsnowflake%20%2Bdata&utm_region=NA&gclid=EAIaIQobChMI0vLv6uDA3gIVEFqGCh3aiwMzEAAYASAAEgI72fD_BwE) ou Snowflake Reader Accounts, no nosso caso). Nós o transformamos lá e depois o movemos para o Looker, onde temos blocos configurados que estruturam e organizam nossos dados.

O Snowflake não é a única opção de depósito. Outras opções incluem [Redshift](https://aws.amazon.com/redshift/), [Google BigQuery](https://cloud.google.com/bigquery/?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-p-dr-1003905&utm_content=text-ad-none-any-DEV_c-CRE_288551384566-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+%7C+US+%7C+en+%7C+PHR+~+Big+Data+~+BigQuery+~+google+bigquery-KWID_43700035823403663-kwd-300487425311&utm_term=KW_google%20bigquery-ST_google+bigquery&gclid=EAIaIQobChMIl9OK8uHA3gIVyVmGCh1lFgB-EAAYASAAEgIfWfD_BwE) e muito mais!

### Contas de leitores do Snowflake

As Contas de Leitor da Snowflake oferecem aos usuários acesso aos mesmos dados e funcionalidades do [Compartilhamento de Dados da Snowflake]({{site.baseurl}}/partners/snowflake/), tudo sem exigir uma conta da Snowflake ou um relacionamento de cliente com a Snowflake. Com as Contas de Leitor, a Braze criará e compartilhará seus dados em uma conta e lhe fornecerá credenciais para fazer login e acessar seus dados. Isso fará com que todo o compartilhamento de dados e o faturamento do uso sejam gerenciados inteiramente pela Braze. 

Para saber mais, entre em contato com seu gerente de sucesso do cliente.

#### Recursos adicionais
Para obter recursos úteis de monitoramento de uso, consulte os artigos [Monitores de recursos](https://docs.snowflake.com/en/user-guide/resource-monitors.html) da Snowflake e [Visualização do uso de crédito do depósito](https://docs.snowflake.com/en/user-guide/credits.html#viewing-warehouse-credit-usage-for-your-account).

## Etapa 4: Use uma ferramenta de Business Intelligence (BI) para manipular seus dados

Por fim, usamos uma ferramenta de BI para analisar nossos dados, transformá-los em gráficos e outras ferramentas visuais, e muito mais, usando [o Looker e o Looker Blocks](https://www.marketplace.looker.com/), para que não precisemos fazer ETL ou ELT sempre que os dados forem transferidos do Currents.

Está se sentindo inspirado a fazer o mesmo? Confira os documentos a seguir para obter mais informações sobre eles e como você pode usá-los para criar seu banco de dados!

- [Bloco de comportamento do usuário](https://marketplace.looker.com/marketplace/detail/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)
- [Bloco de engajamento de mensagens](https://marketplace.looker.com/marketplace/detail/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)

