from django.shortcuts import render
from django.http import JsonResponse

def get_case_info(phrase):
    # In a real-world scenario, replace this with a database lookup or API call
    if "Cairn" in phrase:
        return {
    "Case Description": "The arbitration case between Cairn Energy PLC & Cairn UK Holdings Limited and the Republic of India revolves around tax measures applied by India to transactions undertaken by Cairn in 2006, specifically related to the corporate reorganization and listing of Cairn India Limited (CIL) on the Bombay Stock Exchange. The dispute centers on the application of a 2012 amendment to the Income Tax Act 1961, which was applied retroactively to the 2006 transactions, leading to a tax demand of approximately US$1.6 billion from Cairn. Cairn argues that the reorganization and IPO were conducted in compliance with then-applicable Indian tax laws and that the retroactive application of the 2012 amendment breaches the UK-India Bilateral Investment Treaty (BIT). India counters that the transactions were taxable under Indian law even without the 2012 amendment and that Cairn's corporate reorganization was an elaborate scheme to avoid taxes. The tribunal found in favor of Cairn, ruling that India's actions breached the BIT and awarded Cairn compensation.",
    "Case Timeline": [
        {
        "date": "2006-03-08",
        "event": "Cairn Energy's Board of Directors decides to proceed with the India option for corporate reorganization."
        },
        {
        "date": "2006-04-20",
        "event": "Cairn Energy announces its plan to reorganize its Indian assets and operations under an Indian holding company to be publicly listed in India."
        },
        {
        "date": "2006-06-30",
        "event": "Cairn Energy transfers the entire issued share capital of its nine UK subsidiaries to Cairn UK Holdings Limited (CUHL)."
        },
        {
        "date": "2006-08-02",
        "event": "CUHL incorporates Cairn India Holdings Limited (CIHL) in Jersey."
        },
        {
        "date": "2006-08-21",
        "event": "Cairn India Limited (CIL) is incorporated in India as a wholly-owned subsidiary of CUHL."
        },
        {
        "date": "2006-12-11",
        "event": "Bidding period for CIL\u2019s IPO opens."
        },
        {
        "date": "2006-12-15",
        "event": "Bidding period for CIL\u2019s IPO closes."
        },
        {
        "date": "2006-12-29",
        "event": "CIL acquires the remaining 24.3% of CIHL from CUHL for cash consideration, using a portion of the proceeds from the IPO."
        },
        {
        "date": "2012-03-16",
        "event": "India enacts the 2012 Amendment to the Income Tax Act 1961, allowing retroactive taxation of certain transactions."
        },
        {
        "date": "2015-01-14",
        "event": "Cairn initiates arbitration against India under the UK-India BIT."
        },
        {
        "date": "2020-12-21",
        "event": "The tribunal issues its final award, ruling in favor of Cairn and ordering India to pay compensation."
        }
    ],
    "Claimant": "Cairn Energy PLC & Cairn UK Holdings Limited",
    "Respondent": "Republic of India",
    "Tribunal / Court": "Permanent Court of Arbitration (PCA)",
    "Governing Law": "UK-India Bilateral Investment Treaty (BIT)",
    "Industry Sector": "Energy - Oil & Gas Exploration, extraction and production (upstream)",
    "Dispute Type": "Tax-related investment dispute",
    "Legal Claims": "Breach of fair and equitable treatment, retroactive taxation, expropriation",
    "Legal Defenses": "Tax avoidance, compliance with Indian law",
    "Start Date": "2015-01-14",
    "Date of Award": "2020-12-21",
    "Commodity": None,
    "Listed Stock Entity": [
        {
        "ticker": "CNE"
        },
        {
        "ticker": "VED"
        }
    ],
    "Currency": "USD",
    "Claim Amount": 1600000000,
    "Contract Value": None,
    "Legal Costs": None,
    "Interest Rate on Award": None,
    "Regulatory Fines Imposed": None,
    "Award Amount": None
}
    return {"error": "Case not found"}

def case_lookup(request):
    if request.method == "POST":
        phrase = request.POST.get("phrase", "")
        case_info = get_case_info(phrase)
        return JsonResponse(case_info)
    return render(request, "cases/index.html")
