---
nav_title: Migração para o envio de mensagens do Firebase Cloud
article_title: Migração para a API do Firebase Cloud Messaging
platform: Android
page_order: 29
description: "Este artigo aborda como migrar da API de envio de mensagens em nuvem descontinuada do Google para o Firebase Cloud Messaging (FCM)."
channel:
  - push
search_rank: 3
---

# Migração para a API do Firebase Cloud Messaging

> Saiba como migrar da obsoleta API de envio de mensagens na nuvem do Google para a API do Firebase Cloud Messaging (FCM), que conta com suporte total. Para saber mais, veja as [Perguntas Frequentes do Firebase do Google - 2023](https://firebase.google.com/support/faq#fcm-23-deprecation).

{% alert important %}
Se esta é a primeira vez que você está configurando a integração push para Android, consulte [Integração push padrão do Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration) em vez disso.
{% endalert %}

## Limite de taxa

A API do Firebase Cloud Messaging (FCM) tem um limite de frequência padrão de 600.000 solicitações por minuto. Se você atingir esse limite, o Braze tentará automaticamente outra vez em alguns minutos. Para solicitar um aumento, entre em contato com o [suporte do Firebase](https://firebase.google.com/support).

## Migração para o FCM

### Etapa 1: Verifique seu ID do Projeto

Primeiro, abra o Google Cloud. Na página inicial do seu projeto, verifique o número no campo **Project ID**—você comparará isso com o do seu projeto Firebase a seguir.

![A página inicial do projeto do Google Cloud com o "ID do Projeto" destacado.]({% image_buster /assets/img/android/push_integration/migration/verify-project-id/project-id-gcp.png %})

Em seguida, abra o Firebase Console, depois selecione <i class="fa-solid fa-gear"></i> **Settings** > **Project settings** (Configurações > Configurações do projeto).

![O projeto Firebase com o menu "Settings" (Configurações) aberto.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Na guia **Geral**, verifique se o **ID do Projeto** corresponde ao listado no seu projeto do Google Cloud.

![A página "Configurações" do projeto Firebase com o "ID do Projeto" destacado.]({% image_buster /assets/img/android/push_integration/migration/verify-project-id/project-id-gfb.png %})

### Etapa 2: Verifique seu ID do remetente

Primeiro, abra a Braze e selecione <i class="fa-solid fa-gear"></i> **Configurações** > **Configurações do app**.

![O menu "Configurações" aberto na Braze com "Configurações do app" destacado.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %}){: style="max-width:80%;"}

Nas **Configurações de Notificação por Push** do seu app Android, verifique o número no campo **ID do Remetente do Firebase Cloud Messaging**—você irá compará-lo com o do seu projeto Firebase a seguir.

![O formulário para "Configurações de notificação por push".]({% image_buster /assets/img/android/push_integration/migration/verify-sender-id/verify-sender-id.png %})

Em seguida, abra o Firebase Console, depois selecione <i class="fa-solid fa-gear"></i> **Settings** > **Project settings** (Configurações > Configurações do projeto).

![O projeto Firebase com o menu "Settings" (Configurações) aberto.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Selecione **Cloud Messaging**. Em **API de envio de mensagens na nuvem (Legado)**, verifique se o **ID do remetente** corresponde ao listado no seu dashboard do Braze.

![A página "Cloud Messaging" do projeto Firebase com o "Sender ID" (ID do remetente) destacado.]({% image_buster /assets/img/android/push_integration/migration/verify-sender-id/verify-sender-id-firebase.png %})

### Etapa 3: Ativar a API do Firebase Cloud Messaging

No Google Cloud, selecione o projeto que seu app Android está usando e ative a [API do Firebase Cloud Messaging](https://console.cloud.google.com/apis/library/fcm.googleapis.com).

![API do Firebase Cloud Messaging ativada]({% image_buster /assets/img/android/push_integration/create_a_service_account/firebase-cloud-messaging-api-enabled.png %}){: style="max-width:80%;"}

### Etapa 4: Criar uma Conta de Serviço

Em seguida, crie uma nova conta de serviço, para que a Braze possa fazer chamadas de API autorizadas ao registrar tokens FCM. No Google Cloud, acesse **Contas de Serviço**, depois escolha seu projeto. Na página **Contas de serviço**, selecione **Criar conta de serviço**.

![Página inicial da conta de serviço de um projeto com a opção "Criar conta de serviço" destacada.]({% image_buster /assets/img/android/push_integration/create_a_service_account/select-create-service-account.png %})

Insira um nome de conta de serviço, ID e descrição, em seguida selecione **Criar e continuar**.

![O formulário para "Detalhes da conta de serviço".]({% image_buster /assets/img/android/push_integration/create_a_service_account/enter-service-account-details.png %})

No campo **Função**, encontre e selecione **Admin da API do Firebase Cloud Messaging** na lista de funções. Para um acesso mais restritivo, crie uma [função personalizada](https://cloud.google.com/iam/docs/creating-custom-roles) com a permissão `cloudmessaging.messages.create`, e então escolha-a na lista. Quando terminar, selecione **Concluído**.

{% alert warning %}
Selecione _Admin da **API** do Firebase Cloud Messaging_, não _Admin do Firebase Cloud Messaging_.
{% endalert %}

![O formulário para "Conceder acesso a esta conta de serviço ao projeto" com "Administrador da API do Firebase Cloud Messaging" selecionado como função.]({% image_buster /assets/img/android/push_integration/create_a_service_account/add-fcm-api-admin.png %})

### Etapa 5: Verificar permissões (opcional)

Para verificar quais permissões sua conta de serviço possui, abra o Google Cloud, depois acesse seu projeto e selecione **IAM**. Em **Ver Por Principais**, selecione **Permissões em Excesso**.

![A guia "Ver por Princípios" com o número de permissões em excesso listadas para cada principal.]({% image_buster /assets/img/android/push_integration/create_a_service_account/select-excess-permissions.png %})

Agora você pode revisar as permissões atuais atribuídas ao seu cargo selecionado.

![A lista de permissões atuais atribuídas à função selecionada.]({% image_buster /assets/img/android/push_integration/create_a_service_account/review-permissions.png %}){: style="max-width:75%;"}

### Etapa 6: Gerar credenciais JSON

Em seguida, gere credenciais JSON para sua conta de serviço FCM. No Google Cloud IAM & Admin, acesse **Service Accounts**, depois escolha seu projeto. Localize a conta de serviço FCM [que você criou anteriormente](#step-4-create-a-service-account) e selecione <i class="fa-solid fa-ellipsis-vertical"></i> **Actions** > **Manage Keys**.

![A página inicial da conta de serviço do projeto com o menu "Actions" (Ações) aberto.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-manage-keys.png %})

Selecione **Adicionar chave** > **Criar nova chave**.

{% alert note %}
Criar uma nova chave não removerá suas antigas. Se você excluir acidentalmente sua nova chave selecionando **Reverter Credenciais**, a Braze usará suas chaves legadas como backup.
{% endalert %}

![A conta de serviço selecionada com o menu "Adicionar Chave" aberto.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create-new-key.png %})

Escolha **JSON**, depois selecione **Criar**. Se você criou sua conta de serviço usando um ID de projeto do Google Cloud diferente do ID de projeto do FCM, será necessário atualizar manualmente o valor atribuído ao `project_id` no seu arquivo JSON.

Lembre-se de onde baixou a chave - você precisará dela na próxima etapa.

![O formulário para criar uma chave privada com "JSON" selecionado.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create.png %}){: style="max-width:65%;"}

{% alert warning %}
As chaves privadas podem representar um risco de segurança se forem comprometidas. Armazene suas credenciais JSON em um local seguro por enquanto — você excluirá sua chave depois de fazer upload para a Braze.
{% endalert %}

### Etapa 7: fazer upload suas credenciais JSON para Braze

No Braze, selecione <i class="fa-solid fa-gear"></i> **Configurações** > **Configurações do app**.

![O menu "Configurações" aberto na Braze com "Configurações do app" destacado.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %})

Em **Configurações de Notificação por Push**, selecione **Fazer Upload de Arquivo JSON**, depois escolha o arquivo [que você gerou anteriormente](#step-6-generate-json-credentials). Quando terminar, selecione **Salvar**.

![O formulário para "Configurações de notificação por push" com a chave privada atualizada no campo "Chave do servidor do Firebase Cloud Messaging".]({% image_buster /assets/img/android/push_integration/migration/upload_json_credentials/upload-json-file.png %})

{% alert warning %}
Chaves privadas podem representar um risco de segurança se comprometidas. Agora que sua chave foi carregada para a Braze, exclua o arquivo [que você gerou anteriormente](#step-6-generate-json-credentials) do seu computador.
{% endalert %}

### Etapa 8: Teste suas novas credenciais (opcional)

Assim que você fizer upload de suas credenciais para a Braze, poderá começar a enviar notificações por push usando suas novas credenciais. Para testar suas novas credenciais, envie uma notificação por push real ou de teste para seu app usando FCM ou Braze. Se a notificação por push for enviada, tudo está funcionando. Se não: 

- [Verifique seu ID de remetente](#step-2-verify-your-sender-id)
- [Verifique suas permissões](#step-5-verify-permissions-optional)
- Revise os erros de notificação por push no seu [registro de atividade de mensagens]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)

Se você ainda estiver com problemas, veja [Reversão de credenciais](#reverting-your-credentials).

## Reversão de credenciais

Você pode excluir suas novas credenciais e restaurar suas credenciais legadas a qualquer momento. Assim que suas credenciais forem restauradas, você pode começar a enviar notificações por push usando suas credenciais legadas.

No Braze, selecione <i class="fa-solid fa-gear"></i> **Configurações** > **Configurações do app**. Em **Configurações de notificação por push**, selecione **Reverter credenciais**.

{% alert warning %}
Após excluir suas novas credenciais não será possível restaurá-las depois. Você precisará [gerar novas credenciais](#step-6-generate-json-credentials) e [fazer upload delas para a Braze](#step-7-upload-your-json-credentials-to-braze) novamente.
{% endalert %}

![O formulário para "Configurações de notificação por push" com o botão "Reverter credenciais" destacado.]({% image_buster /assets/img/android/push_integration/revert-credentials.png %})

## Perguntas Frequentes (FAQ) {#faq}

### Como eu sei que minhas novas credenciais estão funcionando?

Suas novas credenciais começam a funcionar assim que você fazer upload delas para a Braze. Para testá-los, selecione **Credenciais de Teste**. Se você receber um erro, sempre pode [reverter suas credenciais](#reverting-your-credentials).

### Preciso migrar para o FCM para meus aplicativos não utilizados ou aplicativos de desenvolvimento?

Não. No entanto, seus aplicativos não utilizados e aplicativos de desenvolvimento continuarão a mostrar uma mensagem de aviso pedindo para você migrar. Para remover esta mensagem, você pode fazer upload de novas credenciais ou excluir esses aplicativos do seu espaço de trabalho. Se você optar por excluir esses aplicativos, certifique-se de verificar com sua equipe primeiro, caso alguém os esteja usando.

### Onde posso verificar mensagens de erro?

Você pode revisar erros de notificação por push no seu [registro de atividade de mensagens]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/).

### Antes de migrar, preciso atualizar meu app ou SDK?

Não. Você só precisa fazer upload de suas novas credenciais para a Braze.

### Preciso excluir minhas credenciais legadas antigas primeiro?

Não. Se você precisar excluir suas novas credenciais, [suas credenciais legadas podem ser usadas em vez disso](#reverting-your-credentials).

### Depois de migrar, por que ainda há uma mensagem de aviso na Braze?

Você continuará a ver esta mensagem de aviso se houver pelo menos um app Android no seu espaço de trabalho que você ainda precisa migrar. Certifique-se de migrar todos os seus aplicativos Android para a API FCM totalmente suportada pelo Google.

### Depois de migrar, quanto tempo até eu enviar notificações por push novamente?

Após a migração, você pode começar a enviar notificações por push usando suas novas credenciais imediatamente.

### E se eu criar minha conta de serviço usando um projeto diferente do meu projeto FCM?

Se você criou sua conta de serviço usando um ID de projeto do Google Cloud diferente do ID de projeto do FCM, precisará atualizar manualmente o valor atribuído ao `project_id` em seu arquivo JSON depois de [criar um novo](#step-6-generate-json-credentials).
