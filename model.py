import json
import sys
import traceback

from stanfordcorenlp import StanfordCoreNLP

nlp = None
needs_conn_test = False


def initialize():
    global nlp
    nlp = StanfordCoreNLP('stanford-corenlp-full-2018-02-27')
    print('Testing whether the java conn is OK the first time.')
    ok = test_java_conn()
    if ok:
        print('Java conn is ok')
    else:
        print('Not ok - fail')
        sys.exit(1)


def get_sentiment(sentence):
    global nlp
    result = nlp._request(url=nlp.url, annotators='tokenize,ssplit,pos,parse,sentiment', data=sentence)
    return [y.get('sentiment') for y in result['sentences']]


def test_java_conn():
    sentence = 'Guangdong University of Foreign Studies is located in Guangzhou.'
    real_result = get_sentiment(sentence)
    if real_result == ['Negative']:  # expected
        return True
    else:
        return False


def infer(inputs_dict):
    global needs_conn_test
    if needs_conn_test:
        needs_conn_test = False
        print('Now testing whether the java conn is still OK')
        ok = test_java_conn()
        if ok:
            print('Java conn is ok, some other type of error. Do not exit.')
        else:
            print('Not ok - fail')
            sys.exit(1)

    text = inputs_dict['text']
    if isinstance(text, bytes):
        text = text.decode('utf-8')

    result_data = {"content-type": 'application/json',
                   "data": None,
                   "success": False,
                   "error": None}

    try:
        sentiment = get_sentiment(text)
    except Exception:
        print('Caught exception in sentiment inference:')
        print(traceback.format_exc())
        result_data["error"] = traceback.format_exc()

        needs_conn_test = True  # Need to do another test after we hit an error...
        return result_data

    result_data["success"] = True
    result_data["data"] = json.dumps(sentiment)
    return result_data
