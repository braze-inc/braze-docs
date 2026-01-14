---
nav_title: OneLogin
article_title: OneLogin
page_order: 5
page_type: tutorial
description: "Este artigo o orientará sobre como configurar o Braze para usar o OneLogin para logon único."

---

# OneLogin

> [O OneLogin](https://www.onelogin.com/) é uma plataforma de identidade em nuvem que oferece uma solução abrangente para o gerenciamento de identidades de usuários. O OneLogin se integra a aplicativos na nuvem e no local usando SAML 2.0, para Single Sign-On (SSO), provisionamento de usuários, autenticação multifator e muito mais.

## Requisitos

Após a configuração, você será solicitado a fornecer uma URL de logon e uma URL do Assertion Consumer Service (ACS).  

| Requisito | Detalhes |
|---|---|
| Domínio Braze | Você precisará de seu domínio Braze para configurar o Braze no OneLogin. Se a sua instância for `US-01`, você precisará inserir o URL do painel no painel do OneLogin. <br><br> Por exemplo, se o URL do seu painel for `https://dashboard-01.braze.com`, você precisará inserir `dashboard-01.braze.com`.  |
| Chave da API do RelayState | Para ativar o login do IdP, vá para **Settings** > **API Keys** ( **Configurações** > **Chaves de API** ) e crie uma chave de API com permissões `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Login iniciado por IdP no OneLogin

### Etapa 1: Configurar o aplicativo Braze

1. Faça login no [OneLogin](https://app.onelogin.com/login). Clique em **Administration (Administração**).]({% image_buster /assets/img/onelogin_1.jpg %})<br><br>
2. Acesse **Apps** > **Add Apps** ( **Aplicativos** > **Adicionar aplicativos** ) na barra de navegação superior. Pesquise por "Braze" e selecione o aplicativo Braze! [Resultados da pesquisa para o Braze no OneLogin.]({% image_buster /assets/img/onelogin_2.jpg %})<br><br>
3. Salve o aplicativo Braze em sua empresa!]({% image_buster /assets/img/onelogin_3.jpg %})<br><br>
4. Quando salvo, vá para **Configuração** e adicione seu **domínio Braze** e a chave de API **RelayState**.]({% image_buster /assets/img/onelogin_4.png %})<br><br>
5. O Braze espera as asserções SAML em um [formato específico]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#configure-your-identity-provider). Em **Parâmetros**, os atributos suportados pelo Braze devem ser preenchidos previamente. Verifique se eles estão corretos. [Parâmetros SAML do Braze no OneLogin.]({% image_buster /assets/img/onelogin_5.jpg %})<br><br>
6. Copie o **certificado** e o **ponto de extremidade SAML 2.0 (HTTP)** necessários para configurar o painel do Braze na guia **SSO**.]({% image_buster /assets/img/onelogin_6.jpg %})

### Etapa 2: Configurar o OneLogin no Braze

Depois de configurar o Braze em seu OneLogin, eles fornecerão um URL de destino (`SAML 2.0 Endpoint (HTTP)`) e um certificado `x.509` que você inserirá em sua conta do Braze.

Depois que o gerente da conta tiver ativado o SAML SSO para sua conta, acesse **Configurações** > Configurações **administrativas** > **Configurações de segurança** e alterne a seção SAML SSO para **ATIVADO**

Nessa página, insira o seguinte:

| Requisito | Detalhes |
|---|---|
| `SAML Name` | Isso aparecerá como o texto do botão na tela de login. Normalmente, esse é o nome do seu provedor de identidade, como "OneLogin". |
| `Target URL` | Este é o URL `SAML 2.0 Endpoint (HTTP)` fornecido pelo OneLogin.|
| `Certificate` | O certificado codificado em `x.509` PEM é fornecido pelo OneLogin. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Configurações de SSO SAML com o botão de alternância selecionado.]({% image_buster /assets/img/samlsso.png %})

{% alert tip %}
Se quiser que os usuários da sua conta Braze façam login apenas com SAML SSO, você poderá [restringir a autenticação de logon único]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) na página **Configurações da empresa**.
{% endalert %}

