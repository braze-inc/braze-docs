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

## Acessando as configurações de provisionamento SCIM

1. No painel do Braze, acesse **Configurações** > **Configurações do Admin** > **Provisionamento SCIM** e adicione um provedor de identidade.
2. Na etapa **Provisionamento do Braze**, selecione um método de provisionamento e forneça as configurações de acesso.

![Uma página para configurar a integração SCIM com seções para selecionar um método de provisionamento e fornecer configurações de acesso.]({% image_buster /assets/img_archive/scim_braze_config.png %}){: style="max-width:70%;"}

{: start="3"}
3\. Na etapa **Configuração do IdP**, siga os passos dentro da plataforma para o método de provisionamento selecionado.

{% tabs %}
{% tab Okta - Braze app %}

{% alert important %}
A integração com o Okta está atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

## Etapa 1: Configure o provisionamento SCIM

### Etapa 1.1: Ativar SCIM

1. Acesse seu aplicativo Braze no Okta.
2. Selecione a guia **Geral**.
3. Na seção **Configurações do App**, selecione **Editar**.
4. No campo **Provisionamento**, selecione **SCIM**, e então selecione **Salvar**.

### Etapa 1.2: Configure a integração SCIM

1. Selecione a guia **Provisionamento**.
2. Em **Configurações** > **Integração** > **Conexão SCIM** selecione **Editar** e preencha os valores dos campos que aparecem na tabela na página **Configurar provisionamento SCIM**.

### Etapa 1.3: Teste as credenciais da API

Selecione **Testar Credenciais da API**. Uma mensagem de verificação aparece se a integração for bem-sucedida e você pode salvar.

### Etapa 1.4: Ativar a capacitação para o app

1. Em **Provisionamento** > **Configurações** > **Para o App** > **Provisionamento para o App**, selecione **Editar**.
2. Ative o seguinte:
    - Criar usuários
    - Atualizar atribuições de usuários
    - Desativar usuários
3. Revise e configure a seção **Mapeamento de Atributos** com os mapeamentos que aparecem na tabela na página **Configurar provisionamento SCIM**.

## Etapa 2: Atribua usuários ao app

1. Selecione a guia **Assignment**.
2. Selecione **Assign** e escolha uma opção.
3. Atribua o app às pessoas que devem ter acesso à Braze.
4. Selecione **Done** quando você tiver concluído a atribuição.

{% endtab %}
{% tab Okta - Custom app integration %}

{% alert important %}
A integração com o Okta está atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

## Etapa 1: Configure o provisionamento SCIM

### Etapa 1.1: Ativar SCIM

1. No Okta, acesse seu app Braze.
2. Selecione a guia **Geral**.
3. Na seção **Configurações do App**, selecione **Editar**.
4. No campo **Provisioning**, selecione **SCIM**.
5. Selecione **Salvar**.

### Etapa 1.2: Configure a integração SCIM

1. Selecione a guia **Provisionamento**.
2. Em **Settings** > **Integration** > **SCIM Connection**, selecione **Edit** e preencha os valores dos campos que aparecem na tabela na página **Setup SCIM provisioning**.
3. Teste as credenciais da API selecionando **Test API Credentials**.
4. Selecione **Salvar**.

### Etapa 1.3: Ativar a capacitação para o app

1. Em **Provisionamento** > **Configurações** > **Para o App** > **Provisionamento para o App**, selecione **Editar**.
2. Ative o seguinte:
    - Criar usuários
    - Atualizar atribuições de usuários
    - Desativar usuários
3. Revise e configure a seção **Mapeamento de Atributos** com os mapeamentos que aparecem na tabela na página **Configurar provisionamento SCIM**.

## Etapa 2: Atribua usuários ao app

1. Selecione a guia **Assignment**.
2. Selecione **Assign** e escolha uma opção.
3. Atribua o app às pessoas que devem ter acesso ao Braze.
4. Selecione **Concluído**.

{% endtab %}
{% tab Entra ID %}

{% alert important %}
A integração do Entra ID está atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

## Etapa 1: Configure o app de provisionamento SCIM

### Etapa 1.1. Faça login no centro de administração do Microsoft Entra
Faça login no seu centro de administração do Microsoft Entra.

### Etapa 1.2: Crie e configure seu app SCIM

1. No menu de navegação, acesse **Entra ID** > **Enterprise apps**.
2. Selecione **New application**.
3. Selecione **Create your own application**.
4. No painel, insira um nome para seu app.
5. Na seção **What are you looking to do with your application?**, selecione **Integrate application you don't find in the gallery (Non-gallery)**.
6. Selecione **Criar**.

### Etapa 1.3: Configure a integração SCIM

1. Acesse a seção **Gerenciar** > **Provisionamento** do seu aplicativo SCIM.
2. Selecione **Conectar seu aplicativo** ou **Nova configuração** e preencha os valores dos campos que aparecem na tabela na página **Configuração do provisionamento SCIM**.

### Etapa 1.4: Ativar a capacitação para o app

1. Acesse a seção **Gerenciar** > **Mapeamento de atributos (Prévia)** do seu aplicativo SCIM.
2. Selecione **Provisionar usuários do Microsoft Entra ID**.
3. Revise e configure a seção **Mapeamento de Atributos** para corresponder aos atributos que aparecem na tabela na página **Configuração do provisionamento SCIM**.
4. Feche a página **Mapeamento de Atributos**.

## Etapa 2: Atribua usuários ao app

1. Acesse **Gerenciar** > **Usuários e Grupos**.
2. Selecione **Adicionar usuário/grupo**.
3. Selecione **Nenhum Selecionado** para atribuir usuários ao app.
4. Selecione o botão **Selecionar** para confirmar a atribuição.

{% endtab %}
{% tab Custom %}

## Etapa 1: Configure suas configurações SCIM

- **Espaço de Trabalho Padrão:** Selecione o espaço de trabalho onde novos usuários devem ser adicionados por padrão. Se você não especificar um espaço de trabalho em sua [solicitação de API SCIM]({{site.baseurl}}/post_create_user_account/), a Braze atribui usuários a este espaço de trabalho.
- **Origem do Serviço:** Insira o domínio de origem de suas solicitações SCIM. A Braze usa isso no cabeçalho `X-Request-Origin` para verificar de onde as solicitações estão vindo.
- **Lista de Permissão de IP (opcional):** Você pode restringir solicitações SCIM a endereços IP específicos. Insira uma lista ou intervalo de endereços IP separados por vírgula para permitir. O cabeçalho `X-Request-Origin` em cada solicitação é usado para verificar o endereço IP da solicitação em relação à lista de permissões.

![Formulário de configurações de Provisionamento SCIM com três campos: Espaço de Trabalho Padrão, Origem do Serviço e lista de permissões de IP opcional. O botão “Gerar Token SCIM” está desativado.]({% image_buster /assets/img/scim_unfilled.png %})

## Etapa 2: Gerar um token SCIM

Após preencher os campos obrigatórios, pressione **Gerar token SCIM** para gerar um token SCIM e ver seu endpoint da API SCIM. Certifique-se de copiar o token SCIM antes de navegar para longe. **Este token aparece apenas uma vez.** 

![Campos de Endpoint da API SCIM e Token SCIM exibidos com valores mascarados e botões de copiar. Abaixo do campo do token está um botão “Redefinir Token”.]({% image_buster /assets/img/scim.png %})

A Braze espera que todas as solicitações SCIM contenham o token de portador da API SCIM anexado por meio de um cabeçalho HTTP `Authorization`.

{% endtab %}
{% endtabs %}
