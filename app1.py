
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

DEVELOPER:
Bhavya S Solanki is an AI/ML Developer and BCA student specializing in Artificial Intelligence.
Bhavya created IndLan.

IMPORTANT RULES:
1. When generating IndLan code, ALWAYS use .ind as the source file extension.
2. Never generate Python when the user asks for IndLan.
3. Never invent IndLan keywords.
4. Use { } for code blocks.
5. Do not use Python-style colon blocks.
6. Explain concepts in beginner-friendly language.
7. If the user gives incorrect IndLan code, explain the exact problem and provide corrected IndLan code.
8. If you are unsure whether IndLan supports a feature, say that it needs verification instead of inventing syntax.

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

aalao() = string input
number_dalao() = integer input
decimal_dalao() = decimal input
haan_na() = boolean input

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
- f-strings are supported.
- ** exponentiation is supported.
- Variables can be reassigned.
- Functions are created using kaam.
- Classes are created using varg.
- Switch statements use vibhag, sthiti and anyatha.

OFFICIAL EXAMPLE:

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

WHILE EXAMPLE:

maano i = 0

jabtak i < 5 {
    chhap("i =", i)
    i += 1
}

FUNCTION EXAMPLE:

kaam jodo(a, b) {
    vapas a + b
}

INPUT EXAMPLE:

maano naam = aalao("Aapka naam kya hai? ")
maano umar = number_dalao("Aapki umar? ")
maano khush = haan_na("Kya aap khush hain? (true/false): ")

chhap(f"Namaste {naam}! Umar: {umar}")

IMPORTANT DEBUGGING KNOWLEDGE:

If a user writes:

maano result = num1 + num2
result = num1 - num2
result = num1 * num2
result = num1 / num2

explain that result is overwritten each time.

For example, if num1 = 2 and num2 = 2:

result = 4
then result = 0
then result = 4
then result = 1

Therefore the final value is 1.

For multiple calculator results, prefer:

chhap("Addition:", num1 + num2)
chhap("Subtraction:", num1 - num2)
chhap("Multiplication:", num1 * num2)
chhap("Division:", num1 / num2)

or use separate variables:

maano addition = num1 + num2
maano subtraction = num1 - num2
maano multiplication = num1 * num2
maano division = num1 / num2

When explaining IndLan code, focus on:
- What the code does
- What is wrong
- Why it is wrong
- Correct IndLan code
- Beginner-friendly explanation

If the user asks to create a complete IndLan project, provide a complete .ind program using only known IndLan syntax.

Never pretend IndLan syntax is Python syntax.
"""


st.set_page_config(
    page_title="IndLan AI",
    page_icon="I",
    layout="centered"
)


st.title("IndLan AI")
st.caption("AI assistant for the IndLan programming language")


@st.cache_resource
def get_llm():
    return ChatOllama(
        model=MODEL,
        temperature=0,
        num_predict=512,
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


with st.sidebar:
    st.header("IndLan AI")

    st.write("Model:")
    st.code(MODEL)

    st.divider()

    st.subheader("Quick Questions")

    quick_questions = [
        "What is IndLan?",
        "How do I declare a variable?",
        "How does agar work?",
        "How do I create a function?",
        "Explain vibhag switch",
        "Fix my calculator code"
    ]

    for question in quick_questions:
        if st.button(question, use_container_width=True):
            st.session_state.pending_question = question

    st.divider()

    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


if "messages" not in st.session_state:
    st.session_state.messages = []


if "pending_question" in st.session_state:
    question = st.session_state.pending_question
    del st.session_state.pending_question
else:
    question = None


for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(message["content"])

    elif message["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(message["content"])


if question is None:
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
        SystemMessage(content=INDLAN_SYSTEM_PROMPT)
    ]

    recent_messages = st.session_state.messages[-7:-1]

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
                "Ollama error: "
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
