# Altcoin System

buy sell altcoin system. written by yasuyuki toriumi.

## Architect

It will work on GAE (GoogleAppEngine).
Cron tasks are also working on it.

## Services

### Cron

`/api/coin`: lauch main buyer logic.

### Emergency Stop

Go to [google cloud console](https://console.cloud.google.com/appengine/settings?project=sandbox-195516&hl=ja&serviceId=default&versionId=20180226t203723).
Click `アプリケーションを無効にする` button.

## Dependencies

- In `lib/` dir for GAE.
  - [https://github.com/bitbankinc/python-bitbankcc](https://github.com/bitbankinc/python-bitbankcc)
  - [https://github.com/requests/requests/tree/v2.3.0](https://github.com/requests/requests/tree/v2.3.0)  
    using not latest version. because later versions from v2.3.0 cannot use for dev_server.py.  
    `('Connection aborted.', error(13, 'Permission denied'))` this error message happened.  
  - [https://pypi.python.org/pypi/attrdict](https://pypi.python.org/pypi/attrdict)
- Use built in by GAE. ([built-in-libraries-27](https://cloud.google.com/appengine/docs/standard/python/tools/built-in-libraries-27))
  - [https://pypi.python.org/pypi/ujson](https://pypi.python.org/pypi/ujson)
  - [https://docs.python.org/dev/library/ssl.html](https://docs.python.org/dev/library/ssl.html)
  - [https://pypi.python.org/pypi/pytz](https://pypi.python.org/pypi/pytz)  

## Development

### Launch dev server for GAE.

```py
dev_appserver.py app.yaml
```

### Local URLs

- dev server  
  [http://localhost:8080/](http://localhost:8080/)
- api server  
  [http://localhost:55480/](http://localhost:55480/)
- admin server   
  [http://localhost:8000](http://localhost:8000)

## Deploy

- deploy app
  ```sh
  gcloud app deploy app.yaml
  ```
- deploy cron
  ```sh
  gcloud app deploy cron.yaml
  ```

## Refs

- [appengine_config.py](https://cloud.google.com/appengine/docs/standard/python/tools/appengineconfig?hl=ja)
- [hide secrets environment variables](https://groups.google.com/forum/#!topic/google-appengine/MnEjnYFUMkg)
- [app.yaml](https://cloud.google.com/appengine/docs/standard/python/config/appref)
- [Can Python Requests library be used on Google App Engine?](https://stackoverflow.com/questions/9604799/can-python-requests-library-be-used-on-google-app-engine/28544823)
- [how to restrict post request](https://cloud.google.com/appengine/docs/standard/python/config/appref#handlers_login)    
  You can add `login: admin` directive, for cron tasks, to restrict requested by normal access.
- [cron.yaml Reference](https://cloud.google.com/appengine/docs/standard/python/config/cronref)
- []()
- []()
