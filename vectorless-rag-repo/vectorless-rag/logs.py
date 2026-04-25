logs = [
    "Pune warehouse backlog due to festival rush",
    "Courier shortage in Pune region",
    "System delay in Mumbai resolved"
]

def search_logs(query):
    return [log for log in logs if "Pune" in log or "delay" in log]