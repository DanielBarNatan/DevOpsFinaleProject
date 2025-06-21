from prometheus_client import Counter

REQUEST_COUNTER = Counter(
    "total_requests", "Total number of requests received"
)

AGE_LEGAL_COUNTER = Counter(
    "legal_age_requests", "Number of users over legal age (18+)"
)
