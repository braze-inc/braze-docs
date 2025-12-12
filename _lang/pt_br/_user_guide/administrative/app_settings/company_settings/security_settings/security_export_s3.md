---
nav_title: Exportação de eventos de segurança com o S3
article_title: Exportação de configurações de segurança com S3
page_order: 1
page_type: reference
description: "Este artigo de referência aborda como exportar automaticamente eventos de segurança todos os dias à meia-noite UTC para o Amazon S3."
---

# Exportação de eventos de segurança com o Amazon S3

> Você pode exportar automaticamente eventos de segurança para o Amazon S3, um provedor de armazenamento em nuvem, com um trabalho diário que é executado à meia-noite UTC. Após a configuração, você não precisará exportar manualmente os eventos de segurança do painel. O trabalho exportará os eventos de segurança das últimas 24 horas em formato CSV para o armazenamento S3 configurado. O arquivo CSV terá a mesma estrutura de um relatório exportado manualmente.

O Braze oferece suporte a dois métodos diferentes de autenticação e autorização do S3 para configurar a exportação do Amazon S3:

- Método de chave de acesso secreto da AWS
- Método ARN da função AWS

## Método de chave de acesso secreto da AWS

Esse método gera uma chave secreta e um ID de chave de acesso que permite que o Braze se autentique como um usuário em sua conta da AWS para gravar dados em seu bucket.

### Etapa 1: Crie um usuário de mensagens no aplicativo

Para recuperar a chave de acesso secreta e o ID da chave de acesso, você precisará criar um usuário de mensagem no aplicativo, seguindo as instruções em [Configurar sua conta AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html#create-an-admin).

### Etapa 2: Obter credenciais

1. Depois de criar um novo usuário, gere a chave de acesso e faça o download do ID da chave de acesso e da chave de acesso secreta.

\![Uma página de resumo para uma função chamada "liyu-chen-test".]({% image_buster /assets/img/security_export/credentials1.png %})

{: start="2"}
2\. Anote essas credenciais em algum lugar ou faça download dos arquivos de credenciais, pois você precisará inseri-las no Braze posteriormente.

\![Campos que contêm a chave de acesso e a chave de acesso secreta.]({% image_buster /assets/img/security_export/retrieve_access_keys.png %})

### Etapa 3: Criar política

1. Vá para **IAM** > **Políticas** > **Criar política** para adicionar permissões ao seu usuário. 
2. Selecione **Criar sua própria política**, que concede permissões limitadas para que o Braze possa acessar apenas os buckets especificados.
3. Especifique um nome de política de sua escolha.
4. Insira o seguinte trecho de código na seção **Policy Document (Documento de política** ). Não se esqueça de substituir "INSERTBUCKETNAME" pelo nome do seu bucket. Sem essas permissões, a integração falhará em uma verificação de credenciais e não será criada.

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

### Etapa 4: Anexar política

1. Depois de criar uma nova política, vá para **Usuários** e selecione seu usuário específico. 
2. Na guia **Permissões**, selecione **Adicionar permissões**, anexe diretamente a política e, em seguida, selecione essa política. 

Agora, você está pronto para vincular suas credenciais da AWS à sua conta Braze!

### Etapa 5: Vincular o Braze ao AWS

1. No Braze, vá para **Configurações** > **Configurações da empresa** > Configurações **administrativas** > **Configurações de segurança** e role até a seção **Download de eventos de segurança**.
2. Ative **Exportar para o AWS S3** em **Exportar para armazenamento em nuvem** e selecione **a chave de acesso secreta do AWS**, que habilita a exportação para o S3. 
3. Insira o seguinte:
- ID da chave de acesso do AWS
- Chave de acesso secreto da AWS
    - Ao inserir essa chave, primeiro selecione **Test Credentials (Testar credenciais** ) para confirmar que suas credenciais funcionam.
- Nome do bucket do AWS 

A página "Security Event Download" com a conta Braze preenchida e as IDs externas Braze.]({% image_buster /assets/img/security_export/security_event_download1.png %})

{: start="4"}
4\. Selecione **Salvar alterações**. 

\![ botão "Salvar alterações".]({% image_buster /assets/img/security_export/save_changes_button.png %}){: style="max-width:50%;"}

Você integrou o AWS S3 à sua conta Braze!

## Método ARN da função AWS

O método ARN de função do AWS gera um ARN (Amazon Resource Name) de função que permite que a conta Braze Amazon se autentique como membro dessa função.

### Etapa 1: Criar política

1. Faça login no console de gerenciamento do AWS como administrador da conta. 
2. No console da AWS, vá para a seção **IAM** > **Políticas** e selecione **Criar política**.

\![Uma página com uma lista de políticas e um botão para "Criar política".]({% image_buster /assets/img/security_export/policies.png %})

{: start="3"}
3\. Abra a guia **JSON** e insira o seguinte trecho de código na seção **Policy Document (Documento de política)**. Não se esqueça de substituir `INSERTBUCKETNAME` pelo nome do seu balde. 

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

{: start="4"}
4\. Selecione **Next** após revisar a política.

\![Uma página que permite que você revise sua política e, opcionalmente, adicione permissões.]({% image_buster /assets/img/security_export/specify_permissions.png %})

{: start="5"}
5\. Dê um nome e uma descrição à política e, em seguida, selecione **Criar política**.

\![Uma página para revisar e criar sua política.]({% image_buster /assets/img/security_export/review_and_create.png %})

### Etapa 2: Criar função

1. No Braze, vá para **Configurações** > **Configurações da empresa** > Configurações **administrativas** > **Configurações de segurança** e role até a seção **Download de eventos de segurança**. 
2. Selecione **AWS Role ARN**. 
3. Anote os identificadores, o ID da conta Braze e o ID externo Braze necessários para criar sua função.

A página "Security Event Download" com a conta Braze preenchida e as IDs externas Braze.]({% image_buster /assets/img/security_export/security_event_download2.png %})

4. No console do AWS, vá para a seção **IAM** > **Funções** > **Criar função**. 
5. Selecione **Outra conta AWS** como o tipo de seletor de entidade confiável. 
6. Forneça seu ID de conta Braze, marque a caixa **Exigir ID externo** e, em seguida, insira seu ID externo Braze. 
7. Selecione **Next** quando terminar.

\![Uma página com opções para selecionar um tipo de entidade confiável e fornecer informações sobre sua conta do AWS.]({% image_buster /assets/img/security_export/select_trusted_entity.png %})

### Etapa 3: Anexar política

1. Procure a política que você criou anteriormente na barra de pesquisa e, em seguida, coloque uma marca de seleção ao lado da política para anexá-la. 
2. Selecione **Next**.

\![Uma lista de políticas com colunas para seu tipo e descrição.]({% image_buster /assets/img/security_export/add_permissions.png %})

{: start="3"}
3\. Dê um nome e uma descrição à função e selecione **Create Role (Criar função**).

Campos para fornecer detalhes da função, como o nome, a descrição, a política de confiança, as permissões e as tags.]({% image_buster /assets/img/security_export/name_review_create.png %})

Sua função recém-criada aparecerá na lista!

### Etapa 4: Link para o Braze AWS

1. No Console do AWS, localize a função recém-criada na lista. Selecione o nome para abrir os detalhes dessa função e anote o **ARN**.

\![A página de resumo de uma função chamada "security-event-export-olaf".]({% image_buster /assets/img/security_export/credentials2.png %})

{: start="2"}
2\. No Braze, vá para **Configurações** > **Configurações da empresa** > Configurações **de administrador** > **Configurações de segurança** e role até a seção **Download de eventos de segurança**.

\!["Security Event Download" (Download de eventos de segurança) com uma opção ativada para "Export to AWS S3" (Exportar para AWS S3).]({% image_buster /assets/img/security_export/security_event_download3.png %})

{: start="3"}
3\. Certifique-se de que **o ARN da função AWS** esteja selecionado e, em seguida, insira o ARN da função e o nome do bucket do AWS S3 nos campos designados.
4\. Selecione **Test Credentials (Testar credenciais** ) para confirmar que suas credenciais funcionam corretamente.
5\. Selecione **Salvar alterações**. 

\![ botão "Salvar alterações".]({% image_buster /assets/img/security_export/save_changes_button.png %}){: style="max-width:40%;"}

Você integrou o AWS S3 à sua conta Braze!