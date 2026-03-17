---
nav_title: Exportação de eventos de segurança com S3
article_title: Exportação de Configurações de Segurança com S3
page_order: 1
page_type: reference
description: "Este artigo de referência cobre como exportar automaticamente eventos de segurança todos os dias à meia-noite UTC para o Amazon S3."
---

# Exportação de eventos de segurança com Amazon S3

> Você pode exportar automaticamente eventos de segurança para o Amazon S3, um provedor de armazenamento em nuvem, com um trabalho diário que é executado à meia-noite UTC. Após a configuração, você não precisa exportar manualmente eventos de segurança do dashboard. O trabalho exporta os eventos de segurança das últimas 24 horas em formato CSV para o seu armazenamento S3 configurado. O arquivo CSV tem a mesma estrutura que um relatório exportado manualmente.

{% alert note %}
O limite de 10.000 linhas se aplica apenas ao download manual do relatório CSV do dashboard. As exportações de eventos de segurança para S3 não estão sujeitas a esse limite de linhas.
{% endalert %}

Braze suporta dois métodos diferentes de autenticação e autorização S3 para configurar a exportação do Amazon S3:

- Método da chave de acesso secreta da AWS
- Método ARN da função AWS

## Método da chave de acesso secreta da AWS

Este método gera uma chave secreta e um ID de chave de acesso que permite ao Braze se autenticar como um usuário na sua conta AWS para gravar dados no seu bucket.

### Etapa 1: Crie um usuário de Gerenciamento de Identidade e Acesso (IAM)

Para recuperar sua chave de acesso secreta e ID de chave de acesso, você precisará criar um usuário IAM, seguindo as instruções em [Configurando sua conta AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html#create-an-admin).

### Etapa 2: Obtenha credenciais

1. Após criar um novo usuário, gere a chave de acesso e baixe seu ID de chave de acesso e chave de acesso secreta.

![Uma página de resumo para um papel chamado "liyu-chen-test".]({% image_buster /assets/img/security_export/credentials1.png %})

{: start="2"}
2\. Anote essas credenciais em algum lugar ou baixe os arquivos de credenciais, pois você precisará inseri-los no Braze mais tarde.

![Campos contendo a chave de acesso e a chave de acesso secreta.]({% image_buster /assets/img/security_export/retrieve_access_keys.png %})

### Etapa 3: Criar política

1. Acesse **IAM** (Gerenciamento de Identidade e Acesso) > **Políticas** > **Criar Política** para adicionar permissões ao seu usuário. 
2. Selecione **Criar Sua Própria Política**, que dá permissões limitadas para que o Braze possa acessar apenas os buckets especificados.
3. Especifique um nome de política de sua escolha.
4. Insira o seguinte trecho de código na seção **Documento da Política**. Certifique-se de substituir "INSERTBUCKETNAME" pelo nome do seu bucket. Sem essas permissões, a integração falhará na verificação de credenciais e não será criada.

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

1. Após criar uma nova política, acesse **Usuários** e selecione seu usuário específico. 
2. Na aba **Permissões**, selecione **Adicionar Permissões**, anexe diretamente a política e, em seguida, selecione essa política. 

Agora, você está pronto para vincular suas credenciais da AWS à sua conta do Braze!

### Etapa 5: Vincular Braze à AWS

1. No Braze, acesse **Configurações** > **Configurações da Empresa** > **Configurações de Admin** > **Configurações de Segurança** e role até a seção **Download de Eventos de Segurança**.
2. Ative **Exportar para AWS S3** em **Exportar para armazenamento em nuvem** e selecione **chave de acesso secreto da AWS**, que habilita a exportação para S3. 
3. Insira o seguinte:
- ID da chave de acesso da AWS
- Chave de acesso de segredo do AWS
    - Ao inserir esta chave, primeiro selecione **Testar Credenciais** para confirmar que suas credenciais funcionam.
- Nome do bucket AWS 

![A página "Download de Eventos de Segurança" com IDs de conta Braze e IDs externos do Braze preenchidos.]({% image_buster /assets/img/security_export/security_event_download1.png %})

{: start="4"}
4\. Selecione **Salvar Alterações**. 

![Botão "Salvar alterações".]({% image_buster /assets/img/security_export/save_changes_button.png %}){: style="max-width:50%;"}

Você integrou o AWS S3 à sua conta do Braze!

## Método ARN da função AWS

O método ARN de função da AWS gera um Nome de Recurso da Amazon (ARN) de função que permite que a conta da Amazon Braze se autentique como um membro dessa função.

### Etapa 1: Criar política

1. Faça login no console de gerenciamento da AWS como um administrador da conta. 
2. No console da AWS, acesse a seção **IAM** (Gerenciamento de Identidade e Acesso) > **Políticas**, e então selecione **Criar Política**.

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
4\. Selecione **Próximo** após revisar a política.

![Uma página que permite revisar sua política e, opcionalmente, adicionar permissões.]({% image_buster /assets/img/security_export/specify_permissions.png %})

{: start="5"}
5\. Dê um nome e uma descrição à política e, em seguida, selecione **Criar Política**.

![Uma página para revisar e criar sua política.]({% image_buster /assets/img/security_export/review_and_create.png %})

### Etapa 2: Criar função

1. No Braze, acesse **Configurações** > **Configurações da Empresa** > **Configurações de Admin** > **Configurações de Segurança** e role até a seção **Download de Eventos de Segurança**. 
2. Selecione **ARN da Função AWS**. 
3. Anote os identificadores, o ID da conta Braze e o ID externo da Braze necessários para criar sua função.

![A página "Download de Eventos de Segurança" com IDs de conta Braze e IDs externos do Braze preenchidos.]({% image_buster /assets/img/security_export/security_event_download2.png %})

4. No console da AWS, acesse a seção **IAM** (Gerenciamento de Identidade e Acesso) > **Funções** > **Criar Função**. 
5. Selecione **Outra Conta da AWS** como o tipo de seletor de entidade confiável. 
6. Forneça seu ID da conta Braze, marque a caixa **Exigir ID externo**, e então insira seu ID externo da Braze. 
7. Selecione **Avançar** quando terminar.

![Uma página com opções para selecionar um tipo de entidade confiável e fornecer informações sobre sua conta da AWS.]({% image_buster /assets/img/security_export/select_trusted_entity.png %})

### Etapa 3: Anexar política

1. Pesquise pela política que você criou anteriormente na barra de pesquisa e, em seguida, marque a caixa ao lado da política para anexá-la. 
2. Selecione **Próximo**.

![Uma lista de políticas com colunas para seu tipo e descrição.]({% image_buster /assets/img/security_export/add_permissions.png %})

{: start="3"}
3\. Dê um nome e uma descrição à função e selecione **Criar Função**.

![Campos para fornecer detalhes da função, como nome, descrição, política de confiança, permissões e tags.]({% image_buster /assets/img/security_export/name_review_create.png %})

Sua nova função criada aparecerá na lista!

### Etapa 4: Link para Braze AWS

1. No console do AWS, localize sua função recém-criada na lista. Selecione o nome para abrir os detalhes desse papel e anote o **ARN**.

![A página de resumo para um papel chamado "security-event-export-olaf".]({% image_buster /assets/img/security_export/credentials2.png %})

{: start="2"}
2\. No Braze, acesse **Configurações** > **Configurações da Empresa** > **Configurações de Administrador** > **Configurações de Segurança** e role até a seção **Download de Evento de Segurança**.

![Seção "Download de Evento de Segurança" com um interruptor ativado para "Exportar para AWS S3".]({% image_buster /assets/img/security_export/security_event_download3.png %})

{: start="3"}
3\. Certifique-se de que **ARN do papel AWS** esteja selecionado, em seguida, insira seu ARN de papel e o nome do bucket S3 da AWS nos campos designados.
4\. Selecione **Testar Credenciais** para confirmar que suas credenciais funcionam corretamente.
5\. Selecione **Salvar Alterações**. 

![Botão "Salvar alterações".]({% image_buster /assets/img/security_export/save_changes_button.png %}){: style="max-width:40%;"}

Você integrou o AWS S3 à sua conta do Braze!