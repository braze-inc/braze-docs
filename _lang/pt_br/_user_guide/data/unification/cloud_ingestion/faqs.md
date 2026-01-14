---
nav_title: Perguntas frequentes
article_title: Perguntas frequentes sobre ingestão de dados na nuvem
page_order: 100
page_type: FAQ
description: "Esta página responde a perguntas frequentes sobre a ingestão de dados na nuvem."
toc_headers: h2
---

# Perguntas frequentes

> Esta página contém respostas para algumas perguntas frequentes sobre a ingestão de dados na nuvem.

## Por que me enviaram um e-mail: "Erro na sincronização do CDI"?

Esse tipo de e-mail geralmente significa que há um problema com sua configuração de CDI. Aqui estão alguns problemas comuns e como corrigi-los:

### O CDI não pode acessar o data warehouse ou a tabela usando suas credenciais

Isso pode significar que as credenciais no CDI estão incorretas ou mal configuradas no data warehouse. Para obter mais informações, consulte [Integrações de Data Warehouse]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/).

### A tabela não pode ser encontrada

Tente atualizar sua integração com a configuração correta do banco de dados ou criar recursos correspondentes no data warehouse, como `database/table`.

### O catálogo não pode ser encontrado

O catálogo configurado na integração não existe no catálogo do Braze. Um catálogo pode ser removido depois que a integração foi configurada. Para resolver o problema, atualize a integração para usar um catálogo diferente ou crie um novo catálogo que corresponda ao nome do catálogo na integração.

## Por que me enviaram um e-mail: "Erros de linha em sua sincronização de CDI"?

Esse tipo de e-mail significa que alguns de seus dados não puderam ser processados durante a sincronização. Para descobrir o erro específico, você pode revisar os registros no Braze acessando **CDI** > **Sync Log**.

## Como faço para corrigir erros na conexão de teste e nos e-mails de suporte?

{% tabs %}
{% tab Snowflake %}
### A conexão de teste é lenta

O Test Connection está sendo executado em seu data warehouse, portanto, aumentar a capacidade do warehouse pode melhorar sua velocidade. O uso de uma instância de SQL sem servidor minimizará o tempo de aquecimento e melhorará o rendimento da consulta, mas poderá resultar em custos de integração um pouco mais altos.

### Erro ao conectar-se à instância do Snowflake: A solicitação de entrada com IP não tem permissão para acessar o Snowflake

Tente adicionar os IPs oficiais do Braze à sua lista de permissões de IP. Para obter mais informações, consulte [Integrações do Data Warehouse]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/) ou permita os IPs relevantes:

{% multi_lang_include data_centers.md datacenters='ips' %}

### Erro ao executar o SQL devido à configuração do cliente: 002003 (42S02): Erro de compilação SQL: não existe ou não está autorizado

Se a tabela não existir, crie a tabela. Se a tabela existir, verifique se o usuário e a função têm permissão para ler a tabela.

### Não foi possível usar o esquema

Se receber esse erro, conceda acesso a esse esquema para o usuário ou função especificada.

### Não foi possível usar a função

Se você receber esse erro, permita que o usuário use a função especificada.

### Acesso do usuário desativado

Se receber esse erro, permita que o usuário tenha acesso à sua conta do Snowflake.

### Erro ao conectar-se à instância do Snowflake com a chave atual e a antiga

Se você receber esse erro, verifique se o usuário está usando a chave pública atual, conforme exibido no painel do Braze.
{% endtab %}

{% tab Redshift %}
### A conexão de teste é lenta

O Test Connection está sendo executado em seu data warehouse, portanto, aumentar a capacidade do warehouse pode melhorar sua velocidade. O uso de uma instância de SQL sem servidor minimizará o tempo de aquecimento e melhorará o rendimento da consulta, mas poderá resultar em custos de integração um pouco mais altos.

### Permissão negada para a relação {table_name}

Se você receber esse erro:

  - Conceda a permissão `usage` no esquema para esse usuário.
  - Conceda a permissão `select` na tabela para esse usuário.

### Erro ao criar conexão

Se você receber esse erro, verifique se o ponto de extremidade e a porta do Redshift estão corretos.

### Erro ao criar túnel SSH

Se você receber esse erro:

  - Verifique se a chave pública em seu painel do braze está no host ec2 usado para o tunelamento SSH.
  - Verifique se o seu nome de usuário está correto.
  - Verifique se o túnel SSH está correto.
{% endtab %}

{% tab BigQuery %}
### A conexão de teste é lenta

O Test Connection está sendo executado em seu data warehouse, portanto, aumentar a capacidade do warehouse pode melhorar sua velocidade. O uso de uma instância de SQL sem servidor minimizará o tempo de aquecimento e melhorará o rendimento da consulta, mas poderá resultar em custos de integração um pouco mais altos.

### O usuário não tem permissão para consultar a tabela

Se receber esse erro, adicione permissões de usuário para consultar a tabela.

### Seu uso excedeu a cota personalizada

Se você receber esse erro, sua cota precisará ser atualizada para que você possa continuar a sincronização na taxa atual.

### A tabela não foi encontrada no local {region} Local

Se você receber esse erro, verifique se a tabela está no projeto e no conjunto de dados corretos.

### Assinatura JWT inválida

Se você receber esse erro, verifique se o serviço da API do BigQuery está ativado para sua conta.
{% endtab %}

{% tab Databricks %}
### A conexão de teste é lenta

O Test Connection está sendo executado em seu data warehouse, portanto, aumentar a capacidade do warehouse pode melhorar sua velocidade. Para o Databricks, pode haver de dois a cinco minutos de tempo de aquecimento quando o Braze se conectar às instâncias Classic e Pro SQL, o que causará atrasos durante a configuração e o teste da conexão, bem como no início das sincronizações programadas. O uso de uma instância de SQL sem servidor minimizará o tempo de aquecimento e melhorará o rendimento da consulta, mas poderá resultar em custos de integração um pouco mais altos.

### O comando falhou porque o depósito foi interrompido

Se você receber esse erro, verifique se o Databricks warehouse está em execução.

### Serviço: Amazon S3; Código de status: 403; Código de erro: 403 Proibido

Se você receber esse erro, consulte [Databricks: Erro proibido ao acessar dados do S3](https://kb.databricks.com/security/forbidden-access-to-s3-data).
{% endtab %}
{% endtabs %}

## Como faço para atualizar minhas preferências de alerta por e-mail para integrações CDI?

Cada integração tem sua própria preferência de notificação. Vá para a página CDI e selecione o nome da integração que deseja atualizar. Na seção **Notification preferences (Preferências de notificação** ), é possível atualizar a forma como você recebe alertas referentes à integração selecionada.

## O que acontecerá se um futuro UPDATED_AT for sincronizado com uma integração?

O CDI usa o site `UPDATED_AT` para decidir quais dados são novos. Depois que um `UPDATED_AT` futuro for sincronizado, todos os dados anteriores a essa data e hora futuras não serão processados. Para corrigir isso:

1. Correto `UPDATED_AT`.
2. Remover todos os dados antigos que já foram sincronizados com o Braze
3. Crie uma nova integração para processar essa tabela novamente.

## Por que "Rows Synced" (Linhas sincronizadas) não corresponde ao número em meu depósito?

O CDI usa o site `UPDATED_AT` para decidir quais registros devem ser coletados durante uma sincronização. Dê uma olhada [nesta ilustração]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/overview/#what-gets-synced) para ver como funciona. No início de uma execução de sincronização, o CDI consulta o seu depósito para obter todos os registros com `UPDATED_AT` igual ou posterior ao carimbo de data/hora `UPDATED_AT` processado anteriormente. Qualquer registro coletado no momento em que a consulta for executada será sincronizado com o Braze. Aqui estão os casos comuns em que um registro pode não ser sincronizado:

- Você está adicionando registros à tabela com um valor `UPDATED_AT` que já foi processado.
- Você está atualizando os valores de registro depois que eles foram processados por uma sincronização, mas deixando o site `UPDATED_AT` inalterado. 
- Você está adicionando ou atualizando registros enquanto uma sincronização está em andamento. Dependendo de quando a consulta CDI é executada, pode haver condições de corrida que fazem com que os registros não sejam coletados.

{% alert tip %}
Para evitar esses comportamentos no futuro, recomendamos usar valores `UPDATED_AT` que aumentem monotonicamente e não atualizar a tabela durante a execução da sincronização agendada.
{% endalert %}

## Durante uma sincronização, a ordem é preservada se vários registros tiverem o mesmo ID?

A ordem de processamento não é 100% previsível. Por exemplo, se houver várias linhas com o mesmo `EXTERNAL_ID` na tabela durante uma sincronização, não poderemos garantir qual valor será incluído no perfil final. Se você estiver atualizando o mesmo `EXTERNAL_ID` com atributos diferentes na coluna de carga útil, todas as alterações serão refletidas quando a sincronização for concluída.

## Quais são as medidas de segurança do CDI?

### Nossas medidas

A Braze tem as seguintes medidas em vigor para CDI:

- Todas as credenciais são criptografadas em nosso banco de dados, e somente determinados funcionários têm acesso autenticado a elas.
- Usamos conexões criptografadas para levar os dados aos armazéns dos clientes.
- Fazemos solicitações aos endpoints da API do Braze usando as mesmas chaves de API e conexões TLS que recomendamos que nossos clientes usem.
- Atualizamos regularmente nossas bibliotecas e recebemos todos os patches de segurança.

### Suas medidas

Recomendamos que você e sua equipe configurem as seguintes medidas de segurança: 

- Restringir o acesso às credenciais ao mínimo necessário para o funcionamento da CDI. Isso se deve ao fato de que precisamos ser capazes de executar a seleção (e a contagem) nas tabelas e exibições específicas.
- Restringir os IPs que podem acessar as tabelas aos [IPs do Braze]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/.#step-1-set-up-tables-or-views) publicados oficialmente.
