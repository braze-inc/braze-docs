# Perguntas frequentes

> Este artigo fornece respostas a algumas perguntas frequentes sobre os Feature Flags.

## Funcionalidade e suporte

### Em quais plataformas os feature flags da Braze podem ser usados? {#platforms}

A Braze oferece suporte a feature flags nas plataformas iOS, Android e Web com os seguintes requisitos de versão do SDK:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

Você precisa de suporte em outras plataformas? Envie um e-mail para nossa equipe: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

### Qual é o nível de esforço envolvido na implementação de um Feature Flag? {#level-of-effort}

Um Feature Flag pode ser criado e integrado em poucos minutos. 

A maior parte do esforço envolvido estará relacionada à sua equipe de engenharia que está desenvolvendo o novo recurso que você planeja implementar. Mas quando se trata de adicionar um sinalizador de recurso, é tão simples quanto uma declaração `IF`/`ELSE` no código do seu app ou site:

{% tabs %}
{% tab JavaScript %}

```javascript
import { getFeatureFlag } from "@braze/web-sdk";

if (getFeatureFlag("new_shopping_cart").enabled) {
    // Show the new homepage your team has built
}
else {
    // Show the old homepage
}
```

{% endtab %}
{% tab Java %}

```java
if (braze.getFeatureFlag("new_shopping_cart").getEnabled()) {
  // Show the new homepage your team has built
} else {
  // Show the old homepage
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
if (braze.getFeatureFlag("new_shopping_cart")?.enabled == true) {
  // Show the new homepage your team has built
} else {
  // Show the old homepage
}
```

{% endtab %}
{% endtabs %}

### Como os sinalizadores de recursos podem beneficiar as equipes de marketing? {#marketing-teams}

As equipes de marketing podem usar sinalizadores de recursos para coordenar anúncios de produtos (como e-mails de lançamento de produtos) quando um recurso é ativado apenas para uma pequena porcentagem de usuários.

Por exemplo, com os sinalizadores de recursos do Braze, você pode implementar um novo programa de fidelidade do cliente para 10% dos usuários do seu app e enviar um e-mail, push ou outra mensagem para esses mesmos 10% de usuários ativados usando a etapa do sinalizador de recursos do Canva. 

### Como os sinalizadores de recursos podem beneficiar as equipes de produtos? {#product-teams}

As equipes de produto podem usar sinalizadores de recursos para realizar implementações graduais ou lançamentos suaves de novos recursos a fim de monitorar os indicadores-chave de desempenho e o feedback dos clientes antes de disponibilizá-los para todos os usuários.

As equipes de produtos podem usar [as propriedades do feature flag]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#properties) para preencher remotamente o conteúdo de um app, como deep linking, texto, imagens ou outro conteúdo dinâmico.

Usando a etapa do Canva Feature Flag, as equipes de produto também podem executar um teste A/B dividido para medir como um novo recurso afeta as taxas de conversão em comparação com os usuários com o recurso desativado. 

### Como os sinalizadores de recursos podem beneficiar as equipes de engenharia? {#engineering-teams}

As equipes de engenharia podem usar sinalizadores de recursos para reduzir o risco inerente ao lançamento de novos recursos e evitar a pressa de implantar correções de código no meio da noite.

Ao liberar um novo código oculto por trás de um sinalizador de recurso, sua equipe pode ativar ou desativar o recurso remotamente a partir do dashboard do Braze, evitando a postergação de push de um novo código ou a espera pela aprovação de uma atualização na loja de aplicativos.

## Implementação e direcionamento de recursos

### Um Feature Flag pode ser implementado apenas para um grupo seleto de usuários? {#target-users}

Sim, crie um segmento na Braze que direcione usuários específicos por endereço de e-mail, `user_id` ou qualquer outra atribuição em seus perfis de usuário. Em seguida, implante o Feature Flag em 100% desse segmento.

### Como o ajuste da porcentagem de distribuição afeta os usuários que foram previamente agrupados no grupo ativado? {#random-buckets}

As implementações de Feature Flag permanecem consistentes para os usuários em todos os dispositivos e sessões.

- Quando um sinalizador de recurso é implementado em 10% dos usuários aleatórios, esses 10% permanecerão ativados e persistirão durante a vida útil desse sinalizador de recurso.
- Se você aumentar a distribuição de 10% para 20%, os mesmos 10% permanecerão capacitados, além de um novo grupo adicional de 10% de usuários que serão adicionados ao grupo capacitado.
- Se você reduzir a distribuição de 20% para 10%, apenas os 10% originais dos usuários permanecerão ativados.

Essa estratégia ajuda a garantir que os usuários tenham uma experiência consistente no app e não fiquem alternando entre as sessões. Obviamente, a desativação de um recurso até 0% removerá todos os usuários do sinalizador de recurso, o que é útil se você descobrir um bug ou precisar desativar o recurso por completo.

## Tópicos técnicos

### Os Feature Flags podem ser usados para controlar quando o SDK da Braze é inicializado? {#initialization}

Não, o SDK deve ser inicializado para baixar e sincronizar os feature flags para o usuário atual. Isso significa que não é possível usar sinalizadores de recursos para limitar quais usuários são criados ou rastreados no Braze.

### Com que frequência o SDK atualiza os feature flags? {#refresh-frequency}

Os Feature Flags são atualizados no início da sessão e ao mudar os usuários ativos. Os Feature Flags também podem ser atualizados manualmente usando o [método de atualização]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#refreshing) do SDK. As atualizações do Feature Flag estão limitadas de frequência a uma vez a cada cinco minutos (sujeito a alterações).

Lembre-se de que as boas práticas de dados recomendam não atualizar os sinalizadores de recursos muito rapidamente (com possível limite de frequência se isso for feito), portanto, é melhor atualizar apenas antes que um usuário interaja com novos recursos ou periodicamente no app, se necessário.

### Os Feature Flags estão disponíveis enquanto o usuário estiver off-line? {#offline}

Sim, depois que os Featureags são atualizados, eles são armazenados localmente no dispositivo do usuário e podem ser acessados off-line.

### O que acontece se os sinalizadores de recursos forem atualizados no meio da sessão? {#listen-for-updates}

Os Feature Flags podem ser atualizados no meio da sessão. Há cenários em que você pode querer atualizar seu app se determinadas variáveis ou sua configuração forem alteradas. Há outros cenários em que talvez você não queira atualizar seu app, para evitar uma mudança chocante na forma como a interface do usuário é renderizada.

Para controlar isso, [ouça as atualizações]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#updates) dos sinalizadores de recursos e determine se o app deve ser renderizado novamente com base em quais sinalizadores de recursos foram alterados. 

### Por que os usuários do meu grupo de controle global não estão recebendo experimentos de sinalizadores de recursos?

Não é possível ativar sinalizadores de recursos para usuários do seu [grupo de controle global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/). Isso significa que os usuários do seu grupo de controle global também não podem fazer parte dos experimentos do Feature Flag.

## Outras perguntas?

Tem dúvidas ou comentários? Envie um e-mail para nossa equipe: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

