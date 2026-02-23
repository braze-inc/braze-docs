Braze를 사용하여 iOS 푸시 알림을 보내려면 먼저 [Apple의 개발자 설명서에](https://developer.apple.com/documentation/usernotifications/establishing-a-token-based-connection-to-apns) 설명된 대로 `.p8` 푸시 알림 파일을 업로드해야 합니다:

1. Apple 개발자 계정에서 다음 위치로 이동합니다. [**인증서, 식별자 & 프로필**](https://developer.apple.com/account/ios/certificate).
2. **키**에서 **모두**를 선택하고 오른쪽 상단에 있는 추가 버튼(+)을 클릭합니다.
3. **키 설명**에 서명 키의 고유한 이름을 입력합니다.
4. **주요 서비스에서** **Apple 푸시 알림 서비스(APN)** 확인란을 선택한 다음 **계속을** 클릭합니다. **확인**을 클릭합니다.
5. 키 ID를 기록해 두세요. **다운로드**를 클릭하여 키를 생성하고 다운로드합니다. 다운로드한 파일은 두 번 이상 다운로드할 수 없으므로 안전한 곳에 저장하세요.
6. Braze에서 **설정** > **앱 설정으로** 이동하여 **Apple 푸시 인증서** 아래에 `.p8` 파일을 업로드합니다. 개발 또는 프로덕션 푸시 인증서를 업로드할 수 있습니다. 앱이 App Store에 출시된 후 푸시 알림을 테스트하려면 앱의 개발 버전을 위한 별도의 워크스페이스를 설정하는 것이 좋습니다.
7. 메시지가 표시되면 앱의 [번들 ID](https://developer.apple.com/documentation/foundation/nsbundle/1418023-bundleidentifier), [키 ID](https://developer.apple.com/help/account/manage-keys/get-a-key-identifier/) 및 [팀 ID를](https://developer.apple.com/help/account/manage-your-team/locate-your-team-id) 입력합니다. 또한 앱의 개발자 환경으로 알림을 보낼지 프로비저닝 프로필로 정의된 프로덕션 환경으로 보낼지 지정해야 합니다. 
8. When you're finished, select **Save**.

