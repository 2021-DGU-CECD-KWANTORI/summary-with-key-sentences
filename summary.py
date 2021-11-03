# -*- coding: utf-8 -*-
from krwordrank.sentence import summarize_with_sentences
from krwordrank.word import summarize_with_keywords
from wordcloud import WordCloud
from flask import Flask, request
from flask_cors import CORS
import kss
import base64

app = Flask(__name__)
CORS(app)

# 거기에 왕인 박사가 오는 그 모습을 재현하는 게 아직도 일본에서는 큰 마을의 어떤 행사로 취해지고 있습니다. 정확하게 이제그 상복 시대에 어떤 일본에 영향을 주었던 어떤 그런 모습들을 지금도 확인할 수 있는 어떤 그런 축제가 아닌가 라는 생각이 듭니다. 이와이런 것들을 봐도 백제의 어떤 유학의 어떤 문화들이 굉장히 많이 발달했음을 알 수 있겠죠. 뿐만 아니라 여러분들 여기에 또 이제 굉장히 그 유려한 문제를 볼 수 있는 근거가 하나 있는데 그 근거가 뭐냐 면 사 지적 비라는 게 있습니다. 네 이거는 부여에서 발견이 된 그런 비석인데요 이 사택 지적비 같은 경우에는 굉장히 문체가 아주 유려해요 그래서 여기에 어떤 불교적인 요소 조교적인 요소. 여러 종교적 요소가 들어갔다고는 하는데. 그게뭐 해석에 따라 달라지기 때문에 그게 중요한 건 아니에요. 다만 

# 성이란 년 미국에서 시작된 경제 위기로 이것이 전 세계적으로 확산되었 고 일본도 예외는 아니었습니다. 이러한 경제 위기를 극복하기 위해 일 그분이 선택한 방법은 다름 아닌 략전쟁이었는데요. 전쟁의 총알바지로 조선이 필요했던 일본은 우리 민족의 정신을 말살하고자 민족 말살 통치를 실시하게 됩니다. 아무래도 이 시기가 일제 강점기 중 가장 힘들었던 시기였겠죠. 그럼 이제 본. 격적으로 년대 무단 통치. 부터 자세히 한번 살펴볼까요. 우리의 국권을 강제로 피탈한 일제는 식민통치 최고 기구로 조선 총독부를 설치하는데요. 부의 수장인 조사 총독은 해공 대장 출신으로 절대 권력을 행사하게 됩니다 또한 우리의 저항을 억누르기 위해 험병 경찰제를 도입해 강압적인 통치를 하게 되는데요. 헌병 경찰은 군인 경찰를 말하는 것이 이들은 즉결 처분권을 가지고 있어 조금이라도 반항을 하면 그 자리에서 바로 처벌을 할 수 있었습니다.

# 지금부터는 빅데이터의 활용 사례들에 대하여 살펴보겠습니다. 빅데이터의 활용 사례는 아주 많습니다. 여러 분야에서 또 여러 나라에서 다양하게 활용되었으며, 앞으로도 계속 많은 활용이 이어질 것으로 예상할 수 있습니다. 대표적인 사례들로만 구성하여 이들을 살펴보고 빅데이터의 활용과 관련한 이해를 돕도록 하겠습니다. 빅데이터 활용 사례로서 먼저 구글의 독감경보 예측 시스템을 살펴보겠습니다. 2009년 신종 인플루엔자가 전 세계를 강타했습니다. 전 세계적으로 8만 명 이상의 환자가 발생했던 대형 사건이었습니다. 그러므로 효과적 방역이 필수적이었고, 이를 위해서 이러한 질병의 진행 상황을 실시간으로 또 효율적으로 모니터링 하는 것이 필요했습니다. 하지만 이러한 일반적인 질병의 전파속도는 매우 빠른 반면, 정부 당국의 모니터링은 실시간으로 이루어지기 힘들어서 대부분의 보건기구들이 일주일에 한 번 정도 예상수치를 업데이트함으로써 실제 진행상황과는 상당한 차이를 보이게 됩니다.

@app.route('/summary', methods=['POST'])
def summary():
    scripts = request.json['text']
    texts = []
    for sent in kss.split_sentences(scripts):
        texts.append(sent)
        print(sent)
    try:
        keywords, sents = summarize_with_sentences(texts, num_keywords=10, num_keysents=3)
    except:
        sents = 'NO SUMMARY'
    return {'summary' : sents}

@app.route('/keyword', methods=['POST'])
def keyword():
    summaries = request.json['text']
    texts = []
    for sent in kss.split_sentences(summaries):
        texts.append(sent)
        print(sent)

    keywords = summarize_with_keywords(texts, min_count=3, max_length=10,
                                       beta=0.85, max_iter=10, verbose=True)
    print("키워드 : ", keywords)

    font_path = 'NanumGothic.ttf'
    krwordrank_cloud = WordCloud(
        font_path=font_path,
        width=800,
        height=800,
        background_color="white"
    )
    krwordrank_cloud = krwordrank_cloud.generate_from_frequencies(keywords)
    file_name = "keyword.png"
    krwordrank_cloud.to_file(file_name)

    with open('keyword.png', mode='rb') as file:
        img = file.read()

    return {'wordcloud': base64.b64encode(img).decode('utf-8')}

if __name__ == "__main__" :
    app.run(debug=True, host='127.0.0.1', port=5001)