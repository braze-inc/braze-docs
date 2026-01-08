---
nav_title: Desinstalar rastreamento
article_title: Desinstalar Rastreamento
page_order: 6
page_type: reference
description: "Este artigo de referência cobre a implementação do rastreamento de desinstalação para estatísticas em nível de campanha e em nível de aplicativo."
tool: Reports

---

# Desinstalar rastreamento

> Este artigo mostra como você pode visualizar desinstalações agregadas de aplicativos ao longo do tempo para localizar tendências e anomalias, e rastrear desinstalações em nível de campanha para determinar se uma campanha específica está impulsionando ou impedindo instalações de aplicativos.

O rastreamento de desinstalação no Braze fornece os seguintes detalhes:

1. Estatísticas diárias de desinstalação em nível de aplicativo em um gráfico de série temporal na página **Início**.
2. Estatísticas de desinstalação em nível de campanha em um gráfico de série temporal na página **Detalhes da Campanha** de uma campanha específica. Esta estatística especifica o número de destinatários da campanha que desinstalam a cada dia.

{% alert note %}
Você deve optar por participar do rastreamento de desinstalação no seu painel do Braze. Este recurso está atualmente disponível para aplicativos no iOS, Android e Fire OS.
{% endalert %}

## Como funciona

O Braze coleta automaticamente um nível básico de informações sobre desinstalação de suas campanhas de push regulares. No entanto, como a frequência com que diferentes usuários recebem campanhas de push pode variar, oferecemos rastreamento de desinstalação para fornecer uma visão mais precisa da atividade de desinstalação entre seus usuários.

## Ativando o rastreamento de desinstalação

Você pode ativar o rastreamento de desinstalação na página **Configurações do App**, em **Configurações**, para cada aplicativo que deseja rastrear.

Quando o rastreamento de desinstalação está ativado para um aplicativo, mensagens de push em segundo plano serão enviadas todas as noites para usuários que não registraram uma sessão ou não receberam um push nas últimas 24 horas.

### Configuração

Para configurar o rastreamento de desinstalação para seu aplicativo iOS, use um [método utilitário]({{site.baseurl}}/developer_guide/analytics/tracking_uninstalls/?sdktab=swift). Para o seu aplicativo Android, use [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html). Quando a Braze detecta uma desinstalação, seja por rastreamento de desinstalação ou entrega normal de campanha de push, registraremos o melhor tempo estimado da desinstalação do usuário. Esse tempo é armazenado no perfil do usuário como um atributo padrão e pode ser usado para definir um segmento de usuários para campanhas de recuperação.

## Filtrando segmentos por desinstalações

O filtro **Desinstalado** seleciona usuários que desinstalaram seu aplicativo dentro de um intervalo de tempo. Como é difícil determinar o tempo exato de uma desinstalação, recomendamos que os filtros de desinstalação tenham intervalos de tempo mais amplos para garantir que todos que desinstalam se enquadrem no segmento em algum momento.

Estatísticas diárias sobre desinstalações estão na página **Início**. 

\![Segmento de desinstalação.]({% image_buster /assets/img_archive/Uninstall_Segment.png %} "Uninstall Segment")

O gráfico pode ser dividido por aplicativo e segmento, semelhante a outras estatísticas que a Braze fornece. Na seção **Visão geral de desempenho**, selecione seu intervalo de datas e, se desejar, um aplicativo. Em seguida, role para baixo até o gráfico **Desempenho ao longo do tempo** e faça o seguinte:

1. No dropdown **Estatísticas para**, selecione **Desinstalações**.
2. No dropdown **Divisão**, selecione **Por segmento**.
3. No dropdown **Valores de divisão**, selecione os segmentos a serem incluídos no gráfico.

{% alert note %}
Aplicativos sem rastreamento de desinstalação habilitado relatarão desinstalações apenas de um subconjunto de seus usuários (aqueles que foram segmentados com notificações push), portanto, os totais diários de desinstalações podem ser maiores do que o mostrado.
{% endalert %}

## Rastreamento de desinstalação para campanhas

O rastreamento de desinstalação de campanhas mostra o número de usuários que receberam uma campanha específica e, subsequentemente, desinstalaram seu aplicativo dentro do intervalo de tempo selecionado. Esta ferramenta fornece insights sobre como as campanhas podem estar incentivando comportamentos negativos indesejados dos usuários e ajuda a medir a eficácia geral da campanha.

As estatísticas de desinstalação para campanhas estão localizadas na página **Análise da Campanha** de uma campanha específica. Para campanhas multicanal e multivariadas, as desinstalações podem ser divididas por canal e variante, respectivamente.

\![Desinstalar no nível da campanha.]({% image_buster /assets/img_archive/campaign_level_uninstall_tracking.png %})

### Como funciona

A Braze rastreia desinstalações observando quando mensagens push enviadas para os dispositivos dos usuários retornam um sinal do Firebase Cloud Messaging (FCM) ou do Apple Push Notification Service (APNs) de que o aplicativo não está mais instalado. Se o Rastreamento Global de Desinstalação estiver ativado para um aplicativo específico, enviamos uma mensagem push silenciosa diária para os usuários para detectar se eles desinstalaram. Esse push "silencioso" é enviado a todos os usuários (a menos que o usuário tenha desativado os pushes silenciosos nas configurações do aplicativo); no entanto, o push não aparece para os usuários. Se detectarmos que um usuário desinstalou, nós:

* Incrementamos a contagem total de desinstalações do aplicativo em um.
* Incrementamos a contagem de desinstalações para cada campanha que o usuário recebeu com sucesso nas últimas 24 horas em um.
* Se um usuário recebe três campanhas em um período de 24 horas e depois desinstala, incrementamos a contagem de "desinstalações" para todas as três campanhas.

O rastreamento de desinstalações está sujeito a restrições impostas a essas informações pelo FCM e APNs. A Braze só incrementa a contagem de desinstalações quando o FCM ou APNs nos informam que um usuário desinstalou, mas esses sistemas de terceiros reservam o direito de nos notificar sobre desinstalações a qualquer momento. Como resultado, o rastreamento de desinstalações deve ser usado para detectar tendências direcionais em vez de estatísticas precisas.

Para mais informações sobre como usar o rastreamento de desinstalações, veja nosso post no blog [Rastreamento de Desinstalações: Uma Análise da Indústria sobre suas Forças e Limitações](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/).

## Solução de Problemas

### Por que estou vendo de repente um aumento nas desinstalações?

Se você notar um aumento nas desinstalações do aplicativo, pode ser devido ao Firebase Cloud Messaging (FCM) e ao Apple Push Notification Service (APNS) revogando tokens antigos com uma frequência diferente.

{% alert note %}
Por razões de privacidade, os provedores de push da Braze podem revogar tokens em intervalos irregulares, o que significa que as contagens de desinstalações podem, às vezes, aumentar em um determinado período de tempo.<br><br>Para validar essas mudanças, monitore o rastreamento de desinstalações juntamente com uma métrica de ação do usuário, como a taxa de abertura de push direto. Se as desinstalações aumentarem acentuadamente, mas as aberturas de push direto permanecerem estáveis, o aumento provavelmente reflete um parceiro revogando tokens antigos em vez de um comportamento real do usuário.
{% endalert %}

### Por que o número de desinstalações do aplicativo é diferente do que está no APNs?

A diferença é esperada. 

A Apple usa um cronograma aleatório para atrasar o relatório quando um token de push se torna inválido, o que significa que mesmo após um usuário desinstalar um aplicativo, o APNs pode continuar a retornar respostas bem-sucedidas para notificações push por um período de tempo. Esse atraso é intencional e projetado para proteger a privacidade do usuário. Nenhum retorno ou falha será relatado até que o APNs retorne um status `410` para um token inválido.

