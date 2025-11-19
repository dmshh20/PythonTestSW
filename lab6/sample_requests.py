import requests

def main():
    print("GET https://httpbin.org/get")
    r = requests.get("https://httpbin.org/get")
    print("Status code:", r.status_code)
    print("Headers (excerpt):")
    for k, v in list(r.headers.items())[:5]:
        print(f"  {k}: {v}")

    print("\nStream example from https://httpbin.org/stream/3")
    r2 = requests.get("https://httpbin.org/stream/3", stream=True)
    for line in r2.iter_lines(decode_unicode=True):
        if line:
            print(line)

if __name__ == "__main__":
    main()
