# api/index.py
def handler(request):
    return {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json" },
        "body": "Hello from Python on Vercel!"
    }
