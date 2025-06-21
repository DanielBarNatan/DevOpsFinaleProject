from prometheus_client import Counter, Histogram

REQUEST_COUNTER = Counter(
    "total_requests_total", "Total number of requests received"
)

AGE_LEGAL_COUNTER = Counter(
    "legal_age_requests_total", "Number of users over legal age (18+)"
)

REQUEST_LATENCY = Histogram(
    "request_latency_seconds", "Time spent processing request"
)

