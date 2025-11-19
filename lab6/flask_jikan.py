try:
    from flask import Flask, render_template_string
    from jikanpy import Jikan
except Exception:
    print("Missing dependencies. Install with: pip install flask jikanpy")
    raise SystemExit(1)

app = Flask(__name__)
jikan = Jikan()

@app.route("/")
def home():
    try:
        data = jikan.anime(54595, extension="episodes")
    except Exception as ex:
        return f"Jikan request failed: {ex}"
    items = []
    for ep in data.get("data", [])[:10]:
        items.append(f"<p>Епізод {ep.get('mal_id')} «{ep.get('title','-')}» — оцінка: {ep.get('score','N/A')}</p>")
    return render_template_string("<h1>Episodes</h1>{{ body|safe }}", body="\n".join(items))

if __name__ == "__main__":
    print("Run: python flask_jikan.py  and open http://127.0.0.1:5000")
    app.run(debug=True)
