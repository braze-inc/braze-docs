---
nav_title: Uninstall Tracking
article_title: Uninstall Tracking
page_order: 6
page_type: reference
description: "Este artigo de referência aborda a implementação do rastreamento de desinstalação para estatísticas em nível de campanha e de aplicativo."
tool: Reports

---

# Desinstalar o rastreamento

> Este artigo mostra como você pode visualizar desinstalações agregadas de aplicativos ao longo do tempo para localizar tendências e anomalias e rastrear desinstalações no nível da campanha para determinar se uma campanha específica está impulsionando ou impedindo instalações de aplicativos.

O rastreamento de desinstalação na Braze fornece os seguintes detalhes:

1. Estatísticas diárias de desinstalação no nível do app em um gráfico de série temporal na página **inicial**.
2. Estatísticas de desinstalação em nível de campanha em um gráfico de série temporal na página **Detalhes da campanha** de uma campanha específica. Essa estatística especifica o número de destinatários da campanha que desinstalam a cada dia.

{% alert note %}
Você deve fazer a aceitação para desinstalar o rastreamento em seu dashboard da Braze. Esse recurso está atualmente disponível para apps no iOS, Android e Fire OS.
{% endalert %}

## Como funciona?

O Braze coleta automaticamente um nível básico de informações de desinstalação de suas campanhas push regulares. No entanto, como a frequência com que diferentes usuários recebem campanhas push pode variar, oferecemos rastreamento de desinstalação para fornecer um instantâneo mais preciso da atividade de desinstalação entre seus usuários.

## Ativação do rastreamento de desinstalação

Você pode ativar o rastreamento de desinstalação na página **Configurações do aplicativo**, em **Configurações**, para cada app que deseja rastrear.

{% alert note %}
Se estiver usando a navegação mais antiga, **Configurações do app** é **Configurações** e está localizado em **Gerenciar configurações**.
{% endalert %}

Quando o rastreamento de desinstalação estiver ativado para um app, mensagens no app em segundo plano serão enviadas todas as noites para os usuários que não tiverem registrado uma sessão ou recebido um push em 24 horas.

### Configuração

Para configurar o rastreamento de desinstalação para seu aplicativo iOS, use um [método utilitário][documentos do iOS]. Para seu aplicativo Android, use [`isUninstallTrackingPush()`][8]. Quando o Braze detectar uma desinstalação, seja por rastreamento de desinstalação ou por entrega normal de campanha push, registraremos o melhor horário estimado da desinstalação para o usuário. Esse tempo é armazenado no perfil do usuário como uma atribuição padrão e pode ser usado para definir um segmento de usuários para campanhas de recuperação.

## Filtragem de segmentos por desinstalações

O filtro **Uninstalled (Desinstalado)** na página **Segmentos** seleciona os usuários que desinstalaram seu app dentro de um intervalo de tempo. Como é difícil determinar a hora exata de uma desinstalação, recomendamos que os filtros de desinstalação tenham intervalos de tempo mais amplos para garantir que todos os que desinstalam sejam incluídos no segmento em algum momento.

![Desinstalar segmento.][5]

### Análise em nível de app

As estatísticas diárias sobre desinstalações estão na página **inicial**. O gráfico pode ser dividido por app e segmento, semelhante a outras estatísticas que a Braze fornece. Na seção **Visão geral da performance**, selecione o intervalo de datas e, se desejar, um app. Em seguida, role a tela para baixo até o gráfico **Performance Over Time** e faça o seguinte:

1. No menu suspenso **Statistics For (Estatísticas para)**, selecione **Uninstalls (Desinstalações)**.
2. No menu suspenso **Detalhamento**, selecione **Por segmento**.
3. No menu suspenso **Breakdown Values**, selecione os segmentos a serem incluídos no gráfico.

{% alert note %}
Os apps sem rastreamento de desinstalação ativado reportarão desinstalações de apenas um subconjunto de seus usuários (aqueles que foram direcionados com notificações por push), portanto, os totais diários de desinstalação podem ser maiores do que o mostrado.
{% endalert %}

![Desinstalar a seleção de gráficos.][2]

## Desinstalar o rastreamento de campanhas

O rastreamento de desinstalação de campanhas mostra o número de usuários que receberam uma campanha específica e, posteriormente, desinstalaram seu app dentro do período de tempo selecionado. Essa ferramenta fornece insight sobre como as campanhas podem estar incentivando comportamentos negativos não intencionais dos usuários e ajuda a medir a eficácia geral da campanha.

As estatísticas de desinstalação de campanhas estão localizadas em uma página específica de **análise de dados da campanha**. Para campanhas multicanais e multivariantes, as desinstalações podem ser divididas por canal e variante, respectivamente.

![Desinstale no nível da campanha.][6]

### Como funciona?

O Braze rastreia as desinstalações observando quando as mensagens push enviadas aos dispositivos dos usuários retornam um sinal do Firebase Cloud Messaging (FCM) ou do serviço de Notificações por Push da Apple (APNs) de que o app não está mais instalado. Se o Rastreamento Global de Desinstalação estiver ativado para um determinado app, enviaremos uma mensagem push silenciosa diária aos usuários para detectar se eles desinstalaram. Esse push "silencioso" é enviado a todos os usuários (a menos que o usuário tenha desativado os pushs silenciosos nas configurações do app); no entanto, o push não aparece para os usuários. Se detectarmos que um usuário desinstalou, nós:

* Aumenta a contagem total de desinstalações do app em um.
* Aumenta em um a contagem de desinstalações para cada campanha que o usuário recebeu com êxito nas últimas 24 horas.
* Se um usuário receber três campanhas em um período de 24 horas e depois desinstalar, incrementamos a contagem de "desinstalações" para todas as três campanhas.

O rastreamento de desinstalação está sujeito a restrições impostas a essas informações pela FCM e pelos APNs. O Braze só aumenta a contagem de desinstalações quando o FCM ou os APNs nos informam que um usuário desinstalou, mas esses sistemas de terceiros se reservam o direito de nos notificar sobre desinstalações a qualquer momento. Como resultado, o rastreamento de desinstalação deve ser usado para detectar tendências direcionais em vez de estatísticas precisas.

Para saber mais sobre como usar o rastreamento de desinstalação, consulte nossa postagem no blog [Rastreamento de desinstalação]: Uma análise do setor sobre seus pontos fortes e limitações][7].

## Solução de problemas

### Por que de repente estou vendo um pico de desinstalações?

Se você observar um aumento nas desinstalações de aplicativos, isso pode ser devido ao envio de mensagens do Firebase Cloud Messaging (FCM) e ao serviço de notificações por Push da Apple (APNS) que revogam tokens antigos em uma frequência diferente.

### Por que o número de desinstalações de aplicativos é diferente do que está nos APNs?

A diferença é esperada. Os APNs começarão a retornar um status 410 para esses tokens em um cronograma impreciso.

[1]: {% image_buster /assets/img_archive/Uninstall_Tracking2.png %} "Caixa de seleção Desinstalar rastreamento"
[2]: {% image_buster /assets/img_archive/Uninstall_Tracking_App2.png %} "Desinstalar a seleção do gráfico"
[4]: {% image_buster /assets/img_archive/User_Profile.png %} Desinstalar atributo
[5]: {% image_buster /assets/img_archive/Uninstall_Segment.png %} "Uninstall Segment" (Desinstalar segmento)
[6]: {% image_buster /assets/img_archive/campaign_level_uninstall_tracking.png %}
Daqui a [7]: https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/
[Documentos do iOS]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/uninstall_tracking/
Daqui a [8]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html
