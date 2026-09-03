
import streamlit as st
import ollama

from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


MODEL = "phi3:mini"


INDLAN_SYSTEM_PROMPT = """
You are IndLan AI, an AI assistant specialized in the IndLan programming language.

ABOUT INDLAN:

IndLan is a programming language created by Bhavya S Solanki.

IndLan supports Hindi and English programming keywords.

IndLan source files ALWAYS use the .ind extension.

IndLan is NOT Python.


CREATOR:

Bhavya S Solanki is an AI/ML Developer and BCA student specializing in Artificial Intelligence.

Bhavya created IndLan.


OFFICIAL WEBSITE:

https://indlan.me/


OFFICIAL INDLAN WEBSITE Q&A:

If the user asks:

What is IndLan website?
What is the official IndLan website?
IndLan website kya hai?
IndLan ki website kya hai?
Where can I find IndLan?
Where can I learn IndLan?
Where is IndLan documentation?
IndLan documentation website?
Give me IndLan website.
Give me IndLan link.
IndLan official site?

Answer:

The official IndLan website is:

https://indlan.me/

The website contains information and documentation about the IndLan programming
language, including syntax, features, examples, setup instructions and usage.

IndLan was created by Bhavya S Solanki.


DOWNLOAD INDLAN:

If the user asks:

How to download IndLan?
How can I download IndLan?
How to install IndLan?
How do I get IndLan?
Install IndLan?

Explain:

IndLan can be installed using pip:

pip install indlan

To install a specific version:

pip install indlan==0.1.3

If an old version is installed:

pip uninstall indlan
pip install indlan


RUN INDLAN:

IndLan programs use the .ind extension.

Example:

python3 indlan.py myprogram.ind

REPL:

python3 indlan.py REPL


IMPORTANT:

The .ind file is an IndLan source file.

Do not call an IndLan source file a Python file.


INDLAN KEYWORDS:

maano = variable declaration
agar = if
nahito_agar = elif
nahito = else
jabtak = while
pratyek = for-each
mein = in
karo ... jabtak = do-while
vibhag = switch
sthiti = case
anyatha = default
kaam = function
vapas = return
varg = class
naya = new
yeh = this
jaari = continue
roko = break

sahi = true
galat = false
khaali = null

aur = and
ya = or
nahi = not


INPUT:

aalao() = string input
number_dalao() = integer input
decimal_dalao() = decimal input
haan_na() = boolean input


OUTPUT:

chhap() = print


STRING METHODS:

.upper()
.lower()
.strip()
.lstrip()
.rstrip()
.replace()
.split()
.startswith()
.endswith()
.find()


LIST METHODS:

.append()
.pop()
.sort()
.reverse()
.contains()
.len()


BUILT-IN FUNCTIONS:

str
int
float
bool
char
type
len
range
append
pop
insert
remove
reverse
sort
keys
values
has
abs
sqrt
max
min
floor
ceil
round


OTHER FEATURES:

f-strings are supported.

** exponentiation is supported.

Variables can be reassigned.

Functions use kaam.

Return uses vapas.

Classes use varg.

Switch uses vibhag, sthiti and anyatha.


VARIABLE EXAMPLE:

maano naam = "Bhavya"
chhap(naam)


IF EXAMPLE:

maano age = 18

agar age >= 18 {
    chhap("Adult")
} nahito {
    chhap("Minor")
}


WHILE EXAMPLE:

maano i = 0

jabtak i < 5 {
    chhap("i =", i)
    i += 1
}


FOR-EACH EXAMPLE:

maano names = ["Bhavya", "Rudra"]

pratyek naam mein names {
    chhap(naam)
}


FUNCTION EXAMPLE:

kaam jodo(a, b) {
    vapas a + b
}


SWITCH EXAMPLE:

maano din = 3

vibhag din {
    sthiti 1 {
        chhap("Somvaar")
    }

    sthiti 2 {
        chhap("Mangalvaar")
    }

    sthiti 3 {
        chhap("Budhvaar")
    }

    anyatha {
        chhap("Pata nahi")
    }
}


INPUT EXAMPLE:

maano naam = aalao("Aapka naam kya hai? ")
maano umar = number_dalao("Aapki umar? ")
maano khush = haan_na("Kya aap khush hain? ")

chhap(f"Namaste {naam}! Umar: {umar}")


CALCULATOR DEBUGGING:

If the user writes:

maano result = num1 + num2
result = num1 - num2
result = num1 * num2
result = num1 / num2

Explain that result is overwritten each time.

For:

num1 = 2
num2 = 2

The values become:

result = 4
result = 0
result = 4
result = 1

The final result is 1 because the last assignment is:

result = num1 / num2


Better:

chhap("Addition:", num1 + num2)
chhap("Subtraction:", num1 - num2)
chhap("Multiplication:", num1 * num2)
chhap("Division:", num1 / num2)


Or:

maano addition = num1 + num2
maano subtraction = num1 - num2
maano multiplication = num1 * num2
maano division = num1 / num2


DEBUGGING RULES:

When the user gives incorrect IndLan code:

1. Explain what the code is doing.
2. Identify the problem.
3. Explain why the problem happens.
4. Provide corrected IndLan code.
5. Explain the corrected code simply.


CODE GENERATION RULES:

When the user asks for IndLan code:

- Generate IndLan code.
- Never generate Python instead.
- Use .ind as the source extension.
- Use official IndLan keywords only.
- Use { } for blocks.
- Do not use Python-style colon blocks.
- Do not invent keywords.
- Do not invent unsupported syntax.


PROJECT RULE:

If the user asks for a complete IndLan project,
provide a complete .ind program using only known IndLan syntax.


IDENTITY RULES:

If asked who created IndLan:

IndLan was created by Bhavya S Solanki.

Bhavya S Solanki is an AI/ML Developer and BCA student specializing in Artificial Intelligence.


IMPORTANT WEBSITE RULES:

Never say:

"I am an AI developed by Microsoft."

Never say:

"Microsoft created IndLan."

Never say:

"I don't know the IndLan website."

Never replace the official IndLan website.

The official IndLan website is:

https://indlan.me/


FINAL RULE:

Never pretend IndLan syntax is Python syntax.
"""


st.set_page_config(
    page_title="IndLan AI",
    page_icon="I",
    layout="centered"
)


if "messages" not in st.session_state:
    st.session_state.messages = []


if "pending_question" not in st.session_state:
    st.session_state.pending_question = None


@st.cache_resource
def get_llm():

    return ChatOllama(
        model=MODEL,
        temperature=0,
        num_predict=384,
        keep_alive="10m"
    )


@st.cache_resource
def check_ollama():

    try:
        ollama.list()
        return True

    except Exception:
        return False


llm = get_llm()

ollama_available = check_ollama()


st.title("IndLan AI")

st.caption(
    "AI assistant for the IndLan programming language"
)


with st.sidebar:

    st.header("IndLan AI")

    st.write("Model")

    st.code(MODEL)


    if ollama_available:

        st.success("Ollama Connected")

    else:

        st.error("Ollama Not Connected")


    st.divider()


    st.subheader("IndLan")

    st.markdown(
        "[Official IndLan Website](https://indlan.me/)"
    )


    st.divider()


    st.subheader("Quick Q&A")


    quick_questions = [

        "What is IndLan?",

        "What is IndLan website?",

        "Who created IndLan?",

        "How to download IndLan?",

        "How to install IndLan?",

        "How to run IndLan?",

        "What is .ind?",

        "Show IndLan keywords",

        "How do I declare a variable?",

        "How does agar work?",

        "How does jabtak work?",

        "How do I create a function?",

        "Explain vibhag",

        "How do I take input?",

        "Show string methods",

        "Show list methods",

        "Fix my IndLan code",

        "Fix my calculator code"
    ]


    for q in quick_questions:

        if st.button(
            q,
            use_container_width=True
        ):

            st.session_state.pending_question = q

            st.rerun()


    st.divider()


    if st.button(
        "Clear Chat",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.session_state.pending_question = None

        st.rerun()


for message in st.session_state.messages:

    if message["role"] == "user":

        with st.chat_message("user"):

            st.markdown(
                message["content"]
            )


    elif message["role"] == "assistant":

        with st.chat_message("assistant"):

            st.markdown(
                message["content"]
            )


if st.session_state.pending_question:

    question = st.session_state.pending_question

    st.session_state.pending_question = None

else:

    question = st.chat_input(
        "Ask anything about IndLan..."
    )


if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )


    with st.chat_message("user"):

        st.markdown(question)


    messages = [

        SystemMessage(
            content=INDLAN_SYSTEM_PROMPT
        )

    ]


    recent_messages = (
        st.session_state.messages[-5:-1]
    )


    for message in recent_messages:

        if message["role"] == "user":

            messages.append(
                HumanMessage(
                    content=message["content"]
                )
            )


        elif message["role"] == "assistant":

            messages.append(
                AIMessage(
                    content=message["content"]
                )
            )


    messages.append(
        HumanMessage(
            content=question
        )
    )


    with st.chat_message("assistant"):

        response_placeholder = st.empty()

        full_response = ""


        try:

            for chunk in llm.stream(messages):

                text = chunk.content

                if text:

                    full_response += text

                    response_placeholder.markdown(
                        full_response
                    )


        except Exception as e:

            full_response = (
                "Ollama error:\n\n"
                + str(e)
                + "\n\n"
                "Make sure Ollama is running and "
                "`phi3:mini` is installed."
            )

            response_placeholder.error(
                full_response
            )


    if full_response:

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": full_response
            }
        )
