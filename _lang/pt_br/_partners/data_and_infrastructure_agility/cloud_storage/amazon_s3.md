---
nav_title: Amazon S3
article_title: Amazon S3
alias: /partners/amazon_s3/
description: "Este artigo de referência descreve a parceria entre o Braze e o Amazon S3, um sistema de armazenamento altamente escalável oferecido pela Amazon Web Services."
page_type: partner
search_tag: Partner

---

# Amazon S3

> [O Amazon S3](https://aws.amazon.com/s3/) é um sistema de armazenamento altamente escalável oferecido pela Amazon Web Services.

A integração entre o Braze e o Amazon S3 aproveita o [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) para enviar dados do Braze para sua instância do S3, ativando a capacitação para armazenar dados lá até que você queira conectá-los a outras plataformas, ferramentas e locais. Você também pode fazer a integração por meio de exportações de dados do dashboard. Siga as instruções nesta página para começar a fazer sua integração com o AWS S3.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Amazon S3 | É necessário ter uma conta no Amazon S3 para aproveitar essa parceria. |
| Bucket S3 dedicado | Antes de se integrar ao Amazon S3, você deve criar um bucket S3 para seu app.<br><br>Se você já tiver um bucket S3, ainda assim recomendamos a criação de um novo bucket especificamente para o Braze para que você possa limitar as permissões. Consulte as instruções a seguir sobre como criar um novo bucket. |
| Currents | Para exportar dados de volta para o Amazon S3, é necessário que [o Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) esteja configurado em sua conta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Criar um novo bucket S3

Para criar um bucket para seu app, abra o [console do Amazon S3](https://console.aws.amazon.com/s3/) e siga as instruções para fazer **login** ou **criar uma conta na AWS**. Depois de fazer login, selecione **S3** na categoria **Storage & Content Delivery**. Selecione **Create Bucket** (Criar bucket) na próxima tela. Você verá opções para criar seu bucket e selecionar uma região.

## Integração

O Braze tem duas estratégias de integração diferentes com o Amazon S3 - uma para o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) e outra para todas as exportações de dados do dashboard (exportações CSV, relatórios de engajamento, etc.) Ambas as integrações suportam dois métodos diferentes de autenticação/autorização:

- [Método da chave de acesso secreta da AWS](#aws-secret-key-auth-method)
- [Método ARN da função AWS](#aws-role-arn-auth-method)

## Método de autenticação de chave secreta da AWS

Esse método de autenticação gera uma chave secreta e um ID de chave de acesso que ativa o Braze para se autenticar como um usuário em sua conta da AWS para gravar dados em seu bucket.

### Etapa 1: Criar usuário {#secret-key-1}

Para recuperar o ID da chave de acesso e a chave de acesso secreta, será necessário [criar um usuário IAM e um grupo de administradores no AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html).

### Etapa 2: Obter credenciais {#secret-key-2}

Depois de criar um novo usuário, clique em **Show User Security Credentials (Mostrar credenciais de segurança do usuário** ) para revelar o ID da chave de acesso e a chave de acesso secreta. Em seguida, anote essas credenciais em algum lugar ou clique no botão **Baixar credenciais**, pois você precisará inseri-las no dashboard do Braze posteriormente.

![][11]

### Etapa 3: Criar política {#secret-key-3}

Navegue até **Policies > Get Started > Create Policy** (Políticas > Começar > Criar política) para adicionar permissões ao seu usuário. Em seguida, selecione **Create Your Own Policy** (Criar sua própria política). Isso concederá permissões limitadas, de modo que a Braze só poderá acessar os buckets especificados. 

![][12]

{% alert note %}
São necessárias políticas diferentes para "Currents" e "Dashboard Data Export" (Exportação de dados do dashboard).
{% endalert %}

Especifique um nome de política de sua escolha e insira o seguinte trecho de código na seção **Policy Document (Documento de política** ). Não se esqueça de substituir `INSERTBUCKETNAME` pelo nome de seu bucket. Sem essas permissões, a integração falhará em uma verificação de credenciais e não será criada.

{% tabs %}
{% tab Braze Currents %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```
{% endtab %}
{% tab Exportação de dados do dashboard %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME*", "arn:aws:s3:::INSERTBUCKETNAME/", "arn:aws:s3:::INSERTBUCKETNAME"]
        }
    ]
}
```
{% endtab %}
{% endtabs %}

### Etapa 4: Anexar política {#secret-key-4}

Depois de criar uma nova política, navegue até **Usuários** e clique no seu usuário específico. Na guia **Permissões**, clique em **Anexar política** e selecione a nova política que você criou. Agora você está pronto para vincular suas credenciais da AWS à sua conta do Braze.

![][13]

### Etapa 5: vincular o Braze ao AWS {#secret-key-5}

{% tabs %}
{% tab Braze Currents %}

Na Braze, navegue até **Integrações com parceiros** > **Exportação de dados**.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), poderá encontrar **o Currents** em **Integrations**.
{% endalert %}

Em seguida, clique em **Create Current** e selecione **Amazon S3 Data Export**.

Dê um nome à sua Current e, na seção **Credentials (Credenciais)**, certifique-se de que o botão de opção **AWS Secret Access Key** esteja selecionado e, em seguida, insira seu ID de acesso S3, a chave de acesso secreta da AWS e o nome do bucket S3 da AWS nos campos designados.

![]({{site.baseurl}}/assets/img/currents-s3-example.png)

{% alert warning %}
Mantenha seu ID de chave de acesso do AWS e sua chave de acesso secreta atualizados. Se as credenciais do conector expirarem, ele deixará de enviar eventos. Se isso persistir por mais de **48 horas**, os eventos do conector serão descartados e os dados serão perdidos permanentemente.
{% endalert %}

Você também pode adicionar as seguintes personalizações de acordo com suas necessidades:

- **Caminho da pasta:** o padrão é `currents`. Se essa pasta não existir, a Braze a criará automaticamente para você. 
- **Criptografia AES-256 do lado do servidor, em repouso:** O padrão é OFF e inclui o cabeçalho `x-amz-server-side-encryption`.

Clique em **Launch Current** para continuar.

Uma notificação informará se suas credenciais foram validadas com sucesso. O AWS S3 agora deve estar configurado para o Braze Currents.

{% endtab %}
{% tab Exportação de dados do dashboard %}

Na Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** e clique em **Amazon S3**.

{% alert note %}
Se você estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), você pode encontrar **Parceiros de Tecnologia** em **Integrações**.
{% endalert %}

Na página de credenciais do AWS, verifique se o botão **AWS Secret Access Key** (Chave de acesso secreta do AWS) está selecionado. Em seguida, insira o ID de acesso, a chave de acesso secreta e o nome do bucket do AWS S3 nos campos designados. Ao inserir sua chave secreta, clique primeiro em **Test Credentials (Testar credenciais** ) para garantir que suas credenciais funcionem e, em seguida, clique em **Save (Salvar** ) quando for bem-sucedido.

![]({{site.baseurl}}/assets/img/s3_tech_partners.png)

{% alert tip %}
Sempre é possível recuperar novas credenciais navegando até o seu usuário e clicando em **Criar chave de acesso** na guia **Credenciais de segurança** no Console da AWS.
{% endalert %}

Uma notificação informará se suas credenciais foram validadas com sucesso. O AWS S3 agora deve estar integrado à sua conta do Braze.

{% endtab %}
{% endtabs %}

## Método de autenticação ARN de função da AWS

Esse método de autenticação gera uma função Amazon Resource Name (ARN) que ativa a conta do Braze na Amazon para autenticar como membro da função que você criou para gravar dados em seu bucket.

### Etapa 1: Criar política {#role-arn-1}

Para começar, faça login no console de gerenciamento do AWS como administrador da conta. Navegue até a seção IAM do Console da AWS, clique em **Políticas** na barra de navegação e clique em **Criar política**.

![]({{site.baseurl}}/assets/img/create_policy_1_list.png)

{% alert note %}
São necessárias políticas diferentes para "Currents" e "Dashboard Data Export" (Exportação de dados do dashboard).
{% endalert %}

Abra a guia **JSON** e insira o seguinte trecho de código na seção **Policy Document (Documento de política)**. Não se esqueça de substituir `INSERTBUCKETNAME` pelo nome de seu bucket. Clique em **Review Policy (Revisar política)** quando terminar.

{% tabs %}
{% tab Braze Currents %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% tab Exportação de dados do dashboard %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject","s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% endtabs %}

Em seguida, dê um nome e uma descrição à política e clique em **Create Policy (Criar política**).

![]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### Etapa 2: criar função {#role-arn-2}

Na mesma seção IAM do console, clique em **Roles > Create Role (Funções > Criar função**).

![]({{site.baseurl}}/assets/img/create_role_1_list.png)

Recupere o ID de sua conta Braze e o ID externo de sua conta Braze:
- **Currents:** Na Braze, navegue até **Integrações com parceiros** > **Exportação de dados**. Em seguida, clique em **Create Current** e selecione **Amazon S3 Data Export**. Aqui você encontrará os identificadores necessários para criar sua função.
- **Exportação de dados do dashboard**: Na Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** e clique em **Amazon S3**. Aqui você encontrará os identificadores necessários para criar sua função.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), essas páginas estão em um local diferente:<br>\- O **Currents** está localizado em **Integrações** > **Currents** <br>\- Os **parceiros de tecnologia** estão localizados em **Integrações**
{% endalert %}

No console do AWS, selecione **Another AWS Account** (Outra conta da AWS) como o tipo de seletor de entidade confiável. Forneça o ID da sua conta da Braze, marque a caixa **Require external ID** (Exigir ID externo) e digite o ID externo da Braze. Clique em **Next** quando terminar.

![A página "Create Role" (Criar função) do S3. Essa página tem campos para nome da função, descrição da função, entidades confiáveis, políticas e limite de permissões.]({{site.baseurl}}/assets/img/create_role_2_another.png)

### Etapa 3: Anexar política {#role-arn-3}

Em seguida, anexe à função a política que você criou anteriormente. Procure a apólice na barra de pesquisa e coloque uma marca de seleção ao lado da apólice para anexá-la. Clique em **Next** quando terminar.

![Função do ARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)

Dê um nome e uma descrição à função e clique em **Create Role (Criar função**).

![Função do ARN]({{site.baseurl}}/assets/img/create_role_4_name.png)

Agora você deve ver a função recém-criada na lista.

### Etapa 4: link para o AWS da Braze {#role-arn-4}

No console do AWS, localize sua função recém-criada na lista. Clique no nome para abrir os detalhes dessa função.

![]({{site.baseurl}}/assets/img/create_role_5_created.png)

Observe o **ARN da função** na parte superior da página de resumo da função.

![]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Retorne à sua conta da Braze e copie o ARN da função no campo fornecido.

{% tabs %}
{% tab Braze Currents %}

No Braze, navegue até a página **Currents** em **Integrations (Integrações**). Em seguida, clique em **Create Current** e selecione **Amazon S3 Data Export**

![]({{site.baseurl}}/assets/img/currents-role-arn.png)

Dê um nome à sua Corrente. Em seguida, na seção **Credentials (Credenciais)**, certifique-se de que o botão de opção **AWS Role ARN** esteja selecionado e forneça o ARN da sua função e o nome do bucket S3 da AWS nos campos designados.

Você também pode adicionar as seguintes personalizações de acordo com suas necessidades:

- Jornada da pasta (o padrão é `currents`)
- Criptografia AES-256 do lado do servidor, em repouso (o padrão é OFF) – inclui o cabeçalho `x-amz-server-side-encryption` 

Clique em **Launch Current** para continuar.

Uma notificação informará se suas credenciais foram validadas com sucesso. O AWS S3 agora deve estar configurado para o Braze Currents.

{% alert important %}
Se você receber um erro "As credenciais do S3 são inválidas", isso poderá ser devido à integração muito rápida após a criação de uma função no AWS. Aguarde e tente novamente.
{% endalert %}

{% endtab %}
{% tab Exportação de dados do dashboard %}

No Braze, navegue até a página **Technology Partners (Parceiros de tecnologia** ) em **Integrations (Integrações** ) e clique em **Amazon S3**.

![]({{site.baseurl}}/assets/img/data-export-role-arn.png)

Na página **AWS Credentials (Credenciais da AWS** ), certifique-se de que o botão de opção **AWS Role ARN** esteja selecionado e, em seguida, insira o ARN da sua função e o nome do bucket S3 da AWS nos campos designados. Clique em **Test Credentials (Testar credenciais** ) primeiro para garantir que suas credenciais funcionem corretamente e, em seguida, clique em **Save (Salvar** ) quando for bem-sucedido.

{% alert tip %}
Sempre é possível recuperar novas credenciais navegando até o seu usuário e clicando em **Criar chave de acesso** na guia **Credenciais de segurança** no Console da AWS.
{% endalert %}

Uma notificação informará se suas credenciais foram validadas com sucesso. O AWS S3 agora deve estar integrado à sua conta do Braze.

{% endtab %}
{% endtabs %}

## Comportamento de exportação

Os usuários que integraram uma solução de armazenamento de dados na nuvem e estão tentando exportar APIs, relatórios de dashboard ou relatórios CSV terão a seguinte experiência:

- Todas as exportações da API não retornarão um URL para baixar no corpo da resposta e devem ser recuperadas por meio do armazenamento de dados.
- Todos os relatórios dashboard e CSV serão enviados para o e-mail dos usuários para serem baixados (não são necessárias permissões de armazenamento) e armazenados em backup no Data Storage. 

## Vários conectores

Se pretender criar mais de um conector Currents para enviar ao seu bucket S3, você poderá usar as mesmas credenciais, mas deverá especificar um caminho de pasta diferente para cada um. Eles podem ser criados no mesmo espaço de trabalho ou divididos e criados em vários espaços de trabalho. Você também tem a opção de criar uma única política para cada integração ou criar uma política que abranja ambas as integrações. 

Se você planeja usar o mesmo bucket S3 para Currents e exportações de dados, precisará criar duas políticas separadas, pois cada integração requer permissões diferentes.


[11]: {% image_buster /assets/img_archive/S3_Credentials.png %}
[12]: {% image_buster /assets/img_archive/S3_CreatePolicy.png %}
[13]: {% image_buster /assets/img_archive/S3_AttachPolicy.png %}
