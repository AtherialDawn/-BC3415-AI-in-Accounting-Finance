from flask import Flask,render_template,request
import google.generativeai as genai

api = "AIzaSyCEsQLEfb07F3TDcauwIjDoOZsZ79iAksM"
genai.configure(api_key=api)
client = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def index():
    return(render_template("Homework 4.html"))

@app.route("/ai_agent", methods = ["GET","POST"])
def ai_agent():
    return(render_template("Homework 4 AI Agent.html"))

@app.route("/ai_agent_reply", methods=["GET", "POST"])
def ai_agent_reply():
    q = request.form.get("q")
    response = client.generate_content(q)
    # Convert the response text from Markdown to HTML
    html_content = markdown2.markdown(response.text)
    return render_template("Homework 4 AI Agent Reply.html", r = html_content)

@app.route("/paynow", methods=["GET","POST"])
def paynow():
    return(render_template("Homework 4 Paynow DApp.html"))

if __name__ == "__main__":
    app.run()
