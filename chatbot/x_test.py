# (A) LOAD SETTINGS & MODULES
import a_settings as set
import b_oto_rodo as oto
from langchain import PromptTemplate
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

# (B) MYSQL + CHAIN
mysqldb = SQLDatabase.from_uri(
  f"mysql+mysqlconnector://{set.db_user}:{set.db_pass}@{set.db_host}/{set.db_name}",
  include_tables = set.db_include
)
chain = SQLDatabaseChain.from_llm(
  oto.llm, mysqldb,
  prompt = PromptTemplate(
    template = set.prompt_template,
    input_variables = ["input", "table_info", "dialect"]
  ),
  ** set.chain_args
)

# (C) COMMAND LINE Q&A
while True:
  query = input("\nEnter a query: ")
  if query == "exit":
    break
  if query.strip() == "":
    continue

  # How many users are there in total?
  # How many boxes of soap are in stock?
  try:
    ans = chain(query)
    print(ans)
    #print(ans.result)
    """
    ans.intermediate_steps
      [0] {"input", "top_k", "dialect", "table_info", "stop"}
      [1] SQL
      [2] {"query", "dialect"}
      [3] SQL
      [4] SQL RESULT
    """
  except Exception as e:
    print(e)