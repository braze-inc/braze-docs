---
nav_title: Fusos horários do espaço de trabalho
article_title: Fusos Horários de Espaço de Trabalho para Envio de Mensagens
alias: /workspace_time_zones/
page_order: 3
description: "Este artigo de referência cobre como configurar diferentes fusos horários para seus espaços de trabalho Braze, proporcionando mais controle sobre o agendamento de campanhas e Canvases para equipes que operam em várias localizações geográficas."
---

# Fusos horários de espaço de trabalho para envio de mensagens

> Os fusos horários de espaço de trabalho permitem que os administradores definam fusos horários específicos para espaços de trabalho individuais. Isso faz com que campanhas agendadas e Canvases (que não usam fuso local ou Intelligent Timing) sejam enviadas de acordo com o fuso horário designado do espaço de trabalho, em vez do fuso horário geral da empresa.

{% multi_lang_include early_access_beta_alert.md feature='Workspace time zones' %}

Por padrão, um novo espaço de trabalho herda o fuso horário definido para sua empresa. Os administradores podem substituir esse padrão para um ou mais espaços de trabalho com fusos horários de espaço de trabalho. Quando um fuso horário de espaço de trabalho é definido, campanhas agendadas e Canvases dentro desse espaço de trabalho referenciam esse novo fuso horário para seus horários de envio.

Por exemplo, se um fuso horário de espaço de trabalho é definido como PST, e uma campanha dentro desse espaço de trabalho está agendada para ser enviada às 15h PST, ela será entregue às 15h PST. Isso é verdade mesmo que o fuso horário geral da sua empresa seja diferente (como EST, onde 15h PST seria 18h EST).

## Gerenciando fusos horários de espaço de trabalho

Se você é um administrador, pode acessar e gerenciar fusos horários de espaço de trabalho indo para **Configurações** > **Configurações do Administrador** > **Fusos Horários de Espaço de Trabalho**.

Aqui, você pode ver uma lista de todos os seus espaços de trabalho, seu fuso horário definido e a última vez que o fuso horário foi editado. Use a barra de pesquisa para encontrar espaços de trabalho específicos pelo nome.

![Página "Fusos Horários de Espaço de Trabalho" com uma lista de espaços de trabalho, seus respectivos fusos horários e quando os fusos horários foram editados pela última vez.]({% image_buster /assets/img/workspaces/time_zones/workspace_time_zones_page.png %})

### Definindo um fuso horário 

{% alert note %}
Pode levar alguns minutos para que as atualizações de fuso horário entrem em vigor.
{% endalert %}

{% tabs %}
{% tab Single workspace %}
1. Localize o espaço de trabalho desejado na lista.
2. Selecione o ícone **Editar** ao lado do nome do espaço de trabalho.

![Botão "Editar" ao lado do nome de um espaço de trabalho.]({% image_buster /assets/img/workspaces/time_zones/single_edit_icon.png %})

{: start="3"}
3\. No menu suspenso, selecione o fuso horário desejado para esse espaço de trabalho.
4\. Selecione **Salvar**.

![Menu suspenso com o fuso horário GMT selecionado.]({% image_buster /assets/img/workspaces/time_zones/edit_single_workspace.png %})
{% endtab %}
{% tab Multiple workspaces %}

Você pode aplicar um fuso horário específico a vários espaços de trabalho ao mesmo tempo fazendo o seguinte:

1. Selecione as caixas ao lado de todos os espaços de trabalho que deseja atualizar.
2. Selecione **Editar fuso horário**.
3. No menu suspenso, selecione um fuso horário para aplicar a todos os espaços de trabalho selecionados.

![Página "Fusos horários do espaço de trabalho" com vários espaços de trabalho selecionados e um botão "Editar fuso horário".]({% image_buster /assets/img/workspaces/time_zones/bulk_edit_workspace_time_zone.png %})

{: start="4"}
4\. Selecione **Salvar**. 

{% endtab %}
{% endtabs %}

## Impacto em campanhas e Canvases

{% alert important %}
Informe as equipes e partes interessadas relevantes dentro de cada espaço de trabalho sobre quaisquer mudanças de fuso horário para evitar confusão sobre os cronogramas das campanhas.
{% endalert %}

- **Fuso local e campanhas de Tempo Inteligente:** Campanhas e Canvases que usam o fuso horário local de um usuário ou [Tempo Inteligente]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/scheduled_delivery/#option-3-intelligent-timing) para entrega continuarão a funcionar como antes e não serão afetados pelos fusos horários do espaço de trabalho.
- **Campanhas e Canvases agendadas:** Qualquer campanha agendada ou Canvas que não use o fuso horário local do usuário ou Tempo Inteligente para entrega agora será enviada com base no fuso horário selecionado do espaço de trabalho.
- **Campanhas agendadas antes de uma mudança de fuso horário:** Se você agendou uma campanha ou Canvas antes de mudar o fuso horário do espaço de trabalho, a Braze mantém o horário de envio original e não o reprograma. Por exemplo, se uma campanha está programada para ser enviada às 19h PST e o fuso horário do espaço de trabalho é alterado para EST, a campanha ainda será enviada às 19h PST (que agora corresponde às 22h EST). O sistema continuará a referenciar o horário original, mas o interpretará através do novo fuso horário do espaço de trabalho.

## Impacto nos filtros de público baseados em data

Quando um fuso horário do espaço de trabalho é atualizado, os filtros de público que usam critérios apenas de data (onde nenhum horário específico é fornecido) são reavaliados com base nos limites do novo fuso horário.

Para filtros como "Última vez que fez o evento personalizado X após" a Braze usa o fuso horário do espaço de trabalho para determinar o início e o fim do dia do calendário. Alterar esta configuração muda o ponto de corte das 23:59 para essa data específica.

### Exemplo

Um espaço de trabalho atualiza seu fuso horário de Horário Padrão do Leste (EST) para Horário Padrão do Pacífico (PST).

- **Hora de corte anterior:** 23:59 EST
- **Nova hora de corte:** 23:59 PST (que é 2:59 EST do dia seguinte)

Após essa mudança, um usuário que realiza o evento personalizado às 22:00 PST em 6 de março de 2026 (que é 1:00 EST em 7 de março de 2026) agora está incluído no público, pois se enquadra na fronteira do calendário PST para essa data.

## Discrepâncias de relatórios

Os fusos horários do espaço de trabalho fornecem controle preciso sobre o envio de campanhas, mas você deve estar ciente de possíveis discrepâncias de relatórios enquanto este recurso estiver em acesso antecipado. Faça uma referência cruzada dos pontos de dados e esteja atento ao fuso horário ao analisar relatórios para espaços de trabalho com substituições de fuso horário específicas.