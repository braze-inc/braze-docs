---
nav_title: Segmentação de usuários
article_title: Segmentação de usuários
page_order: 9
page_type: reference
description: "Este artigo de referência aborda como segmentar seu público-alvo em sua campanha e nos editores do Canvas."
tool:
    - Campaigns
    - Canvas
---

# Segmentação de usuários

> Determinar como direcionar seus usuários é uma das etapas mais importantes ao criar uma campanha ou um Canvas. Ao entender como segmentar seu público-alvo com base em seus comportamentos, preferências e dados demográficos, você pode adaptar e personalizar suas mensagens.

## Criação de um público-alvo

### Etapa 1: Escolha os usuários

Em **Targeting Options (Opções de segmentação**), você pode usar as seguintes opções para escolher os usuários que deseja segmentar para sua campanha ou Canvas. Somente os usuários que corresponderem aos critérios definidos receberão a mensagem. Lembre-se de que a associação exata ao segmento é sempre calculada imediatamente antes de a mensagem ser enviada.

{% tabs local %}
{% tab single segment %}
Para direcionar membros de um segmento criado anteriormente, selecione um segmento no menu suspenso em **Target Users by Segment (Direcionar usuários por segmento**).
{% endtab %}

{% tab multiple segments %}
Para direcionar usuários que se enquadram em vários segmentos criados anteriormente, adicione vários segmentos no menu suspenso em **Target Users by Segment (Direcionar usuários por segmento**). O público-alvo resultante será composto por usuários do primeiro segmento, do segundo segmento e do terceiro segmento, etc.
{% endtab %}

{% tab multiple filters %}
Para segmentar usuários sem adicionar um segmento, você pode usar uma série de filtros. Esse é um público improvisado durante a criação da mensagem e permite que você ignore a criação de segmentos ao enviar para públicos únicos.

Filtros adicionais para uma mensagem direcionada a usuários que abriram um aplicativo pela última vez no dia, que nunca receberam uma campanha ou etapa do Canvas e que fizeram uma compra há menos de 30 dias.]({% image_buster /assets/img_archive/additional_filters.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab segments & filters %}
Também é possível direcionar usuários de um ou mais segmentos criados anteriormente que também se enquadram em filtros adicionais. Depois de selecionar seus segmentos, você pode refinar ainda mais seu público-alvo na seção **Additional Filters (Filtros adicionais** ). Isso é demonstrado na captura de tela a seguir, que tem como alvo os usuários que estão no segmento "Usuários ativos diários", no segmento "Nunca abri e-mail" e que fizeram uma compra há mais de 30 dias.

Opções de segmentação para uma mensagem que inclui dois segmentos e tem um filtro adicional para uma última compra feita há menos de 30 dias.]({% image_buster /assets/img_archive/target_segmenter.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab Specific apps %}

Você pode enviar uma mensagem de campanha ou uma etapa do Canvas para aplicativos específicos, como enviar uma mensagem no aplicativo ou uma notificação por push somente para aplicativos Android ou iOS.

No entanto, lembre-se de que é possível que um usuário use vários aplicativos. O filtro "Has app" identifica todos os usuários que têm o aplicativo selecionado, mas não controla quais aplicativos recebem mensagens. Por exemplo, se você aplicar um filtro de segmento em que "Has app" esteja definido como Android, todos os usuários que também tiverem o aplicativo iOS também receberão a mensagem em seu aplicativo iOS.

\![Um filtro para usuários que têm o aplicativo "Hello, World (Android)".]({% image_buster /assets/img_archive/has_app_hello_world.png %}){: style="max-width:60%;"}

Digamos que você queira enviar uma mensagem no aplicativo somente para aplicativos Android.

1. Crie um segmento e defina **Aplicativos e sites direcionados** a **Usuários de aplicativos específicos** e, em seguida, selecione seu aplicativo Android.

\![Um segmento direcionado a usuários de um aplicativo específico, "Test_Android".]({% image_buster /assets/img_archive/app_test_android.png %}){: style="max-width:60%;"}

{: start="2"}
2\. Em sua campanha ou Canvas, vá para a etapa **Target Audiences (Públicos-alvo** ) e confirme se o seu segmento foi adicionado na seção **Target Users By Segment (Usuários-alvo por segmento** ). 

A etapa "Target Audiences" (Públicos-alvo) com um segmento de exemplo selecionado.]({% image_buster /assets/img_archive/target_users_by_segment_example.png %})

{% alert note %}
Isso não funcionará se você adicionar seu segmento na seção **Additional Filters (Filtros adicionais** ) por meio de um filtro de associação de segmento. Você deve fazer referência direta ao seu segmento em **Target Users By Segment** para enviar sua mensagem somente para esse aplicativo.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert tip %}
Para campanhas de e-mail, você pode segmentar Seed Groups na seção **Seed Groups**. Observe que os Seed Groups não estão disponíveis para campanhas de API, embora você possa incluir Seed Groups por meio de uma entrada acionada por API em uma campanha. Para obter mais informações, consulte [Seed Groups]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#seed-groups).
{% endalert %}

### Etapa 2: Teste seu público

Depois de adicionar segmentos e filtros ao seu público, você pode testar se o público está configurado conforme o esperado, [procurando um usuário]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) para confirmar se ele corresponde aos critérios do público.

A seção "User Lookup" com um botão "Lookup User".]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

#### Resumo do público

O **Resumo do público-alvo** mostrará uma visão geral de quem está em seu público-alvo. Aqui, você pode limitar ainda mais seu público-alvo definindo um limite máximo de usuários ou [limitando a]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) velocidade de entrega.

\![A seção "Audience Summary" (Resumo do público) com opções para definir um limite máximo de usuários ou uma velocidade de entrega limitada.]({% image_buster /assets/img_archive/audience_summary.png %})

#### Teste A/B

Na seção **A/B Testing (Teste A/B** ), é possível configurar um teste para comparar as respostas dos usuários a várias versões da mesma campanha de marketing. Essas versões compartilham objetivos de marketing semelhantes, mas diferem em termos de redação e estilo. O objetivo é identificar a versão da campanha que melhor atinja suas metas de marketing. 

Para obter mais informações e práticas recomendadas, consulte [Multivariate & A/B Testing]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

#### Estatísticas de público

O Braze fornece estatísticas detalhadas do público-alvo dos canais segmentados no rodapé. Quanto maior for a sua base de usuários, maior a probabilidade de o valor de **usuários alcançáveis** ser uma estimativa aproximada. O número de usuários acessíveis pode diminuir se você usar um [Grupo de Controle Global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) ou configurar a elegibilidade de mensagens. 

- Para determinar um número exato de usuários acessíveis, selecione [Calculate exact statistics (Calcular estatísticas exatas]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics)), pois isso pesquisará todos os usuários da sua base de usuários.
- Para ver qual porcentagem da sua base de usuários está sendo direcionada ou o Lifetime Value (LTV) para esse segmento, selecione **Show Additional Statistics (Mostrar estatísticas adicionais**).

##### Por que a contagem do público-alvo pode ser diferente da contagem de usuários alcançáveis

{% multi_lang_include segments.md section='Differing audience size' %}

\![A seção "Total Population" (População total) com contagens estimadas de usuários alcançáveis em cada canal direcionado.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

{% alert note %}
O cálculo de estatísticas exatas pode levar alguns minutos para ser executado. Essa função calcula apenas as estatísticas exatas no nível do segmento, não no nível do filtro ou do grupo de filtros.<br><br>
Em segmentos grandes, é normal haver uma pequena variação, mesmo ao calcular estatísticas exatas. Espera-se que a precisão desse recurso seja de 99,999% ou mais.
{% endalert %}

## Como o público-alvo e os critérios de inscrição funcionam juntos

Quando você cria uma campanha ou Canvas no Braze, a segmentação ocorre em duas partes:

1. **Público-alvo:** Quem se qualifica
2. **Critérios de entrada:** O que aciona a entrega

A ordem é importante: O Braze verifica se alguém faz parte do público-alvo antes que os critérios de entrada sejam avaliados. Se um usuário ainda não estiver qualificado para o público-alvo naquele momento, ele não entrará na campanha ou no Canvas, mesmo que depois acione o evento de entrada. Pense no público-alvo como uma sala de espera: somente os usuários que já estiverem lá dentro quando o acionador ocorrer poderão avançar.

### Exemplo 1

Você deseja enviar uma mensagem push durante a primeira sessão de um usuário.

Você define:

- **Público-alvo:** Usuários com contagem de sessões = 0
- **Evento de entrada:** Início da sessão

Quando o usuário abre seu aplicativo, o Braze vê que a contagem de sessões dele agora é 1 e ele não se qualifica mais para o público. O evento de entrada ocorre depois que eles são elegíveis, portanto, a mensagem não será enviada.

Para que isso funcione, o usuário precisa se qualificar para o público-alvo antes do início da sessão (inverter o público-alvo e o acionador de entrada).

### Exemplo 2

Você deseja enviar um e-mail aos usuários que gastaram mais de US$ 10 nos últimos 7 dias.

Você define:

- **Público-alvo:** Usuários que gastaram mais de US$ 10 nos últimos 7 dias
- **Evento de entrada:** Qualquer compra

Agora imagine que um usuário gaste US$ 12 hoje. Isso não aciona a mensagem - apenas os torna qualificados para entrar no público. Eles não receberão o e-mail a menos que façam outra compra posteriormente.

Uma abordagem melhor seria usar um público mais amplo e transferir o filtro para os critérios de entrada:

- **Público:** Todos os usuários (ou seu público-alvo básico)
- **Evento de entrada:** Fazer uma compra
- **Filtro de entrada:** Total de gastos nos últimos 7 dias > US$ 10

Dessa forma, uma compra qualificada atende ao filtro e aciona a mensagem - não é necessária uma segunda ação.

## Práticas recomendadas

- Certifique-se de que o segmento de público-alvo inclua usuários antes da ocorrência dos critérios de entrada.
- Evite usar filtros de público que só se aplicam após o evento. Se um filtro depender de algo que acontece no momento do acionador (como "contagem de sessões = 0"), o usuário poderá não estar mais qualificado no momento em que o Braze fizer a verificação.
- Use a lógica baseada em tempo de forma ponderada. Por exemplo, se você quiser segmentar novos usuários:
    - Defina seu público-alvo como "aplicativo usado pela primeira vez nos últimos 7 dias".
    - Defina seu evento de entrada como "início da sessão".
    - Dessa forma, apenas os usuários que ainda estão na primeira semana se qualificarão e entrarão quando iniciarem uma sessão.
