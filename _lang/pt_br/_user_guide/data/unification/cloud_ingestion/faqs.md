---
nav_title: Perguntas frequentes
article_title: Perguntas frequentes sobre ingestão de dados na nuvem
page_order: 100
page_type: FAQ
description: "Esta página responde às perguntas frequentes sobre a ingestão de dados na nuvem."
toc_headers: h2
---

# Perguntas frequentes

> Esta página contém respostas para algumas perguntas frequentes sobre a ingestão de dados na nuvem.

## Por que recebi o e-mail: "Erro na sincronização do CDI"?

Esse tipo de e-mail geralmente significa que há um problema com a configuração do seu CDI. Aqui estão alguns problemas comuns e como corrigi-los:

### O CDI não consegue acessar o data warehouse ou a tabela usando suas credenciais

Isso pode significar que as credenciais no CDI estão incorretas ou mal configuradas no data warehouse. Para saber mais, consulte [Integrações de data warehouse]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/).

### A tabela não pode ser encontrada

Tente atualizar sua integração com a configuração correta do banco de dados ou criar recursos correspondentes no data warehouse, como `database/table`.

### O catálogo não pode ser encontrado

O catálogo configurado na integração não existe no catálogo da Braze. Um catálogo pode ser removido depois que a integração foi configurada. Para resolver o problema, atualize a integração para usar um catálogo diferente ou crie um novo catálogo que corresponda ao nome do catálogo na integração.

## Por que recebi o e-mail: "Erros de linha na sua sincronização de CDI"?

Esse tipo de e-mail significa que alguns dos seus dados não puderam ser processados durante a sincronização. Para descobrir o erro específico, você pode revisar os registros na Braze acessando **CDI** > **Sync Log**.

## Como faço para corrigir erros na conexão de teste e nos e-mails de suporte?

{% tabs %}
{% tab Snowflake %}
### A conexão de teste é lenta

A conexão de teste está sendo executada no seu data warehouse, portanto, aumentar a capacidade do data warehouse pode melhorar sua velocidade. O uso de uma instância de SQL sem servidor minimizará o tempo de aquecimento e melhorará a taxa de transferência da consulta, mas poderá resultar em custos de integração ligeiramente mais altos.

### Erro ao conectar-se à instância do Snowflake: a solicitação de entrada com IP não tem permissão para acessar o Snowflake

Tente adicionar os IPs oficiais da Braze à sua lista de permissões de IP. Para saber mais, consulte [Integrações de data warehouse]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/), ou permita os IPs relevantes:

{% multi_lang_include data_centers.md datacenters='ips' %}

### Erro ao executar o SQL devido à configuração do cliente: 002003 (42S02): erro de compilação SQL: não existe ou não está autorizado

Se a tabela não existir, crie a tabela. Se a tabela existir, verifique se o usuário e a função têm permissão para ler a tabela.

### Não foi possível usar o esquema

Se receber esse erro, conceda acesso a esse esquema para o usuário ou função especificada.

### Não foi possível usar a função

Se você receber esse erro, permita que esse usuário use a função especificada.

### Acesso do usuário desativado

Se receber esse erro, permita que esse usuário tenha acesso à sua conta do Snowflake.

### Erro ao se conectar à instância do Snowflake com a chave atual e a antiga

Se receber esse erro, verifique se o usuário está usando a chave pública atual, conforme exibido no dashboard da Braze.
{% endtab %}

{% tab Redshift %}
### A conexão de teste é lenta

A conexão de teste está sendo executada no seu data warehouse, portanto, aumentar a capacidade do data warehouse pode melhorar sua velocidade. O uso de uma instância de SQL sem servidor minimizará o tempo de aquecimento e melhorará a taxa de transferência da consulta, mas poderá resultar em custos de integração ligeiramente mais altos.

### Permissão negada para a relação {table_name}

Se você receber esse erro:

  - Conceda a permissão `usage` no esquema para esse usuário.
  - Conceda a permissão `select` na tabela para esse usuário.

### Erro ao criar conexão

Se você receber esse erro, verifique se o endpoint e a porta do Redshift estão corretos.

### Erro ao criar túnel SSH

Se você receber esse erro:

  - Verifique se a chave pública no seu dashboard da Braze está no host ec2 usado para o tunelamento SSH.
  - Verifique se o seu nome de usuário está correto.
  - Verifique se o túnel SSH está correto.
{% endtab %}

{% tab BigQuery %}
### A conexão de teste é lenta

A conexão de teste está sendo executada no seu data warehouse, portanto, aumentar a capacidade do data warehouse pode melhorar sua velocidade. O uso de uma instância de SQL sem servidor minimizará o tempo de aquecimento e melhorará a taxa de transferência da consulta, mas poderá resultar em custos de integração ligeiramente mais altos.

### O usuário não tem permissão para consultar a tabela

Se receber esse erro, adicione permissões de usuário para consultar a tabela.

### Seu uso excedeu a cota personalizada

Se receber esse erro, sua cota precisará ser atualizada para que você possa continuar sincronizando na taxa atual.

### A tabela não foi encontrada no local {region}

Se você receber esse erro, verifique se a tabela está no projeto e no conjunto de dados corretos.

### Assinatura JWT inválida

Se você receber esse erro, verifique se o serviço da API do BigQuery está ativado na sua conta.
{% endtab %}

{% tab Databricks %}
### A conexão de teste é lenta

A conexão de teste está sendo executada no seu data warehouse, portanto, aumentar a capacidade do data warehouse pode melhorar sua velocidade. Para o Databricks, pode haver de dois a cinco minutos de tempo de aquecimento quando a Braze se conecta às instâncias do SQL Classic e Pro, o que causará atrasos durante a configuração e o teste da conexão, bem como no início das sincronizações programadas. O uso de uma instância de SQL sem servidor minimizará o tempo de aquecimento e melhorará a taxa de transferência da consulta, mas poderá resultar em custos de integração ligeiramente mais altos.

### O comando falhou porque o warehouse foi interrompido

Se você receber esse erro, verifique se o Databricks warehouse está em execução.

### Serviço: Amazon S3; Código de status: 403; Código de erro: 403 Forbidden

Se você receber esse erro, consulte [Databricks: Erro forbidden ao acessar dados do S3](https://kb.databricks.com/security/forbidden-access-to-s3-data).
{% endtab %}
{% endtabs %}

## Como faço para atualizar minhas preferências de alerta por e-mail para integrações CDI?

Cada integração tem sua própria preferência de notificação. Acesse a página do CDI e selecione o nome da integração que deseja atualizar. Na seção **Notification preferences**, é possível atualizar a forma como você recebe alertas referentes à integração selecionada.

## O que acontece se um UPDATED_AT futuro for sincronizado com uma integração?

O CDI usa `UPDATED_AT` para decidir quais dados são novos. Depois que um `UPDATED_AT` futuro for sincronizado, todos os dados anteriores a essa data e hora futuras não serão processados. Para corrigir isso:

1. Corrija `UPDATED_AT`.
2. Remova quaisquer dados antigos que já estejam sincronizados com a Braze.
3. Crie uma nova integração para processar essa tabela novamente.

## Por que "Rows Synced" não corresponde ao número no meu data warehouse?

O CDI usa `UPDATED_AT` para decidir quais registros devem ser coletados durante uma sincronização. Dê uma olhada [nesta ilustração]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/overview/#what-gets-synced) para ver como funciona. No início de uma execução de sincronização, o CDI consulta seu data warehouse para obter todos os registros com `UPDATED_AT` posterior ao valor `UPDATED_AT` processado anteriormente. Registros no timestamp exato do limite também podem ser ressincronizados se novas linhas compartilharem esse timestamp. Qualquer registro coletado no momento em que a consulta for executada será sincronizado com a Braze. Aqui estão os casos comuns em que um registro pode não ser sincronizado:

- Você está adicionando registros à tabela com um valor `UPDATED_AT` que já foi processado.
- Você está atualizando os valores de registro depois que eles foram processados por uma sincronização, mas deixando `UPDATED_AT` inalterado. 
- Você está adicionando ou atualizando registros enquanto uma sincronização está em andamento. Dependendo de quando a consulta do CDI é executada, pode haver condições de corrida que fazem com que os registros não sejam coletados.

{% alert tip %}
Para evitar esses comportamentos no futuro, recomendamos usar valores `UPDATED_AT` que aumentem monotonicamente e não atualizar a tabela durante a execução da sincronização agendada.
{% endalert %}

## Durante uma sincronização, a ordem é preservada se vários registros tiverem o mesmo ID?

A ordem de processamento não é 100% previsível. Por exemplo, se houver várias linhas com o mesmo `EXTERNAL_ID` na tabela durante uma sincronização, não é possível garantir qual valor será incluído no perfil final. Se você estiver atualizando o mesmo `EXTERNAL_ID` com atributos diferentes na coluna de carga útil, todas as alterações serão refletidas quando a sincronização for concluída.

## Por que novos usuários não estão sendo criados a partir da minha sincronização do CDI?

Se sua integração do CDI tiver a opção **Atualizar apenas usuários existentes** ativada, apenas os usuários que já existem na Braze são atualizados, e novos usuários não são criados. Isso significa que, se uma linha na sua tabela de sincronização referenciar um `EXTERNAL_ID` que não corresponda a nenhum usuário existente na Braze, essa linha será ignorada.

Para criar novos usuários através do CDI, desative o toggle **Atualizar apenas usuários existentes** nas configurações da sua integração. Acesse **Configurações de Dados** > **Ingestão de Dados na Nuvem** e selecione uma integração.

## Quais são as medidas de segurança do CDI?

### Nossas medidas

A Braze tem as seguintes medidas em vigor para o CDI:

- Todas as credenciais são criptografadas em nosso banco de dados, e somente determinados colaboradores têm acesso autenticado a elas.
- Usamos conexões criptografadas para transferir dados aos data warehouses dos clientes.
- Fazemos solicitações aos endpoints da API da Braze usando as mesmas chaves de API e conexões TLS que recomendamos que nossos clientes usem.
- Atualizamos regularmente nossas bibliotecas e aplicamos todos os patches de segurança.

### Suas medidas

Recomendamos que você e sua equipe configurem as seguintes medidas de segurança do seu lado: 

- Restrinja o acesso às credenciais ao mínimo necessário para o funcionamento do CDI. Isso porque precisamos ser capazes de executar select (e count) nas tabelas e visualizações específicas.
- Restrinja os IPs que podem acessar as tabelas aos [IPs da Braze]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/.#step-1-set-up-tables-or-views) publicados oficialmente.