---
nav_title: Visão geral
article_title: Visão geral
description: "Este artigo de referência abordará como usar a sincronização de público do Braze para o Facebook, para veicular anúncios com base em gatilhos comportamentais, segmentação e mais."
page_order: 0
Tool:
  - Canvas

---

# Visão geral da sincronização do público

> O recurso de Sincronização de público da Braze ajuda você a expandir o alcance de suas campanhas para muitas das principais tecnologias sociais e de publicidade. Por meio do [Braze Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas), as marcas podem sincronizar dinamicamente e com segurança os dados de usuários de primeira parte no ecossistema de publicidade para impulsionar a eficiência de marketing e operacional.

## Casos de uso

- Direcionamento de usuários de alto valor por meio de canais próprios e pagos para impulsionar compras incrementais ou engajamento.
- Criando públicos semelhantes de seus usuários de alto valor para otimizar os custos de aquisição de novos usuários e conversões.
- Redirecionamento de usuários com anúncios que são menos responsivos a outros canais de marketing.
- Criando públicos de supressão para evitar que os usuários recebam anúncios quando já são consumidores fiéis da sua marca.

## Disponibilidade de recursos

Todos os clientes da Braze terão acesso imediato ao Audience Sync para Google e Facebook. Para desbloquear destinos adicionais do Audience Sync, como TikTok, Pinterest, Snapchat ou Criteo, você precisará adquirir o Audience Sync Pro. Entre em contato com o gerente de conta da Braze para mais detalhes.

## Como funciona?

Para usar a sincronização de público com o Google ou o Facebook, conecte sua conta de anúncio procurando pelo parceiro na página de **Parceiros de Tecnologia**.

![][3]{: style="max-width:35%;"} ![][4]{: style="max-width:35%;"}

Depois de conectar sua conta de anúncios, você pode criar uma canva com uma etapa de Sincronização de Público.

![][22]{: style="max-width:75%;"}

Em seguida, selecione o parceiro para sincronizar os públicos.

![][19]{: style="max-width:85%;"}

Para cada parceiro, você precisará configurar o seguinte como parte da sua etapa do Audience Sync: 
- Conta de anúncio
- Público 
- Ação para adicionar ou remover usuários 
- Campos para corresponder 

Lembre-se de que a Braze sincronizará os usuários assim que eles entrarem na etapa de Sincronização de Público dentro do seu canva. 

Para cada destino de Sincronização de público, o parceiro pode ter requisitos diferentes para os campos que podemos enviar. Consulte a documentação específica do parceiro para mais detalhes. 

### Audience Sync Pro

Para usar um parceiro do Audience Sync Pro, como TikTok, Pinterest, Snapchat ou Criteo, você poderá selecionar seus parceiros com base em suas cotas de compra do Audience Sync Pro na seção **Audience Sync Pro** na página **Parceiros de tecnologia**.

![][5]{: style="max-width:75%;"}

Primeiro, selecione os parceiros que você pretende usar em "Selecionar parceiros". Cada compra do Audience Sync Pro fornecerá a você 3 destinos do Audience Sync Pro alocados, que estarão disponíveis em cada um de seus espaços de trabalho no dashboard.

![][6]{: style="max-width:65%;"}

Depois de selecionar seus destinos do Audience Sync Pro, conecte sua conta de anúncio do parceiro selecionado clicando no bloco do parceiro.

![][7]{: style="max-width:70%;"}

![][9]{: style="max-width:70%;"}

Por fim, crie sua etapa do Audience Sync no canva usando o destino do Audience Sync Pro.

## Considerações sobre privacidade de dados

{% alert important %}
Esta documentação não se destina a fornecer, nem pode ser considerada como fornecendo aconselhamento jurídico. O uso da sincronização de público está sujeito a requisitos legais específicos. Busque orientação jurídica para ter certeza de que você está utilizando o serviço conforme a legislação aplicável.
{% endalert %}

Ao criar públicos para rastreamento de anúncios, você pode desejar incluir ou excluir certos usuários com base em suas preferências e para cumprir as leis de privacidade, como o direito de “Não Vender ou Compartilhar” sob o [CCPA](https://oag.ca.gov/privacy/ccpa). Os profissionais de marketing devem implementar os filtros relevantes para a elegibilidade dos usuários em seus critérios de entrada no Canva. Abaixo, listamos algumas opções.

Se você coletou o [IDFA do iOS pelo SDK da Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), poderá usar o filtro "Rastreamento de anúncios ativado". Selecione o valor como `true` para enviar os usuários apenas para destinos do Audience Sync que eles aceitaram.

![][2]

Se você estiver coletando `opt-ins`, `opt-outs`, `Do Not Sell Or Share` ou quaisquer outros atributos personalizados relevantes, deve incluir esses dentro dos seus critérios de entrada da canva como um filtro:

![Uma canva com um público de entrada de "opted_in_marketing" é igual a "true".][1]

Para saber mais sobre como cumprir essas leis de Proteção de Dados na plataforma Braze, consulte [Assistência Técnica de Proteção de Dados]({{site.baseurl}}/dp-technical-assistance/).

[1]: {% image_buster /assets/img/audience_sync/audience_sync.png %}
[2]: {% image_buster /assets/img/audience_sync/audience_sync2.png %}
[3]: {% image_buster /assets/img/audience_sync/facebook_partner.png %}
[4]: {% image_buster /assets/img/audience_sync/google_ads_partner.png %}
[5]: {% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}
[6]: {% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}
[7]: {% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}
[8]: {% image_buster /assets/img/audience_sync/audience_sync_pro3b.png %}
[9]: {% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
[21]: {% image_buster /assets/img/audience_sync/audience_sync6.png %}
[22]: {% image_buster /assets/img/audience_sync/audience_sync7.png %}