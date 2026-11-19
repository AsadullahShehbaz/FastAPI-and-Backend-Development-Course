from redis import Redis

r = Redis(host="localhost", port=6379, decode_responses=True)
r.set("Name", "Asadullah AI")
print(r.get("Name"))  # Asadullah AI