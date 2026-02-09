---
nav_title: "Filtragem de cliques de bots"
article_title: "Filtragem de cliques de bots de SMS e RCS"
description: "Este artigo de referência aborda a filtragem de cliques de bots de SMS e RCS."
alias: /sms_rcs_bot_click_filtering/
page_type: reference
page_order: 11
channel:
  - SMS
  - RCS
---

# Filtragem de cliques de bots de SMS e RCS

> A filtragem de cliques de bots de SMS e RCS aprimora a análise de dados e os fluxos de trabalho da campanha, excluindo cliques suspeitos de bots. Um "clique de bot" se refere a cliques automatizados em links encurtados em mensagens SMS e RCS, como os de rastreadores da internet, prévias de links para Android e iOS ou software de segurança CPaaS. Esse recurso facilita a geração de relatórios precisos, a segmentação e a orquestração para engajar usuários reais. <br><br> Para filtragem de cliques de bots em campanhas de e-mail, consulte [Filtragem de bots para e-mails]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/bot_filtering/).

## Como funciona?

O Braze tem um sistema de detecção exclusivo que usa várias entradas para identificar cliques suspeitos de bots, também conhecidos como interações não humanas (NHI). Os cliques de bots podem inflar as taxas de cliques, distorcendo as métricas de engajamento. Ao filtrá-los, o Braze facilita a captura de dados confiáveis para a tomada de decisões.

Nosso sistema analisa os agentes de usuário associados a rastreadores da Web, prévias de links para Android e iOS ou software de segurança CPaaS. Alguns exemplos de agentes de usuário filtrados incluem `GoogleBot`, `python-requests/2.32.3` e `Barracuda Sentinel (EE)`.

## Métricas e fluxos de trabalho afetados

As seguintes métricas e fluxos de trabalho do Braze são afetados por cliques de bots:

- **_Total de cliques_:** A análise de campanhas e a análise de dados do Canva excluirão os cliques de bots, refletindo apenas as interações humanas.
- **Filtros de segmentação:** Os filtros de segmento que fazem referência a interações de links de SMS excluirão cliques de bots para redirecionamento mais preciso em campanhas e Canvas.
- **Orquestração:** Os cliques de bots são filtrados a partir de acionadores baseados em ação e jornadas de ação do Canvas que fazem referência a interações de links de SMS, permitindo que os acionadores reflitam o comportamento humano.
- **Inteligência do Braze:**
    - **Seleção inteligente:** Exclui os cliques de bots ao otimizar a seleção de variantes.
    - **Canal inteligente:** Exclui cliques de bots quando SMS ou RCS é selecionado para uma seleção precisa do canal.
    - **Etapas do experimento:** Exclui cliques de bots para obter resultados confiáveis do experimento.
    - **Exportação de dados de Currents:** Inclui os campos `is_suspected_bot_click` e `suspected_bot_click_reason` para ajudar a analisar os cliques de humanos e de bots. Esses campos estão disponíveis no [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/), no [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) e no [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/).

Os cancelamentos de inscrição por suspeita de cliques de bots não são afetados. O Braze processa todas as solicitações de cancelamento de inscrição como de costume. Para bloquear esses cancelamentos de inscrição, [envie feedback sobre o produto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

## Campos Currents em eventos de clique de SMS

O Braze inclui os seguintes campos Currents para eventos de clique de SMS:

| Campo | Tipo de dados | Descrição |
| --- | --- | --- |
| `is_suspected_bot_click` | Booleano | Indica se o clique é um clique suspeito de bot. Retorna `null` para todos os usuários até que a filtragem de cliques de bots seja ativada para sua empresa. Quando ativada, ela será preenchida com `true` ou `false` para todos os novos cliques futuros. |
| `suspected_bot_click_reason` | String, Matriz | Indica o motivo de um clique suspeito de bot (como `user_agent`). É preenchido mesmo se a filtragem estiver desativada, fornecendo insight sobre possíveis atividades de bots. Esse campo está disponível globalmente e é preenchido com um motivo para todos os usuários, mesmo que a filtragem de cliques de bots ainda não esteja ativada. Isso fornece insight sobre a possível atividade de bots antes de ativar a filtragem de cliques de bots. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Modelo do Query Builder

Para ajudar a analisar seus dados, você pode usar o modelo móvel pré-criado de **eventos de clique em SMS por bots** no [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/).

## Perguntas frequentes

### Como a filtragem de cliques de bots afeta a performance da campanha?

A filtragem não afeta as campanhas enviadas anteriormente. Quando ativada, ela reduz as taxas de cliques a partir desse momento, excluindo os cliques de bots.

### A filtragem de cliques de bots evita que os bots cliquem nos tk's de cancelamento de inscrição?

Não. Todas as solicitações de cancelamento de inscrição são processadas normalmente.

### As prévias de links estão incluídas na filtragem de cliques de bots?

Sim. As prévias de links (como as prévias de links para Android e iOS) são sinalizadas como cliques de bots e filtradas.

### Como faço para ativar a filtragem de cliques de bots?

É necessário entrar em contato com a equipe da sua conta Braze para ativar a filtragem de cliques de bots durante o acesso antecipado. Quando a filtragem de cliques de bots tiver disponibilidade geral, o recurso será ativado por padrão para todos os usuários de SMS e RCS.

Certifique-se também de ter ativado o rastreamento avançado de cliques para [encurtamento de links]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/). Isso permite que você receba a análise de dados de cliques do bot, pois rastreamos esses dados no nível do usuário individual. 

{% alert note %}
Para obter mais assistência, [entre em contato com o Suporte]({{site.baseurl}}/braze_support/).
{% endalert %}