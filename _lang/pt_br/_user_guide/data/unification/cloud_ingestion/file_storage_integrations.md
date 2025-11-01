---
nav_title: Integrações de armazenamento de arquivos
article_title: Integrações de armazenamento de arquivos
description: "Esta página aborda a ingestão de dados do Braze Cloud e como sincronizar dados relevantes do S3 para o Braze."
page_order: 3
page_type: reference

---

# Integrações de armazenamento de arquivos

> Esta página aborda como configurar o suporte à ingestão de dados na nuvem e sincronizar dados relevantes do S3 para o Braze.

## Como funciona

Você pode usar o Cloud Data Ingestion (CDI) para S3 para integrar diretamente um ou mais buckets S3 em sua conta do AWS com o Braze. Quando novos arquivos são publicados no S3, uma mensagem é postada no SQS, e o Braze Cloud Data Ingestion recebe esses novos arquivos. 

A ingestão de dados na nuvem oferece suporte ao seguinte:

- Arquivos JSON
- Arquivos CSV
- Arquivos de parquet
- Atributo, evento personalizado, evento de compra, exclusão de usuário e dados de catálogo

## Pré-requisitos

A integração requer os seguintes recursos:

 - Balde S3 para armazenamento de dados 
 - Fila SQS para notificações de novos arquivos 
 - Função IAM para acesso ao Braze  

### Definições da AWS

Primeiro, vamos definir alguns dos termos usados durante esta tarefa.

| Prazo | Definição |
| --- | --- |
| Nome do recurso amazônico (ARN) | O ARN é um identificador exclusivo dos recursos do AWS. |
| Gerenciamento de identidade e acesso (IAM) | O IAM é um serviço da Web que permite controlar com segurança o acesso aos recursos do AWS. Neste tutorial, você criará uma política de IAM e a atribuirá a uma função de IAM para integrar seu bucket S3 ao Braze Cloud Data Ingestion. |
| Serviço de fila simples da Amazon (SQS) | O SQS é uma fila hospedada que permite integrar sistemas e componentes de software distribuídos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Configuração da ingestão de dados na nuvem no AWS

### Etapa 1: Criar um bucket de origem

Crie um bucket S3 de uso geral com configurações padrão em sua conta do AWS. Os buckets S3 podem ser reutilizados em várias sincronizações, desde que a pasta seja exclusiva.

As configurações padrão são:

- ACLs desativadas
- Bloquear todo o acesso público
- Desativar o controle de versão do bucket
- Criptografia SSE-S3

Anote a região em que você criou o bucket, pois você criará uma fila SQS na mesma região na próxima etapa.

### Etapa 2: Criar fila SQS

Crie uma fila SQS para rastrear quando os objetos são adicionados ao bucket que você criou. Use as definições de configuração padrão por enquanto. 

Uma fila SQS deve ser exclusiva globalmente (por exemplo, somente uma pode ser usada para uma sincronização de CDI e não pode ser reutilizada em outro espaço de trabalho).

{% alert important %}
Certifique-se de criar esse SQS na mesma região em que você criou o bucket.
{% endalert %}

Certifique-se de anotar o ARN e o URL do SQS, pois você o usará com frequência durante esta configuração.

\![Selecionando "Advanced" (Avançado) com um exemplo de objeto JSON para definir quem pode acessar uma fila.]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})

### Etapa 3: Configurar a política de acesso

Para configurar a política de acesso, selecione **Opções avançadas**. 

Anexe a seguinte declaração à política de acesso da fila, tomando cuidado para substituir `YOUR-BUCKET-NAME-HERE` pelo nome do seu bucket, `YOUR-SQS-ARN` pelo ARN da fila SQS e `YOUR-AWS-ACCOUNT-ID` pelo ID da sua conta do AWS: 

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

1. No bucket criado na etapa 1, vá para **Properties** > **Event notifications**( **Propriedades** > **Notificações de eventos**).
2. Dê um nome à configuração. Opcionalmente, especifique um prefixo ou sufixo para o alvo se você quiser que apenas um subconjunto de arquivos seja ingerido pelo Braze.
3. Em **Destination (Destino**), selecione **SQS queue (Fila SQS** ) e forneça o ARN do SQS que você criou na etapa 2.

{% alert note %}
Se você fizer upload de seus arquivos para a pasta raiz de um bucket S3 e, em seguida, mover alguns dos arquivos para uma pasta específica no bucket, poderá encontrar um erro inesperado. Em vez disso, você pode alterar as notificações de eventos para que sejam enviadas apenas para os arquivos no prefixo, evitar colocar arquivos no bucket do S3 fora desse prefixo ou atualizar a integração sem prefixo, o que fará a ingestão de todos os arquivos.
{% endalert %}

### Etapa 5: Criar uma política de IAM

Crie uma política de IAM para permitir que o Braze interaja com seu bucket de origem. Para começar, faça login no console de gerenciamento do AWS como administrador da conta. 

1. Vá para a seção IAM do Console da AWS, selecione **Políticas** na barra de navegação e, em seguida, selecione **Criar política**.<br><br>O botão "Criar política" no Console do AWS.]({% image_buster /assets/img/create_policy_1_list.png %})<br><br>

2. Abra a guia **JSON** e insira o seguinte trecho de código na seção **Policy Document (Documento de política)**, tomando o cuidado de substituir `YOUR-BUCKET-NAME-HERE` pelo nome do seu bucket e `YOUR-SQS-ARN-HERE` pelo nome da fila do SQS: 

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

4. Dê um nome e uma descrição à política e, em seguida, selecione **Criar política**.  

\![Um exemplo de política chamada "new-policy-name".]({% image_buster /assets/img/create_policy_3_name.png %})

\![O campo de descrição da política.]({% image_buster /assets/img/create_policy_4_created.png %})

### Etapa 6: Criar uma função de IAM

Para concluir a configuração no AWS, você criará uma função de IAM e anexará a ela a política de IAM da etapa 4. 

1. Na mesma seção de IAM do console em que criou a política de IAM, acesse **Roles** > **Create Role**( **Funções** > **Criar função**). 

<br><br>\![O botão "Criar função".]({% image_buster /assets/img/create_role_1_list.png %})<br><br>

{: start="2"}
2\. Copie o ID da conta Braze AWS do seu painel de controle Braze. Acesse **Cloud Data Ingestion**, selecione **Create New Data Sync** e selecione **S3 Import**.

3. No AWS, selecione **Outra conta do AWS** como o tipo de seletor de entidade confiável. Forneça o ID de sua conta Braze. Marque a caixa de seleção **Exigir ID externa** e digite uma ID externa para o Braze usar. Esse é o ID externo gerado a partir da criação de uma conexão S3 Currents na seção **Credentials (Credenciais** ) da sua conexão Currents no painel do Braze. Selecione **Next** quando terminar. 

<br><br> \![A página "Criar função" do S3. Essa página tem campos para nome da função, descrição da função, entidades confiáveis, políticas e limite de permissões.]({% image_buster /assets/img/create_role_2_another.png %})<br><br>

{: start="4"}
4\. Anexe a política criada na etapa 4 à função. Procure a política na barra de pesquisa e marque uma marca de seleção ao lado da política para anexá-la. Selecione **Next** quando terminar.

<br><br>ARN de função com o nome da nova política selecionado.]({% image_buster /assets/img/create_role_3_attach.png %})<br><br>

Dê um nome e uma descrição à função e selecione **Create Role (Criar função**).

<br><br>\![Um exemplo de função denominada "new-role-name".]({% image_buster /assets/img/create_role_4_name.png %})<br><br>

{: start="5"}
5\. Anote o ARN da função que você acabou de criar e o ID externo que você gerou, pois você os usará para criar a integração do Cloud Data Ingestion.

## Configuração da ingestão de dados na nuvem no Braze

1. Para criar uma nova integração, vá para **Configurações de dados** > **Ingestão de dados na nuvem**, selecione **Criar nova sincronização de dados** e selecione **S3 Import** na seção de fontes de arquivo. 
2. Insira as informações do processo de configuração do AWS para criar uma nova sincronização. Especifique o seguinte:

  - Função ARN
  - ID externa
  - URL do SQS (deve ser exclusivo para cada nova integração)
  - Nome do balde
  - Caminho da pasta (opcional, deve ser exclusivo entre as sincronizações em um espaço de trabalho)
  - Região

Exemplo de credenciais de segurança, conforme exibido no S3, para criar uma nova sincronização de importação.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3\. Dê um nome à sua integração e selecione o tipo de dados para essa integração. 

<br><br>\![Configurando detalhes de sincronização para "cdi-s3-as-source-integration" com atributos de usuário como o tipo de dados.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_2.png %})<br><br>

{: start="4"}
4\. Adicione um e-mail de contato para receber notificações se a sincronização for interrompida devido a problemas de acesso ou permissões. Opcionalmente, ative as notificações para erros no nível do usuário e sucessos de sincronização. 

<br><br> \![Configurando preferências de notificação para notificações de erros de sincronização.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_3.png %})<br><br>

{: start="5"}
5\. Por fim, teste a conexão e salve a sincronização. 

<br><br>\![Uma opção para testar a conexão com uma visualização de dados.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

## Formatos de arquivo necessários

A ingestão de dados na nuvem é compatível com arquivos JSON, CSV e Parquet. Cada arquivo deve conter uma ou mais das colunas de identificador compatíveis e uma coluna de carga útil como uma cadeia de caracteres JSON.

O Braze não impõe nenhum requisito adicional de nome de arquivo além do que é imposto pela AWS. Os nomes de arquivos devem ser exclusivos. Recomendamos anexar um carimbo de data/hora para garantir a exclusividade.

### Identificadores de usuário

Seu arquivo de origem pode conter uma ou mais colunas ou chaves de identificador de usuário. Cada linha deve conter apenas um identificador, mas um arquivo de origem pode ter vários tipos de identificadores.

| Identificador | Descrição |
| --- | --- |
| `EXTERNAL_ID` | Isso identifica o usuário que você deseja atualizar. Isso deve corresponder ao valor `external_id` usado no Braze. |
| `ALIAS_NAME` e `ALIAS_LABEL` | Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas somente um `alias_name` por `alias_label`. |
| `BRAZE_ID` | O identificador de usuário do Braze. Isso é gerado pelo Braze SDK, e novos usuários não podem ser criados usando um Braze ID por meio da ingestão de dados na nuvem. Para criar novos usuários, especifique um ID de usuário externo ou um alias de usuário. |
| `EMAIL` | O endereço de e-mail do usuário. Se houver vários perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente terá prioridade nas atualizações. Se você incluir e-mail e telefone, usaremos o e-mail como identificador principal. |
| `PHONE` | O número de telefone do usuário. Se houver vários perfis com o mesmo número de telefone, o perfil atualizado mais recentemente terá prioridade nas atualizações. |
|`PAYLOAD` | Essa é uma string JSON dos campos que você deseja sincronizar com o usuário no Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Diferentemente das fontes de data warehouse, a coluna `UPDATED_AT` não é necessária nem suportada.
{% endalert %}

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
ID,PAYLOAD
85,"{""product_name"": ""Product 85"", ""price"": 85.85}" 
1,"{""product_name"": ""Product 1"", ""price"": 1.01}" 
```
{% endtab %}

{% endtabs %}  

Para obter exemplos de todos os tipos de arquivos compatíveis, consulte os arquivos de amostra em [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage).  

## Coisas para saber

- Os arquivos adicionados ao bucket de origem S3 não devem exceder 512 MB. Arquivos com mais de 512 MB resultarão em um erro e não serão sincronizados com o Braze.
- Embora não haja limite adicional para o número de linhas por arquivo, recomendamos o uso de arquivos menores para aumentar a velocidade de execução das sincronizações. Por exemplo, um arquivo de 500 MB levaria muito mais tempo para ser ingerido do que cinco arquivos separados de 100 MB.
- Não há limite adicional para o número de arquivos carregados em um determinado período.
- Não há suporte para pedidos em arquivos ou entre eles. Recomendamos que as atualizações em lote sejam feitas periodicamente se você estiver monitorando quaisquer condições de corrida esperadas.

## Solução de problemas

### Carregamento de arquivos e processamento

O CDI processará apenas os arquivos adicionados após a criação da sincronização. Nesse processo, o Braze procura por novos arquivos a serem adicionados, o que aciona uma nova mensagem para o SQS. Isso dará início a uma nova sincronização para processar o novo arquivo.

Os arquivos existentes podem ser usados para validar a estrutura de dados na conexão de teste, mas eles não serão sincronizados com o Braze. Todos os arquivos existentes que devem ser sincronizados devem ser recarregados no S3 para serem processados pela CDI.

### Tratamento de erros inesperados de arquivos

Se estiver observando um grande número de erros ou arquivos com falha, é possível que outro processo esteja adicionando arquivos ao bucket do S3 em uma pasta diferente da pasta de destino do CDI.

Quando os arquivos são carregados no bucket de origem, mas não na pasta de origem, o CDI processa a notificação do SQS, mas não executa nenhuma ação no arquivo, portanto, isso pode aparecer como um erro.
