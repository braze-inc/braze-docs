---
nav_title: Sobre o Audience Sync
article_title: Sobre o Audience Sync
description: "Este artigo de referência abordará como usar a sincronização de público do Braze para o Facebook, para veicular anúncios com base em gatilhos comportamentais, segmentação e mais."
page_order: 0
Tool:
  - Canvas

---

# Sobre o Audience Sync

> O recurso de Sincronização de público da Braze ajuda você a expandir o alcance de suas campanhas para muitas das principais tecnologias sociais e de publicidade. Por meio do [Braze Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas), as marcas podem sincronizar dinamicamente e com segurança os dados de usuários de primeira parte no ecossistema de publicidade para impulsionar a eficiência de marketing e operacional.

## Disponibilidade de recursos

Todos os clientes da Braze terão acesso imediato ao Audience Sync para Google e Facebook. Para desbloquear destinos adicionais do Audience Sync, como TikTok, Pinterest, Snapchat ou Criteo, você precisará adquirir o Audience Sync Pro. Entre em contato com o gerente de conta da Braze para mais detalhes.

## Casos de uso

- Direcionamento de usuários de alto valor usando canais proprietários e pagos para gerar compras ou engajamento incrementais.
- Criando públicos semelhantes de seus usuários de alto valor para otimizar os custos de aquisição de novos usuários e conversões.
- Redirecionamento de usuários com anúncios que são menos responsivos a outros canais de marketing.
- Criando públicos de supressão para evitar que os usuários recebam anúncios quando já são consumidores fiéis da sua marca.

## Visão geral

<style>
table td {
    word-break: break-word;
}
</style>

| Destino | Tempo para que os destinos correspondam aos membros do público | Limite de taxa | Semelhante ou semelhante | Dicas |
| --- | --- | --- | --- | --- |
| [Criteo]({{site.baseurl}}/partners/canvas_steps/criteo_audience_sync) | Até 24 horas | 250.000 solicitações por minuto. Em lote a cada 5 segundos com uma tentativa automática com base no feedback do Google. | Sim | {::nomarkdown}<ul><li>A Criteo suporta até 1.000 públicos-alvo de anúncios.</li><li>O tamanho mínimo do público é 500, e o recomendado é mais de 20.000.</li></ul>{:/} |
| [Facebook ou Instagram]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync/) | Até 24 horas | 190.000 contas de anúncios por hora | Sim | {::nomarkdown}<ul><li>O Facebook suporta até 500 públicos de anúncios.</li><li>O Facebook exige que o público tenha pelo menos 1.000 usuários.</li></ul>{:/} |
| [Google Ads ou YouTube]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/) | Entre 6 e 12 horas | Em lote a cada 5 segundos com uma tentativa automática baseada no feedback do Google | Não | {::nomarkdown}<ul><li><b>Correspondência com o cliente:</b> Use o anúncio para celular, o endereço de e-mail ou o número de telefone.</li><li>O público do Google exige pelo menos 5.000 usuários para começar a veicular anúncios.</li><li>O tamanho do público será mostrado como zero até que haja pelo menos 1.000 usuários.</li></ul>{:/} |
| [LinkedIn]({{site.baseurl}}/partners/canvas_steps/linkedin_audience_sync) | 48 horas | O LinkedIn processa 10 consultas por segundo e 100.000 usuários por solicitação. Usuários de lotes de Braze a cada 5 segundos. | Público com previsão de IA | {::nomarkdown}<ul><li>O tamanho mínimo do público é de 300 membros, levando em consideração o direcionamento por local.</li><li>O LinkedIn mostra a taxa correspondente no dashboard do Braze.</li></ul>{:/} |
| [Pinterest]({{site.baseurl}}/partners/canvas_steps/pinterest_audience_sync/) | Entre 24 e 48 horas | O Pinterest processa 7 consultas por segundo e 100.000 usuários por solicitação. Usuários de lotes de Braze a cada 5 segundos. | Sim | Os públicos do Pinterest exigem pelo menos 100 usuários. |
| [Snapchat]({{site.baseurl}}/partners/canvas_steps/snapchat_audience_sync/) | N/D | O Snapchat processa 10 consultas por segundo e 100.000 usuários por solicitação. Usuários de lotes de Braze a cada 5 segundos. | Sim | O Snapchat suporta até 1.000 públicos de anúncios. |
| [TikTok]({{site.baseurl}}/partners/canvas_steps/tiktok_audience_sync/) | Entre 24 e 48 horas | O TikTok processa 50 consultas por segundo e 10.000 usuários por solicitação. Usuários de lotes de Braze a cada 5 segundos. | Sim | {::nomarkdown}<ul><li>O TikTok suporta até 400 públicos-alvo de anúncios.</li><li>O público do TikTok precisa de pelo menos 1.000 usuários para começar a veicular anúncios.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }
<sup>Quando o limite de frequência for atingido, o Braze tentará novamente as sincronizações por 13 horas.</sup>

## Como funciona?

Para usar a sincronização de público com o Google ou o Facebook, conecte sua conta de anúncio procurando pelo parceiro na página de **Parceiros de Tecnologia**.

![Parceiro tecnológico do Facebook.][3]{: style="max-width:35%;"} ![Parceiro de tecnologia de anúncios do Google Ads.][4]{: style="max-width:35%;"}

Depois de conectar sua conta de anúncios, você pode criar um Canva com uma etapa do Audience Sync.

![Menu do componente de tela para adicionar a etapa do Audience Sync à jornada do usuário.][22]{: style="max-width:75%;"}

Em seguida, selecione o parceiro para sincronizar os públicos.

![Opção para selecionar seu parceiro de sincronização de público na etapa Audience Sync.][19]{: style="max-width:85%;"}

Para cada parceiro, você precisará configurar o seguinte como parte da sua etapa do Audience Sync: 

- Conta de anúncio
- Público 
- Ação para adicionar ou remover usuários 
- Campos para corresponder 

Lembre-se de que a Braze sincronizará os usuários assim que eles entrarem na etapa de Sincronização de Público dentro do seu canva. 

Para cada destino de Sincronização de público, o parceiro pode ter requisitos diferentes para os campos que podemos enviar. Consulte a documentação específica do parceiro para mais detalhes. 

### Audience Sync Pro

Para usar um parceiro do Audience Sync Pro, como TikTok, Pinterest, Snapchat ou Criteo, você poderá selecionar seus parceiros com base em suas cotas de compra do Audience Sync Pro na seção **Audience Sync Pro** na página **Parceiros de tecnologia**.

![Audience Sync Pro sem parceiros selecionados ainda.][5]{: style="max-width:75%;"}

Primeiro, selecione os parceiros que você pretende usar em "Selecionar parceiros". Cada compra do Audience Sync Pro fornecerá a você 3 destinos do Audience Sync Pro alocados, que estarão disponíveis em cada um de seus espaços de trabalho no dashboard.

![Opção para selecionar até três parceiros para se conectar ao Braze.][6]{: style="max-width:65%;"}

Depois de selecionar seus destinos do Audience Sync Pro, conecte sua conta de anúncio do parceiro selecionado clicando no bloco do parceiro.

![Um exemplo do Snapchat e do TikTok selecionados como parceiros para o Audience Sync.][7]{: style="max-width:70%;"}

![Configurações do Snapchat Audience Sync com a mensagem: "Você conectou com sucesso 1 conta do Snapchat".][9]{: style="max-width:70%;"}

Por fim, crie sua etapa do Audience Sync no canva usando o destino do Audience Sync Pro.

### E-mails de erro do Audience Sync

Se o erro estiver relacionado à integração geral com parceiros (como um problema de autorização), um e-mail será enviado ao usuário que conectou a integração. Se esse usuário não existir mais, os administradores receberão os e-mails. 

Se o erro estiver relacionado a problemas com o componente Audience Sync (como "O público não existe") no Canvas, um e-mail será enviado ao usuário que configurou o Canvas. Se esse usuário não existir mais, a responsabilidade recairá sobre o administrador da empresa.

Para configurar quem receberá esses e-mails, entre em contato com o gerente de sucesso do cliente para adicionar destinatários em **Notification Preferences (Preferências de notificação**). Como esse recurso mudará o comportamento atual, você precisará adicionar imediatamente os destinatários a essa nova preferência de notificação, já que o Braze não faz a aceitação de ninguém por padrão, e para garantir que nenhum e-mail de erro seja perdido.

## Considerações sobre privacidade de dados

{% alert important %}
Esta documentação não se destina a fornecer, nem pode ser considerada como fornecendo aconselhamento jurídico. O uso da sincronização de público está sujeito a requisitos legais específicos. Busque orientação jurídica para ter certeza de que você está utilizando o serviço conforme a legislação aplicável.
{% endalert %}

Ao criar públicos para rastreamento de anúncios, você pode desejar incluir ou excluir certos usuários com base em suas preferências e para cumprir as leis de privacidade, como o direito de “Não Vender ou Compartilhar” sob o [CCPA](https://oag.ca.gov/privacy/ccpa). Os profissionais de marketing devem implementar os filtros relevantes para a elegibilidade dos usuários em seus critérios de entrada no Canva. Abaixo, listamos algumas opções.

Se você coletou o [IDFA do iOS pelo SDK da Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), poderá usar o filtro "Rastreamento de anúncios ativado". Selecione o valor como `true` para enviar os usuários apenas para destinos do Audience Sync que eles aceitaram.

![Uma tela com um público de entrada de "A capacitação do rastreamento de anúncios é verdadeira".][2]

Se você estiver coletando `opt-ins`, `opt-outs`, `Do Not Sell Or Share` ou quaisquer outros atributos personalizados relevantes, deve incluir esses dentro dos seus critérios de entrada da canva como um filtro:

![Uma tela com um público de entrada "opted_in_marketing equals true".][1]

Para saber mais sobre como cumprir essas leis de Proteção de Dados na plataforma Braze, consulte [Assistência Técnica de Proteção de Dados]({{site.baseurl}}/dp-technical-assistance/).

## Gerenciamento do consentimento para direcionamento de anúncios

Como anunciante, é sua responsabilidade gerenciar o consentimento para rastreamento de anúncios ou direcionamento de seus usuários.

Para enviar anúncios aos seus usuários, é necessário cumprir todas as leis e regulamentos aplicáveis, bem como as políticas e os requisitos da plataforma de anúncios. Use o Braze para direcionamento e sincronização de usuários somente quando tiver obtido o consentimento deles. 

Para manter suas listas de público nessas plataformas de anúncios atualizadas e remover usuários que revogaram seu consentimento, configure um Canva para remover usuários dessas listas de público existentes usando uma etapa do Audience Sync.


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