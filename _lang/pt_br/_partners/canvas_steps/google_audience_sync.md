---
nav_title: Google
article_title: Canvas Audience Sync para o Google
alias: /google_audience_sync/
description: "Este artigo de referência abordará como usar a sincronização de público do Braze para o Google, para veicular anúncios com base em gatilhos comportamentais, segmentação e mais."
Tool:
  - Canvas
page_order: 3

---

# Audience Sync para o Google

{% alert important %}
O Google está atualizando sua [Política de Consentimento do Usuário da UE](https://www.google.com/about/company/user-consent-policy/) em resposta às mudanças na [Lei dos Mercados Digitais (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), que está em vigor a partir de 6 de março de 2024. Essa nova alteração exige que os anunciantes divulguem determinadas informações aos seus usuários finais do EEE, Reino Unido e Suíça, bem como obtenham deles os consentimentos necessários. Consulte a documentação a seguir para saber mais.
{% endalert %}

A integração de sincronização de público do Braze com o Google permite que as marcas ampliem o alcance de suas jornadas de clientes em vários canais para o Google Search, Google Shopping, Gmail, YouTube e Google Display. Usando seus dados de cliente de primeira parte, você pode entregar anúncios com segurança com base em gatilhos comportamentais dinâmicos, segmentação e mais. Qualquer critério que você normalmente usaria para disparar uma mensagem (por exemplo, push, e-mail ou SMS) como parte de um canva da Braze pode ser usado para disparar um anúncio para esse usuário via [Customer Match](https://support.google.com/google-ads/answer/6379332?hl=en) do Google.

{% alert important %}
A partir de 1º de maio de 2023, o Google Ads não gerará mais públicos similares, também conhecidos como "públicos semelhantes", para direcionamento e relatórios. Consulte a documentação do [Google Ads](https://support.google.com/google-ads/answer/12463119?) para saber mais.
{% endalert %}

**Casos de uso comuns para sincronização de Públicos Personalizados incluem:**
- Direcionamento de usuários de alto valor por meio de vários canais para impulsionar compras ou engajamento.
- Redirecionamento de usuários que são menos responsivos a outros canais de marketing.
- Criando públicos de supressão para evitar que os usuários recebam anúncios quando já são consumidores fiéis da sua marca.

{% alert note %}
Esse recurso permite que as marcas controlem quais dados primários específicos são compartilhados com o Google. Na Braze, as integrações com as quais você pode e não pode compartilhar seus dados primários recebem a máxima consideração. Para saber mais sobre nossa política de privacidade de dados da Braze, clique [aqui](https://www.braze.com/privacy).
{% endalert %}

## Pré-requisitos

Os seguintes itens precisam ser criados e concluídos antes de configurar sua etapa de público do Google no canva.

| Requisito | Origin | Descrição |
| ----------- | ------ | ----------- |
| Conta do Google Ads | [Google](https://support.google.com/google-ads/answer/6366720?hl=en) | Uma conta ativa do Google Ads para sua marca.<br><br>Se você deseja compartilhar um público entre várias contas gerenciadas, pode fazer upload de seus públicos na sua [conta de gerente](https://support.google.com/google-ads/answer/6139186). |
| Termos do Google Ads e Políticas do Google Ads | [Google](https://support.google.com/adspolicy/answer/54818?hl=en) | Você deve aceitar e garantir que está em conformidade com os [Termos de Anúncios do Google](https://payments.google.com/u/0/paymentsinfofinder?hostOrigin=aHR0cHM6Ly9wYXltZW50cy5nb29nbGUuY29tOjQ0Mw..&sri=-40) e as [Políticas de Anúncios do Google](https://support.google.com/adspolicy/answer/6008942?sjid=15557182366992806023-NC), que incluem a [Política de Consentimento de Usuário da UE](https://www.google.com/about/company/user-consent-policy/), conforme aplicável a você, no uso do Braze Audience Sync.<br><br>Consulte sua equipe jurídica sobre a nova Política de consentimento do usuário da UE do Google para garantir que esteja coletando o consentimento adequado para usar os serviços do Google Ads para seus usuários finais do EEE, Reino Unido e Suíça. |
| Segmentação por lista de clientes do Google | [Google](https://support.google.com/google-ads/answer/6299717) |  A segmentação por lista de clientes não está disponível para todos os anunciantes.<br><br>**Para usar a segmentação por lista de clientes, sua conta deve ter:**<br>• Um bom histórico de conformidade com as políticas<br>• Um bom histórico de pagamento.<br>• Pelo menos 90 dias de histórico no Google Ads.<br>Mais de US$ 50.000 gastos totais ao longo da vida. Para os anunciantes cujas contas não sejam em USD, o valor gasto será convertido para USD usando a taxa de conversão média mensal para essa moeda.<br><br>Caso não atenda a esses critérios, sua conta não será considerada qualificada para usar a segmentação por lista de clientes.<br><br>Fale com seu representante do Google Ads para obter mais orientações sobre a disponibilidade da segmentação por lista de clientes para sua conta. |
| Sinais de Consentimento do Google | [Google](https://support.google.com/google-ads/answer/14310715) |  Se você deseja veicular anúncios para usuários finais do EEE usando o serviço Customer Match do Google, precisará passar para a Braze os seguintes atributos personalizados (booleanos) como parte da Política de Consentimento do Usuário da UE do Google. Mais detalhes podem ser encontrados em [Coleta de consentimento para usuários finais do EEE, Reino Unido e Suíça](#collecting-consent-for-eea-uk-and-switzerland-end-users): <br> `$google_ad_user_data` <br> - `$google_ad_personalization` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Ao usar os SDKs da Braze para coletar sinais de consentimento, observe as seguintes versões mínimas:

{% sdk_min_versions swift:7.6.0 android:1.3.2 web:3.0.0 %}

### Coleta de consentimento para usuários finais do EEE, Reino Unido e Suíça

A Política de consentimento do usuário da UE do Google exige que os anunciantes divulguem o seguinte aos seus usuários finais do EEE, Reino Unido e Suíça, bem como obtenham seu consentimento para isso:

* O uso de cookies ou outro armazenamento local onde legalmente exigido; e
* A coleta, compartilhamento e uso de seus dados pessoais para personalização de anúncios.

Isso não afeta os usuários finais dos EUA ou quaisquer outros usuários finais localizados fora do EEE, do Reino Unido ou da Suíça. Consulte sua equipe jurídica sobre a nova Política de consentimento do usuário da UE do Google para garantir que esteja coletando o consentimento adequado para usar os serviços do Google Ads para seus usuários finais do EEE, Reino Unido e Suíça.

De acordo com os requisitos da Lei de Mercados Digitais (DMA) em vigor a partir de 6 de março de 2024, os anunciantes devem aprovar o consentimento dos usuários finais do EEE, Reino Unido e Suíça ao compartilhar dados com o Google. Como parte dessa mudança, você pode coletar ambos os sinais de consentimento no Braze como os seguintes atributos personalizados booleanos:

* `$google_ad_user_data`
* `$google_ad_personalization`

Braze sincronizará os dados desses atributos personalizados com os [campos de consentimento apropriados no Google](https://support.google.com/google-ads/answer/14310715#:~:text=These%20consent%20fields%20are%3A).

#### Como gerenciar consentimento revogado

Para manter suas listas de público atualizadas no caso de um usuário final do EEE ter sido adicionado à lista de público e, em seguida, ter retirado qualquer um dos dois consentimentos (`$google_ad_user_data` ou `$google_ad_personalization`), você deve configurar um canva para remover usuários das listas de público existentes usando uma etapa do Audience Sync.

{% alert note %}
Se um EEA já tiver fornecido consentimento para ambos os sinais, esses dados continuarão a ser usados para a Correspondência de Clientes do Google até que essa lista expire, ou que o status de consentimento seja explicitamente atualizado via público do Google Sync, ou ambos.
{% endalert %}

#### Dicas

* Envie o valor como tipo booleano, não como string.
* Prefixe o cifrão ($) para o nome do atributo. Braze usa um cifrão no início de um nome de atributo para indicar que esta é uma chave especial e reservada.
* Digite o nome do atributo em letras minúsculas.
* Embora você não possa definir explicitamente um usuário como não especificado, se você enviar um valor `null` ou `nil` ou qualquer valor que não seja `true` ou `false`, a Braze passará esse usuário para o Google como `UNSPECIFIED`.
* Novos usuários adicionados ou atualizados sem especificar qualquer atributo de consentimento serão sincronizados com o Google com esses atributos de consentimento marcados como não especificados.

Se tentar sincronizar um usuário do EEE sem os campos de consentimento necessários e o status concedido, o Google rejeitará a tentativa e não exibirá anúncios para esse usuário. Além disso, se um anúncio for exibido a um usuário do EEE sem o seu consentimento explícito, você pode ser responsabilizado e correr risco financeiro. Para evitar isso, sugerimos o envio de campanhas com filtros de segmento que incluam apenas usuários do EEE, Reino Unido e Suíça com atribuições de consentimento do Google com `true`. Para mais detalhes sobre a Política de Consentimento do Usuário da UE para parceiros da segmentação por lista de clientes, consulte as [perguntas frequentes](https://support.google.com/google-ads/answer/14310715) do Google.

### Configurando seu Canvas

Após a sincronização com o Braze, as seguintes atribuições de consentimento estarão disponíveis em seus perfis de usuário e para segmentação:

- `$google_ad_user_data`
- `$google_ad_personalization`

Em qualquer Canva em que esteja direcionando usuários finais do EEE, Reino Unido e Suíça usando o Google Audience Sync para adicionar usuários a um público, será necessário excluir esses usuários sempre que ambas as atribuições de consentimento tiverem qualquer valor que não seja `true`. Isso pode ser feito segmentando esses usuários quando os valores de consentimento são definidos como `true`. Isso também garante que as análises de dados mais precisas dos usuários sejam sincronizadas, pois sabemos que o Google rejeitará esses usuários do público. Note que, se estiver usando o Google Audience Sync para remover usuários de um público, as atribuições de consentimento não serão necessárias.

## Integração

### Etapa 1: conecte a conta do Google

Para começar, acessar **Integrações de Parceiros** > **Parceiros de Tecnologia** > **Google Ads** e selecionar **Conectar Google Ads**. Você será solicitado com um modal para selecionar o e-mail associado à sua conta do Google Ads e, em seguida, conceder acesso ao Braze à sua conta do Google Ads.

{% alert note %}
Se você estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), você pode encontrar **Parceiros de Tecnologia** em **Integrações**.
{% endalert %}

Depois de conectar com sucesso sua conta do Google Ads, você voltará automaticamente à sua página de parceiro do Google Ads. Em seguida, você precisará selecionar quais contas de anúncios gostaria que fossem acessadas dentro do espaço de trabalho da Braze.

![]({% image_buster /assets/img/google_sync/googlesync.gif %}){: style="max-width:85%;"}

{% alert important %}
Se você planeja exportar IDFA ou IDs de publicidade do Google do iOS pela sincronização de público, o Google exige o ID do app para iOS e Android nas solicitações. Em Google Audience Sync, selecione **Add Mobile Advertising IDs**, insira o ID do aplicativo iOS e o ID do aplicativo Android (nome do pacote do aplicativo) e salve cada um.
<br><br>
![A página de tecnologia atualizada do Google Ads mostrando as contas de anúncios conectadas. Aqui você pode sincronizar de novo contas e adicionar IDs de publicidade móvel.]({% image_buster /assets/img/google_sync/google_sync5.png %}){: style="max-width:75%;"}
{% endalert %}

### Etapa 2: adicione uma etapa Google Audience no Canvas Flow

Adicione um componente na sua canva e selecione **Sincronização de público**.

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### Etapa 3: Configuração de sincronização

Clique no botão **Público personalizado** para abrir o editor de componentes.

Selecione **Google** como o parceiro de sincronização de público desejado.

![][19]{: style="max-width:80%;"}

Selecione a conta de anúncio do Google desejada. No menu suspenso **Escolha um público novo ou existente**, digite o nome de um público novo ou existente. 

{% tabs %}
{% tab Criar um novo público %}
**Crie um Novo Público**<br>
Digite um nome para o novo público personalizado, selecione **Adicionar Usuários ao Público** e selecione quais campos você gostaria de sincronizar com o Google. Você pode selecionar os seguintes campos para sincronizar com o Google:

- E-mail 
- Telefone
- Nome e sobrenome
- Cidade
- País
- Data de nascimento
- Gênero
- IDs de anúncios para dispositivos móveis
  - Você deve optar pela coleta de [IDFA]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection) ou [GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection#google-advertising-id-android-only) através dos SDKs da Braze.

Digite um nome para o novo público personalizado, selecione **Adicionar Usuários ao Público** e selecione os dados do campo de usuário de primeira parte para enviar com seu público. Você pode escolher qualquer um:

- **Informações de contato do cliente**: Contém o e-mail ou os números de telefone de seus usuários, ou ambos se existirem no Braze
- **ID de anunciante móvel**: selecione iOS IDFA ou Android GAID

Em seguida, salve seu público clicando no botão **Criar Público** na parte inferior do editor de etapas.

![Vista expandida do componente de Canva de Público Personalizado. Aqui a conta de anúncio desejada está selecionada, um novo público é criado e a caixa de seleção "Informações de contato do cliente" está selecionada.]({% image_buster /assets/img/audience_sync/g_sync.png %})

Os usuários serão notificados no topo do editor de etapas se o público for criado com sucesso ou se ocorrerem erros durante este processo. Os usuários podem referenciar este público para remoção de usuários mais tarde na jornada do Canva porque o público foi criado no modo de rascunho. 

![Um alerta que aparece depois que um novo público é criado no componente do canva.]({% image_buster /assets/img/audience_sync/g_sync3.png %})

Quando você lança uma canva com um novo público, a Braze criará um novo público personalizado ao lançar a canva e, subsequentemente, sincronizará os usuários em quase tempo real à medida que eles entrarem no componente do público do Google. 

{% alert important %}
De acordo com os requisitos da segmentação por lista de clientes do Google, você não pode ter informações de contato de clientes e IDs de anunciantes móveis nas mesmas listas de clientes. A segmentação por lista de clientes do Google usará essas informações para determinar quem pode ser segmentado no Google Search, Google Display, YouTube e Gmail. Para mais detalhes sobre os requisitos da segmentação por lista de clientes do Google, revise sua [documentação](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507).
{% endalert %}
{% endtab %}
{% tab Sincronização com um público existente %}
**Sincronizar com um Público Existente**<br>
A Braze também oferece a capacidade de adicionar ou remover usuários de listas de clientes do Google existentes para garantir que esses públicos estejam atualizados. Para sincronizar com um público existente, selecione um público personalizado existente para sincronizar e, em seguida, escolha se deseja **Adicionar ao público** ou **Remover do público**. Em seguida, a Braze adiciona ou remove usuários em tempo quase real à medida que eles entram na etapa do Google Audience. 

Depois de configurar sua etapa do Google Audience, selecione **Done** (Concluído). Sua etapa do Google Audience incluirá detalhes sobre o novo público.

![Vista expandida do componente de Canva de Público Personalizado. Aqui a conta de anúncios desejada e o público existente estão selecionados, assim como o botão "Adicionar usuário ao público".]({% image_buster /assets/img/audience_sync/g_sync2.png %})

{% endtab %}
{% endtabs %}

### Etapa 4: Lançar canva

Complete o restante da sua jornada de usuário dentro do canva e depois é só abri-lo! Se você optou por criar um novo público, a Braze criará o público no Google e, em seguida, adicionará usuários à medida que eles alcançarem esta etapa no seu canva. Se você selecionou adicionar ou remover usuários de um público existente, a Braze adicionará ou removerá usuários quando eles alcançarem esta etapa em sua jornada de usuário.

Os usuários então avançarão para o próximo componente da canva, se houver um, ou sairão da canva se for a última etapa da jornada do usuário. 

## Considerações sobre sincronização de usuário e limite de frequência

À medida que os usuários alcançam o componente Audience Sync, a Braze os sincronizará em tempo quase real, respeitando os limites de frequência da API do Google Ads. Na prática, isso significa que a Braze tentará agrupar e processar o maior número possível de usuários a cada 5 segundos antes de enviar esses usuários para o Google. 

Quando um cliente estiver perto de atingir o limite de frequência da API do Google Ads, o Google fornecerá feedback à Braze sobre recomendações de nova tentativa. Se um cliente da Braze atingir seu limite de frequência, Braze o canva tentará sincronizar novamente por até ~13 horas. Se a sincronização não for possível, esses usuários são listados na métrica de Usuários com Erro.

## Detalhes da análise de dados 

A tabela a seguir inclui métricas e descrições para ajudá-lo a entender melhor a análise de dados do seu público na etapa de sincronização de público.

| Métrica | Descrição |
| ------ | ----------- |
| *Entraram* | Número de usuários que entraram nesta etapa para serem sincronizados com o Google. |
| *Avançaram para a etapa seguinte* | Quantos usuários avançaram para o próximo componente, se houver um. Todos os usuários avançarão automaticamente. Se esta for a última etapa no ramo do canva, esta métrica será 0. |
| *Usuários sincronizados* | Número de usuários que foram sincronizados com sucesso com o Google. |
| *Usuário não sincronizado* | Número de usuários que não foram sincronizados devido a campos ausentes para corresponder ou o atributo de consentimento foi definido como `false`. |
| *Usuários com erro* | Número de usuários que não foram sincronizados com o Google devido a um erro, após ~13 horas de tentativas. Para erros específicos, como interrupções no serviço da API do Google Ads, o canva tentará sincronizar novamente por até ~13 horas. Se a sincronização ainda não for possível nesse ponto, o *Usuário Não Sincronizado* será preenchido. |
| *Usuários pendentes* | Número de usuários atualmente sendo processados pela Braze para sincronizar com o Google. |
| *Saíram do canva* | Número de usuários que saíram da canva. Isso ocorre quando a última etapa em um canva é uma etapa do Google. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Solução de problemas

{% details Por que não posso selecionar vários campos para corresponder na configuração da etapa do público do Google? %}
A segmentação por lista de clientes do Google tem requisitos rigorosos sobre como esses públicos são formatados e quais informações do cliente são incluídas. Especificamente, os IDs de anunciantes móveis precisam ser carregados separadamente das informações de contato do cliente (como e-mail e número de telefone). Para mais detalhes, consulte a [documentação sobre segmentação por lista de clientes do Google](https://support.google.com/google-ads/answer/7659867?hl=en#undefined).
{% enddetails %}

{% details Quanto tempo levará para meus públicos sincronizarem no Google? %}
Pode levar de 6 a 12 horas para um público ser sincronizado no Google.
{% enddetails %}

{% details Eu sincronizei um público, mas o tamanho do público no Google é zero. %}
Para fins de privacidade, o tamanho da lista de usuários mostrará zero até que a lista tenha pelo menos **1.000 membros**. Depois disso, o tamanho será arredondado para os dois dígitos mais significativos.
{% enddetails %}

{% details Eu sincronizei um público no Google, mas meus anúncios não estão sendo exibidos. %}
Verifique se seus públicos contêm pelo menos **5.000** usuários para garantir que os anúncios comecem a ser exibidos.
{% enddetails %}

{% details Como resolver o erro "IDs de app móvel excluídos"? %}
Se você estiver sincronizando públicos com o Google, esse erro será disparar se você tiver selecionado sincronizar identificadores móveis como parte de suas sincronizações, mas excluiu seus IDs de app móvel da página de parceiros do Google.
Para resolver esse problema, certifique-se de que você adicionou os IDs apropriados do app móvel para iOS e Android na página de parceiros do Google.
{% enddetails %}

[1]: {% image_buster /assets/img/google_sync/google_sync1.png %}
[2]: {% image_buster /assets/img/google_sync/google_sync2.png %}
[3]: {% image_buster /assets/img/google_sync/google_sync3.png %}
[4]: {% image_buster /assets/img/google_sync/google_sync4.png %}
[6]: {% image_buster /assets/img/google_sync/google_sync6.png %}
[8]: {% image_buster /assets/img/google_sync/google_sync8.png %}
[13]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
[21]: {% image_buster /assets/img/audience_sync/g_sync.png %}
[22]: {% image_buster /assets/img/audience_sync/g_sync2.png %}
[23]: {% image_buster /assets/img/audience_sync/g_sync3.png %}
