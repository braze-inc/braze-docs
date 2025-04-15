---
nav_title: Coleta de IDFV
article_title: Coleta de IDFV
platform: Swift
page_type: reference
description: "Este artigo de referência descreve como coletar o campo IDFV opcional para o Swift SDK."
page_order: 4

---

# Coleta de IDFV 

## Fundo

Nas versões anteriores do SDK da Braze para iOS, o campo IDFV (Identifier for Vendor, identificador do fornecedor) era coletado automaticamente como o ID do dispositivo do usuário. A partir do Swift SDK v5.7.0, o campo IDFV foi opcionalmente desativado e, em vez disso, a Braze definiu um UUID aleatório como o ID do dispositivo. A partir do Swift SDK v7.0.0, o campo IDFV não será coletado por padrão, e um UUID será definido como o ID do dispositivo.

O recurso `useUUIDAsDeviceId` configura o [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) para definir o ID do dispositivo como um UUID. Tradicionalmente, o SDK do iOS atribuía a ID do dispositivo igual ao valor IDFV gerado pela Apple. Com esse recurso ativado por padrão em seu app iOS, todos os novos usuários criados por meio do SDK receberiam um ID de dispositivo igual a um UUID.

Se ainda desejar coletar o IDFV separadamente, você ainda poderá fazer isso por meio do Swift SDK, conforme descrito [aqui](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)).

## Considerações

### Versão do SDK

No Swift SDK v7.0.0+, quando `useUUIDAsDeviceId` estiver ativado (padrão), todos os novos usuários criados serão atribuídos a um ID de dispositivo aleatório. Todos os usuários existentes anteriormente manterão o mesmo valor de ID do dispositivo, que pode ter sido IDFV.

Quando esse recurso não estiver ativado, os dispositivos continuarão a ser atribuídos ao IDFV após a criação.

### Downstream 

**Parceiros tecnológicos**: Quando esse recurso for ativado, todos os parceiros de tecnologia que derivam o valor IDFV do ID do dispositivo Braze não terão mais acesso a esses dados. Se o valor IDFV derivado do dispositivo for necessário para a integração com parceiros, recomendamos que você defina esse recurso como verdadeiro.

**Currents**: `useUUIDAsDeviceId` definido como true significa que o ID do dispositivo enviado em Currents não será mais igual ao valor IDFV.

## Perguntas frequentes

#### Essa mudança afetará meus usuários existentes no Braze?
Não. Quando ativado, esse recurso não substituirá nenhum dado de usuário no Braze. Somente dispositivos recém-criados - ou depois que `wipedata()` for chamado - gerarão novos IDs de dispositivo UUID.

#### Posso desativar esse recurso depois de ativá-lo?
Sim, esse recurso pode ser ativado e desativado a seu critério. Os IDs de dispositivos armazenados anteriormente nunca serão substituídos.

#### Ainda posso capturar o valor do IDFV via Braze em outro lugar?
Sim, você ainda pode coletar opcionalmente o IDFV por meio do Swift SDK (a coleta está desativada por padrão). 
