---
nav_title: Alertas
article_title: Boas práticas para alertas
description: "Informações, diretrizes e exemplos para os tipos de alerta usados na documentação da Braze."
page_order: 2
noindex: true
---

# Boas práticas para alertas

> Este documento contém informações, diretrizes gerais e exemplos para os tipos de alerta usados na documentação da Braze.

## Tipos de alerta {#alert-types}

Os alertas categorizam informações que devem ser do conhecimento do leitor. Existem quatro tipos de alerta que podem ser usados na nossa documentação:

* Importante  
* Nota  
* Dica  
* Aviso

## Quando usar um alerta {#when-to-use-an-alert}

Use alertas para chamar a atenção do leitor para informações importantes. Mantenha o conteúdo curto e direto ao ponto. Queremos garantir que a informação fique na memória do leitor.

Consulte a tabela a seguir para ver as definições de cada alerta:

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<colgroup><col style="width: 20%;"><col style="width: 80%;"></colgroup>
<thead>
<tr><th>Tipo de alerta</th><th>Definição</th></tr>
</thead>
<tbody>
<tr><td>Importante</td><td>Inclui informações essenciais que <strong>devem</strong> ser observadas pelo leitor, como: <ul><li>Recursos descontinuados</li><li>Impactos na cobrança</li><li>Informações referentes a atualizações relevantes</li><li>Ressalvas urgentes sobre recursos (ex.: recursos em beta)</li><li>Outras informações importantes</li></ul></td></tr>
<tr><td>Nota</td><td>Inclui informações pontuais que o leitor deve conhecer, como: <ul><li>Ressalvas sobre recursos</li><li>Orientações de formatação</li><li>Destaques úteis</li><li>Informações rebaixadas de um alerta Importante devido à redução da gravidade do conteúdo (ex.: um alerta importante de longa data sendo convertido em uma nota padrão)</li></ul></td></tr>
<tr><td>Dica</td><td>Inclui conhecimento complementar e recomendações para o leitor, como: <ul><li>Artigos adicionais de solução de problemas</li><li>Etapas e atalhos que ajudam a aumentar a usabilidade (ex.: personalização adicional para mensagens no app)</li></ul></td></tr>
<tr><td>Aviso</td><td>Inclui informações essenciais que o leitor deve observar obrigatoriamente e pode incluir: <ul><li>Consequências irreversíveis (ex.: exclusão de campanhas e Canvas)</li><li>Comportamento que quebra o recurso</li><li>Perda de dados</li><li>Outros avisos cruciais</li></ul></td></tr>
</tbody>
</table>
{:/}

**Boas práticas para alertas**  
Aqui estão diretrizes gerais e boas práticas para alertas.

Como regra geral, evite usar alertas para conteúdo essencial à estrutura do artigo (como introduções de recursos, instruções de configuração e etapas para usar um recurso). Em caso de dúvida, consulte a equipe durante a revisão por pares.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<colgroup><col style="width: 50%;"><col style="width: 50%;"></colgroup>
<thead>
<tr><th>Diretriz</th><th>Exemplo</th></tr>
</thead>
<tbody>
<tr><td>Explique a informação no alerta de forma clara e concisa.</td><td>{% multi_lang_include alerts/note_alerts.md alert='Segment profiles first app use' %}<br><br> <a href="{{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment">Alerta de nota na Etapa 4: Seção Adicionar filtros ao seu segmento</a></td></tr>
<tr><td>Para alertas que se aplicam a diferentes seções do mesmo artigo, considere criar uma nova seção que capture esses detalhes para evitar conteúdo repetitivo.</td><td>{% multi_lang_include currents/property_details_dispatch_state_source.md %}<br><br> <a href="{{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#subscription-group-state-change-events">Informações de propriedade em Eventos de engajamento com mensagem</a></td></tr>
<tr><td>Separe as informações em parágrafos curtos ou listas dentro do alerta.</td><td>{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}<br><br> <a href="{{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/import_your_email_list/">Alerta importante em Importar sua lista de e-mails</a></td></tr>
<tr><td>Considere qualquer formatação adicional que possa impactar a exibição do alerta (trechos de código, etapas, imagens ao redor e mais).</td><td>{% multi_lang_include alerts/tip_alerts.md alert='catalog data images' %}<br><br> <a href="{{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/#considerations">Alerta de dica com trecho de código em Notificações de queda de preço</a></td></tr>
<tr><td>Inclua uma quebra de linha para alertas que iniciam um artigo.</td><td><img src="{% image_buster /assets/img/contributing/style_guide/alert_5.png %}" alt="Exemplo de um alerta iniciando um artigo."><br><br> <a href="{{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/implementation_guide/">Guia de implementação de cartões de conteúdo</a></td></tr>
<tr><td>Ao escrever sobre recursos em beta, inclua um alerta Importante que destaque o status de beta e as informações de contato da Braze. Posicione esse alerta de beta após o texto de visão geral e antes do primeiro título principal.</td><td><img src="{% image_buster /assets/img/contributing/style_guide/alert_6.png %}" alt="Exemplo de um alerta importante para um recurso em beta."></td></tr>
<tr><td>Evite usar dois ou mais alertas em sequência, se possível. Em vez disso, reorganize ou inclua a informação como parte do texto.</td><td><img src="{% image_buster /assets/img/contributing/style_guide/alert_7.png %}" alt="Um exemplo de dois alertas lado a lado, o que deve ser evitado."></td></tr>
<tr><td>Se o seu alerta estiver extenso, considere criar uma nova seção que inclua as informações como uma lista. Por exemplo, em vez de incluir etapas de solução de problemas em um alerta, considere criar uma seção de solução de problemas ou fornecer um link para um artigo relacionado.</td><td><img src="{% image_buster /assets/img/contributing/style_guide/alert_8.png %}" alt="Exemplo de uma nova seção de conteúdo."></td></tr>
</tbody>
</table>
{:/}

## Exemplos de alertas {#alert-examples}

Consulte os exemplos a seguir para entender como e por que cada tipo de alerta é usado na nossa documentação.

### Alerta importante {#important-alert}

{% multi_lang_include alerts/important_alerts.md alert='Web push private browsing' %}

* **Artigo:** [Push para a web]({{site.baseurl}}/user_guide/message_building_by_channel/push/web/)
* **Caso de uso:** Inclui ressalva essencial sobre o recurso que o leitor deve conhecer ao configurar seu push para a web.
* **Justificativa do alerta:** Use um alerta Importante em vez de um alerta de Nota porque a importância do conteúdo é maior para o leitor ao configurar seu push para a web.

{% multi_lang_include alerts/important_alerts.md alert='BCC address billable emails' %}

* **Artigo:** [Configurações de e-mail]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/)
* **Caso de uso:**
  - Fornece ressalva importante sobre a possibilidade de dobrar os e-mails faturáveis
  - Redireciona o leitor para entrar em contato com seu gerente de sucesso do cliente conforme necessário
* **Justificativa do alerta:** O alerta Importante é usado aqui para comunicar detalhes sobre os endereços de CCO nas configurações de e-mail. Essa informação é melhor apresentada usando um alerta Importante em vez de um alerta de Aviso porque omitir essa informação não impacta o recurso de forma irreversível (como quebra do recurso ou perda permanente de dados).

{% multi_lang_include alerts/important_alerts.md alert='Android notification priority' %}

* **Artigo:** [Configurações avançadas de campanha]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#notification-display-priority)
* **Caso de uso:** Inclui ressalva urgente sobre a Prioridade de Notificação. Redireciona o leitor para novas informações disponíveis.
* **Justificativa do alerta:** O alerta Importante é mais adequado aqui para redirecionar o leitor para informações atualizadas e destacar que a seção se aplica apenas a determinados usuários. Ele também é posicionado após o título da seção, o que obriga o usuário a observar o alerta importante antes de ler o restante da seção.

### Alerta de nota {#note-alert}

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

* **Artigo:** [Criar um cartão de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/)
* **Caso de uso:** Inclui informações adicionais que o leitor deve conhecer ao aprender mais sobre Cartões de conteúdo.
* **Justificativa do alerta:** Este alerta de Nota fornece informações de contexto sobre como a Braze faz a rotação de Cartões de conteúdo mais antigos para os usuários. Essa é uma informação complementar e útil para o leitor e não requer o uso de um alerta Importante ou de Dica.

{% multi_lang_include alerts/note_alerts.md alert='Custom Attributes time attribute' %}

* **Artigo:** [Atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/)
* **Caso de uso:** Inclui informações gerais que o leitor deve conhecer. Fornece um artigo para saber mais sobre conteúdo relacionado (atributos de tempo).
* **Justificativa do alerta:** Essa informação é melhor transmitida usando um alerta de Nota em vez de um alerta Importante porque o conteúdo visa fornecer informações gerais. Desconsiderar essa informação não impactaria a facilidade de uso do recurso.

{% multi_lang_include alerts/note_alerts.md alert='Manage custom data storage' %}

* **Artigo:** [Gerenciar dados personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/#managing-properties)
* **Caso de uso:** Inclui informações gerais que o leitor deve conhecer. Redireciona para o contato da Braze para mais informações.
* **Justificativa do alerta:** Este alerta de Nota fornece informações adicionais sobre armazenamento de dados que seriam úteis para o leitor ao gerenciar seus atributos personalizados. No entanto, o conteúdo não requer uma indicação mais forte de importância para o leitor, então um alerta de Nota é aceitável aqui.

### Alerta de dica {#tip-alert}

{% multi_lang_include alerts/tip_alerts.md alert='SMS segment calculator' %}

* **Artigo:** [Calculadoras de cobrança de SMS e RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/)
* **Caso de uso:** Inclui uma ferramenta para o leitor entender o comprimento da mensagem e a contagem de segmentos de SMS. Fornece informações que podem ser úteis para o leitor na compreensão dos limites de texto.
* **Justificativa do alerta:** Este é um alerta de Dica extenso porque fornece um espaço para inserir o texto e ver quantos segmentos uma mensagem envia. O alerta de Dica é a melhor opção aqui porque é um gerador útil para o leitor usar no processo de configuração de suas mensagens SMS.

{% multi_lang_include alerts/tip_alerts.md alert='Export troubleshooting' %}

* **Artigo:** [Exportar KPIs de desinstalações diárias do app por data]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/)
* **Caso de uso:** Fornece orientações de solução de problemas ao usar este endpoint.
* **Justificativa do alerta:** O alerta de Dica fornece suporte adicional para o leitor. Use um alerta de Dica em vez de um alerta de Nota porque o foco do conteúdo é auxiliar o leitor fornecendo o artigo de solução de problemas.

### Alerta de aviso {#warning-alert}

{% multi_lang_include alerts/warning_alerts.md alert='User profile external_id' %}

* **Artigo:** [Ciclo de vida do perfil de usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/)
* **Caso de uso:** Indica algo que o leitor não deve fazer ao criar seus perfis de usuário na Braze.
* **Justificativa do alerta:** O alerta de Aviso é usado para alertar o leitor contra atribuir um external_id antes de identificá-lo de forma única. Essa informação é melhor transmitida usando um alerta de Aviso em vez de um alerta Importante porque inclui consequências irreversíveis para o perfil de usuário.

{% multi_lang_include alerts/warning_alerts.md alert='Segment Currents multiple connectors' %}

* **Artigo:** [Segment para Currents]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents/)
* **Caso de uso:** Alerta o leitor ao criar conectores de Currents. Inclui a consequência de criar esses conectores incorretamente.
* **Justificativa do alerta:** O alerta de Aviso é mais adequado aqui para descrever as limitações da integração Braze Segment Currents. Use um alerta de Aviso em vez de um alerta Importante porque criar mais de um conector de Currents igual incorretamente pode resultar em perda de dados.

{% multi_lang_include alerts/warning_alerts.md alert='Canvas race condition audience trigger' %}

* **Artigo:** [Criar um Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
* **Caso de uso:** Lista as informações que podem fazer com que o recurso não funcione. Detalha como o público pretendido pode não receber a campanha ou entrar no Canvas.
* **Justificativa do alerta:** O alerta de Aviso é usado aqui para observar como o recurso pode funcionar incorretamente. Essa informação é melhor transmitida usando um alerta de Aviso em vez de um alerta Importante porque a informação é crítica e pode resultar na quebra da entrega do Canvas.