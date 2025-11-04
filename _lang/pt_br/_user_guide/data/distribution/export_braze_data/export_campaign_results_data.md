---
nav_title: Exportar dados da campanha
article_title: Exportar dados da campanha
page_order: 0
page_type: reference
description: "Este artigo de referência aborda como exportar dados de resultados de campanha de campanhas únicas, multicanais ou multivariadas. O artigo também lista como exportar dados de usuário dos destinatários."
tool: 
  - Campaigns
  - Reports
  
---

# Exportar dados da campanha

> Na página **Campaigns (Campanhas** ) do painel, selecione a campanha que deseja visualizar e role para baixo até os gráficos de desempenho histórico, que podem ser exportados.<br><br>Esta página aborda como exportar dados de resultados de campanha de campanhas únicas, multicanais e multivariadas, e como exportar dados de usuário dos destinatários.

## Campanhas multicanais

Para campanhas multicanal, os dados que podem ser exportados dependem dos canais de mensagens que você usou. Aqui está uma lista de todos os dados que podem ser exportados de uma campanha que usou iOS push, Android push, e-mail e mensagens no aplicativo:

- Mensagens enviadas por data
    - Total de mensagens enviadas
    - Mensagens enviadas pelos canais da campanha (podem incluir push, e-mail e mensagem no aplicativo)
- Engajamento de mensagens de e-mail por data
    - Número de e-mails entregues
    - Número de e-mails enviados
    - Número de e-mails abertos
    - Número de cliques em e-mails
    - Número de devoluções de e-mail
    - Número de e-mails denunciados como spam
- Engajamento com mensagens no aplicativo por data
    - Número de mensagens enviadas no aplicativo
    - Impressões de mensagens no aplicativo
    - Número de cliques em mensagens no aplicativo
- Engajamento de push do iOS por data
    - Número de notificações push do iOS enviadas
    - Total de aberturas
    - Aberturas diretas
    - Saltos
- Engajamento com o Android Push por data
    - Número de notificações push do Android enviadas
    - Total de aberturas
    - Aberturas diretas
    - Saltos

## Campanhas multivariadas

Para campanhas multivariadas, que usam apenas um canal de mensagens, você pode exportar dados que mostram o desempenho de cada variante na análise do canal de mensagens específico ao longo do tempo. Você pode visualizar esses dados agrupados por estatística ou por variante de mensagem.

Os resultados da campanha push contêm gráficos para as seguintes análises:

- Mensagens enviadas por data para cada variante
- Conversões por data para cada variante
- Destinatários únicos por data para cada variante
- Aberturas por data para cada variante
- Aberturas diretas por data para cada variante
- Rejeições por data para cada variante

Os resultados da campanha de e-mail contêm gráficos para as seguintes análises:

- Número entregue por data para cada variante
- Número enviado por data para cada variante
- Aberturas por data para cada variante
- Cliques por data para cada variante
- Rejeições por data para cada variante
- Relatórios de spam por data para cada variante

Os resultados da campanha de mensagens in-app contêm gráficos para as seguintes análises:

- Enviado por data para cada variante
- Impressões por data para cada variante
- Cliques por data para cada variante

## Destinatários da campanha

É possível exportar dados de usuário para todos os destinatários de uma campanha como um arquivo CSV. Para fazer isso, selecione o botão **User Data (Dados do usuário** ) na seção **Campaign Details (Detalhes da campanha** ).

{% alert note %}
Não consegue ver o botão **Dados do usuário**? Para exportar dados do usuário, é necessário ter as [permissões]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) **Exportar dados do usuário** para esse espaço de trabalho.
{% endalert %}

dropdown User Data (Dados do usuário) na página Campaign Details (Detalhes da campanha)]({% image_buster /assets/img/campaign_export_example.png %})

A saída CSV contém dados de perfil de usuário para cada destinatário da campanha. O Braze gerará o relatório em segundo plano e o enviará por e-mail para o usuário que estiver conectado no momento.

Se você tiver vinculado suas [credenciais do Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) ao Braze, o CSV também será carregado em seu bucket do S3. Caso contrário, o link enviado por e-mail para você expirará em algumas horas.

O arquivo exportado inclui os mesmos campos de dados do usuário que são incluídos quando você [exporta dados do usuário para um segmento]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data). Além desses campos de dados, se você escolher "Exportar todos os dados do destinatário", o arquivo exportado também conterá os seguintes dados para cada usuário:

- Nome da variação da campanha recebida
- ID da API da variação da campanha recebida
- Se o usuário está no grupo de controle

{% alert tip %}
Para obter ajuda com exportações de CSV e API, consulte [Solução de problemas de exportação]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

