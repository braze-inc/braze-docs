---
nav_title: Usuários-alvo
article_title: Usuários-alvo
page_order: 12
page_type: reference
description: "Este artigo de referência cobre como segmentar seu público em sua campanha e editores do Canva."
tool:
    - Campaigns
    - Canvas
---

# Usuários-alvo

> Determinar como direcionar seus usuários é um dos passos mais cruciais ao criar uma campanha ou Canva. Ao entender como segmentar seu público com base em seus comportamentos, preferências e demografia, você pode personalizar e adaptar seu envio de mensagens.

## Criando um público-alvo

### Etapa 1: Escolher usuários

Em **Opções de Direcionamento**, você pode usar as seguintes opções para escolher quais usuários você gostaria de direcionar para sua campanha ou Canva. Apenas os usuários que correspondem aos seus critérios definidos receberão a mensagem. Lembre-se de que a associação exata ao segmento de mensagens é sempre calculada imediatamente antes do envio da mensagem.

{% tabs local %}
{% tab single segment %}
Para direcionar os membros de um segmento criado anteriormente, selecione um segmento no menu suspenso em **Target Users by Segment (Direcionar usuários por segmento**).
{% endtab %}

{% tab multiple segments %}
Para direcionar usuários que se enquadram em vários segmentos criados anteriormente, adicione vários segmentos no menu suspenso em **Target Users by Segment (Direcionar usuários por segmento**). O público-alvo resultante será composto por usuários do primeiro, do segundo e do terceiro segmento, etc.
{% endtab %}

{% tab multiple filters %}
Para direcionar usuários sem adicionar um segmento, é possível usar diversos filtros. Este é um público improvisado durante a criação da mensagem e permite que você pule a criação de segmentos ao enviar para públicos únicos.

![Filtros adicionais para uma mensagem que direciona usuários que abriram um app pela última vez no dia, nunca receberam uma campanha ou etapa do Canva, e que fizeram uma compra há menos de 30 dias.]({% image_buster /assets/img_archive/additional_filters.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab segments & filters %}
Também é possível direcionar usuários de um ou mais segmentos criados anteriormente que também se enquadram em filtros adicionais. Depois de selecionar seus segmentos, você pode refinar ainda mais seu público na seção **Additional Filters (Filtros adicionais** ). Isso é demonstrado na captura de tela a seguir, que direciona usuários que estão no segmento "Usuários Ativos Diários", segmento "Nunca abriu e-mail", e que fizeram uma compra há mais de 30 dias.

![Opções de direcionamento para uma mensagem que incluem dois segmentos e têm um filtro adicional para uma última compra feita há menos de 30 dias.]({% image_buster /assets/img_archive/target_segmenter.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab Specific apps %}

Você pode enviar uma mensagem de campanha ou etapa do Canva para aplicativos específicos, como enviar uma mensagem no app ou notificação por push apenas para aplicativos Android ou iOS.

No entanto, lembre-se de que é possível que um usuário use vários aplicativos. O filtro "Tem app" identifica todos os usuários que têm o aplicativo selecionado, mas não controla quais aplicativos recebem mensagens. Por exemplo, se você aplicar um filtro de segmento onde "Tem app" está definido como Android, qualquer usuário que também tenha o app iOS também receberá a mensagem em seu app iOS.

![Um filtro para usuários que têm o app "Hello, World (Android)".]({% image_buster /assets/img_archive/has_app_hello_world.png %}){: style="max-width:60%;"}

Vamos supor que você queira enviar uma mensagem no app apenas para aplicativos Android.

1. Crie um segmento e defina **Aplicativos e sites direcionados** para **Usuários de aplicativos específicos**, em seguida, selecione seu app Android.

![Um segmento direcionando usuários de um aplicativo específico, "Test_Android".]({% image_buster /assets/img_archive/app_test_android.png %}){: style="max-width:60%;"}

{: start="2"}
2\. Na sua campanha ou Canva, acesse a etapa **Públicos Alvo** e confirme que seu segmento foi adicionado na seção **Usuários Alvo por Segmento**. 

![O passo "Públicos Alvo" com um segmento de exemplo selecionado.]({% image_buster /assets/img_archive/target_users_by_segment_example.png %})

{% alert note %}
Isso não funcionará se você adicionar seu segmento na seção **Filtros Adicionais** através de um filtro de associação de segmento. Você deve referenciar diretamente seu segmento em **Usuários Alvo Por Segmento** para entregar sua mensagem apenas para esse app.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert tip %}
Para campanhas de e-mail, é possível direcionar os grupos de teste na seção **Grupos de teste**. Observe que os grupos de teste não estão disponíveis para campanhas de API, embora seja possível incluir grupos de teste por meio de uma entrada disparada pela API em uma campanha. Para saber mais, consulte [Grupos de teste]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#seed-groups).
{% endalert %}

### Etapa 2: Teste seu público

Depois de adicionar segmentos e filtros ao seu público, é possível testar se o público está configurado conforme o esperado, [procurando um usuário]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) para confirmar se ele corresponde aos critérios do público.

![A seção "Busca de Usuário" com um botão "Buscar Usuário".]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

#### Resumo do público

O **Público Resumido** mostrará uma visão geral de quem está no seu público-alvo. Aqui, você pode limitar ainda mais seu público definindo um limite máximo de usuários ou a velocidade de entrega [limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/).

![A seção "Resumo do Público" com opções para definir um limite máximo de usuários ou limite de frequência de entrega.]({% image_buster /assets/img_archive/audience_summary.png %})

#### Testes A/B

Na seção **Testes A/B**, você pode configurar um teste para comparar as respostas dos usuários a várias versões da mesma campanha de marketing. Essas versões compartilham objetivos de marketing semelhantes, mas diferem em termos de redação e estilo. O objetivo é identificar a versão da campanha que melhor atinja suas metas de marketing. 

Para saber mais e melhores práticas, consulte [Multivariante & Testes A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

#### Estatísticas do público

O Braze fornece estatísticas detalhadas do público dos canais direcionados no rodapé. Quanto maior for a sua base de usuários, maior a probabilidade de o valor de **usuários alcançáveis** ser uma estimativa aproximada. O número de usuários acessíveis pode diminuir se você usar um [grupo de controle global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) ou configurar a elegibilidade de mensagens. 

- Para determinar um número preciso de usuários alcançáveis, selecione [Calcular estatísticas exatas]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics), pois isso buscará em todos os usuários da sua base de usuários.
- Para ver qual porcentagem da sua base de usuários está sendo direcionada ou o valor do tempo de vida (LTV) desse segmento, selecione **Show Additional Statistics (Mostrar estatísticas adicionais)**.

##### Por que a contagem do público-alvo pode diferir da contagem de usuários alcançáveis

{% multi_lang_include segments.md section='Differing audience size' %}

![A seção "População Total" com contagens estimadas de usuários alcançáveis em cada canal direcionado.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

{% alert note %}
O cálculo de estatísticas exatas pode levar alguns minutos para ser executado. Essa função calcula apenas as estatísticas exatas no nível do segmento, não no nível do filtro ou do grupo de filtros.<br><br>
Em segmentos grandes, é normal haver uma pequena variação, mesmo ao calcular estatísticas exatas. Espera-se que a precisão desse recurso seja de 99,999% ou mais.
{% endalert %}

## Como o público-alvo e os critérios de entrada funcionam juntos

Quando você cria uma campanha ou Canvas no Braze, o direcionamento acontece em duas partes:

1. **Público-alvo:** Quem se qualifica
2. **Critérios de entrada:** O que aciona a entrega

A ordem importa: O Braze verifica se alguém está no público-alvo antes que os critérios de entrada sejam avaliados. Se um usuário não se qualificar para o público naquele momento, ele não entrará na campanha ou no canva—mesmo que depois dispare o evento de entrada. Pense no público-alvo como uma sala de espera: apenas os usuários que já estão dentro quando o disparo ocorre podem avançar.

### Exemplo 1

Você quer enviar uma mensagem push durante a primeira sessão de um usuário.

Você define:

- **Público-alvo:** Usuários com contagem de sessões = 0
- **Evento de entrada:** Início da sessão

Quando o usuário abre seu app, o Braze vê que a contagem de sessões agora é 1—e eles não se qualificam mais para o público. O evento de entrada acontece depois que eles se tornam elegíveis, então a mensagem não será enviada.

Para que isso funcione, o usuário precisa se qualificar para o público antes que a sessão comece (inverta o público-alvo e o disparo de entrada).

### Exemplo 2

Você quer enviar um e-mail para usuários que gastaram mais de R$10 nos últimos 7 dias.

Você define:

- **Público-alvo:** Usuários que gastaram mais de R$10 nos últimos 7 dias
- **Evento de entrada:** Qualquer compra

Agora imagine que um usuário gasta R$12 hoje. Isso não dispara a mensagem—apenas os torna elegíveis para entrar no público. Eles não receberão o e-mail a menos que façam outra compra mais tarde.

Uma abordagem melhor seria usar um público mais amplo e mover o filtro para os critérios de entrada:

- **Público:** Todos os usuários (ou seu público base)
- **Evento de entrada:** Fazer uma compra
- **Filtro de entrada:** Gasto total nos últimos 7 dias > $10

Dessa forma, uma compra qualificada atende ao filtro e dispara a mensagem—sem necessidade de uma segunda ação.

## Melhores práticas

- Certifique-se de que o segmento de público inclua usuários antes que os critérios de entrada ocorram.
- Evite usar filtros de público que só se aplicam após o seu evento. Se um filtro depende de algo que acontece no momento do disparo (como "contagem de sessões = 0"), o usuário pode não se qualificar mais quando o Braze verifica.
- Use a lógica baseada em tempo com cuidado. Por exemplo, se você quiser segmentar novos usuários:
    - Defina seu público-alvo como "primeiro uso do app nos últimos 7 dias".
    - Defina seu evento de entrada como "início da sessão".
    - Dessa forma, apenas usuários que ainda estão na sua primeira semana se qualificarão e entrarão quando iniciarem uma sessão.
