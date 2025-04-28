---
nav_title: Sobre os Feature Flags
article_title: Sobre os Feature Flags
page_order: 1
description: "Este artigo de referência aborda uma visão geral dos feature flags, incluindo pré-requisitos e casos de uso."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web
  - Unity
  - Cordova
  - React Native
  - Flutter
  - Roku

---

# Sobre os Feature Flags

> Os Feature Flags permitem ativar ou desativar remotamente a capacitação de uma seleção específica ou aleatória de usuários. É importante ressaltar que eles permitem ativar e desativar um recurso na produção sem implementação adicional de código ou atualizações na App Store. Isso permite que você implemente novos recursos com segurança e confiança. 

Está procurando etapas sobre como criar um feature flag na Braze? Consulte [Criação de feature flags]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/).

## Pré-requisitos

Para usar os feature flags, confira se os seus SDKs estão atualizados com pelo menos essas versões mínimas:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

## Uso de feature flags

Use os Feature Flags para:

- [Introduzir implementações graduais](#gradual-rollouts)
- [Controle remotamente as variáveis do app](#remotely-control-app-variables)
- [Sincronize a implementação de recursos e o envio de mensagens](#message-coordination)
- [Experimente os novos recursos](#feature-experimentation)
- [Segmente os usuários por feature flags](#segmentation)

### Implementações graduais

Use os feature flags para ativar gradualmente os recursos em uma população de amostra. Por exemplo, você pode lançar um novo recurso para seus usuários VIP primeiro. Essa estratégia ajuda a reduzir os riscos associados ao envio de novos recursos para todos ao mesmo tempo e ajuda a detectar bugs com antecedência.

![Imagem em movimento do controle deslizante de tráfego de lançamento acessando de 0% a 100%.]({% image_buster /assets/img/feature_flags/feature-flags-rollout.gif %})

Por exemplo, digamos que decidimos adicionar um novo link "Live Chat Support" ao nosso app para agilizar o atendimento ao cliente. Poderíamos liberar esse recurso para todos os clientes de uma só vez. No entanto, um lançamento amplo traz riscos, como, por exemplo: 

* Nossa equipe de suporte ainda está em treinamento, e os clientes podem iniciar tickets de suporte após o lançamento. Isso não nos dá nenhuma margem de manobra caso a equipe de suporte precise de mais tempo.
* Não temos certeza do volume real de novos casos de suporte que receberemos, portanto, talvez não tenhamos a equipe adequada.
* Se nossa equipe de suporte estiver sobrecarregada, não temos nenhuma estratégia para desativar rapidamente esse recurso novamente.
* Pode haver bugs introduzidos no widget de bate-papo, e não queremos que os clientes tenham uma experiência negativa.

Com os feature flags da Braze, podemos implementar gradualmente o recurso e mitigar todos esses riscos:

* Ativaremos o recurso "Live Chat Support" quando a equipe de suporte disser que está pronta.
* Ativaremos esse novo recurso para apenas 10% dos usuários para determinar se estamos com a equipe adequada.
* Se houver algum erro, podemos desativar rapidamente o recurso em vez de nos apressarmos em enviar uma nova versão.

Para implementar gradualmente esse recurso, podemos [criar]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/) um feature flag chamado "Live Chat Widget".

![Detalhes do Feature Flag para um exemplo chamado Live Chat Widget. A ID é enable_live_chat. A descrição desse sinalizador de recurso indica que o widget de bate-papo ao vivo será exibido na página de suporte.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-livechat-1.png %})

Em nosso código do app, mostraremos o botão **Start Live Chat** somente quando a bandeira do recurso Braze estiver ativada:

```javascript
import {useState} from "react";
import * as braze from "@braze/web-sdk";

// Get the initial value from the Braze SDK
const featureFlag = braze.getFeatureFlag("enable_live_chat");
const [liveChatEnabled, setLiveChatEnabled] = useState(featureFlag.enabled);

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(() => {
    const newValue = braze.getFeatureFlag("enable_live_chat").enabled;
    setLiveChatEnabled(newValue);
});

// Only show the Live Chat if the Braze SDK determines it is enabled
return (<>
  Need help? <button>Email Our Team</button>
  {liveChatEnabled && <button>Start Live Chat</button>}
</>)

```

### Controle remotamente as variáveis do app

Use os sinalizadores de recursos para modificar a funcionalidade do seu app na produção. Isso pode ser particularmente importante para aplicativos móveis, em que as aprovações da loja de aplicativos impedem a implementação rápida de alterações para todos os usuários.

Por exemplo, digamos que nossa equipe de marketing queira listar nossas vendas e promoções atuais na navegação do app. Normalmente, nossos engenheiros exigem um prazo de uma semana para qualquer alteração e três dias para uma revisão da loja de aplicativos. Porém, com o Dia de Ação de Graças, a Black Friday, a Cyber Monday, o Hanukkah, o Natal e o Ano Novo em dois meses, não conseguiremos cumprir esses prazos apertados.

Com os sinalizadores de recursos, podemos permitir que o Braze controle o conteúdo do link de navegação do nosso app, permitindo que nosso profissional de marketing faça alterações em minutos, em vez de dias.

Para configurar remotamente esse recurso, criaremos um novo feature flag chamado `navigation_promo_link` e definiremos as seguintes propriedades iniciais:

![Feature Flag com propriedades de link e texto que direcionam para uma página de vendas genérica.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-1.png %})

Em nosso app, usaremos os métodos getter do Braze para recuperar as propriedades desse sinalizador de recurso e criar os links de navegação com base nesses valores:

```javascript
import * as braze from "@braze/web-sdk";
import {useState} from "react";

const featureFlag = braze.getFeatureFlag("navigation_promo_link");
// Check if the feature flag is enabled
const [promoEnabled, setPromoEnabled] = useState(featureFlag.enabled);
// Read the "link" property
const [promoLink, setPromoLink] = useState(featureFlag.getStringProperty("link"));
// Read the "text" property
const [promoText, setPromoText] = useState(featureFlag.getStringProperty("text"));

return (<>
  <div>
    <a href="/">Home</a>
    { promoEnabled && <a href={promoLink}>{promoText}</a> }
    <a href="/products">Products</a>
    <a href="/categories">Categories
  </div>
</>)
```

Agora, na véspera do Dia de Ação de Graças, só precisamos alterar esses valores de propriedade no dashboard da Braze.

![Feature Flag com propriedades de link e texto que direcionam para uma página de vendas do Dia de Ação de Graças.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-2.png %})

Como resultado, na próxima vez que alguém carregar o app, verá as novas ofertas de Ação de Graças.

### Coordenação de mensagens

Use sinalizadores de recursos para sincronizar a implementação e o envio de mensagens de um recurso. Isso permitirá que você use a Braze como a fonte da verdade para a experiência do usuário e o envio de mensagens relevantes. Para conseguir isso, direcione o novo recurso a um segmento específico ou a uma parte filtrada de seu público. Em seguida, crie uma campanha ou um canva direcionado somente a esse segmento. 

Digamos que estamos lançando um novo programa de fidelidade para nossos usuários. Pode ser difícil para as equipes de Marketing e Produto coordenar perfeitamente o momento do envio de mensagens promocionais com o lançamento de um recurso. Os sinalizadores de recursos no Canva permitem aplicar uma lógica sofisticada quando se trata de ativar um recurso para um público selecionado e controlar o envio de mensagens relacionadas a esses mesmos usuários.

Para coordenar efetivamente a implementação de recursos e o envio de mensagens, criaremos um novo feature flag chamado `show_loyalty_program`. Em nosso lançamento inicial em fases, deixaremos que o Canva controle quando e para quem o sinalizador de recurso será ativado. Por enquanto, deixaremos a porcentagem de implementação em 0% e não selecionaremos nenhum segmento de direcionamento.

![Uma bandeira de recurso com o nome Loyalty Rewards Program (Programa de fidelidade). O ID é show_loyalty_program, e a descrição é que isso mostra o novo programa de fidelidade na tela inicial e na página de perfil.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-loyalty.png %})

Em seguida, no Canvas Flow, criaremos uma [etapa do Feature Flag]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) que ativa o feature flag `show_loyalty_program` para nosso segmento "Clientes de alto valor":

![Um exemplo de um Canva com uma etapa do Audience Split em que o segmento de clientes de alto valor ativa o sinalizador do recurso show_loyalty_program.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-canvas-flow.png %})

Agora, os usuários desse segmento começarão a ver o novo programa de fidelidade e, depois que ele for ativado, um e-mail e uma pesquisa serão enviados automaticamente para ajudar nossa equipe a obter feedback.

### Experimentação de recursos

Use os sinalizadores de recursos para fazer experimentos e confirmar suas hipóteses sobre o novo recurso. Ao dividir o tráfego em dois ou mais grupos, você pode comparar o impacto de um sinalizador de recurso entre os grupos e determinar o melhor curso de ação com base nos resultados.

Um [teste A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) é uma ferramenta poderosa que compara as respostas dos usuários a várias versões de uma variável.

Neste exemplo, nossa equipe criou um novo fluxo de checkout para nosso app de comércio eletrônico. Embora estejamos confiantes de que ele está melhorando a experiência do usuário, queremos executar um teste A/B para medir seu impacto na receita do nosso app.

Para começar, criaremos um novo feature flag chamado `enable_checkout_v2`. Não adicionaremos um público ou porcentagem de implementação. Em vez disso, usaremos um experimento de sinalização de recurso para dividir o tráfego, ativar o recurso e medir o resultado.

Em nosso app, verificaremos se o sinalizador de recurso está ativado ou não e trocaremos o fluxo de checkout com base na resposta:

```javascript
import * as braze from "@braze/web-sdk";

const featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag?.enabled) {
  return <NewCheckoutFlow />  
} else {
  return <OldCheckoutFlow />
}
```

Configuraremos nosso teste A/B em um [Feature Flag Experiment]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments/).

Agora, 50% dos usuários verão a experiência antiga, enquanto os outros 50% verão a nova experiência. Em seguida, podemos analisar as duas variantes para determinar qual fluxo de checkout resultou em uma taxa de conversão mais alta. {% multi_lang_include metrics.md metric='Conversion Rate' %}

![Um experimento de Feature Flag que divide o tráfego em dois grupos de 50%.]({% image_buster /assets/img/feature_flags/feature-flag-use-case-campaign-experiment.png %})

Assim que determinarmos o vencedor, poderemos interromper essa campanha e aumentar a porcentagem de implementação do recurso para 100% para todos os usuários, enquanto nossa equipe de engenharia codifica isso em nossa próxima versão do app.

### Segmentação

Use o filtro **Feature Flag** para criar um segmento ou direcionar o envio de mensagens aos usuários com base no fato de eles terem ou não uma feature flag ativada. Por exemplo, digamos que temos um sinalizador de recurso que controla o conteúdo premium em nosso app. Poderíamos criar um segmento que filtrasse os usuários que não tivessem a Feature Flag ativada e, em seguida, enviar a esse segmento uma mensagem pedindo que fizessem upgrade da conta para ver o conteúdo premium.

![]({% image_buster /assets/img/feature_flags/feature_flag_segmentation_filter.png %})

Para saber mais sobre filtragem em segmentos, consulte [Criação de um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

{% alert note %}
Para evitar segmentos recursivos, não é possível criar um segmento que faça referência a outros feature flags.
{% endalert %}

## Limitações

A tabela a seguir descreve as limitações que se aplicam em um nível de sinalizador de recurso. Para adquirir a versão paga dos sinalizadores de recursos, entre em contato com o gerente da sua conta Braze ou solicite um upgrade no dashboard do Braze.

| Área de limitação                                                                                                   | Versão gratuita     | Versão paga      |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| [Feature Flags ativos](#active-feature-flags)                                                                     | 10 por espaço de trabalho | 110 por espaço de trabalho |
| [Experimentos de campanha ativos]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments/)          | 1 por espaço de trabalho  | 100 por espaço de trabalho |
| [Etapas do canva do Feature Flag]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) | Ilimitado        | Ilimitado         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Feature Flags ativos

Uma feature flag é considerada ativa e contará para o seu limite se qualquer uma das seguintes situações se aplicar:

- A implementação é superior a 0%
- Usado em uma tela ativa
- Usado em um experimento ativo

Mesmo que o mesmo sinalizador de recurso corresponda a vários critérios, por exemplo, se for usado em uma tela e a implementação for de 50%, ele contará apenas como 1 sinalizador de recurso ativo para o seu limite.

