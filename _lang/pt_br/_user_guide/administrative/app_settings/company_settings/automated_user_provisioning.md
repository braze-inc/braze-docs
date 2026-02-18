---
nav_title: Provisionamento automatizado de usuários
article_title: Provisionamento automatizado de usuários
page_order: 10
page_type: reference
description: "Este artigo de referência aborda as informações que precisam ser fornecidas para o provisionamento automatizado de usuários e como e onde usar o token gerado pelo System for Cross-domain Identity Management (SCIM)."
alias: /scim/automated_user_provisioning/

---

# Provisionamento automatizado de usuários

> Use o provisionamento SCIM para criar e gerenciar automaticamente usuários do Braze através da API. Este artigo orienta você sobre quais informações fornecer, como gerar seu token SCIM e onde encontrar seu endpoint da API SCIM.

{% include early_access_beta_alert.md feature='SCIM provisioning' %}

## Acessando as configurações de provisionamento SCIM

1. No painel do Braze, acesse **Configurações** > **Configurações do Administrador** > **Provisionamento SCIM**, e então selecione **Configurar integração SCIM**.
2. Na etapa de **configuração do Braze**, selecione um método de provisionamento e forneça as configurações de acesso.

![Uma página para configurar a integração SCIM com seções para selecionar um método de provisionamento e fornecer configurações de acesso.]({% image_buster /assets/img_archive/scim_braze_config.png %}){: style="max-width:70%;"}

{: start="3"}
3\. Na etapa de **configuração do IdP**, siga os passos dentro da plataforma para o método de provisionamento selecionado.

{% tabs %}
{% tab Okta - Braze app %}

{% include early_access_beta_alert.md feature='The Okta integration' %}

Use a opção **Okta - aplicativo Braze** se você configurou o aplicativo Braze para SSO SAML no Okta. Se você configurou um aplicativo personalizado para SSO, siga as instruções na aba [Integração de aplicativo personalizado Okta]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/automated_user_provisioning/?tab=okta%20-%20custom%20app%20integration#step-1-set-up-scim-provisioning).

## Etapa 1: Configure o provisionamento SCIM

### Etapa 1.1: Ativar SCIM

1. No Okta, acesse **Aplicações** > **Aplicações**, então selecione **Criar Integração de Aplicativo**. Selecione **SAML 2.0** como o método de login.
2. Preencha os seguintes detalhes (que estão localizados na etapa [**configuração do IdP** do Braze](#accessing-scim-provisioning-settings)) para criar um aplicativo personalizado:
- Logotipo do app
- URL de logon único
- URL do público (ID da entidade SP)
3. Selecione **Finish (Acabamento**).
4. Selecione a aba **Geral**. 
5. Na seção **Configurações do Aplicativo**, selecione **Editar**.
6. No campo **Provisionamento**, selecione **SCIM**. 

### Etapa 1.2: Desativar a visibilidade do aplicativo

1. No campo **Visibilidade do Aplicativo**, selecione a caixa de seleção **Não exibir ícone do aplicativo para o usuário**. Isso impede que os usuários acessem o SSO através do aplicativo, que é destinado exclusivamente ao SCIM. 
2. Selecione **Salvar**.

### Etapa 1.3: Configure a integração SCIM

1. Selecione a guia **Provisionamento**.
2. Em **Configurações** > **Integração** > **Conexão SCIM**, selecione **Editar** e preencha os valores dos campos que aparecem na tabela na página **Configuração do provisionamento SCIM**.

### Etapa 1.4: Teste as credenciais da API

Selecione **Testar Credenciais da API**. Uma mensagem de verificação aparece se a integração for bem-sucedida e você pode salvar.

### Etapa 1.5: Ative o provisionamento para o app

1. Em **Provisionamento** > **Configurações** > **Para o App** > **Provisionamento para o App**, selecione **Editar**.
2. Ative o seguinte:
    - Criar usuários
    - Atualizar atribuições de usuários
    - Desativar usuários
3. Revise e configure a seção **Mapeamento de Atributos** com os mapeamentos que aparecem na tabela na página **Configuração do provisionamento SCIM**.

## Etapa 2: Atribua usuários ao app

1. Selecione a guia **Atribuição**.
2. Selecione **Atribuir** e escolha uma opção.
3. Atribua o app às pessoas que devem ter acesso ao Braze.
4. Selecione **Concluído** quando você tiver completado a atribuição.

{% endtab %}
{% tab Okta - Custom app integration %}

{% include early_access_beta_alert.md feature='The Okta integration' %}

Use a opção **Okta - Integração de app personalizado** se você configurou um app personalizado para SSO. Se você configurou o app Braze para SAML SSO no Okta, siga as instruções na guia [Okta - app Braze]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/automated_user_provisioning/?tab=okta%20-%20braze%20app#step-1-set-up-scim-provisioning).

## Etapa 1: Configure o provisionamento SCIM

### Etapa 1.1: Ativar SCIM

1. No Okta, acesse seu app Braze.
2. Selecione a aba **Geral**.
3. Na seção **Configurações do Aplicativo**, selecione **Editar**.
4. No campo **Provisionamento**, selecione **SCIM**.
5. Selecione **Salvar**.

### Etapa 1.2: Configure a integração SCIM

1. Selecione a guia **Provisionamento**.
2. Em **Configurações** > **Integração** > **Conexão SCIM**, selecione **Editar** e preencha os valores dos campos que aparecem na tabela na página **Configuração do provisionamento SCIM**.
3. Teste as credenciais da API selecionando **Testar Credenciais da API**.
4. Selecione **Salvar**.

### Etapa 1.3: Ative o provisionamento para o app

1. Em **Provisionamento** > **Configurações** > **Para o App** > **Provisionamento para o App**, selecione **Editar**.
2. Ative o seguinte:
    - Criar usuários
    - Atualizar atribuições de usuários
    - Desativar usuários
3. Revise e configure a seção **Mapeamento de Atributos** com os mapeamentos que aparecem na tabela na página **Configuração do provisionamento SCIM**.

## Etapa 2: Atribua usuários ao app

1. Selecione a guia **Atribuição**.
2. Selecione **Atribuir** e escolha uma opção.
3. Atribua o app às pessoas que devem ter acesso ao Braze.
4. Selecione **Concluído**.

{% endtab %}
{% tab Entra ID %}

{% include early_access_beta_alert.md feature='The Entra ID integration' %}

## Etapa 1: Configure o app de provisionamento SCIM

### Etapa 1.1: Faça login no centro de administração do Microsoft Entra

Faça login no seu centro de administração do Microsoft Entra.

### Etapa 1.2: Crie e configure seu aplicativo SCIM

1. No menu de navegação, acesse **Entra ID** > **Aplicativos corporativos**.
2. Selecione **Novo aplicativo**.
3. Selecione **Crie seu próprio aplicativo**.
4. No painel, insira um nome para seu app.
5. Na seção **O que você está procurando fazer com seu aplicativo?**, selecione **Integrar aplicativo que você não encontra na galeria (Não-galeria)**.
6. Selecione **Criar**.

### Etapa 1.3: Configure a integração SCIM

1. Acesse a seção **Gerenciar** > **Provisionamento** do seu aplicativo SCIM.
2. Selecione **Conectar seu aplicativo** ou **Nova configuração** e preencha os valores dos campos que aparecem na tabela na página **Configurar provisionamento SCIM**.

### Etapa 1.4: Ative o provisionamento para o app

1. Acesse a seção **Gerenciar** > **Mapeamento de atributos (Prévia)** do seu aplicativo SCIM.
2. Selecione **Provisionar usuários do Microsoft Entra ID**.
3. Revise e configure a seção **Mapeamento de Atributos** para corresponder aos atributos que aparecem na tabela na página **Configurar provisionamento SCIM**.
4. Feche a página **Mapeamento de Atributos**.

## Etapa 2: Atribua usuários ao app

1. Acesse **Gerenciar** > **Usuários e Grupos**.
2. Selecione **Adicionar usuário/grupo**.
3. Selecione **Nenhum Selecionado** para atribuir usuários ao app.
4. Selecione o botão **Selecionar** para confirmar a atribuição.

{% endtab %}
{% tab Custom %}

## Etapa 1: Configure suas configurações SCIM

- **Espaço de Trabalho Padrão:** Selecione o espaço de trabalho onde novos usuários devem ser adicionados por padrão. Se você não especificar um espaço de trabalho na sua [solicitação da API SCIM]({{site.baseurl}}/post_create_user_account/), a Braze atribui usuários a este espaço de trabalho.
- **Origem do Serviço:** Insira o domínio de origem das suas solicitações SCIM. A Braze usa isso no cabeçalho `X-Request-Origin` para verificar de onde as solicitações estão vindo.
- **Lista de Permissão de IP (opcional):** Você pode restringir solicitações SCIM a endereços IP específicos. Insira uma lista de endereços IP separados por vírgula ou um intervalo de endereços IP para permitir. O cabeçalho `X-Request-Origin` em cada solicitação é usado para verificar o endereço IP da solicitação em relação à lista de permissão.

![Formulário de configurações de Provisionamento SCIM com três campos: Espaço de Trabalho Padrão, Origem do Serviço e lista de permissão de IP opcional. O botão “Gerar Token SCIM” está desativado.]({% image_buster /assets/img/scim_unfilled.png %})

## Etapa 2: Gerar um token SCIM

Após preencher os campos obrigatórios, pressione **Gerar token SCIM** para gerar um token SCIM e ver seu endpoint da API SCIM. Certifique-se de copiar o token SCIM antes de navegar para longe. **Este token aparece apenas uma vez.** 

![Campos de Endpoint da API SCIM e Token SCIM exibidos com valores mascarados e botões de copiar. Abaixo do campo do token está um botão “Redefinir Token”.]({% image_buster /assets/img/scim.png %})

A Braze espera que todas as solicitações SCIM contenham o token de portador da API SCIM anexado por meio de um cabeçalho HTTP `Authorization`.

{% endtab %}
{% endtabs %}
