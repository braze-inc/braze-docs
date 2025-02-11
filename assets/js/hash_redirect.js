
var validurls = (typeof validurls === "undefined")  ? {} : validurls;

(function(){
  function redirecturl(ky,uh,redirect) {
    var val_urls = validurls[ky];
    if (site_language && (site_language != 'en')){
      if (!val_urls.match(/^\/docs\/(\w{2}|\w{2}\-\w{2})\//)) {
        val_urls = val_urls.replace(/^\/docs\//, `\/docs\/${site_language}\/`);
      }
    }

    var hashes = val_urls.split('#');
    var redirect_params = ((hashes[0].indexOf('?') > -1 ) ? '&' : '?') + redirect;
    var returl = hashes[0] + redirect_params;
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
  var redirected_count = parseInt(query_params.get('redirected'),10) || 0;
  if (!redirected_count) {
    if (urlhash) {
      redirected_count++;
      urlhash = urlhash.replace('#','')
      query_params.set('redirected',redirected_count );
      var redirected  = query_params.toString();
      if (validurls[urlhash] ) {
        window.location = redirecturl(urlhash,urlhash,redirected);
      }
      else {

      }
    }
  }
}  )();
