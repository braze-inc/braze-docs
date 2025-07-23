---
nav_title: Microsoft Entra SSO
article_title: Microsoft Entra SSO
page_order: 3
page_type: tutorial
description: "Este artigo o orientará sobre como configurar os recursos de logon único do Microsoft Entra com o Braze."

---

# Microsoft Entra SSO

> O [Microsoft Entra SSO](https://learn.microsoft.com/en-us/entra/identity/saas-apps/braze-tutorial) é o serviço de gerenciamento de identidade e acesso baseado em nuvem da Microsoft, que ajuda seus colaboradores a fazer login e acessar recursos. Você pode usar o Entra SSO para controlar o acesso aos seus apps e aos recursos do seu app, com base nos seus requisitos de negócios.

## Solicitações

Após a configuração, solicitaremos que você forneça uma URL de login e um URL do Assertion Consumer Service (ACS).  

| Requisito | Informações |
|---|---|
| URL de login | `https://<SUBDOMAIN>.braze.com/sign_in` <br><br> Para o subdomínio, use o subdomínio de coordenação listado no [URL de]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) sua [instância do Braze]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/). Por exemplo, se sua instância for `US-01`, seu URL será `https://dashboard-01.braze.com`. Isso significa que seu subdomínio será `dashboard-01`. |
| URL do serviço de consumidor de asserção (ACS) | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br> Para alguns provedores de identidade, isso também pode ser chamado de URL de resposta, URL do público ou URI do público. |
| ID da entidade | `braze_dashboard`|
| Chave de API do RelayState | Para ativar o login do provedor de identidade, acesse **Settings** > **API Keys (** **Configurações** > **Chaves de API** ) e crie uma chave de API com permissões `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Login iniciado pelo prestador de serviço (SP) no Microsoft Entra SSO

### Etapa 1: Adicionar Braze da galeria

1. No centro de administração do Microsoft Entra, acesse **Identidade** > **Aplicativos** > **Aplicativos empresariais** e selecione **Novo aplicativo**.
2. Pesquise **Braze** na caixa de pesquisa, selecione-o no painel de resultados e, em seguida, selecione **Add (Adicionar)**.

### Etapa 2: Configurar o Microsoft Entra SSO

1. No centro de administração do Microsoft Entra, acesse a página de integração do aplicativo Braze e selecione **Logon único**.
2. Na página **Selecionar um método de logon único**, selecione **SAML** como seu método.
3. Na página **Configurar logon único com SAML**, selecione o ícone de edição para **Configuração básica de SAML**.
4. Configure o aplicativo no modo iniciado por IdP inserindo um **URL de resposta** que combine sua [instância da Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) com o seguinte padrão: `https://<SUBDOMAIN>.braze.com/auth/saml/callback`.
5. Opcionalmente, configure o RelayState inserindo sua chave de API gerada pelo Relay State no campo **Relay State (Optional)**.
6. Se quiser configurar o aplicativo no modo iniciado por SP, selecione **Definir URLs adicionais** e insira um URL de login que combine sua [instância da Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) com o seguinte padrão: `https://<SUBDOMAIN>.braze.com/sign_in`.
7. Formatar as asserções SAML no formato específico esperado pelo Braze. Consulte as guias a seguir sobre atribuições e reivindicações do usuário para entender como esses atributos e valores devem ser formatados.

{% tabs %}
{% tab Atribuições do usuário %}
É possível gerenciar os valores dessas atribuições na seção **Atributos do usuário** na página **Integração de aplicativos**.

Use os seguintes pares de atribuições:

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
{% tab Reivindicações do usuário %}

Na página **Configurar logon único com SAML**, selecione **Editar** para abrir a caixa de diálogo **Atribuições do usuário**. Em seguida, edite as reivindicações do usuário de acordo com o formato adequado.

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
8\. Acesse a página **Set up Single Sign-On with SAML (Configurar logon único com SAML** **)**, role até a seção **SAML Signing Certificate (Certificado de assinatura SAML** **)** e baixe o **certificado** apropriado **(Base64)** com base em seus requisitos.
9\. Acesse a seção **Configurar a Braze** e copie os URLs apropriados para uso na [configuração da Braze](#step-3).

### Etapa 3: Configurar o SSO do Microsoft Entra no Braze {#step-3}

Depois que você configurar o Braze no centro de administração do Microsoft Entra, o Microsoft Entra fornecerá um URL de direcionamento (URL de login) e um certificado **x.509** que você inserirá em sua conta do Braze.

Depois que seu gerente de conta ativar o SAML SSO para sua conta, faça o seguinte:

1. Acesse **Configurações** > **Configurações administrativas** > **Configurações de segurança** e alterne a seção SAML SSO para **ATIVADO**.
2. Na mesma página, adicione o seguinte:

| Requisito | Informações |
|---|---|
| `SAML Name` | Isso aparecerá como o texto do botão na tela de login. Normalmente, esse é o nome de seu provedor de identidade, como "Microsoft Entra". |
| `Target URL` | Esse é o URL de login fornecido pelo Microsoft Entra.|
| `Certificate` | O certificado codificado em `x.509` PEM é fornecido por seu provedor de identidade. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Se você deseja que os usuários da sua conta Braze façam login apenas com SAML SSO, você pode [restringir a autenticação de logon único]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) na página **Configurações da Empresa**.
{% endalert %}
