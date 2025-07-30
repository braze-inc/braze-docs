---
nav_title: Okta
article_title: Okta
page_order: 4
page_type: tutorial
description: "Este artigo orientará sobre como configurar a Braze para usar o Okta para logon único." 

---

# Okta 

> O Okta conecta qualquer pessoa a qualquer aplicativo em qualquer dispositivo. É um serviço de gerenciamento de identidade de nível empresarial, construído para a nuvem, mas compatível com muitos aplicativos locais. Com o Okta, sua equipe de TI pode gerenciar o acesso de qualquer colaborador a qualquer aplicativo ou dispositivo.

## Solicitações

| Requisito | Informações |
| ----------- | ------- |
| Okta ativado para sua conta | Entre em contato com o gerente da sua conta Braze para ativar isso na sua conta. |
| Privilégios de administrador do Okta | Certifique-se de ter privilégios de administrador antes de configurar o Okta. |
| Privilégios de administrador do Braze | Certifique-se de ter privilégios de administrador antes de configurar o Okta. |
| Chave de API RelayState | Para ativar o login IdP, Acessar **Configurações** > **Chaves de API** e criar uma chave de API com permissões de `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Etapa 1: Configure Braze

### Etapa 1a: Navegue para Configurações de Segurança no Braze

Depois que o gerente da sua conta ativar o SSO SAML para sua conta, acessar **Configurações** > **Configurações de Administrador** > **Configurações de Segurança** e alternar a seção SSO SAML para **LIGADO**.

![SSO do Okta SAML ativado na página Configurações de segurança.]({% image_buster/assets/img/Okta/okta1.png %})

### Etapa 1b: Editar configurações de SSO SAML

No seu dashboard de administração do Okta, você receberá uma URL de destino (URL de login) e `x.509` certificado, que você deve inserir na página **Configurações de Segurança** da sua conta Braze.

![]({% image_buster /assets/img/Okta/okta5.png %}){: style="max-width:75%"}

| Requisito | Informações |
|---|---|
| `SAML Name` | Isso aparecerá como o texto do botão na tela de login. Este é normalmente o nome do seu provedor de identidade, por exemplo, "Okta". |
| `Target URL` | Este é o URL de login fornecido pelo dashboard do administrador do Okta. Encontre-o indo para **Aplicativos** > seu aplicativo > **Geral** guia > **Link de Incorporação do App** > **Link de Incorporação**. |
| `Certificate` | O certificado `x.509` codificado em PEM é fornecido pelo seu provedor de identidade. Você deve copiar e colar neste campo. Recupere-o no Okta acessando **Certificados de Assinatura SAML** e selecionando **Ações** > **baixar certificado**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Selecione **Salvar alterações** na parte inferior da página quando concluído.

## Etapa 2: Configurar Okta

No Okta, selecione a guia **Sign On** para o app Braze SAML, depois clique em **Editar**. 

Em seguida, insira a chave de API do RelayState com permissão `sso.saml.login` no campo **Default Relay State**. 

![Okta Default RelayState na guia Fazer login.]({% image_buster /assets/img/Okta/okta2.png %}){: style="max-width:75%"}

Certifique-se de salvar essas novas configurações.

{% alert tip %}
Se você deseja que os usuários da sua conta Braze façam login apenas com SAML SSO, você pode [restringir a autenticação de logon único]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) na página **Configurações da Empresa**.
{% endalert %}

## Etapa 3: Entrar

Agora você deve conseguir fazer registro na Braze usando Okta!

![Login no dashboard do Braze com o SSO do Okta ativado.]({% image_buster /assets/img/Okta/okta4.png %}){: style="max-width:60%"}

