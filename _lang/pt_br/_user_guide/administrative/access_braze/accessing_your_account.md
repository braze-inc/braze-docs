---
nav_title: Acesse sua conta
article_title: Acesse sua conta
page_order: 0
page_type: reference
description: "Este artigo aborda como obter sua conta Braze, como fazer o registro após a concessão de acesso e como redefinir sua senha Braze."

---

# Acesse sua conta

> Este artigo aborda como obter sua conta Braze, como fazer o registro após a concessão de acesso e como solucionar problemas de acesso ao painel e de performance do painel.

Se for o primeiro usuário Braze da sua empresa e estiver se registrando pela primeira vez, receberá um e-mail de boas-vindas de `@alerts.braze.com` solicitando que confirme seu e-mail e se registre no primeiro dia do seu contrato.

Depois de confirmar a sua conta, você pode adicionar outros usuários na página [Company Users (Usuários da empresa]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/) ) do seu dashboard. Todos os usuários receberão um e-mail solicitando a confirmação da conta depois de serem adicionados.

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

## Acesso a vários dashboards do Braze

O Braze não permite que você registre o mesmo endereço de e-mail para vários usuários de dashboards no mesmo cluster (por exemplo, se você tiver dois dashboards no US-01). É possível usar o mesmo e-mail para criar contas em clusters diferentes (por exemplo, se você tiver um dashboard na US-01 e outro na US-05). Se precisar acessar vários dashboards do Braze no mesmo cluster, você pode fazer o seguinte:

### Use aliases de e-mail

Se o seu provedor de e-mail for o Gmail, você poderá criar aliases adicionando um sinal `+` seguido de qualquer texto ao seu endereço de e-mail. Por exemplo:
- **Origin e-mail:** `rocky@gmail.com`
- **E-mail de apelido:** `rocky+1@gmail.com`

Ambos os endereços de e-mail direcionarão os e-mails para a mesma caixa de entrada, mas o Braze os reconhecerá como contas separadas quando você fizer o registro.

### Criar aliases separados com outros provedores

Se o seu provedor de e-mail não suportar o envio de e-mails para `+`, você ainda poderá criar aliases separados, como, por exemplo, configurar `rocky@braze.com` para encaminhar para `rocky.lotito@braze.com`. Isso permite que vários endereços sejam canalizados para a mesma caixa de entrada e, ao mesmo tempo, sejam reconhecidos como e-mails diferentes pelo Braze.

### Usar desenvolvedores de várias empresas

O recurso de desenvolvedores de várias empresas permite o compartilhamento de uma única conta de usuário entre várias empresas. Os usuários podem alternar entre diferentes dashboards da empresa no menu do perfil do usuário.

Se você tiver SSO e quiser configurar desenvolvedores de várias empresas, precisará ativar uma ID de entidade personalizada SAML configurando uma integração SSO SAML personalizada. Siga as etapas do [login iniciado pelo prestador de serviço (SP)]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/), mas aplique essas alterações:
- Altere **o ID da entidade** para `braze_dashboard_<companyID>` para cada integração do dashboard.
- Entre em contato com seu gerente de sucesso do cliente ou gerente de conta para ativar o flipper do recurso `saml_sso_custom_entity_id` para cada dashboard.

### Considerações sobre logon único (SSO)

Se você usa logon único (SSO), saiba que ter vários endereços de e-mail diferentes pode causar complicações. Confirme se suas configurações de SSO estão definidas corretamente para evitar problemas de acesso.

## Solução de problemas

### Redefinição de sua senha

Para redefinir sua senha, selecione o link **Esqueceu sua senha?** na página de login do dashboard. Será solicitado que você insira seu e-mail para receber um link para redefinir sua senha.

![Login no dashboard com prompt "Esqueceu sua senha?".]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### Limpar o cache e os cookies do navegador

Se você está tendo problemas com o desempenho do dashboard, como seu dashboard ou lista de desempenho de segmentos não carregando, tente limpar o cache e os cookies do seu navegador seguindo os passos para o seu respectivo navegador.

{% alert important %}
Limpar cookies fará com que você saia, portanto, trabalhos não salvos serão perdidos.
{% endalert %}

- [Limpar o cache & cookies no Chrome](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
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

### Acessando o aprendizado do Braze

Se estiver com problemas para registrar-se no Braze Learning e ficar preso em um loop que o redireciona para o dashboard, siga as etapas a seguir:

1. Se você tiver várias contas Braze, o registro com a conta errada duas vezes o enviará para o dashboard Braze. Confirme se está registrando a conta correta. 
2. Se você tiver um bloqueador de anúncios, confirme se ele está desativado. Ele pode bloquear os cookies necessários para a funcionalidade de logon único.
3. Acesse Configurações da empresa > Configurações de segurança e verifique se o logon único (SSO) está ativado.
4. Confirme se o perfil de usuário do dashboard inclui um nome e um sobrenome. O fato de não ter um sobrenome pode atrapalhar o processo de login.
5. Acesse o Braze Learning em seu dashboard, indo para **Suporte** > **Braze Learning**. 
6. Se continuar a ter problemas, considere a possibilidade de recriar sua conta. Os usuários que acessaram o Braze Learning durante a fase de teste gratuito podem ter dificuldades para acessá-lo agora.

### Problemas com a autenticação de dois fatores (2FA)

Se um usuário estiver enfrentando problemas com a autenticação de dois fatores (2FA) e não conseguir acessar o dashboard do Braze, isso pode ser devido a vários motivos. Mais comumente, eles podem não ter mais acesso ao número de telefone registrado ou ao dispositivo em que o app Authy está instalado.

Um administrador deve redefinir a 2FA para o usuário afetado fazendo o seguinte: 

1. Acesse **Gerenciar usuários**.
2. Selecione **Editar usuário** para o usuário que está tendo problemas com a 2FA.
3. Escolha a opção para redefinir a 2FA.
4. Confirme a redefinição da 2FA quando solicitado.
5. Se a redefinição não resolver o problema imediatamente, limpe os cookies e o cache.

O Braze não pode redefinir a 2FA em nome dos usuários por motivos de segurança, portanto, se o administrador não puder redefinir a 2FA, crie um ticket de suporte.

#### Considerações

- Se a 2FA for aplicada em nível de empresa: Após a redefinição, o Braze solicita que o usuário configure a 2FA novamente na próxima vez que fizer o registro.
- Se a 2FA não for aplicada em nível de empresa: O usuário fará o registro no dashboard sem precisar configurar a 2FA novamente. Se desejarem ativar a 2FA, poderão fazê-lo nas Configurações da conta.

{% alert note %}
Esse processo de redefinição também se aplica a usuários que foram bloqueados em suas contas devido à solicitação de muitos tokens na última hora.
{% endalert %}