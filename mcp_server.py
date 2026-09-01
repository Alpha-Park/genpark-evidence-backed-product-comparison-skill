import json
import sys
from client import EvidenceBackedProductComparisonClient

if __name__ == "__main__":
    for line in sys.stdin:
        try:
            request=json.loads(line); response=EvidenceBackedProductComparisonClient().run(request.get("records",[]),request.get("query",""))
        except Exception as error:
            response={"status":"error","error":str(error)}
        print(json.dumps(response),flush=True)
