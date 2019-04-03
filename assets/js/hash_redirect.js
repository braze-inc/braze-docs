
var validurls = (typeof validurls === "undefined")  ? {} : validurls;

(function(){


  var urlpath = removeleadingslash(window.location.pathname);

  //lower case name => path name
  function removeleadingslash(str){
    var rstr = str;
    if (rstr.slice(-1) === "/") {
      rstr = rstr.slice(0, -1);
    }
    return rstr;
  }


  function redirecturl(ky,uh,redirect) {
    var val_urls = validurls[ky];
    var hashes = val_urls.split('#');
    var returl = hashes[0] + redirect;
    if (hashes[1]) {
      returl += '#' + hashes[1];
    }
    else if (uh ) {
      returl += '#' + uh;
    }
    return returl;
  }
  var urlhash = window.location.hash;
  var urlsearch = window.location.search;

  if (window.location.href.indexOf('redirected=true') == -1) {
    if (urlhash) {
      urlhash = urlhash.replace('#','')
      var redirected  = '?redirected=true' ;
      if (urlsearch.indexOf('?') > -1 ) {
        redirected = urlsearch + '&redirected=true';
      }
      if (validurls[urlhash] ) {
        window.location  =  redirecturl(urlhash,urlhash,redirected);
      }
      else {

      }
    }
  }
}  )();
