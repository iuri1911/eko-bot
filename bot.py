import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Llama Index dependencies
from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex, ServiceContext
from langchain import OpenAI
from llama_index import PromptHelper, LLMPredictor

# Load environment variables from .env file
load_dotenv()

# Set up your keys and tokens
GPT_API_KEY = os.getenv("GPT_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("GPT_API_KEY")
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Define Llama Index functions
def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 2000
    max_chunk_overlap = 20
    chunk_size_limit = 600

    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.5, model_name="text-davinci-003", max_tokens=num_outputs))

    documents = SimpleDirectoryReader(directory_path).load_data()
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    index = GPTSimpleVectorIndex.from_documents(documents, service_context=service_context)

    index.save_to_disk('index.json')

    return index

def ask_ai(index, query):
    response = index.query(query)
    return response.response

# Build and load the Llama Index
construct_index("context_data/data")
index = GPTSimpleVectorIndex.load_from_disk('index.json')

# Set up the Discord bot
intents = discord.Intents.all()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")

@bot.command(name="ask")
async def ask(ctx, *, question_text):
    response = ask_ai(index, question_text)
    await ctx.send(response)

bot.run(DISCORD_BOT_TOKEN)
