2025-10-29 09:27:51 [INFO] 🚀 Starting Bulk Unsubscribe Report Generator...

2025-10-29 09:27:51 [INFO] [FETCH] 📄 Fetching page 1...
2025-10-29 09:27:51 [INFO] [AUTH] Requesting new access token...
2025-10-29 09:28:02 [WARNING] Retrying (Retry(total=4, connect=4, read=5, redirect=None, status=None)) after connection broken by 'NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x00000270CD7190A0>: Failed to resolve 'ocp.optum.com' ([Errno 11001] getaddrinfo failed)")': /oauth2/token
2025-10-29 09:28:17 [WARNING] Retrying (Retry(total=3, connect=3, read=5, redirect=None, status=None)) after connection broken by 'NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x00000270CF4138F0>: Failed to resolve 'ocp.optum.com' ([Errno 11001] getaddrinfo failed)")': /oauth2/token
2025-10-29 09:28:36 [WARNING] Retrying (Retry(total=2, connect=2, read=5, redirect=None, status=None)) after connection broken by 'NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x00000270CF4139B0>: Failed to resolve 'ocp.optum.com' ([Errno 11001] getaddrinfo failed)")': /oauth2/token
2025-10-29 09:29:03 [WARNING] Retrying (Retry(total=1, connect=1, read=5, redirect=None, status=None)) after connection broken by 'NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x00000270CF413B00>: Failed to resolve 'ocp.optum.com' ([Errno 11001] getaddrinfo failed)")': /oauth2/token
2025-10-29 09:29:46 [WARNING] Retrying (Retry(total=0, connect=0, read=5, redirect=None, status=None)) after connection broken by 'NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x00000270CF413C50>: Failed to resolve 'ocp.optum.com' ([Errno 11001] getaddrinfo failed)")': /oauth2/token
Traceback (most recent call last):
  File "C:\Users\smarim18\AppData\Roaming\Python\Python312\site-packages\urllib3\connection.py", line 198, in _new_conn
    sock = connection.create_connection(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\smarim18\AppData\Roaming\Python\Python312\site-packages\urllib3\util\connection.py", line 60, in create_connection        
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python312\Lib\socket.py", line 976, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
socket.gaierror: [Errno 11001] getaddrinfo failed

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\smarim18\AppData\Roaming\Python\Python312\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    response = self._make_request(
               ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\smarim18\AppData\Roaming\Python\Python312\site-packages\urllib3\connectionpool.py", line 488, in _make_request
    raise new_e
  File "C:\Users\smarim18\AppData\Roaming\Python\Python312\site-packages\urllib3\connectionpool.py", line 464, in _make_request
    self._validate_conn(conn)
  File "C:\Users\smarim18\AppData\Roaming\Python\Python312\site-packages\urllib3\connectionpool.py", line 1093, in _validate_conn
    conn.connect()
  File "C:\Users\smarim18\AppData\Roaming\Python\Python312\site-packages\urllib3\connection.py", line 704, in connect
    self.sock = sock = self._new_conn()
                       ^^^^^^^^^^^^^^^^
  File "C:\Users\smarim18\AppData\Roaming\Python\Python312\site-packages\urllib3\connection.py", line 205, in _new_conn
    raise NameResolutionError(self.host, self, e) from e
urllib3.exceptions.NameResolutionError: <urllib3.connection.HTTPSConnection object at 0x00000270CF413DA0>: Failed to resolve 'ocp.optum.com' ([Errno 11001] getaddrinfo failed)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\smarim18\AppData\Roaming\Python\Python312\site-packages\requests\adapters.py", line 667, in send
    resp = conn.urlopen(
           ^^^^^^^^^^^^^
  File "C:\Users\smarim18\AppData\Roaming\Python\Python312\site-packages\urllib3\connectionpool.py", line 871, in urlopen
    return self.urlopen(
           ^^^^^^^^^^^^^
  File "C:\Users\smarim18\AppData\Roaming\Python\Python312\site-packages\urllib3\connectionpool.py", line 871, in urlopen
    return self.urlopen(
           ^^^^^^^^^^^^^
  File "C:\Users\smarim18\AppData\Roaming\Python\Python312\site-packages\urllib3\connectionpool.py", line 871, in urlopen
    return self.urlopen(
           ^^^^^^^^^^^^^
  [Previous line repeated 2 more times]
  File "C:\Users\smarim18\AppData\Roaming\Python\Python312\site-packages\urllib3\connectionpool.py", line 841, in urlopen
    retries = retries.increment(
              ^^^^^^^^^^^^^^^^^^
  File "C:\Users\smarim18\AppData\Roaming\Python\Python312\site-packages\urllib3\util\retry.py", line 519, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='ocp.optum.com', port=443): Max retries exceeded with url: /oauth2/token (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x00000270CF413DA0>: Failed to resolve 'ocp.optum.com' ([Errno 11001] getaddrinfo failed)"))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\smarim18\Documents\SMS_CAMPAIGN\UnSubscribes Report\Unsubscribers8.py", line 77, in renew_token
    response = session.post(self.auth_url, data=payload, timeout=20)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\smarim18\AppData\Roaming\Python\Python312\site-packages\requests\sessions.py", line 637, in post
    return self.request("POST", url, data=data, json=json, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\smarim18\AppData\Roaming\Python\Python312\site-packages\requests\sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\smarim18\AppData\Roaming\Python\Python312\site-packages\requests\sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\smarim18\AppData\Roaming\Python\Python312\site-packages\requests\adapters.py", line 700, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='ocp.optum.com', port=443): Max retries exceeded with url: /oauth2/token (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x00000270CF413DA0>: Failed to resolve 'ocp.optum.com' ([Errno 11001] getaddrinfo failed)"))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\smarim18\Documents\SMS_CAMPAIGN\UnSubscribes Report\Unsubscribers8.py", line 200, in <module>
    unsubscribed_data = fetcher.fetch_all_unsubscribed()
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\smarim18\Documents\SMS_CAMPAIGN\UnSubscribes Report\Unsubscribers8.py", line 120, in fetch_all_unsubscribed
    response = session.get(url, headers=self.token_service.get_headers(), timeout=30)
                                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\smarim18\Documents\SMS_CAMPAIGN\UnSubscribes Report\Unsubscribers8.py", line 90, in get_headers
    self.renew_token()
  File "C:\Users\smarim18\Documents\SMS_CAMPAIGN\UnSubscribes Report\Unsubscribers8.py", line 87, in renew_token
    raise Exception(f"[AUTH ERROR] Request failed: {e}")
Exception: [AUTH ERROR] Request failed: HTTPSConnectionPool(host='ocp.optum.com', port=443): Max retries exceeded with url: /oauth2/token (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x00000270CF413DA0>: Failed to resolve 'ocp.optum.com' ([Errno 11001] getaddrinfo failed)"))
