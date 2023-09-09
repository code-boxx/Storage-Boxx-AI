# (A) LOAD SETTINGS & MODULES
import a_settings as set
import b_oto_rodo as oto
from langchain import PromptTemplate
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

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

# (C) COMMAND LINE Q&A
while True:
  query = input("\nEnter a query: ")
  if query == "exit":
    break
  if query.strip() == "":
    continue

  # How many cakes can a person eat in a day?
  # What is John's favorite color?
  # What is John's dream?
  # What is John wearing?
  # How old is John?
  print(chain.run(query))