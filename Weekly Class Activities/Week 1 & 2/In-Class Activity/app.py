from flask import Flask,render_template,request
import os
import openai

# Add API key before using
client = openai.OpenAI()

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    return(render_template("Week 2 index.html"))

#Changes made in Week 2
@app.route("/ai_agent", methods=["GET","POST"])
def ai_agent():
    return(render_template("ai_agent.html"))

@app.route("/ai_agent_reply", methods=["GET","POST"])
def ai_agent_reply():
    q = request.form.get("q")
    r = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": "q"}]
    )
    return(render_template("ai_agent_reply.html", r = r.choices[0].message.content))

@app.route("/prediction", methods=["GET","POST"])
def prediction():
    return(render_template("Week 2 index.html"))
#End changes made in Week 2

if __name__ == "__main__":
    app.run()