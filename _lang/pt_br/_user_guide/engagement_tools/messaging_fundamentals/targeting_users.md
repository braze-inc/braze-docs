---
nav_title: Direcionamento de usuários
article_title: Direcionamento de usuários
page_order: 9
page_type: reference
description: "Este artigo de referência aborda como fazer o direcionamento para o público em sua campanha e para os editores do Canva."
tool:
    - Campaigns
    - Canvas
---

# Direcionamento de usuários

> Determinar como direcionar seus usuários é uma das etapas mais cruciais ao criar uma campanha ou um Canva. Ao entender como segmentar seu público com base em seus comportamentos, preferências e dados demográficos, você pode adaptar e personalizar seu envio de mensagens.

## Criação de um público-alvo

### Etapa 1: Escolha os usuários

Em **Opções de direcionamento**, você pode usar as seguintes opções para escolher os usuários que deseja direcionar para sua campanha ou Canva. Somente os usuários que corresponderem aos critérios definidos receberão a mensagem. Lembre-se de que a associação exata ao segmento de mensagens é sempre calculada imediatamente antes do envio da mensagem.

{% tabs local %}
{% tab segmento único %}
Para direcionar os membros de um segmento criado anteriormente, selecione um segmento no menu suspenso em **Target Users by Segment (Direcionar usuários por segmento**).
{% endtab %}

{% tab vários segmentos %}
Para direcionar usuários que se enquadram em vários segmentos criados anteriormente, adicione vários segmentos no menu suspenso em **Target Users by Segment (Direcionar usuários por segmento**). O público-alvo resultante será composto por usuários do primeiro, do segundo e do terceiro segmento, etc.
{% endtab %}

{% tab vários filtros %}
Para direcionar usuários sem adicionar um segmento, é possível usar diversos filtros. Esse é um público improvisado durante a criação da mensagem e permite que você ignore a criação de segmentos ao enviar para públicos únicos.

![Filtros adicionais para uma mensagem direcionada a usuários que abriram um app pela última vez em um dia, que nunca receberam uma campanha ou etapa do Canva e que fizeram uma compra há menos de 30 dias.]({% image_buster /assets/img_archive/additional_filters.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab segmentos e filtros %}
Também é possível direcionar usuários de um ou mais segmentos criados anteriormente que também se enquadram em filtros adicionais. Depois de selecionar seus segmentos, você pode refinar ainda mais seu público na seção **Additional Filters (Filtros adicionais** ). Isso é demonstrado na captura de tela a seguir, que direciona os usuários que estão no segmento "Usuários ativos diários", no segmento "Nunca abri e-mail" e que fizeram uma compra há mais de 30 dias.

![Opções de direcionamento para uma mensagem que inclui dois segmentos e tem um filtro adicional para uma última compra feita há menos de 30 dias.]({% image_buster /assets/img_archive/target_segmenter.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab Aplicativos específicos %}

Você pode enviar uma mensagem de campanha ou uma etapa do Canva para aplicativos específicos, como enviar uma mensagem no app ou uma notificação por push somente para aplicativos Android ou iOS.

No entanto, lembre-se de que é possível que um usuário use vários apps. O filtro "Has app" identifica todos os usuários que têm o aplicativo selecionado, mas não controla quais aplicativos recebem mensagens. Por exemplo, se você aplicar um filtro de segmento em que "Has app" esteja definido como Android, todos os usuários que também tiverem o aplicativo iOS também receberão a mensagem no app iOS.

![Um filtro para usuários que têm o app "Hello, World (Android)".]({% image_buster /assets/img_archive/has_app_hello_world.png %}){: style="max-width:60%;"}

Digamos que você queira enviar uma mensagem no app somente para aplicativos Android.

1. Crie um segmento e defina **aplicativos e sites direcionados** a **usuários de aplicativos específicos** e, em seguida, selecione seu aplicativo Android.

![Um segmento direcionado a usuários de um app específico, "Test_Android".]({% image_buster /assets/img_archive/app_test_android.png %}){: style="max-width:60%;"}

{: start="2"}
2\. Em sua campanha ou Canva, vá para a etapa de **públicos-alvo** e confirme se o seu segmento foi adicionado na seção **Usuários-alvo por segmento**. 

![A etapa "Direcionamento ao público" com um exemplo de segmento selecionado.]({% image_buster /assets/img_archive/target_users_by_segment_example.png %})

{% alert note %}
Isso não funcionará se você adicionar seu segmento na seção **Additional Filters (Filtros adicionais** ) por meio de um filtro de associação de segmento. Você deve fazer referência direta ao seu segmento em **Target Users By Segment** para entregar sua mensagem somente a esse app.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert tip %}
Para campanhas de e-mail, é possível direcionar os grupos de teste na seção **Grupos de teste**. Observe que os grupos de teste não estão disponíveis para campanhas de API, embora seja possível incluir grupos de teste por meio de uma entrada disparada pela API em uma campanha. Para saber mais, consulte [Grupos de teste]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#seed-groups).
{% endalert %}

### Etapa 2: Teste seu público

Depois de adicionar segmentos e filtros ao seu público, é possível testar se o público está configurado conforme o esperado, [procurando um usuário]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) para confirmar se ele corresponde aos critérios do público.

![A seção "User Lookup" com um botão "Lookup User".]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

#### Resumo do público

O **Resumo do público** mostrará uma visão geral de quem está em seu público-alvo. Aqui, é possível limitar ainda mais o público definindo um limite máximo de usuários ou [limitando a]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) velocidade de entrega.

![A seção "Audience Summary" (Resumo do público) com opções para definir um limite máximo de usuários ou um limite de frequência de velocidade de entrega.]({% image_buster /assets/img_archive/audience_summary.png %})

#### Testes A/B

Na seção **Testes A/B**, é possível configurar um teste para comparar as respostas dos usuários a várias versões da mesma campanha de marketing. Essas versões compartilham objetivos de marketing semelhantes, mas diferem em termos de redação e estilo. O objetivo é identificar a versão da campanha que melhor atinja suas metas de marketing. 

Para saber mais e conhecer as práticas recomendadas, consulte [Testes multivariantes e Testes A/B.]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)

#### Estatísticas do público

O Braze fornece estatísticas detalhadas do público dos canais direcionados no rodapé. Quanto maior for a sua base de usuários, maior a probabilidade de o valor de **usuários alcançáveis** ser uma estimativa aproximada. O número de usuários acessíveis pode diminuir se você usar um [grupo de controle global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) ou configurar a elegibilidade de mensagens. 

- Para determinar um número exato de usuários acessíveis, selecione [Calculate exact statistics (Calcular estatísticas exatas]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics)), pois isso pesquisará todos os usuários da sua base de usuários.
- Para ver qual porcentagem da sua base de usuários está sendo direcionada ou o valor do tempo de vida (LTV) desse segmento, selecione **Show Additional Statistics (Mostrar estatísticas adicionais)**.
- Para ver qual porcentagem da sua base de usuários está sendo direcionada ou o valor do tempo de vida (LTV) desse segmento, selecione **Show Additional Statistics (Mostrar estatísticas adicionais)**.

##### Por que a contagem do público-alvo pode ser diferente da contagem de usuários alcançáveis

{% multi_lang_include segments.md section='Diferentes tamanhos de público' %}

![A seção "Total Population" (População total) com contagens estimadas de usuários alcançáveis em cada canal direcionado.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

{% alert note %}
O cálculo de estatísticas exatas pode levar alguns minutos para ser executado. Essa função calcula apenas as estatísticas exatas no nível do segmento, não no nível do filtro ou do grupo de filtros.<br><br>
Em segmentos grandes, é normal haver uma pequena variação, mesmo ao calcular estatísticas exatas. Espera-se que a precisão desse recurso seja de 99,999% ou mais.
{% endalert %}

