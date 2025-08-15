---
nav_title: Exportar análises de dados de uso
article_title: Exportar análises de dados de uso
page_order: 3

page_type: reference
description: "Este artigo de referência aborda como exportar dados de uso do app de alto nível."
tool: 
  - Reports

---

# Exportação de análises de dados de uso

> Esta página cobre a página **inicial** do dashboard, que contém dados de alto nível de uso do app, bem como estatísticas detalhadas de diferentes KPIs por data.

Para exportar CSVs de dados dessa página:

1. Defina o período de tempo e os apps para os quais deseja visualizar os dados. Por padrão, o dashboard mostra os últimos 30 dias de dados de todos os aplicativos.

![Período de tempo e campos de app no dashboard inicial.]({% image_buster /assets/img_archive/home_dashboard_select_date.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Role a tela para baixo até o gráfico **Performance Over Time (Desempenho ao longo do tempo** ).
3\. Selecione os dados que você gostaria de exportar no campo **Statistics For (Estatísticas para** ). Veja os [dados disponíveis](#available-data) para você exportar.

![Gráfico de performance ao longo do tempo no dashboard inicial.]({% image_buster /assets/img_archive/home_dashboard_export.png %})

{:start="4"}
4\. Selecionar <i class="fas fa-bars" title="Menu de contexto do gráfico"></i> e, em seguida, selecione sua opção de exportação.

## Dados disponíveis

Você pode exportar CSVs com os seguintes dados:

- Contagem de sessões por data
    - (Opcional) Contagem de sessões para diferentes segmentos
    - (Opcional) Contagem de sessões para diferentes versões do app
- DAUs por data
    - (Opcional) DAUs para diferentes segmentos
- Estatísticas de envio de e-mail por data
    - Número de e-mails enviados
    - Número de e-mails enviados
    - Número de e-mails abertos
    - Número de cliques em e-mails
    - Número de envios de e-mail devolvidos
    - Número de e-mails relatados como spam
- Envio de mensagens no app por data
    - Número de mensagens no app enviadas
    - Impressões de mensagem no app
    - Número de mensagens no app abertas
- MAUs por data
- Número de novos usuários por data
- Notificações por push por data
    - (Opcional) Notificações por push para diferentes plataformas de app
    - Número de notificações por push enviadas
    - Total de aberturas
    - Aberturas diretas
    - Bounces
- Contagem de sessões por hora
- Contagem de sessões por MAU por data
- Aderência por data

{% alert tip %}
Para obter ajuda com exportações CSV e API, visite nosso artigo [de solução de problemas de exportação]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

