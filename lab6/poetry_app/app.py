import requests

def main():
    print("Poetry app: GET https://httpbin.org/get")
    r = requests.get("https://httpbin.org/get")
    print("Status:", r.status_code)
    for k, v in list(r.headers.items())[:5]:
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()
