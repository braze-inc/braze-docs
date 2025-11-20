---
nav_title: Consciência de recursos e nova versão do aplicativo
article_title: Consciência de Recursos e Nova Versão do Aplicativo
page_order: 9
page_type: reference
description: "Este artigo de referência discute como manter seus usuários informados e empolgados sobre quando você lança novos recursos ou versões."
tool: Campaigns

---

# Consciência de recursos e nova versão do aplicativo

> Este artigo de referência aborda como usar a plataforma Braze para manter seus clientes atualizados sobre novos recursos e versões do seu aplicativo. 

Você trabalha duro para atualizar e melhorar continuamente seu aplicativo, e deseja que seus usuários experimentem esses novos recursos empolgantes e novas versões do aplicativo. Aprenda como ensinar seus usuários sobre os novos recursos que eles ainda não usaram e incentive-os a explorar o aplicativo para aproveitar ao máximo o que você tem a oferecer.

Campanhas de conscientização de recursos são uma ótima maneira de incentivar os usuários a se manterem engajados com seu aplicativo enquanto você continua a melhorar a funcionalidade do seu aplicativo.  Manter os usuários atualizados é uma ótima maneira de mantê-los ativos, aumentar as classificações e garantir o engajamento do usuário.

## Filtrando pelas versões mais recentes do aplicativo

Os SDKs da Braze rastreiam automaticamente a versão mais recente do aplicativo de um usuário. Essas versões podem ser usadas em filtros e segmentos para determinar quais usuários devem receber uma mensagem ou campanha.

\![O painel de Opções de Segmentação na etapa de Usuários Alvo no fluxo de trabalho de construção de campanha. A seção Filtros Adicionais inclui o seguinte filtro "O Número da Versão Mais Recente do Aplicativo para Android Stopwatch (Android) está abaixo de 3.7.0 (134.0.0.0)".]({% image_buster /assets/img_archive/new_app_version.png %}){: style="max-width:90%;"}

{% alert note %}
Pode levar tempo para que as versões atuais do aplicativo sejam populadas. A versão do aplicativo no perfil do usuário é atualizada quando as informações são capturadas pelo SDK, que depende de quando os usuários abrem seus aplicativos. Se o usuário não abrir o aplicativo, a versão atual não será atualizada. <br><br> Esses filtros também não se aplicarão retroativamente. É bom usar "maior que" ou "igual" às versões atuais e futuras, mas usar filtros de versões passadas pode causar comportamentos inesperados.
{% endalert %}

### Número da versão do aplicativo

Use o filtro **Versão do App** para segmentar usuários pela versão e número de compilação do aplicativo. 

Este filtro suporta comparações numéricas para direcionar uma faixa de versões de aplicativos. Por exemplo, você pode direcionar usuários cujo aplicativo está "abaixo", "acima" e "igual a" versão do aplicativo "1.2.3", o que pode ser benéfico para promover um novo recurso que requer uma atualização do aplicativo.

Este novo filtro pode substituir o filtro legado "Nome da Versão do App" que exigiria listar explicitamente cada versão anterior ou usar uma expressão regular.

**Como funciona**

* Cada parte da versão `major.minor.patch` enviada na versão do aplicativo é comparada como inteiros.
* Se os números principais forem iguais, os números menores são comparados, etc.

**Importante**

* Os aplicativos Android têm tanto uma [`versionName`](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) legível por humanos quanto uma [`versionCode`](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()) interna. O filtro de Número da Versão do App usa `versionCode` porque é garantido que será incrementado com cada lançamento na loja de aplicativos.
* Isso pode causar confusão quando a `versionName` e a `versionCode` do seu aplicativo ficam fora de sincronia, especialmente porque ambos os campos podem ser visualizados no painel do Braze. Como uma boa prática, verifique se a `versionName` e a `versionCode` do seu aplicativo são incrementadas juntas.
* Se você precisar filtrar pelo campo legível por humanos `versionName` em vez disso (pouco comum), use o filtro Nome da Versão do App.

#### Requisitos do SDK

Os valores para este filtro são coletados a partir do Braze Android SDK v3.6.0+ e iOS SDK v3.21.0+. Mesmo que este filtro tenha requisitos de SDK, você ainda poderá direcionar usuários que estão em versões mais baixas (mais antigas) do seu aplicativo usando este recurso!

Para Android, este número da versão é baseado no [Código Longo da Versão do Pacote](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()) para o aplicativo.

Para iOS, este número da versão é baseado na [String da Versão Curta](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) para o aplicativo.

{% alert tip %}
Este filtro irá preencher valores após os usuários atualizarem seus aplicativos para as Versões do SDK Braze suportadas. Até lá, o filtro não mostrará nenhuma versão quando selecionado.
{% endalert %}

#### Caso de uso

No cenário a seguir, vamos supor que você primeiro atualizou para os SDKs do Braze que suportam este filtro na versão `2.0.0` do seu aplicativo.

Uma vez que o Braze recebe dados da versão 2.0.0 do seu aplicativo, você pode segmentar usuários com versões anteriores ou posteriores.

| Filtro  | Versão do aplicativo do usuário  | Resultado |
:------------- | :----------- | :---------|
| Menos que 2.0.0 | 1.0.0 | O usuário está no segmento, mesmo que seu SDK do Braze não tenha suportado o filtro "Número da Versão do Aplicativo". |
| Maior que 2.0.0 | 2.5.1 | O usuário e todas as futuras instalações estarão no segmento. |
| Maior que 2.0.0 | 1.9.9 | O usuário não está no segmento. |
| Menos ou igual a 2.0.0 | 3.0.1 | O usuário não está no segmento. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Nome da versão do aplicativo

Use o filtro "Nome da Versão do Aplicativo" para segmentar usuários pelo "nome da versão" visível ao usuário do aplicativo. 

Este filtro suporta correspondência com "é", "não é" e expressões regulares. Por exemplo, você pode direcionar usuários que têm um aplicativo que não é a versão "1.2.3-test-build".

Para Android, esse nome de versão é baseado no [Nome da Versão do Pacote](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) para o aplicativo. Para iOS, esse nome de versão é baseado no [String da Versão Curta](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) para o aplicativo.

### Não usou o recurso

Quando você lança uma nova versão do aplicativo e introduz novos recursos, os usuários podem não notar o novo conteúdo. Executar uma campanha de conscientização sobre recursos é uma ótima maneira de ensinar os usuários sobre novos recursos ou recursos que eles nunca usaram. Para fazer isso, você deve criar um [atributo personalizado]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#custom-data) que é atribuído a usuários que nunca completaram uma determinada ação dentro do seu aplicativo ou usar um [evento personalizado]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#custom-data) para rastrear uma ação específica. Você pode usar esse atributo (ou evento) para segmentar os usuários que deseja enviar a campanha.

{% alert tip %}
Procurando redirecionar uma parte específica do seu público? Confira [Campanhas de Redirecionamento]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/) para aprender como redirecionar campanhas aproveitando as ações anteriores do seu usuário.
{% endalert %}


