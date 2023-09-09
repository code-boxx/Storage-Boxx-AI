# (A) LOAD MODULES
import os, torch

# (B) MODEL
# hugging face url path, or model file inside models/
model_name = "TheBloke/vicuna-7B-v1.5-GPTQ"
#model_name = "llama-2-7b.Q5_K_M.gguf"

# (C) AUTO - PATH
path_base = os.path.dirname(os.path.realpath(__file__))
path_models = os.path.join(path_base, "models")

# (D) LLAMA CPP
if os.path.isfile(os.path.join(path_models, model_name)):
  model_file = os.path.join(path_models, model_name)
  model_args = {
    "max_tokens" : 2000,
    "temperature" : 0.7,
    "top_k" : 40,
    "top_p" : 1,
    "n_gpu_layers" : 40,
    "n_batch" : 512,
    "streaming" : False,
    "verbose" : False
  }

# (E) HF TRANSFORMER
else:
  os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "true"
  os.environ["TRANSFORMERS_CACHE"] = path_models
  model_args = {
    "do_sample" : True,
    "max_new_tokens" : 2000,
    "batch_size" : 1,
    "temperature" : 0.7,
    "top_k" : 40,
    "top_p" : 1,
    "num_return_sequences" : 1
  }

# (F) AUTO - CPU OR GPU
if not any((torch.cuda.is_available(), torch.backends.mps.is_available())):
  gpu = False
else:
  gpu = True

# (G) PROMPT TEMPLATE
prompt_template = """Given an input question, first create a syntactically correct MYSQL query to run, then look at the results of the query and return the answer.
Use the following format:

Question: "Question here"
SQLQuery: "SQL Query to run"
SQLResult: "Result of the SQLQuery"
Answer: "Final answer here"

Only use the following tables:

{table_info}.

Question: {input}"""

# (H) HTTP ENDPOINT
http_allow = ["http://localhost"]
http_host = "localhost"
http_port = 8008

# (I) JWT
jwt_algo = ""
jwt_secret = ""

# (J) MYSQL
db_host = ""
db_name = ""
db_user = ""
db_pass = ""