from prometheus_client import Counter

REQUEST_COUNTER = Counter(
    "total_requests_total", "Total number of requests received"
)

AGE_LEGAL_COUNTER = Counter(
    "legal_age_requests_total", "Number of users over legal age (18+)"
)

AGE_ILLEGAL_COUNTER = Counter(
    "illegal_age_requests_total", "Number of users under legal age (<18)"
)
