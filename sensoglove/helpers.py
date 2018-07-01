import json


def read_json_payload(s):
    data = s.recv(1024)
    data = data.decode().rstrip()
    try:
        pdata = json.loads(data)
        return pdata
    except json.decoder.JSONDecodeError:
        return None
