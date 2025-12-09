### - [Ollama](https://ollama.com/download/windows) Setup
  * Ollama Update

```
curl -fsSL https://ollama.com/install.sh | sh
sudo systemctl restart ollama
```

  * Ollama Version, Model List

```
ollama --version
ollama list
```

  * Ollama Install GPT-OSS

```
ollama pull gpt-oss:20b
```

### - Run GPT-OSS-20B Chat Server

```
streamlit run streamlit-chat-server.py
```

