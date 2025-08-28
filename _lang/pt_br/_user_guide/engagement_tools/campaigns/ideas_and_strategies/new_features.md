---
nav_title: Conscientização sobre os recursos e a nova versão do app
article_title: Conscientização sobre os recursos e a nova versão do app
page_order: 9
page_type: reference
description: "Este artigo de referência discute como manter os usuários informados e entusiasmados com o lançamento de novos recursos ou versões."
tool: Campaigns

---

# Reconhecimento de recursos e nova versão do app

> Este artigo de referência aborda como usar a plataforma Braze para manter seus clientes atualizados sobre novos recursos e versões de seu app. 

Você trabalha arduamente para atualizar e melhorar continuamente seu aplicativo e deseja que seus usuários experimentem esses novos recursos e novas versões do app. Saiba como ensinar seus usuários sobre os novos recursos que eles ainda não usaram e incentive-os a explorar o app para obter o máximo que você tem a oferecer.

As campanhas de conscientização de recursos são uma ótima maneira de incentivar os usuários a permanecerem engajados com o seu app à medida que você continua a melhorar a funcionalidade do aplicativo.  Manter os usuários atualizados é uma ótima maneira de mantê-los ativos, aumentar as taxas de engajamento e garantir o envolvimento do usuário.

## Filtragem por versões mais recentes do app

Os SDKs do Braze rastreiam automaticamente a versão mais recente do app de um usuário. Essas versões podem ser usadas em filtros e segmentos para determinar quais usuários devem receber uma mensagem ou campanha.

![O painel Opções de direcionamento na etapa Usuários-alvo no fluxo de trabalho de criação de campanhas. A seção Filtros adicionais inclui o seguinte filtro "O número da versão mais recente do app para Android Stopwatch (Android) é inferior a 3.7.0 (134.0.0.0)".]({% image_buster /assets/img_archive/new_app_version.png %}){: style="max-width:90%;"}

### Número da versão do app

Use o filtro **App Version Number** para segmentar os usuários pela versão e pelo número de compilação do app. 

Esse filtro suporta comparações numéricas para direcionamento de uma gama de versões de aplicativos. Por exemplo, você pode direcionar os usuários cujo aplicativo está "abaixo", "acima" e "igual" à versão do aplicativo "1.2.3", o que pode ser benéfico para promover um novo recurso que requer um upgrade do aplicativo.

Esse novo filtro pode substituir o antigo filtro "App Version Name", que exigiria a listagem explícita de cada versão mais antiga ou o uso de uma expressão regular.

**Como funciona?**

* Cada parte da versão do `major.minor.patch` enviada na versão do app do seu aplicativo é comparada como números inteiros
* Se os números maiores forem iguais, os números menores serão comparados, etc.

**Importante**

* Os apps para Android têm um arquivo legível por humanos [`versionName`](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) legível por humanos e um [`versionCode`](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()). O filtro Número da versão do app usa `versionCode` porque é garantido que ele seja incrementado a cada lançamento da loja de aplicativos.
* Isso pode causar confusão quando o `versionName` e o `versionCode` do seu app ficam fora de sincronia, especialmente porque ambos os campos podem ser visualizados no dashboard do Braze. Como prática recomendada, verifique se `versionName` e `versionCode` do seu app são incrementados juntos.
* Se, em vez disso, você precisar filtrar pelo campo `versionName` legível por humanos (incomum), use o filtro App Version Name.

#### Requisitos do SDK

Os valores para esse filtro são coletados a partir do Braze Android SDK v3.6.0+ e iOS SDK v3.21.0+. Mesmo que esse filtro tenha requisitos de SDK, você ainda poderá direcionar os usuários que estão em versões inferiores (mais antigas) do seu app usando esse recurso!

Para Android, esse número de versão é baseado no [código de versão longa](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()) do [pacote](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()) para o app.

Para iOS, esse número de versão é baseado na [Short Version String](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) do aplicativo.

{% alert tip %}
Esse filtro preencherá os valores depois que os usuários fizerem upgrade de seus apps para as versões suportadas do SDK da Braze. Até lá, o filtro não mostrará nenhuma versão quando selecionado.
{% endalert %}

#### Caso de uso

No cenário a seguir, vamos supor que você tenha feito upgrade para os SDKs da Braze, que oferecem suporte a esse filtro na versão `2.0.0` do seu app.

Quando a Braze receber dados da versão 2.0.0 do seu app, você poderá direcionar os usuários com versões anteriores ou posteriores.

| Filtrar  | Versão do app do usuário  | Resultado |
:------------- | :----------- | :---------|
| Menos de 2.0.0 | 1.0.0 | O usuário está no segmento, mesmo que o SDK da Braze não seja compatível com o filtro "App Version Number". |
| Maior que 2.0.0 | 2.5.1 | O usuário e todas as instalações futuras estarão no segmento. |
| Maior que 2.0.0 | 1.9.9 | O usuário não está no segmento. |
| Menor ou igual a 2.0.0 | 3.0.1 | O usuário não está no segmento. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Nome da versão do app

Use o filtro "App Version Name" para segmentar os usuários pelo "nome de compilação" do app voltado para o usuário. 

Esse filtro suporta correspondência com "is", "is not" e expressões regulares. Por exemplo, você pode direcionar usuários que tenham um app que não seja da versão "1.2.3-test-build".

No Android, esse nome de versão é baseado no [nome da versão do pacote](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) do app. Para iOS, esse nome de versão é baseado na [Short Version String](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) do app.

### Não utilizou o recurso

Quando você lança uma nova versão do app e introduz novos recursos, os usuários podem não notar o novo conteúdo. A execução de uma campanha de conscientização de recursos é uma ótima maneira de ensinar aos usuários sobre novos recursos ou sobre recursos que eles nunca usaram. Para isso, é necessário criar um [atributo personalizado]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#custom-data) atribuído aos usuários que nunca concluíram uma determinada ação no app ou usar um [evento personalizado]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#custom-data) para rastrear uma ação específica. Você pode usar essa atribuição (ou evento) para segmentar os usuários para os quais deseja enviar a campanha.

{% alert tip %}
Deseja redirecionar uma parte específica de seu público? Confira [Campanhas de redirecionamento]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/) para saber como redirecionar campanhas aproveitando as ações anteriores do usuário.
{% endalert %}


