---
nav_title: OneLogin
article_title: OneLogin
page_order: 5
page_type: tutorial
description: "Este artigo explicará como configurar a Braze para usar o OneLogin para logon único."

---

# OneLogin

> [O OneLogin](https://www.onelogin.com/) é uma plataforma de identidade em nuvem que fornece uma solução abrangente para o gerenciamento de identidades de usuários. O OneLogin se integra a aplicativos na nuvem e no local usando SAML 2.0, para logon único (SSO), provisionamento de usuários, autenticação multifator e muito mais.

## Solicitações

Após a configuração, solicitaremos que você forneça uma URL de login e um URL do Assertion Consumer Service (ACS).  

| Requisito | Informações |
|---|---|
| Domínio Braze | Você precisará de seu domínio Braze para configurar o Braze no OneLogin. Se a sua instância for `US-01`, será necessário inserir o URL do painel no painel do OneLogin. <br><br> Por exemplo, se o URL do seu dashboard for `https://dashboard-01.braze.com`, você precisará inserir `dashboard-01.braze.com`.  |
| Chave de API do RelayState | Para ativar o login IdP, Acessar **Configurações** > **Chaves de API** e criar uma chave de API com permissões de `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Login iniciado por IdP no OneLogin

### Etapa 1: Configurar o app Braze

1. Faça o registro no [OneLogin](https://app.onelogin.com/login). Clique em **Administration**.![Página de administração do OneLogin.]({% image_buster /assets/img/onelogin_1.jpg %})<br><br>
2. Acesse **Apps** > **Add Apps** na barra de navegação superior. Pesquise "Braze" e selecione o app Braze.![Resultados da pesquisa para a Braze no OneLogin.]({% image_buster /assets/img/onelogin_2.jpg %})<br><br>
3. Salve o app da Braze em sua empresa.![]({% image_buster /assets/img/onelogin_3.jpg %})<br><br>
4. Quando salvo, acesse **Configuração** e adicione seu **domínio Braze** e a chave de API **RelayState**.![Guia Configuração do OneLogin para o aplicativo Braze.]({% image_buster /assets/img/onelogin_4.png %})<br><br>
5. O Braze espera as asserções SAML em um [formato específico]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#configure-your-identity-provider). Em **Parâmetros**, as atribuições aceitas pela Braze devem ser pré-preenchidas. Verifique se eles estão corretos.![Parâmetros SAML da Braze no OneLogin.]({% image_buster /assets/img/onelogin_5.jpg %})<br><br>
6. Copie o **certificado** e o **ponto de extremidade SAML 2.0 (HTTP)** necessários para configurar o dashboard do Braze na guia **SSO**.![Certificados para copiar da guia SSO do app do Braze no OneLogin.]({% image_buster /assets/img/onelogin_6.jpg %})

### Etapa 2: Configurar o OneLogin no Braze

Depois de configurar a Braze em seu OneLogin, eles fornecerão um URL de direcionamento (`SAML 2.0 Endpoint (HTTP)`) e um certificado `x.509` que você inserirá em sua conta da Braze.

Depois que o gerente da conta ativar o SAML SSO para sua conta, acesse **Configurações** > **Configurações administrativas** > **Configurações de segurança** e alterne a seção SAML SSO para **ATIVADO**

Nessa página, insira o seguinte:

| Requisito | Informações |
|---|---|
| `SAML Name` | Isso aparecerá como o texto do botão na tela de login. Normalmente, esse é o nome de seu provedor de identidade, como "OneLogin". |
| `Target URL` | Este é o URL `SAML 2.0 Endpoint (HTTP)` fornecido pelo OneLogin.|
| `Certificate` | O certificado codificado em `x.509` PEM é fornecido por seu OneLogin. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Configurações de SAML SSO com o botão de alternância selecionado.]({% image_buster /assets/img/samlsso.png %})

{% alert tip %}
Se você deseja que os usuários da sua conta Braze façam login apenas com SAML SSO, você pode [restringir a autenticação de logon único]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) na página **Configurações da Empresa**.
{% endalert %}

