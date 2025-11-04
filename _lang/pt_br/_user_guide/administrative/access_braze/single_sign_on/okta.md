---
nav_title: Okta
article_title: Okta
page_order: 4
page_type: tutorial
description: "Este artigo irá guiá-lo sobre como configurar o Braze para usar o Okta para autenticação única." 

---

# Okta 

> Okta conecta qualquer pessoa a qualquer aplicativo em qualquer dispositivo. É um serviço de gerenciamento de identidade de nível empresarial, construído para a nuvem, mas compatível com muitos aplicativos locais. Com o Okta, sua equipe de TI pode gerenciar o acesso de qualquer funcionário a qualquer aplicativo ou dispositivo.

## Requisitos

| Requisito | Detalhes |
| ----------- | ------- |
| Okta ativado para sua conta | Entre em contato com seu gerente de conta do Braze para ativar isso para sua conta. |
| Privilégios de administrador do Okta | Certifique-se de ter privilégios de administrador antes de configurar o Okta. |
| Privilégios de administrador do Braze | Certifique-se de ter privilégios de administrador antes de configurar o Okta. |
| Chave de API RelayState | Para habilitar o login do IdP, vá para **Configurações** > **Chaves de API** e crie uma chave de API com permissões `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Passo 1: Configurar Braze

### Passo 1a: Navegue até Configurações de Segurança no Braze

Depois que seu gerente de conta ativar o SSO SAML para sua conta, vá para **Configurações** > **Configurações do Administrador** > **Configurações de Segurança** e altere a seção SSO SAML para **ATIVADO**.

\![Okta SSO SAML ativado na página de Configurações de Segurança.]({% image_buster/assets/img/Okta/okta1.png %})

### Passo 1b: Editar configurações de SSO SAML

No seu painel de administração do Okta, você receberá uma URL de destino (URL de login) e `x.509` certificado, que você deve inserir na página **Configurações de Segurança** da sua conta Braze.

\![]({% image_buster /assets/img/Okta/okta5.png %}){: style="max-width:75%"}

| Requisito | Detalhes |
|---|---|
| `SAML Name` | Isso aparecerá como o texto do botão na tela de login. Isso é tipicamente o nome do seu provedor de identidade, por exemplo, "Okta". |
| `Target URL` | Esta é a URL de login fornecida pelo painel de administração do Okta. Encontre-a indo para **Aplicações** > seu aplicativo > **Geral** aba > **Link de Incorporação do App** > **Link de Incorporação**. |
| `Certificate` | O certificado `x.509` codificado em PEM é fornecido pelo seu provedor de identidade. Você deve copiá-lo e colá-lo neste campo. Recupere-o no Okta indo para **Certificados de Assinatura SAML** e selecionando **Ações** > **Baixar certificado**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Selecione **Salvar Alterações** na parte inferior da página quando concluído.

## Passo 2: Configurar Okta

No Okta, selecione a aba **Login** para o aplicativo SAML Braze, em seguida, clique em **Editar**. 

Em seguida, insira a chave da API RelayState com `sso.saml.login` permissão no campo **Estado de Relay Padrão**. 

\![Estado de Relay Padrão do Okta na aba Login.]({% image_buster /assets/img/Okta/okta2.png %}){: style="max-width:75%"}

Certifique-se de salvar essas novas configurações.

{% alert tip %}
Se você quiser que os usuários da sua conta Braze façam login apenas com SAML SSO, você pode [restringir a autenticação de login único]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) na página **Configurações da Empresa**.
{% endalert %}

## Passo 3: Faça login

Agora você deve conseguir fazer login no Braze usando o Okta!

\![Login do painel Braze com Okta SSO habilitado.]({% image_buster /assets/img/Okta/okta4.png %}){: style="max-width:60%"}

