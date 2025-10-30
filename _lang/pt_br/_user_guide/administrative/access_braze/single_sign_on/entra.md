---
nav_title: Microsoft Entra SSO
article_title: Microsoft Entra SSO
page_order: 3
page_type: tutorial
description: "Este artigo o orientará sobre como configurar os recursos de logon único do Microsoft Entra com o Braze."

---

# Microsoft Entra SSO

> [O Microsoft Entra SSO](https://learn.microsoft.com/en-us/entra/identity/saas-apps/braze-tutorial) é o serviço de gerenciamento de identidade e acesso baseado em nuvem da Microsoft, que ajuda seus funcionários a fazer login e acessar recursos. Você pode usar o Entra SSO para controlar o acesso aos seus aplicativos e aos seus recursos de aplicativos, com base nos seus requisitos comerciais.

## Requisitos

Após a configuração, você será solicitado a fornecer um URL do Assertion Consumer Service (ACS).  

| Requisito | Detalhes |
|---|---|
| URL do serviço de consumidor de asserção (ACS) | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br> Para alguns provedores de identidade, isso também pode ser chamado de URL de resposta, URL de público-alvo ou URI de público-alvo. |
| ID da entidade | `braze_dashboard`|
| Chave da API do RelayState | Para ativar o login do provedor de identidade, vá para **Settings** > **API Keys (** **Configurações** > **Chaves de API** ) e crie uma chave de API com permissões `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Login iniciado pelo provedor de serviços (SP) no Microsoft Entra SSO

### Etapa 1: Adicionar Braze da galeria

1. No centro de administração do Microsoft Entra, vá para **Identidade** > **Aplicativos** > **Aplicativos empresariais** e selecione **Novo aplicativo**.
2. Pesquise **Braze** na caixa de pesquisa, selecione-o no painel de resultados e, em seguida, selecione **Add (Adicionar**).

### Etapa 2: Configurar o Microsoft Entra SSO

1. No centro de administração do Microsoft Entra, vá para a página de integração do aplicativo Braze e selecione **Single sign-on**.
2. Na página **Selecionar um método de logon único**, selecione **SAML** como seu método.
3. Na página **Set up Single Sign-On with SAML (Configurar logon único com SAML** ), selecione o ícone de edição para **Basic SAML Configuration (Configuração básica de SAML**).
4. Configure o aplicativo no modo iniciado por IdP inserindo um **URL de resposta** que combine sua [instância do Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) com o seguinte padrão: `https://<SUBDOMAIN>.braze.com/auth/saml/callback`.
5. Opcionalmente, configure o RelayState inserindo sua chave de API gerada pelo Relay State no campo **Relay State (Optional)**.

{% alert important %}
**Não** defina o campo **URL de logon**. Deixe esse campo em branco para evitar problemas com o SSO SAML iniciado pelo IdP.
{% endalert %}

{: start="6"}
6\. Formatar asserções SAML no formato específico esperado pelo Braze. Consulte as guias a seguir sobre atributos e declarações do usuário para entender como esses atributos e valores devem ser formatados.

{% tabs %}
{% tab User Attributes %}
É possível gerenciar os valores desses atributos na seção **User Attributes (Atributos do usuário** ) da página **Application Integration (Integração de aplicativos** ).

Use os seguintes pares de atributos:

- `givenname` = `user.givenname`
- `surname`= `user.surname`
- `emailaddress` = `user.mail`
- `name` = `user.userprincipalname`
- `email` = `user.userprincipalname`
- `first_name` = `user.givenname`
- `last_name` = `user.surname`
- `Unique User Identifier` = `user.userprincipalname`

{% alert important %}
É extremamente importante que o campo de e-mail corresponda ao que está configurado para seus usuários no Braze. Na maioria dos casos, será o mesmo que `user.userprincipalname`. No entanto, se você tiver uma configuração diferente, trabalhe com o administrador do sistema para garantir que esses campos correspondam exatamente.
{% endalert %}

{% endtab %}
{% tab User Claims %}

Na página **Configurar Single Sign-On com SAML**, selecione **Editar** para abrir a caixa de diálogo **Atributos do usuário**. Em seguida, edite as reivindicações do usuário de acordo com o formato adequado.

Use os seguintes pares de nomes de reivindicações:

- `claims/givenname` = `user.givenname`
- `claims/surname` = `user.surname`
- `claims/emailaddress` = `user.userprincipalname`
- `claims/name` = `user.userprincipalname`
- `claims/nameidentifier` = `user.userprincipalname`

{% alert important %}
É extremamente importante que o campo de e-mail corresponda ao que está configurado para seus usuários no Braze. Na maioria dos casos, será o mesmo que `user.userprincipalname`. No entanto, se você tiver uma configuração diferente, trabalhe com o administrador do sistema para garantir que esses campos correspondam exatamente.
{% endalert %}

Você pode gerenciar essas reivindicações e valores do usuário na seção **Gerenciar reivindicação**.

{% endtab %}
{% endtabs %}

{: start="8"}
8\. Vá para a página **Set up Single Sign-On with SAML (Configurar logon único com SAML** ), role até a seção **SAML Signing Certificate (Certificado de assinatura SAML** ) e faça download do **certificado** apropriado **(Base64)** com base em seus requisitos.
9\. Vá para a seção **Configurar o Braze** e copie os URLs apropriados para uso na [configuração do Braze](#step-3).

### Etapa 3: Configurar o SSO do Microsoft Entra no Braze {#step-3}

Depois que você configurar o Braze no centro de administração do Microsoft Entra, o Microsoft Entra fornecerá um URL de destino (URL de login) e um certificado **x.509** certificado que você inserirá em sua conta Braze.

Depois que seu gerente de conta ativar o SAML SSO para sua conta, faça o seguinte:

1. Vá para **Configurações** > Configurações **administrativas** > **Configurações de segurança** e alterne a seção SAML SSO para **ATIVADO**.
2. Na mesma página, adicione o seguinte:

| Requisito | Detalhes |
|---|---|
| `SAML Name` | Isso aparecerá como o texto do botão na tela de login. Normalmente, esse é o nome do seu provedor de identidade, como "Microsoft Entra". |
| `Target URL` | Esse é o URL de login fornecido pelo Microsoft Entra.|
| `Certificate` | O certificado codificado em `x.509` PEM é fornecido por seu provedor de identidade. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Se quiser que os usuários da sua conta Braze façam login apenas com SAML SSO, você poderá [restringir a autenticação de logon único]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) na página **Configurações da empresa**.
{% endalert %}
