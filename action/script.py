import httpx
import sys
import os

server = sys.argv[1]
file = sys.argv[2]
ssl_verify = sys.argv[3]

with httpx.Client(base_url=server, verify=bool(ssl_verify)) as c:
    f = c.post(url=os.environ["GITHUB_SHA"], files=open(file))
    json = f.json()
    with open("GITHUB_OUTPUT", "a") as fh:
        f_name = server+json['file']
        print(f"fileloc={f_name}", file=fh)
