---
nav_title: Documentation Request
permalink: "/request/"
hide_nav: true
layout: basic
hide_toc: true
---

  <style type="text/css">
  body {
      line-height: 2;
      background-color: #fff;
      font-weight: 400;
      font-size: 15px;
      font-family: Sailec W00 Regular,Arial,sans-serif;
      font-style: normal;
      color: #212123;
  }
  #main-container {
    margin-top: 20px;
  }
  #main-container label {
    font-weight: bold;
    font-size: 18px;
  }

  .container {
    margin-top: 40px;
  }


  .popover{
    max-width: 95%;
    min-width: 350px;
  }


  .container-fluid {
    max-width: 820px;
  }
  .header {
    margin-top: 20px;
    margin-left: 5%;
  }
  .header .navbar-brand img {
      max-width: none;
      width: 112px;
      height: 51px;
  }


  .gradient-line {
      background: linear-gradient(30deg,#3accdd,#f7918e 64%,#ff9349 90%);
      height: 2px;
      width: 50%;
      margin-bottom:20px;
  }

  a {
    color: #3bcddf;
  }
  a:hover {
    color: #333;
  }


    @media (min-width: 1400px) {
      .container {
        max-width: 1340px;
      }
    }

    .h1, h1  {
      font-size: 44px;
    }

    .h2, h2 {
      font-size: 20px;
    }

    #ticket_footer {
      margin-left: auto;
      margin-right: auto;
      border-top: 1px solid #c9c9c9;
      text-align: center;
      font-size: 10px;
      padding-top: 10px;
    }

    #ticket_footer a {
      text-decoration: none;
      color: #212123;
    }
    #ticket_footer li {
      display: inline;
      margin: 10px;

    }
    .btn, input[type=submit] {
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
      .btn, input[type=submit] {
        padding: 1.64286rem 3.92857rem
      }
    }

    .btn:before, input[type=submit]:before {
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

    .btn:focus, .btn:hover, input[type=submit]:focus, input[type=submit]:hover {
      color: #fff
    }

    .btn:focus:before, .btn:hover:before, input[type=submit]:focus:before, input[type=submit]:hover:before {
      transform: translateZ(0)
    }

    .btn-black, input[type=submit] {
      color: #fff
    }

    .btn-black:before, input[type=submit]:before {
      background-color: #fff
    }

    .btn-black:after, input[type=submit]:after {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      z-index: -2;
      height: 100%;
      width: 100%;
      background-color: #212123
    }

    .btn-black:focus, .btn-black:hover, input[type=submit]:focus, input[type=submit]:hover {
      color: #212123
    }

    .btn-small {
      padding: 1.07143rem 1.78571rem !important
    }
  </style>
  <script type="text/javascript">
    ! function(e, i) {
      if ("function" == typeof define && define.amd) define(["exports", "jquery"], function(e, r) {
        return i(e, r)
      });
      else if ("undefined" != typeof exports) {
        var r = require("jquery");
        i(exports, r)
      } else i(e, e.jQuery || e.Zepto || e.ender || e.$)
    }(this, function(e, i) {
      function r(e, r) {
        function n(e, i, r) {
          return e[i] = r, e
        }

        function a(e, i) {
          for (var r, a = e.match(t.key); void 0 !== (r = a.pop());)
            if (t.push.test(r)) {
              var u = s(e.replace(/\[\]$/, ""));
              i = n([], u, i)
            } else t.fixed.test(r) ? i = n([], r, i) : t.named.test(r) && (i = n({}, r, i));
          return i
        }

        function s(e) {
          return void 0 === h[e] && (h[e] = 0), h[e]++
        }

        function u(e) {
          switch (i('[name="' + e.name + '"]', r).attr("type")) {
            case "checkbox":
              return "on" === e.value ? !0 : e.value;
            default:
              return e.value
          }
        }

        function f(i) {
          if (!t.validate.test(i.name)) return this;
          var r = a(i.name, u(i));
          return l = e.extend(!0, l, r), this
        }

        function d(i) {
          if (!e.isArray(i)) throw new Error("formSerializer.addPairs expects an Array");
          for (var r = 0, t = i.length; t > r; r++) this.addPair(i[r]);
          return this
        }

        function o() {
          return l
        }

        function c() {
          return JSON.stringify(o())
        }
        var l = {},
          h = {};
        this.addPair = f, this.addPairs = d, this.serialize = o, this.serializeJSON = c
      }
      var t = {
        validate: /^[a-z_][a-z0-9_]*(?:\[(?:\d*|[a-z0-9_]+)\])*$/i,
        key: /[a-z0-9_]+|(?=\[\])/gi,
        push: /^$/,
        fixed: /^\d+$/,
        named: /^[a-z0-9_]+$/i
      };
      return r.patterns = t, r.serializeObject = function() {
        return new r(i, this).addPairs(this.serializeArray()).serialize()
      }, r.serializeJSON = function() {
        return new r(i, this).addPairs(this.serializeArray()).serializeJSON()
      }, "undefined" != typeof i.fn && (i.fn.serializeObject = r.serializeObject, i.fn.serializeJSON = r.serializeJSON), e.FormSerializer = r, r
    });
  </script>
  <script type="text/javascript">
    $(document).ready(function() {
      $('#doc_form').submit(function(e) {
        var mform = $(this);
        e.preventDefault();
        $('#doc_div').hide();
        var url = 'https://script.google.com/macros/s/AKfycbzDu2Q-VK18apU8-UAMEQFGteT-MuD5b648QWiE-MvmN99XfyBm/exec';
        //console.log(mform.serializeObject());
        //console.log(mform.serialize());

        var jqxhr = $.ajax({
          url: url,
          method: "GET",
          dataType: "json",
          data: mform.serializeObject()
        }).done(function() {
          $('#doc_thankyou').fadeIn("slow");
          $('#doc_thankyou_msg').html('<h3>Thanks for your submission!</h3> Somebody should reach out to you shortly.');

        });
      });
    });
  </script>




<div class="container-fluid" id="main-container">

      <div id="doc_div">
        <form id="doc_form">
          <div class="row">
            <div class="col">
              <h1 class="h1">Request Documentation Change</h1>
              <p class="subhead">Submit a change request here.</p>
                  <div class="gradient-line"></div>
            </div>
          </div>
          <div class="row">
            <div class="col">
    
    
              <div class="form-group" id="doc_name_div">
                <label for="doc_name" id="doc_name_label">    * What's your name?</label>
                <input type="text" name="Name" id="doc_name" maxlength="80" required="required" value="" placeholder="Enter your name" class="form-control" />
              </div>
              <div class="form-group">
    
                <label for="doc_email" id="doc_email_label"> * Email Address</label>
                <div class="input-group">
                  <div class="input-group-prepend">
                    <span class="input-group-text" id="basic-addon1">@</span>
                  </div>
                  <input type="email" class="form-control" id="doc_email" maxlength="80" name="Email" placeholder="Enter email" required="required" value="" /></div>
              </div>
              <div class="form-group" id="doc_request_div">
                <label for="doc_request" id="doc_request_label">    * What needs to be changed?</label>
                <input type="text" name="Request_Subject" id="doc_request" maxlength="180" required="required" value="" placeholder="Enter your request" class="form-control" />
              </div>
              <div class="form-group" id="doc_pm_div">
              <div class="form-check">
                <input class="form-check-input" type="checkbox" value="Y" id="doc_is_pm" name="Request_Is_PM">
                <label class="form-check-label" for="doc_is_pm">
                Are you a Product Manager?
              </label>
              </div>
              </div>
    
              <div class="form-group" id="doc_urgent_div">
              <div class="form-check">
                <input class="form-check-input" type="checkbox" value="Y" id="doc_urgent" name="Request_Urgent">
                <label class="form-check-label" for="doc_urgent">
                Is this request Urgent?
              </label>
              </div>
              </div>
    
    
    
              <div class="form-group">
    
                <label for="doc_description" id="doc_description_label">   * Please describe your request. </label>
    
                <textarea name="Description" class="form-control" id="doc_description" data-toggle="popover" data-trigger="focus" data-placement="top" data-content="What needs to be done for you to consider this request complete? Be as descriptive as possible.&#10;&#10;Link to as many resources as necessary, including drive folders full of images. Include links to existing documentation that needs to be repaired as well as links that might need to be included in the documentation." placeholder="What needs to be done for you to consider this request complete? Be as descriptive as possible.&#10;&#10;Link to as many resources as necessary, including drive folders full of images. Include links to existing documentation that needs to be repaired as well as links that might need to be included in the documentation."
                  rows="7"></textarea>
              </div>
    
              <div class="form-group">
    
                <label for="doc_snippet" id="doc_snippet_label">   * Please insert relevant code snippets with context.</label>
    
                <textarea name="Snippet" class="form-control" id="doc_snippet" data-toggle="popover" data-trigger="focus" data-placement="top" data-content="This is useful if you're a developer. Make sure it's clear which language this is written in, too. " placeholder="This is useful if you're a developer. Make sure it's clear which language this is written in, too. "
                  rows="7"></textarea>
              </div>
              <button type="submit" name="Submit Question" value="Submit" class="btn btn-black" id="ticket_submit_button" role="button"> Send </button>
    
            </div>
    
          </div>
        </form>
      </div>
    
    
      <div id="doc_thankyou" style="display:none;"><div class="row"><div class="col" id="doc_thankyou_msg"></div></div></div>
    
    </div>
<br /><br /><br />
