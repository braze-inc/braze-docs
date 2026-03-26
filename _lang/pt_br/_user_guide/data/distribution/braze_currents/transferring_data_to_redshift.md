---
nav_title: Transferir dados para o Redshift
article_title: Transferir dados para o Redshift
page_order: 8
page_type: tutorial
description: "Este artigo explica como transferir dados do Amazon S3 para o Redshift por meio de um processo de extração, transformação e carga (ETL)."
tool: Currents

---

# Transferir dados para o Redshift

> [O Amazon Redshift](https://aws.amazon.com/redshift/) é um data warehouse popular que é executado no Amazon Web Services juntamente com o Amazon S3. Os dados do Braze do Currents são estruturados para transferência direta para o Redshift.

O seguinte descreve como transferir dados do Amazon S3 para o Redshift através de um processo de Extração, Transformação e Carga (ETL). Para o código-fonte completo, consulte os exemplos do Currents [repositório do GitHub](https://github.com/Appboy/currents-examples).

{% alert important %}
Essa é apenas uma das muitas opções que você pode escolher quando se trata de transferir seus dados para os locais mais vantajosos para você.
{% endalert %}

## Visão geral do carregador S3 para Redshift

O script [`s3loader.py`](https://github.com/Appboy/currents-examples/tree/master/redshift-s3-loader) usa uma tabela de manifesto separada no mesmo banco de dados do Redshift para acompanhar os arquivos que já foram copiados. A estrutura geral é a seguinte:

1. Liste todos os arquivos no S3, depois identifique os novos arquivos desde a última vez que você executou `s3loader.py` comparando a lista com o conteúdo na tabela de manifesto.
2. Crie um arquivo [manifesto](http://docs.aws.amazon.com/redshift/latest/dg/loading-data-files-using-manifest.html) contendo os novos arquivos.
3. Execute uma consulta `COPY` para copiar os novos arquivos do S3 para o Redshift usando o arquivo de manifesto.
4. Insira os nomes dos arquivos que foram copiados na tabela de manifesto separada no Redshift.
5. Confirme.

## Dependências

Você deve instalar o AWS Python SDK e o Psycopg para executar o carregador:

```bash
pip install boto3
pip install psycopg2
```

## Permissões

### Função do Redshift com acesso de leitura ao S3

Se você ainda não fez isso, siga a [documentação da AWS](http://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-create-an-iam-role.html) para criar uma função que possa executar comandos `COPY` em seus arquivos no S3.

### Regras de entrada do VPC do Redshift

Se seu cluster do Redshift estiver em um VPC, você deve configurar o VPC para permitir conexões do servidor em que você está executando o carregador S3. Acesse seu Cluster do Redshift e selecione a entrada de Grupos de Segurança do VPC que você deseja que o carregador se conecte. Em seguida, adicione uma nova regra de entrada: **Tipo** = Redshift, **Protocolo** = TCP, **Porta** = a porta do seu cluster, **Fonte** = o IP do servidor que está executando o carregador (ou "Qualquer lugar" para testes).

### Usuário do Identity and Access Management (IAM) com acesso total ao S3

O carregador S3 requer acesso de leitura aos arquivos que contêm seus dados de Currents e acesso total ao local dos arquivos de manifesto que ele gera para os comandos Redshift `COPY`. Crie um novo usuário do Identity and Access Management (IAM) com a permissão `AmazonS3FullAccess` do [console IAM](https://console.aws.amazon.com/iam/home#/users). Salve as credenciais, pois você precisará passá-las para o carregador.

Você pode passar as credenciais de acesso para o carregador através de variáveis de ambiente, do arquivo de credenciais compartilhadas (`~/.aws/credentials`) ou do [arquivo de configuração AWS](http://boto3.readthedocs.io/en/latest/guide/configuration.html#configuring-credentials). Alternativamente, você pode incluí-las diretamente no carregador atribuindo-as aos campos `aws_access_key_id` e `aws_secret_access_key` dentro de um objeto `S3LoadJob`, mas não recomendamos codificar credenciais diretamente no seu código-fonte.

## Uso

### Uso de exemplo

O seguinte programa de exemplo carrega dados para o evento `users.messages.contentcard.Impression` do S3 para a tabela `content_card_impression` no Redshift.

```
if __name__ == '__main__':
    host = '{YOUR_CLUSTER}.redshift.amazonaws.com'
    port = 5439
    database = '{YOUR_DATABASE}'
    user = '{YOUR_USER}'
    password = '{YOUR_PASSWORD}'
    role = '{YOUR_REDSHIFT_ROLE_ARN}'

    # Do not hard code these credentials.
    aws_access_key_id = None
    aws_secret_access_key = None

    # Content Card Impression Avro fields:
    #   id            - string
    #   user_id       - string
    #   external_user_id - string (nullable)
    #   app_id        - string
    #   content_card_id  - string
    #   campaign_id   - string (nullable)
    #   send_id       - string (nullable)
    #   time          - int
    #   platform      - string (nullable)
    #   device_model  - string (nullable)

    print('Loading Content Card Impression...')
    cc_impression_s3_bucket = '{YOUR_CURRENTS_BUCKET}'
    cc_impression_s3_prefix = '{YOUR_CURRENTS_PREFIX}'
    cc_impression_redshift_table = 'content_card_impression'
    cc_impression_redshift_column_def = [
        ('id', 'text'),
        ('user_id', 'text'),
        ('external_user_id', 'text'),
        ('app_id', 'text'),
        ('content_card_id', 'text'),
        ('campaign_id', 'text'),
        ('send_id', 'text'),
        ('time', 'integer'),
        ('platform', 'text'),
        ('device_model', 'text')
    ]

    cc_impression_redshift = RedshiftEndpoint(host, port, database, user, password,
        cc_impression_redshift_table, cc_impression_redshift_column_def)
    cc_impression_s3 = S3Endpoint(cc_impression_s3_bucket, cc_impression_s3_prefix)

    cc_impression_job = S3LoadJob(cc_impression_redshift, cc_impression_s3, role,
        aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    cc_impression_job.perform()
```

### Credenciais

Para executar o carregador, você deve primeiro fornecer o `host`, `port` e `database` do seu cluster Redshift, bem como o `user` e `password` de um usuário Redshift que pode executar consultas `COPY`. Além disso, você deve fornecer o ARN da função Redshift com acesso de leitura ao S3 que você criou em uma seção anterior.

```
host = '{YOUR_CLUSTER}.redshift.amazonaws.com'
port = 5439
database = '{YOUR_DATABASE}'
user = '{YOUR_USER}'
password = '{YOUR_PASSWORD}'
role = '{YOUR_REDSHIFT_ROLE_ARN}'
```

### Configuração do trabalho

Você deve fornecer o bucket S3 e o prefixo dos seus arquivos de evento, bem como o nome da tabela Redshift que você deseja `COPY`.

Além disso, para `COPY` arquivos Avro com a opção "auto" conforme exigido pelo carregador, a definição da coluna na sua tabela Redshift deve corresponder aos nomes dos campos no esquema Avro, conforme mostrado no programa de exemplo, com o mapeamento de tipo apropriado (por exemplo, `string` para `text`, `int` para `integer`).

Você também pode passar uma opção `batch_size` para o carregador se achar que leva muito tempo para copiar todos os arquivos de uma vez. Passar um `batch_size` permite que o carregador copie e comite incrementalmente um lote por vez, sem precisar copiar tudo ao mesmo tempo. O tempo que leva para carregar um lote depende do `batch_size`, bem como do tamanho dos seus arquivos e do tamanho do seu cluster Redshift.

```
# Content Card Impression Avro fields:
#   id            - string
#   user_id       - string
#   external_user_id - string (nullable)
#   app_id        - string
#   content_card_id  - string
#   campaign_id   - string (nullable)
#   send_id       - string (nullable)
#   time          - int
#   platform      - string (nullable)
#   device_model  - string (nullable)
cc_impression_s3_bucket = '{YOUR_CURRENTS_BUCKET}'
cc_impression_s3_prefix = '{YOUR_CURRENTS_PREFIX}'
cc_impression_redshift_table = 'content_card_impression'
cc_impression_redshift_column_def = [
    ('id', 'text'),
    ('user_id', 'text'),
    ('external_user_id', 'text'),
    ('app_id', 'text'),
    ('content_card_id', 'text'),
    ('campaign_id', 'text'),
    ('send_id', 'text'),
    ('time', 'integer'),
    ('platform', 'text'),
    ('device_model', 'text')
]
cc_impression_batch_size = 1000
```