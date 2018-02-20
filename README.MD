# Altcoin System

buy sell altcoin system. written by yasuyuki toriumi.

## Architect

It will work on GAE (GoogleAppEngine).
Cron tasks are also working on it.

## Dependencies

- In `lib/` dir for GAE.
  - [https://github.com/bitbankinc/python-bitbankcc](https://github.com/bitbankinc/python-bitbankcc)
  - [https://github.com/requests/requests/tree/v2.3.0](https://github.com/requests/requests/tree/v2.3.0)
      using not latest version. because later versions from v2.3.0 cannot use for dev_server.py.
      `('Connection aborted.', error(13, 'Permission denied'))` this error message happened.
- Use built in by GAE. [built-in-libraries-27](https://cloud.google.com/appengine/docs/standard/python/tools/built-in-libraries-27)
  - [https://pypi.python.org/pypi/ujson](https://pypi.python.org/pypi/ujson)
  - [https://docs.python.org/dev/library/ssl.html](https://docs.python.org/dev/library/ssl.html)

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

## Ref

- [appengine_config.py](https://cloud.google.com/appengine/docs/standard/python/tools/appengineconfig?hl=ja)
- [hide secrets environment variables](https://groups.google.com/forum/#!topic/google-appengine/MnEjnYFUMkg)
- [app.yaml](https://cloud.google.com/appengine/docs/standard/python/config/appref)
- [Can Python Requests library be used on Google App Engine?](https://stackoverflow.com/questions/9604799/can-python-requests-library-be-used-on-google-app-engine/28544823)
- []()
- []()
- []()
- []()
