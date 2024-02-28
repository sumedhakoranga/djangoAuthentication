# Configuration for Google OAuth and Gmail API


To use this application, you must configure it with your Google OAuth and Gmail API credentials. This involves creating a credential.env file for the OAuth credentials and a credential.json file for the Gmail API credentials. Follow the steps below to set up these files:

**Setting up Google OAuth Credentials**

1. **Create a Project in Google Cloud Console**: Go to the [Google Cloud Console](https://console.cloud.google.com/) and create a new project or select an existing one.
2. **Enable OAuth Consent Screen**: Navigate to the OAuth consent screen under API & Services and set up the consent screen. This step is crucial for authenticating users.
3. **Create OAuth Credentials**: In the Credentials section, click "Create Credentials" and choose "OAuth client ID". Select the application type (e.g., Web application).
4. **Download OAuth Credentials**: Once the OAuth client ID is created, download the credentials JSON file. However, for the credential.env, you'll manually create the file and enter the `client_id` and `client_secret` as follows:

**Creating credential.env** 

1. Open a text editor and create a new file named credential.env.
2. Add the following lines, replacing YOUR_CLIENT_ID and YOUR_CLIENT_SECRET with the values from the Google OAuth credentials you just created:
  ```GOOGLE_CLIENT_ID=YOUR_CLIENT_ID```
  ```GOOGLE_CLIENT_SECRET=YOUR_CLIENT_SECRET```
3. Save credential.env in the root directory of the application.

**Setting up Gmail API Credentials**

1. Enable the Gmail API: In the Google Cloud Console, navigate to the "Library" section under "APIs & Services". Search for the Gmail API and enable it for your project.
2. Download the JSON Credentials: Typically, the same OAuth 2.0 credentials can be used. Make sure to download the credentials JSON file which contains the client_id, client_secret, and other necessary information.
3. Save the Credentials JSON File:
    - Rename the downloaded JSON file to credential.json.
    - Place credential.json in the root directory of your application.
