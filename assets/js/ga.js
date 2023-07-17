import * as params from '@params';


analyticsID = params["googleAnalyticsID"];

// If the GA ID was not defined in the hugo config, it would be set as null
// Therefore we should skip execution in those cases
if (analyticsID !== null) {
    console.log(`GA enabled for ID ${analyticsID}`);

    const gaScript = document.createElement("script");
    gaScript.src = `https://www.googletagmanager.com/gtag/js?id=${analyticsID}`;
    gaScript.async = true;
    document.head.appendChild(gaScript);

    window.dataLayer = window.dataLayer || [];
    function gtag() {
        dataLayer.push(arguments);
    }
    gtag('js', new Date());
    gtag('config', analyticsID);
} else {
    console.log("Google Analytics enabled, but ID was never defined.")
}
