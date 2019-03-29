# Sentiment Analysis

## For details see [Sentiment Analysis](https://deepai.org/machine-learning-model/sentiment-analysis) on [Deep AI](https://deepai.org).

<p>
    <a href="https://cloud.docker.com/u/deepaiorg/repository/docker/deepaiorg/sentiment-analysis">
        <img src='https://img.shields.io/docker/cloud/automated/deepaiorg/sentiment-analysis.svg?style=plastic' />
        <img src='https://img.shields.io/docker/cloud/build/deepaiorg/sentiment-analysis.svg' />
    </a>
</p>

This model has been integrated with [ai_integration](https://github.com/deepai-org/ai_integration/blob/master/README.md) for seamless portability across hosting providers.


# Quick Start
```bash
docker pull deepaiorg/sentiment-analysis
```

### HTTP
```bash
docker run --rm -it -e MODE=http -p 5000:5000 deepaiorg/sentiment-analysis
```
Open your browser to localhost:5000 (or the correct IP address)

### Command Line
Save your input text as input.txt in the current directory.
```bash
docker run --rm -it -v `pwd`:/shared -e MODE=command_line deepaiorg/sentiment-analysis --text /shared/input.txt
```

### Command Line with Piped input

```bash
echo '{"text":"I am very happy because this model is great!"}' | docker run -e MODE=test_inputs_dict_json --rm -i deepaiorg/sentiment-analysis
```

# Docker build
```bash
docker build -t sentiment-analysis .
```
