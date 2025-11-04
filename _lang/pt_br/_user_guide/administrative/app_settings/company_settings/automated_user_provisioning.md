---
nav_title: Provisionamento automatizado de usuários
article_title: Provisionamento automatizado de usuários
page_order: 10
page_type: reference
description: "Este artigo de referência aborda as informações que você precisa fornecer para o provisionamento automatizado de usuários e como e onde usar o token gerado pelo System for Cross-domain Identity Management (SCIM)."
alias: /scim/automated_user_provisioning/

---

# Provisionamento automatizado de usuários

> Use o provisionamento SCIM para criar e gerenciar automaticamente os usuários do Braze por meio da API. Este artigo o orienta sobre as informações a serem fornecidas, como gerar o token SCIM e onde encontrar o ponto de extremidade da API SCIM.

## Etapa 1: Acessar as configurações de privacidade do SCIM

No painel de controle do Braze, acesse **Configurações** > **Configurações administrativas** > **Provisionamento SCIM**.

## Etapa 2: Configure suas definições SCIM

Para ativar o provisionamento do SCIM, forneça as seguintes informações:

- **Espaço de trabalho padrão:** Selecione o espaço de trabalho onde os novos usuários serão adicionados por padrão. Se você não especificar um espaço de trabalho em sua [solicitação da API SCIM]({{site.baseurl}}/post_create_user_account/), o Braze atribuirá os usuários a esse espaço de trabalho.
- **Origem do serviço:** Digite o domínio de origem de suas solicitações SCIM. O Braze usa isso no cabeçalho `X-Request-Origin` para verificar de onde as solicitações estão vindo.
- **Lista de permissões de IP (opcional):** Você pode restringir as solicitações SCIM a endereços IP específicos.
Digite uma lista separada por vírgulas ou um intervalo de endereços IP a serem permitidos. O cabeçalho `X-Request-Origin` em cada solicitação será usado para verificar o endereço IP da solicitação em relação à lista de permissões.

{% alert note %}
Esse endpoint SCIM não se integra diretamente aos provedores de identidade.
{% endalert %}

Formulário de configurações de provisionamento do SCIM com três campos: Default Workspace (Espaço de trabalho padrão), Service Origin (Origem do serviço) e IP Allowlisting (Lista de permissões de IP) opcional. O botão "Generate SCIM Token" (Gerar token SCIM) está desativado.]({% image_buster /assets/img/scim_unfilled.png %})

## Etapa 3: Obtenha seu token e ponto de extremidade SCIM

Depois de preencher os campos obrigatórios, pressione **Generate SCIM token (Gerar token** SCIM) para gerar um token SCIM e ver seu ponto de extremidade da API SCIM. Certifique-se de copiar o token SCIM antes de sair navegando. **Esse token será apresentado apenas uma vez.** 

Os campos SCIM API Endpoint e SCIM Token são exibidos com valores mascarados e botões de cópia. Abaixo do campo de token há um botão "Reset Token".]({% image_buster /assets/img/scim.png %})

O Braze espera que todas as solicitações SCIM contenham o token do portador da API SCIM anexado por meio de um cabeçalho HTTP `Authorization`.

