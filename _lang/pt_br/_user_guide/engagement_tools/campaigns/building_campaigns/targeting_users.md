---
nav_title: Direcionamento de usuários
article_title: Direcionamento de usuários
page_order: 4
tool: Campaigns
page_type: reference
description: "Este artigo de referência aborda as opções de direcionamento encontradas na etapa de públicos-alvo da criação da campanha."
---

# Direcionamento de usuários

> Depois de [criar a campanha][1] e determinar o [cronograma de entrega][2], você pode definir os destinatários-alvo da campanha na etapa **Públicos-alvo**. 

## Opções de direcionamento

Na seção **Targeting Options (Opções de direcionamento)**, você encontrará algumas opções para quem pode enviar sua campanha.

{% alert note %}
Somente os usuários que corresponderem aos seus critérios definidos receberão a campanha. Lembre-se de que a associação exata ao segmento de mensagens é sempre calculada imediatamente antes do envio da mensagem.
{% endalert %}

### Direcionamento a usuários em um segmento existente {#existing-segment}

Para direcionar os membros de um segmento criado anteriormente, selecione um segmento no menu suspenso em **Target Users by Segment (Direcionar usuários por segmento**).

### Direcionamento a usuários em vários segmentos existentes {#multiple-existing-segment}

Para direcionar usuários que se enquadram em vários segmentos criados anteriormente, adicione vários segmentos no menu suspenso em **Target Users by Segment (Direcionar usuários por segmento**). O público-alvo resultante será composto por usuários do primeiro, do segundo e do terceiro segmento, etc.

### Direcionamento de usuários em vários segmentos e filtros existentes {#existing_segment_filter}

Também é possível direcionar usuários de um ou mais segmentos criados anteriormente que também se enquadram em filtros adicionais. Depois de selecionar seus segmentos, você pode refinar ainda mais seu público na seção **Additional Filters (Filtros adicionais** ). Isso é demonstrado na captura de tela a seguir, que direciona os usuários que estão no segmento de usuários ativos diários, no segmento de e-mails não abertos e que fizeram uma compra há menos de 30 dias.

![][25]

### Direcionamento de usuários sem segmentos {#without-segment}

Para direcionar usuários sem adicionar um segmento, é possível usar diversos filtros. Isso significa que não é necessário direcionar uma campanha para um segmento pré-existente; você pode criar um público improvisado durante a criação da campanha usando apenas os filtros adicionais e não selecionando nenhum segmento em **Target Users By Segment**. Isso permitirá que você ignore a criação de segmentos ao enviar campanhas para públicos únicos.

![][26]

## Direcionamento de grupos de teste

Para campanhas de e-mail, é possível direcionar os grupos de teste na seção **Grupos de teste**. Observe que os grupos de teste não estão disponíveis para campanhas de API, embora seja possível incluir grupos de teste por meio de uma entrada disparada pela API em uma campanha. Para saber mais, consulte [Grupos de teste]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#seed-groups).

## Testar seu público

Depois de adicionar segmentos e filtros ao seu público, é possível testar se o público está configurado conforme o esperado, [procurando um usuário]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) para confirmar se ele corresponde aos critérios do público.

![]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:60%"}

## Resumo do público

Depois de adicionar segmentos ou filtros para ajustar seu público, o **Resumo do público** mostrará uma visão geral de quem está em seu público-alvo. Aqui é possível limitar ainda mais o público da campanha com a definição do máximo de usuários ou da [taxa de frequência máxima][3] da velocidade de entrega. Para campanhas de envio de e-mail e notificações por push, é possível selecionar qual inscrição e status de aceitação serão direcionados.

![][27]

## Testes A/B

Na seção **Testes A/B**, é possível configurar um teste para comparar as respostas dos usuários a várias versões da mesma campanha de marketing. Essas versões compartilham objetivos de marketing semelhantes, mas diferem em termos de redação e estilo. O objetivo é identificar a versão da campanha que melhor atinja suas metas de marketing. 

Para saber mais e conhecer as práticas recomendadas, consulte [Testes multivariantes e Testes A/B.][4]

## Estatísticas do público

O Braze fornece estatísticas detalhadas do público dos canais direcionados no rodapé. 

Quanto maior for a sua base de usuários, maior a probabilidade de o valor de **usuários alcançáveis** ser uma estimativa aproximada. O número de usuários acessíveis pode diminuir se você usar um [grupo de controle global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) ou configurar a elegibilidade de mensagens. Selecione [Calculate exact statistics (Calcular estatísticas exatas)]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics) para determinar um número preciso para seus usuários acessíveis, pois isso pesquisará cada usuário em sua base de usuários. 

Note que:

- O cálculo de estatísticas exatas pode levar alguns minutos para ser executado. Essa função calcula apenas as estatísticas exatas no nível do segmento, não no nível do filtro ou do grupo de filtros.
- Em segmentos grandes, é normal haver uma pequena variação, mesmo ao calcular estatísticas exatas. Espera-se que a precisão desse recurso seja de 99,999% ou mais.

![][24]

Para ver qual porcentagem da sua base de usuários está sendo direcionada ou o valor do tempo de vida (LTV) desse segmento, selecione **Show Additional Statistics (Mostrar estatísticas adicionais)**.

[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/
[3]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/
[4]: {{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/
[24]: {% image_buster /assets/img_archive/multi_channel_footer.png %}
[25]: {% image_buster /assets/img_archive/target_segmenter.png %}
[26]: {% image_buster /assets/img_archive/additional_filters.png %}
[27]: {% image_buster /assets/img_archive/audience_summary.png %}
