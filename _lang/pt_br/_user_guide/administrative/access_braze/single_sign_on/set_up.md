---
nav_title: Configuração do SAML SSO
article_title: Configuração do SAML SSO
page_order: 0
page_type: tutorial
description: "Este artigo orientará você sobre como ativar o logon único SAML para sua conta Braze."

---

# Login iniciado pelo prestador de serviço (SP)

> Este artigo orientará você sobre como ativar o logon único SAML para sua conta Braze.

## Solicitações

Após a configuração, solicitaremos que você forneça uma URL de login e um URL do Assertion Consumer Service (ACS).  

| Requisito | Informações |
|---|---|
| URL do serviço de consumidor de asserção (ACS) | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> Para domínios da União Europeia, o URL do ASC é `https://<SUBDOMAIN>.braze.eu/auth/saml/callback`. <br><br> Para alguns IdPs, isso também pode ser chamado de URL de resposta, URL de login, URL do público ou URI do público. |
| ID da entidade | `braze_dashboard` |
| Chave de API do RelayState | Acesse **Configurações** > **Chaves de API** ) e crie uma chave de API com permissões `sso.saml.login` e, em seguida, insira a chave de API gerada como o parâmetro `RelayState` em seu IdP. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Se você estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), você pode encontrar suas chaves API em **Configurações** na **console de desenvolvedor** > **Configurações de API**.
{% endalert %}

## Configuração do SAML SSO

### Etapa 1: Configure seu provedor de identidade

Configure o Braze como um prestador de serviço (SP) em seu provedor de identidade (IdP) com as seguintes informações. Além disso, configure o mapeamento de atribuições SAML.

{% alert important %}
Se planeja usar o Okta como provedor de identidade, use a integração pré-construída encontrada no [site do Okta](https://www.okta.com/integrations/braze/).
{% endalert %}

| Atributo SAML | Necessário? | Atribuições SAML aceitas |
|---|---|---|
|`email` | Obrigatória | `email` <br> `mail` <br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | Opcional | `first_name` <br> `firstname` <br> `firstName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | Opcional | `last_name` <br> `lastname` <br> `lastName` <br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |

{% alert note %}
A Braze requer apenas o endereço `email` na declaração SAML.
{% endalert %}

### Etapa 2: Configurar o Braze

Quando terminar de configurar a Braze em seu provedor de identidade, ele fornecerá um URL de direcionamento e um certificado `x.509` para inserir em sua conta Braze.

Depois que o gerente da conta ativar o SAML SSO para a sua conta, acesse **Configurações** > **Configurações administrativas** > **Configurações de segurança** e alterne a seção SAML SSO para **ATIVADO**.

{% alert note %}
Se você estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), selecione o ícone da sua conta e acesse **Configurações da Empresa** > **Configurações de Segurança** para encontrar a seção SAML SSO.
{% endalert %}

Na mesma página, insira o seguinte:

| Requisito | Informações |
|---|---|
| `SAML Name` | Isso aparecerá como o texto do botão na tela de login.<br>Normalmente, esse é o nome de seu provedor de identidade, como "Okta". |
| `Target URL` | Isso acontecerá após a configuração da Braze em seu IdP.<br> Alguns IdPs fazem referência a isso como URL de SSO ou endpoint SAML 2.0. |
| `Certificate` | O certificado `x.509` que é fornecido por seu provedor de identidade.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Confira se o seu certificado `x.509` segue esse formato ao adicioná-lo ao dashboard:

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![Abertura das configurações de segurança e adição de detalhes de SSO SAML]({% image_buster /assets/img/samlsso.gif %})

### Etapa 3: Faça login no Braze

Salve suas configurações de segurança e faça o registro. Em seguida, faça login novamente com seu provedor de identidade.

![Tela de login do dashboard com SSO ativado]({% image_buster /assets/img/sso1.png %}){: style="max-width:40%;"}

## Comportamento de SSO

Os membros que aceitarem usar o SSO não poderão mais usar sua senha como faziam antes. Os usuários que continuarem a usar sua senha poderão, a menos que sejam restringidos pelas seguintes configurações.

## Restrição

Você pode restringir os membros de sua organização para que façam login apenas com o Google SSO ou o SAML SSO. Para ativar as restrições, acesse **Security Settings** e selecione **Enforce Google SSO only login** ou **Enforce custom SAML SSO only login**.

![Seção Authentication Rules (Regras de autenticação) da página Security Settings (Configurações de segurança)]({% image_buster /assets/img/sso3.png %})

Ao ativar as restrições, os usuários do Braze da sua empresa não poderão mais se registrar usando uma senha, mesmo que já tenham se registrado com uma senha anteriormente.
