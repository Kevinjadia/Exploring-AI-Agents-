OpenAI Agents SDK Exploration

This repository contains practice scripts exploring the OpenAI Agents SDK. It demonstrates core features such as agent setup, function tools, web search integration, structured outputs, and external API usage like OpenWeatherMap.

---

## 📁 Files Included

- `first_agent.py` – Basic agent setup  
- `agent_with_functiontool.py` – Using function tool  
- `agent_with_websearchtool.py` – Web search integration  
- `agents_as_tool.py` – Calling agents as tools  
- `agents_structured_output.py` – Structured response handling  
- `customizing_handoffs.py` – Custom handoff logic  
- `hand_off_example.py` – Basic handoff between agents  
- `passing_data_during_handoff.py` – Sharing memory between agents  
- `test.py` – Miscellaneous testing  

---

## ✅ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/openai-agents-sdk-exploration.git
cd openai-agents-sdk-exploration
```
### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

```
### 3. Install dependencies

```bash
pip install -r requirements.txt
```
### 4. Get your API keys

- [OpenAI API Key](https://platform.openai.com/account/api-keys)  
- [OpenWeatherMap API Key](https://home.openweathermap.org/api_keys)

### 5. Create a `.env` file

```env
OPENAI_API_KEY=your_openai_key_here
OPENWEATHERMAP_API_KEY=your_openweathermap_key_here
```
### 6. Run any script

```bash
python first_agent.py
```
