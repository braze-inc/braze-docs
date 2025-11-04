---
nav_title: Sobre a Sincronização de Público
article_title: Sobre a Sincronização de Público
alias: /partners/about_audience_sync/
description: "Este artigo de referência abordará como usar a sincronização de público do Braze para o Facebook, para veicular anúncios com base em gatilhos comportamentais, segmentação e mais."
page_order: 0
Tool:
  - Canvas

---

# Sobre a Sincronização de Público

> O recurso de Sincronização de público da Braze ajuda você a expandir o alcance de suas campanhas para muitas das principais tecnologias sociais e de publicidade. Por meio do [Braze Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas), as marcas podem sincronizar dinamicamente e com segurança os dados de usuários de primeira parte no ecossistema de publicidade para impulsionar a eficiência de marketing e operacional.

## Disponibilidade de recursos

Todos os clientes da Braze terão acesso imediato ao Audience Sync para Google e Facebook. Para desbloquear destinos adicionais do Audience Sync, como TikTok, Pinterest, Snapchat ou Criteo, você precisará adquirir o Audience Sync Pro. Entre em contato com o gerente de conta da Braze para mais detalhes.

## Casos de uso

- Direcionamento de usuários de alto valor usando canais próprios e pagos para impulsionar compras ou engajamento incremental.
- Criando públicos semelhantes de seus usuários de alto valor para otimizar os custos de aquisição de novos usuários e conversões.
- Redirecionamento de usuários com anúncios que são menos responsivos a outros canais de marketing.
- Criando públicos de supressão para evitar que os usuários recebam anúncios quando já são consumidores fiéis da sua marca.

## Visão geral

<style>
table td {
    word-break: break-word;
}
</style>

| Destino | Tempo para o destino coincidir com os membros do público | Limite de taxa | Lookalike ou actalike | Dicas |
| --- | --- | --- | --- | --- |
| [Criteo]({{site.baseurl}}/partners/canvas_audience_sync/criteo_audience_sync/) | Até 24 horas | 250.000 solicitações por minuto. Agrupado a cada 5 segundos com uma nova tentativa automática com base no feedback do Google. | Sim | {::nomarkdown}<ul><li>A Criteo suporta até 1.000 públicos de anúncios.</li><li>O tamanho mínimo do público é 500, e o recomendado é mais de 20.000.</li></ul>{:/} |
| [Facebook ou Instagram]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) | Até 24 horas | 190.000 contas de anúncios por hora | Sim | {::nomarkdown}<ul><li>O Facebook suporta até 500 públicos de anúncios.</li><li>O Facebook exige que os públicos tenham pelo menos 1.000 usuários.</li></ul>{:/} |
| [Google Ads ou YouTube]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) | Entre 6 a 12 horas | Agrupado a cada 5 segundos com uma nova tentativa automática com base no feedback do Google | Não | {::nomarkdown}<ul><li><b>Correspondência de clientes:</b> Use anúncio móvel, ou endereço de e-mail ou número de telefone.</li><li>Os Públicos do Google exigem pelo menos 5.000 usuários para começar a exibir anúncios.</li><li>O tamanho do público será mostrado como zero até que haja pelo menos 1.000 usuários.</li></ul>{:/} |
| [LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync/) | 48 horas | O LinkedIn processa 10 consultas por segundo e 100.000 usuários por solicitação. O Braze agrupa usuários a cada 5 segundos. | Públicos preditivos de IA | {::nomarkdown}<ul><li>O tamanho mínimo do público é de 300 membros, considerando o direcionamento por localização.</li><li>O LinkedIn mostra a correspondência da taxa no dashboard do Braze.</li></ul>{:/} |
| [Pinterest]({{site.baseurl}}/partners/canvas_audience_sync/pinterest_audience_sync/) | Entre 24 e 48 horas | O Pinterest processa 7 consultas por segundo e 100.000 usuários por solicitação. O Braze agrupa usuários a cada 5 segundos. | Sim | Os públicos do Pinterest exigem pelo menos 100 usuários. |
| [Snapchat]({{site.baseurl}}/partners/canvas_audience_sync/snapchat_audience_sync/) | N/D | O Snapchat processa 10 consultas por segundo e 100.000 usuários por solicitação. O Braze agrupa usuários a cada 5 segundos. | Sim | O Snapchat suporta até 1.000 públicos de anúncios. |
| [TikTok]({{site.baseurl}}/partners/canvas_audience_sync/tiktok_audience_sync/) | Entre 24 e 48 horas | O TikTok processa 50 consultas por segundo e 10.000 usuários por solicitação. O Braze agrupa usuários a cada 5 segundos. | Sim | {::nomarkdown}<ul><li>O TikTok suporta até 400 públicos de anúncios.</li><li>Os públicos do TikTok exigem pelo menos 1.000 usuários para começar a exibir anúncios.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }
<sup>Quando o limite de frequência é atingido, o Braze tentará sincronizações por 13 horas.</sup>

## Como funciona?

Para usar a sincronização de público com o Google ou o Facebook, conecte sua conta de anúncio procurando pelo parceiro na página de **Parceiros de Tecnologia**.

![Parceiro de tecnologia do Facebook.]({% image_buster /assets/img/audience_sync/facebook_partner.png %}){: style="max-width:35%;"} ![Parceiro de tecnologia do Google Ads.]({% image_buster /assets/img/audience_sync/google_ads_partner.png %}){: style="max-width:35%;"}

Após conectar sua conta de anúncios, você pode criar um Canva com uma etapa de Sincronização de Público.

![Menu de componentes do Canva para adicionar a etapa de Sincronização de Público à jornada do usuário.]({% image_buster /assets/img/audience_sync/audience_sync7.png %}){: style="max-width:75%;"}

Em seguida, selecione o parceiro para sincronizar os públicos.

![Opção para selecionar seu parceiro de sincronização de público na etapa de Sincronização de Público.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:85%;"}

Para cada parceiro, você precisará configurar o seguinte como parte da sua etapa do Audience Sync: 

- Conta de anúncio
- Público 
- Ação para adicionar ou remover usuários 
- Campos para corresponder 

Lembre-se de que a Braze sincronizará os usuários assim que eles entrarem na etapa de Sincronização de Público dentro do seu canva. 

Para cada destino de Sincronização de público, o parceiro pode ter requisitos diferentes para os campos que podemos enviar. Consulte a documentação específica do parceiro para mais detalhes. 

### Audience Sync Pro

Para usar um parceiro do Audience Sync Pro, como TikTok, Pinterest, Snapchat ou Criteo, você poderá selecionar seus parceiros com base em suas cotas de compra do Audience Sync Pro na seção **Audience Sync Pro** na página **Parceiros de tecnologia**.

![Sincronização de Público Pro sem parceiros selecionados ainda.]({% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}){: style="max-width:75%;"}

Primeiro, selecione os parceiros que você pretende usar em "Selecionar parceiros". Cada compra do Audience Sync Pro fornecerá a você 3 destinos do Audience Sync Pro alocados, que estarão disponíveis em cada um de seus espaços de trabalho no dashboard.

![Opção para selecionar até três parceiros para conectar ao Braze.]({% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}){: style="max-width:65%;"}

Depois de selecionar seus destinos do Audience Sync Pro, conecte sua conta de anúncio do parceiro selecionado clicando no bloco do parceiro.

![Um exemplo do Snapchat e TikTok selecionados como parceiros para a Sincronização de Público.]({% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}){: style="max-width:70%;"}

![Configurações de Sincronização de Público do Snapchat com a mensagem: "Você conectou com sucesso 1 conta do Snapchat".]({% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}){: style="max-width:70%;"}

Por fim, crie sua etapa do Audience Sync no canva usando o destino do Audience Sync Pro.

### E-mails de erro da Sincronização de Público

Se o erro estiver relacionado à integração geral com parceiros (como um problema de autorização), um e-mail é enviado ao usuário que conectou a integração. Se esse usuário não existir mais, os administradores receberão os e-mails. 

Se o erro estiver relacionado a problemas com o componente de Sincronização de Público (como "Público Não Existe") no Canva, um e-mail é enviado ao usuário que configurou o Canva. Se esse usuário não existir mais, então recai sobre o administrador da empresa.

Para configurar quem receberá esses e-mails, entre em contato com seu gerente de sucesso do cliente para adicionar destinatários em **Preferências de Notificação**. Como esse recurso mudará o comportamento atual, você precisará adicionar imediatamente destinatários a essa nova preferência de notificação, pois o Braze não opta por ninguém por padrão, e para garantir que nenhum e-mail de erro seja perdido.

## Considerações sobre privacidade de dados

{% alert important %}
Esta documentação não se destina a fornecer, nem pode ser considerada como fornecendo aconselhamento jurídico. O uso da sincronização de público está sujeito a requisitos legais específicos. Busque orientação jurídica para ter certeza de que você está utilizando o serviço conforme a legislação aplicável.
{% endalert %}

Ao criar públicos para rastreamento de anúncios, você pode desejar incluir ou excluir certos usuários com base em suas preferências e para cumprir as leis de privacidade, como o direito de “Não Vender ou Compartilhar” sob o [CCPA](https://oag.ca.gov/privacy/ccpa). Os profissionais de marketing devem implementar os filtros relevantes para a elegibilidade dos usuários em seus critérios de entrada no Canva. Abaixo, listamos algumas opções.

Se você coletou o [IDFA do iOS pelo SDK da Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), poderá usar o filtro "Rastreamento de anúncios ativado". Selecione o valor como `true` para enviar os usuários apenas para destinos do Audience Sync que eles aceitaram.

![Um Canva com um público de entrada de "Rastreamento de Anúncios Habilitado é verdadeiro".]({% image_buster /assets/img/audience_sync/audience_sync2.png %})

Se você estiver coletando `opt-ins`, `opt-outs`, `Do Not Sell Or Share` ou quaisquer outros atributos personalizados relevantes, deve incluir esses dentro dos seus critérios de entrada da canva como um filtro:

![Um Canva com um público de entrada de "opted_in_marketing igual a verdadeiro".]({% image_buster /assets/img/audience_sync/audience_sync.png %})

Para saber mais sobre como cumprir essas leis de proteção de dados na plataforma Braze, consulte a [Assistência Técnica de Proteção de Dados]({{site.baseurl}}/dp-technical-assistance/).

## Gerenciando consentimento para direcionamento de anúncios

Como anunciante, é sua responsabilidade gerenciar o consentimento para rastreamento de anúncios ou direcionamento de seus usuários.

Para enviar anúncios aos seus usuários, você deve cumprir todas as leis e regulamentos aplicáveis, bem como as políticas e requisitos da plataforma de anúncios. Use apenas o Braze para direcionar e sincronizar usuários onde você obteve o consentimento deles. 

Para manter suas listas de público nessas plataformas de anúncios atualizadas e remover usuários que revogaram seu consentimento, configure um Canva para remover usuários dessas listas de público existentes usando uma etapa de Sincronização de Público.


