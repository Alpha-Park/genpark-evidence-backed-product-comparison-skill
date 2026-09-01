from typing import Any, Dict, List

class EvidenceBackedProductComparisonClient:
    def run(self, records: List[Dict[str, Any]], query: str) -> Dict[str, Any]:
        if not isinstance(records, list): raise ValueError("records must be a list")
        if not isinstance(query, str) or not query.strip(): raise ValueError("query must be non-empty")
        terms=set(query.lower().split()); ranked=[]
        for index, record in enumerate(records):
            if not isinstance(record, dict): continue
            text=" ".join(str(value) for value in record.values()).lower()
            hits=sum(1 for term in terms if term in text)
            score=round(hits/max(1,len(terms)),4)
            if hits: ranked.append(dict(rank=0, record_index=index, score=score, evidence=text[:300]))
        ranked.sort(key=lambda item:(-item["score"],item["record_index"]))
        for rank,item in enumerate(ranked,1): item["rank"]=rank
        return dict(status="ok", query=query, matches=ranked, count=len(ranked))
