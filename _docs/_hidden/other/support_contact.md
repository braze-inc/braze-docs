---
permalink: /support_contact/
nav_title: Help | Braze
hide_nav: true
layout: basic
hide_toc: true
---
<link rel="stylesheet" href="https://cdn.jsdelivr.net/docsearch.js/2/docsearch.min.css" />


<style type="text/css">
  .legal-disclaimer{
     font-size: 14px;
    word-wrap: normal;
    color: #101828;
  }

.su-tooltip {
  background: #fff;
  border: 1px solid #ccc;
  border-radius: 6px;
  padding: 8px 10px;
  max-width: 280px;
  font-size: 13px;
  line-height: 1.4;
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}

.su-tooltip strong {
  font-size: 14px;
  display: block;
  margin-bottom: 4px;
}

lable.lable-gpt {
    font-weight: 700;
    font-size: 14px;
    line-height: 16px;
    color: black;
    vertical-align: middle;
    margin-top: 15px;
}

@media (min-width: 768px) and (max-width: 1024px) {
    .container-fluid {
        width: 910px !important;
    }
    .main-border {
        width: 950px !important;
    }
    .svg-hr svg {
        width: 945px !important;
    }
    input#subject {
        width: 910px !important;
    }
    textarea#description {
        width: 910px !important;
    }
    .svg1 svg {
    width: 910px !important;;
}
 .svg2 svg {
    width: 910px !important;;
}

#basic_page {
    min-height: calc(68vh - 186px) !important;
  }
}

  @media (max-width: 600px) {
    .btn-right {
    display: flex;
    flex-direction: column;
}


    .container-fluid {
        width: 354px;
        padding-right: 15px;
        padding-left: 15px;
        margin-right: auto;
        margin-left: auto;
        min-height: calc(100vh - 700px) !important;
    }
    .svg-hr svg {
    width: 417px !important;
    }
    .svg1 svg {
      width: 300px !important;;
    } 
    .svg2 svg {
      width: 300px !important;;
    }

    .gpt-res-buttons {
        flex-direction: column;
    }

    .steps {
        display: none !important;
    }

    .main-border {
        border-radius: 14px;
        border: 2px solid #D0D5DD;
        background: #FFF;
        width: 407px !important;
        box-shadow: 0 4px 27px 0 rgba(0, 0, 0, 0.02);
    }

    input#subject {
        width: 367px !important;
    }

    textarea#description {
        width: 367px !important;
    }

    .step:before {
        padding-left: 13px;
    }

    .step {
        margin-bottom: 2px;
        text-align: left;
        display: flex;
        align-items: center;
    }

    .submit-btn {
        width: 262px;
        margin-bottom: 10px;
        margin-right: 0;
    }
}


 .svg-dot path {
  stroke: gray; /* default */
}

.svg-dot.active path {
  stroke: #5711E5; /* when active */
}

  body{
     font-family: "Aribau Grotesk Regular", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;
  }
div#ticket_thankyou {
    margin-top: 5rem;
    margin-bottom: 155px;
    display: flex;
    justify-content: center;
}

  button#ticket_submit_button {
    padding: 12px !important;
    background: #4411D6 !important;
    border-radius: var(--inner, 8px) !important;
    border: 2px solid #4411D6 !important;
}
   button#ticket_submit_button {
    border-radius: var(--inner, 8px);
    background: #4411D6;
    color:white;
}
  .flex-display{
    display:none;
  }
  .gpt-res-buttons {
  display: flex;
  justify-content: space-between; /* Back on left, rest on right */
  align-items: center;
  width: 100%;
  margin-top: 15px;
}

.btn-right {
  display: flex;
  gap: 10px; /* space between the two right buttons */
}
  .gpt-text1{
    display:none;
  }


  button#backToStep1 {
    border-radius: var(--inner, 8px);
    background-color: #4411D6 !important;
    height: 40px;
    padding-top: -12px;
    padding: 6px var(--lg, 16px);
    color:white;
}

button.submit-btn {
    border-radius: var(--inner, 8px);
    border: 1px solid #0103C5;
    background: var(--neutral-background-default, #FFF);
    color: #4411D6;
    text-align: center;
    leading-trim: both;
    text-edge: cap;
    font-size: 14px;
    font-style: normal;
    font-weight: 700;
    line-height: 20px;
}

.for-line {
    margin-top: -29px;
    line-height: 21px;
    margin-left: -11px;
    height: 300px;
}

   
.svg2 svg path {
  stroke-dasharray: 1250;   /* total path length */
  stroke-dashoffset: 1250;  /* initially hidden */
  animation: progressAnim 3s linear forwards;
}

@keyframes progressAnim {
  from {
    stroke-dashoffset: 1250;
  }
  to {
    stroke-dashoffset: 0;
  }
}

  .svg1{
     fill: linear-gradient(90deg, rgba(201, 196, 255, 0.40) 21.38%, rgba(128, 30, 215, 0.40) 42.75%, rgba(255, 165, 36, 0.40) 64.13%);
  }
  .svg2{
     fill: linear-gradient(90deg, rgba(201, 196, 255, 0.40) 50.12%, rgba(128, 30, 215, 0.40) 71.5%, rgba(255, 165, 36, 0.40) 92.87%);
  }
  .steps svg {
    margin-top: 14px;
   
}
  div#suggestionsBox h1 {
    font-size: 20px;
    font-weight: bold;
  }

  div#suggestionsBox p {
      font-size: 14px;
  }

  div#suggestionsBox h2, div#suggestionsBox h3 {
      font-size: 18px;
      font-weight: bold;
  }

  div#suggestionsBox li {
      font-size: 14px;
  }
  
   .gpt-text {
    margin-top: 2px;
   }

   .gpt-heading{
      color: #5711E5;
      font-size: 18px;
      font-weight: 700;
      line-height: 20.8px; /* 115.556% */
   }

  .gpt-responce {
    display: inline-flex;
    gap:9px;
    color: #212123;
    font-size: 16px;
    font-weight: 700;
    line-height: 20px;
    padding: 9px;
  }

  textarea#description {
    border-radius: var(--inner, 8px);
    border: 1px solid #7D7D83;
    background: var(--neutral-background-default, #FFF);
    display: flex;
    width: 1250px;
    height: 154px;
    padding-left: var(--md, 12px);
    justify-content: space-between;
    align-items: center;
   
}
  input#subject {
    border-radius: var(--inner, 8px);
    border: 1px solid #7D7D83;
    background: var(--neutral-background-default, #FFF);
    display: flex;
    width: 1250px;
    height: var(--Field-height-Regular, 40px);
    padding-left: var(--md, 12px);
    justify-content: space-between;
    align-items: center;
}

  button#toStep2 {
    border-radius: var(--inner, 8px);
    border: 1px solid #0103C5;
    background: var(--neutral-background-default, #FFF);
    color: #4411D6;
    text-align: center;
    leading-trim: both;
    text-edge: cap;
    font-size: 14px;
    font-weight: 700;
    line-height: 20px; /* 142.857% */
}

  .main-form{
    margin-bottom: 29px;
  }

  .main-border {
    border-radius: 14px;
    border: 2px solid #D0D5DD;
    background: #FFF;
    width:1314px;
    box-shadow: 0 4px 27px 0 rgba(0, 0, 0, 0.02);
}

  div#articles {
    display: none !important;
}

div#ticket_resources {
    display: none;
}

#main-container {
  margin-top: 20px;
  margin-bottom: 50px;
  min-height: 600px;
  margin-left:-4rem;
}
#main-container label {
  font-weight: bold;
  
  color: #101828;
leading-trim: both;
text-edge: cap;
 font-family: "Aribau Grotesk Regular", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;
font-size: 13px;
font-style: normal;
font-weight: 700;
line-height: 18px; /* 138.462% */
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
  background: linear-gradient(90deg, rgba(201,196,255,1) 30%, rgba(128,30,215,1) 60%, rgba(255,165,36,1) 90%);
  height: 3px;
  width: 108px;
}

a {
  font-family: "Aribau Grotesk Regular", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;
  display: inline;
  color: rgb(128, 30, 215);
  font-weight: normal;
  @media print {
    font-weight: normal;
  }
  transition: all ease 0.2s;
  -webkit-transition: all ease 0.2s;
  -moz-transition: all ease 0.2s;
  border-color: rgb(128, 30, 215);
  border-bottom-width: 2px;
  border-bottom-style: solid;
  line-height: 2.5;
}

a:hover {
  background-color: rgb(128, 30, 215);
  text-decoration: none;

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
  font-family: "Aribau Grotesk Regular", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;
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
  background-color: #4411D6 !important;
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
.hidden {
              display: none !important;
            }
        h1 {
            color: #2c3e50;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }

        /* Divider Line */
        hr {
            border: 0;
            height: 1px;
            background: linear-gradient(to right, transparent, #3498db, transparent);
            margin: 30px 0;
        }

        /* Step Indicators */
        .steps {
            display: flex;
            justify-content: space-between;
            margin: 30px 41px !important;
            counter-reset: step;
            margin-bottom: -11px !important;
        }

        .step {
            position: relative;
            flex: 1;
            text-align: center;
            color: #7f8c8d;
        }

        .step:before {
            counter-increment: step;
            content: counter(step);
            display: inline-block;
            width: 37px;
            height: 37px;
            margin: 0  10px;
            line-height: 35px;
            margin-bottom: 24px;
            background-color: #bdc3c7;
            color: white;
            border-radius: 50%;
            font-weight: bold;
        }

        .step.active {
            color: #2c3e50;
            font-weight: bold;
        }

        .step.active:before {
            background-color: #5711E5;
        }

        /* Form Styles */
        .form-group {
            margin-bottom: 25px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #2c3e50;
        }

        .form-group input[type="text"],
        .form-group textarea,
        .form-group select {
            width: 100%;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
            transition: border-color 0.3s;
        }

        .form-group input[type="text"]:focus,
        .form-group textarea:focus,
        .form-group select:focus {
            border-color: #3498db;
            outline: none;
            box-shadow: 0 0 0 2px rgba(52, 152, 219, 0.2);
        }

        .form-group textarea {
            min-height: 150px;
            resize: vertical;
        }

        /* Required Field Indicator */
        .required::before  {
            content: " *";
            color: #e74c3c;
        }

        /* Button Styles */
        .submit-btn {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 12px 25px;
            font-size: 16px;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
            margin-right: 10px;
        }

       

        /* Support Link */
        .support-link {
            color: #3498db;
            text-decoration: none;
            font-weight: 600;
        }

        .support-link:hover {
            text-decoration: underline;
        }

        /* Form Container */
        .form-container {
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: none !important;
        }

        /* Attachment Styles */
        .attachment-container {
            margin-top: 20px;
        }

        .attachment-label {
            font-weight: 600;
            margin-bottom: 8px;
            color: #2c3e50;
        }

        /* Button Container */
        .button-container {
            display: flex;
            justify-content: space-between;
            margin-top: 30px;
        }

        /* Responsive Adjustments */
        @media (max-width: 600px) {
            .steps {
                flex-direction: column;
            }
            
            .step {
                margin-bottom: 20px;
                text-align: left;
                display: flex;
                align-items: center;
            }
            
            .step:before {
                margin: 0 15px 0 0;
            }
            
            .button-container {
                flex-direction: column;
            }
            
            .submit-btn {
                width: 100%;
                margin-bottom: 10px;
                margin-right: 0;
            }
        }

        /* Popover Styles */
        .popover {
            max-width: 400px;
        }
        
        /* Header Styles */
        h1 {
            color: #2c3e50;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }

        /* Divider Line */
        hr {
            border: 0;
            height: 1px;
            background: linear-gradient(to right, transparent, #3498db, transparent);
            margin: 30px 0;
        }

        /* Step Indicators */
        .steps {
            display: flex;
            justify-content: space-between;
            margin: 30px 0;
            counter-reset: step;
        }

        .step {
            position: relative;
            flex: 1;
            text-align: center;
            color: #7f8c8d;
        }


        .step.active {
            color: #2c3e50;
            font-weight: bold;
        }

        .step.active:before {
            background-color:#5711E5 ;
        }

        /* Form Styles */
        .form-group {
            margin-bottom: 25px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #2c3e50;
        }

        .form-group input[type="text"],
        .form-group textarea {
            width: 100%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
            transition: border-color 0.3s;
        }

        .form-group input[type="text"]:focus,
        .form-group textarea:focus {
            border-color: #3498db;
            outline: none;
            box-shadow: 0 0 0 2px rgba(52, 152, 219, 0.2);
        }

        .form-group textarea {
            min-height: 150px;
            resize: vertical;
        }

        /* Required Field Indicator */
        .required::before {
            content: " *";
            color: #e74c3c;
        }

        /* Button Styles */
        .submit-btn {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 12px 25px;
            font-size: 16px;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        /* Support Link */
        .support-link {
            color: #3498db;
            text-decoration: none;
            font-weight: 600;
        }

        .support-link:hover {
            text-decoration: underline;
        }

        /* Form Container */
        .form-container {
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        /* Response Styles */
        #suggestionsBox {
            padding: 15px;
            border-radius: 4px;
        }

        #articles {
            margin-top: 20px;
            display: none;
        }

        .article {
            margin-bottom: 10px;
        }

        .article a {
            color: #3498db;
            text-decoration: none;
        }

        .article a:hover {
            text-decoration: underline;
        }

        /* Responsive Adjustments */
        @media (max-width: 600px) {
            .steps {
                flex-direction: column;
            }
            
            .step {
                margin-bottom: 20px;
                text-align: left;
                display: flex;
                align-items: center;
            }
        }

        #suggestionsBox {
            padding: 15px;
            border-radius: 4px;
            line-height: 26px;
        }
        
        #suggestionsBox h1, #suggestionsBox h2, #suggestionsBox h3 {
            color: #2c3e50;
            margin-top: 0;
        }
        
        #suggestionsBox ul { padding-left: 20px; }        
        #suggestionsBox li { margin-bottom: 8px; }
        span.highlight { color: black !important; }
        
        .su_citation {
          border: none;
          color: #081A59;
          font-family: "Aribau Grotesk TRIAL";
          font-size: 13px;
          line-height: 160%;
          border-radius: 2px;
          background: rgba(87, 17, 229, 0.12);
          margin-right: 11px;
          cursor: pointer;
          margin-left: 6px;
      }


      .gptGradientContainer{
          background: linear-gradient(342.01deg, rgba(212, 239, 243, 0.2) 17.09%, rgba(253, 163, 161, 0.3) 113.99%, #FBA9F8 280.75%);
          margin-bottom:24px;
          border-radius:8px;
          padding:12px;
      }

</style>

<div>
    <div class="container-fluid" id="main-container">
      <div class="row main-form">
          <div class="col" >
              <h1 class="h1">Need Help? </h1>
              <div class="gradient-line"></div>
          </div>
   </div>
        <div class="main-border">
        <div class="steps">
            <div class="step active">Basic Details</div>
            <svg xmlns="http://www.w3.org/2000/svg" width="282" height="2" viewBox="0 0 282 2" fill="none">
  <path d="M0 1L282 1.00002" stroke="#5711E5" stroke-dasharray="3 3"/>
</svg>
            <div class="step">Suggested Content</div>
            <div class="svg-dot">
            <svg xmlns="http://www.w3.org/2000/svg" width="282" height="2" viewBox="0 0 282 2" >
  <path d="M0 1L282 1.00002"  stroke-dasharray="3 3"/>
</svg>
</div>
            <div class="step">Submit the Case</div>
        </div>

        <div class='svg-hr'>
        <svg xmlns="http://www.w3.org/2000/svg" width="1310" height="2" viewBox="0 0 1310 2" fill="none">
  <path d="M0 1H1310" stroke="#D0D5DD" stroke-width="2"/>
</svg>
        </div>

<div class="form-container">
        <form id="supportForm">
            <!-- Step 1 -->
            <div id="step1">
                <div class="form-group">
                    <label for="subject" class="required">Subject</label>
                    <input type="text" id="subject" name="subject"  required>
                </div>

                <div class="form-group">
                    <label for="description" class="required">Description</label>
                    <textarea id="description" name="description" required></textarea>
                </div>

                <button type="button" class="submit-btn" id="toStep2" >Continue to Suggested Content</button>
            </div>

            <!-- Step 2 -->
            <div id="step2" style="display:none;">
                <h2 class='gpt-heading'></h2>
                 <h2 class='gpt-heading'></h2>
                <div class="gptGradientContainer">
                 <div class='gpt-responce'>
                 <svg xmlns="http://www.w3.org/2000/svg" width="20" height="21" viewBox="0 0 20 21" fill="none">
  <path d="M16.1 14.5812L15.305 16.3662L13.544 17.1722C13.456 17.2137 13.3816 17.2793 13.3295 17.3615C13.2774 17.4436 13.2498 17.5389 13.2498 17.6362C13.2498 17.7335 13.2774 17.8287 13.3295 17.9109C13.3816 17.9931 13.456 18.0587 13.544 18.1002L15.305 18.9062L16.1 20.7062C16.1389 20.7952 16.203 20.8709 16.2844 20.9241C16.3657 20.9773 16.4608 21.0056 16.558 21.0056C16.6551 21.0056 16.7502 20.9773 16.8315 20.9241C16.9129 20.8709 16.977 20.7952 17.016 20.7062L17.811 18.9212L19.582 18.1152C19.6699 18.0737 19.7443 18.0081 19.7964 17.9259C19.8485 17.8437 19.8762 17.7485 19.8762 17.6512C19.8762 17.5539 19.8485 17.4586 19.7964 17.3765C19.7443 17.2943 19.6699 17.2287 19.582 17.1872L17.821 16.3812L17.026 14.5812C16.9857 14.4921 16.9206 14.4165 16.8385 14.3635C16.7564 14.3104 16.6607 14.2822 16.563 14.2822C16.4652 14.2822 16.3695 14.3104 16.2874 14.3635C16.2053 14.4165 16.1402 14.4921 16.1 14.5812Z" fill="#91186E"/>
  <path d="M9.14095 7.94993L7.54095 4.37893C7.46284 4.20119 7.33468 4.05003 7.17211 3.9439C7.00954 3.83776 6.81959 3.78125 6.62545 3.78125C6.4313 3.78125 6.24135 3.83776 6.07878 3.9439C5.91621 4.05003 5.78806 4.20119 5.70995 4.37893L4.10995 7.94993L0.584947 9.57193C0.408701 9.6548 0.259678 9.78611 0.155296 9.95053C0.0509136 10.1149 -0.0045166 10.3057 -0.0045166 10.5004C-0.0045166 10.6952 0.0509136 10.8859 0.155296 11.0503C0.259678 11.2148 0.408701 11.3461 0.584947 11.4289L4.10695 13.0509L5.70695 16.6219C5.78506 16.7997 5.91321 16.9508 6.07578 17.057C6.23835 17.1631 6.4283 17.2196 6.62245 17.2196C6.81659 17.2196 7.00654 17.1631 7.16911 17.057C7.33168 16.9508 7.45984 16.7997 7.53795 16.6219L9.13795 13.0509L12.6599 11.4289C12.8362 11.3461 12.9852 11.2148 13.0896 11.0503C13.194 10.8859 13.2494 10.6952 13.2494 10.5004C13.2494 10.3057 13.194 10.1149 13.0896 9.95053C12.9852 9.78611 12.8362 9.6548 12.6599 9.57193L9.14095 7.94993Z" fill="#801ED7"/>
  <path d="M17.0259 6.41957L17.8209 4.63457L19.5819 3.82857C19.6699 3.78709 19.7443 3.72143 19.7964 3.63928C19.8485 3.55712 19.8761 3.46185 19.8761 3.36457C19.8761 3.2673 19.8485 3.17203 19.7964 3.08987C19.7443 3.00772 19.6699 2.94206 19.5819 2.90057L17.8209 2.09257L17.0259 0.292575C16.9869 0.203559 16.9229 0.127833 16.8415 0.074658C16.7602 0.0214831 16.6651 -0.00683594 16.5679 -0.00683594C16.4708 -0.00683594 16.3757 0.0214831 16.2943 0.074658C16.213 0.127833 16.1489 0.203559 16.1099 0.292575L15.3149 2.07757L13.5449 2.89257C13.4569 2.93406 13.3826 2.99972 13.3305 3.08187C13.2784 3.16403 13.2507 3.2593 13.2507 3.35658C13.2507 3.45385 13.2784 3.54912 13.3305 3.63128C13.3826 3.71343 13.4569 3.77909 13.5449 3.82057L15.3059 4.62657L16.1009 6.42657C16.142 6.51509 16.2076 6.58992 16.29 6.64212C16.3724 6.69433 16.4681 6.7217 16.5657 6.72096C16.6632 6.72022 16.7585 6.69141 16.8401 6.63796C16.9218 6.58452 16.9863 6.5087 17.0259 6.41957Z" fill="#E9371F"/>
</svg>
<div class='gpt-text'>Generating... </div>
<div class='gpt-text1'>Generated answer for you </div>
                 </div>

                <div id="suggestionsBox">
                <div class= "for-line">
                
                <div class="svg1"><svg xmlns="http://www.w3.org/2000/svg" width="100%" height="9" viewBox="0 0 1250 9" fill="none">
  <path d="M1246.26 0H3.74224C1.67546 0 0 2.01472 0 4.5C0 6.98528 1.67546 9 3.74224 9H1246.26C1248.32 9 1250 6.98528 1250 4.5C1250 2.01472 1248.32 0 1246.26 0Z" fill="url(#paint0_linear_45139_47694)" fill-opacity="0.4"/>
  <defs>
    <linearGradient id="paint0_linear_45139_47694" x1="0" y1="4.5" x2="890.654" y2="4.5" gradientUnits="userSpaceOnUse">
      <stop offset="0.3" stop-color="#C9C4FF"/>
      <stop offset="0.6" stop-color="#801ED7"/>
      <stop offset="0.9" stop-color="#FFA524"/>
    </linearGradient>
  </defs>
</svg></div>
                <div class="svg2"><svg xmlns="http://www.w3.org/2000/svg" width="100%" height="9" viewBox="0 0 1250 9" fill="none">
  <path d="M3.74231 0H1246.26C1248.32 0 1250 2.01472 1250 4.5C1250 6.98528 1248.32 9 1246.26 9H3.74231C1.67554 9 0 6.98528 0 4.5C0 2.01472 1.67554 0 3.74231 0Z" fill="url(#paint0_linear_45139_47693)" fill-opacity="0.4"/>
  <defs>
    <linearGradient id="paint0_linear_45139_47693" x1="890.652" y1="4.5" x2="-0.00114137" y2="4.5" gradientUnits="userSpaceOnUse">
      <stop offset="0.3" stop-color="#C9C4FF"/>
      <stop offset="0.6" stop-color="#801ED7"/>
      <stop offset="0.9" stop-color="#FFA524"/>
    </linearGradient>
  </defs>
</svg></div>
</div>
                </div>
             




                <div id="articles">
                    <h3>Related Articles:</h3>
                    <div id="articles-list"></div>
                </div>
                </div>

                <div class="flex-display">
                <div class= "legal-disclaimer">
                  <em>Disclaimer: This reply was generated by AI and is for information only. Please confirm the linked sources in the Braze Documentation.</em>
                </div>
                <div class="gpt-res-buttons">
                <button type="button" class="submit-btn" id="backToStep1" style="background-color:grey;">Back</button>
                <div class="btn-right">

                <lable class='lable-gpt'>Did this resolve your issue?</lable>
                <button type="button" class="submit-btn" onclick="window.location.href='/docs/'" >Yes, close this Window </button>
                <button type="button" class="submit-btn" id="toStep3">No, continue with ticket creation</button>
                </div>
                </div>
                </div>

            </div>


        </form>
    </div>

<div class="form-container1"  style="display:none;">
 <div id="step3" >
<div id="firefox_warning" style="display:none;">For Firefox users, allowlist this site or check your <a href="https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Privacy/Tracking_Protection?utm_source=mozilla&utm_medium=firefox-console-errors&utm_campaign=default" target="_blank">Tracking Protection Settings</a>, or your ticket might not be submitted.</div>

<div id="ticket_mainform" class="container">
    <form  id="ticket_form">
      <div id="step3">
        <h2>Not finding what you need? Contact our Support team.</h2>
        <!-- Row 1 -->
        <div class="row">
          <div class="col-md-6">
            <div class="form-group">
              <label for="ticket_topic" class="required">What can we help you with? </label>
              <select id="ticket_topic" name="00N0V000009G0MG" class="form-control"></select>
            </div>
          </div>
          <div class="col-md-6">
            <div class="form-group">
              <label for="ticket_category" class="required">Category </label>
              <select id="ticket_category" name="00N0V000009G0MB" class="form-control"></select>
            </div>
          </div>
        </div>
  
        <!-- Row 2 -->
        <div class="row">
          <div class="col-md-6" id="subcategory_div" style="display:none;">
            <div class="form-group">
              <label for="ticket_subcategory" class="required">My question is about... </label>
              <select id="ticket_subcategory" name="00N0V000009G0ML" class="form-control"></select>
            </div>
          </div>
          <!-- <div class="col-md-6">
            <div class="form-group">
              <label for="ticket_type">Platform *</label>
              <select id="ticket_type" name="00N0V000009G0MQ" class="form-control"></select>
            </div>
          </div> -->
        </div>
  
        <!-- <h2>Not finding what you need? Contact our Support team.</h2> -->
  
        <!-- Row 3 -->
        <div class="row">
          <div class="col-md-6">
            <div class="form-group">
              <label for="ticket_name" class="required">Name</label>
              <input type="text" id="ticket_name" name="Name" placeholder="Enter your name" class="form-control" required>
            </div>
          </div>
          <div class="col-md-6">
            <div class="form-group">
              <label for="ticket_email" class="required">Email address </label>
              <input type="email" id="ticket_email" name="Email" placeholder="Enter email" class="form-control" required>
            </div>
          </div>
        </div>
  
        <!-- Row 4 -->
        <div class="row">
          <div class="col-md-6">
            <div class="form-group">
              <label for="ticket_ccemail">CC Email address</label>
              <input type="email" id="ticket_ccemail" name="CCEmail" placeholder="Enter CC email" class="form-control">
            </div>
          </div>
          <div class="col-md-6">
            <div class="form-group">
              <label for="ticket_priority" class="required">Issue severity </label>
              <select id="ticket_priority" name="priority" class="form-control">
                <option value="Critical">Critical: System is down or severe data integrity issues</option>
                <option value="High">High: Severe loss of functionality or a campaign will not send</option>
                <option value="Medium">Medium: Degraded performance or issue causing significant business impact</option>
                <option value="Low" selected>Low: Question about Braze functionality or analytics</option>
              </select>
            </div>
          </div>
        </div>
  
        <!-- Subject (Full width) -->
        <div class="form-group">
          <label for="ticket_subject" class="required">Subject </label>
          <input type="text" id="ticket_subject" name="Subject" placeholder="What's your question about?" class="form-control" required>
        </div>
  
        <!-- Question (Full width) -->
        <div class="form-group">
          <label for="ticket_issue" class="required">Question </label>
          <textarea id="ticket_issue" name="ticket_issue" rows="7" class="form-control" placeholder="Include details such as platform, SDK version, REST API endpoints, steps to reproduce..."></textarea>
        </div>
  
        <!-- Info text -->
        <div class="form-group small-text">
          <p>In order to provide you with technical support or address service or technical problems, be aware that Braze may need to access your dashboard and data. Braze technical support operates during standard business hours across multiple time zones to serve our global customer base. For specific support hours in your region or for issues logged outside of business hours, please refer to the support handbook. Response times may vary based on when your request is submitted, your support tier, and the severity of the issue.</p>
        </div>
  
        <!-- Submit button -->
        <div class="form-group text-right">
          <button type="submit" name="Submit" value="Submit" class="btn btn-black" id="ticket_submit_button" role="button"> SUBMIT </button>
        </div>
  
      </div>
    </form>
  </div>
       <div id="ticket_thankyou" style="display:none;"><div class="row"><div class="col" id="ticket_thankyou_msg"></div></div></div>
</div>
</div>
</div>


</div>
 


</div>
<script type="text/javascript" src="https://d3afgxkm1vz2tp.cloudfront.net/217433e2c4c2797776e373f19d94feff/search-clients/63590d8d-65fd-11f0-ada3-0242ac120007/an.js"></script>

<script type="text/javascript">

   let citationClicked = false;
   const steps = document.querySelectorAll('.step');
    const step1 = document.getElementById('step1');
    const step2 = document.getElementById('step2');
    const step3 = document.getElementById('step3');
   const subjectInput = document.getElementById('subject');
const descriptionInput = document.getElementById('description');
const nextButton = document.getElementById('toStep2');

// Step 1: Enter in Subject → focus Description
subjectInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        e.preventDefault();
        descriptionInput.focus();
    }
});



nextButton.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        e.preventDefault();
        nextButton.click();
    }
});



    const caseId = "CASE-" + Date.now() + "-" + Math.floor(Math.random() * 1000);
    const caseNumber = Math.floor(100000 + Math.random() * 900000);

     function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
        return null;
      }
       const sid = getCookie('_gz_sid');  
       const taid = getCookie('_gz_taid');



  document.addEventListener('DOMContentLoaded', function() {
    
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
  'LinksTitle': ['Marketer documentation','Developer documentation','Marketer troubleshooting guide','Frequently Asked Questions'],
  'Links': ['{{site.baseurl}}/user_guide/introduction/','{{site.baseurl}}/developer_guide/platform_wide/platform_features/','{{site.baseurl}}/help/home/','{{site.baseurl}}/help/faqs/'],
  'SelectOption': {
    'Technical Issue': {
      'Label': '* Category',
      'SelectDefault': 'Select a category...',
      'LinksTitle': ['Platform Features'],
      'Links' : ['{{site.baseurl}}/developer_guide/platform_wide/platform_features/'],
      'SelectOption' : {
        'SDK Integrations' : {
          'Label': 'My question is about... *',
          'SelectDefault': 'Select a type...',
          'LinksTitle': ['Self-Service SDK Debugging Tool','iOS: Initial SDK Setup','Android: Initial SDK Setup','Web: Initial SDK Setup','Sending Test Messages','Braze Learning Course: Technical Integration Checklist and Toolkits'],
          'Links': ['{{site.baseurl}}/developer_guide/sdk_integration/debugging','{{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview','{{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/','{{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/','https://learning.braze.com/technical-integration-checklists-and-toolkits'],
          'SelectOption' : {
            'Push' : {
              'SelectDefault': 'Select a platform...',
              'LinksTitle': [],
              'Links': [],
              'Label': 'Platform *',
              'SelectOption' : {
                'Android' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Android: Push Integration','Android: Push Troubleshooting'],
                  'Links' : ['{{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/troubleshooting/']
                },
                'iOS' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['iOS: Push Integration', 'iOS: Push Troubleshooting'],
                  'Links': ['{{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/troubleshooting/']
                },
                'Web' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Web: Push Integration','Web: Error Logging'],
                  'Links': ['{{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#error-logging']
                },
                'Other' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Braze Developer Guide','SDK Changelog','Sending Test Messages','Braze Learning Course: Technical Integration Checklist and Toolkits'],
                  'Links' : ['{{site.baseurl}}/developer_guide/home','{{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs','{{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/','https://learning.braze.com/technical-integration-checklists-and-toolkits']
                }
              }
            },
            'In-App Messages': {
              'LinksTitle': [''],
              'Links':  [''],
              'Label': 'Platform *',
              'SelectDefault': 'Select data type...',
              'SelectOption' : {
                'Android' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Android: In-App Message Integration','Android: In-App Message Customization','Android: In-App Message Troubleshooting'],
                  'Links' : ['{{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization','{{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/troubleshooting/']
                },
                'iOS' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['iOS: In-App Message Integration','iOS: In-App Message Customization','iOS: In-App Message Troubleshooting'],
                  'Links': ['{{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization','{{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/troubleshooting/']
                },
                'Web' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Web: In-App Message Integration','Web: In-App Message Customization','Web: In-App Message Troubleshooting','Web: Error Logging'],
                  'Links': ['{{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/customization','{{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/troubleshooting/','{{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#error-logging']
                },
                'Other' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Braze Developer Guide','SDK Changelog','Sending Test Messages','Braze Learning Course: Technical Integration Checklist and Toolkits'],
                  'Links' : ['{{site.baseurl}}/developer_guide/home','{{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs','{{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/','https://learning.braze.com/technical-integration-checklists-and-toolkits']
                }
              }
            },
            'Content Cards': {
              'LinksTitle': [''],
              'Label': 'Platform *',
              'SelectDefault': 'Select data type...',
              'SelectOption' : {
                'Android' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Android: Content Card Integration','Android: Content Card Customization'],
                  'Links' : ['{{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization']
                },
                'iOS' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['iOS: Content Card Integration','iOS: Content Card Customization'],
                  'Links' : ['{{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/customization']
                },
                'Web' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Web: Content Card Integration','Web: Content Card Customization','Web: Error Logging'],
                  'Links' : ['{{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization','{{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#error-logging']
                },
                'Other' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Braze Developer Guide','SDK Changelog','Sending Test Messages','Braze Learning Course: Technical Integration Checklist and Toolkits'],
                  'Links' : ['{{site.baseurl}}/developer_guide/home','{{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs','{{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/','https://learning.braze.com/technical-integration-checklists-and-toolkits']
                }
              }
            },
            'User Data' :{
              'ShowSubmit': false,
              'Label': 'Category *',
              'LinksTitle': ['Automatically Collected Data','Event Naming Conventions','User Profile Lifecycle'],
              'Links': ['{{site.baseurl}}/developer_guide/platform_wide/analytics_overview#automatically-collected-data','{{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/','{{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-profile-lifecycle'],
                'SelectOption' : {
                'Custom Events, Purchase Event, and Properties' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Custom Events','Purchase Events','Android: Tracking Custom Events','iOS: Tracking Custom Events','Web: Tracking Custom Events'],
                  'Links' : ['{{site.baseurl}}/user_guide/data_and_analytics/custom_data/events/','{{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/','{{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/','{{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/','{{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events']
                },
                'Custom Attributes' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Custom Attributes','Android: Setting Custom Attributes','iOS: Setting Custom Attributes','Web: Setting Custom Attributes'],
                  'Links' : ['{{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#custom-attributes','{{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/','{{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/','{{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes/']
                }
              }
            },
            'Other' :{
              'ShowSubmit': true,
              'LinksTitle': [''],
              'Links': ['']
            }
          }
        },
        'REST APIs' : {
          'Label': 'My question is about... *',
          'SelectDefault': 'Select a type...',
          'LinksTitle': ['REST API: Endpoint Dictionary'],
          'Links': ['{{site.baseurl}}/api/home'],
          'SelectOption' : {
            'Errors' : {
              'ShowSubmit': true,
              'LinksTitle': ['API Errors and Responses'],
              'Links' : ['{{site.baseurl}}/api/errors/']
            },
            'Importing Data' : {
              'ShowSubmit': true,
              'LinksTitle': ['User Import', 'REST API: User Data Endpoints'],
              'Links' : ['{{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/','{{site.baseurl}}/api/endpoints/user_data']
            },
            'Exporting Data' : {
              'ShowSubmit': true,
              'LinksTitle': ['Exporting Braze Data','REST API: Export Endpoints', 'Export Frequently Asked Questions'],
              'Links' : ['{{site.baseurl}}/user_guide/data_and_analytics/export_braze_data','{{site.baseurl}}/api/endpoints/export','{{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/faqs/']
            },
            'API Campaigns' : {
              'ShowSubmit': true,
              'LinksTitle': ['API Campaign Overview','REST API: Send API-Triggered Campaign Endpoint','REST API: Schedule API-Triggered Campaign Endpoint'],
              'Links' : ['{{site.baseurl}}/api/api_campaigns/','{{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/','{{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/']
            },
            'Rate Limits' : {
              'ShowSubmit': true,
              'LinksTitle': ['API Rate Limits'],
               'Links' : ['{{site.baseurl}}/api/api_limits/']
             },
             'Other' : {
               'ShowSubmit': true,
               'LinksTitle': ['API Basics', 'API Connectivity Issues','Postman and Sample Requests'],
               'Links' : ['{{site.baseurl}}/api/basics/','{{site.baseurl}}/api/network_connectivity_issues','{{site.baseurl}}/api/postman_collection/']
             }
          }
        },
        'Email' : {
          'SelectDefault': 'Select a type...',
          'Label': 'My question is about... *',
          'LinksTitle': ['Email Best Practices','Email Frequently Asked Questions'],
          'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/','{{site.baseurl}}/user_guide/message_building_by_channel/email/faq/'],
          'SelectOption': {
            'Setup (whitelabeled IPs, DNS records)' : {
              'ShowSubmit': true,
              'LinksTitle': ['Email Onboarding Resources','Setting Up IPs and Domains','IP warming'],
              'Links' : ['{{site.baseurl}}/user_guide/onboarding_with_braze/email_setup','{{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/setting_up_ips_and_domains/','{{site.baseurl}}/user_guide/onboarding_with_braze/email_setup#ip-warming']
            },
            'Reporting and Analytics' : {
              'ShowSubmit': true,
              'LinksTitle': ['Email Reporting and Analytics'],
              'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/']
            },
            'Email Editors' : {
              'ShowSubmit': true,
              'LinksTitle': ['Email Drag-and Drop Editor', 'Email HTML Editor', 'Drag-And-Drop Editor Frequently Asked Questions'],
              'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop','{{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor','{{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/faq/']
            },
            'Deliverability' :{
              'ShowSubmit': true,
              'LinksTitle': ['Deliverability Pitfalls and Spam Traps','IP Warming','Braze Learning Course: Achieving High Email Deliverability'],
               'Links' : ['{{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/deliverability_pitfalls_and_spam_traps#deliverability-pitfalls-and-spam-traps','{{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming/#ip-warming','https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability']
            },
            'User Subscriptions' :{
              'ShowSubmit': true,
              'LinksTitle': ['Managing User Subscriptions'],
               'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/']
            },
            'Email Templates' : {
              'ShowSubmit': true,
              'LinksTitle': ['Creating an Email Template','Email Template Frequently Asked Questions'],
              'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template#step-3-customize-your-template','{{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/']
            },
            'Liquid' : {
              'ShowSubmit': true,
              'LinksTitle': ['Liquid Templating in Messages','Liquid Frequently Asked Questions','Braze Learning Course: Dynamic Personalization with Liquid'],
              'Links' : ['{{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid#about-liquid','{{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/faq/','https://learning.braze.com/dynamic-personalization-with-liquid']
            }
          }
        },
        'SMS and MMS' :{
          'SelectDefault': 'Select a type...',
          'Label': 'My question is about... *',
          'LinksTitle': ['SMS Best Practices','SMS Frequently Asked Questions', 'MMS Frequently Asked Questions', 'Braze Learning Course: SMS Fundamentals'],
          'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/sms/best_practices','{{site.baseurl}}/user_guide/message_building_by_channel/sms/faqs/','{{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/faqs/','https://learning.braze.com/sms-fundamentals'],
          'SelectOption': {
            'Setup' : {
              'ShowSubmit': true,
              'LinksTitle': ['SMS Onboarding Resources'],
              'Links' : ['{{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup']
            },
            'Subscription Groups' : {
              'ShowSubmit': true,
              'LinksTitle': ['SMS Subscription Groups'],
              'Links' : ['{{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup/sms_subscription_groups/']
            },
            'Short and Long Codes' : {
              'ShowSubmit': true,
              'LinksTitle': ['Short and Long Codes'],
              'Links' : ['{{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup/short_and_long_codes/']
            },
            'User Retargeting' : {
              'ShowSubmit': true,
              'LinksTitle': ['SMS User Retargeting'],
              'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/']
            }
          }
        },
        'WhatsApp' :{
          'SelectDefault': 'Select a type...',
          'Label': 'My question is about... *',
          'LinksTitle': ['WhatsApp Frequently Asked Questions'],
          'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/faqs/'],
          'SelectOption': {
            'Setup' : {
              'ShowSubmit': true,
              'LinksTitle': ['WhatsApp Setup Overview'],
              'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/']
            },
            'Subscription Groups' : {
              'ShowSubmit': true,
              'LinksTitle': ['WhatsApp User Subscription'],
              'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/']
            },
            'User Phone Numbers' : {
              'ShowSubmit': true,
              'LinksTitle': ['WhatsApp User Phone Numbers'],
              'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/']
            }
          }
        },
        'Campaigns and Canvas' :{
          'SelectDefault': 'Select a type...',
          'Label': 'My question is about... *',
          'LinksTitle': ['Campaign Frequently Asked Questions','Canvas Frequently Asked Questions'],
          'Links' : ['{{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/','{{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/'],
          'SelectOption': {
            'Messaging Personalization' : {
              'ShowSubmit': true,
              'LinksTitle': ['Personalization and Dynamic Content','Personalization Using Liquid Tags','Liquid Use Case Library','Connected Content'],
              'Links' : ['{{site.baseurl}}/user_guide/personalization_and_dynamic_content','{{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid','{{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases','{{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content']
            },
            'Targeting and Segmentation' : {
              'ShowSubmit': true,
              'LinksTitle': ['Segmentation','Segment Insights','Braze Learning Course: Segmentation',''],
              'Links' : ['{{site.baseurl}}/user_guide/engagement_tools/segments','{{site.baseurl}}/user_guide/engagement_tools/segments/segment_insights/','https://learning.braze.com/segmentation-course']
            },
            'Message Composition by Channel' : {
              'LinksTitle': ['Available Channels','Know Before You Send: Channels'],
              'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel','{{site.baseurl}}/help/help_articles/campaigns_and_canvas/know_before_send/'],
              'Label': 'Channel *',
              'SelectDefault': 'Select channel...',
              'SelectOption' : {
                'Email' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Creating an Email Campaign with the Drag-And-Drop Editor','Creating an Email Campaign with the HTML Editor'],
                  'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/','{{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/']
                },
                'Push' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Creating a Push Campaign','Braze Learning Course: Push'],
                  'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message#creating-a-push-message','https://learning.braze.com/messaging-channels-push']
                },
                'In-App Messages' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['In-App Message Drag-And-Drop Editor Campaign','In-App Message Traditional Editor Campaign','Braze Learning Course: In-App and In-Browser Messages'],
                  'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/','{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/','https://learning.braze.com/messaging-channels-in-app-in-browser']
                },
                'Content Cards' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Creating a Content Card Campaign','Braze Learning Course: Content Cards'],
                  'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/','https://learning.braze.com/messaging-channels-content-cards']
                },
                'Webhooks' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Creating a Webhook Campaign'],
                  'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/']
                },
                'SMS and MMS' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Create an SMS Campaign','Creating as MMS Campaign'],
                  'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/create/','{{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/create/']
                },
                'WhatsApp' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Create a WhatsApp Campaign'],
                  'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/']
                }
              }             
            }
          }
        },
        'Login Issues' :{
          'SelectDefault': 'Select a type...',
          'Label': 'My question is about... *',
          'LinksTitle': [''],
          'Links' : [''],
          'SelectOption': {
            'Password Error' : {
              'ShowSubmit': true,
              'LinksTitle': ['Locked Out of Account'],
              'Links' : ['{{site.baseurl}}/help/help_articles/account/locked_out/#password-error']
            },
            'Instance Error' : {
              'ShowSubmit': true,
              'LinksTitle': ['Instance Error'],
              'Links' : ['{{site.baseurl}}/help/help_articles/account/locked_out/#instance-error']
            },
            'SAML and Single Sign On' : {
              'ShowSubmit': true,
              'LinksTitle': ['SAML and Single Sign On'],
              'Links' : ['{{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on']
            },
            'Other' : {
              'ShowSubmit': true,
              'LinksTitle': ['Account Login Issues'],
              'Links' : ['{{site.baseurl}}/help/help_articles/account/locked_out/']
            }
          }
        },
        'Technology Partners' :{
          'SelectDefault': 'Select a type...',
          'Label': 'My question is about... *',
          'LinksTitle': [''],
          'Links' : [''],
          'SelectOption': {
            'Message Personalization' : {
              'ShowSubmit': true,
              'LinksTitle': ['Message Personalization Partners'],
              'Links' : ['{{site.baseurl}}/partners/message_personalization']
            },
            'Message Orchestration' : {
              'ShowSubmit': true,
              'LinksTitle': ['Message Orchestration Partners'],
              'Links' : ['{{site.baseurl}}/partners/message_orchestration']
            },
            'Data Infrastructure and Agility' : {
              'ShowSubmit': true,
              'LinksTitle': ['Data and Infrastructure Agility Partners'],
              'Links' : ['{{site.baseurl}}/partners/data_and_infrastructure_agility']
            },
            'Other' : {
              'ShowSubmit': true,
              'LinksTitle': ['Available Partner Integrations'],
              'Links' : ['{{site.baseurl}}/partners/home']
            }
          }
        },
        'System Status' :{
          'SelectDefault': 'Select a type...',
          'Label': 'My question is about... *',
          'LinksTitle': ['System Status'],
          'ShowSubmit': true,
          'Links' : ['https://braze.statuspage.io/'],
        },
        'Other' :{
          'SelectDefault': 'Select a type...',
          'Label': 'My question is about... *',
          'ShowSubmit': true,
          'LinksTitle': ['System Status','SDK Changelogs'],
          'Links' : ['https://braze.statuspage.io/','{{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs'],
        }
      }
    },
    'Strategy Assistance' : {
      'Label': '* Category',
      'SelectDefault': 'Select a category...',
      'LinksTitle': ['Campaign Ideas and Strategies','Canvas Ideas and Strategies','Building Accessible Messages in Braze','Braze Learning Course: Create Customer Journeys with Canvas Flow'],
      'Links': ['{{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/','{{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies','{{site.baseurl}}/help/accessibility/','https://learning.braze.com/create-customer-journeys-with-canvas-flow'],
      'SelectOption' : {
        'Tools and Use Cases' : {
          'ShowSubmit': true,
          'LinksTitle': ['Campaign Ideas and Strategies', 'Canvas Ideas and Strategies','Braze Learning Course: Customer Engagement Tools and Use Cases'],
          'Links':  ['{{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/','{{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies','https://learning.braze.com/braze-customer-engagement-tools-use-cases']
        },
        'Best Practices and Frequently Asked Questions' :{
          'ShowSubmit': true,
          'LinksTitle': ['Best Practices and Frequently Asked Questions'],
          'Links':  ['{{site.baseurl}}/help/faqs']
        },
        'Other' :{
          'ShowSubmit': true,
          'LinksTitle': [''],
          'Links':  ['']
        }
      }
    },

    'Account Administration' : {
      'Label': '* Category',
      'SelectDefault': 'Select a category...',
      'Links': [],
      'ReferenceText': 'Your account manager is a great resource for billing and contract related questions. ',
      'SelectOption' : {
        'Data Points' : {
          'ShowSubmit': true,
          'LinksTitle': ['Data Points'],
          'Links': ['{{site.baseurl}}/user_guide/data_and_analytics/data_points#data-points']
        },
        'Billing' : {
          'ShowSubmit': true,
          'LinksTitle': ['Billing'],
          'Links': ['{{site.baseurl}}/user_guide/administrative/app_settings/subscription_and_usage/']
        },
        'Other' :{
          'ShowSubmit': true,
          'ReferenceText': 'Your account manager is a great resource for billing and contract related questions. ',
          'LinksTitle': [''],
          'Links':  ['']
        }
      }
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
    'appgroupid': '00N0V000009G0N9',
    'companyid': '00NVP0000002y6X',
    'developerid': '00NVP0000004UvZ',
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
  function notEmpty(listarr){
    var empty = false;
    if (Array.isArray(listarr) && listarr.length){
      for (var i = 0; i < listarr.length; i++){
        if (listarr[i]){
          empty = true;
          i = listarr.length;
        }
      }
    }
    return empty;    
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
      if (notEmpty(linklist) && (linklist.length > 0)){
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
        if ('ShowSubmit' in curquestion) {
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
          resdiv.show();
        }
        else {
          resdiv.hide();
        }
      }
      else {
        resmsg.html('');
        if (notEmpty(linklist) ) {
          $('#ticket_submit_option').show();
        }
        else {
          resdiv.html('');
          resdiv.hide();
          if ('ShowSubmit' in curquestion) {
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
        }
        if (resstr) {
          resdiv.html(resstr);
          resdiv.show();
        }
        else {
          resdiv.hide();
        }
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
      $.each(subtype_options['SelectOption'],function(subtype, val)  {
        subtype_menu.append($('<option>',{value: subtype}).html(val.SelText || subtype));
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

  // default hide
  $('#subcategory_div').hide();

  if (type_selected && 'SelectOption' in type_options) {
    hide_page(3);

    // show only if subcategories exist
    if (Object.keys(type_options['SelectOption']).length > 0) {
      $('#subcategory_div').show();
    }

    if ('SelectDefault' in type_options) {
      type_menu.append($('<option>',{value: ''}).html(type_options['SelectDefault']));
    }
    else {
      type_menu.append($('<option>',{value: ''}).html('Select a subcategory...'));
    }

    $.each(type_options['SelectOption'],function(type, val)  {
      type_menu.append($('<option>',{value: type}).html(val.SelText || type));
    });
  }
  else {
    hide_page(2);
  }
  showlinks(type_options);
}


  function topic_change(e) {
    reset_page(1);

    $('#subcategory_div').hide(); 
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
      $.each(category_options['SelectOption'],function(category, val) {
        category_menu.append($('<option>',{value: category}).html( val.SelText || category));
      });
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
    $.each(ticket_options,function(topic, val)  {
      topic_menu.append($('<option>',{value: topic}).html(val.SelText || topic));
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
    var sels = mform.find('select');
    var user_name = $('#ticket_name').val();
    var user_email = $('#ticket_email').val();
    var user_ccemail = $('#ticket_ccemail').val();

    var user_subject = $('#ticket_subject').val();

    var user_issue = $('#ticket_issue').val();

    var sf_submit = new iframeform('https://webto.salesforce.com/servlet/servlet.WebToCase?encoding=UTF-8');

    sf_submit.addParameter('orgid','00Dd0000000e3l4');
    sf_submit.addParameter('retURL','https://braze.com');
    sf_submit.addParameter('name',user_name);
    sf_submit.addParameter('email',user_email);
    sf_submit.addParameter('subject',user_subject);
    if (user_ccemail) {
      sf_submit.addParameter('00N0V000008wX0Y',user_ccemail);
    }
    sf_submit.addBodyText('description',user_issue);
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

    var gs_submit = new iframeform('https://c9616da7-4322-4bed-9b51-917c1874fb31.trayapp.io/support_request');
    gs_submit.addParameter('Name', user_name);
    gs_submit.addParameter('Email', user_email);
    gs_submit.addParameter('Subject', user_subject);
    if (user_ccemail) {
      gs_submit.addParameter('CC_Email',user_ccemail);
    }
    gs_submit.addBodyText('Question', user_issue);
    var gs_mapping = {
      "00N0V000009G0MG" : "Topic", // Topic
      "00N0V000009G0MB" : "Category",  // Category
      "00N0V000009G0ML" : "Subcategory", // Subcategory
      "00N0V000009G0MQ" : "Type", // Type
      "priority" : "Priority", // Priority
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
    $.each(hiddenlist, function(k,v){
      if ($.urlParam(k) ){
        gs_submit.addParameter(v,$.urlParam(k));
      };
    });
    gs_submit.send();

    $('#ticket_mainform').hide();

    $('#ticket_thankyou').fadeIn("slow");
    $('#ticket_thankyou_msg').html('<h3>Thanks for your submission!</h3>A member of our Support team will respond to your ticket soon.<br />If you did not get a confirmation email, check your browser\'s addon, content/privacy setting and email spam folder.<br />Otherwise, contact your success manager (or email us at <a href="mailto:support@braze.com">support@braze.com</a>) to make sure your ticket has been submitted.');
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


const suggestionsBox = document.getElementById('suggestionsBox');
const articlesDiv = document.getElementById('articles');
const articlesList = document.getElementById('articles-list');
const formContainer = document.querySelector(".form-container");
const formContainer1 = document.querySelector(".form-container1");

const langSelect = document.getElementById('lang_select');
console.log("language ==>", langSelect);

let selectedLanguage = 'en'; 

const languageMap = {
  'en': 'English',
  'de': 'German',
  'es': 'Spanish',
  'fr': 'French',
  'ja': 'Japanese',
  'ko': 'Korean',
  'pt-br': 'Portuguese'
};

langSelect.addEventListener('change', (e) => {
  const langCode = e.target.value;
  selectedLanguage = langCode; 
  console.log('Language changed to:', langCode, '(', languageMap[langCode] || 'English', ')');

  if (window.currentSubject && window.currentSid) {
    getSearchResultByPost(window.currentSubject, window.currentSid, selectedLanguage);
  }
});

async function getSearchResultByPost(subject, sid , language) {
  const langCode = language || langSelect.value || 'en'; 
  console.log('Resolved language code:', langCode);
    const payload = {
        langAttr: "en",
        react: 1,
        isRecommendationsWidget: false,
        searchString: subject,
        from: 0,
        sortby: "_score",
        orderBy: "desc",
        pageNo: 1,
        aggregations: [
        {
          type: "language",
          filter: [langCode] 
        }
      ],
        clonedAggregations: [],
        uid: "63590d8d-65fd-11f0-ada3-0242ac120007",
        resultsPerPage: 10,
        exactPhrase: "",
        withOneOrMore: "",
        withoutTheWords: "",
        pageSize: 10,
        sid: sid,
        language: "en",
        mergeSources: false,
        versionResults: false,
        suCaseCreate: false,
        visitedtitle: "",
        paginationClicked: false,
        email: "",
        storeContext: true,
        searchUid: "a13d1e1d-31d8-4208-bed2-6993ab758b0c",
        accessToken: "9ad5ad4164aea64521fd3c00a19b76c8",
        getAutoTunedResult: true,
        getSimilarSearches: true,
        smartFacets: false
    };

    try {
        const response = await fetch("https://bz072508p.searchunify.com/search/searchResultByPost", {
            method: "POST",
            headers: {
                "accept": "*/*",
                "content-type": "application/json",
                "origin": "https://bz072508p.searchunify.com",
                "referer": "https://bz072508p.searchunify.com"
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) throw new Error(`Search API error: ${response.status}`);
        const data = await response.json();
        const results = data.result?.hits || data.hits || data.results || [];
        console.log('resss==>', results);

        return {
            llmContextId: data.llmContextId || data.context?.llmContextId || data.response?.llmContextId || "fallback-llm-context",
            results: results
        };

    } catch (err) {
        console.error("Error fetching searchResultByPost:", err);
        return { llmContextId: "fallback-llm-context", results: [] };
    }
}

document.getElementById('toStep2').addEventListener('click', async function () {
    const subject = document.getElementById('subject').value.trim();
    const description = document.getElementById('description').value.trim();
    if (!subject || !description) {
        alert('Please fill in all required fields');
        return;
    }

    step1.style.display = 'none';
    step2.style.display = 'block';
    steps[1].classList.add('active');
    articlesDiv.style.display = 'none';
    articlesList.innerHTML = '';
    document.querySelector('.gpt-heading').textContent = subject;
    const susResponse = await getSearchResultByPost(subject, sid);
    const llmContextId = susResponse.llmContextId;
    const results = susResponse.results;

    // --- Build a map of article metadata for hover tooltip ---
    const articleMetaMap = {};
    results.forEach(result => {
        const url = result.href || result.Id || "";
        articleMetaMap[url] = {
            title: result.highlight?.TitleToDisplay?.[0] || result.highlight?.TitleToDisplayString?.[0] || result.objLabel || "Untitled",
            summary: result.highlight?.SummaryToDisplay?.[0] ||
                     (result.autosuggestData?.find(d => d.key === "Summary")?.value?.[0]) ||
                     "No summary available"
        };
    });

    // --- Streaming / GPT Suggestions ---
    try {
        const requestBody = {
            query: subject,
            streaming: true,
            llm: true,
            separator: "$___$__$_$",
            searchBody: {
                react: 1,
                searchString: subject,
                uid: "63590d8d-65fd-11f0-ada3-0242ac120007",
                language: "en",
                searchUid: "22d6676b-80b1-4145-af19-6a422417e5d0",
                accessToken: "9ad5ad4164aea64521fd3c00a19b76c8",
                getAutoTunedResult: true,
                getSimilarSearches: true,
                smartFacets: false,
                showMoreSummary: false,
                minSummaryLength: 100,
                showContentTag: true,
                "sid-session": sid,
                "taid-device": taid
            },
            llmContextId: llmContextId
        };

        const response = await fetch("https://bz072508p.searchunify.com/mlService/su-gpt", {
            method: "POST",
            headers: {
                "accept": "*/*",
                "content-type": "application/json",
                "origin": "https://d3afgxkm1vz2tp.cloudfront.net",
                "referer": "https://d3afgxkm1vz2tp.cloudfront.net/",
                "search-client-type": "6",
                "search-id": "22d6676b-80b1-4145-af19-6a422417e5d0",
                "sid-session": sid,
                "taid-device": taid,
                "token": "9ad5ad4164aea64521fd3c00a19b76c8",
                "uid": "63590d8d-65fd-11f0-ada3-0242ac120007"
            },
            body: JSON.stringify(requestBody)
        });

        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);

        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let fullResponse = '';
        let articles = [];
        let articlesCollected = false;

        let partialAccumulator = '';

        while (true) {
          const { done, value } = await reader.read();
          if (done) break;

          const chunk = decoder.decode(value, { stream: true });
          const chunkParts = chunk.split('$___$__$_$');

          for (const part of chunkParts) {
            if (!part.trim()) continue;

            let jsonString = part;
            try {
              const validJson = partialAccumulator + jsonString;
              const data = JSON.parse(validJson);

              partialAccumulator = '';

              if (data.data?.choices?.[0]?.delta?.content) {
                fullResponse += data.data.choices[0].delta.content;
                suggestionsBox.innerHTML = fullResponse;
                document.querySelector('.flex-display').style.display = 'block';
                document.querySelector('.gpt-text1').style.display = 'block';
                document.querySelector('.gpt-text').style.display = 'none';
              }

              if (!articlesCollected && data.data?.articles) {
                const uniqueUrls = new Set(articles.map(a => a.href));
                for (const article of data.data.articles) {
                  if (!uniqueUrls.has(article.href)) {
                    articles.push(article);
                    uniqueUrls.add(article.href);
                  }
                }

                if (articles.length > 0) {
                  articlesList.innerHTML = articles.map(article =>
                    `<div class="article">
                      <a href="${article.href.split('_doc_doc_').pop()}" target="_blank">${article.title}</a>
                    </div>`
                  ).join('');
                  articlesDiv.style.display = 'block';
                }
                articlesCollected = true;
              }

              if (data.data?.no_answer?.length && fullResponse === '') {
                fullResponse = `<p>${data.data.no_answer[0]}</p>`;
                suggestionsBox.innerHTML = fullResponse;
              }
            } catch (e) {
              partialAccumulator += jsonString;
            }
          }
        }

        if (fullResponse === '' && articles.length > 0) {
            suggestionsBox.innerHTML = "<p>Here are some articles that might help:</p>";
        } else if (fullResponse === '') {
            suggestionsBox.innerHTML = "<p>No suggestions found.</p>";
        }

        // --- Citation hover tooltip ---
        const trackedCitations = new Set();
        document.querySelectorAll('.su_citation').forEach(button => {
            button.addEventListener('mouseenter', function () {
                const url = this.getAttribute('data-url')?.split('_doc_doc_').pop() || '';
                const meta = articleMetaMap[url];
                if (meta) {
                    let tooltip = document.createElement('div');
                    tooltip.className = 'su-tooltip';
                    tooltip.innerHTML = `<strong>${meta.title}</strong><small>${meta.summary}</small>`;
                    document.body.appendChild(tooltip);

                    const rect = this.getBoundingClientRect();
                    tooltip.style.position = 'absolute';
                    tooltip.style.top = `${rect.bottom + window.scrollY + 5}px`;
                    tooltip.style.left = `${rect.left + window.scrollX}px`;
                    tooltip.style.zIndex = 10000;

                    this._tooltip = tooltip;
                }
            });

            button.addEventListener('mouseleave', function () {
                if (this._tooltip) {
                    this._tooltip.remove();
                    delete this._tooltip;
                }
            });

            button.addEventListener('click', function () {
                const url = this.getAttribute('data-url')?.split('_doc_doc_').pop() || '';
                citationClicked = true;

                 if (!window.searchEventSent) {
                    const searchPayload = {
                      event: "search",
                      id: crypto.randomUUID(),
                      searchString: subject,
                      result_count: 0,
                      page_no: 1,
                      uid: "63590d8d-65fd-11f0-ada3-0242ac120007",
                      filter: {},
                      sid_session: sid || "",
                      taid_device: taid || "",
                      analyticsId: window._gza_analytics_id || crypto.randomUUID(),
                      referrer: document.referrer || "",
                      url: window.location.href
                    };

                    try {
                      navigator.sendBeacon(
                        "https://bz072508p.searchunify.com/analytics/suanlytics.png",
                        new Blob([JSON.stringify(searchPayload)], { type: "application/json" })
                      );
                      console.log("[Analytics] Search event sent on citation click");
                      window.searchEventSent = true; 
                    } catch (err) {
                      console.error("[Analytics] Error sending search event:", err);
                    }
                  }

                // Conversion analytics (once per citation)
                if (!trackedCitations.has(url)) {
                    const citationPayload = {
                        event: "conversion",
                        id: crypto.randomUUID(),
                        convUrl: url,
                        convSub: articleMetaMap[url]?.title
                        ? articleMetaMap[url].title.replace(/<[^>]+>/g, '').trim()
                        : '',

                        index: "1_12_doc",
                        type: "doc",
                        relevance_score: "7.0017533",
                        searchString: subject,
                        rank: 53510,
                        analyticsId: window._gza_analytics_id || crypto.randomUUID(),
                        url: window.location.href,
                        referrer: document.referrer,
                        uid: "63590d8d-65fd-11f0-ada3-0242ac120007",
                        sid_session: sid || "",
                        taid_device: taid || ""
                    };

                    try {
                        const data = JSON.stringify(citationPayload);
                        const sent = navigator.sendBeacon(
                            'https://bz072508p.searchunify.com/analytics/suanlytics.png',
                            new Blob([data], { type: 'application/json' })
                        );
                        if (!sent) {
                            fetch('https://bz072508p.searchunify.com/analytics/suanlytics.png', {
                                method: 'POST',
                                headers: { 'Content-Type': 'application/json' },
                                body: data
                            }).catch(console.error);
                        }
                    } catch (err) {
                        console.error('[Analytics] Error sending conversion payload', err);
                    }

                    trackedCitations.add(url);
                }

                setTimeout(() => window.open(url, '_blank'), 200);
            });
        });

    } catch (err) {
        suggestionsBox.innerHTML = `<p>Error: ${err.message}</p>`;
        console.error(err);
    }
});


    // Back to Step 1
    document.getElementById('backToStep1').addEventListener('click', function () {
        step2.style.display = 'none';
        step1.style.display = 'block';
        steps.forEach(s => s.classList.remove('active'));
        steps[0].classList.add('active');
        document.getElementById('suggestionsBox').innerHTML = "";
        window.searchEventSent = false;
    });
    
// Optional: Add a back button to return to the 3-step form
function addBackButton() {
    const backButton = document.createElement('button');
    backButton.textContent = 'Back to Suggestions';
    backButton.className = 'submit-btn';
    backButton.style.backgroundColor = 'grey';
    backButton.style.marginTop = '20px';
    backButton.onclick = function() {
        document.querySelector('.form-container1').style.display = 'none';
        document.querySelector('.form-container').style.display = 'block';
    };
    
    // Add the back button to the support form
    const ticketMainForm = document.getElementById('ticket_mainform');
    if (ticketMainForm) {
        ticketMainForm.appendChild(backButton);
    }
}


document.addEventListener('DOMContentLoaded', function() {
    addBackButton();
});


});
function initCaseForm() {
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
        return null;
    }

    function createNewSid() {
        return Date.now().toString() + Math.floor(1000 + Math.random() * 9000);
    }

    function sendSearchEvent(searchString, sid) {
        const searchPayload = {
            event: "search",
            id: crypto.randomUUID(),
            searchString: searchString,
            result_count: 0,
            page_no: 1,
            uid: "63590d8d-65fd-11f0-ada3-0242ac120007",
            filter: {},
            sid_session: sid,
            taid_device: taid || "",
            analyticsId: window._gza_analytics_id || crypto.randomUUID(),
            referrer: document.referrer || "",
            url: window.location.href
        };

        fetch("https://bz072508p.searchunify.com/analytics/suanlytics.png", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(searchPayload)
        })
        .catch(err => console.error("API Error (search):", err));
    }



    document.getElementById('toStep3').addEventListener('click', function () {
        document.querySelector(".form-container").classList.add("hidden");
        document.querySelector(".form-container1").style.display = "block";
        steps[2].classList.add('active'); 
        document.getElementById('ticket_subject').value = document.getElementById('subject').value;
        document.getElementById('ticket_issue').value = document.getElementById('description').value;
        step2.style.display = 'none';
        step3.style.display = 'block';

        document.querySelector(".svg-dot").classList.add("active");

        //  Submit Case Created Event
        document.getElementById('ticket_form').addEventListener('submit', function(e) {
            e.preventDefault(); 

            const subject = document.getElementById('ticket_subject').value;
            const caseId = "CASE-" + Date.now() + "-" + Math.floor(Math.random() * 1000);
            const caseNumber = Math.floor(100000 + Math.random() * 900000);
            const prioritySelect = document.getElementById('ticket_priority');
            const issueSeverity = prioritySelect.options[prioritySelect.selectedIndex].text;

            let sid = getCookie("_gz_sid");
            if (!sid) {
                sid = createNewSid();
                document.cookie = `_gz_sid=${sid}; path=/; SameSite=None; Secure`;
                sendSearchEvent(subject, sid); 
            }

            if (!citationClicked) {
            const subject = document.getElementById('subject').value;
           sendSearchEvent(subject, sid);
           }

            fetch('https://bz072508p.searchunify.com/analytics/suanlytics.png', {
                method: 'POST',
                headers: {
                    'content-type': 'application/json; charset=UTF-8',
                },
                body: JSON.stringify({
                    "subject": subject,
                    "uid": "63590d8d-65fd-11f0-ada3-0242ac120007",
                    "event": "caseCreated",
                    "caseId": caseId,         
                    "caseNumber": caseNumber,
                    "Issue_Severity__c": issueSeverity,
                    "isFreshSearch": !citationClicked,
                    "searchUid": "76a357a5-3804-449f-aa1e-211ed865a48b",
                    "referrer": document.referrer || "",
                    "e": "caseCreated",
                    "t": "Contact Us | What can we help you with today? | Bluebeam Technical",
                    "r": 60691,
                    "sid_session": sid, 
                    "taid_device": taid || "",
                    "internal": ""
                })
            })
            .catch(error => console.error("API Error (caseCreated):", error));
        });
    });
}

initCaseForm();


</script>