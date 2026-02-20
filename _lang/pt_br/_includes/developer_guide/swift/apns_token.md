Antes de enviar uma notificação por push para iOS usando Braze, você precisa fazer upload do seu arquivo de notificação por push `.p8`, conforme descrito na [documentação do desenvolvedor da Apple](https://developer.apple.com/documentation/usernotifications/establishing-a-token-based-connection-to-apns):

1. Na sua conta de desenvolvedor da Apple, acesse [**Certificados, Identificadores & Perfis**](https://developer.apple.com/account/ios/certificate).
2. Em **Chaves**, selecione **Todos** e clique no botão adicionar (+) no canto superior direito.
3. Em **Descrição da Chave**, insira um nome único para a chave de assinatura.
4. Em **Serviços Principais**, selecione a caixa de seleção **serviço de Notificações por Push da Apple (APNs)**, depois clique em **Continuar**. Clique **Confirmar**.
5. Nota o ID da chave. Clique em **baixar** para gerar e baixar a chave. Certifique-se de salvar o arquivo baixado em um local seguro, pois você não pode baixar isso mais de uma vez.
6. No Braze, acessar **Configurações** > **Configurações do app** e fazer upload do arquivo `.p8` em **Certificado de Push da Apple**. Você pode fazer upload do seu certificado de push de desenvolvimento ou de produção. Para testar notificações por push depois que seu app estiver disponível na App Store, é recomendável configurar um espaço de trabalho separado para a versão de desenvolvimento do seu app.
7. Quando solicitado, insira o [ID do pacote](https://developer.apple.com/documentation/foundation/nsbundle/1418023-bundleidentifier) do seu app, [ID da chave](https://developer.apple.com/help/account/manage-keys/get-a-key-identifier/), e [ID da equipe](https://developer.apple.com/help/account/manage-your-team/locate-your-team-id). Você também precisará especificar se deseja enviar notificações para o ambiente de desenvolvimento ou produção do seu app, que é definido pelo seu perfil de provisionamento. 
8. Quando terminar, selecione **Salvar**.

