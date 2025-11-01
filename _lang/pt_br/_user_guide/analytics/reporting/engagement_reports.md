---
nav_title: Relatórios de engajamento
article_title: Relatórios de engajamento
page_order: 3
local_redirect:
  report-glossary: '/docs/user_guide/data_and_analytics/report_metrics/'
page_type: tutorial
description: "Este artigo explica como criar, personalizar e programar relatórios de envolvimento para campanhas e Canvases."
tool:
  - Campaigns
  - Canvas
  - Reports
---

# Relatórios de engajamento

> Os Relatórios de Engajamento permitem que você obtenha estatísticas de engajamento para mensagens específicas de campanhas e Canvases para receber como um e-mail no momento de sua preferência.

{% alert note %}
Você precisa de permissões de "Exportar dados do usuário" para executar Relatórios de envolvimento.
{% endalert %}

Com os Relatórios de Envolvimento, você pode selecionar manualmente campanhas e Canvases para incluir em seu relatório de e-mail ou especificar regras para selecionar automaticamente campanhas e Canvases relevantes.

Independentemente do número de campanhas ou Canvases que você selecionar, serão gerados até dois arquivos CSV - um para todos os dados da campanha e outro para todos os dados do Canvas. Você pode acessar esses arquivos CSV a partir do link incorporado no e-mail do seu relatório. Os Relatórios de Engajamento não são salvos no painel do Braze.

Certos dados são agregados no nível da campanha ou do Canvas em comparação com a variante de campanha individual ou o nível da etapa do Canvas. Se você [excluir uma etapa do Canvas após o lançamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-details), isso também removerá os dados dos Relatórios de envolvimento.

{% alert tip %}
Você pode executar novamente o relatório para gerar estatísticas atualizadas.
{% endalert %}

## Criação de um novo relatório

### Etapa 1: Criar um relatório

Em sua conta do painel, vá para **Analytics** > **Relatórios de envolvimento**. Selecione **\+ Criar novo relatório**.

### Etapa 2: Adicionar mensagens

Adicione as campanhas e as mensagens do Canvas que você gostaria de compilar em seu relatório. Você pode selecionar suas mensagens de duas maneiras:

- Selecionar manualmente campanhas e Canvases
- Selecionar automaticamente campanhas e Canvases com base em regras específicas

![engagement_reports_message_selection]({% image_buster /assets/img_archive/engagement_report_add_messages.png %})

#### Selecionar manualmente campanhas ou Canvases

Essa opção lhe dá a liberdade de escolher as campanhas ou Canvases que deseja incluir nesse relatório.

#### Selecionar automaticamente campanhas ou Canvases

Essa opção permite que você inclua automaticamente todas as mensagens que contenham uma [tag]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) específica. Você pode direcionar mensagens que tenham qualquer uma ou todas as tags listadas. Essa opção é útil se você estiver configurando relatórios recorrentes e marcar regularmente suas mensagens de engajamento.

### Etapa 3: Adicionar estatísticas {#add-statistics-to-your-reports}

A etapa **Add Stats (Adicionar estatísticas** ) mostra as estatísticas dos tipos de campanhas ou Canvases que você selecionou. Por exemplo, se você selecionou mensagens de e-mail, só poderá visualizar as estatísticas de e-mail relevantes. Se você escolheu uma combinação de e-mail e push, poderá visualizar as estatísticas desses dois canais.

![engagement_report_add_stats]({% image_buster /assets/img_archive/engagement_report_add_stats.png %})

| Canal | Estatísticas disponíveis |
| ------| --------------|
| E-mail | Envios, aberturas, aberturas exclusivas, cliques, cliques exclusivos, cliques para abrir, cancelamentos de assinatura, devoluções, entregas, spam denunciado |
| Empurrar  | Envios, aberturas, aberturas influenciadas, rejeições, cliques no corpo |
| Web Push | Envios, aberturas, rejeições, cliques no corpo |
| Mensagem no aplicativo | Impressões, cliques, cliques no primeiro botão, cliques no segundo botão |
| Webhook  |  Envios, erros |
| SMS | Envios, Envios para a transportadora, Entregas confirmadas, Falhas na entrega, Rejeições |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
O *envio para a operadora* está obsoleto, mas continuará a ter suporte para os usuários que já o possuem.
{% endalert %}

### Etapa 4: Configuração completa do relatório

Dê um nome ao seu relatório, escolha como ele será formatado e selecione os destinatários. Por padrão, os Relatórios de envolvimento são enviados como um arquivo ZIP em que os dados são delimitados por vírgulas (em que cada parte dos dados é separada por uma vírgula).

Você pode selecionar entre as seguintes opções de compressão e delimitador:

- **Compressão:** ZIP, não compactado ou gzip
- **Delimitador:** Vírgula (`,`), Dois pontos (`:`), Ponto e vírgula (`;`) ou Pipe (`|`)

{% alert note %}
As estatísticas são coletadas apenas para o intervalo de datas especificado pelo relatório. Para receber estatísticas precisas de taxa de abertura e de cliques, selecione um intervalo de datas que inclua quando os eventos de envio foram realizados para suas campanhas e Canvases.
{% endalert %}

#### Selecione o período de tempo

Por padrão, o intervalo de dados mostrado é baseado no fuso horário de sua empresa e vai da mensagem mais antiga selecionada até a data atual. Você pode personalizar isso selecionando o menu suspenso de datas e usando a seleção de intervalo personalizado OU selecionando o botão de opção seguinte e definindo seu intervalo de datas com as opções de menu suspenso disponíveis.

#### Selecione a exibição de dados

Por padrão, os dados exibidos nos relatórios de envolvimento são diários (um dia). Para visualizar esses dados em diferentes intervalos, escolha um número explícito de dias ou semanas para agregar os dados ao relatório. Portanto, em vez de ver métricas diárias, você pode visualizar seu envolvimento por semana, mês, trimestre ou algo semelhante. Se uma agregação centrada no tempo não for suficiente, você também pode optar por exportar dados no nível da campanha ou do Canvas.

![engagement_reports_data_coverage]({% image_buster /assets/img_archive/engagement_report_datacoverage.png %})

#### Agende seu relatório

Há duas opções para agendar seu relatório:

- **Enviar imediatamente:** Depois que o relatório for lançado, o Braze enviará esse relatório imediatamente.
- **Enviar em um horário determinado:** Essa opção lhe dá a flexibilidade de escolher a frequência com que você recebe esse relatório. Você pode optar por enviar esse relatório a cada número definido de dias, semanas ou meses. Você também pode definir quando interromper o envio do relatório.

![engagement_reports_schedule_report]({% image_buster /assets/img_archive/engagement_report_reportschedule.png %}){: style="max-width:65%;" }

### Etapa 5: Revisão e lançamento

A etapa final da configuração do relatório mostra uma visão geral somente de visualização das opções configuradas. Revise o relatório e, quando estiver satisfeito, selecione **Launch Report (Iniciar relatório**).

### Etapa 6: Verifique seu e-mail  

Você receberá um e-mail com links para seus relatórios no horário ou na programação que escolher. **Esses links expiram uma hora após o envio do relatório.** Ao selecionar os links fornecidos, você fará o download automático de um arquivo ZIP contendo seus arquivos CSV - um para todas as campanhas.

O relatório contém todas as estatísticas selecionadas na seção [Add Stats (Adicionar estatísticas](#add-statistics-to-your-reports) ) do processo de configuração.


