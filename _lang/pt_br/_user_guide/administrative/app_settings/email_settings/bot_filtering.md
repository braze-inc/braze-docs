---
nav_title: Filtragem de bots para e-mails
article_title: Filtragem de bots para e-mails
page_type: reference
page_order: 1
toc_headers: h2
alias: "/bot_filtering/"
description: "Este artigo fornece uma visão geral da filtragem de bots para e-mail."
---

# Filtragem de bots para e-mails

> Configure a filtragem de bots em suas [Preferências de e-mail]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings) para excluir todos os cliques suspeitos de máquinas ou bots. Um "clique de bot" em e-mail refere-se a um clique em hiperlinks em um e-mail gerado por um programa automatizado. Ao filtrar esses cliques de bots, você pode acionar intencionalmente e enviar mensagens para destinatários que estejam engajados.

{% alert important %}
A partir de 9 de julho de 2025, todos os novos espaços de trabalho criados terão a configuração de filtragem de bots ativada para gerar relatórios de cliques mais precisos no Braze.
{% endalert %}

## Sobre cliques de bots

O Braze tem um sistema de detecção que emprega várias entradas para identificar cliques suspeitos de bots, também chamados de interações não humanas (NHI). Os cliques de bots podem distorcer suas métricas de engajamento por e-mail, aumentando artificialmente as taxas de cliques. Essa abordagem nos permite diferenciar entre interações humanas genuínas e atividades suspeitas de bots para manter a integridade das métricas e dos insights de engajamento por clique.

## Métricas afetadas por cliques de bots

{% alert note %}
A filtragem de bots bloqueia ativamente cliques automatizados suspeitos para melhorar a precisão de suas métricas de engajamento. No entanto, os scanners e bots evoluem continuamente com o tempo, de modo que o Braze não pode garantir a remoção de todas as interações não humanas.
{% endalert %}

As seguintes métricas do Braze podem ser afetadas por cliques de bots:

- Taxa total de cliques
- Taxa de cliques únicos
- Taxa de cliques para abrir
- Taxa de conversão (se "Campanha de cliques" for selecionada como o evento de conversão)
- Mapa de calor
- Determinados filtros de segmento

[Os recursos do Braze Intelligence]({{site.baseurl}}/user_guide/brazeai/intelligence) que utilizam dados de cliques em nossos sistemas de detecção podem ser afetados. A ativação da configuração pode interromper temporariamente nossos sistemas de detecção, o que pode resultar em uma diminuição na métrica ou na entrada devido a essa exclusão de cliques suspeitos de bots:

- Seleção inteligente
- Canal inteligente
- Cronograma inteligente
- Etapa do experimento
    - Caminho da vitória
    - Caminho personalizado
- Campanha
    - Variante vencedora
    - Variante personalizada
- Taxa de abertura real estimada

Os cancelamentos de inscrição decorrentes de cliques suspeitos de bots não serão afetados. A Braze continuará processando todas as solicitações de cancelamento de inscrição como de costume. Se você quiser que a Braze bloqueie esses cancelamentos de inscrição, envie [um feedback sobre o produto]({{site.baseurl}}/user_guide/administrative/access_braze/portal).

## Filtros de segmentação afetados pela filtragem de bots

Os seguintes [filtros de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) podem ser afetados pela filtragem de bots para mensagens de e-mail:

- [Campanha clicada/aberta ou Canvas com tag]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-opened-campaign-or-canvas-with-tag)
- [Etapa clicada/aberta]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-opened-step)
- [Alias clicado na campanha]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-alias-in-campaign)
- [Alias clicado na etapa do Canvas]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-alias-in-canvas-step)
- [Alias clicado em qualquer etapa do Campaign ou do Canvas]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-alias-in-any-campaign-or-canvas-step)
- [Último engajamento com a mensagem]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#last-engaged-with-message)
- [Canal inteligente]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#intelligent-channel)

## Ativação da filtragem de bots

Vá para **Configurações** > **Preferências de e-mail**. Em seguida, selecione **Remove bot clicks (Remover cliques de bots**). Essa configuração é aplicada no nível do espaço de trabalho.

Qualquer suspeita de cliques de bots só será removida depois que a configuração for ativada e não se aplica retroativamente às métricas em seu espaço de trabalho.

Configuração de e-mail de filtragem de bots ativada nas Preferências de e-mail.]({% image_buster /assets/img/bot_tracking_email.png %})

{% alert important %}
Se você ativar essa configuração e depois desativá-la, o Braze não poderá restaurar nenhuma atividade de bot removida anteriormente em sua análise.
{% endalert %}

## Campos em eventos de clique de e-mail para Currents e Snowflake

O Braze enviará os campos `is_suspected_bot_click` e `suspected_bot_click_reason` em Currents e Snowflake para um evento de clique em e-mail.

| Campo | Tipo de dados | Descrição | Campo
| `is_suspected_bot_click` | Boolean | Indica que se trata de um clique suspeito de bot. Isso será enviado como valores nulos até que você ative a configuração **Remove bots clicks** workspace. Essa abordagem permite que você entenda programaticamente quando a filtragem de cliques suspeitos de bots foi iniciada em seu espaço de trabalho para que você possa comparar com precisão os dados no Currents e no Snowflake. |
| `suspected_bot_click_reason` | Array | Indica o motivo pelo qual esse é um clique suspeito de ser de um bot. Isso será preenchido com valores, como `user_agent` e `ip_address`, mesmo que a configuração do espaço de trabalho de filtragem de bots esteja desativada. Esse campo pode fornecer informações sobre o possível impacto da ativação dessa configuração, comparando o número de cliques decorrentes de cliques suspeitos de bots com interações humanas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Perguntas frequentes

### Como a filtragem de bots afetará o desempenho da minha campanha?

Isso não afetará as métricas de nenhuma campanha anterior já enviada. Quando a filtragem de bots estiver ativada em seu espaço de trabalho, o Braze começará a filtrar os cliques suspeitos de bots de todos os cliques. Você pode notar uma queda nas taxas de cliques, mas a taxa de cliques é uma representação mais precisa do envolvimento dos usuários com as mensagens de e-mail.

### A filtragem de bots impedirá que os bots que clicarem no link de cancelamento de assinatura do Braze cancelem a assinatura?

Não. Todas as solicitações de cancelamento de assinatura continuarão a ser processadas.

### As aberturas de máquina são consideradas na filtragem de cliques de bots?

Não.
