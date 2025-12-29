---
nav_title: Exportar análises de uso
article_title: Exportar análises de uso
page_order: 3

page_type: reference
description: "Este artigo de referência aborda como exportar dados de uso de aplicativos de alto nível."
tool: 
  - Reports

---

# Exportação de análises de uso

> Esta página abrange a página **inicial** do painel, que contém dados de alto nível de uso do aplicativo, bem como estatísticas detalhadas de diferentes KPIs por data.

Para exportar CSVs de dados dessa página:

1. Defina o período de tempo e os aplicativos para os quais você deseja visualizar os dados. Por padrão, o painel mostra os últimos 30 dias de dados de todos os aplicativos.

Período de tempo e campos de aplicativos no painel inicial.]({% image_buster /assets/img_archive/home_dashboard_select_date.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Role para baixo até o gráfico **Performance Over Time (Desempenho ao longo do tempo** ).
3\. Selecione os dados que você gostaria de exportar no campo **Statistics For (Estatísticas para** ). Veja os [dados disponíveis](#available-data) para você exportar.

Gráfico de desempenho ao longo do tempo no painel inicial.]({% image_buster /assets/img_archive/home_dashboard_export.png %})

{:start="4"}
4\. Selecionar <i class="fas fa-bars" title="Menu de contexto do gráfico"></i> e, em seguida, selecione sua opção de exportação.

## Dados disponíveis

Você pode exportar CSVs com os seguintes dados:

- Contagem de sessões por data
    - (Opcional) Contagem de sessões para diferentes segmentos
    - (Opcional) Contagem de sessões para diferentes versões de aplicativos
- DAUs por data
    - (Opcional) DAUs para diferentes segmentos
- Estatísticas de e-mail por data
    - Número de e-mails enviados
    - Número de e-mails entregues
    - Número de e-mails abertos
    - Número de cliques em e-mails
    - Número de devoluções de e-mail
    - Número de e-mails denunciados como spam
- Mensagens no aplicativo por data
    - Número de mensagens enviadas no aplicativo
    - Impressões de mensagens no aplicativo
    - Número de mensagens no aplicativo abertas
- MAUs por data
- Número de novos usuários por data
- Notificações push por data
    - (Opcional) Notificações por push para diferentes plataformas de aplicativos
    - Número de notificações push enviadas
    - Total de aberturas
    - Aberturas diretas
    - Saltos
- Contagem de sessões por hora
- Contagem de sessões por MAU por data
- Aderência por data

{% alert tip %}
Para obter ajuda com exportações CSV e API, visite nosso artigo [de solução de problemas de exportação]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

