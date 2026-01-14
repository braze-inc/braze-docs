---
nav_title: Configuração do SSO SAML
article_title: Configuração do SSO SAML
page_order: 0
page_type: tutorial
description: "Este artigo irá guiá-lo sobre como habilitar o login único SAML para sua conta Braze."

---

# Login iniciado pelo Provedor de Serviço (SP)

> Este artigo irá guiá-lo sobre como habilitar o login único SAML para sua conta Braze e como obter um rastreamento SAML.

## Requisitos

Após a configuração, você será solicitado a fornecer uma URL de login e uma URL de Serviço de Consumidor de Aserção (ACS).  

| Requisito | Detalhes |
|---|---|
| URL do Serviço de Consumidor de Aserção (ACS) | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> Para domínios da União Europeia, a URL ASC é `https://<SUBDOMAIN>.braze.eu/auth/saml/callback`. <br><br> Para alguns IdPs, isso também pode ser referido como a URL de Resposta, URL de Login, URL de Público ou URI de Público. |
| ID da Entidade | `braze_dashboard` |
| Chave da API RelayState | Vá para **Configurações** > **Chaves de API** e crie uma chave de API com permissões `sso.saml.login`, e então insira a chave de API gerada como o parâmetro `RelayState` dentro do seu IdP. Para etapas detalhadas, consulte [Configurando seu RelayState](#setting-up-your-relaystate). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Configurando SSO SAML

### Passo 1: Configure seu provedor de identidade

Configure o Braze como um provedor de serviços (SP) em seu provedor de identidade (IdP) com as seguintes informações. Além disso, configure o mapeamento de atributos SAML.

{% alert important %}
Se você planeja usar o Okta como seu provedor de identidade, certifique-se de usar a integração pré-construída encontrada no [site do Okta](https://www.okta.com/integrations/braze/).
{% endalert %}

| Atributo SAML | Necessário? | Atributos SAML Aceitos |
|---|---|---|
|`email` | Necessário | `email` <br> `mail` <br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | Opcional | `first_name` <br> `firstname` <br> `firstName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | Opcional | `last_name` <br> `lastname` <br> `lastName` <br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |

{% alert note %}
O Braze só requer `email` na Aserção SAML.
{% endalert %}

### Passo 2: Configurar o Braze

Quando você terminar de configurar o Braze em seu provedor de identidade, seu provedor de identidade fornecerá uma URL de destino e `x.509` certificado para inserir em sua conta Braze.

Depois que seu gerente de conta ativar o SSO SAML para sua conta, vá para **Configurações** > **Configurações do Administrador** > **Configurações de Segurança** e altere a seção SSO SAML para **ATIVADO**.

Na mesma página, insira o seguinte:

| Requisito | Detalhes |
|---|---|
| Nome SAML | Isso aparecerá como o texto do botão na tela de login.<br>Isso é tipicamente o nome do seu provedor de identidade, como "Okta." |
| URL de Destino | Isso é fornecido após configurar o Braze dentro do seu IdP.<br> Alguns IdPs referenciam isso como a URL SSO ou o Endpoint SAML 2.0. |
| Certificado | O certificado `x.509` que é fornecido pelo seu provedor de identidade.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Certifique-se de que seu certificado `x.509` siga este formato ao adicioná-lo ao painel:

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

\![Configurações SAML SSO com o toggle selecionado.]({% image_buster /assets/img/samlsso.png %})

### Passo 3: Faça login no Braze

Salve suas configurações de segurança e saia. Em seguida, faça login novamente com seu provedor de identidade.

\![Tela de login do painel com SSO habilitado]({% image_buster /assets/img/sso1.png %}){: style="max-width:60%;"}

## Configurando seu RelayState

1. No Braze, vá para **Configurações** > **APIs e Identificadores**.
2. Na aba **Chaves de API**, selecione o botão **Criar chave de API**.
3. No campo **Nome da chave de API**, insira um nome para sua chave.
4. Expanda o dropdown **SSO** em **Permissões** e marque **sso.saml.login**.<br><br>\![A seção "Permissões" com sso.saml.login marcada.]({% image_buster /assets/img/relaystate_troubleshoot.png %}){: style="max-width:70%;"}<br><br>
5. Selecione **Criar chave de API**.
6. Na aba **Chaves de API**, copie o identificador ao lado da chave de API que você criou.
7. Cole a chave de API RelayState no RelayState do seu IdP (pode também aparecer como "Estado de Relay" ou "Estado de Relay Padrão" dependendo do seu IdP).

## Comportamento SSO

Membros que optarem por usar SSO não poderão mais usar sua senha como faziam antes. Usuários que continuarem a usar sua senha poderão fazê-lo, a menos que sejam restritos pelas seguintes configurações.

## Restrição

Você pode restringir os membros da sua organização a fazer login apenas com o Google SSO ou SAML SSO. Para ativar as restrições, vá para **Configurações de Segurança** e selecione **Impor login apenas com Google SSO** ou **Impor login apenas com SAML SSO personalizado**.

\![Exemplo de configuração da seção "Regras de Autenticação" com um comprimento mínimo de senha de 8 caracteres e reutilização de senha de 3 vezes. As senhas expirarão após 180 dias, e os usuários serão desconectados após 1.440 minutos de inatividade.]({% image_buster /assets/img/sso3.png %})

Ao ativar as restrições, os usuários da Braze da sua empresa não poderão mais fazer login usando uma senha, mesmo que tenham feito login com uma senha antes.

## Obtendo um rastreamento SAML

Se você tiver problemas de login relacionados ao SSO, obter um rastreamento SAML pode ajudá-lo a solucionar sua conexão SSO, identificando o que é enviado nas solicitações SAML.

### Pré-requisitos

Para executar um rastreamento SAML, você precisará de um rastreador SAML. Aqui estão duas opções possíveis com base no seu navegador:

- [Google Chrome](https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch)
- [Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/saml-tracer/)

### Passo 1: Abra o rastreador SAML

Selecione o rastreador SAML na barra de navegação do seu navegador. Certifique-se de que **Pausar** não esteja selecionado, pois isso impedirá que o rastreador SAML capture o que é enviado nas solicitações SAML. Quando o rastreador SAML estiver aberto, você verá que ele preenche o rastreamento.

\![Rastreador SAML para Google Chrome.]({% image_buster /assets/img/saml_tracer_example.png %})

### Passo 2: Faça login no Braze usando SSO

Vá para o seu painel do Braze e tente fazer login usando SSO. Se você encontrar um erro, abra o rastreador SAML e tente novamente. Um rastreamento SAML foi coletado com sucesso se houver uma linha com uma URL como `https://dashboard-XX.braze.com/auth/saml/callback` e uma tag SAML laranja.

### Passo 3: Exporte e envie para o Braze

Selecione **Exportar**. Para **Selecionar perfil de filtro de cookie**, selecione **Nenhum**. Em seguida, selecione **Exportar**. Isso gerará um arquivo JSON que você pode enviar para o Suporte do Braze para mais solução de problemas.

\!["Menu de preferências de exportação de rastreamento SAML" com a opção "Nenhum" selecionada.]({% image_buster /assets/img/export_saml_trace_preferences.png %})

## Solução de problemas

### O endereço de e-mail do usuário está configurado corretamente?

Se você está recebendo o erro `ERROR_CODE_SSO_INVALID_EMAIL`, o endereço de e-mail do usuário não é válido. Confirme no rastreamento SAML que o campo `saml2:Attribute Name="email"` corresponde ao endereço de e-mail que o usuário está usando para fazer login. Se você usa o Microsoft Entra ID (anteriormente Azure Active Directory), o mapeamento de atributos é `email = user.userprincipalname`.

O endereço de e-mail é sensível a maiúsculas e minúsculas e deve corresponder exatamente ao que foi configurado no Braze, incluindo o que foi configurado no seu provedor de identidade (como Okta, OneLogin, Microsoft Entra ID e outros).

Outros erros que indicam que você tem problemas com o endereço de e-mail do usuário incluem:
- `ERROR_CODE_SSO_EMAIL_DOES_NOT_EXIST`: O endereço de e-mail do usuário não está dentro do painel.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISSING`: O endereço de e-mail do usuário está em branco ou de outra forma mal configurado.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISMATCH` ou `ERROR_CODE_SSO_SIGN_IN_EMAIL_MISMATCH` : O endereço de e-mail do usuário não corresponde ao usado para configurar o SSO.

### Você tem um certificado SAML válido (x.509 certificado)?

Você pode validar seu certificado SAML usando [esta ferramenta de validação SAML](https://www.samltool.com/validate_response.php). Observe que um certificado SAML expirado também é um certificado SAML inválido.

### Você enviou um certificado SAML correto (x.509 certificado)?

Confirme que o certificado na seção `ds:X509Certificate` do rastreamento SAML corresponde ao que você enviou para o Braze. Isso não inclui o cabeçalho `-----BEGIN CERTIFICATE-----` e o rodapé `-----END CERTIFICATE-----`.

### Você digitou ou formatou incorretamente seu certificado SAML (x.509 certificado)?

Confirme que não há espaços em branco ou caracteres extras no certificado que você enviou no painel do Braze.

Quando você insere seu certificado no Braze, ele precisa estar codificado em Privacy Enhanced Mail (PEM) e formatado corretamente (incluindo o cabeçalho `-----BEGIN CERTIFICATE-----` e o rodapé `-----END CERTIFICATE-----`). 

Aqui está um exemplo de certificado que está formatado corretamente:

```
-----BEGIN CERTIFICATE-----
THIS_IS_A_MOCKED_CERTIFICATE_4ysJLTzETANBgkqhkiG9w0BAQsFADA0MTIwMAYDVQQDEylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZpY2F0ZTAeFw0yMjA1MjcwOTA4MzFaFw0yNTAbMjcwOTA4MzFaMDQxMjAwBgNVBAMTKU1pY3Jvca9mdCBBenVyZSBGZWRlcmF0ZWQgU1NPIENlcnAFWAOKGPAWIGKJPOAMWANBgkqhkiG9w0BAQEFAAaCAQ8AMIIBCgKCAQEA1+KFJwxoac6jdFztQd+vQu59qM8rgfX5RICk0ODfpXkuDUNudcI0XmOAkKHRoMNPYlmMEf5NSiZ7TMElEPtK9zZlpAoSchxxC0Ndegc1AMFi7i2BsEIqPwrer0G6kx2vuAjdrDROPPafkmwalkfmklaw23FlYmV7doE0Vrj2WxR1PG0eFAdsxPLsO1ny55fPj2ibwaqc0XpDkfTrO9GnFvmZAS8ebYtLZsYAMAGLKWAMLGKAWMLKMFDW6vBDaK290s9FdaWza3GPHTcDstawRhyqbXpVjiqpQ0mtxANW4WduSiohhpeqv05TlSOhx87QalkfmwalfmAWMFLKQEBCwUAA4IBAQBdZ5E9FqICfL1q+G6D1tChKl1Y6I6IVULQb4LESSJRaxv53nakmflwakmMALKFMWOYKAeUWO2hdED54qGMgUnLL6YheQBrsm6ilBC68F7ZFmIzVKycvw65yamWbTMi2f2lF60GNYMrq8sGQUkgO0O2zTN07J9wGTe9M+MAFLKWAMFLKalkmflkawoij4jpcsLXXFZJoHSXnF3+qQuzu+49D6pR2lF7DDW+5+PRoc1QpDSytdXxWzItsjQ6IFRuvIGsbrMg0FVaze7ePdKrc47wSlElno7SQ0H+6g40q25rsDSLO
-----END CERTIFICATE-----
```

### O token de sessão do usuário é válido?

Peça ao usuário afetado [limpar o cache e os cookies do navegador](https://its.uiowa.edu/services/how-clear-cache-and-cookies-your-web-browser), e então tente fazer login com SAML SSO novamente.

### Você definiu seu RelayState?

Se você está recebendo o erro `ERROR_CODE_SSO_INVALID_RELAY_STATE`, seu RelayState pode estar mal configurado ou inexistente. Se você ainda não fez isso, precisa definir seu RelayState no seu sistema de gerenciamento de IdP. Para etapas, consulte [Configurando seu RelayState](#setting-up-your-relaystate). 

### O usuário está preso em um loop de login entre Okta e Braze?

Se um usuário não consegue fazer login porque está preso ciclando entre o SSO do Okta e o painel do Braze, você precisa ir ao Okta e definir o destino da URL do SSO para sua [instância do Braze]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) (por exemplo, `https://dashboard-07.braze.com`). 

Se você estiver usando outro IdP, verifique se sua empresa enviou o SAML ou o x.509 certificado correto para o Braze.

### Você está usando uma integração manual?

Se sua empresa não baixou o aplicativo Braze da loja de aplicativos do seu IdP, você precisa baixar a integração pré-construída. Por exemplo, se o Okta é seu IdP, você deve baixar o aplicativo Braze da [página de integração](https://www.okta.com/integrations/braze/) deles.
