import redis

# client = redis.Redis(host='localhost', port=6379, db=0)
client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

client.set('foo', 'barśćź')

# dodanie decode_responses=True
# powoduje, że dostajemy nie bajty a znaki tekstowe
value = client.get('foo')
print(value)  # b'bar\xc5\x9b\xc4\x87\xc5\xba'
# print(value.decode('utf-8')) # barśćź
# barśćź
print(20 * "-")
print(value)
# --------------------
# barśćź
