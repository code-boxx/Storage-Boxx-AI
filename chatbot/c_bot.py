# (A) LOAD SETTINGS & MODULES
# (A1) SETTINGS & LANGCHAIN
import a_settings as set
import b_oto_rodo as oto
from langchain import PromptTemplate
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

# (A2) FLASK
import jwt
from flask import Flask, Response, request

# (B) MYSQL + CHAIN
# mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
mysqldb = SQLDatabase.from_uri(f"mysql+mysqlconnector://{set.db_user}:{set.db_pass}@{set.db_host}/{set.db_name}")
chain = SQLDatabaseChain.from_llm(
  oto.llm, mysqldb,
  prompt = PromptTemplate(
    template = set.prompt_template,
    input_variables = ["input", "table_info"]
  )
  # verbose = True
)

# (C) VERIFY USER
def jwtVerify(cookies):
  try:
    token = jwt.decode(
      jwt = cookies.get("cbsess"),
      key = set.jwt_secret,
      audience = set.http_host,
      algorithms = [set.jwt_algo]
    )
    # DO WHATEVER YOU WANT WITH THE DECODED USER TOKEN
    # print(token)
    return True
  except Exception as error:
    # print(error)
    return False

# (D) FLASK
app = Flask(__name__)
@app.route("/", methods = ["POST"])
def bot():
  # (D1) CORS
  if "HTTP_ORIGIN" in request.environ and request.environ["HTTP_ORIGIN"] in set.http_allow:
    # (D1-1) ALLOW ONLY REGISTERED USERS
    if jwtVerify(request.cookies) is False:
      return Response("Not Allowed", status = 405)

    # (D1-2) ANSWER THE QUESTION
    data = dict(request.form)
    if "query" in data:
      ans = chain.run(data["query"])
      ans = ans["result"]
    else:
      ans = "Where's the question, yo?"
    response = Response(ans, status = 200)
    response.headers.add("Access-Control-Allow-Origin", request.environ["HTTP_ORIGIN"] )
    response.headers.add("Access-Control-Allow-Credentials", "true")

  # (D2) ORIGIN NOT ALLOWED
  else:
    response = Response("Not Allowed", status = 405)
  return response

# (E) GO!
if __name__ == "__main__":
  app.run(
    host = set.http_host,
    port = set.http_port
  )