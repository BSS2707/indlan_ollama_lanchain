# IndLan AI

IndLan AI is an AI-powered assistant designed to help users learn, write, understand, and debug programs written in the **IndLan programming language**.

IndLan AI uses **Ollama**, **Phi-3 Mini**, **LangChain**, and **Streamlit** to provide dynamic AI-powered assistance.

## Features

* IndLan programming assistant
* IndLan syntax explanations
* IndLan code generation
* Code debugging
* Beginner-friendly explanations
* Calculator and programming problem assistance
* Conversation memory during the current chat
* Streaming AI responses
* Local AI using Ollama
* No external AI API required
* Fast and lightweight interface
* Supports `.ind` IndLan source files

## Technology Stack

* Python
* Streamlit
* Ollama
* Phi-3 Mini
* LangChain
* LangChain Ollama

## AI Model

This project uses:

```text
phi3:mini
```

Install the model with:

```bash
ollama pull phi3:mini
```

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Open the project folder:

```bash
cd indlan-ai
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Start Ollama

Make sure Ollama is installed and running.

Start the Ollama server:

```bash
ollama serve
```

In another terminal, download the model if you have not already:

```bash
ollama pull phi3:mini
```

## Run IndLan AI

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## IndLan

IndLan is a programming language created by **Bhavya S Solanki**.

IndLan supports both Hindi and English programming keywords and is designed to make programming more accessible to beginners.

### Example

```ind
maano naam = aalao("Aapka naam kya hai? ")

agar naam == "Bhavya" {
    chhap("Welcome Bhavya")
} nahito {
    chhap("Welcome")
}
```

## Common IndLan Keywords

| IndLan        | Meaning              |
| ------------- | -------------------- |
| `maano`       | Variable declaration |
| `agar`        | If                   |
| `nahito_agar` | Else if              |
| `nahito`      | Else                 |
| `jabtak`      | While                |
| `pratyek`     | For-each             |
| `mein`        | In                   |
| `vibhag`      | Switch               |
| `sthiti`      | Case                 |
| `anyatha`     | Default              |
| `kaam`        | Function             |
| `vapas`       | Return               |
| `varg`        | Class                |
| `naya`        | New                  |
| `yeh`         | This                 |
| `jaari`       | Continue             |
| `roko`        | Break                |

## Input and Output

### Output

```ind
chhap("Hello IndLan")
```

### String Input

```ind
maano naam = aalao("Enter your name: ")
```

### Integer Input

```ind
maano age = number_dalao("Enter your age: ")
```

### Decimal Input

```ind
maano price = decimal_dalao("Enter price: ")
```

### Boolean Input

```ind
maano answer = haan_na("Are you happy? ")
```

## Functions

Functions use the `kaam` keyword:

```ind
kaam jodo(a, b) {
    vapas a + b
}

maano result = jodo(10, 20)

chhap("Result:", result)
```

## Switch

```ind
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
```

## Project Structure

```text
indlan-ai/
│
├── app.py
├── requirements.txt
└── README.md
```

## Requirements

Python 3.9 or newer is recommended.

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

The model is configured in `app.py`:

```python
MODEL = "phi3:mini"
```

You can change the model if another Ollama model is installed and compatible with the application.

## How IndLan AI Works

```text
User
  |
  v
Streamlit Interface
  |
  v
LangChain
  |
  v
Ollama
  |
  v
Phi-3 Mini
  |
  v
IndLan AI Response
```

The system prompt provides the AI with IndLan's programming rules, keywords, examples, and common beginner mistakes.

## Important

IndLan AI should generate **IndLan code**, not Python code, when the user asks for IndLan.

IndLan source files use:

```text
.ind
```

IndLan code uses `{ }` for blocks and does not use Python-style `:` block syntax.

## Creator

**Bhavya S Solanki**

AI/ML Developer and BCA student specializing in Artificial Intelligence.

Bhavya created **IndLan**, a programming language designed to make programming more accessible to beginners.

## License

This project is created for learning, experimentation, and development with the IndLan programming language.
