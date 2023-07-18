(() => {
  // ns-params:@params
  var googleAnalyticsID = "G-6W31KMZWGE";

  // <stdin>
  analyticsID = googleAnalyticsID;
  if (analyticsID !== null) {
    let gtag = function() {
      dataLayer.push(arguments);
    };
    console.log(`GA enabled for ID ${analyticsID}`);
    const gaScript = document.createElement("script");
    gaScript.src = `https://www.googletagmanager.com/gtag/js?id=${analyticsID}`;
    gaScript.async = true;
    document.head.appendChild(gaScript);
    window.dataLayer = window.dataLayer || [];
    gtag("js", new Date());
    gtag("config", analyticsID);
  } else {
    console.log("Google Analytics enabled, but ID was never defined.");
  }
})();
