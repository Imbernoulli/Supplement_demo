# GitAgent

## RUN LOCALLY

### 1. Install dependencies

```bash
cd GitAgent
pip install -r requirements.txt
docker build -t condaimage .
```

### 2. Set your api keys in `config.json`

```json
{
    "GITHUB_TOKEN": "<your github token here>",
    "OPENAI_API_KEY": "<your openai api key here>",
    "Model":"<default is gpt-4-0125-preview (which performs best in test)>",
    "Temperature": "<default is 0.7>"
}
```

### 3. Run test

```bash
python scripts/GitAgent.py 
--query "your query here" 
--name "log folder name" 
--gpt_version "gpt version here(default is gpt-4-0125-preview)" --temperature "temperature here(default is 0.7)"
```

## TO START BACKEND SERVER
### 1. Install dependencies and prepare docker image
```bash
cd GitAgent
pip install -r requirements.txt
docker build -t condaimage .
```
### 2. Set your api keys in `config.json`
```json
{
    "GITHUB_TOKEN": "your github token here",
    "OPENAI_API_KEY": "your openai api key here",
    "Model":"default is gpt-4-0125-preview (which performs best in test)",
    "Temperature": "default is 0.7"
}
```
### 3. Start the server

```bash
python scripts/manage.py runserver 5000
```

