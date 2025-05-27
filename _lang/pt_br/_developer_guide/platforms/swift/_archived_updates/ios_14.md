---
nav_title: Guia de atualização do iOS 14
article_title: Guia de atualização do SDK do iOS 14
page_order: 7
platform: iOS
description: "Este artigo de referência aborda a atualização do SDK do iOS 14, destacando alterações como geofences, direcionamento de local, IDFA e muito mais."
hidden: true
noindex: true
---

# Guia de atualização do SDK do iOS 14

> Este guia descreve as alterações relacionadas à Braze introduzidas no iOS 14 e as etapas de upgrade necessárias para sua integração do SDK da Braze para iOS. Para obter uma lista completa das novas atualizações do iOS 14, consulte a página da Apple sobre [o iOS 14](https://www.apple.com/ios/ios-14/).

{% alert tip %}
A partir do iOS 14.5, a coleta de **IDFA** e [determinados compartilhamentos de dados](https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track) exigirão o novo prompt de permissão da estrutura [AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency)[(saiba mais](#idfa)).
{% endalert %}

#### Resumo das mudanças significativas no iOS 14

- Os apps com direcionamento para o iOS 14 / Xcode 12 devem usar nossa [versão oficial do iOS 14](https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.27.0).
- [O iOS não oferece mais suporte a](https://developer.apple.com/documentation/corelocation/cllocationmanager/3600215-accuracyauthorization) geofences para usuários que escolhem a nova permissão de _local aproximado_.
- O uso dos recursos de direcionamento "Último local conhecido" exigirá uma atualização para o Braze iOS SDK v3.26.1+ para compatibilidade com a permissão de _local aproximado_. Note que, se estiver usando o Xcode 12, será necessário fazer upgrade para, pelo menos, a versão 3.27.0.
- A partir do iOS 14.5, a coleta de IDFA e [determinados compartilhamentos de dados](https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track) exigem o novo prompt de permissão da estrutura [AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency).
- Se usar o campo "Rastreamento de anúncios ativado" para direcionamento de campanhas ou análise de dados, será necessário fazer upgrade para o Xcode 12 e usar a nova estrutura AppTrackingTransparency para informar o status de aceitação dos usuários.

## Resumo do upgrade

<style>
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2) {
    min-width:230px;
}
table td {
    word-break: break-word;
}
</style>

|Se o seu app usa:|Recomendação para fazer upgrade|Descrição|
|------|--------|---|
|Xcode 12|**Faça upgrade para o iOS SDK v3.27 ou posterior**|Os clientes que usam o Xcode 12 devem usar a versão 3.27.0+ para compatibilidade. Se você tiver algum problema ou dúvida relacionada à nossa compatibilidade com o iOS 14, abra um novo [tópico no GitHub](https://github.com/Appboy/appboy-ios-sdk/issues).|
|Local mais recente| **Faça upgrade para o iOS SDK v3.26.1 ou posterior**|Se você usa o recurso de direcionamento para o local mais recente e ainda está usando o Xcode 11, deve fazer upgrade para, pelo menos, o iOS SDK v3.26.1, que oferece suporte ao novo recurso de _localização aproximada_. Os SDKs mais antigos não conseguirão coletar o local de forma confiável quando um usuário fizer upgrade para o iOS 14 _e_ escolher a opção "Localização aproximada".<br><br>Mesmo que seu app não seja direcionado ao iOS 14, seus usuários podem fazer upgrade para o iOS 14 e começar a usar a nova opção de precisão de local. Os apps que não fizerem upgrade para o iOS SDK v3.26.1+ não poderão coletar de forma confiável atribuições de local quando os usuários fornecerem sua _localização aproximada_ em dispositivos iOS 14.|
|ID de rastreamento de anúncios IDFA| **Pode ser necessário fazer upgrade para o Xcode 12 e o iOS SDK v3.27**|Em algum momento de 2021, a Apple começará a exigir uma solicitação de permissão para a coleta do IDFA. Nesse momento, os apps deverão fazer upgrade para o Xcode 12 e usar a nova estrutura `AppTrackingTransparency` para continuar coletando o IDFA. Se você passar o IDFA para o SDK da Braze, também deverá fazer upgrade para a versão 3.27.0+ no mesmo momento.<br><br>Os apps que não usarem as novas APIs do iOS 14 não poderão coletar o IDFA e, em vez disso, coletarão um ID em branco (`00000000-0000-0000-0000-000000000000`) depois que a Apple começar a aplicar essa alteração em 2021. Para saber se isso se aplica ou não ao seu app, consulte [os detalhes do IDFA](#idfa).|


## Mudanças de comportamento no iOS 14

### Permissão de local aproximado

![Localização precisa]({% image_buster /assets/img/ios/ios14-approximate-location.png %}){: style="float:right;max-width:45%;margin-left:15px;"}

#### Visão geral

Ao solicitar permissão de localização, os usuários agora terão a opção de fornecer seu _local preciso_ (comportamento anterior) ou o novo _local aproximado_. O local aproximado retornará um raio maior no qual o usuário está localizado, em vez de suas coordenadas exatas.

#### Geofences {#geofences}

[O iOS não oferece mais suporte a](https://developer.apple.com/documentation/corelocation/cllocationmanager/3600215-accuracyauthorization) geofences para usuários que escolhem a nova permissão de _local aproximado_. Embora não sejam necessárias atualizações para a integração do SDK do Braze, talvez seja necessário ajustar sua [estratégia de marketing baseada em local](https://www.braze.com/blog/geofencing-geo-targeting-beaconing-when-to-use/) para campanhas que dependem de geofences.

#### Direcionamento para a localização {#location-tracking}

Para continuar a coletar a _última localização conhecida_ dos usuários quando _a localização aproximada_ for informada, seu app precisará fazer upgrade para, no mínimo, a versão 3.26.1 da SDK da Braze para iOS. Lembre-se de que o local será menos preciso e, com base em nossos testes, tem sido de mais de 12.000 metros (mais de 7 milhas). Ao usar as opções de direcionamento do _último local conhecido_ no dashboard do Braze, certifique-se de aumentar o raio do local para levar em conta os novos _locais aproximados_ (recomendamos um raio de pelo menos 1 milha/1,6 km).

Os apps que não fizerem upgrade da SDK da Braze para iOS para pelo menos a versão 3.26.1 não poderão mais usar o monitoramento de localização quando _a localização aproximada_ for informada em dispositivos iOS 14.

Os usuários que já concederam acesso ao local continuarão a fornecer _a localização precisa_ após fazer o upgrade.

Note que, se estiver usando o Xcode 12, será necessário fazer upgrade para, pelo menos, a versão 3.27.0.

Para saber mais sobre a localização aproximada, assista ao vídeo da Apple [What's New In Location](https://developer.apple.com/videos/play/wwdc2020/10660/) WWDC.

### IDFA e transparência no rastreamento de aplicativos {#idfa}

#### Visão geral

O IDFA (Identifier for Advertisers) é um identificador fornecido pela Apple para uso com parceiros de publicidade e atribuição para rastreamento entre dispositivos e está vinculado ao ID Apple de um indivíduo.

A partir do iOS 14.5, um novo prompt de permissão (lançado pela nova estrutura `AppTrackingTransparency` ) deve ser exibido para coletar o consentimento explícito do usuário para o IDFA. Essa solicitação de permissão para "rastrear você em apps e sites de outras empresas" será solicitada de forma semelhante à solicitação de localização dos usuários.

Se um usuário não aceitar o prompt ou se você não fizer upgrade para a estrutura `AppTrackingTransparency` do Xcode 12, um valor IDFA em branco (`00000000-0000-0000-0000-000000000000`) será retornado e seu app não poderá solicitar o usuário novamente.

{% alert important %}
Essas atualizações do IDFA entrarão em vigor depois que os usuários finais fizerem upgrade de seus dispositivos para o iOS 14.5. Confira se o seu app está usando o novo `AppTransparencyFramework` com o Xcode 12 se você planeja coletar o IDFA.
{% endalert %}

#### Mudanças na coleção Braze IDFA
![IDFA]({% image_buster /assets/img/ios/ios14-idfa.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

1. O Braze continuará a permitir que os apps forneçam o valor IDFA de um usuário _ao_ SDK do Braze.

2. A macro de compilação `ABK_ENABLE_IDFA_COLLECTION`, que compilaria condicionalmente na coleta automática opcional de IDFA, não funcionará mais no iOS 14 e foi removida na versão 3.27.0. 

3. Se usar o campo "Rastreamento de anúncios ativado" para direcionamento de campanhas ou análise de dados, será necessário fazer upgrade para o Xcode 12 e usar a nova estrutura AppTrackingTransparency para informar o status de aceitação dos usuários. O motivo dessa alteração é que, no iOS 14, o antigo campo [`advertisingTrackingEnabled`](https://developer.apple.com/documentation/adsupport/asidentifiermanager/1614148-advertisingtrackingenabled) sempre retornará No.

4. Se o seu app tiver usado IDFA ou IDFV como ID externo da Braze, recomendamos fortemente que você migre desses identificadores em favor de um UUID. Para saber mais sobre a migração de IDs externas, consulte nossos [pontos de extremidade da API de migração de IDs externas]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/).

Leia mais sobre as [atualizações de privacidade](https://developer.apple.com/app-store/user-privacy-and-data-use/) da Apple e a nova [estrutura de transparência de rastreamento de aplicativos](https://developer.apple.com/documentation/apptrackingtransparency).

### Autorização push {#push-provisional-auth}

{% alert important %}
Nenhuma alteração na autorização provisória por push foi incluída no iOS 14. Em uma versão beta anterior do iOS 14, a Apple introduziu uma alteração que, desde então, foi revertida para o comportamento anterior.
{% endalert %}

## Novos recursos do iOS 14

### Visão geral da privacidade do app e da coleta de dados {#app-privacy}

Desde 8 de dezembro de 2020, todos os envios para a App Store exigem etapas adicionais para aderir aos [novos padrões de privacidade de aplicativos da Apple](https://developer.apple.com/app-store/app-privacy-details/).

#### Questionário do portal do desenvolvedor da Apple

No _Portal do desenvolvedor da Apple_:
* Será solicitado que você preencha um questionário para descrever como seu app ou parceiros de terceiros coletam dados.
  * Espera-se que o questionário esteja sempre atualizado com seu lançamento mais recente na App Store.
  * O questionário pode ser atualizado mesmo sem o envio de um novo app.
* Será necessário colar um link para o URL da Política de Privacidade do seu app.

Ao preencher seu questionário, consulte sua equipe jurídica e considere como o uso da Braze para os seguintes campos pode afetar seus requisitos de divulgação.

#### Coleta de dados padrão do Braze
**Identificadores** \- Um identificador de dispositivo anônimo é sempre coletado pelo Braze SDK. Atualmente, está definido como o IDFV (identificador do fornecedor) do dispositivo.

**Dados de uso** \- podem incluir dados de sessão do Braze, bem como qualquer evento ou coleta de atribuição que você use para medir a interação com o produto.

#### Coleta de dados opcional
Dados que você pode estar coletando opcionalmente por meio do uso do Braze:

**Localização** \- Tanto a localização aproximada quanto o local preciso podem ser coletados opcionalmente pelo SDK da Braze. Esses recursos são desativados por padrão.

**Informações de contato** \- Pode incluir eventos e atribuições relacionadas à identidade do usuário.

**Compras** \- Isso pode incluir eventos e compras registrados em nome do usuário.

{% alert important %}
Note que esta não é uma lista exaustiva. Se você coletar manualmente outras informações sobre seus usuários na Braze que se aplicam a outras categorias no Questionário de privacidade do app, também precisará divulgá-las.
{% endalert %}

Para saber mais sobre esse recurso, consulte [Privacidade e uso de dados da Apple](https://developer.apple.com/app-store/user-privacy-and-data-use/).

