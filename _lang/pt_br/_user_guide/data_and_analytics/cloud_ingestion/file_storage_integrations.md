---
nav_title: Integrações de armazenamento de arquivos
article_title: Integrações de armazenamento de arquivos
description: "Este artigo de referência aborda a ingestão de dados para nuvem da Braze e como sincronizar dados relevantes do S3 para a Braze"
page_order: 3
page_type: reference

---

# Integrações de armazenamento de arquivos

> Este artigo aborda como configurar o suporte da ingestão de dados na nuvem e sincronizar dados relevantes do S3 para a Braze.

Agora você pode usar a Ingestão de dados na nuvem (CDI) para S3 para integrar diretamente um ou mais buckets S3 em sua conta da AWS com a Braze. Quando novos arquivos são publicados no S3, uma mensagem é postada no SQS, e a Ingestão de dados para a nuvem da Braze recebe esses novos arquivos. 

A ingestão de dados na nuvem é compatível com arquivos JSON, CSV e Parquet, além de atributos, eventos, compras e dados de exclusão de usuários.

A integração requer os seguintes recursos:
 - Bucket S3 para armazenamento de dados 
 - Fila SQS para notificações de novos arquivos 
 - Função IAM para acesso ao Braze  


## Definições da AWS

Primeiro, vamos definir alguns dos termos usados nesta tarefa.

| Termo | Definição |
| --- | --- |
| Nome do recurso da Amazon (ARN) | O ARN é um identificador exclusivo dos recursos da AWS. |
| Gerenciamento de identidade e acesso (IAM) | IAM é um serviço da Web que permite controlar com segurança o acesso aos recursos da AWS. Nesse tutorial, você criará uma política de IAM e a atribuirá a uma função de IAM para integrar seu bucket S3 à ingestão de dados para nuvem da Braze. |
| Serviço de fila simples da Amazon (SQS) | O SQS é uma fila hospedada que permite integrar sistemas e componentes de software distribuídos. |
{: .reset-td-br-1 .reset-td-br-2 }
 

## Configuração da ingestão de dados na nuvem na AWS

### Etapa 1: Criar um bucket de origem

Crie um bucket S3 de uso geral com configurações padrão em sua conta da AWS. 

As configurações padrão são:
  - ACLs desativadas
  - Bloquear todo o acesso público
  - Desativar o controle de versão do bucket
  - Criptografia SSE-S3

Observe em que região você criou o bucket, pois você criará uma fila SQS na mesma região na próxima etapa.

### Etapa 2: Criar fila SQS

Crie uma fila SQS para rastrear quando os objetos são adicionados ao bucket que você criou. Use as definições de configuração padrão por enquanto.

{% alert important %}
Certifique-se de criar esse SQS na mesma região em que você criou o bucket.
{% endalert %}

Não deixe de notar o ARN e o URL do SQS, pois você o usará com frequência durante essa configuração.
<br><br>![]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})
<br><br>

### Etapa 3: Configurar a política de acesso

Para configurar a política de acesso, selecione **Opções avançadas**. 

Anexe a seguinte declaração à política de acesso da fila, tomando cuidado para substituir `YOUR-BUCKET-NAME-HERE` pelo nome do bucket, e `YOUR-SQS-ARN` pelo ARN da fila SQS e `YOUR-AWS-ACCOUNT-ID` pelo ID da conta da AWS: 

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

1. No bucket criado na etapa 1, acesse **Propriedades** > **Notificações de eventos**.

2. Dê um nome à configuração. Opcionalmente, especifique um prefixo ou sufixo para direcionamento se quiser que apenas um subconjunto de arquivos seja ingerido pela Braze.

3. Em **Destinos**, selecione a **fila SQS** e forneça o ARN do SQS que você criou na etapa 2.

### Etapa 5: Criar uma política de IAM

Crie uma política de IAM para permitir que o Braze interaja com seu bucket de origem. Para começar, faça login no console de gerenciamento do AWS como administrador da conta. 

1. Acesse a seção IAM do console da AWS, selecione **Políticas** na barra de navegação e, em seguida, selecione **Criar política**.<br><br>![]({{site.baseurl}}/assets/img/create_policy_1_list.png)<br><br>

2. Abra a guia **JSON** e insira o seguinte trecho de código na seção **Policy Document (Documento de política)**, tomando o cuidado de substituir `YOUR-BUCKET-NAME-HERE` pelo nome do bucket e `YOUR-SQS-ARN-HERE` pelo nome da fila do SQS: 

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
3\. Selecione **Revisar política** quando terminar.

4. Dê um nome e uma descrição à política e selecione **Criar política**.  

![]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### Etapa 6: Criar uma função de IAM

Para concluir a configuração na AWS, você criará uma função de IAM e anexará a ela a política de IAM da etapa 4. 

1. Na mesma seção de IAM do console em que criou a política de IAM, acesse **Roles** > **Create Role**( **Funções** > **Criar função**). <br><br>![]({{site.baseurl}}/assets/img/create_role_1_list.png)<br><br>

2. Copie o ID da conta AWS do Braze do seu dashboard. Acessar **Ingestão de Dados na Nuvem**, clique **Criar Nova Sincronização de Dados** e selecione **Importação S3**. <br><br>![]({{site.baseurl}}/assets/img/cloud_ingestion/s3_copy_braze_account_id.png)<br><br>

3. Na AWS, selecione **Outra conta AWS** como o tipo de seletor de entidade confiável. Forneça a ID de sua conta Braze, marque a caixa de seleção **Require external ID (Exigir ID externa** ) e insira uma ID externa para o Braze usar. Selecione **Next** quando terminar. <br><br> ![A página "Create Role" (Criar função) do S3. Essa página tem campos para nome da função, descrição da função, entidades confiáveis, políticas e limite de permissões.]({{site.baseurl}}/assets/img/create_role_2_another.png)

4. Anexe a política criada na etapa 4 à função. Procure a política na barra de pesquisa e marque uma marca de seleção ao lado da política para anexá-la. Selecione **Avançar** quando terminar.<br><br>![Função do ARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)<br><br>Dê um nome e uma descrição à função e clique em **Create Role (Criar função**).<br><br>![Função do ARN]({{site.baseurl}}/assets/img/create_role_4_name.png)<br><br>

{: start="5"}
5\. Note o ARN da função que você acabou de criar e o ID externo que você gerou, pois você os usará para criar a integração da ingestão de dados na nuvem.  

## Configuração da ingestão de dados na nuvem no Braze

1. Para criar uma nova integração, acesse **Configurações de dados** > **Ingestão de dados na nuvem**, selecione **Criar nova sincronização de dados** e selecione **Importação S3** na seção de fontes de arquivo. 

2. Insira as informações do processo de configuração da AWS para criar uma nova sincronização. Especifique o seguinte:
- Função do ARN
- ID externo
- URL do SQS (deve ser exclusivo para cada nova integração)
- Nome do bucket
- Jornada da pasta (opcional)
- Região  

![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3\. Dê um nome à sua integração e selecione o tipo de dados para essa integração. <br><br>![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_2.png %})<br><br>

4. Adicione um e-mail de contato para receber notificações se a sincronização for interrompida devido a problemas de acesso ou permissões. Opcionalmente, ative as notificações para erros no nível do usuário e sucessos de sincronização. <br><br> ![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_3.png %})<br><br>

{: start="5"}
5\. Por fim, teste a conexão e salve a sincronização. <br><br>![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})


## Formatos de arquivo necessários

A ingestão de dados na nuvem aceita arquivos JSON, CSV e Parquet. Cada arquivo deve conter uma ou mais colunas de identificadores compatíveis e uma coluna de carga útil como uma string JSON. 

- Identificadores de usuário. Seu arquivo de origem pode conter uma ou mais colunas ou chaves de identificador de usuário. Cada linha deve conter apenas um identificador, mas um arquivo de origem pode ter vários tipos de identificadores. 
    - `EXTERNAL_ID` - Isso identifica o usuário que você deseja atualizar. Esse valor deve corresponder ao valor `external_id` usado no Braze. 
    - `ALIAS_NAME` e `ALIAS_LABEL` \- Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.
    - `BRAZE_ID` - O identificador de usuário do Braze. Isso é gerado pelo SDK da Braze, e novos usuários não podem ser criados usando um Braze ID por meio da ingestão de dados na nuvem. Para criar novos usuários, especifique um ID de usuário externo ou um alias de usuário.
    - `EMAIL` - O endereço de e-mail do usuário. Se houver vários perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente terá prioridade para atualizações. Se você incluir e-mail e telefone, usaremos o e-mail como identificador principal.
    - `PHONE` - O número de telefone do usuário. Se houver vários perfis com o mesmo número de telefone, o perfil atualizado mais recentemente terá prioridade nas atualizações. 
- `PAYLOAD` - Essa é uma string JSON dos campos que você deseja sincronizar com o usuário no Braze.

{% alert note %}
Ao contrário das fontes de data warehouse, a coluna `UPDATED_AT` não é necessária nem aceita.
{% endalert %}

{% alert note %}
Os arquivos adicionados ao bucket de origem S3 não devem exceder 512 MB. Arquivos com mais de 512 MB gerarão um erro e não serão sincronizados com a Braze.
{% endalert %}

{% tabs %}
{% tab Atribuições JSON %}
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
{% tab Eventos personalizados JSON %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```  
{% alert important %}
Todas as linhas do seu arquivo de origem devem conter JSON válido, ou o arquivo será ignorado.
{% endalert %}
{% endtab %}
{% tab Eventos de compra JSON %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```  
{% alert important %}
Todas as linhas do seu arquivo de origem devem conter JSON válido, ou o arquivo será ignorado.
{% endalert %}

{% endtab %}
{% tab Atribuições CSV %}
``` csv  
external_id,payload
s3-qa-load-0-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""SNXIM"", ""age"": 54, ""subscriber"": true, ""retention"": {""previous_purchases"": 19, ""vip"": true}, ""last_visit"": ""2023-08-08T16:03:26.598806""}"
s3-qa-load-1-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""0J747"", ""age"": 73, ""subscriber"": false, ""retention"": {""previous_purchases"": 22, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598816""}"
s3-qa-load-2-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""EP1U0"", ""age"": 99, ""subscriber"": false, ""retention"": {""previous_purchases"": 23, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598822""}"
```
{% endtab %}
{% endtabs %}  

Para obter exemplos de todos os tipos de arquivos aceitos, consulte os arquivos de amostra em [Braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage).  
