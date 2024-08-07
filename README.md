# Quick call page for Webex Devices

Simple app for Webex one tap to call (DEMO)

![Webex one tap to call](img/webex-one-tap-to-call.gif)

Web page and Macros for Webex Devices provide you interface to create a page with one click Dial. 

The solution allows you to create a helpful Directory with an extensive photo/name of the contact and call it with one click.

## Prerequisites

**Open web interface of your Webex device**

![](img/Desk_Pro_GUI.png)

Using Webex device GUI, you need to make the following changes. First, go to Setup -> Configurations In the left menu, choose HttpClient settings and change AllowInsecureHTTPS from False to True.

![](img/Webex_device_Settings.png)

OR Open terminal

```
ssh user@10.10.30.15
```
and run this
```
xConfiguration HttpClient Mode: On
```

Create Macros, copy and paste JS code from `macros.js` file
After deplou the app, edit this line
`const URL = 'IP_OR_URL_TO_THE_PAGE_API_ENDPOINT' + '/api';`

You can store your app in the same network that your Webex device or deploy it externally on [Heroku](https://signup.heroku.com/)

Clone the repo
```
git clone https://github.com/oborys/Quick-call-page-for-Webex-Devices.git

cd Quick-call-page-for-Webex-Devices
```

Paste related photos in `static/images`
The name should be `1.png`, `2.png` etc

Edit file `templates/script.html` if you want to add or remove the Directory photo

When the user clicks on a related photo page, call the `clickEvent` function and send as a parameter `id` (0,1,2...)

Then app send id in python function and write related SIP from the `SIPLIST` variable (file: `app.py`)

By default there you can find an SIP address that allows you to test the app.

For make visible in Webex Device Screen we need to add icon and link to external app (that we deploy in next steps). [Instructions here](https://github.com/oborys/Quick-call-page-for-Webex-Devices#create-web-app-in-your-webex-device-gui)


## Installation

**Deploy internal**
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt 
```
Run Flask
```
flask run
```

Open app [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

![](img/Quick-call-page.png)

**Or Deploy external**
In related folder
```
cd Quick-call-page-for-Webex-Devices
```

Delete local `.git` repo
```
rm -rf .git
```

Create [Heroku App](https://dashboard.heroku.com/apps)


```
heroku git:clone -a [Heroku_App_name]
```
Copy and paste a file from `Quick-call-page-for-Webex-Devices` to [`Heroku_App_name`] folder

```
cp -R * Heroku_App_name
```

```
cd webexicondial
```

```
curl https://cli-assets.heroku.com/install.sh | sh
```

```
heroku login
```

```
git add .
git commit -m "Add files"
git push heroku master
```

Open your Heroku app.

## Create Web App in your Webex device GUI

![](img/UI_Extensions_configuration.png)

add related URL in URL Field and upload it to the Webex device

![](img/Create_Web_App.png)

## Related Sandbox

[Webex Developer Sandbox](https://developer.webex.com/docs/developer-sandbox-guide)

[CE programmability for Webex Devices](https://devnetsandbox.cisco.com/RM/Diagram/Index/937bd886-3eed-45a2-afe0-8c48337e8bea?diagramType=Topology) [Deprecated]

Capabilities:
- Discover the admin interface from your laptops Web browser

- Open an ssh session to the Room Kit and enter t-shell commands: `xconfig`, `xstatus` and `xcommand`

- Invoke the device's xAPI via HTTP requests and Node.js scripts thanks to the `jsxapi` wrapper

### Useful link
- [HTTP request from Webex device](https://help.webex.com/en-US/article/nthg6le/Sending-HTTP-Requests-from-a-Board,-Room,-or-Desk-Device)

- [Webex devices macros sample](https://github.com/CiscoDevNet/roomdevices-macros-samples)

- [Deploying a Python Flask Example Application Using Heroku](https://realpython.com/flask-by-example-part-1-project-setup/)
