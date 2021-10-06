import xapi from 'xapi';

const URL = 'IP_OR_URL_TO_THE_PAGE_API_ENDPOINT' + '/api';
console.log("Macros for quick call page");
const payload = 'data'
// CHANGE the API_Key, this one is for example
const API_Key = 'a2n619bc-f49c-4330-bd39-56n73041c509'

let isInCall = false;

xapi.Status.SystemUnit.State.NumberOfActiveCalls.on(async (callCount) => {
isInCall = callCount > 0;
});

setInterval(function(){ 
xapi.command('HttpClient Post', { 
    Header: ["Content-Type: application/json", "X-API-Key: " + API_Key], 
    Url: URL,
    ResultBody: 'plaintext'
  }, 
    payload)
  .then((result) => {
    console.log("Status Code:" + result.StatusCode)

    const resp = String(result.Body).replace(/(\r\n|\n|\r)/gm, "")
      if (!isInCall && resp.replace(/\"/g, "") != 'False') { 
        console.log('Calling...')
      xapi.command('Dial', { Number:  resp.replace(/\"/g, "")});
    }
  })
  .catch((err) => {
      console.log("failed: " + err.message)
  });
}, 9000);
