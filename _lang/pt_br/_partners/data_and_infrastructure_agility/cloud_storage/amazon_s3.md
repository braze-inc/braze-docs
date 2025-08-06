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

A integração do Braze com o Amazon S3 apresenta duas estratégias de integração:

- Aproveite [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), permitindo que você armazene dados lá até que queira conectá-los a outras plataformas, ferramentas e locais.
- Use exportações de dados do dashboard (como exportações CSV e relatórios de engajamento).

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Amazon S3 | É necessário ter uma conta no Amazon S3 para aproveitar essa parceria. |
| Bucket S3 dedicado | Antes de se integrar ao Amazon S3, você deve criar um bucket S3 para seu app.<br><br>Se você já tiver um bucket S3, ainda assim recomendamos a criação de um novo bucket especificamente para o Braze para que você possa limitar as permissões. Consulte as instruções a seguir sobre como criar um novo bucket. |
| Currents | Para exportar dados de volta para o Amazon S3, é necessário que [o Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) esteja configurado em sua conta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Criando um novo bucket S3

Para criar um bucket para seu app, faça o seguinte:

1. Abra o [console do Amazon S3](https://console.aws.amazon.com/s3/) e siga as instruções para **fazer login** ou **Criar uma conta com a AWS**. 
2. Depois de fazer login, selecione **S3** na categoria **Storage & Content Delivery**. 
3. Selecione **Create Bucket** (Criar bucket) na próxima tela. 
4. Você verá opções para criar seu bucket e selecionar uma região.

{% alert note %}
Currents não suporta buckets com [Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) configurado.
{% endalert %}

## Integração

O Braze tem duas estratégias de integração diferentes com o Amazon S3—uma para [Braze Currents]({{site.baseurl}}/user_guide/data/braze_currents/) e uma para todas as exportações de dados do dashboard (como exportações CSV ou relatórios de engajamento). Ambas as integrações suportam dois métodos diferentes de autenticação ou autorização:

- [Método da chave de acesso secreta da AWS](#aws-secret-key-auth-method)
- [Método ARN da função AWS](#aws-role-arn-auth-method)

## Método de autenticação de chave secreta da AWS

Esse método de autenticação gera uma chave secreta e um ID de chave de acesso que ativa o Braze para se autenticar como um usuário em sua conta da AWS para gravar dados em seu bucket.

### Etapa 1: Criar usuário {#secret-key-1}

Para recuperar o ID da chave de acesso e a chave de acesso secreta, será necessário [criar um usuário IAM e um grupo de administradores no AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html).

### Etapa 2: Obter credenciais {#secret-key-2}

Após criar um novo usuário, selecione **Mostrar credenciais de segurança do usuário** para revelar seu ID de chave de acesso e chave de acesso secreta. Em seguida, anote essas credenciais em algum lugar ou selecione o botão **Baixar credenciais**, pois você precisará inseri-las no dashboard do Braze mais tarde.

![][11]

### Etapa 3: Criar política {#secret-key-3}

Navegue até **Políticas** > **Começar** > **Criar política** para adicionar permissões para seu usuário. Em seguida, selecione **Create Your Own Policy** (Criar sua própria política). Isso concederá permissões limitadas, de modo que a Braze só poderá acessar os buckets especificados. 

![][12]

{% alert note %}
Políticas diferentes são necessárias para Currents e Exportação de Dados do Dashboard. `s3:GetObject` é necessário para permitir que o backend do Braze realize o tratamento de erros.
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

Após criar uma nova política, vá para **Usuários** e selecione seu usuário específico. Na aba **Permissões**, selecione **Anexar política**, e selecione a nova política que você criou. Agora, você está pronto para vincular suas credenciais da AWS à sua conta do Braze.

![][13]

### Etapa 5: vincular o Braze ao AWS {#secret-key-5}

{% tabs %}
{% tab Braze Currents %}

No Braze, acesse **Integrações de Parceiros** > **Exportação de Dados**.

Em seguida, selecione **Criar Current** e depois **Exportação de Dados do Amazon S3**.

Nomeie seu Current. Na seção **Credenciais**, certifique-se de que **Chave de Acesso Secreta da AWS** esteja selecionada, e insira seu ID de acesso S3, chave de acesso secreta da AWS e nome do bucket S3 da AWS nos campos designados.

![]({{site.baseurl}}/assets/img/currents-s3-example.png)

{% alert warning %}
Mantenha seu ID de chave de acesso do AWS e sua chave de acesso secreta atualizados. Se as credenciais do conector expirarem, ele deixará de enviar eventos. Se isso persistir por mais de **48 horas**, os eventos do conector serão descartados e os dados serão perdidos permanentemente.
{% endalert %}

Você também pode adicionar as seguintes personalizações de acordo com suas necessidades:

- **Caminho da pasta:** o padrão é `currents`. Se essa pasta não existir, a Braze a criará automaticamente para você. 
- **Criptografia AES-256 do lado do servidor, em repouso:** O padrão é OFF e inclui o cabeçalho `x-amz-server-side-encryption`.

Selecione **Iniciar Current** para continuar.

Uma notificação informará se suas credenciais foram validadas com sucesso. O AWS S3 agora deve estar configurado para o Braze Currents.

{% endtab %}
{% tab Exportação de dados do dashboard %}

No Braze, acesse **Integrações de Parceiros** > **Parceiros de Tecnologia** e selecione **Amazon S3**.

Na página **Credenciais da AWS**, certifique-se de que **Chave de Acesso Secreta da AWS** está selecionada, em seguida, insira seu ID de acesso da AWS, chave de acesso secreta da AWS e nome do bucket S3 da AWS nos campos designados. Ao inserir sua chave secreta, selecione **Testar Credenciais** primeiro para garantir que suas credenciais funcionem, em seguida, selecione **Salvar** quando for bem-sucedido.

![]({{site.baseurl}}/assets/img/s3_tech_partners.png)

{% alert tip %}
Você sempre pode recuperar novas credenciais navegando até seu usuário e selecionando **Criar Chave de Acesso** na aba **Credenciais de Segurança** dentro do Console da AWS.
{% endalert %}

Uma notificação informará se suas credenciais foram validadas com sucesso. O AWS S3 agora deve estar integrado à sua conta do Braze.

{% endtab %}
{% endtabs %}

## Método de autenticação ARN de função da AWS

Este método de autenticação gera um Nome de Recurso da Amazon (ARN) de função que permite que a conta Amazon do Braze se autentique como um membro da função que você criou para gravar dados em seu bucket.

### Etapa 1: Criar política {#role-arn-1}

Para começar, faça login no console de gerenciamento do AWS como administrador da conta. Navegue até a seção IAM do Console da AWS, selecione **Políticas** na barra de navegação e selecione **Criar Política**.

![]({{site.baseurl}}/assets/img/create_policy_1_list.png)

{% alert note %}
Políticas diferentes são necessárias para Currents e Exportação de Dados do Dashboard. `s3:GetObject` é necessário para permitir que o backend do Braze realize o tratamento de erros.
{% endalert %}

Abra a guia **JSON** e insira o seguinte trecho de código na seção **Policy Document (Documento de política)**. Não se esqueça de substituir `INSERTBUCKETNAME` pelo nome de seu bucket. Selecione **Revisar política** quando terminar.

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

Em seguida, dê um nome e uma descrição à política e selecione **Criar Política**.

![]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### Etapa 2: criar função {#role-arn-2}

Dentro da mesma seção IAM do console, selecione **Funções** > **Criar Função**.

![]({{site.baseurl}}/assets/img/create_role_1_list.png)

Recupere o ID de sua conta Braze e o ID externo de sua conta Braze:
- **Currents:** No Braze, acesse **Integrações de Parceiros** > **Exportação de Dados**. Em seguida, selecione **Criar Atual** e depois **Exportação de Dados do Amazon S3**. Aqui você encontrará os identificadores necessários para criar sua função.
- **Exportação de dados do dashboard**: No Braze, acesse **Integrações de Parceiros** > **Parceiros de Tecnologia** e selecione **Amazon S3**. Aqui você encontrará os identificadores necessários para criar sua função.

No console do AWS, selecione **Another AWS Account** (Outra conta da AWS) como o tipo de seletor de entidade confiável. Forneça o ID da sua conta da Braze, marque a caixa **Require external ID** (Exigir ID externo) e digite o ID externo da Braze. Selecione **Avançar** quando terminar.

![A página "Create Role" (Criar função) do S3. Essa página tem campos para nome da função, descrição da função, entidades confiáveis, políticas e limite de permissões.]({{site.baseurl}}/assets/img/create_role_2_another.png)

### Etapa 3: Anexar política {#role-arn-3}

Em seguida, anexe à função a política que você criou anteriormente. Procure a apólice na barra de pesquisa e coloque uma marca de seleção ao lado da apólice para anexá-la. Selecione **Avançar** quando terminar.

![Função do ARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)

Dê um nome e uma descrição à função e selecione **Criar Função**.

![Função do ARN]({{site.baseurl}}/assets/img/create_role_4_name.png)

Agora você deve ver a função recém-criada na lista.

### Etapa 4: link para o AWS da Braze {#role-arn-4}

No console do AWS, localize sua função recém-criada na lista. Selecione o nome para abrir os detalhes dessa função.

![]({{site.baseurl}}/assets/img/create_role_5_created.png)

Observe o **ARN da função** na parte superior da página de resumo da função.

![]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Retorne à sua conta da Braze e copie o ARN da função no campo fornecido.

{% tabs %}
{% tab Braze Currents %}

No Braze, acesse a página **Currents** em **Integrações**. Em seguida, selecione **Criar Atual** e selecione **Exportação de Dados do Amazon S3**.

![]({{site.baseurl}}/assets/img/currents-role-arn.png)

Dê um nome à sua Corrente. Então, na seção **Credenciais**, certifique-se de que **ARN da Função da AWS** está selecionado, em seguida, forneça seu ARN da função e nome do bucket S3 da AWS nos campos designados.

Você também pode adicionar as seguintes personalizações de acordo com suas necessidades:

- Jornada da pasta (o padrão é `currents`)
- Criptografia AES-256 do lado do servidor, em repouso (o padrão é OFF) – inclui o cabeçalho `x-amz-server-side-encryption` 

Selecione **Iniciar Current** para continuar. Uma notificação indicará se suas credenciais foram validadas com sucesso. O AWS S3 agora deve estar configurado para o Braze Currents.

{% alert important %}
Se você receber um erro "As credenciais do S3 são inválidas", isso poderá ser devido à integração muito rápida após a criação de uma função no AWS. Aguarde e tente novamente.
{% endalert %}

{% endtab %}
{% tab Exportação de dados do dashboard %}

No Braze, acesse a página **Parceiros de Tecnologia** em **Integrações** e selecione **Amazon S3**.

![]({{site.baseurl}}/assets/img/data-export-role-arn.png)

Na página **AWS Credentials (Credenciais da AWS** ), certifique-se de que o botão de opção **AWS Role ARN** esteja selecionado e, em seguida, insira o ARN da sua função e o nome do bucket S3 da AWS nos campos designados. Selecione **Testar Credenciais** primeiro para confirmar se suas credenciais funcionam corretamente, em seguida, selecione **Salvar** quando for bem-sucedido.

{% alert tip %}
Você sempre pode recuperar novas credenciais navegando até seu usuário e selecionando **Criar Chave de Acesso** na aba **Credenciais de Segurança** dentro do Console da AWS.
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
