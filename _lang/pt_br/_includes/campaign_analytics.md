## Análise de dados de campanha

Uma vez que você lançou sua campanha, pode retornar à página de detalhes dessa campanha para visualizar métricas-chave. Navegue até a página **Campanhas** e selecione sua campanha para abrir a página de detalhes. Para {% if include.channel == "Content Card" %}Cartões de Conteúdo {% elsif include.channel == "email" %}e-mail {% elsif include.channel == "in-app message" %}mensagens no aplicativo {% elsif include.channel == "push" %}mensagens push {% elsif include.channel == "SMS" %}mensagens SMS {% elsif include.channel == "whatsapp" %}mensagens WhatsApp {% elsif include.channel == "webhook" %}webhooks {% endif %}enviados no canva, consulte [análise de dados]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/).

{% alert tip %}
Procurando definições para os termos e métricas listados em seu relatório? Consulte
  {% if include.channel == "email" %}[Glossário de Análise de Dados de E-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/)
  {% elsif include.channel == "Content Card" %}[Glossário de Métricas de Relatório]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/) e filtre por Cartões de Conteúdo
  {% elsif include.channel == "in-app message" %}[Glossário de Métricas de Relatório]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/) e filtre por mensagem no app
  {% elsif include.channel == "push" %}[Glossário de Métricas de Relatório]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/) e filtrar por push
  {% elsif include.channel == "SMS" %}[Glossário de Métricas de Relatório]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/) e filtre por SMS
  {% elsif include.channel == "whatsapp" %}[Glossário de Métricas de Relatório]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/) e filtre por WhatsApp
  {% elsif include.channel == "webhook" %}[Glossário de Métricas de Relatório]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/) e filtre por Webhook{% endif %}.
{% endalert %}

Da guia **Análise da campanha**, você pode visualizar seus relatórios em uma série de painéis. Você pode ver mais ou menos do que os listados nas seções abaixo, mas cada um tem seu próprio propósito útil.

### Informações da campanha

O painel **Informações da campanha** mostra uma visão geral de alto nível de todo o desempenho para
  {% if include.channel == "Content Card" %}o seu cartão de conteúdo.
  {% elsif include.channel == "email" %}e-mail.
  {% elsif include.channel == "in-app message" %}a sua mensagem no app.
  {% elsif include.channel == "push" %}a sua mensagem por push.
  {% elsif include.channel == "SMS" %}SMS.
  {% elsif include.channel == "whatsapp" %}Mensagens do WhatsApp.
  {% elsif include.channel == "webhook" %}webhook.
  {% endif %}

Revise este painel para ver métricas gerais, como o número de mensagens enviadas para o número de destinatários, a taxa de conversão primária e a receita total gerada por esta mensagem. Você também pode revisar as configurações de entrega, público e conversão a partir desta página.

{% if include.channel == "whatsapp" %}
{% alert note %}
O canal do WhatsApp inclui a taxa de leitura. Esta métrica é entregue apenas para usuários com recibos de leitura ativados, o que pode variar.
{% endalert %}
{% endif %}

{% if include.channel == "Content Card" %}
![Painel de Detalhes da Campanha com uma visão geral das métricas usadas para determinar o desempenho da campanha.]({% image_buster /assets/img/cc-campaign-details.png %})

{% elsif include.channel == "email" %}
![Painel de Detalhes da Campanha com uma visão geral das métricas usadas para determinar o desempenho da campanha.]({% image_buster /assets/img/campaign_details_email.png %})

{% elsif include.channel == "push" %}
![Painel de Detalhes da Campanha com uma visão geral das métricas usadas para determinar o desempenho da campanha.]({% image_buster /assets/img/campaign_details_push.png %})

{% elsif include.channel == "SMS" %}
![Painel de Detalhes da Campanha com uma visão geral das métricas usadas para determinar o desempenho da campanha.]({% image_buster /assets/img/campaign_details_sms.png %})

{% elsif include.channel == "in-app message" %}
![Painel de Detalhes da Campanha com uma visão geral das métricas usadas para determinar o desempenho da campanha.]({% image_buster /assets/img/campaign_details_iam.png %})

No canva, você verá a performance da mensagem no app mapeada no canva que você criou. Você pode usar o painel de controle na parte superior da página para limpar outros tipos de envio de mensagens (canais) e visualizar apenas as mensagens no app em seu canva.

![]({% image_buster /assets/img/in-app_message_canvas_reporting.png %})

{% elsif include.channel == "webhook" %}
![Painel de Detalhes da Campanha com uma visão geral das métricas usadas para determinar o desempenho da campanha.]({% image_buster /assets/img/campaign_details_webhook.png %})

{% endif %}

{% if include.channel == "Content Card" %}

#### Grupos de controle {#cc-control-group}

Para medir o impacto de um cartão de conteúdo individual, você pode adicionar um [grupo de controle][2] a um teste A/B. O painel **Detalhes da Campanha** de nível superior não inclui métricas da variante grupo de controle.

{% elsif include.channel == "SMS" %}

#### Grupos de controle {#sms-control-group}

Para medir o impacto de uma mensagem SMS individual, você pode adicionar um [grupo de controle][2] a um teste A/B. O painel **Detalhes da Campanha** de nível superior não inclui métricas da variante grupo de controle.

{% elsif include.channel == "whatsapp" %}

#### Grupos de controle {#whatsapp-control-group}

Para medir o impacto de uma mensagem individual do WhatsApp, você pode adicionar um [grupo de controle][2] a um teste A/B. O painel **Detalhes da Campanha** de nível superior não inclui métricas da variante grupo de controle.

{% elsif include.channel == "webhook" %}

#### Grupos de controle {#webhook-control-group}

Para medir o impacto de uma mensagem de webhook individual, você pode adicionar um [grupo de controle][2] a um teste A/B. O painel **Detalhes da Campanha** de nível superior não inclui métricas da variante grupo de controle.

{% endif %}

#### alterações desde a última visualização

O número de atualizações da campanha por outros membros da sua equipe é rastreado pela métrica *Alterações Desde a Última Visualização* na página de visão geral da campanha. Selecione **Alterações Desde a Última Visualização** para ver um changelog de atualizações no nome da campanha, cronograma, tags, mensagem, público, status de aprovação ou configuração de acesso da equipe. Para cada atualização, você pode ver quem realizou a atualização e quando. Você pode usar este changelog para auditar as mudanças na sua campanha.

<!--
### Message Performance

The **Message Performance** panel outlines how well your message has performed across various dimensions. The metrics in this panel vary depending on your chosen messaging channel, and whether or not you are running a multivariate test. You can click on the <i class="fa fa-eye preview-icon"></i> **Preview** icon to view your message for each variant or channel.
-->
{% if include.channel == "Content Card" %}
### Performance do cartão de conteúdo

O painel de **performance do cartão de conteúdo** descreve o desempenho da sua mensagem em várias dimensões. As métricas neste painel variam dependendo do canal de envio de mensagens escolhido e se você está ou não executando um teste multivariante. Você pode clicar no ícone de <i class="fa fa-eye preview-icon"></i> **prévia** para visualizar sua mensagem para cada variante ou canal.

![Análise de performance de mensagem do cartão de conteúdo]({% image_buster /assets/img/cc-message-performance.png %})

{% elsif include.channel == "email" %}
### Performance de e-mail

O painel de **performance de e-mail** descreve o desempenho da sua mensagem em várias dimensões. As métricas neste painel variam dependendo do canal de envio de mensagens escolhido e se você está ou não executando um teste multivariante. Você pode clicar no ícone de <i class="fa fa-eye preview-icon"></i> **prévia** para visualizar sua mensagem para cada variante ou canal.

![Análise de performance de mensagem de e-mail]({% image_buster /assets/img_archive/email_message_performance.png %})

{% elsif include.channel == "in-app message" %}
### Performance de mensagem no app

O painel de **performance de mensagem no app** descreve o desempenho da sua mensagem em várias dimensões. As métricas neste painel variam dependendo do canal de envio de mensagens escolhido e se você está ou não executando um teste multivariante. Você pode clicar no ícone de <i class="fa fa-eye preview-icon"></i> **prévia** para visualizar sua mensagem para cada variante ou canal.

![Análise de performance de mensagem no app]({% image_buster /assets/img_archive/iam_message_performance.png %})

{% elsif include.channel == "push" %}
### Performance de push

O painel de **performance de push** descreve o desempenho da sua mensagem em várias dimensões. As métricas neste painel variam dependendo do canal de envio de mensagens escolhido e se você está ou não executando um teste multivariante. Você pode clicar no ícone de <i class="fa fa-eye preview-icon"></i> **prévia** para visualizar sua mensagem para cada variante ou canal.

![Análise de performance de mensagem de push]({% image_buster /assets/img_archive/push_message_performance.png %})

{% elsif include.channel == "SMS" %}
### Performance de SMS

O painel de **performance de SMS** descreve o desempenho da sua mensagem em várias dimensões. As métricas neste painel variam dependendo do canal de envio de mensagens escolhido e se você está ou não executando um teste multivariante. Você pode clicar no ícone de <i class="fa fa-eye preview-icon"></i> **prévia** para visualizar sua mensagem para cada variante ou canal.

![Painel de performance de SMS/MMS que inclui uma tabela de métricas para um grupo de controle, Variante 1 e Variante 2.]({% image_buster /assets/img_archive/sms_message_performance.png %})

{% elsif include.channel == "webhook" %}
### Performance de webhook

O painel de **performance do webhook** descreve o desempenho da sua mensagem em várias dimensões. As métricas neste painel variam dependendo do canal de envio de mensagens escolhido e se você está ou não executando um teste multivariante. Você pode clicar no ícone de <i class="fa fa-eye preview-icon"></i> **prévia** para visualizar sua mensagem para cada variante ou canal.

![Painel de performance do Webhook que inclui uma tabela de métricas para um grupo de controle e Variante 1.]({% image_buster /assets/img/webhook_message_performance.png %})

{% elsif include.channel == "whatsapp" %}
### Performance do WhatsApp

O painel de **performance de whatsapp** descreve o desempenho da sua mensagem em várias dimensões. As métricas neste painel variam dependendo do canal de envio de mensagens escolhido e se você está ou não executando um teste multivariante. Você pode clicar no ícone de <i class="fa fa-eye preview-icon"></i> **prévia** para visualizar sua mensagem para cada variante ou canal.

![Painel de desempenho do WhatsApp que inclui uma tabela de métricas para a Variante 1.]({% image_buster /assets/img/whatsapp_message_performance.png %})

{% endif %}

Se você quiser simplificar sua visualização, clique <i class="fas fa-plus"></i> **Adicionar/Remover Colunas** e limpe quaisquer métricas conforme desejado. Por padrão, todas as métricas são exibidas.

{% if include.channel == "email" %}

#### Mapas de calor

Usando mapas de calor, você pode ver quão bem-sucedidos são os diferentes links em uma única campanha de e-mail. Da seção **análise de dados**, acesse o painel **performance de e-mail**. Selecione **Prévia e mapa de calor** para visualizar uma prévia da sua campanha de e-mail e o mapa de calor. Alternativamente, você pode selecionar o hyperlink no nome da variante para ver o mapa de calor.

Nesta visualização, você pode usar o **Mostrar mapa de calor** para trazer uma visão visual do seu e-mail que mostra a frequência geral e o local dos cliques durante a duração da campanha. No painel **Link Table by Total Clicks**, você pode ver todos os links na sua campanha de e-mail e classificar por total de cliques. Isso pode fornecer um insight adicional sobre onde seus usuários navegam. Para salvar uma cópia do mapa de calor para referência, selecione o botão de baixar.

![Exemplo da página de Prévia e Mapa de Calor que inclui uma campanha de e-mail, e um painel com exemplos de alias de link com seus cliques totais.]({% image_buster /assets/img_archive/email_heatmap_example.png %})

#### Imagens

Sugerimos habilitar CORS para suas URLs de imagem para ajudar a evitar que as imagens quebrem nas prévias e exportações do mapa de calor.

{% endif %}

{% if include.channel == "Content Card" %}

#### Métricas do cartão de conteúdo

Aqui está uma análise de algumas métricas-chave que você pode ver ao revisar o desempenho da sua mensagem. Para as definições completas de todas as métricas dos Cartões de Conteúdo, consulte o [Glossário de Métricas do Relatório][1] e filtre por Cartões de Conteúdo.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrico</th>
            <th>Definição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#messages-sent">Mensagens enviadas</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Messages Sent' %} <br><br>
                Isso é calculado de forma diferente dependendo do que você selecionou para 
                <a href="/docs/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression">Criação de cartão</a><br><br>
                <ul>
                    <li><b>No lançamento ou etapa de entrada:</b> O número de cartões criados e disponíveis para serem vistos. Isso não conta se os usuários visualizaram o cartão.</li>
                    <li><b>Na primeira impressão:</b> O número de cartões exibidos para os usuários.</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">Total de impressões</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total de Impressões' %} Isso pode aumentar várias vezes para o mesmo usuário.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">Impressões únicas</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Impressões Únicas' %} <span style="white-space: nowrap">Esta contagem</span> não incrementa na segunda vez que um usuário visualiza um cartão.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">Destinatários únicos</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Recipients' %}Ò <br><br> Porque um espectador pode ser um destinatário único a cada dia, você deve esperar que isso seja maior do que <i>Impressões Únicas</i>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">Cliques únicos projetados</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Clicks' %} Isso inclui cliques em links de cancelar inscrição fornecidos pela Braze.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-dismissals">Descartes únicos</a></td>
            <td>{% multi_lang_include metrics.md metric='Unique Dismissals' %}</td>
        </tr>
    </tbody>
</table>

{% alert note %}
Em relação a como as impressões são registradas, existem algumas nuances entre web, Android e iOS. De maneira geral, o Braze registra uma impressão quando um cartão é visto, que ocorre após um usuário rolar até o cartão de conteúdo específico em seu feed.
{% endalert %}

#### Destinatários Únicos versus Impressões Únicas

Existem algumas métricas disponíveis que cobrem a visibilidade da sua mensagem. Isto inclui _Mensagens Enviadas_, _Destinatários Únicos_, e _Impressões Únicas_. Em particular, a diferença entre _Destinatários Únicos_ e _Impressões Únicas_ pode ser um pouco confusa. Vamos usar alguns cenários de exemplo para entender melhor essas métricas.

Vamos supor que você veja um cartão de conteúdo hoje, depois veja o mesmo cartão amanhã, e novamente depois de amanhã—você será contado como um _Destinatário Único_ três vezes. No entanto, você será contado apenas uma vez para uma _Impressão Única_. Você também será incluído no número de _Mensagens Enviadas_, já que o cartão estava disponível no seu dispositivo.

Como outro exemplo, suponha que você veja cinco _Impressões Únicas_ em uma campanha de cartão de conteúdo mostrando 150.000 _Mensagens Enviadas_.  Isso significa que o cartão foi disponibilizado (no backend) para um público de 150.000 usuários, mas apenas cinco dispositivos de usuários realizaram todas as seguintes etapas após o envio ocorrer:

1. Iniciou uma sessão ou o app solicitou explicitamente uma sincronização de Cartões de Conteúdo (ou ambos)
2. Navegou para a visualização de Cartões de Conteúdo
3. O SDK registrou uma impressão e a registrou no servidor

Suas _Mensagens Enviadas_ referem-se a Cartões de Conteúdo disponíveis para serem vistos, enquanto _Destinatários Únicos_ referem-se a Cartões de Conteúdo que foram realmente vistos.

{% elsif include.channel == "email" %}

#### Métricas de e-mail

Aqui estão algumas métricas específicas de e-mail que você não verá em outros canais. Para ver as definições completas de todas as métricas de e-mail usadas no Braze, consulte nosso [Glossário de Análise de E-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrico</th>
            <th>Definição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">Cliques únicos projetados</a></td>
            <td class="no-split">
                {% multi_lang_include metrics.md metric='Unique Clicks' %} Isso é monitorado ao longo de um período de sete dias para e-mail e medido por <a href='https://braze.com/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>. Isto inclui cliques em links de cancelar inscrição fornecidos pelo Braze. Este número deve estar entre 5–10%. Qualquer coisa acima de 10% é excepcional!
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-opens">Aberturas únicas projetadas</a></td>
            <td class="no-split">
                {% multi_lang_include metrics.md metric='Unique Opens' %} Para e-mail, isso é rastreado ao longo de um período de 7 dias. Este número deve estar entre 30–40%. Qualquer coisa acima de 40% é excepcional!
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#click-to-open-rate">Taxa de cliques por abertura</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Click-to-Open Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#spam">Taxa de spam</a></td>
            <td class="no-split">
                {% multi_lang_include metrics.md metric='Spam' %} Se essa métrica for maior que 0,08, isso pode ser um sinal de que o texto da sua mensagem é muito comercial, ou você deve reconsiderar seus métodos de coleta de endereços de e-mail (para confirmar que você está enviando mensagens para aqueles que estão interessados em sua correspondência).
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unsubscribers-or-unsub">Cancelamento de inscrição</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unsubscribers or Unsub' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#other-opens">Outras aberturas</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Other Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#estimated-real-opens">Aberturas reais estimadas</a></td>
            <td class="no-split"> {% multi_lang_include metrics.md metric='Estimated Real Opens' %} See the following section for details.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#machine-opens">Aberturas por máquina</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Machine Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">Bounces</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Bounces' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#hard-bounce">Hard bounce</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Hard Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#soft-bounce">Soft bounce</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Soft Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deferral">Adiamentos</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Deferral' %}</td>
        </tr>
    </tbody>
</table>

##### Prorrogações

O adiamento ou a prorrogação é quando um e-mail não foi entregue imediatamente, mas o Braze tentará reenviar o e-mail por até 72 horas após essa falha temporária de entrega para maximizar as chances de entrega bem-sucedida antes que as tentativas para essa campanha específica sejam interrompidas. As razões típicas para adiamentos incluem limitação de taxa de volume de e-mail baseada na reputação do provedor de caixa de entrada, problemas temporários de conectividade ou erros de DNS.

Os _adiamentos_ diferem dos _Soft Bounces_. Se nenhum e-mail foi entregue com sucesso durante este período de nova tentativa, a Braze enviará um evento de soft bounce por campanha enviada. Antes de 25 de fevereiro de 2025, essas tentativas foram contadas como múltiplos soft bounces para 1 envio de campanha.

Observe que os _adiamentos_ estão atualmente disponíveis apenas usando os recursos Snowflake Currents ou Braze (como o Construtor de Consultas, Segmento SQL, Compartilhamento de Dados Snowflake). Se você gostaria de incluir isso na análise de campanhas ou do canva, [envie um feedback sobre o produto]({{site.baseurl}}/user_guide/administrative/access_braze/portal).

##### Taxa de abertura real estimada {#estimated-real-open-rate}

Esta estatística utiliza um modelo analítico proprietário criado pela Braze para reconstruir uma estimativa da taxa de abertura única da campanha como se as aberturas de máquina não existissem. Enquanto recebemos rótulos de *Aberturas por máquina* em alguns eventos abertos de remetentes de e-mail (veja acima), esses rótulos podem frequentemente rotular aberturas atuais como aberturas reais. Em outras palavras, os *Outros Abertos* provavelmente são uma subestimação das aberturas reais (por usuários reais). Em vez disso, Braze usa dados de cliques de cada campanha para inferir a taxa na qual humanos reais abriram a mensagem. Isso compensa vários mecanismos de abertura de máquina, incluindo o MPP da Apple.

_Taxa de Abertura Real Estimada_ é calculada 36 horas após o início do envio do e-mail e é recalculada a cada 24 horas a partir de então. Se uma campanha se repetir, a estimativa é recalculada 36 horas após o envio de outra.

Normalmente, são necessários cerca de 10.000 e-mails entregues para que a estatística seja calculada com sucesso, embora esse número possa variar dependendo da taxa de cliques. Se a estatística não puder ser calculada, então a coluna exibe "--".

###### Limitações

A taxa de abertura real estimada está disponível apenas em campanhas e não é relatada em eventos atuais. Esta métrica é calculada retroativamente apenas para campanhas ativas lançadas antes de 14 de novembro de 2023.

{% elsif include.channel == "in-app message" %}

#### métricas de mensagem no app

Aqui estão algumas métricas chave de mensagem no app que você pode ver na análise de dados. Para ver as definições completas de todas as métricas de mensagem no app usadas no Braze, consulte nosso [Glossário de Métricas de Relatório][1].

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrico</th>
            <th>Definição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#body-clicks">Cliques no corpo do texto</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Body Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-1-clicks">Cliques no botão 1</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Button 1 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-2-clicks">Cliques no botão 2</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Button 2 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">Impressões únicas</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">Total de impressões</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversions-b-c-d">Conversões (B, C, D)</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Conversions (B, C, D)' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-conversions">Conversões totais</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Conversions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversion-rate">Taxa de conversão</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Conversion Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#close-message">Fechar mensagem</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Close Message' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "push" %}

#### Métricas de push

Aqui está uma análise de algumas métricas-chave que você pode ver ao revisar o desempenho da sua mensagem. Para as definições completas de todas as métricas de push, consulte o [Glossário de Métricas do Relatório][1] e filtre por push.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrico</th>
            <th>Descrição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">Bounces</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Bounces' %} Veja <a href="#bounced-push">Notificações por push com bounce</a>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#direct-opens">Aberturas diretas</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Direct Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opens">Aberturas</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Opens' %}</td>
        </tr>
    </tbody>
</table>

> A entrega de notificações é um "esforço máximo" pelos serviços de Notificação por Push da Apple (APNs). Não se destina a entregar dados ao seu app, apenas a notificar o usuário de que há novos dados disponíveis. A distinção importante é que exibiremos quantas mensagens entregamos com sucesso a APNs, não necessariamente quantos APNs entregaram com sucesso aos dispositivos.

##### Rastreamento de descadastramentos

As cancelamentos de inscrição de push não estão incluídos como uma métrica na análise de dados da campanha. Consulte [rastreamento de cancelamento de inscrição de push]({{site.baseurl}}/help/help_articles/push/push_unsubscribes) para saber como rastrear manualmente essa métrica.

##### A compreensão abre

Mesmo que _aberturas diretas_ e _aberturas por influência_ incluam a palavra "aberturas", na verdade, são métricas diferentes. _aberturas diretas_ refere-se à abertura direta de uma notificação por push, conforme declarado na tabela acima. _aberturas por influência_ refere-se à abertura de um app, sem abrir uma notificação por push dentro de um intervalo de tempo específico após recebê-la. Então, _aberturas por influência_ refere-se às aberturas do app, não às aberturas de notificação por push.

##### Por que os envios de push podem exceder os destinatários únicos

O número de _Sends_ pode exceder o número de _Unique Recipients_ devido aos seguintes motivos:

- **Reeligibilidade está em:** Quando a re-eligibilidade está habilitada nas configurações da sua campanha ou canva, os usuários que atendem aos critérios de segmento e entrega podem receber a mesma notificação por push várias vezes. Isso resulta em um número maior de envios totais.
- **Os usuários têm múltiplos dispositivos:** Se a re-eligibilidade não estiver habilitada, a diferença pode ser explicada pelo fato de os usuários terem vários dispositivos associados ao seu perfil. Por exemplo, um usuário pode ter tanto um smartphone quanto um tablet, e a notificação por push está sendo enviada para todos os dispositivos registrados. Cada entrega conta como um envio, mas apenas um destinatário único é registrado.
- **Os usuários são atribuídos a vários aplicativos:** Se os usuários estiverem associados a mais de um app (como ao testar um novo app), eles podem receber a mesma notificação por push em cada app. Isso contribui para um maior número de envios.

##### Por que bounces ocorrem {#bounced-push}

{% tabs %}
{% tab serviço de Notificações por Push da Apple %}

Os bounces ocorrem nos serviços de Notificação por Push da Apple (APNs) quando uma notificação por push tenta ser entregue a um dispositivo que não tem o app pretendido instalado. APNs também têm o direito de mudar tokens para dispositivos de forma arbitrária. Se você tentar enviar para o dispositivo de um usuário cujo token por push mudou entre o momento em que registramos anteriormente seu token (como no início de cada sessão, quando registramos um usuário para um token por push) e o momento do envio, isso causaria um bounce.

Se um usuário desativar o push nas configurações do dispositivo, ao abrir o app novamente, o SDK detectará que o push foi desativado e notificará a Braze. Neste ponto, atualizaremos o estado de push de habilitado para desabilitado. Quando um usuário com deficiência recebe uma campanha de push antes de ter uma nova sessão, a campanha seria enviada com sucesso e apareceria como entregue. O push não sofrerá bounce para este usuário. Após uma sessão subsequente, quando você tenta enviar um push para o usuário, o Braze já está ciente se temos um token em primeiro plano, portanto, nenhuma notificação é enviada.

Notificações por push que expiram antes da entrega não são consideradas como falhas e não serão registradas como um bounce.

{% endtab %}
{% tab Firebase Cloud Messaging %}

O Firebase Cloud Messaging (FCM) pode ter falhas em três casos:

| Cenário | Descrição |
| -- | -- |
| Aplicativos desinstalados | Quando uma mensagem tenta ser entregue a um dispositivo e o aplicativo pretendido está desinstalado nesse dispositivo, a mensagem será descartada e o ID de registro do dispositivo será invalidado. Qualquer tentativa futura de envio de mensagens para o dispositivo retornará um erro NotRegistered. |
| Aplicativo de backup | Quando um aplicativo é salvo, seu ID de registro pode se tornar inválido antes que o aplicativo seja restaurado. Neste caso, o FCM não armazenará mais o ID de registro do aplicativo e o aplicativo não receberá mais mensagens. Assim, os IDs de registro **não** devem ser salvos quando um aplicativo é salvo. |
| Aplicativo atualizado | Quando um aplicativo é atualizado, o ID de registro da versão anterior pode não funcionar mais. Assim, um aplicativo atualizado deve substituir seu ID de registro existente. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}


{% elsif include.channel == "SMS" %}

#### Métricas de SMS

Aqui está uma análise de algumas métricas-chave que você pode ver ao revisar o desempenho da sua mensagem. Para as definições completas de todas as métricas de SMS, consulte o [Glossário de Métricas do Relatório][1] e filtre por SMS.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrico</th>
            <th>Definição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sent">Envios</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Sent' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends-to-carrier">Envios para operadora</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Sends to Carrier' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#delivery-failures">Falhas na entrega</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Delivery Failures' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confirmed-delivery">Entrega Confirmada</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Confirmed Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#rejections">Rejeições</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Rejections' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opt-out">Cancelamentos de inscrição</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Opt-Out' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#help">Ajuda</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Help' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">Total de cliques</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Clicks' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "webhook" %}

#### Métricas de Webhook

Aqui estão algumas métricas de webhook chave que você pode ver em sua análise de dados. Para ver as definições completas de todas as métricas de webhook usadas no Braze, consulte nosso [Glossário de Métricas de Relatório][1].

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrico</th>
            <th>Definição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">Destinatários únicos</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Recipients' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">Envios</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#errors">Erros</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Errors' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "whatsapp" %}

#### Métricas do WhatsApp

Aqui estão algumas métricas importantes do WhatsApp que você pode ver em sua análise de dados. Para ver as definições completas de todas as métricas do WhatsApp usadas no Braze, consulte nosso [Glossário de Métricas de Relatório][1].

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrico</th>
            <th>Definição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">Envios</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deliveries">Entregas</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#reads">Leituras</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Reads' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#failures">Falhas</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Failures' %}</td>
        </tr>
    </tbody>
</table>

#### Métricas de bloqueio e relatório do usuário final

Métricas adicionais podem ser acessadas através do [WhatsApp Manager dashboard](https://www.facebook.com/business/help/683499390267496?content_id=NZUBj7XjkYjYuWx), embora a [confirmação do seu acesso](https://www.facebook.com/business/help/218116047387456) seja necessária para acessar todos os insights disponíveis. 

{% endif %}

### Desempenho histórico

O painel de **Desempenho Histórico** permite que você visualize as métricas do painel **Desempenho de Mensagens** como um gráfico ao longo do tempo. Use os filtros na parte superior do painel para modificar as estatísticas e canais mostrados no gráfico. O intervalo de tempo deste gráfico sempre refletirá o intervalo de tempo especificado no topo da página. 

Para obter uma análise dia a dia, clique no <i class="fas fa-bars"></i> menu de hambúrguer e selecione **baixar CSV** para receber uma exportação CSV do relatório.

![Um gráfico do painel de Performance Histórica com estatísticas de exemplo para um e-mail de fevereiro de 2021 a maio de 2022.]({% image_buster /assets/img/cc-historical-performance.png %})

{% if include.channel == "in-app message" %}

{% alert note %}
Se você optar por enviar apenas para usuários que podem ver a versão mais recente do Braze das mensagens no aplicativo (Geração 3), seu **público-alvo** não se ajusta para refletir sua escolha.
{% endalert %}

{% endif %}

{% if include.channel == "SMS" %}

### Respostas de palavras-chave

O painel **Respostas de Palavras-Chave** mostra uma linha do tempo das palavras-chave recebidas com as quais os usuários responderam após receber sua mensagem.  

![Painel de Respostas de Palavras-Chave SMS/MMS em Nível de Campanha que inclui um gráfico de linha da distribuição de palavras-chave ao longo do tempo, e uma seção de Categorias de Palavras-Chave com caixas de seleção selecionadas para aceitação, Opt-Out, Ajuda, Outro, Mais e Coaching.]({% image_buster /assets/img/sms/keyword_responses.png %})

Aqui, você também pode ver a distribuição de respostas de cada categoria de palavra-chave para determinar os próximos passos para [redirecionamento]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns) e para [criar um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment).

![A tabela abaixo do gráfico de linhas que possui colunas para Categoria de Palavra-chave, Distribuição de Resposta e redirecionamento, onde você tem a opção de criar um segmento com a categoria de palavra-chave.]({% image_buster /assets/img/sms/keyword_segments.png %})

{% endif %}

### Detalhes do evento de conversão

O painel **Detalhes do evento de conversão** mostra a performance de seus eventos de conversão para sua campanha. Para saber mais, consulte [Eventos de Conversão]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/#step-3-view-results).

![O painel de Detalhes do Evento de Conversão.]({% image_buster /assets/img/cc-conversion.png %})

### Correlação de conversão

O painel de **Correlação de conversão** oferece a você insight sobre quais atributos e comportamentos dos usuários ajudam ou prejudicam os resultados que você definiu para as campanhas. Para saber mais, consulte [Correlação de conversão]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation/).

![O painel de Correlação de Conversão com uma análise sobre atributos e comportamento do usuário a partir do Evento de Conversão Primária - A.]({% image_buster /assets/img/convcorr.png %})

{% if include.channel == "whatsapp" %}

### Meta análise de dados

Além da análise de dados da Braze, a análise de dados em nível de modelo pode ser acessada no WhatsApp Business Manager. Para mais informações, consulte a [documentação do Meta](https://www.facebook.com/business/help/218116047387456). 

{% endif %}

{% if include.channel == "SMS" %}

### Eventos de Currents de SMS

Assim como e-mail, Braze recebe eventos em nível de usuário relacionados a uma mensagem SMS enquanto ela faz sua jornada até um usuário. Qualquer evento de SMS recebido também será enviado como um evento Currents através do [SMS InboundReceived]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#sms-inbound-received-events) evento. Isso permite que você execute ações adicionais ou relatórios sobre as mensagens que seus usuários estão enviando fora da plataforma Braze. 

{% alert note %}
As mensagens de entrada são truncadas após 1.600 caracteres.
{% endalert %}

{% endif %}

{% if include.channel != "whatsapp" %}

## Relatório de retenção

Os relatórios de retenção mostram as taxas em que seus usuários realizaram um evento de retenção selecionado ao longo de períodos de tempo em uma campanha específica ou canva. Para saber mais, consulte [Relatórios de retenção]({{site.baseurl}}/user_guide/data_and_analytics/reporting/retention_reports/).

## Relatório de funil

O relatório de funil oferece um relatório visual que permite analisar as jornadas que seus clientes fazem após receber uma campanha ou canva. Se sua campanha ou canva usar um grupo de controle ou múltiplas variantes, você poderá entender como as diferentes variantes impactaram o funil de conversão de forma mais granular e otimizar com base nesses dados.

Para saber mais, consulte [Relatórios de funil]({{site.baseurl}}/user_guide/data_and_analytics/reporting/funnel_reports/).

{% endif %}

[1]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/
[2]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants
