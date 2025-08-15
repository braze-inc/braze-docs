---
nav_title: Exportação de eventos de segurança com S3
article_title: Exportação de configurações de segurança com S3
page_order: 1
page_type: reference
description: "Este artigo de referência aborda como exportar automaticamente eventos de segurança todos os dias à meia-noite UTC para o Amazon S3."
---

# Exportação de eventos de segurança com o Amazon S3

> Você pode exportar automaticamente os Eventos de Segurança para o Amazon S3, um provedor de armazenamento em nuvem, com um trabalho diário que é executado à meia-noite UTC.  Uma vez configurado, você não precisa exportar manualmente os eventos de segurança do dashboard.

O Braze oferece suporte a dois métodos diferentes de autenticação e autorização do S3 para configurar a exportação do Amazon S3:

- Método da chave de acesso secreta da AWS
- Método ARN da função AWS

## Método da chave de acesso secreta da AWS

Esse método gera uma chave secreta e um ID de chave de acesso que permite que o Braze se autentique como um usuário em sua conta da AWS para gravar dados em seu bucket.

### Etapa 1: Crie um usuário de mensagem no app

Para recuperar a chave de acesso secreta e o ID da chave de acesso, será necessário criar um usuário de mensagem no app, seguindo as instruções em [Configurar sua conta da AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html#create-an-admin).

### Etapa 2: Obter credenciais

1. Depois de criar um novo usuário, gere a chave de acesso e baixe o ID da chave de acesso e a chave de acesso secreta.

![Uma página de resumo para uma função chamada "liyu-chen-test".]({% image_buster /assets/img/security_export/credentials1.png %})

{: start="2"}
2\. Anote essas credenciais em algum lugar ou baixe os arquivos de credenciais, pois será necessário inseri-las no Braze posteriormente.

![Campos que contêm a chave de acesso e a chave de acesso secreta.]({% image_buster /assets/img/security_export/retrieve_access_keys.png %})

### Etapa 3: Criar política

1. Acesse **IAM** > **Políticas** > **Criar política** para adicionar permissões ao seu usuário. 
2. Selecione **Criar sua própria política**, que concede permissões limitadas para que o Braze possa acessar apenas os buckets especificados.
3. Especifique um nome de política de sua escolha.
4. Insira o seguinte trecho de código na seção **Policy Document (Documento de política** ). Certifique-se de substituir "INSERTBUCKETNAME" pelo nome de seu bucket. Sem essas permissões, a integração falhará em uma verificação de credenciais e não será criada.

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

1. Depois de criar uma nova política, acesse **Usuários** e selecione seu usuário específico. 
2. Na guia **Permissões**, selecione **Adicionar permissões**, anexe diretamente a política e, em seguida, selecione essa política. 

Agora, você está pronto para vincular suas credenciais da AWS à sua conta do Braze!

### Etapa 5: Vincular o Braze à AWS

1. No Braze, acesse **Configurações** > **Configurações da empresa** > Configurações **administrativas** > **Configurações de segurança** e role até a seção **Baixar evento de segurança**.
2. Ative **Exportar para AWS S3** em **Exportar para armazenamento em nuvem** e selecione **a chave de acesso secreta da AWS**, que ativa a exportação para S3. 
3. Insira o seguinte:
- ID da chave de acesso da AWS
- Chave de acesso de segredo do AWS
    - Ao inserir essa chave, primeiro selecione **Test Credentials (Testar credenciais** ) para confirmar que suas credenciais funcionam.
- Nome do bucket da AWS 

![A página "Security Event Download" (Baixar evento de segurança) com conta Braze preenchida e IDs externas Braze.]({% image_buster /assets/img/security_export/security_event_download1.png %})

{: start="4"}
4\. Selecione **Salvar alterações**. 

![Botão "Salvar alterações".]({% image_buster /assets/img/security_export/save_changes_button.png %}){: style="max-width:50%;"}

Você integrou o AWS S3 em sua conta Braze!

## Método ARN da função AWS

O método ARN de função da AWS gera um nome de recurso amazônico (ARN) de função que permite que a conta da Braze Amazon se autentique como membro dessa função.

### Etapa 1: Criar política

1. Faça login no console de gerenciamento da AWS como administrador da conta. 
2. No console da AWS, acesse a seção **IAM** > **Políticas** e selecione **Criar política**.

![Uma página com uma lista de políticas e um botão para "Criar política".]({% image_buster /assets/img/security_export/policies.png %})

{: start="3"}
3\. Abra a guia **JSON** e insira o seguinte trecho de código na seção **Policy Document (Documento de política)**. Não se esqueça de substituir `INSERTBUCKETNAME` pelo nome de seu bucket. 

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

![Uma página que permite que você revise sua política e, opcionalmente, adicione permissões.]({% image_buster /assets/img/security_export/specify_permissions.png %})

{: start="5"}
5\. Dê um nome e uma descrição à política e, em seguida, selecione **Criar política**.

![Uma página para revisar e criar sua política.]({% image_buster /assets/img/security_export/review_and_create.png %})

### Etapa 2: Criar função

1. No Braze, acesse **Configurações** > **Configurações da empresa** > Configurações **administrativas** > **Configurações de segurança** e role até a seção **Baixar evento de segurança**. 
2. Selecione **AWS Role ARN**. 
3. Note os identificadores, o ID da conta Braze e o ID externo Braze necessários para criar sua função.

![A página "Security Event Download" (Baixar evento de segurança) com conta Braze preenchida e IDs externas Braze.]({% image_buster /assets/img/security_export/security_event_download2.png %})

4. No console da AWS, acesse a seção **IAM** > **Funções** > **Criar função**. 
5. Selecione **Outra conta AWS** como o tipo de seletor de entidade confiável. 
6. Forneça sua ID de conta Braze, marque a caixa **Exigir ID externa** e, em seguida, insira sua ID externa Braze. 
7. Selecione **Avançar** quando terminar.

![Uma página com opções para selecionar um tipo de entidade confiável e fornecer informações sobre sua conta da AWS.]({% image_buster /assets/img/security_export/select_trusted_entity.png %})

### Etapa 3: Anexar política

1. Procure a política que você criou anteriormente na barra de pesquisa e, em seguida, coloque uma marca de seleção ao lado da política para anexá-la. 
2. Selecione **Próximo**.

![Uma lista de políticas com colunas para seu tipo e descrição.]({% image_buster /assets/img/security_export/add_permissions.png %})

{: start="3"}
3\. Dê um nome e uma descrição à função e selecione **Create Role (Criar função**).

![Campos para fornecer detalhes da função, como o nome, a descrição, a política de confiança, as permissões e as tags.]({% image_buster /assets/img/security_export/name_review_create.png %})

Sua função recém-criada aparecerá na lista!

### Etapa 4: Link para o Braze AWS

1. No console do AWS, localize sua função recém-criada na lista. Selecione o nome para abrir os detalhes dessa função e anote o **ARN**.

![A página de resumo de uma função chamada "security-event-export-olaf".]({% image_buster /assets/img/security_export/credentials2.png %})

{: start="2"}
2\. No Braze, acesse **Configurações** > **Configurações da empresa** > Configurações **administrativas** > **Configurações de segurança** e role até a seção **Baixar evento de segurança**.

![Seção "Security Event Download" (Baixar evento de segurança) com um botão de alternância ativado para "Export to AWS S3" (Exportar para AWS S3).]({% image_buster /assets/img/security_export/security_event_download3.png %})

{: start="3"}
3\. Certifique-se de que **o ARN da função AWS** esteja selecionado e, em seguida, insira o ARN da função e o nome do bucket S3 da AWS nos campos designados.
4\. Selecione **Test Credentials (Testar credenciais** ) para confirmar que suas credenciais funcionam corretamente.
5\. Selecione **Salvar alterações**. 

![Botão "Salvar alterações".]({% image_buster /assets/img/security_export/save_changes_button.png %}){: style="max-width:40%;"}

Você integrou o AWS S3 em sua conta Braze!