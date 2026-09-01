from client import EvidenceBackedProductComparisonClient

if __name__ == "__main__":
    result = EvidenceBackedProductComparisonClient().run([{"title":"Audience strategy","body":"creator campaign product discovery"}, {"title":"Budget plan","body":"compare audience reach"}], "creator audience")
    assert result["status"] == "ok"
    print("PASS", result)
