---
nav_title: Apptimize le partenariat
page_order: 0
page_type: Mettre à jour
description: "Cet article archivé couvre le partenariat entre Apptimize et Braze. Braze a déprécié le support du partenariat Apptimize en septembre 2019."
---

# Apptimize

{% alert update %}
Braze a déprécié le support du partenariat Apptimize en septembre 2019.

<br>

Si vous utilisez actuellement Apptimize avec Braze, vous ne rencontrerez pas de perturbation du service. Vous pouvez toujours définir des attributs personnalisés Apptimize pour les profils d'utilisateurs de Braze. Cependant, aucun soutien officiel d'escalade avec le partenaire ne sera fourni.

<br>

Veuillez contacter votre représentant de Braze ou Apptimize si vous avez d'autres questions.
{% endalert %}


[Apptimize](https://apptimize.com/) est une plateforme mobile de test et de croissance de l'application qui permet aux clients d'itérer rapidement tout au long du processus de développement de l'application.

Apptimize peut être utilisé en conjonction avec Braze pour compléter vos stratégies de croissance marketing / CRM avec les tests de l'interface utilisateur du produit en synchronisant les expériences et les données sur les deux plateformes.

## Cas d'utilisation

Avec Braze et Apptimize ensemble, vous pouvez tirer parti des deux plateformes en conjonction pour créer de puissantes expériences de bout en bout :

* Synchronisez les expériences marketing dans l'application et CRM pour une promotion personnalisée.
* Testez une nouvelle expérience d'intégration dans Apptimize, et utilisez Braze pour nourrir les utilisateurs tout au long du nouveau flux.
* En même temps que la messagerie utilisateur appropriée, les configurations des produits sont actuellement mises à l'épreuve.
* Adapter les expériences dans l'application et leurs messages appropriés pour différents segments des utilisateurs finaux.

## Comment ça marche

Braze et Apptimize peuvent être intégrés ensemble pour passer des données du SDK au SDK. Vous pouvez synchroniser les groupes de test Apptimize A/B à nouveau au Brésil, vous permettant de redimensionner les utilisateurs dans un test d'Apptimize particulier dans Braze via push, email, ou Messagerie In-App.

Nous avons un exemple de code d'intégration qui montre comment les SDK Braze et Apptimize peuvent transmettre des données à la puissance personnalisée de ciblage et de segmentation dans Braze basé sur Apptimize données d'expérience.

Cet exemple d’intégration définira des attributs personnalisés sur les profils de vos utilisateurs Braze pour les données d’Apptimize suivantes :

* La liste complète des expériences actives auxquelles l'utilisateur est actuellement inscrit.
* La liste complète des expériences auxquelles l'utilisateur a été inscrit, y compris les expériences terminées.
* Les variantes que l'utilisateur a vues comme faisant partie d'une participation d'expérience.

> Les Drapeaux de Fonctionnalités sont considérés comme des expériences où la seule variante est de savoir si le Drapeau de la Fonctionnalité est activé. Si l'indicateur de fonctionnalité est désactivé, aucune donnée ne sera signalée.

De plus, cette intégration enregistrera un événement personnalisé Braze pour le premier événement de participation d'une expérience. Cela peut être fait de deux manières:

* Un événement personnalisé est généré hors de la boîte avec des données de propriété indiquant le nom de l'expérience, l'ID de l'expérience, le nom de la variante et l'ID de la variante. Vous pouvez ensuite rediriger les utilisateurs en temps réel en utilisant les campagnes de livraison basées sur l'action de Braze et Canvases. Utilisez ces propriétés pour identifier l'expérimentation Apptimize que vous voulez déclencher.
* Un tableau d'attributs est généré hors de la boîte avec des entrées pour chaque participation qui s'est produite. Chaque participation est formatée comme `experiment_id_EXPERIMENT_ID:variant_id_VARIANT_ID:experiment_name_EXPERIMENT_NAME:variant_name_VARIANT_NAME`

Vous pouvez ensuite utiliser les campagnes de livraison basées sur l'action de Braze ou Canvases pour envoyer messages de suivi aux utilisateurs en temps réel lorsque ces événements sont déclenchés.

## Intégration

### iOS
In order to integrate with your app, import the following `Appboy-Apptimize.m` and `Apptimize-Appboy.h` files into your Xcode project, import the `Appboy-Apptimize.h` header into your AppDelegate implementation and add the following to `didFinishLaunchingWithOptions` after initializing both Appboy and Apptimize:

```objc
[ApptimizeAppboy setupExperimentTracking];
```

#### Appboy-Apptimize.h:

```objc
// Apptimize-Appboy.h

#ifndef Apptimize_Appboy_h
#define Apptimize_Appboy_h

@interface ApptimizeAppboyboy : NSObject
+ (void)setupExperimentTracking;
@end

#endif /* Apptimize_Appboy_h */
```

#### Appboy-Apptimize.m:

```objc
//  Apptimize-Appboy.m

#import <Foundation/Foundation.h>

#import "Apptimize-Appboy.h"

#import <Apptimize/Apptimize.h>
#import <Apptimize/Apptimize+Variables.h>

#import "Appboy.h"
#import "ABKUser.h"

// Key to store previous enrollment dictionary to check against to see if enrollment has changed
NSString *const ApptimizeAppboyTestEnrollmentStorageKey = @"ApptimizeAppboyTestEnrollmentStorageKey";

@implementation ApptimizeAppboy

+ (void)setupExperimentTracking
{
    // Track for enrollment changes
    [[NSNotificationCenter defaultCenter] addObserver:self
                                                selector:@selector(apptimizeTestsProcessed:)
                                                    name:ApptimizeTestsProcessedNotification
                                                object:nil];
    // Track for participation events
    [[NSNotificationCenter defaultCenter] addObserver:self
                                                selector:@selector(experimentDidGetViewed:)
                                                    name:ApptimizeTestRunNotification
                                                object:nil];
}

+ (void)apptimizeTestsProcessed:(NSNotification*)notification
{
    NSLog(@"Appboy-Apptimize integration processing new Apptimize tests");
    [self updateForNewTests];
}

+ (void)updateForNewTests
{
    NSDictionary *savedEnrollmentDictionary = [[NSUserDefaults standardUserDefaults] objectForKey:ApptimizeAppboyTestEnrollmentStorageKey];
    NSDictionary *currentEnrollmentDictionary = [self getEnrollmentDictionaryFromTestInfo];

    BOOL enrollmentChanged = NO;

    for (id key in currentEnrollmentDictionary) {
        if (![savedEnrollmentDictionary[key] isEqualToString:currentEnrollmentDictionary[key]]) {
            enrollmentChanged = YES;
            NSString *testAttributeKey = [@"apptimize_test_" stringByAppendingString:key];
            [[Appboy sharedInstance].user addToCustomAttributeArrayWithKey:testAttributeKeyvalue :currentEnrollmentDictionary[key]];
        }
    }

    if (currentEnrollmentDictionary.count != savedEnrollmentDictionary.count) {
        enrollmentChanged = YES;
    }

    if (enrollmentChanged) {
        [[Appboy sharedInstance].user setCustomAttributeArrayWithKey:@"active_apptimize_tests" array:currentEnrollmentDictionary.allKeys];

        for (id key in currentEnrollmentDictionary.allKeys) {
            [[Appboy sharedInstance].user addToCustomAttributeArrayWithKey:@"all_apptimize_tests" value:key];
        }

        [[NSUserDefaults standardUserDefaults] setObject:currentEnrollmentDictionary forKey:ApptimizeAppboyTestEnrollmentStorageKey];
        [[NSUserDefaults standardUserDefaults] synchronize];
    }
}

// Dictionary with variant IDs keyed by test ID, both as NSStrings
+ (NSMutableDictionary *)getEnrollmentDictionaryFromTestInfo
{
    NSMutableDictionary *enrollmentDictionary = [NSMutableDictionary dictionary];

    for(id key in [Apptimize testInfo]) {
        NSLog(@"key=%@ value=%@", key, [[Apptimize testInfo] objectForKey:key]);
        NSDictionary<ApptimizeTestInfo> *testInfo = [[Apptimize testInfo] objectForKey:key];
        enrollmentDictionary[[testInfo.testID stringValue]] = [testInfo.enrolledVariantID stringValue];
    }

    return enrollmentDictionary;
}

+ (void)experimentDidGetViewed:(NSNotification*)notification
{
    if (![notification.userInfo[ApptimizeTestFirstRunUserInfoKey] boolValue]) {
        return;
    }

    // Apptimize doesn't notify with IDs, so we iterate over all experiments to find the matching one.
    NSString *name = notification.userInfo[ApptimizeTestNameUserInfoKey];
    NSString *variant = notification. serInfo[ApptimizeVariantNameUserInfoKey];

    [[Apptimize testInfo] enumerateKeysAndObjectsUsingBlock:^(id key, id<ApptimizeTestInfo> expérimentation, BOOL *stop) {
        match BOOL = [expérimentation. estName isEqualToString:name] && [expérimentation. nrolledVariantName isEqualToString:variant];
        if (! atch) {
            retourner;
        }

        // Si vous voulez enregistrer un événement personnalisé pour chaque participation
        [[Appboy sharedInstance] logCustomEvent:@"apptimize_experiment_viewed"
                                    withProperties: @{@"apptimize_experiment_name" : [experiment testName],
                                                        @"apptimize_variant_name" : [experiment enrolledVariantName],
                                                        @"apptimize_experiment_id" : [experiment testID],
                                                        @"apptimize_variant_id" : [experiment enrolledVariantID]}] ;

        // Si vous voulez un jeu d'attributs personnalisés pour chaque participation
        [[Appboy sharedInstance]. ser addToCustomAttributeArrayWithKey:@"apptimize_experiments"
                                                                    valeur:[NSString stringWithFormat:@"experiment_id_%@:variant_id_%@:experiment_name_%@:variant_name_%@",
                                                                            [testID d'expérience], [experiment enrolledVariantID], [experiment testName], [experiment enrolledVariantName] ]];
        *stop = OUI;
    }];
}

@end
```

### Android

import the `apptimizeappboy.java` class into your app and in your main `activity` implementation, create a private member `appboyApptimizeIntegration`:

```java
ApptimizeAppboy privé appboyApptimizeIntegration;
```

Puis dans votre méthode onCred, après l'initialisation de Braze et Apptimize:

```java
appboyApptimizeIntegration = new ApptimizeAppboy();
appboyApptimizeIntegration.configureExperimentTracking(ceci);
```

#### ApptimizeAppboy.java :

```java
package com.apptimize.appboykit;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.Map;
import java.util.HashMap;
import android.util.Log;

import android.content.Context;

import com.apptimize.Apptimize;
import com.apptimize.ApptimizeTestInfo;
import com.apptimize.Apptimize.OnExperimentsProcessedListener;
import com.apptimize.Apptimize.OnExperimentRunListener;

import com.appboy.Appboy;
import com.appboy.AppboyUser;
import com.appboy.models.outgoing.AppboyProperties;

public class ApptimizeAppboy
        implements Apptimize.OnExperimentRunListener,
                    Apptimize.OnExperimentsProcessedListener {

    public void configureExperimentTracking(Context context) {
        appboyInstance = Braze.getInstance(context);
        enrollmentStorage = new File(context.getDir("apptimize-appboy", Context.MODE_PRIVATE), ApptimizeAppboyTestEnrollmentStorage);

        Apptimize.setOnExperimentRunListener(this);
        Apptimize.addOnExperimentsProcessedListener(this);
    }

    @Override
    public void onExperimentRun(String experimentName, String variantName, boolean firstRun) {
        if (!firstRun) {
            return;
        }
        Map<String,ApptimizeTestInfo> testInfoMap = Apptimize.getTestInfo();

        if (testInfoMap == null) {
            return;
        }

        String experimentId = "";
        String variantId = "";

        Log.d("Apptimize-Appboy", "In onExperimentRun");

        for (ApptimizeTestInfo testInfo : testInfoMap.values()) {
            if (testInfo.getTestName().equals(experimentName) &&
                testInfo.getEnrolledVariantName().equals(variantName)) {
                experimentId = String.valueOf(testInfo.getTestId());
                variantId = String.valueOf(testInfo.getEnrolledVariantId());
            }
        }
        Log.d("Apptimize-Appboy", "Logging participation for " + experimentName + ":" + experimentId + " and variant " + variantName + ":" + variantId);

        // If you want to log a custom event for each participation
        logParticipationEventAsEvent(experimentName, variantName, experimentId, variantId);

        // If you want a custom attribute array set for each participation
        logParticipationEventAsAttributes(experimentName, variantName, experimentId, variantId);
    }

    private void logParticipationEventAsEvent(String experimentName, String variantName, String experimentId, String variantId) {
        AppboyProperties eventProperties = new AppboyProperties();

        eventProperties.addProperty("apptimize_experiment_name", experimentName);
        eventProperties.addProperty("apptimize_variant_name", variantName);
        eventProperties.addProperty("apptimize_experiment_id", experimentId);
        eventProperties.addProperty("apptimize_variant_id", variantId);

        appboyInstance.logCustomEvent("apptimize_experiment_viewed", eventProperties);
    }

    private void logParticipationEventAsAttributes(String experimentName, String variantName, String experimentId, String variantId) {
        appboyInstance.getCurrentUser().addToCustomAttributeArray("apptimize_experiments",
                "experiment_id_" + experimentId + ":variant_id_" + variantId + ":experiment_name_" + experimentName + ":variant_name_" + variantName);
    }

    @Override
    public void onExperimentsProcessed() {
        Map<String,String> currentEnrollmentDictionary = getEnrollmentDictionary();
        Map<String,String> savedEnrollmentDictionary = getPreviousEnrollmentDictionary();
        AppboyUser appboyUser = appboyInstance.getCurrentUser();

        boolean enrollmentChanged = false;

        Log.d("Apptimize-Appboy", "Processing experiments");

        for (String key : currentEnrollmentDictionary.keySet()) {
            if (savedEnrollmentDictionary == null ||
                !currentEnrollmentDictionary.get(key).equals(savedEnrollmentDictionary.get(key))) {
                Log.d("Apptimize-Appboy", "Found change in enrollment" + currentEnrollmentDictionary.get(key));
                enrollmentChanged = true;
                String testAttributeKey = "apptimize_test_" + key;
                appboyUser.addToCustomAttributeArray(testAttributeKey, currentEnrollmentDictionary.get(key));
            }
        }

        if (currentEnrollmentDictionary.size() == 0 && savedEnrollmentDictionary.size() != 0) {
            enrollmentChanged = true;
        }

        if (enrollmentChanged) {
            Log.d("Apptimize-Appboy", "Enrollment changed");
            appboyUser.setCustomAttributeArray("active_apptimize_tests", currentEnrollmentDictionary.keySet().toArray(new String[0]));

            for (String key : currentEnrollmentDictionary.keySet()) {
                appboyUser.addToCustomAttributeArray("all_apptimize_tests", key);
            }

            storePreviousEnrollmentDictionary(currentEnrollmentDictionary);
        }
    }

    private Map<String,String> getEnrollmentDictionary()
    {
        Map<String,String> enrollment = new HashMap<String,String>();
        Map<String,ApptimizeTestInfo> testInfoMap = Apptimize.getTestInfo();
        for (ApptimizeTestInfo testInfo : testInfoMap.values()) {
            Log.d("Apptimize-Appboy", "TestID: " + String.valueOf(testInfo.getTestId()) + " VariantID: " + String.valueOf(testInfo.getEnrolledVariantId()));
            enrollment.put(String.valueOf(testInfo.getTestId()), String.valueOf(testInfo.getEnrolledVariantId()));
        }
        return enrollment;
    }

    private Map<String,String> getPreviousEnrollmentDictionary()
    {
        ObjectInputStream enrollmentStream;
        try {
            enrollmentStream = new ObjectInputStream(new FileInputStream(enrollmentStorage));
        } catch(Exception e) {
            Log.d("Apptimize-Appboy", "Unable to open file");
            return null;
        }

        Map<String, String> previousEnrollment;
        try {
                previousEnrollment = (Map<String,String>)enrollmentStream.readObject();
        } catch (Exception e) {
            Log.d("Apptimize-Appboy", "Unable to get previous enrollment");
            return null;
        }

        return previousEnrollment;
    }

    private void storePreviousEnrollmentDictionary(Map<String,String> enrollmentDictionary)
    {
        try {
            ObjectOutputStream enrollmentStream = new ObjectOutputStream(new FileOutputStream(enrollmentStorage));
            enrollmentStream.writeObject(enrollmentDictionary);
            enrollmentStream.flush();
            enrollmentStream.close();
        } catch (Exception e) {
            Log.d("Apptimize-Appboy", "Unable to save enrollment information");
        }

    }

    private Appboy appboyInstance;
    private File enrollmentStorage;

    private static String ApptimizeAppboyStorageDirectory;
    private static String ApptimizeAppboyTestEnrollmentStorage = "ApptimizeAppboyTestEnrollmentStorage";
}
```
