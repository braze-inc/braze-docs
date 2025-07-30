---
nav_title: Exportar dados da campanha
article_title: Exportar dados da campanha
page_order: 0
page_type: reference
description: "Este artigo de referência aborda como exportar dados de resultados de campanhas de campanhas únicas, multicanais ou multivariantes. O artigo também lista como exportar dados de usuários dos destinatários."
tool: 
  - Campaigns
  - Reports
  
---

# Exportar dados da campanha

> Na página **Campaigns (Campanhas)** do dashboard, selecione a campanha que deseja visualizar e role para baixo até os gráficos de performance histórica, que podem ser exportados.<br><br>Esta página aborda como exportar dados de resultados de campanhas de campanhas únicas, multicanais e multivariantes e como exportar dados de usuários dos destinatários.

## Campanhas multicanais

Para campanhas de vários canais, os dados que podem ser exportados dependem dos canais de envio de mensagens que você usou. Aqui está uma lista de todos os dados que podem ser exportados de uma campanha que usou iOS push, Android push, e-mail e mensagens no app:

- Envio de mensagens por data
    - Total de mensagens enviadas
    - Envio de mensagens nos canais da campanha (pode incluir push, e-mail e mensagem no app)
- Engajamento com mensagens de e-mail por data
    - Número de e-mails enviados
    - Número de e-mails enviados
    - Número de e-mails abertos
    - Número de cliques em e-mails
    - Número de envios de e-mail devolvidos
    - Número de e-mails relatados como spam
- Engajamento com mensagens no app por data
    - Número de mensagens no app enviadas
    - Impressões de mensagem no app
    - Número de cliques em mensagens no app
- Engajamento de push do iOS por data
    - Número de notificações por push do iOS enviadas
    - Total de aberturas
    - Aberturas diretas
    - Bounces
- Engajamento do Android por data
    - Número de notificações por push enviadas para Android
    - Total de aberturas
    - Aberturas diretas
    - Bounces

## Campanhas multivariantes

Para campanhas multivariantes, que usam apenas um canal de envio de mensagens, é possível exportar dados que mostrem como foi a performance de cada variante nas análises do canal de envio de mensagens específico ao longo do tempo. Você pode visualizar esses dados agrupados por estatística ou por variante de mensagem.

Os resultados da campanha push contêm gráficos para as seguintes análises de dados:

- Envio de mensagens por data para cada variante
- Conversões por data para cada variante
- Destinatários únicos por data para cada variante
- Aberturas por data para cada variante
- Aberturas diretas por data para cada variante
- Bounces por data para cada variante

Os resultados da campanha de envio de e-mail contêm gráficos para as seguintes análises de dados:

- Número entregue por data para cada variante
- Número enviado por data para cada variante
- Aberturas por data para cada variante
- Cliques por data para cada variante
- Bounces por data para cada variante
- Relatórios de spam por data para cada variante

Os resultados da campanha de mensagens no app contêm gráficos para as seguintes análises de dados:

- Enviado por data para cada variante
- Impressões por data para cada variante
- Cliques por data para cada variante

## Destinatários da campanha

É possível exportar dados de usuários para todos os destinatários de uma campanha como um arquivo CSV. Para fazer isso, selecione o botão **Dados de usuários** na seção **Detalhes da campanha**.

{% alert note %}
Não consegue ver o botão **Dados de usuários**? Para **exportar dados de usuários**, é necessário ter as [permissões]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) Exportar dados de usuários para esse espaço de trabalho.
{% endalert %}

![Dados de usuários na página Detalhes da campanha]({% image_buster /assets/img/campaign_export_example.png %})

A saída CSV contém dados de perfil de usuários para cada destinatário da campanha. O Braze gerará o relatório em segundo plano e o enviará por e-mail para o usuário que estiver conectado no momento.

Se você tiver vinculado suas [credenciais do Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) ao Braze, o CSV também será feito upload em seu bucket S3. Caso contrário, o link enviado por e-mail expirará em algumas horas.

O arquivo exportado inclui os mesmos campos de dados de usuários que são incluídos quando você [exporta dados de usuários para um segmento]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data). Além desses campos de dados, se você escolher "Export All Recipient Data" (Exportar todos os dados do destinatário), o arquivo exportado também conterá os seguintes dados de cada usuário:

- Nome da variação da campanha recebida
- API ID da variação da campanha recebida
- Se o usuário está no grupo de controle

{% alert tip %}
Para obter ajuda com exportações CSV e API, consulte [Solução de problemas de exportação]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

