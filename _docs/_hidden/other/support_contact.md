---
permalink: /support_contact/
nav_title: Help | Braze
hide_nav: true
layout: basic
hide_toc: true
---
<link rel="stylesheet" href="https://cdn.jsdelivr.net/docsearch.js/2/docsearch.min.css" />

<style type="text/css">

#main-container {
  margin-top: 20px;
  margin-bottom: 50px;
  min-height: 800px;
}
#main-container label {
  font-weight: bold;
  font-size: 18px;
}

.container {
  margin-top: 40px;
}

.popover{
  max-width: 65%;
  min-width: 350px;
  top: -15px !important;
}
@media (max-width:600px)  {
  .popover{
    max-width: 95%;
  }
}
.container-fluid {
  max-width: 1280px;
}

.header {
  margin-top: 20px;
  margin-bottom: 20px;
}

.header .navbar-brand img {
    max-width: none;
    width: 112px;
    height: 51px;
}

#ticket_resources {
  border-left: solid 1px #c9c9c9;
  padding-left: 40px;
  min-height: 340px;
}
@media (max-width:600px)  {
  #ticket_resources {
    padding-left: 15px;
    border: none;
  }
}

.algolia-autocomplete-listbox-2 {
    display: inline !important;
}

#algolia-autocomplete-listbox-2 {
  position: relative !important;
}

.algolia-autocomplete {
  line-height: normal;
  display: inline !important;
}
#search-input {
    padding: 0 0 20px;
    position: relative;
}

#search-input input[type="text"] {
    padding: .5em 0 .5em 0;
    outline: 0;
    border: 0;
    border-bottom: solid 2px #c9c9c9;
    width: 100%;
    font-size: 15px;
    display: inline-block;
    background-image:url(/docs/assets/img/search_black_shark.svg);
    background-position: right 10px top 9px;
    background-size: 14px 14px;
    background-repeat: no-repeat;
}

#search-input .fa-search {
  line-height: normal;
  position: relative;
  top: 15px;
  left: 5px;
}

.aa-suggestion {
  margin-top: 5px;
  line-height: 25px;
}

#ticket_search div.aa-suggestion {
  color: #6d6d70;
  cursor: pointer;
  display: inline;
  border-bottom-width: 0px;
}

#ticket_search aa-suggestions:hover div {
  text-decoration: none;
  color: #6d6d70;
  border-bottom-width: 2px;
  border-color: #3accdd;
}


#ticket_search aa-suggestion--highlight{

}

#ticket_search .algolia-docsearch-footer {
  padding-top: 5px;
}

.gradient-line {
    background: linear-gradient(30deg,#3accdd,#f7918e 64%,#ff9349 90%);
    height: 2px;
    width: 108px;
}

a {
  color: #3accdd;
}
a:hover {
  color: #333;
}
#ticket_mainform {
  margin-top: 20px;
}
#ticket_leftmain {
  padding-right: 40px;

}
#ticket_reference {
  line-height: normal;
}

#ticket_footer {
  margin-left: auto;
  margin-right: auto;
  border-top: 1px solid #dfdfe3;
  text-align: center;
  font-size: 12px;
  padding-top: 10px;
  color: #6e6e70;
}

#ticket_footer a {
  text-decoration: none;
  color: #6e6e70;
}
#ticket_footer li {
  display: inline;
  margin: 8px;

}
.h1, h1  {
  font-size: 44px;
}

.h2, h2 {
  font-size: 20px;
}


#ticket_submit_option {
  margin-top: 20px;
}

#ticket_form button[type=submit] {
  display: inline-block;
  vertical-align: middle;
  font: inherit;
  text-align: center;
  margin: 0;
  cursor: pointer;
  font-size: 14px;
  font-size: 1rem;
  line-height: 1.4;
  font-family: Sailec W00 Bold, Arial, sans-serif;
  text-transform: uppercase;
  padding: 1.14286rem 2.85714rem;
  border-radius: 0;
  letter-spacing: .10714rem;
  white-space: normal;
  border: 2px solid #212123;
  color: #212123;
  background-color: transparent;
  position: relative;
  z-index: 1;
  overflow: hidden;
  transition: color .3s cubic-bezier(.5, 0, .1, 1), border-color .3s cubic-bezier(.5, 0, .1, 1);
  will-change: color, border-color
}

@media (min-width:36em) {
  #ticket_form button[type=submit] {
    padding: 1.64286rem 3.92857rem
  }
}

#ticket_form button[type=submit]:before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
  height: 100%;
  background-color: #212123;
  transform-origin: top right;
  width: 100%;
  transform: translate3d(-101%, 0, 0);
  transition: transform .3s cubic-bezier(.5, 0, .1, 1);
  will-change: transform
}

#ticket_form button[type=submit]:focus, #ticket_form button[type=submit]:hover {
  color: #fff
}

#ticket_form button[type=submit]:focus:before, #ticket_form button[type=submit]:hover:before {
  transform: translateZ(0)
}

#ticket_form button[type=submit] {
  color: #fff
}

#ticket_form button[type=submit]:before {
  background-color: #fff
}

#ticket_form button[type=submit]:after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  z-index: -2;
  height: 100%;
  width: 100%;
  background-color: #212123;
}

#ticket_form button[type=submit]:focus, #ticket_form button[type=submit]:hover {
  color: #212123
}

#firefox_warning {
  width: 100%;
  text-align: center;
  background-color: #f4f4f7;
  padding: 10px;
}
#firefox_warning a, #ticket_thankyou_msg a{
  color: #3accdd;
  text-decoration: none;
}
#firefox_warning a:hover, #ticket_thankyou_msg a:hover {
  color: #3accdd;
  text-decoration: none;
}
#support-search-panel .aa-Panel {
  top: 0px !important;
  position: static;
  box-shadow: none;
}
#support-search-panel .aa-Item {
  top: 0px !important;
  position: static;
  box-shadow: none;
  min-height: 1.8em;
  line-height: 1.3em;
}
#support-search-panel .aa-PanelLayout {
  padding-top: 0px;
}
#support-search-div {
  padding-bottom: 15px;
}
#support-search-div .aa-Form {
  box-shadow: none;
  border-color: transparent;
  border-radius: 0px;
  border-bottom: solid 2px #c9c9c9;
}
#support-search-div .aa-Form button {
  padding-top: 10px;
}
</style>


<script type="text/javascript">
function support_doc_submit(){
  window.location = base_url + '/search/?query=' + encodeURIComponent($('#support-search-form .aa-Form .aa-Input').val());
  return false;
}

String.prototype.mapReplace = function(map) {
  var mstr = this;
  for (var wd in map) {
    if (map.hasOwnProperty(wd)) {
        var rep = new RegExp('\\b' + wd + '\\b','gi');
        mstr = mstr.replace(rep,map[wd]);
    }
  }
  return mstr;
};

var wordmap = {
  'REST' : 'REST',
  'API' : 'API',
  'APIs' : 'APIs',
  'iOS' : 'iOS',
  'ID' : 'ID',
  'IDs' : 'IDs',
  'FAQ' : 'FAQ',
  'FAQS' : 'FAQs',
  'Android' : 'Android'
}
var ticket_lookuptable = {
  'SelectText' : 'What can we help you with?',
  'Label': '* What can we help you with?',
  'SelectDefault': 'Select a topic...',
  'LinksTitle': ['Marketer documentation','Developer documentation','Marketer troubleshooting guide','FAQs'],
  'Links': ['{{site.baseurl}}/user_guide/introduction/','{{site.baseurl}}/developer_guide/platform_wide/platform_features/','{{site.baseurl}}/help/home/','{{site.baseurl}}/help/faqs/'],
  'SelectOption': {
    'Technical Question': {
      'Label': '* Category',
      'SelectDefault': 'Select a category...',
      'LinksTitle': ['Platform wide integration steps'],
      'Links' : ['{{site.baseurl}}/developer_guide/platform_wide/platform_features/','{{site.baseurl}}/help/faqs/'],
      'SelectOption' : {
        'SDK Integration' : {
          'Label': '*  My question is about...',
          'SelectDefault': 'Select a type...',
          'LinksTitle': ['iOS Initial SDK Setup','Android Initial SDK Setup','Web Initial SDK Setup'],
          'Links': ['{{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/','{{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/'],
          'SelectOption' : {
            'Push' : {
              'SelectDefault': 'Select a platform...',
              'LinksTitle': ['iOS: push integration','Android: push integration'],
              'Links' : ['{{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/'],
              'Label': '* Platform',
              'SelectOption' : {
                'Android' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Android: push integration','Android: push troubleshooting','Android: silent push notifications'],
                  'Links' : ['{{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/troubleshooting/','{{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/silent_push_notifications/']
                },
                'iOS' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['iOS: push integration','iOS: push troubleshooting','iOS 10: rich notifications','iOS: silent push notifications'],
                  'Links': ['{{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/troubleshooting/','{{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#ios-10-rich-notifications','{{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/']
                },
                'Other' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Xamarin push integration'],
                  'Links' : ['{{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/push_notifications/']
                }
              }
            },
            'User data and external IDs': {
              'LinksTitle': ['iOS: data tracking','Android: data tracking','Web: data tracking'],
              'Links':  ['{{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/','{{site.baseurl}}//developer_guide/platform_integration_guides/android/analytics/tracking_sessions/','{{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/'],
              'Label': '* Type of Data',
              'SelectDefault': 'Select data type...',
              'SelectOption' : {
                'Setting external IDs' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['iOS: setting user IDs','Android: setting user IDs','User ID FAQs'],
                  'Links' : ['{{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#setting-user-ids','{{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#setting-user-ids','{{site.baseurl}}/developer_guide/rest_api/basics/#external-user-id-explanation']
                },
                'Custom events and event properties' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['iOS: tracking custom events','Android: tracking custom events'],
                  'Links' : ['{{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/#tracking-custom-events','{{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events']
                },
                'Custom attributes' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['iOS: tracking custom attributes','Android: tracking custom attributes'],
                  'Links' : ['{{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/#setting-custom-attributes','{{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-custom-attributes']
                }
              }
            },
            'Web SDK' :{
              'ShowSubmit': true,
              'LinksTitle': ['Web SDK integration','Web: push integration','Web: soft push prompts','Web: in-browser messaging','Web: data tracking'],
              'Links': ['{{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/','{{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#soft-push-prompts','{{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#in-app-messaging','{{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/'],
            },
            'Other' :{
              'ShowSubmit': true,
              'LinksTitle': ['iOS: push integration','Android: push integration'],
              'Links': ['{{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/']
            }
          }
        },
        'REST APIs' : {
          'Label': '*  My question is about...',
          'SelectDefault': 'Select a type...',
          'LinksTitle': ['REST APIs','REST APIs: updating user data','REST APIs: messaging','REST APIs: exporting Braze data'],
          'Links': ['{{site.baseurl}}/developer_guide/rest_api/basics/','{{site.baseurl}}/developer_guide/rest_api/user_data/','{{site.baseurl}}/api/endpoints/messaging/','{{site.baseurl}}/developer_guide/rest_api/export/'],
          'SelectOption' : {
            'Importing data' : {
              'ShowSubmit': true,
              'LinksTitle': ['REST APIs: updating user data','REST APIs: updating user attributes','REST APIs: updating user events','REST APIs: updating user purchases','REST APIs: deleting users'],
              'Links' : ['{{site.baseurl}}/developer_guide/rest_api/user_data/','{{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification',	'{{site.baseurl}}/developer_guide/rest_api/user_data/#event-object-specification',	'{{site.baseurl}}/developer_guide/rest_api/user_data/#purchase-object-specification','{{site.baseurl}}/developer_guide/rest_api/user_data/#user-delete-endpoint']
            },
            'Exporting data' : {
              'ShowSubmit': true,
              'LinksTitle': ['REST APIs: exporting Braze data','REST APIs: exporting your user data','REST APIs: exporting campaign data'],
              'Links' : ['{{site.baseurl}}/developer_guide/rest_api/export/','{{site.baseurl}}/developer_guide/rest_api/export/#user-export','{{site.baseurl}}/developer_guide/rest_api/export/#campaign-export']
            },
            'API campaigns' : {
              'ShowSubmit': true,
              'LinksTitle': ['Sending messages immediately via REST API','Sending messages via API-triggered delivery','Tracking API campaigns via Braze\'s dashboard'],
              'Links' : ['{{site.baseurl}}/developer_guide/rest_api/messaging/#sending-messages-immediately-via-api-only','{{site.baseurl}}/developer_guide/rest_api/messaging/#sending-messages-via-api-triggered-delivery','{{site.baseurl}}/developer_guide/rest_api/api_campaigns/']
            },
            'Rate limits' : {
              'ShowSubmit': true,
              'LinksTitle': ['REST API rate limits'],
               'Links' : ['{{site.baseurl}}/developer_guide/rest_api/basics/#api-limits']
             },
             'Other' : {
               'ShowSubmit': true,
               'LinksTitle': ['REST API parameter definitions','What is a REST API?'],
               'Links' : ['{{site.baseurl}}/developer_guide/rest_api/basics/#api-definitions','{{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api']
             }
          }
        },
        'Partner Integrations' : {
          'Label': '*  My question is about...',
          'SelectDefault': 'Select a type...',
          'LinksTitle': ['Braze partner integrations instructions'],
          'Links': ['{{site.baseurl}}/partners/home/'],
          'SelectOption' : {
            'mParticle' : {
              'ShowSubmit': true,
              'LinksTitle': ['mParticle integration instructions'],
              'Links': ['{{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mparticle/']
            },
            'Segment' : {
              'ShowSubmit': true,
              'LinksTitle': ['Segment integration instructions'],
              'Links' : ['{{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/']
            },
            'Install attribution' : {
              'ShowSubmit': true,
              'LinksTitle': ['Attribution partner integrations','Attribution partner integration instructions'],
              'Links' : ['{{site.baseurl}}/partners/advertising_technologies/attribution/adjust/','{{site.baseurl}}/partners/home/']
            },
            'Other' : {
              'ShowSubmit': true,
              'LinksTitle': ['Braze partner integrations instructions'],
              'Links' : ['{{site.baseurl}}/partners/home/']
            }
          }
        },
        'Email' : {
          'SelectDefault': 'Select a type...',
          'Label': '*  My question is about...',
          'LinksTitle': ['Email best practices','LAB course: Achieving High Email Deliverability'],
          'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/','https://lab.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability'],
          'SelectOption': {
            'Setup (whitelabeled IPs, DNS records)' : {
              'ShowSubmit': true,
              'LinksTitle': ['LAB course: Achieving High Email Deliverability','IP warming'],
              'Links' : ['https://lab.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability','{{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming/#ip-warming']
            },
            'Deliverability' :{
              'ShowSubmit': true,
              'LinksTitle': ['IP warm','LAB course: Achieving High Email Deliverability'],
               'Links' : ['{{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming/#ip-warming','https://lab.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability']
            },
            'IP warmup' : {
              'ShowSubmit': true,
              'LinksTitle': ['IP warming'],
              'Links' : ['{{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming/#ip-warming']
            },
            'Managing unsubscribes and opt-ins' : {
              'ShowSubmit': true,
              'LinksTitle': ['Managing email subscription states','Email subscription state definitions','Changing email subscription states'],
              'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/','{{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states','{{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-subscriptions']
            },
            'Other' : {
              'ShowSubmit': true,
              'LinksTitle': ['Email best practices','LAB course: Achieving High Email Deliverability'],
              'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/','https://lab.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability']
            }
          }
        },
        'Webhooks' :{
          'ShowSubmit': true,
          'Label': '*  My question is about...',
          'SelectDefault': 'Select a type...',
          'LinksTitle': ['Creating webhooks'],
          'Links': ['{{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/']
        },
        'Other' :{
          'ShowSubmit': true,
          'Label': '*  My question is about...',
          'SelectDefault': 'Select a type...',
          'LinksTitle': ['Developer documentation','Troubleshooting guide','FAQs'],
          'Links': ['{{site.baseurl}}/developer_guide/platform_wide/platform_features/','{{site.baseurl}}/help/home/','{{site.baseurl}}/help/faqs/']
        }
      }
    },

    'Issue / Bug' : {
      'Label': '* Category',
      'SelectDefault': 'Select a category...',
      'LinksTitle': ['Braze SDK changelogs','Braze status page'],
      'Links': ['{{site.baseurl}}/help/release_notes/most_recent/','https://braze.statuspage.io/'],
      'SelectOption': {
        'SDK issue or error' :{
          'Label': '*  My question is about...',
          'SelectDefault': 'Select a type...',
          'LinksTitle': ['Sending test messages','LAB course: technical integration checklists','Android: test your integration'],
          'Links': ['{{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#test-your-basic-integration','https://lab.braze.com/technical-integration-checklists-and-toolkits','{{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#test-your-basic-integration'],
          'SelectOption': {
            'I\'m running into an issue during SDK integration.' :{
              'ShowSubmit': true,
              'LinksTitle': ['iOS: push troubleshooting','Android: push troubleshooting','Web: error logging'],
              'Links' : ['{{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/troubleshooting/','{{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#troubleshooting','{{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#error-logging']
            },
            'I\'m seeing a bug.' : {
              'ShowSubmit': true,
              'LinksTitle': ['Braze status page'],
              'Links': ['https://braze.statuspage.io/']
            },
            'Other' : {
              'ShowSubmit': true,
              'LinksTitle': ['Sending test messages','LAB course: technical integration checklists','Android: test your integration'],
              'Links': ['{{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/#sending-test-messages','https://lab.braze.com/technical-integration-checklists-and-toolkits','{{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#test-your-basic-integration']
            }
          }
        },
        'REST API issue or error' : {
          'Label': '*  My question is about...',
          'SelectDefault': 'Select a type...',
          'LinksTitle': ['REST APIs'],
          'Links': ['{{site.baseurl}}/developer_guide/rest_api/basics/'],
          'SelectOption': {
            'I\'m seeing an issue when using REST APIs.' : {
              'ShowSubmit': true,
              'LinksTitle': ['REST APIs','REST API limits'],
              'Links': ['{{site.baseurl}}/developer_guide/rest_api/basics/','{{site.baseurl}}/developer_guide/rest_api/basics/#api-limits']
            },
            'I see an error I don’t understand.' :{
              'ShowSubmit': true,
              'LinksTitle': ['REST API fatal errors','REST API user track endpoint responses'],
              'Links' : ['{{site.baseurl}}/developer_guide/rest_api/messaging/#fatal-errors','{{site.baseurl}}/developer_guide/rest_api/user_data/#user-track-responses']
            },
            'I\'m running into rate limits.' :  {
              'ShowSubmit': true,
              'LinksTitle':['REST API limits'],
              'Links' : ['{{site.baseurl}}/developer_guide/rest_api/basics/#api-limits']
            },
            'Other' : {
              'ShowSubmit': true,
              'LinksTitle':['REST APIs'],
              'Links' : ['{{site.baseurl}}/developer_guide/rest_api/basics/']
            }
          }
        },
        'Braze dashboard issue or error' : {
          'Label': '*  My question is about...',
          'SelectDefault': 'Select a type...',
          'LinksTitle': ['Troubleshoting guide'],
          'Links': ['{{site.baseurl}}/help/home/'],
          'SelectOption' : {
            'I\'m experiencing an issue when working within the dashboard.' : {
              'ShowSubmit': true,
              'LinksTitle': ['Troubleshooting guide','Braze status page'],
              'Links': ['{{site.baseurl}}/help/home/','https://braze.statuspage.io/']
            },
            'My campaign, Canvas or segment is displaying unexpected behavior.' :{
              'ShowSubmit': true,
              'LinksTitle': ['Sending test messages'],
              'Links' : ['{{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/#sending-test-messages']
            },
            'I\'m seeing unexpected reporting or data.' : {
              'ShowSubmit': true,
              'LinksTitle': ['Data and analytics reporting','Email reporting','Push reporting','In-app message reporting','Exporting data from Braze\'s dashboard'],
              'Links':['{{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting','{{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/','{{site.baseurl}}/help/best_practices/push/push_reporting/#push-reporting','{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/','{{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/']
            },
            'Other' : {
              'ShowSubmit': true,
              'LinksTitle': ['Troubleshooting guide','Braze status page'],
              'Links': ['{{site.baseurl}}/help/home/','https://braze.statuspage.io/']
            }
          }
        },
        'QA and troubleshooting' :  {
          'ShowSubmit': true,
          'Label': '*  My question is about...',
          'SelectDefault': 'Select a type...',
          'LinksTitle': ['Troubleshooting guide'],
          'Links': ['{{site.baseurl}}/help/home/']
        },
        'Other' : {
          'ShowSubmit': true,
          'Label': '*  My question is about...',
          'SelectDefault': 'Select a type...',
          'LinksTitle': ['Troubleshooting guide','Braze status page'],
          'Links': ['{{site.baseurl}}/help/home/','https://braze.statuspage.io/']
        }
      }
    },
    'Braze dashboard functionality question' : {
      'Label': '* Category',
      'SelectDefault': 'Select a category...',
      'LinksTitle': ['Getting started guide'],
      'Links': ['{{site.baseurl}}/user_guide/introduction/'],
      'SelectOption' : {
        'Creating Campaigns and Canvases' : {
          'ShowSubmit': true,
          'LinksTitle': ['Canvas','Importing users','LAB course: Canvas','Getting started guide','Scheduling and organizing campaigns'],
          'Links':  ['{{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/','{{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/','https://lab.braze.com/canvas-course/174101/scorm/20ff1lsqbf4t','{{site.baseurl}}/user_guide/introduction/','{{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/']
        },
        'Understanding reporting' : {
          'ShowSubmit': true,
          'LinksTitle': ['Email reporting','Push reporting','In-app message reporting','Data and analytics reporting','Exporting data from Braze\'s dashboard'],
          'Links' :  ['{{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/','{{site.baseurl}}/help/best_practices/push/push_reporting/#push-reporting','{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/','{{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting','{{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data']
        },
        'Personalization, Liquid and Connected Content' : {
          'ShowSubmit': true,
          'LinksTitle': ['Personalization and Liquid','Connected Content','LAB course: dynamic personalization and liquid'],
          'Links':  ['{{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/','{{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/','https://lab.braze.com/dynamic-personalization-with-liquid']
        },
        'Webhooks' :  {
          'ShowSubmit': true,
          'LinksTitle': ['Creating a webhook','Sending SMS via Twilio'],
          'Links': ['{{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/','{{site.baseurl}}/partners/additional_channels/sms/twilio/']
        },
        'Currents' :  {
          'ShowSubmit': true,
          'LinksTitle': ['Braze Currents'],
          'Links': ['{{site.baseurl}}/partners/braze_currents/how_it_works/']
        },
        'Location Targeting and Geofencing' :  {
          'ShowSubmit': true,
          'LinksTitle': ['Targeting users based on location','Geofencing'],
          'Links': ['{{site.baseurl}}/user_guide/engagement_tools/segments/location_targeting/#step-2-customize-your-location','{{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/']
        },
        'Other' :  {
          'ShowSubmit': true,
          'LinksTitle': ['Marketer documentation','Marketer troubleshooting guide','FAQs'],
          'Links': ['{{site.baseurl}}/user_guide/introduction/','{{site.baseurl}}/help/home/','{{site.baseurl}}/help/faqs/']
        }
      }
    },

    'Marketing strategy question' : {
      'Label': '* Category',
      'SelectDefault': 'Select a category...',
      'LinksTitle': ['Campaign ideas and strategies','Mobile marketing best practices'],
      'Links': ['{{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/active_user_campaigns/#active-user-campaigns','{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/'],
      'SelectOption' : {
        'Campaign and Canvas strategies' : {
          'ShowSubmit': true,
          'LinksTitle': ['Campaign ideas and strategies','LAB course: Canvas'],
          'Links': ['{{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/active_user_campaigns/#active-user-campaigns','https://lab.braze.com/canvas-course']
        },
        'Segmentation and targeting' : {
          'ShowSubmit': true,
          'LinksTitle': ['Creating a segment','Segment insights','LAB course: segmentation'],
          'Links': ['{{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment','{{site.baseurl}}/user_guide/engagement_tools/segments/segment_insights/#segment-insights','https://lab.braze.com/segmentation-course']
        },
        'Managing push opt-ins' : {
          'ShowSubmit': true,
          'LinksTitle': ['Creating custom opt-in prompts','Push subscription states'],
          'Links': ['{{site.baseurl}}/help/best_practices/push/creating_custom_opt-in_prompts/#creating-custom-opt-in-prompts','{{site.baseurl}}/help/best_practices/push/push_subscription_status/#subscribed-opted-in-and-unsubscribed']
        },
        'Setting up custom events, attributes and purchases' :{
          'ShowSubmit': true,
          'LinksTitle': ['Data automatically tracked by Braze SDK','Custom events','Custom event properties','Custom attributes'],
          'Links':  ['{{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#automatically-collected-data','{{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-events','{{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-event-properties','{{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attributes']
        },
        'Other' :{
          'ShowSubmit': true,
          'LinksTitle': ['Campaign ideas and strategies','Mobile marketing best practices'],
          'Links':  ['{{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/active_user_campaigns/#active-user-campaigns','{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/']
        }
      }
    },

    'Billing / Account Administration' : {
      'Label': '* Category',
      'SelectDefault': 'Select a category...',

      'Links': [],
      'ReferenceText': 'Your Account Manager is a great resource for billing and contract related questions. ',
      'SelectOption' : {
        'Understanding data points usage' : {
          'ShowSubmit': true,
          'ReferenceText': 'Your Account Manager is a great resource for billing and contract related questions. ',
          'Links': []
        },
        'Account/ contract questions' : {
          'ShowSubmit': true,
          'ReferenceText': 'Your Account Manager is a great resource for billing and contract related questions. ',
          'Links': []
        },
        'Other' :{
          'ShowSubmit': true,
          'ReferenceText': 'Your Account Manager is a great resource for billing and contract related questions. ',
          'Links': []
        }
      }
    },
    'Other' :{
      'ShowSubmit': true,
      'Label': '* Category',
      'LinksTitle': ['Marketer documentation','Developer documentation','Marketer troubleshooting guide','FAQs'],
      'Links': ['{{site.baseurl}}/user_guide/introduction/','{{site.baseurl}}/developer_guide/platform_wide/platform_features/','{{site.baseurl}}/help/home/','{{site.baseurl}}/help/faqs/']
    }
  }
}
var ticket_options = ticket_lookuptable['SelectOption'];
$( document ).ready(function() {

  $.urlParam = function(name){
    var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
    if (results==null){
      return null;
    }
    else{
      return decodeURIComponent(results[1]) || 0;
    }
  }

  var autofilllist = {
    'name': '#ticket_name',
    'email': '#ticket_email'
  };
  var hiddenlist = {
    'appgroup': '00N0V000009G0NE',
    'appgroupid': '00N0V000009G0N9'
  };

  $.each(autofilllist, function(k,v){
    if ($.urlParam(k) ){
      $(v).val($.urlParam(k));
    };
  });

  var droplist = ['ticket_topic','ticket_category','ticket_subcategory','ticket_type'];
  var result_div = 'ticket_result';

  function reset_page(ind = 1){
    for(var i = ind; i < droplist.length;i++){
        $('#' + droplist[i]).empty();
    };
    $('#' + result_div).html('');
    /* if (!$("#submit_ticket").prop("checked")) {
      $("#submit_ticket").prop("checked", false);
      $("#submit_ticket").trigger("change");
    }*/
  }
  function hide_page(ind){
    for(var i = 0; i < droplist.length;i++){
        if (i < ind){
          $('#' + droplist[i]).attr('required',true);
          $('#' + droplist[i] + '_div').show();
        }
        else {
          $('#' + droplist[i]).attr('required',false);
          $('#' + droplist[i] + '_div').hide();
        }
    };
  }
  function removeleadingslash(str){
    var rstr = str;
    if (rstr.slice(-1) === "/") {
      rstr = rstr.slice(0, -1);
    }
    return rstr;
  }

  function showlinks(curquestion){
    if (curquestion) {
      var linklist = curquestion['Links'];
      var linkstitle = curquestion['LinksTitle'];
      var resdiv = $('#ticket_reference');
      var resmsg = $('#ticket_message');

      var resstr = '';
      if ('ReferenceText' in curquestion){
        resstr += curquestion['ReferenceText'] + '<br />'
      }
      if (linklist.length && linklist.length > 0){
        resmsg.html('Have you tried...')
        for (var i = 0 ; i < linklist.length; i++ ) {
          var title = '';
          if ((typeof linkstitle !== 'undefined') && (i in linkstitle) && linkstitle[i]) {
            title = linkstitle[i];
          }
          else {
            var linkparts =  linklist[i].split('#');
            var linkurl = removeleadingslash(linkparts[0]);
            var urlpart = linkurl.split('/')


            if (urlpart.length > 1) {
              title += ' ' + urlpart[urlpart.length-1].replace(/\_/g,' ').replace(/\-/g,' ');;
            }
            if (linkparts.length > 1) {
              var hashpart = linkparts[linkparts.length-1].replace(/\b\w/g, function(l){ return l.toUpperCase() });
              title += ': ' + hashpart.replace(/\_/g,' ').replace(/\-/g,' ');
            }
            title = title.mapReplace(wordmap)
          }
          resstr += '<a href="' + linklist[i] + '" target="braze_reference">' + title+ '</a><br />';
        }
      }
      if (!linklist.length  ) {

        $('#ticket_submit_option').show();
      }
      else if ('ShowSubmit' in curquestion) {
        if (curquestion['ShowSubmit']) {
          $('#ticket_submit_option').show();
        }
        else {
          $('#ticket_submit_option').hide();
        }
      }
      else {
        $('#ticket_submit_option').hide();
      }
      if (resstr) {
        resdiv.html(resstr);
      }
      /*if ('ShowSubmit' in curquestion) {
        if (curquestion['ShowSubmit']) {
          if (!$("#submit_ticket").prop("checked")) {
            $("#submit_ticket").prop("checked", true);
            $("#submit_ticket").trigger("change");
          }
        }
      }*/
    }
  }

  function subtype_change(e){
    var topic_selected =  $('#ticket_topic option:selected').val();
    var category_selected =  $('#ticket_category option:selected').val();
    var type_selected =  $('#ticket_subcategory option:selected').val();

    var subtype_selected =  $('#ticket_type option:selected').val();
    var subtype_links = ticket_options[topic_selected]['SelectOption'][category_selected]['SelectOption'][type_selected]['SelectOption'][subtype_selected];
    showlinks(subtype_links)

  }

  function type_change(e) {
    reset_page(3);
    var topic_selected =  $('#ticket_topic option:selected').val();
    var category_selected =  $('#ticket_category option:selected').val();
    var type_selected =  $('#ticket_subcategory option:selected').val();
    var subtype_selected = this.value;

    var subtype_options = ticket_options[topic_selected]['SelectOption'][category_selected]['SelectOption'][type_selected];
    if (subtype_options && ('Label' in subtype_options)){
      $('#ticket_type_label').html(subtype_options['Label']);
    }

    if (subtype_selected && 'SelectOption' in subtype_options) {
      hide_page(4);
      if ('SelectDefault' in subtype_options) {
        subtype_menu.append($('<option>',{value: ''}).html(subtype_options['SelectDefault']));
      }
      else {
        subtype_menu.append($('<option>',{value: ''}).html('Select a type...'));
      }
      $.each(subtype_options['SelectOption'],function(subtype)  {
        subtype_menu.append($('<option>',{value: subtype}).html(subtype));
      });
    }
    else {
      hide_page(3);
      //showlinks(subtype_options);
    }
    showlinks(subtype_options);
  }

  function category_change(e) {
    reset_page(2);

    var topic_selected =  $('#ticket_topic option:selected').val();
    var type_selected = this.value;
    var type_options = ticket_options[topic_selected]['SelectOption'][type_selected];
    //type_menu.empty();

    if (type_selected && 'SelectOption' in type_options) {
      hide_page(3);
      if ('SelectDefault' in type_options) {
        type_menu.append($('<option>',{value: ''}).html(type_options['SelectDefault']));
      }
      else {
        type_menu.append($('<option>',{value: ''}).html('Select a subcategory...'));
      }
      $.each(type_options['SelectOption'],function(type)  {
        type_menu.append($('<option>',{value: type}).html(type));
      });

    }
    else {
      hide_page(2);
    }
    showlinks(type_options);
  }

  function topic_change(e) {
    reset_page(1);
    var topic_selected = this.value;
    var category_options = ticket_options[topic_selected];
    if (topic_selected && 'SelectOption' in category_options ) {
      hide_page(2);
      if ('SelectDefault' in category_options) {
        category_menu.append($('<option>',{value: ''}).html(category_options['SelectDefault']));
      }
      else {
        category_menu.append($('<option>',{value: ''}).html('Select a category...'));
      }
      $.each(category_options['SelectOption'],function(category) {
        category_menu.append($('<option>',{value: category}).html(category));
      });
      // showlinks(category_options);
    }
    else {
      hide_page(1);
    }
    showlinks(category_options);
  }


  var tmenu = $('#ticket_menu');
  var topic_menu = $('#ticket_topic');
  var subtype_menu = $('#ticket_type');
  var type_menu = $('#ticket_subcategory');
  var category_menu = $('#ticket_category');

  function settopic(){
    reset_page(0);
    hide_page(1);

    //topic_menu.empty();
    if ('SelectDefault' in ticket_lookuptable) {
      topic_menu.append($('<option>',{value: ''}).html(ticket_lookuptable['SelectDefault']));
    }
    else {
      topic_menu.append($('<option>',{value: ''}).html('Select a topic...'));
    }
    /* Generate Initial Menu */
    $.each(ticket_options,function(topic)  {
      topic_menu.append($('<option>',{value: topic}).html(topic));
    });

  };
  settopic();

  /* if menu changes, dynamically create new menu */
  category_menu.on('change',category_change);
  type_menu.on('change',type_change);
  topic_menu.on('change',topic_change);
  subtype_menu.on('change',subtype_change);

  $('#ticket_submit_option').hide();
  /* $('#submit_ticket').on('change',function(e){
    if(this.checked){
      $('#ticket_submit_option').show();
    }
    else{
      $('#ticket_submit_option').hide();
    }
  });*/
  //showlinks(ticket_lookuptable);
  function iframeform(url) {
      var object = this;
      object.time = new Date().getTime();
      object.form = $('<form action="'+url+'" target="iframe'+object.time+'" method="post" style="display:none;" id="form'+object.time+'" name="form'+object.time+'"></form>');

      object.addParameter = function(parameter,value) {
          $("<input type='text' />")
           .attr("name", parameter)
           .attr("value", value)
           .appendTo(object.form);
      }
      object.addBodyText = function(parameter,value) {
          $("<textarea type='hidden' />")
           .attr("name", parameter)
           .html(value)
           .appendTo(object.form);
      }
      object.send = function() {
          var iframe = $('<iframe data-time="'+object.time+'" style="display:none;" id="iframe'+object.time+'"  name="iframe'+object.time+'" ></iframe>');
          $( "body" ).append(iframe);
          $( "body" ).append(object.form);
          object.form.submit();
          iframe.on('load',function(){  $('#form'+$(this).data('time')).remove();  $(this).remove();   });
      }
  }

  $('#ticket_form').submit(function(e){
    e.preventDefault();

    var mform = $(this);
    var sf_submit = new iframeform('https://webto.salesforce.com/servlet/servlet.WebToCase?encoding=UTF-8');
    var sels = mform.find('select');
    var user_name = $('#ticket_name').val();
    var user_email = $('#ticket_email').val();
    var user_ccemail = $('#ticket_ccemail').val();

    var user_subject = $('#ticket_subject').val();

    var user_issue = $('#ticket_issue').val();
    //var user_comments = mform.find('#ticket_comment').val();


    var userinfo = '';

    userinfo += "Question:\n" + user_issue ; //+  "\n\nComments: " + user_comments;
    // userinfo += "\n\nAllow Dashboard Access: ";
    // if($("#all_dashboard").is(':checked')) {
    //   userinfo += 'Yes'
    // }
    // else {
    //   userinfo += 'No'
    // }


    sf_submit.addParameter('orgid','00Dd0000000e3l4');
    sf_submit.addParameter('retURL','https://braze.com');
    sf_submit.addParameter('name',user_name);
    sf_submit.addParameter('email',user_email);
    sf_submit.addParameter('subject',user_subject);
    if (user_ccemail) {
      sf_submit.addParameter('00N0V000008wX0Y',user_ccemail);
    }
    sf_submit.addBodyText('description',userinfo);
    $.each(sels,function(k,v){
      var selopt = $(this);
      var selval = selopt.find(':selected');
      if (typeof selval !== 'undefined') {
        sf_submit.addParameter(selopt.attr('name'),selval.val());
      }
    });
    $.each(hiddenlist, function(k,v){
      if ($.urlParam(k) ){
        sf_submit.addParameter(v,$.urlParam(k));
      };
    });

    sf_submit.addParameter('external','1');
    sf_submit.send();
    var gs_submit = new iframeform('https://docs.google.com/forms/u/0/d/e/1FAIpQLScJ7eoZEY-FLTBSL5r92k6Y-iUpskG9SffRHv0GylQzgSMH-w/formResponse');
    gs_submit.addParameter('entry.1850709480', user_name);
    gs_submit.addParameter('entry.1269583593', user_email);
    gs_submit.addParameter('entry.83902596', user_subject);
    if (user_ccemail) {
      gs_submit.addParameter('entry.2143316233',user_ccemail);
    }
    gs_submit.addBodyText('entry.353828619', userinfo);
    var gs_mapping = {
      "00N0V000009G0MG" : "entry.657215056", // Topic
      "00N0V000009G0MB" : "entry.716293339",  // Category
      "00N0V000009G0ML" : "entry.1633602955", // Subcategory
      "00N0V000009G0MQ" : "entry.1959649079", // Type
      "priority" : "entry.631884783", // Priority
    }

    $.each(sels,function(k,v){
      var selopt = $(this);
      var selval = selopt.find(':selected');
      if (typeof selval !== 'undefined') {
        if (gs_mapping[selopt.attr('name')]) {
          gs_submit.addParameter(gs_mapping[selopt.attr('name')],selval.val());
        }
      }
    });
    gs_submit.send();

    $('#ticket_mainform').hide();

    $('#ticket_thankyou').fadeIn("slow");
    $('#ticket_thankyou_msg').html('<h3>Thanks for your submission!</h3>A member of our Support Team will respond to your ticket soon.<br />If you did not get a confirmation email, please check your browser\'s addon, content/privacy setting and email spam folder.<br />Otherwise, please contact your Success Manager (or email us at <a href="mailto:support@braze.com">support@braze.com</a>) to make sure your ticket has been submitted.');
    $("html, body").animate({ scrollTop: 0 }, "slow");
  });
  $('#ticket_issue').popover();
  $('#ticket_comment').popover();
  $('#ticket_priority_info').popover({
    html: true
  });

  $("#submit_ticket").trigger("change");


  function string_to_slug(str) {
    if (str) {
      str = str.toLowerCase().replace(/\s/g, '-').replace(/[^\w-]/g, '');
    }
    return str;
  }
  const algoliaInsightsPluginSupport = createAlgoliaInsightsPlugin({
    insightsClient,
    onItemsChange({ insights, insightsEvents }) {
      const events = insightsEvents.map((insightsEvent) => ({
        ...insightsEvent,
        eventName: 'Viewed from Support Search',
      }));
      insights.viewedObjectIDs(...events);
    },
    onSelect({ insights, insightsEvents }) {
      const events = insightsEvents.map((insightsEvent) => ({
        ...insightsEvent,
        eventName: 'Clicked from Support Search',
      }));
      insights.clickedObjectIDsAfterSearch(...events);
    },
  });
  autocomplete({
    container: "#support-search-div",
    panelContainer: "#support-search-panel",
    debug: true,
    placeholder: "Search",
    plugins: [algoliaInsightsPluginSupport],
    detachedMediaQuery: 'none',
    onSubmit(e){
      var query = e.state.query;
      window.location = base_url + '/search/?query=' + encodeURIComponent(query);
    },
    getSources() {
      return [{
          sourceId: "querySuggestions",
          getItemInputValue: ({ item }) => item.query,
          getItems({ query }) {
            return getAlgoliaResults({
              searchClient,
              queries: [
                {
                  indexName: "DocSearch",
                  query,
                  params: {
                    hitsPerPage: 5,
                    attributesToSnippet: ["description:12"],
                    snippetEllipsisText: " ...",
                    clickAnalytics: true,
                  },
                },
              ],
            });
          },
          getItemUrl({ item }) {
           return base_url + item.url;
         },
         templates: {
           noResults({createElement}) {
             return createElement("div", {
               dangerouslySetInnerHTML: {
                 __html: '<div class="no_results">No results were found with your current search. Try to change the search query.</div>',
                 },
               })
          },

          item({ item, createElement }) {
            var content = "";
            var title = "";
            var type = "";
            var category = "";
            var platform = "";
            var subname = "";
            var heading = "";

            if ("nav_title" in item) {
              title = item.nav_title.replaceUnder();
            } else {
              title = item.title.replaceUnder();
            }
            if ("type" in item) {
              type = item.type.replaceUnder().upCaseWord();
            }
            if ("category" in item) {
              category = item.category.replaceUnder();
            }

            if ("platform" in item) {
              if (Array.isArray(item.platform)){
                platform = item.platform.join(',').replace(/\%20/g, ' ').replace(/\_/g, ' ') + ' > ';
              }
              else {
                platform = item.platform.replace(/\%20/g, ' ').replace(/\_/g, ' ') + ' > ';
              }
            }
            if ("headings" in item) {
              if (item["headings"]) {
                heading = item["headings"][item["headings"].length - 1];
              }
            }

            var url = item.url;
            if (heading) {
              url += "#" + string_to_slug(heading);
            }
            var resulttemplate = '<a href="' +
                base_url + url + '"><div class="title"> * ' +
                platform + title + ' <div class="category">' +
                subname.replace(/\_/g, " ") +
                "</div></div></a>";
            return createElement("div", {
              dangerouslySetInnerHTML: {
                __html: resulttemplate,
              },
            });
          },
        },
      }];
    }
  });

 if (navigator.userAgent.toLowerCase().indexOf('firefox') > -1 ) {
   var ff_div = $('#firefox_warning').detach();
   ff_div.insertBefore($('#basic_page')).show();
 }
});
</script>
<div id="firefox_warning" style="display:none;">For Firefox users, please whitelist this site or check your <a href="https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Privacy/Tracking_Protection?utm_source=mozilla&utm_medium=firefox-console-errors&utm_campaign=default" target="_blank">Tracking Protection Settings</a>, or your ticket might not be submitted.</div>

<div class="container-fluid" id="main-container">
      <div class="row">
          <div class="col" >
              <h1 class="h1">Need Help? </h1>
              <div class="gradient-line"></div>
          </div>
      </div>
        <div id="ticket_mainform" class="row">
        <div class="col-sm-7" id="ticket_leftmain">
          <form id="ticket_form">


                <div class="row">
                    <div class="col">
                        <div class="form-group" id="ticket_topic_div">
                          <label for="ticket_topic" id="ticket_topic_label"> * What can we help you with? </label>
                          <select id="ticket_topic" name="00N0V000009G0MG"  class="form-control" ></select>

                        </div>
                        <div class="form-group" id="ticket_category_div">
                          <label for="ticket_category" id="ticket_category_label"> * Category </label>
                          <select id="ticket_category" name="00N0V000009G0MB"  class="form-control" ></select>
                        </div>
                        <div class="form-group" id="ticket_subcategory_div">
                          <label for="ticket_subcategory" id="ticket_subcategory_label">  * My question is about... </label>
                          <select id="ticket_subcategory" name="00N0V000009G0ML"  class="form-control" ></select>
                        </div>
                        <div class="form-group" id="ticket_type_div">
                          <label for="ticket_type" id="ticket_type_label"> * Platform </label>
                          <select id="ticket_type" name="00N0V000009G0MQ"  class="form-control" ></select>
                        </div>
                        <div class="form-group">
                          <label id="ticket_message"></label>
                          <div id="ticket_reference"></div>
                        </div>
                    </div>

                </div>
                <!-- div class="row">
                  <div class="col">
                    <label for="submit_ticket" class="checkbox-inline">

                    <input type="checkbox" value="submit_ticket" name="submit_ticket" id="submit_ticket"  />
                    Submit a ticket.</label>
                  </div>
                </div -->

                <div class="row">

                  <div class="col">
                    <div id="ticket_submit_option">
                      <h2>Not finding what you need? Contact our Support team.</h2>
                      <div class="form-group" >
                          <label for="ticket_name" id="ticket_name_label">  Name *</label>
                          <input type="text" name="Name" id="ticket_name"  maxlength="80" required="required" value="" placeholder="Enter your name" class="form-control" />
                      </div>
                      <div class="form-group" >

                        <label for="ticket_email" id="ticket_email_label"> Email Address *</label>
                        <div class="input-group">
                          <div class="input-group-prepend">
                            <span class="input-group-text" id="basic-addon1">@</span>
                          </div>
                          <input type="email" class="form-control" id="ticket_email"  maxlength="80" name="Email" placeholder="Enter email" required="required" value="" /></div>
                      </div>
                      <div class="form-group" >
                        <label for="ticket_email" id="ticket_ccemail_label"> CC Email Address </label>
                        <div class="input-group">
                          <div class="input-group-prepend">
                            <span class="input-group-text" id="basic-addon1">@</span>
                          </div>
                          <input type="email" class="form-control" id="ticket_ccemail"  maxlength="80" name="CCEmail" placeholder="Enter CC email"  value="" /></div>
                      </div>
                      <div class="form-group" >
                          <label for="ticket_subject" id="ticket_subject_label">   Subject *</label>
                          <input type="text" class="form-control" id="ticket_subject"  maxlength="80" name="Subject" placeholder="What's your question about?" required="required" value="" />
                      </div>

                      <div class="form-group" id="ticket_priority_div">
                        <label for="ticket_priority" id="ticket_priority_label"> * Issue Severity </label>
                        <a id="ticket_priority_info" title="Issue Severity Description"
                          data-toggle="popover" data-placement="top" data-trigger="click"
                          data-content="A <b>Critical Severity</b> issue has a critical business impact on use of the Braze Services that impact all Users. Examples include complete system unavailability or data integrity issues, with no workaround available at the time the issue is logged with Braze Technical Support.<br />
                          A <b>High Severity</b> issue is causing a significant loss or reductions of functionality to the customer’s use of the platform causing a serious impact to the customer’s operational activities.<br />
                          A <b>Medium Severity</b> issue causes a material loss or reduction of functionality which has an impact on the customer’s normal use of the platform.<br />
                          A <b>Low Severity</b> issue is any question about the use of Braze Services and Analytics or a minor loss or disruption of normal platform functionality."><span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-question-circle" ></span></a>
                        <select id="ticket_priority" name="priority"  class="form-control" >
                          <option value="Critical">Critical: System is Down or Severe Data Integrity Issues</option>
                          <option value="High">High: Severe Loss of Functionality or a Campaign Will Not Send</option>
                          <option value="Medium">Medium: Degraded Performance or Issue Causing Significant Business Impact</option>
                          <option value="Low" selected="selected">Low: Question About Braze Functionality or Analytics</option>
                        </select>
                      </div>

                      <div class="form-group" >

                          <label for="ticket_issue" id="ticket_issue_label">     Question </label>

                          <textarea name="ticket_issue" class="form-control" id="ticket_issue" data-toggle="popover" data-trigger="focus" data-placement="top"
                          data-content="Include information helpful for investigation and troubleshooting, such as your platform, SDK version, REST API endpoints, links to segments or campaigns, and relevant user IDs. Please also include steps to reproduce your issue. "
                          placeholder="Include information helpful for investigation and troubleshooting, such as your platform, SDK version, REST API endpoints, links to segments or campaigns, and relevant user IDs. Please also include steps to reproduce your issue.  " rows="7"></textarea>
                      </div>
                      <!-- div class="form-group" >

                          <label for="ticket_comment"  id="ticket_comment_label">     Additional comments and screenshots  </label>

                          <textarea name="Issue_Steps" class="form-control" id="ticket_comment" data-toggle="popover" data-trigger="focus" data-placement="top"
                          data-content="Add any other comments and link to any relevant screenshots or screencasts."
                          placeholder="Add any other comments and link to any relevant screenshots or screencasts." rows="7"></textarea>
                      </div -->
                      <div class="form-group">
                          <label style="font-size: 12px;">
                         In order to provide you with technical support or address service or technical problems, please be aware that Braze may need to access your dashboard and data.
                          </label>
                          <label style="font-size: 12px;">
                          Braze Technical Support Hours of Operation are from 9am-5pm GMT and 8am-8pm ET, Monday - Friday, excluding Braze Recognized Holidays. For issues logged outside of these hours, you should anticipate a response on the next business day.
                          </label>
                      </div>
                      <button type="submit" name="Submit Ticket" value="Submit" class="btn btn-black" id="ticket_submit_button" role="button"> SUBMIT TICKET </button>
                      </div>
                  </div>
              </div>
              </form>
        </div>
        <div class="col-sm-5" id="ticket_resources">
        <div id="support-search-div">
         </div>

           <div id="support-search-panel"></div>

            <legend>Useful Resources</legend>

            <div id="ticket_usefulresources">
              <a target="" href="{{site.baseurl}}/user_guide/introduction/">User Guide</a><br />
              <a target="" href="{{site.baseurl}}/developer_guide/platform_wide/platform_features/">Developer Guide</a><br />
              <a target="" href="{{site.baseurl}}/help/home/">Help & Troubleshooting Guides</a><br />
              <a target="" href="{{site.baseurl}}/help/faqs/">FAQs</a><br />
              <a target="" href="https://lab.braze.com/">LAB</a><br />
              <a target="" href="https://dashboard.braze.com/">Braze Dashboard</a><br />
            </div>

        </div>
    </div>
    <div id="ticket_thankyou" style="display:none;"><div class="row"><div class="col" id="ticket_thankyou_msg"></div></div></div>
</div>
