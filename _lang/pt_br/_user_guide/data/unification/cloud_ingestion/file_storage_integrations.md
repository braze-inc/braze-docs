---
nav_title: Integrações de armazenamento de arquivos
article_title: Integrações de Armazenamento de Arquivos
description: "Esta página cobre a Ingestão de Dados na Nuvem da Braze e como sincronizar dados relevantes do S3 para a Braze."
page_order: 3
page_type: reference

---

# Integrações de armazenamento de arquivos

> Esta página aborda como configurar o suporte da Ingestão de Dados na Nuvem e sincronizar dados relevantes do S3 para a Braze.

Esta página mostra as etapas de sincronização e origem que estão atualmente em Acesso Antecipado (EA). Para as etapas da experiência geralmente disponível, consulte [Experiência de disponibilidade geral](#general-availability-experience).

## Como funciona

Você pode usar a Ingestão de Dados na Nuvem (CDI) para S3 para integrar diretamente um ou mais buckets S3 na sua conta AWS com a Braze. Quando novos arquivos são publicados no S3, uma mensagem é postada no SQS, e a Ingestão de Dados na Nuvem da Braze recebe esses novos arquivos. 

A Ingestão de Dados na Nuvem suporta o seguinte:

- Arquivos JSON
- Arquivos CSV
- Arquivos Parquet
- Dados de atributos, eventos personalizados, eventos de compra, exclusão de usuários e catálogos

## Pré-requisitos

A integração requer os seguintes recursos:

 - Bucket S3 para armazenamento de dados 
 - Fila SQS para notificações de novos arquivos 
 - Função IAM para acesso da Braze  

### Definições da AWS

Primeiro, vamos definir os termos usados durante esta tarefa.

| Termo | Definição |
| --- | --- |
| Nome do Recurso da Amazon (ARN) | O ARN é um identificador exclusivo dos recursos da AWS. |
| Gerenciamento de Identidade e Acesso (IAM) | IAM é um serviço da web que permite controlar com segurança o acesso aos recursos da AWS. Neste tutorial, você criará uma política de IAM e a atribuirá a uma função de IAM para integrar seu bucket S3 à Ingestão de Dados na Nuvem da Braze. |
| Serviço de Fila Simples da Amazon (SQS) | O SQS é uma fila hospedada que permite integrar sistemas e componentes de software distribuídos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Configuração da Ingestão de Dados na Nuvem na AWS

### Etapa 1: Criar um bucket de origem

Crie um bucket S3 de uso geral com configurações padrão na sua conta AWS. Buckets S3 podem ser reutilizados em sincronizações desde que a pasta seja única.

As configurações padrão são:

- ACLs desativadas
- Bloquear todo o acesso público
- Desativar o controle de versão do bucket
- Criptografia SSE-S3
  - SSE-S3 é o único tipo de criptografia do lado do servidor suportado. A criptografia do Amazon KMS não é suportada.

Anote a região em que você criou o bucket — você criará uma fila SQS na mesma região na próxima etapa.

### Etapa 2: Criar fila SQS

Crie uma fila SQS para rastrear quando os objetos são adicionados ao bucket que você criou. Use as definições de configuração padrão por enquanto. 

Uma fila SQS deve ser única globalmente (por exemplo, apenas uma pode ser usada para uma sincronização CDI e não pode ser reutilizada em outro espaço de trabalho).

{% alert important %}
Certifique-se de criar esta SQS na mesma região em que você criou o bucket.
{% endalert %}

Anote o ARN e o URL da fila SQS — você precisará deles com frequência durante esta configuração.

![Selecionando "Avançado" com um objeto JSON de exemplo para definir quem pode acessar uma fila.]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})

### Etapa 3: Configurar a política de acesso

Para configurar a política de acesso, selecione **Opções avançadas**. 

Anexe a seguinte declaração à política de acesso da fila, tomando cuidado para substituir `YOUR-BUCKET-NAME-HERE` pelo nome do bucket, `YOUR-SQS-ARN` pelo ARN da fila SQS e `YOUR-AWS-ACCOUNT-ID` pelo ID da conta da AWS: 

``` json 
{
  "Sid": "braze-cdi-s3-sqs-publish",
  "Effect": "Allow",
  "Principal": {
    "Service": "s3.amazonaws.com"
  },
  "Action": "SQS:SendMessage",
  "Resource": "YOUR-SQS-ARN",
  "Condition": {
    "StringEquals": {
      "aws:SourceAccount": "YOUR-AWS-ACCOUNT-ID"
    },
    "ArnLike": {
      "aws:SourceArn": "arn:aws:s3:::YOUR-BUCKET-NAME-HERE"
    }
  }
} 
```

### Etapa 4: Adicionar uma notificação de evento ao bucket S3

1. No bucket criado na etapa 1, acesse **Properties** > **Event notifications**.
2. Dê um nome à configuração. Opcionalmente, especifique um prefixo ou sufixo para direcionamento se quiser que apenas um subconjunto de arquivos seja ingerido pela Braze.
3. Em **Destination**, selecione **SQS queue** e forneça o ARN da SQS que você criou na etapa 2.

{% alert note %}
Se você fizer upload dos seus arquivos para a pasta raiz de um bucket S3 e depois mover alguns dos arquivos para uma pasta específica no bucket, pode encontrar um erro inesperado. Em vez disso, você pode alterar as notificações de evento para enviar apenas para os arquivos no prefixo, evitar colocar arquivos no bucket S3 fora desse prefixo ou atualizar a integração sem prefixo, o que fará com que todos os arquivos sejam ingeridos.
{% endalert %}

### Etapa 5: Criar uma política de IAM

Crie uma política de IAM para permitir que a Braze interaja com seu bucket de origem. Para começar, faça login no console de gerenciamento da AWS como administrador da conta. 

1. Acesse a seção IAM do console da AWS, selecione **Policies** na barra de navegação e, em seguida, selecione **Create Policy**.<br><br>![O botão "Create policy" no Console da AWS.]({% image_buster /assets/img/create_policy_1_list.png %})<br><br>

2. Abra a guia **JSON** e insira o seguinte trecho de código na seção **Policy Document**, tomando o cuidado de substituir `YOUR-BUCKET-NAME-HERE` pelo nome do bucket e `YOUR-SQS-ARN-HERE` pelo nome da fila do SQS: 

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE/*"]
        },
        {
            "Effect": "Allow",
            "Action": [
                "sqs:DeleteMessage",
                "sqs:GetQueueUrl",
                "sqs:ReceiveMessage",
                "sqs:GetQueueAttributes"
            ],
            "Resource": "YOUR-SQS-ARN-HERE"
        }
    ]
}

```  

{: start="3"}
3. Selecione **Review Policy** quando terminar.

4. Dê um nome e uma descrição à política e selecione **Create Policy**.  

![Uma política de exemplo chamada "new-policy-name."]({% image_buster /assets/img/create_policy_3_name.png %})

![O campo de descrição para a política.]({% image_buster /assets/img/create_policy_4_created.png %})

### Etapa 6: Criar uma função de IAM

Para concluir a configuração na AWS, crie uma função de IAM e anexe a ela a política de IAM da etapa 5. 

1. Na mesma seção de IAM do console em que criou a política de IAM, acesse **Roles** > **Create Role**. 

![O botão "Create Role".]({% image_buster /assets/img/create_role_1_list.png %})

{: start="2"}
2. Na AWS, selecione **Another AWS Account** como o tipo de seletor de entidade confiável. Forneça seu ID de conta da Braze. Marque a caixa de seleção **Require external ID**.
3. Na Braze, acesse **Data Settings** > **Cloud Data Ingestion** > **Sources**, selecione **Add data source** e selecione **Amazon S3** na seção de fontes de arquivo.
4. Copie o **Braze Account ID** gerado automaticamente. 

![A página "Add New Source" mostrando as seções Source Name e S3 Connection Details.]({% image_buster /assets/img/braze_account_id.png %})

{: start="6"}
5. Na AWS, cole o ID da conta e selecione **Next**.

![A página "Create Role" do S3. Essa página tem campos para nome da função, descrição da função, entidades confiáveis, políticas e limite de permissões.]({% image_buster /assets/img/create_role_2_another.png %})<br><br>

{: start="7"}
6. Anexe a política criada na etapa 5 à função. Procure a política na barra de pesquisa e marque a caixa de seleção ao lado da política para anexá-la. Selecione **Next** quando terminar.

![ARN da função com a nova política selecionada.]({% image_buster /assets/img/create_role_3_attach.png %})

Dê um nome e uma descrição à função e selecione **Create Role**.

![Uma função de exemplo chamada "new-role-name".]({% image_buster /assets/img/create_role_4_name.png %})

{: start="8"}
7. Anote o ARN da função que você criou e o ID externo que você gerou, pois você precisará deles para criar a integração de Ingestão de Dados na Nuvem.

## Configuração da Ingestão de Dados na Nuvem na Braze

1. Primeiro, crie uma nova origem no dashboard da Braze. Acesse **Data Settings** > **Cloud Data Ingestion** > **Sources**, selecione **Add data source** e, em seguida, selecione **Amazon S3**.
2. Escolha um nome para sua origem e insira as informações do processo de configuração da AWS para criar uma nova origem. Especifique o seguinte:

  - ARN da função
  - ID externo
  - Nome do bucket
  - Região

![A seção S3 Connection Details mostrando Credentials (configuração da AWS e da Braze) e campos de Configuration.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3. Selecione **Test connection** para confirmar que a Braze pode acessar seu bucket. Após um teste bem-sucedido, selecione **Connect to Source**. Se a conexão falhar, uma mensagem de erro será exibida para ajudar a solucionar o problema.

{: start="4"}
4. Em seguida, crie uma nova sincronização. Acesse **Data Settings** > **Cloud Data Ingestion** > **Syncs** e selecione **Create data sync**.

![A página "Create New Sync" mostrando o nome da sincronização e a configuração da fonte de dados.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_3.png %})

{: start="5"}
5. Escolha um nome para sua sincronização. Em seguida, selecione qualquer origem S3 ativa e insira sua tabela de origem para a sincronização. Selecione um tipo de dado e selecione **Test Connection**.

![Uma opção para testar a conexão com uma prévia de dados.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

6. Insira as informações restantes do processo de configuração da AWS. Especifique o seguinte:
- URL do SQS (deve ser exclusivo para cada nova integração)
- Caminho da pasta (opcional, deve ser único entre as sincronizações em um espaço de trabalho)

7. Selecione um tipo de dado e selecione **Test Connection** para confirmar que a Braze pode listar os arquivos disponíveis para ingestão (não os dados dentro desses arquivos). Após o sucesso, selecione **Next: Notifications**.
8. Adicione e-mail(s) de contato para notificações se a sincronização for interrompida devido a problemas de acesso ou permissões. Opcionalmente, ative as notificações para erros no nível do usuário e sucessos de sincronização.
9. Crie a sincronização.

{% details Experiência de disponibilidade geral %}

1. Para criar uma nova integração, acesse **Data Settings** > **Cloud Data Ingestion**, selecione **Create New Data Sync** e selecione **S3 Import** na seção de fontes de arquivo. 
2. Insira as informações do processo de configuração da AWS para criar uma nova sincronização. Especifique o seguinte:

  - ARN da função
  - ID externo
  - URL do SQS (deve ser exclusivo para cada nova integração)
  - Nome do bucket
  - Caminho da pasta (opcional, deve ser único entre as sincronizações em um espaço de trabalho)
  - Região

{: start="3"}
3. Nomeie sua integração e selecione o tipo de dado para esta integração. 

{: start="4"}
4. Adicione um e-mail de contato para receber notificações se a sincronização for interrompida devido a problemas de acesso ou permissões. Opcionalmente, ative as notificações para erros no nível do usuário e sucessos de sincronização. 

{: start="5"}
5. Por fim, selecione **Test connection** para confirmar que a Braze pode acessar seu bucket e listar os arquivos disponíveis para ingestão (não os dados dentro desses arquivos). Em seguida, salve a sincronização. 

{% enddetails %}

## Formatos de arquivo necessários

A Ingestão de Dados na Nuvem aceita arquivos JSON, CSV e Parquet. As colunas obrigatórias dependem do tipo de dado:

- Dados de usuários (atributos, eventos personalizados, eventos de compra) usam identificadores de usuário e uma carga útil
- Dados de catálogo usam identificadores de catálogo

A Braze não impõe requisitos adicionais de nome de arquivo além do que é imposto pela AWS. Os nomes dos arquivos devem ser únicos. Adicionar um timestamp ajuda a garantir a exclusividade.

Para exemplos de todos os tipos de arquivo suportados (atributos, eventos personalizados, compras, catálogos e exclusões de usuários), consulte os arquivos de amostra em [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage).

### Identificadores de usuário {#user-identifiers}

Para sincronizações de dados de usuários (atributos, eventos personalizados, eventos de compra), cada linha no seu arquivo de origem requer exatamente um identificador de usuário e uma coluna `PAYLOAD`. Um arquivo de origem pode conter linhas com diferentes tipos de identificadores, mas cada linha individual deve usar apenas um.

| Identificador | Descrição |
| --- | --- |
| `EXTERNAL_ID` | Identifica o usuário que você deseja atualizar. Esse valor deve corresponder ao valor `external_id` usado na Braze. |
| `ALIAS_NAME` e `ALIAS_LABEL` | Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador único, e `alias_label` especifica o tipo de alias. Os usuários podem ter múltiplos aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`. |
| `BRAZE_ID` | O identificador de usuário da Braze. Isso é gerado pelo SDK da Braze, e novos usuários não podem ser criados usando um Braze ID por meio da Ingestão de Dados na Nuvem. Para criar novos usuários, especifique um ID externo ou um alias de usuário. |
| `EMAIL` | O endereço de e-mail do usuário. Se houver vários perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente terá prioridade nas atualizações. Se você incluir e-mail e telefone, a Braze usará o e-mail como identificador principal. |
| `PHONE` | O número de telefone do usuário. Se houver vários perfis com o mesmo número de telefone, o perfil atualizado mais recentemente terá prioridade nas atualizações. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Além de um identificador, cada linha deve incluir uma coluna `PAYLOAD` contendo uma string JSON dos campos que você deseja sincronizar com o usuário na Braze.

{% alert note %}
Diferente das fontes de data warehouse, a coluna `UPDATED_AT` não é obrigatória nem suportada para sincronizações de armazenamento de arquivos.
{% endalert %}

### Identificadores de catálogo {#catalog-identifiers}

Para sincronizações de catálogo, seu arquivo de origem deve conter as seguintes colunas. Arquivos de catálogo usam identificadores diferentes dos arquivos de dados de usuários.

| Coluna | Obrigatória | Descrição |
| --- | --- | --- |
| `ID` | Sim | O identificador único do item do catálogo. Usado para criar, atualizar ou excluir o item na Braze. |
| `PAYLOAD` | Sim | Uma string JSON dos campos e valores do catálogo a serem sincronizados. Deve corresponder ao esquema do seu catálogo na Braze. |
| `DELETED` | Não | Quando `true`, o item do catálogo com o `ID` correspondente é removido do catálogo na Braze. Omita esta coluna ou defina como `false` para operações de criação ou atualização. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Exemplos

{% tabs %}
{% tab JSON Attributes %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"name\": \"GT896\", \"age\": 74, \"subscriber\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
{"external_id":"s3-qa-1","payload":"{\"name\": \"HSCJC\", \"age\": 86, \"subscriber\": false, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600824\"}"}
{"external_id":"s3-qa-2","payload":"{\"name\": \"YTMQZ\", \"age\": 43, \"subscriber\": false, \"retention\": {\"previous_purchases\": 23, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600831\"}"}
{"external_id":"s3-qa-3","payload":"{\"name\": \"5P44M\", \"age\": 15, \"subscriber\": true, \"retention\": {\"previous_purchases\": 7, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600838\"}"}
{"external_id":"s3-qa-4","payload":"{\"name\": \"WMYS7\", \"age\": 11, \"subscriber\": true, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600844\"}"}
{"external_id":"s3-qa-5","payload":"{\"name\": \"KCBLK\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 11, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600850\"}"}
{"external_id":"s3-qa-6","payload":"{\"name\": \"T93MJ\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 10, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600856\"}"}
```  
{% alert important %}
Todas as linhas do seu arquivo de origem devem conter JSON válido, ou o arquivo será ignorado. 
{% endalert %}
{% endtab %}
{% tab JSON Custom Events %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```  
{% alert important %}
Todas as linhas do seu arquivo de origem devem conter JSON válido, ou o arquivo será ignorado. 
{% endalert %}
{% endtab %}
{% tab JSON Purchase Events %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```  
{% alert important %}
Todas as linhas do seu arquivo de origem devem conter JSON válido, ou o arquivo será ignorado.
{% endalert %}

{% endtab %}
{% tab CSV Attributes %}
```plaintext  
external_id,payload
s3-qa-load-0-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""SNXIM"", ""age"": 54, ""subscriber"": true, ""retention"": {""previous_purchases"": 19, ""vip"": true}, ""last_visit"": ""2023-08-08T16:03:26.598806""}"
s3-qa-load-1-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""0J747"", ""age"": 73, ""subscriber"": false, ""retention"": {""previous_purchases"": 22, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598816""}"
s3-qa-load-2-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""EP1U0"", ""age"": 99, ""subscriber"": false, ""retention"": {""previous_purchases"": 23, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598822""}"
```
{% endtab %}
{% tab CSV Catalogs  %}
```plaintext  
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
Inclua uma coluna opcional `DELETED`. Quando `DELETED` é `true`, esse item de catálogo é removido do catálogo na Braze. Para a lista completa de colunas obrigatórias, consulte [Identificadores de catálogo](#catalog-identifiers). Para o comportamento de exclusão, consulte [Excluindo itens do catálogo](#deleting-catalog-items).
{% endtab %}

{% endtabs %}  

## Excluindo dados

A Ingestão de Dados na Nuvem para S3 suporta a exclusão de usuários e itens do catálogo por meio de uploads de arquivos. Use sincronizações e formatos de arquivo separados para cada um.

- **[Excluindo usuários](#deleting-users)** – Crie uma sincronização com o tipo de dado **Delete Users** e faça upload de arquivos que contenham apenas identificadores de usuários (sem carga útil).
- **[Excluindo itens do catálogo](#deleting-catalog-items)** – Use sua sincronização de catálogo existente e adicione uma coluna `deleted` (ou `DELETED`) para marcar itens para remoção.

### Excluindo usuários

Para excluir perfis de usuários na Braze usando arquivos no S3:

1. Crie uma nova sincronização de Ingestão de Dados na Nuvem (mesma [configuração da AWS e da Braze](#setting-up-cloud-data-ingestion-in-aws) que para outras sincronizações).
2. Ao configurar a sincronização na Braze, defina **Data Type** como **Delete Users**.
3. Faça upload de arquivos para seu bucket S3 que contenham apenas colunas de identificador de usuário. Não inclua uma coluna `PAYLOAD` — a sincronização falha se a carga útil estiver presente, para evitar exclusões acidentais.

Cada linha no arquivo deve identificar exatamente um usuário usando um dos seguintes:

| Identificador | Descrição |
| --- | --- |
| `EXTERNAL_ID` | Corresponde ao `external_id` usado na Braze. |
| `ALIAS_NAME` e `ALIAS_LABEL` | Ambas as colunas juntas identificam o usuário por alias. |
| `BRAZE_ID` | ID de usuário gerado pela Braze (apenas usuários existentes). |

{% alert important %}
A exclusão de usuários é permanente e não pode ser desfeita. Inclua apenas usuários que você realmente pretende remover. Para mais detalhes, consulte [Excluir usuários com Ingestão de Dados na Nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/delete_users/).
{% endalert %}

**Exemplo – JSON (exclusão de usuários):**
```jsonl
{"external_id":"user-to-delete-001"}
{"external_id":"user-to-delete-002"}
{"braze_id":"braze-id-from-profile"}
```

**Exemplo – CSV (exclusão de usuários):**
```plaintext
external_id
user-to-delete-001
user-to-delete-002
```

Quando a sincronização é executada, a Braze processa novos arquivos no bucket e exclui os perfis de usuário correspondentes.

### Excluindo itens do catálogo

Para remover itens de um catálogo usando armazenamento de arquivos:

1. Use a mesma sincronização S3 que você usa para [sincronizar dados do catálogo]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/) (tipo de dado **Catalogs**).
2. Nos seus arquivos CSV ou JSON, adicione uma coluna opcional **`deleted`** (ou **`DELETED`**).
3. Defina `deleted` como `true` para qualquer item do catálogo que você deseja remover do catálogo na Braze.

Cada linha ainda precisa de `ID` e `PAYLOAD`. Para linhas marcadas para exclusão, a carga útil pode ser mínima; a Braze remove o item pelo `ID`.

**Exemplo – JSON (exclusão de item do catálogo):**
```jsonl
{"id":"85","payload":"{\"product_name\": \"Product 85\", \"price\": 85.85}"}
{"id":"1","payload":"{\"product_name\": \"Product 1\", \"price\": 1.01}","deleted":true}
```

**Exemplo – CSV (exclusão de item do catálogo):**
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```

Quando a sincronização é executada, linhas com `deleted: true` fazem com que o item do catálogo correspondente seja excluído na Braze. Para o comportamento completo de sincronização e exclusão do catálogo, consulte [Sincronizar e excluir dados do catálogo]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/).

## Informações importantes

- Os arquivos adicionados ao bucket de origem S3 não devem exceder 512&nbsp;MB. Arquivos maiores que 512&nbsp;MB resultarão em um erro e não serão sincronizados com a Braze.
- Embora não haja limite adicional no número de linhas por arquivo, recomendamos usar arquivos menores para melhorar a velocidade das suas sincronizações. Por exemplo, um arquivo de 500&nbsp;MB levaria consideravelmente mais tempo para ser ingerido do que cinco arquivos separados de 100&nbsp;MB.
- Não há limite adicional no número de arquivos enviados em um determinado período.
- A ordenação não é suportada dentro ou entre arquivos. Recomendamos agrupar atualizações periodicamente se você estiver monitorando possíveis condições de corrida.

## Solução de problemas

### Upload e processamento de arquivos

O CDI só processará arquivos que forem adicionados após a criação da sincronização. Nesse processo, a Braze procura novos arquivos sendo adicionados, o que aciona uma nova mensagem para o SQS. Isso inicia uma nova sincronização para processar o novo arquivo.

Você pode usar arquivos existentes para validar se a Braze consegue acessar seu bucket e detectar arquivos para ingestão, mas eles não são sincronizados com a Braze. Para que o CDI os processe, você deve fazer upload novamente para o S3 de quaisquer arquivos existentes que deseja sincronizar. 

### Tratando erros inesperados de arquivos

Se você estiver observando um alto número de erros ou arquivos com falha, pode haver outro processo adicionando arquivos ao bucket S3 em uma pasta diferente da pasta de destino do CDI.

Quando arquivos são enviados para o bucket de origem, mas não na pasta de origem, o CDI processará a notificação do SQS, mas não tomará nenhuma ação sobre o arquivo, então isso pode aparecer como um erro.