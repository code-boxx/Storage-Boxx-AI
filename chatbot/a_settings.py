# (A) LOAD MODULES
import os, torch

# (B) MODEL
# hugging face url path, or model file inside models/
model_name = "TheBloke/vicuna-7B-v1.5-GPTQ"
# model_name = "codellama-7b.Q5_K_M.gguf"

# (C) AUTO - PATH
path_base = os.path.dirname(os.path.realpath(__file__))
path_models = os.path.join(path_base, "models")

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

  # (D3) LLAMA PROMPT TEMPLATE
  prompt_template = """Given an input question, first create a syntactically correct MYSQL query to run, then look at the results of the query and return the answer.
  Use the following format:

  Question: "Question here"
  SQLQuery: "SQL Query to run"
  SQLResult: "Result of the SQLQuery"
  Answer: "Final answer here"

  Only use the following tables:

  {table_info}.

  Question: {input}"""

# (E) HF TRANSFORMER
else:
  # (E1) TRANSFORMER ENVIRONMENT VARIABLES
  os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "true"
  os.environ["TRANSFORMERS_CACHE"] = path_models

  # (E2) MODEL VARIABLES
  # @TODO - https://huggingface.co/docs/transformers/main_classes/text_generation
  model_args = {
    "do_sample" : True,
    "max_new_tokens" : 2000,
    "batch_size" : 1,
    "temperature" : 0.7,
    "top_k" : 40,
    "top_p" : 1,
    "num_return_sequences" : 1
  }

  # (E3) PROMPT TEMPLATE
  prompt_template = """Given an input question, first create a syntactically correct MYSQL query to run, then look at the results of the query and return the answer.
  Use the following format:

  Question: "Question here"
  SQLQuery: "SQL Query to run"
  SQLResult: "Result of the SQLQuery"
  Answer: "Final answer here"

  Only use the following tables:

  {table_info}.

  Question: {input}"""

# (F) AUTO - CPU OR GPU
if not any((torch.cuda.is_available(), torch.backends.mps.is_available())):
  gpu = False
else:
  gpu = True

# (G) HTTP ENDPOINT
http_allow = ["http://localhost"]
http_host = "localhost"
http_port = 8008

# (H) JWT
jwt_algo = ""
jwt_secret = ""

# (I) MYSQL
db_include = ["items", "item_batches", "item_mvt", "suppliers", "suppliers_items", "users"]
db_host = ""
db_name = ""
db_user = ""
db_pass = ""