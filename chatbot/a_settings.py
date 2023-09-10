# (A) MODEL
# hugging face url path, or model file inside models/
model_name = "codellama-7b-instruct.Q5_K_M.gguf"

# (B) AUTO - PATH
import os
path_base = os.path.dirname(os.path.realpath(__file__))
path_models = os.path.join(path_base, "models")

# (C) AUTO - CPU OR GPU
import torch
if not any((torch.cuda.is_available(), torch.backends.mps.is_available())):
  gpu = False
else:
  gpu = True 

# (D) LLAMA CPP
if os.path.isfile(os.path.join(path_models, model_name)):
  # (D1) LLAMA MODEL FILE
  model_file = os.path.join(path_models, model_name)

  # (D2) LLAMA MODEL SETTINGS
  # https://api.python.langchain.com/en/latest/llms/langchain.llms.llamacpp.LlamaCpp.html
  # FACTUAL
  model_args = {
    "repeat_penalty" : 1.176,
    "temperature" : 0.7,
    "top_k" : 40,
    "top_p" : 0.1,
    "n_ctx" : 3000,
    "max_tokens" : 3000,
    "n_gpu_layers" : 40,
    "n_batch" : 512,
    "streaming" : False,
    "verbose" : False
  }
  """ CREATIVE
  "repeat_penalty" : 1.1,
  "temperature" : 0.75,
  "top_k" : 0,
  "top_p" : 0.7,
  """

# (E) HF TRANSFORMER
else:
  # (E1) TRANSFORMER ENVIRONMENT VARIABLES
  os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "true"
  os.environ["TRANSFORMERS_CACHE"] = path_models

  # (E2) MODEL VARIABLES
  # https://huggingface.co/docs/transformers/main_classes/text_generation
  model_args = {
    "do_sample" : True,
    "temperature" : 0.7,
    "top_k" : 40,
    "top_p" : 1,
    "max_new_tokens" : 3000
  }

# (F) PROMPT TEMPLATE
prompt_template = """Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
Use the following format:

Question: "Question here"
SQLQuery: "SQL Query to run"
SQLResult: "Result of the SQLQuery"
Answer: "Final answer here"

Only use the following tables:

{table_info}.

Question: {input}"""

# (G) CHAIN SETTING
# https://python.langchain.com/docs/use_cases/sql/sqlite
chain_args = {
  "use_query_checker" : True,
  "top_k" : 3,
  "return_intermediate_steps" : True,
  "verbose" : False
}

# (H) HTTP ENDPOINT
http_allow = ["http://localhost", "https://localhost"]
http_host = "localhost"
http_port = 8008

# (I) JWT
jwt_algo = ""
jwt_secret = ""

# (J) MYSQL
db_include = ["items", "item_batches", "item_mvt", "suppliers", "suppliers_items", "users"]
db_host = "localhost"
db_name = "storageboxx"
db_user = "root"
db_pass = ""