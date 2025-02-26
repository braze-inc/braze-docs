---
nav_title: Clarisights
article_title: Clarisights
description: "Este artigo de referência descreve a parceria entre o Braze e a Clarisights, uma plataforma de relatórios de marketing de performance de autoatendimento, permitindo que você importe dados de campanhas do Braze e do Canvas para ajudar a obter uma interface unificada de relatórios de marketing de performance e CRM/retenção."
alias: /partners/Clarisights/
page_type: partner
search_tag: Partner

---

# Clarisights

> A [Clarisights][2] é uma plataforma de relatórios de marketing de performance de autoatendimento para organizações orientadas por dados. Ela integra, processa e visualiza automaticamente todos os seus dados de fontes de marketing, analíticas e de atribuição.

A integração entre o Braze e a Clarisights permite que você importe dados de campanhas do Braze e do Canvas para ajudar a obter uma interface unificada de relatórios de marketing de performance e CRM/retenção.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Clarisights | É necessário ter um espaço de trabalho da Clarisights para usar a parceria |
| chave da API REST Braze | Uma chave da API REST do Braze com as seguintes permissões:  <br> - `campaigns.list` <br>  - `campaigns.details`<br> - `campaigns.data_series` <br> - `canvas.details`<br> - `canvas.list` <br>  - `canvas.data_series` <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST do Braze | [Seu URL do ponto de extremidade REST][1]. Seu endpoint dependerá do URL do Braze para sua instância. |
| Nome do espaço de trabalho do Braze | O nome do espaço de trabalho associado à chave de API do Braze. Esse nome será usado para identificar a integração do espaço de trabalho no Clarisights. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

Com a integração do Braze e do Clarisights, os usuários podem criar diferentes visualizações e tabelas para obter insights das campanhas que criaram. Os casos de uso populares incluem:

{% tabs %}
{% tab Melhor visibilidade %}
Melhor visibilidade das campanhas gerais e da performance das Canvas.

![Um gráfico que mostra um exemplo de melhor viabilidade na plataforma da Clarisights. Esse gráfico inclui estatísticas de aberturas de campanhas e telas, cliques, envios, conversões etc.]({{site.baseurl}}/assets/img/clarisights/overall_view.png)
{% endtab %}
{% tab Relatórios granulares %}
Relatórios granulares para campanhas e telas.

![Um gráfico que mostra relatórios granulares, como "total enviado por canal de envio" e "taxa de conversão".]({{site.baseurl}}/assets/img/clarisights/unified_dashboard.png)
{% endtab %}
{% tab Dashboards unificados %}
Dashboards unificados para CMOs e CXOs.

![Um gráfico que mostra um exemplo de dashboards unificados.]({{site.baseurl}}/assets/img/clarisights/granular_reporting.png)
{% endtab %}
{% endtabs %}

## Integração

Para sincronizar os dados da Braze com a Clarisights, crie um conector da Braze e conecte os espaços de trabalho da Braze.

1. No Clarisights, navegue até a página **Integrações**, localize o conector **Braze** e selecione **\+ Conectar**.<br>![Uma lista de conectores disponíveis no marketplace de integrações do Clarisights.][6]<br><br>
2. Em seguida, usando o fluxo de integração, conecte sua conta da Clarisights à Braze. Isso pode ser feito fornecendo sua chave da API REST da Braze, o nome do espaço de trabalho da Braze e endpoint REST da Braze.<br>![Conector de espaço de trabalho da Braze na plataforma da Clarisights. Esta página tem campos para o nome do espaço de trabalho da Braze, a chave da API REST da Braze e o endpoint REST da Braze.][7]<br><br>Antes da integração bem-sucedida, os usuários verão os espaços de trabalho conectados na mesma página.<br>![Em "Braze Accounts" (Contas Braze), você encontrará uma lista de espaços de trabalho conectados.][9]<br><br>

## Usando essa integração

Para incluir o Braze como uma fonte de dados em seus relatórios do Clarisights, navegue até **Criar novo relatório**. Dê um nome ao seu relatório e selecione o **Braze** como fonte de dados no prompt que aparece. Você também pode escolher as métricas e dimensões a serem incluídas no relatório. Quando concluído, selecione **Criar relatório**. 

Os dados do Braze começarão a fluir a partir do momento da próxima importação de dados programada. Entre em contato com o gerente de sucesso do cliente da Clarisights para solicitar provisionamentos para durações mais longas. 

![Configurações de relatório da Clarisights mostrando campos para nome e fonte de dados. Para este exemplo, a Braze é selecionada como a fonte de dados.][8]

Visite o Clarisights para saber mais sobre as [métricas e dimensões][10] disponíveis ou sobre [a criação de relatórios][11].

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://clarisights.com
[3]: {{site.baseurl}}/assets/img/clarisights/overall_view.png
[4]: {{site.baseurl}}/assets/img/clarisights/unified_dashboard.png
[5]: {{site.baseurl}}/assets/img/clarisights/granular_reporting.png
[6]: {{site.baseurl}}/assets/img/clarisights/integrations.png
[7]: {{site.baseurl}}/assets/img/clarisights/braze_flow.png
[8]: {{site.baseurl}}/assets/img/clarisights/braze_report.png
[9]: {{site.baseurl}}/assets/img/clarisights/connected.png
[10]: https://help.clarisights.com/en/articles/5670864-braze-metrics-and-dimensions
[11]: https://help.clarisights.com/en/articles/1421478-creating-a-report-using-clarisights
