---
nav_title: Provisionamento automatizado de usuários
article_title: Provisionamento automatizado de usuários
page_order: 10
page_type: reference
description: "Este artigo de referência aborda as informações que precisam ser fornecidas para o provisionamento automatizado de usuários e como e onde usar o token gerado pelo System for Cross-domain Identity Management (SCIM)."
alias: /scim/automated_user_provisioning/

---

# Provisionamento automatizado de usuários

> Saiba o que é necessário fornecer para o provisionamento automatizado de usuários e como e onde usar o token gerado do System for Cross-domain Identity Management (SCIM) e o endpoint da API do SCIM. Em seguida, é possível chamar esse endpoint com sua API para provisionar automaticamente novos usuários do dashboard.

Para acessar essa página, acesse **Configurações** > **Configurações administrativas** > **Provisionamento SCIM**.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), selecione o menu suspenso da sua conta e acesse **Configurações da empresa** > **Provisionamento automatizado de usuários**.
{% endalert %}

## Como obter seu token SCIM

Você precisará fornecer as seguintes informações para obter seu token SCIM:

1. Selecione um espaço de trabalho padrão para os novos desenvolvedores de dashboard a serem adicionados. Se você não especificar um espaço de trabalho na [chamada da API SCIM para criar usuários](/docs/post_create_user_account/), eles serão adicionados aqui.
2. Fornecer uma origem de serviço. A origem do serviço é como a Braze identifica de onde a solicitação está vindo.
3. Opcionalmente, forneça uma lista separada por vírgulas ou um intervalo de endereços IP permitidos para solicitações SCIM. O cabeçalho `X-Origin-Request` em cada solicitação será usado para verificar o endereço IP da solicitação em relação à lista de permissões.<br><br>

{% alert note %}
Esse endpoint SCIM não se integra diretamente aos provedores de identidade.
{% endalert %}

![][1]

Depois de preencher os campos obrigatórios, você pode gerar um token SCIM e ver seu endpoint da API SCIM. **Esse token será apresentado apenas uma vez.** A Braze espera que todas as solicitações SCIM contenham o token de portador da API SCIM anexado por meio de um cabeçalho HTTP `Authorization`.

[1]: {% image_buster /assets/img/scim.png %}
