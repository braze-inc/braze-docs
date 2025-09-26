---
nav_title: Acesso à sua conta
article_title: Acesso à sua conta
page_order: 2
page_type: reference
description: "Este artigo aborda como obter sua conta Braze, como fazer o registro após a concessão de acesso e como redefinir sua senha Braze."

---

# Acesso à sua conta

> Este artigo aborda como obter sua conta Braze, como fazer o registro após a concessão de acesso e como solucionar problemas de acesso ao painel e de performance do painel.

Se for o primeiro usuário Braze da sua empresa e estiver se registrando pela primeira vez, receberá um e-mail de boas-vindas de `@alerts.braze.com` solicitando que confirme seu e-mail e se registre no primeiro dia do seu contrato.

Depois de confirmar a sua conta, você pode adicionar outros usuários na página [Company Users (Usuários da empresa]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/) ) do seu dashboard. Todos os usuários receberão um e-mail solicitando a confirmação da conta depois de serem adicionados.

Se você não for o primeiro usuário da conta Braze da sua empresa, entre em contato com o administrador da conta Braze da sua empresa e peça que ele crie a sua conta. Em seguida, você receberá um e-mail de boas-vindas do `@alerts.braze.com` solicitando a confirmação do seu e-mail e o registro.

## Login

Vamos falar sobre como fazer o registro, seja pela primeira vez ou pela milionésima! Se você for o primeiro usuário da sua empresa, siga as orientações da seção anterior. Caso contrário, você poderá registrar-se depois que o administrador do Braze de sua empresa criar sua conta.

Você pode fazer o registro a partir do [Braze.com](https://www.braze.com) ou simplesmente usar o URL do dashboard que corresponde à sua [instância específica da Braze]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/). Para sua conveniência, o Braze tem várias opções de logon único (SSO), como:

* [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/)
    * [Provisionamento SAML just-in-time]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit/)
* [Microsoft Entra SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/)
* [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)
* [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)

{% alert note %}
Depois de entrar no Braze com SSO, você não poderá mais usar sua senha para se registrar no dashboard.
{% endalert %}

## Navegadores compatíveis

O dashboard da Braze é compatível com os seguintes navegadores:
- Chrome (versão 87 ou mais recente)
- Firefox (versão 85 ou mais recente)
- Safari (versão 15.4 ou mais recente)
- Edge (versão 87 ou mais recente)

Se o seu dashboard Braze disser que você tem um erro inesperado e sua ferramenta de console do navegador mostrar o erro `ReferenceError: structuredClone is not defined`, seu navegador está desatualizado. Se esse erro continuar ocorrendo, desinstale e reinstale seu navegador.

## Solução de problemas

### Redefinição de sua senha

Para redefinir sua senha, selecione o link **Esqueceu sua senha?** na página de login do dashboard. Será solicitado que você insira seu e-mail para receber um link para redefinir sua senha.

![Login no dashboard com prompt "Esqueceu sua senha?".]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### Limpar o cache e os cookies do navegador

Se você está tendo problemas com o desempenho do dashboard, como seu dashboard ou lista de desempenho de segmentos não carregando, tente limpar o cache e os cookies do seu navegador seguindo os passos para o seu respectivo navegador.

{% alert important %}
Limpar cookies fará com que você saia, portanto, trabalhos não salvos serão perdidos.
{% endalert %}

- [Limpar cache e cookies no Chrome](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Limpar cookies no Safari no Mac](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Limpar cookies e dados do site no Firefox](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Excluir todos os cookies no Microsoft Edge](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

Se limpar o cache e os cookies do seu navegador não resolver seus problemas, entre em contato com o [Suporte]({{site.baseurl}}/support_contact/).

### Acessando o editor de arrastar e soltar

Para a maioria dos usuários do Braze, o editor de arrastar e soltar deve ser carregado. No entanto, se você estiver usando uma VPN ou estiver atrás de um firewall, talvez seja necessário colocar um domínio na lista de permissões. Entre em contato com o administrador de TI para verificar se o site `*.bz-rndr.com` está na lista de permissões.

O editor pode apresentar problemas de carregamento devido ao seguinte:

- **Erro transitório:** São falhas temporárias que podem afetar a conectividade, a comunicação ou a transferência de dados. Felizmente, elas geralmente se resolvem sozinhas, sem necessidade de intervenção significativa, pois geralmente são causadas por condições de curta duração e não indicam problemas sistêmicos.
- **Erro grave:** Isso pode envolver um problema subjacente de infraestrutura ou de produto.  Você pode verificar nossa [página de status do sistema Braze](https://braze.statuspage.io/), pois provavelmente estamos cientes da situação e trabalhando ativamente para resolvê-la.

{% alert important %}
Se ainda estiver com problemas, [abra um tíquete de suporte]({{site.baseurl}}/user_guide/administrative/access_braze/support/). Antes de fazer isso, verifique se o administrador de TI confirmou que o site `*.bz-rndr.com` está na lista de permissões em seu local.
{% endalert %}

