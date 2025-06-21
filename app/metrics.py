from prometheus_client import Counter

REQUEST_COUNTER = Counter("check_age_requests_total", "Total check-age requests")
AGE_LEGAL_COUNTER = Counter("legal_age_true_total", "Users over 18")

