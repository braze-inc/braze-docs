---
nav_title: Fivetran
article_title: Fivetran
alias: /partners/fivetran/
description: "Este artigo de referência descreve a parceria entre o Braze e a Fivetran, uma ferramenta de automação de fluxo de trabalho que pode ajudá-lo na tomada de decisões com base em dados, fornecendo dados prontos para consulta em seu data warehouse na nuvem."
page_type: partner
search_tag: Partner
tool: Currents

---

# Fivetran

> [A Fivetran](https://fivetran.com/) é uma marca reconhecida mundialmente, cujos produtos voltados para analistas e pipelines totalmente gerenciados ativam decisões baseadas em dados, fornecendo dados prontos para consulta em seu data warehouse na nuvem.

A integração do Braze e do Fivetran permite que os usuários criem um pipeline sem manutenção que o capacita a coletar e analisar dados do Braze, conectando todos os seus aplicativos e bancos de dados a um data warehouse central. Depois que os dados são coletados no data warehouse central, as equipes de dados podem explorar os dados da Braze de forma eficaz usando suas ferramentas de business intelligence preferidas. 

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Fivetran | É necessário ter uma conta [Fivetran](https://fivetran.com/login?next=%2Fdashboard) para usar a parceria. |
| Chave da API REST do Braze | Uma chave da API REST do Braze com as seguintes permissões:<br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages.schedule_broadcasts<br>- campaigns.list<br>- campaigns.details<br>- canvas.list<br>- canvas.details<br>- segments.list<br>- segments.details<br>- purchases.product_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Ponto de extremidade REST do Braze  | Sua URL de endpoint REST. Seu endpoint dependerá do [URL do Braze para sua instância]({{site.baseurl}}/api/basics/#api-definitions). |
| Braze Currents | O [Braze Currents](https://www.braze.com/product/data-agility-management/currents/) deve estar conectado ao Amazon S3 ou ao Google Cloud Storage. |
| Amazon S3 ou Google Cloud Storage | Essa integração exige que você tenha acesso a um Amazon S3 ou Google Cloud Storage. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Integração

A seguinte integração do Currents é compatível com o [Amazon S3](#setting-up-braze-currents-for-s3) e [o Google Cloud Storage](#setting-up-braze-currents-for-google-cloud-storage).

### Configuração do Braze Currents para S3

#### Etapa 1: Localize sua ID externa {#step-one}

No [Fivetran Dashboard](https://fivetran.com/dashboard), selecione **\+ Connector** e, em seguida, selecione o conector **Braze** para iniciar o formulário de configuração. Em seguida, selecione **Amazon S3**. Note o ID externo fornecido aqui; você precisará dele para permitir que o Fivetran acesse seu bucket S3. 

![O formulário do conector Fivetran para a Braze. O campo de ID externo necessário para esta etapa está localizado no meio da página em uma caixa cinza claro.]({% image_buster /assets/img/fivetran_braze_setupform_as3.png %})

#### Etapa 2: conceda ao Fivetran acesso a um bucket S3 especificado

##### Criação de uma política de IAM

Abra o [Console do Amazon IAM](https://console.aws.amazon.com/iam/home#home) e navegue até **Políticas > Criar política**.

![Console do Amazon IAM com lista de políticas.]({% image_buster /assets/img/fivetran_as3_iam.png %})

Em seguida, abra a guia **JSON** e cole a seguinte política. Substitua `{your-bucket-name}` pelo nome de seu bucket S3.

{% raw %}
```json
{
"Version": "2012-10-17",
"Statement": [
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}/*"
    },
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}"
    }
  ]
}
```
{% endraw %}

Por fim, selecione **Revisar política** e dê à política um nome e uma descrição exclusivos. Selecione **Criar política** para criar sua política. 

![Campos para nomear a política e fornecer uma descrição.]({% image_buster /assets/img/fivetran_iam_policy_meta.png %})

##### Criar uma função de IAM {#step-two}

Na AWS, navegue até **Roles (Funções**) e selecione **Create New Role (Criar nova função**).

![A página "Roles" (Funções) com o botão para criar uma nova função.]({% image_buster /assets/img/fivetran_iam_new_role.png %})

Selecione **Another AWS Account** (Outra conta AWS) e forneça o ID da conta Fivetran `834469178297`. Certifique-se de marcar a caixa de seleção **Require external ID (Exigir ID externo** ). Aqui você fornecerá o ID externo encontrado na etapa 1.

![O campo para inserir seu "ID da conta", uma caixa de seleção para exigir o ID externo e uma caixa de texto em branco para inserir seu "ID externo".]({% image_buster /assets/img/fivetran_another_aws_account.png %})

Em seguida, selecione **Next: Permissions (Permissões)** para selecionar a política que você acabou de criar.

![Lista de políticas.]({% image_buster /assets/img/fivetran_as3_select_policy.png %})

Selecione **Next: Consulte**, nomeie sua nova função (como Fivetran) e selecione **Create Role (Criar função**). Depois que a função for criada, selecione-a e note o ARN da função mostrado.

![O ARN do Amazon S3 listado na função.]({% image_buster /assets/img/fivetran_iam_role_arn.png %})

{% alert note %}
Você pode especificar permissões para o ARN de função que designar para o Fivetran. A concessão de permissões seletivas a essa função permitirá que o Fivetran sincronize apenas o que tem permissão para ver.
{% endalert %}

#### Etapa 3: Complete o conector Fivetran

No Fivetran, selecione **\+ Connector** e, em seguida, selecione o conector **Braze** para abrir o formulário de configuração. No formulário, preencha os campos fornecidos com os valores apropriados:
- `Destination schema`: Um nome de esquema exclusivo.
- `API URL`: Seu endpoint da API REST da Braze.
- `API Key`: Sua chave da API REST do Braze. 
- `External ID`: A ID externa definida na [etapa 2](#step-two) das instruções de configuração do Currents. Essa ID é um valor fixo.
- `Bucket`: Encontrado em sua conta Braze, navegando até **Integrações com parceiros** > **Exportação de dados** > Seu nome atual.
- `Role ARN`: O ARN da função pode ser encontrado na [etapa 1](#step-one) das instruções de configuração do Current.

{% alert important %}
Certifique-se de que **o Amazon S3** esteja selecionado como a opção de **armazenamento em nuvem**.
{% endalert %}

Por fim, selecione **Save & Test (Salvar e testar**), e o Fivetran fará o resto, sincronizando com os dados de sua conta Braze!

### Configuração do Braze Currents para o Google Cloud Storage

#### Etapa 1: recupere seu e-mail do Fivetran no Google Cloud Storage {#step-one2}

No [dashboard do Fivetran](https://fivetran.com/dashboard), selecione **\+ Connector** e, em seguida, selecione o conector **Braze** para iniciar o formulário de configuração. Em seguida, selecione **Google Cloud Storage**. Anote o endereço de e-mail que aparece.

![O formulário do conector Fivetran para a Braze. O campo de e-mail necessário para essa etapa está localizado no meio da página, em uma caixa cinza claro.]({% image_buster /assets/img/fivetran_braze_setupform_gcs.png %})

#### Etapa 2: conceda acesso ao bucket

Navegue até o [Google Storage Console](https://console.cloud.google.com/storage/browser), selecione o bucket com o qual você configurou o Braze Currents e selecione **Editar permissões do bucket**.

![Os compartimentos disponíveis no Console de armazenamento do Google. Localize um bucket e selecione o ícone de três pontos verticais para abrir o menu suspenso que permite editar as permissões do bucket.]({% image_buster /assets/img/fivetran_edit_bucket_permissions_gcs.png %})

Em seguida, conceda ao `Storage Object Viewer` acesso ao e-mail da [etapa 1](#step-one2), adicionando-o como membro. Anote o nome do bucket; você precisará dele na próxima etapa para configurar o Fivetran.

![Balde com permissões.]({% image_buster /assets/img/fivetran_add_members_gcs.png %})

#### Etapa 3: Complete o conector Fivetran

No Fivetran, selecione **\+ Connector** e, em seguida, selecione o conector **Braze** para abrir o formulário de configuração. No formulário, preencha os campos fornecidos com os valores apropriados:
- `Destination schema`: Um nome de esquema exclusivo.
- `API URL`: Seu endpoint da API REST da Braze.
- `API Key`: Sua chave da API REST do Braze. 
- `Bucket Name`: Encontrado em sua conta Braze, navegando até **Integrações com parceiros** > **Exportação de dados** > Seu nome atual.
- `Folder`: Encontrado em sua conta Braze, navegando até **Integrações com parceiros** > **Exportação de dados** > Seu nome atual.

{% alert important %}
Certifique-se de que **o Google Cloud Storage** esteja selecionado como a opção de **armazenamento na nuvem**.
{% endalert %}

Por fim, selecione **Save & Test (Salvar e testar**), e o Fivetran fará o resto, sincronizando com os dados de sua conta Braze!

