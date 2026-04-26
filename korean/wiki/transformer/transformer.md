# 트랜스포머 (기계 학습)

{{기계 학습|인공 신경망}}
[[파일:Transformer,_full_architecture.png|섬네일|왼쪽에는 인코더, 오른쪽에는 디코더가 있는 표준 트랜스포머 아키텍처. 참고: 원래 2017년 트랜스포머에서 사용된 Post-LN 컨벤션과는 다른 Pre-LN 컨벤션을 사용한다.]]
'''트랜스포머'''(transformer)는 멀티 헤드 [[어텐션 (기계 학습)|어텐션]] 메커니즘을 기반으로 하는 [[딥 러닝]] 아키텍처이며, 텍스트가 [[대형 언어 모델#토큰화|토큰]]이라는 수치 표현으로 변환되고 각 토큰은 [[워드 임베딩]] 테이블에서 조회를 통해 벡터로 변환된다.<ref name="2017_Attention_Is_All_You_Need">{{서적 인용|last1=Vaswani |first1=Ashish |author1-link=Ashish Vaswani |last2=Shazeer |first2=Noam |last3=Parmar |first3=Niki |last4=Uszkoreit |first4=Jakob |last5=Jones |first5=Llion |last6=Gomez |first6=Aidan N |author6-link=Aidan Gomez |last7=Kaiser |first7=Łukasz |last8=Polosukhin |first8=Illia |date=2017 |title=Attention is All you Need |url=https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf |journal=Advances in Neural Information Processing Systems |publisher=Curran Associates, Inc. |volume=30}}</ref> 각 레이어에서 각 [[토큰화 (어휘 분석)|토큰]]은 병렬 멀티 헤드 어텐션 메커니즘을 통해 [[컨텍스트 창]] 범위 내에서 다른(마스크되지 않은) 토큰과 함께 [[컨텍스트화 (컴퓨터 과학)|컨텍스트화]]되며, 이를 통해 핵심 토큰에 대한 신호가 증폭되고 덜 중요한 토큰은 약화된다.

트랜스포머는 순환 유닛이 없다는 장점이 있어 [[장단기 메모리]] (LSTM)와 같은 이전 [[순환 신경망|순환 신경망 아키텍처]] (RNN)보다 훈련 시간이 적게 걸린다.<ref name="lstm1997">{{서적 인용|last1=Hochreiter |first1=Sepp |author-link=Sepp Hochreiter |last2=Schmidhuber |first2=Jürgen |author-link2=Jürgen Schmidhuber |date=1 November 1997 |title=Long Short-Term Memory |journal=Neural Computation |volume=9 |issue=8 |pages=1735–1780 |doi=10.1162/neco.1997.9.8.1735 |issn=0899-7667 |pmid=9377276 |s2cid=1915014}}</ref> 이후의 변형들은 대규모 (언어) [[훈련용 검증용 테스트 데이터 세트|데이터셋]]에서 [[대형 언어 모델]] (LLM)을 훈련하는 데 널리 채택되었다.<ref name=":7">{{웹 인용|url=https://openai.com/blog/better-language-models/|title=Better Language Models and Their Implications|date=2019-02-14|website=OpenAI|access-date=2019-08-25|archive-date=2020-12-19|archive-url=https://web.archive.org/web/20201219132206/https://openai.com/blog/better-language-models/|url-status=live}}</ref>

트랜스포머의 현대 버전은 2017년 [[구글]] 연구원들의 논문 "[[어텐션 이즈 올 유 니드]]"에서 제안되었다.<ref name="2017_Attention_Is_All_You_Need" /> 트랜스포머는 원래 [[기계 번역]]을 위한 이전 아키텍처를 개선하기 위해 개발되었지만,<ref name="inventors">{{ArXiv 인용|eprint=1409.0473 |class=cs.CL |last1=Bahdanau |first2=Kyunghyun |last2=Cho |title=Neural Machine Translation by Jointly Learning to Align and Translate |date=September 1, 2014 |last3=Bengio |first3=Yoshua}}</ref><ref name="inventconfirm">{{ArXiv 인용|eprint=1508.04025 |class=cs.CL |first1=Minh-Thang |last1=Luong |first2=Hieu |last2=Pham |title=Effective Approaches to Attention-based Neural Machine Translation |date=August 17, 2015 |last3=Manning |first3=Christopher D.}}</ref> 이후 많은 응용 분야에서 사용되었다. 대규모 [[자연어 처리]], [[컴퓨터 비전]] ([[비전 트랜스포머]]), [[강화 학습]],<ref name=":10" /><ref>{{서적 인용|last1=Parisotto |first1=Emilio |last2=Song |first2=Francis |last3=Rae |first3=Jack |last4=Pascanu |first4=Razvan |last5=Gulcehre |first5=Caglar |last6=Jayakumar |first6=Siddhant |last7=Jaderberg |first7=Max |last8=Kaufman |first8=Raphaël Lopez |last9=Clark |first9=Aidan |last10=Noury |first10=Seb |last11=Botvinick |first11=Matthew |last12=Heess |first12=Nicolas |last13=Hadsell |first13=Raia |date=2020-11-21 |title=Stabilizing Transformers for Reinforcement Learning |url=https://proceedings.mlr.press/v119/parisotto20a.html |journal=Proceedings of the 37th International Conference on Machine Learning |language=en |publisher=PMLR |pages=7487–7498}}</ref> [[오디오 신호 처리|오디오]],<ref name="Robust Speech Recognition via Large-Scale Weak Supervision">{{ArXiv 인용|eprint=2212.04356 |last1=Radford |first1=Alec |author2=Jong Wook Kim |last3=Xu |first3=Tao |last4=Brockman |first4=Greg |last5=McLeavey |first5=Christine |last6=Sutskever |first6=Ilya |title=Robust Speech Recognition via Large-Scale Weak Supervision |year=2022 |class=eess.AS }}</ref> [[멀티모덜 학습]], [[로봇공학]],<ref>{{서적 인용|last1=Monastirsky |first1=Maxim |last2=Azulay |first2=Osher |last3=Sintov |first3=Avishai |date=February 2023 |title=Learning to Throw With a Handful of Samples Using Decision Transformers |url=https://ieeexplore.ieee.org/document/9984828 |journal=IEEE Robotics and Automation Letters |volume=8 |issue=2 |pages=576–583 |doi=10.1109/LRA.2022.3229266 |issn=2377-3766|url-access=subscription }}</ref> 심지어 [[컴퓨터 체스]]를 두는 데에도 사용된다.<ref name="grandmaster">{{ArXiv 인용|last1=Ruoss |first1=Anian |last2=Delétang |first2=Grégoire |last3=Medapati |first3=Sourabh |last4=Grau-Moya |first4=Jordi |last5=Wenliang |first5=Li |last6=Catt |first6=Elliot |last7=Reid |first7=John |last8=Genewein |first8=Tim |date=2024-02-07 |title=Grandmaster-Level Chess Without Search |class=cs.LG |eprint=2402.04494v1}}</ref> 또한 [[전이학습|사전 훈련 시스템]]인 [[GPT (언어 모델)|GPT]] (Generative Pre-trained Transformers) 및<ref name="wolf2020">{{서적 인용|last1=Wolf |first1=Thomas| last2=Debut |first2=Lysandre| last3=Sanh |first3=Victor |last4=Chaumond |first4=Julien| last5=Delangue |first5=Clement| last6=Moi |first6=Anthony |last7=Cistac |first7=Pierric |last8=Rault |first8=Tim |last9=Louf |first9=Remi |last10=Funtowicz |first10=Morgan |last11=Davison |first11=Joe |last12=Shleifer |last12=Sam |last13=von Platen |first13=Patrick |last14=Ma |first14=Clara |last15=Jernite |first15=Yacine |last16=Plu |first16=Julien |last17=Xu |first17=Canwen |last18=Le Scao |first18=Teven |last19=Gugger |first19=Sylvain |last20=Drame |first20=Mariama |last21=Lhoest |first21=Quentin |last22=Rush |first22=Alexander |title=Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations |chapter=Transformers: State-of-the-Art Natural Language Processing |year=2020|pages=38–45 |doi=10.18653/v1/2020.emnlp-demos.6 |s2cid=208117506}}</ref> [[BERT (언어 모델)|BERT]] (Bidirectional Encoder Representations from Transformers)의 개발로 이어졌다.<ref name=":6">{{웹 인용|url=http://ai.googleblog.com/2018/11/open-sourcing-bert-state-of-art-pre.html|title=Open Sourcing BERT: State-of-the-Art Pre-training for Natural Language Processing|website=Google AI Blog|date=2 November 2018 |access-date=2019-08-25|archive-date=2021-01-13|archive-url=https://web.archive.org/web/20210113211449/https://ai.googleblog.com/2018/11/open-sourcing-bert-state-of-art-pre.html|url-status=live}}</ref>{{목차숨김|3}}

== 역사 ==
{{참고|기계 학습 연표}}

=== 이전 모델 ===
수년 동안 시퀀스 모델링 및 생성은 일반 [[순환 신경망]] (RNN)을 사용하여 수행되었다. 잘 인용된 초기 예는 [[엘만 네트워크]] (1990)였다. 이론적으로 한 토큰의 정보는 시퀀스를 따라 임의로 멀리 전파될 수 있지만, 실제로는 [[소실 경사 문제]]로 인해 긴 문장 끝에서 모델의 상태가 이전 토큰에 대한 정확하고 추출 가능한 정보 없이 남게 된다.

주요 돌파구는 [[장단기 메모리|LSTM]] (1995)이었다.{{주태그|[[게이트 순환 유닛]] (2014)은 복잡성을 더욱 줄였다.}} LSTM은 소실 경사 문제를 극복하기 위한 다양한 혁신을 사용하여 긴 시퀀스 모델링을 효율적으로 학습할 수 있었다. 한 가지 주요 혁신은 다른 뉴런의 출력을 곱하는 뉴런, 즉 곱셈 단위를 사용하는 [[어텐션 메커니즘]]을 사용한 것이었다.<ref>{{서적 인용|last1=Feldman |first1=J. A. |last2=Ballard |first2=D. H. |date=1982-07-01 |title=Connectionist models and their properties |url=https://www.sciencedirect.com/science/article/pii/S0364021382800013 |journal=Cognitive Science |volume=6 |issue=3 |pages=205–254 |doi=10.1016/S0364-0213(82)80001-3 |issn=0364-0213|url-access=subscription }}</ref> 곱셈 단위를 사용하는 신경망은 나중에 시그마-파이 네트워크<ref name="PDP">{{서적 인용|last1=Rumelhart |first1=David E. |url=https://stanford.edu/~jlmcc/papers/PDP/Chapter2.pdf |title=Parallel Distributed Processing, Volume 1: Explorations in the Microstructure of Cognition: Foundations, Chapter 2 |last2=McClelland |first2=James L. |last3=Hinton |first3=Geoffrey E. |date=1987-07-29 |publisher=Bradford Books |isbn=978-0-262-68053-0 |location=Cambridge, Mass |language=en}}</ref> 또는 [[고차 신경망|고차 네트워크]]라고 불렸다.<ref>{{서적 인용|last1=Giles |first1=C. Lee |last2=Maxwell |first2=Tom |date=1987-12-01 |title=Learning, invariance, and generalization in high-order neural networks |url=https://opg.optica.org/abstract.cfm?URI=ao-26-23-4972 |journal=Applied Optics |language=en |volume=26 |issue=23 |pages=4972–4978 |doi=10.1364/AO.26.004972 |pmid=20523475 |issn=0003-6935|url-access=subscription }}</ref> LSTM은 2017년 트랜스포머 발표 전까지 장기 시퀀스 모델링을 위한 표준 아키텍처가 되었다.
그러나 LSTM은 대부분의 다른 RNN처럼 순차 처리를 사용했다.{{주태그|RWKV 또는 상태 공간 모델과 같은 일부 아키텍처는 이 문제를 피한다.}} 특히 RNN은 한 번에 하나의 토큰을 처음부터 끝까지 처리하며, 시퀀스의 모든 토큰에 대해 병렬로 작동할 수 없다.

현대 트랜스포머는 이 문제를 극복했지만, RNN과 달리 컨텍스트 창의 크기에 대해 [[이차 함수|이차적]]으로 계산 시간이 필요하다. 선형적으로 스케일링되는 [[고속 가중치]] 컨트롤러 (1992)는 입력에 따라 추가 처리를 위한 가중치 행렬을 계산하는 방법을 학습한다.<ref name="transform19922">{{서적 인용|last1=Schmidhuber |first1=Jürgen |author-link1=Jürgen Schmidhuber |date=1992 |title=Learning to control fast-weight memories: an alternative to recurrent nets. |url=https://archive.org/download/wikipedia-scholarly-sources-corpus/10.1162.zip/10.1162%252Fneco.1992.4.1.131.pdf |journal=Neural Computation |volume=4 |issue=1 |pages=131–139 |doi=10.1162/neco.1992.4.1.131 |s2cid=16683347}}</ref> 두 네트워크 중 하나는 "고속 가중치" 또는 "동적 링크" (1981)를 가지고 있다.<ref name="malsburg1981">Christoph von der Malsburg: The correlation theory of brain function. Internal Report 81-2, MPI Biophysical Chemistry, 1981. http://cogprints.org/1380/1/vdM_correlation.pdf See Reprint in Models of Neural Networks II, chapter 2, pages 95–119. Springer, Berlin, 1994.</ref><ref name="feldman1982">Jerome A. Feldman, "Dynamic connections in neural networks," Biological Cybernetics, vol. 46, no. 1, pp. 27–39, Dec. 1982.</ref><ref>{{서적 인용|last1=Hinton |first1=Geoffrey E. |last2=Plaut |first2=David C. |date=1987 |title=Using Fast Weights to Deblur Old Memories |url=https://escholarship.org/uc/item/0570j1dp |journal=Proceedings of the Annual Meeting of the Cognitive Science Society |language=en |volume=9}}</ref> 느린 신경망은 경사 하강법을 통해 쿼리에 대한 답변을 계산하는 빠른 신경망의 가중치 변경을 계산하기 위한 키와 값을 생성하는 방법을 학습한다.<ref name="transform19922"/> 이는 나중에 비정규화된 선형 트랜스포머와 동등하다는 것이 입증되었다.<ref name="fastlinear20202">{{콘퍼런스 인용|last1=Katharopoulos |first1=Angelos |first2=Apoorv |last2=Vyas |first3=Nikolaos |last3=Pappas |first4=François |last4=Fleuret |date=2020 |title=Transformers are RNNs: Fast autoregressive Transformers with linear attention |url=https://proceedings.mlr.press/v119/katharopoulos20a.html |publisher=PMLR |pages=5156–5165 |book-title=ICML 2020}}</ref><ref name="schlag20212">{{콘퍼런스 인용|last1=Schlag |first1=Imanol |last2=Irie |first2=Kazuki |last3=Schmidhuber |first3=Jürgen |author-link3=Juergen Schmidhuber |date=2021 |title=Linear Transformers Are Secretly Fast Weight Programmers |publisher=Springer |pages=9355–9366 |book-title=ICML 2021}}</ref>

=== Seq2seq와 어텐션 ===
{{본문|Seq2seq#역사}}
인코더-디코더 시퀀스 변환 개념은 2010년대 초에 개발되었다. 일반적으로 seq2seq의 원형으로 인용되는 것은 2014년에 동시에 발표된 두 개의 논문이다.<ref name=":22">{{서적 인용|last1=Cho |first1=Kyunghyun |last2=van Merriënboer |first2=Bart |last3=Gulcehre |first3=Caglar |last4=Bahdanau |first4=Dzmitry |last5=Bougares |first5=Fethi |last6=Schwenk |first6=Holger |last7=Bengio |first7=Yoshua |chapter=Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation |date=October 2014 |editor-last=Moschitti |editor-first=Alessandro |editor2-last=Pang |editor2-first=Bo |editor3-last=Daelemans |editor3-first=Walter |title=Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP) |chapter-url=https://aclanthology.org/D14-1179 |location=Doha, Qatar |publisher=Association for Computational Linguistics |pages=1724–1734 |doi=10.3115/v1/D14-1179|arxiv=1406.1078 }}</ref><ref name="sequence">{{ArXiv 인용|eprint=1409.3215 |class=cs.CL |first1=Ilya |last1=Sutskever |first2=Oriol |last2=Vinyals |title=Sequence to sequence learning with neural networks |date=14 Dec 2014 |last3=Le |first3=Quoc Viet}} [first version posted to arXiv on 10 Sep 2014]</ref>

기계 번역을 위한 3억 8천만 매개변수 모델은 두 개의 [[장단기 메모리]] (LSTM)를 사용한다.<ref name="sequence" /> 이 아키텍처는 두 부분으로 구성된다. 인코더는 토큰 시퀀스를 입력받아 벡터로 변환하는 LSTM이다. 디코더는 벡터를 토큰 시퀀스로 변환하는 또 다른 LSTM이다. 유사하게, 또 다른 1억 3천만 매개변수 모델은 LSTM 대신 [[게이트 순환 유닛]] (GRU)을 사용했다.<ref name=":22" /> 이후 연구에 따르면 GRU는 seq2seq에서 LSTM보다 성능이 더 좋지도 나쁘지도 않다.<ref name="MyUser_Arxiv.org_May_18_2016c">{{ArXiv 인용|eprint=1412.3555 |class=cs.NE |first1=Junyoung |last1=Chung |first2=Caglar |last2=Gulcehre |title=Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling |last3=Cho |first3=KyungHyun |last4=Bengio |first4=Yoshua |year=2014}}</ref><ref name="gruber_jockisch">{{인용|last1=Gruber |first1=N. |title=Are GRU cells more specific and LSTM cells more sensitive in motive classification of text? |journal=Frontiers in Artificial Intelligence |volume=3 |page=40 |year=2020 |doi=10.3389/frai.2020.00040 |pmc=7861254 |pmid=33733157 |s2cid=220252321 |last2=Jockisch |first2=A. |doi-access=free}}</ref>

이러한 초기 seq2seq 모델에는 어텐션 메커니즘이 없었고, 상태 벡터는 원본 텍스트의 마지막 단어가 처리된 후에만 접근할 수 있었다. 이론적으로 이러한 벡터가 전체 원본 문장에 대한 정보를 유지하지만, 실제로는 정보가 제대로 보존되지 않았다. 이는 입력이 하나의 순환 네트워크에 의해 고정된 크기의 출력 벡터로 순차적으로 처리된 다음, 다른 순환 네트워크에 의해 출력으로 처리되기 때문이다. 입력이 길면 출력 벡터가 모든 관련 정보를 포함할 수 없으므로 출력이 저하된다. 증거로, 입력 문장을 뒤집는 것이 seq2seq 번역을 개선했다.<ref>{{서적 인용 |last1=Sutskever |first1=Ilya |last2=Vinyals |first2=Oriol |last3=Le |first3=Quoc V |date=2014 |title=Sequence to Sequence Learning with Neural Networks |url=https://proceedings.neurips.cc/paper/2014/hash/a14ac55a4f27472c5d894ec1c3c743d2-Abstract.html |journal=Advances in Neural Information Processing Systems |publisher=Curran Associates, Inc. |volume=27 |arxiv=1409.3215 |access-date=2025-06-20 |archive-date=2025-01-27 |archive-url=https://web.archive.org/web/20250127094117/https://proceedings.neurips.cc/paper/2014/hash/a14ac55a4f27472c5d894ec1c3c743d2-Abstract.html |url-status= }}</ref>

RNNsearch 모델은 병목 현상 (고정된 크기의 출력 벡터 문제)을 해결하기 위해 기계 번역을 위한 seq2seq에 어텐션 메커니즘을 도입하여 모델이 장거리 의존성을 더 쉽게 처리할 수 있게 했다. 이 이름은 "번역 디코딩 중에 원본 문장을 검색하는 것을 에뮬레이션한다"는 의미이다.<ref name="inventors" />

기계 번역을 위한 전역 (RNNsearch의) 및 지역 (슬라이딩 윈도우) 어텐션 모델 아키텍처 간의 상대적 성능을 비교한 결과, 혼합 어텐션이 전역 어텐션보다 품질이 높았고, 지역 어텐션은 번역 시간을 단축했다.<ref>{{ArXiv 인용|eprint=1508.04025 |class=cs.CL |first1=Minh-Thang |last1=Luong |first2=Hieu |last2=Pham |title=Effective Approaches to Attention-based Neural Machine Translation |date=2015 |last3=Manning |first3=Christopher D.}}</ref>

2016년, [[구글 번역]]은 [[구글 신경망 기계 번역]]으로 개편되었으며, 이는 이전 [[통계적 기계 번역]] 기반 모델을 대체했다. 새로운 모델은 인코더와 디코더 모두 8계층의 양방향 LSTM으로 구성된 seq2seq 모델이었다.<ref name="Y4moj">{{ArXiv 인용|eprint=1609.08144 |class=cs.CL |first1=Yonghui |last1=Wu |first2=Mike |last2=Schuster |title=Google's Neural Machine Translation System: Bridging the Gap between Human and Machine Translation |date=2016-09-01 |display-authors=1 |last3=Chen |first3=Zhifeng |last4=Le |first4=Quoc V. |last5=Norouzi |first5=Mohammad |last6=Macherey |first6=Wolfgang |last7=Krikun |first7=Maxim |last8=Cao |first8=Yuan |last9=Gao |first9=Qin |last10=Macherey |first10=Klaus |last11=Klingner |first11=Jeff |last12=Shah |first12=Apurva |last13=Johnson |first13=Melvin |last14=Liu |first14=Xiaobing |last15=Kaiser |first15=Łukasz}}</ref> 개발에 9개월이 걸렸으며, 10년이 걸린 통계적 접근 방식을 능가했다.<ref name="UJDu8">{{뉴스 인용|last=Lewis-Kraus |first=Gideon |date=2016-12-14 |title=The Great A.I. Awakening |url=https://www.nytimes.com/2016/12/14/magazine/the-great-ai-awakening.html |archive-url=https://web.archive.org/web/20230524052626/https://www.nytimes.com/2016/12/14/magazine/the-great-ai-awakening.html |archive-date=24 May 2023 |access-date=2023-06-22 |work=The New York Times |issn=0362-4331}}</ref>

=== 병렬화 어텐션 ===
{{본문|어텐션 (기계 학습)#역사}}
어텐션 (자체 어텐션 포함)이 있는 Seq2seq 모델은 여전히 순환 네트워크와 동일한 문제, 즉 [[병렬 컴퓨팅|병렬화]]하기 어렵다는 문제로 인해 GPU에서 가속화할 수 없었다. 2016년, 분해 가능한 어텐션은 [[순방향 신경망|순방향 네트워크]]에 자체 어텐션 메커니즘을 적용하여 쉽게 병렬화할 수 있었고, LSTM보다 매개변수를 10배 적게 사용하여 [[텍스트 추론]]에서 [[최첨단|SOTA]] 결과를 달성했다.<ref>{{ArXiv 인용|last1=Parikh |first1=Ankur P. |title=A Decomposable Attention Model for Natural Language Inference |date=2016-09-25 |eprint=1606.01933 |last2=Täckström |first2=Oscar |last3=Das |first3=Dipanjan |last4=Uszkoreit |first4=Jakob|class=cs.CL }}</ref> 저자 중 한 명인 야코프 우슈코레이트(Jakob Uszkoreit)는 순환 없이 어텐션만으로도 언어 번역에 충분할 것이라고 예상했으며, 그래서 "어텐션이 필요한 전부"라는 제목이 붙었다.<ref name=":11">{{잡지 인용|last=Levy |first=Steven |title=8 Google Employees Invented Modern AI. Here's the Inside Story |url=https://www.wired.com/story/eight-google-employees-invented-modern-ai-transformers-paper/ |url-status=live |archive-url=https://web.archive.org/web/20240320101528/https://www.wired.com/story/eight-google-employees-invented-modern-ai-transformers-paper/ |archive-date=20 Mar 2024 |access-date=2024-08-06 |magazine=Wired |language=en-US |issn=1059-1028}}</ref> 당시에는 이 가설이 통념에 반하는 것이었으며, 심지어 그의 아버지이자 유명한 전산 언어학자인 [[한스 우슈코레이트]]도 회의적이었다.<ref name=":11" /> 같은 해, LSTM에 자체 어텐션 (내부 어텐션 또는 문장 내부 어텐션이라 불림)이 제안되었다.<ref>{{서적 인용|last1=Cheng |first1=Jianpeng |title=Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing |last2=Dong |first2=Li |last3=Lapata |first3=Mirella |date=November 2016 |publisher=Association for Computational Linguistics |editor-last=Su |editor-first=Jian |location=Austin, Texas |pages=551–561 |chapter=Long Short-Term Memory-Networks for Machine Reading |doi=10.18653/v1/D16-1053 |editor2-last=Duh |editor2-first=Kevin |editor3-last=Carreras |editor3-first=Xavier |chapter-url=https://aclanthology.org/D16-1053/}}</ref>

2017년, 원래 (1억 규모의) 인코더-디코더 트랜스포머 모델은 "[[어텐션 이즈 올 유 니드]]" 논문에서 제안되었다. 당시 연구의 초점은 [[기계 번역]]을 위한 [[Seq2seq]]를 개선하는 것이었다. 모든 토큰을 병렬로 처리하기 위해 순환을 제거하면서 텍스트 처리 성능을 유지하기 위해 점곱 어텐션 메커니즘을 유지했다.<ref name="2017_Attention_Is_All_You_Need" /> 이는 독립적인 헤드 사용과 순환 부족으로 인해 병렬화하기 더 쉬운 멀티 헤드 어텐션 모델의 도입으로 이어졌다. 이 모델의 병렬화 가능성은 대규모 신경망에서 널리 사용되는 중요한 요인이었다.<ref>{{인용|last1=Peng |first1=Bo |title=RWKV: Reinventing RNNs for the Transformer Era |date=2023-12-10 |arxiv=2305.13048 |last2=Alcaide |first2=Eric |last3=Anthony |first3=Quentin |last4=Albalak |first4=Alon |last5=Arcadinho |first5=Samuel |last6=Biderman |first6=Stella |last7=Cao |first7=Huanqi |last8=Cheng |first8=Xin |last9=Chung |first9=Michael}}</ref>
{{앵커|트랜스포머 붐}}

=== AI 붐 시대 ===
2017년 봄, "어텐션 이즈 올 유 니드" 초판이 발표되기도 전에 공동 저자 중 한 명은 아키텍처의 "디코더-온리" 변형을 사용하여 가상의 위키백과 기사를 생성했다.<ref>{{잡지 인용|last=Marche |first=Stephen |date=2024-08-23 |title=Was Linguistic A.I. Created by Accident? |url=https://www.newyorker.com/science/annals-of-artificial-intelligence/was-linguistic-ai-created-by-accident |access-date=2024-08-27 |magazine=The New Yorker |language=en-US |issn=0028-792X}}</ref> 트랜스포머 아키텍처는 현재 진행 중인 [[AI 붐]]에 기여하는 많은 [[생성형 인공지능|생성 모델]]과 함께 사용된다.

언어 모델링에서 [[ELMo]] (2018)는 문맥화된 [[워드 임베딩]]을 생성하는 양방향 LSTM으로, [[단어 가방 모형]] 및 [[Word2vec]] 연구를 개선했다. 그 뒤를 이어 인코더-온리 트랜스포머 모델인 [[BERT (언어 모델)|BERT]] (2018)가 나왔다.<ref name=":03">{{ArXiv 인용|eprint=1810.04805v2 |class=cs.CL |first1=Jacob |last1=Devlin |first2=Ming-Wei |last2=Chang |title=BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding |date=11 October 2018 |last3=Lee |first3=Kenton |last4=Toutanova |first4=Kristina}}</ref> 2019년 10월, 구글은 검색 쿼리 처리에 BERT를 사용하기 시작했다.<ref>{{웹 인용|date=2020-10-15 |title=Google: BERT now used on almost every English query |url=https://searchengineland.com/google-bert-used-on-almost-every-english-query-342193 |access-date=2020-11-24 |website=Search Engine Land}}</ref> 2020년, 구글 번역은 이전 RNN-인코더-RNN-디코더 모델을 트랜스포머-인코더-RNN-디코더 모델로 교체했다.<ref>{{웹 인용|title=Recent Advances in Google Translate |url=http://research.google/blog/recent-advances-in-google-translate/ |access-date=2024-05-08 |website=research.google |language=en}}</ref>

2018년부터 오픈AI의 [[GPT (언어 모델)|GPT 시리즈]]는 디코더-온리 트랜스포머로서 [[자연어 생성]] 분야에서 최첨단이 되었다. 2022년, GPT-3 기반 챗봇인 [[챗GPT]]가 예상치 못하게<ref>{{웹 인용|title=The inside story of how ChatGPT was built from the people who made it |url=https://www.technologyreview.com/2023/03/03/1069311/inside-story-oral-history-how-chatgpt-built-openai/ |access-date=2024-08-06 |website=MIT Technology Review |language=en}}</ref> 인기를 끌면서 [[대형 언어 모델]]에 대한 붐을 일으켰다.<ref name="gpt12">{{웹 인용|date=June 11, 2018 |title=Improving language understanding with unsupervised learning |url=https://openai.com/research/language-unsupervised |url-status=live |archive-url=https://web.archive.org/web/20230318210736/https://openai.com/research/language-unsupervised |archive-date=2023-03-18 |access-date=2023-03-18 |website=openai.com}}</ref><ref name="ngEG3">{{인용|title=finetune-transformer-lm |date=June 11, 2018 |url=https://github.com/openai/finetune-transformer-lm |access-date=2023-05-01 |publisher=OpenAI}}</ref>

2020년부터 트랜스포머는 텍스트를 넘어선 모달리티에 적용되기 시작했으며, 여기에는 [[비전 트랜스포머]],<ref name="auto2">{{ArXiv 인용|eprint=2010.11929 |class=cs.CV |first1=Alexey |last1=Dosovitskiy |first2=Lucas |last2=Beyer |title=An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale |date=2021-06-03 |last3=Kolesnikov |first3=Alexander |last4=Weissenborn |first4=Dirk |last5=Zhai |first5=Xiaohua |last6=Unterthiner |first6=Thomas |last7=Dehghani |first7=Mostafa |last8=Minderer |first8=Matthias |last9=Heigold |first9=Georg |last10=Gelly |first10=Sylvain |last11=Uszkoreit |first11=Jakob}}</ref> 음성 인식,<ref name="Gulati2020" /> 로봇공학,<ref name=":10">{{인용|last1=Chen |first1=Lili |title=Decision Transformer: Reinforcement Learning via Sequence Modeling |date=2021-06-24 |arxiv=2106.01345 |last2=Lu |first2=Kevin |last3=Rajeswaran |first3=Aravind |last4=Lee |first4=Kimin |last5=Grover |first5=Aditya |last6=Laskin |first6=Michael |last7=Abbeel |first7=Pieter |last8=Srinivas |first8=Aravind |last9=Mordatch |first9=Igor}}</ref> 그리고 [[멀티모덜 학습|멀티모덜]]이 포함된다.<ref name="choromanski2020">{{인용|last1=Choromanski |first1=Krzysztof |title=Rethinking Attention with Performers |date=2022-11-19 |arxiv=2009.14794 |last2=Likhosherstov |first2=Valerii |last3=Dohan |first3=David |last4=Song |first4=Xingyou |last5=Gane |first5=Andreea |last6=Sarlos |first6=Tamas |last7=Hawkins |first7=Peter |last8=Davis |first8=Jared |last9=Mohiuddin |first9=Afroz}}</ref> 비전 트랜스포머는 다시 [[합성곱 신경망]]의 새로운 발전을 촉진했다.<ref>{{콘퍼런스 인용|last1=Liu |first1=Zhuang |last2=Mao |first2=Hanzi |last3=Wu |first3=Chao-Yuan |last4=Feichtenhofer |first4=Christoph |last5=Darrell |first5=Trevor |last6=Xie |first6=Saining |date=2022 |conference=Conference on Computer Vision and Pattern Recognition |title=A ConvNet for the 2020s |url=https://openaccess.thecvf.com/content/CVPR2022/html/Liu_A_ConvNet_for_the_2020s_CVPR_2022_paper.html |language=en |pages=11976–11986}}</ref> [[DALL-E]] (2021), [[스테이블 디퓨전|스테이블 디퓨전 3]] (2024),<ref name=":62">{{인용|last1=Esser |first1=Patrick |title=Scaling Rectified Flow Transformers for High-Resolution Image Synthesis |date=2024-03-05 |arxiv=2403.03206 |last2=Kulal |first2=Sumith |last3=Blattmann |first3=Andreas |last4=Entezari |first4=Rahim |last5=Müller |first5=Jonas |last6=Saini |first6=Harry |last7=Levi |first7=Yam |last8=Lorenz |first8=Dominik |last9=Sauer |first9=Axel}}</ref> 및 [[소라 (텍스트-비디오 모델)|소라]] (2024)와 같은 이미지 및 비디오 생성기는 트랜스포머를 사용하여 입력 데이터 (텍스트 프롬프트 등)를 "토큰"으로 분해한 다음 자체 어텐션을 사용하여 각 토큰 간의 관련성을 계산하여 모델이 데이터 내의 컨텍스트와 관계를 이해하도록 돕는다.

== 훈련 ==
=== 훈련 안정화 방법 ===
일반 트랜스포머 아키텍처는 수렴에 어려움을 겪었다. 원본 논문에서<ref name="2017_Attention_Is_All_You_Need" /> 저자들은 학습률 웜업을 사용할 것을 권장했다. 즉, 학습률은 훈련의 첫 부분 (보통 총 훈련 단계의 2%로 권장됨) 동안 0에서 최대값으로 선형적으로 스케일링된 후 다시 감소해야 한다.

2020년 논문에서는 멀티헤드 어텐션 및 순방향 레이어 전 (후가 아닌) [[레이어 정규화]]를 사용하면 학습률 웜업 없이 훈련이 안정화된다는 사실을 발견했다.<ref name="auto1">{{ArXiv 인용|eprint=2002.04745 |class=cs.LG |first1=Ruibin |last1=Xiong |first2=Yunchang |last2=Yang |title=On Layer Normalization in the Transformer Architecture |date=2020-06-29 |last3=He |first3=Di |last4=Zheng |first4=Kai |last5=Zheng |first5=Shuxin |last6=Xing |first6=Chen |last7=Zhang |first7=Huishuai |last8=Lan |first8=Yanyan |last9=Wang |first9=Liwei |last10=Liu |first10=Tie-Yan}}</ref>

=== 사전 훈련-미세 조정 ===
트랜스포머는 일반적으로 먼저 대규모 일반 데이터셋에서 [[자기 지도 학습]]을 통해 사전 훈련된 다음, 작은 작업별 데이터셋에서 [[지도 학습|지도]] [[파인 튜닝|미세 조정]]된다. 사전 훈련 데이터셋은 일반적으로 [[더 파일 (데이터셋)|더 파일]]과 같은 레이블이 없는 대규모 코퍼스이다. 사전 훈련 및 미세 조정을 위한 작업은 일반적으로 다음을 포함한다.
* [[언어 모델링]]<ref name=":6" />
* 다음 문장 예측<ref name=":6" />
* [[질의 응답]]<ref name=":7" />
* [[자연어 이해|독해]]
* [[감정 분석]]<ref name="2017_Attention_Is_All_You_Need" />
* [[텍스트 요약|다른 말로 표현하기]]<ref name="2017_Attention_Is_All_You_Need" />
[[T5 (언어 모델)|T5 트랜스포머]] 보고서<ref name=":0">{{서적 인용|last1=Raffel |first1=Colin |last2=Shazeer |first2=Noam |last3=Roberts |first3=Adam |last4=Lee |first4=Katherine |last5=Narang |first5=Sharan |last6=Matena |first6=Michael |last7=Zhou |first7=Yanqi |last8=Li |first8=Wei |last9=Liu |first9=Peter J. |date=2020-01-01 |title=Exploring the limits of transfer learning with a unified text-to-text transformer |url=https://dl.acm.org/doi/abs/10.5555/3455716.3455856 |journal=The Journal of Machine Learning Research |volume=21 |issue=1 |pages=140:5485–140:5551 |arxiv=1910.10683 |issn=1532-4435}}</ref>는 수많은 [[자연어]] 사전 훈련 작업을 문서화한다. 몇 가지 예는 다음과 같다.

* 불완전하거나 손상된 텍스트 복원 또는 수정. 예를 들어, 입력 "Thank you{{NNBSP|~~}}me to your party{{NNBSP|~~}}week"는 출력 "Thank you '''for inviting''' me to your party '''last''' week"를 생성할 수 있다.''
* 자연어 간 번역 ([[기계 번역]])
* 자연어의 실용적 허용 여부 판단. 예를 들어, 다음 문장은 문법적으로는 잘 형성되었지만 일반적인 인간의 사용에서는 가능성이 낮기 때문에 "허용되지 않음"으로 판단될 수 있다.<ref>{{ArXiv 인용| eprint=1910.10683 | last1=Raffel | first1=Colin | last2=Shazeer | first2=Noam | last3=Roberts | first3=Adam | last4=Lee | first4=Katherine | last5=Narang | first5=Sharan | last6=Matena | first6=Michael | last7=Zhou | first7=Yanqi | last8=Li | first8=Wei | last9=Liu | first9=Peter J. | title=Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer | date=2019 | class=cs.LG }}</ref> ''The course is jumping well.''

이러한 각 작업은 해당 언어의 원어민에게는 사소하거나 명백한 반면, 이전 세대의 기계 학습 아키텍처에서는 일반적으로 어려움을 겪었다는 점에 유의해야 한다.

=== 작업 ===
{{참고|대형 언어 모델#평가}}
일반적으로 언어 모델링 작업은 "마스크드",<ref name=":5">{{웹 인용|title=Masked language modeling |url=https://huggingface.co/docs/transformers/tasks/masked_language_modeling |access-date=2023-10-05 |website=huggingface.co}}</ref> "자기회귀",<ref name=":8">{{웹 인용|title=Causal language modeling |url=https://huggingface.co/docs/transformers/tasks/language_modeling |access-date=2023-10-05 |website=huggingface.co}}</ref> 및 "prefixLM"의 3가지 클래스로 나뉜다.<ref name=":4" /> 이러한 클래스는 트랜스포머와 같은 특정 모델링 아키텍처와는 독립적이지만, 트랜스포머의 맥락에서 종종 논의된다.

마스크드 작업에서,<ref name=":5" /> 하나 이상의 토큰이 마스킹되고 모델은 컨텍스트를 기반으로 마스킹된 토큰이 무엇인지 예측하는 확률 분포를 생성한다. 작업의 [[손실 함수]]는 일반적으로 마스킹된 토큰에 대한 [[퍼플렉시티|로그-퍼플렉시티]]의 합이다.<math display="block">\text{Loss} = -\sum_{t\in\text{masked tokens}}\ln(\text{probability of }t\text{ conditional on its context}) </math>그리고 모델은 이 손실 함수를 최소화하도록 훈련된다. [[BERT (언어 모델)|BERT 시리즈 모델]]은 마스크드 토큰 예측 및 다른 작업을 위해 훈련된다.

자기회귀 작업에서,<ref name=":8" /> 전체 시퀀스가 처음에는 마스킹되고 모델은 첫 번째 토큰에 대한 확률 분포를 생성한다. 그런 다음 첫 번째 토큰이 드러나고 모델은 두 번째 토큰을 예측하는 식으로 진행된다. 이 작업의 손실 함수는 여전히 일반적으로 동일하다. [[GPT (언어 모델)|GPT 시리즈 모델]]은 자기회귀 작업을 통해 훈련된다.

prefixLM 작업에서,<ref name=":4" /> 시퀀스는 두 부분으로 나뉜다. 첫 번째 부분은 컨텍스트로 제공되며, 모델은 두 번째 부분의 첫 번째 토큰을 예측한다. 그런 다음 해당 토큰이 드러나고, 모델은 두 번째 토큰을 예측하는 식으로 진행된다. 이 작업의 손실 함수는 여전히 일반적으로 동일하다. [[T5 (언어 모델)|T5 시리즈 모델]]은 prefixLM 작업을 통해 훈련된다.

"마스크드 언어 모델링"의 "마스크드"는 "[[#마스크드 어텐션|마스크드 어텐션]]"의 "마스크드"와 다르며, "prefixLM" (접두사 언어 모델링)은 [[#prefixLM|"prefixLM" (접두사 언어 모델)]]과 다르다는 점에 유의해야 한다.

== 아키텍처 ==
모든 트랜스포머는 동일한 주요 구성 요소를 가지고 있다.
* 토크나이저: 텍스트를 토큰으로 변환한다.
* 임베딩 레이어: 토큰과 토큰의 위치를 벡터 표현으로 변환한다.
* 트랜스포머 레이어: 벡터 표현에 반복적인 변환을 수행하여 점점 더 많은 언어 정보를 추출한다. 이들은 교대로 어텐션 및 순방향 레이어로 구성된다. 두 가지 주요 유형의 트랜스포머 레이어가 있으며, 더 많은 변형이 있다. 인코더 레이어와 디코더 레이어가 그것이다.
* 언임베딩 레이어: 최종 벡터 표현을 토큰에 대한 확률 분포로 다시 변환한다.
다음 설명은 원본 논문에 기술된 트랜스포머를 정확히 따른다. [[#후속 연구|다음 섹션]]에 설명된 변형도 있다.

관례적으로 모든 벡터를 행 벡터로 작성한다. 예를 들어, 벡터를 선형 레이어를 통해 밀어넣는 것은 <math>xW</math>와 같이 오른쪽에 가중치 행렬을 곱하는 것을 의미한다.

=== 토큰화 ===
{{본문|낱말 분석}}

트랜스포머 아키텍처는 기본적으로 텍스트가 아닌 숫자 데이터를 처리하므로 텍스트와 토큰 간의 변환이 필요하다. 토큰은 문자 또는 짧은 문자 세그먼트를 나타내는 정수이다. 입력 측에서 입력 텍스트는 토큰 시퀀스로 구문 분석된다. 마찬가지로 출력 측에서 출력 토큰은 다시 텍스트로 구문 분석된다. 텍스트와 토큰 시퀀스 간의 변환을 수행하는 모듈은 [[낱말 분석|토크나이저]]이다.

모든 토큰의 집합은 토크나이저의 어휘이며, 그 크기는 ''어휘 크기'' <math>n_{\text{vocabulary}}</math>이다. 어휘 외의 토큰에 직면했을 때는 일반적으로 "[UNK]"("알 수 없음")라는 특수 토큰이 사용된다.

일반적으로 사용되는 토크나이저로는 바이트 쌍 인코딩, WordPiece, SentencePiece 등이 있다.

=== 임베딩 ===
{{추가 정보|워드 임베딩}}
각 토큰은 [[순람표]]를 통해 임베딩 벡터로 변환된다. 동등하게 말하자면, 토큰의 [[원-핫]] 표현에 임베딩 행렬 <math>M</math>을 곱한다. 예를 들어, 입력 토큰이 <math>3</math>이라면 원-핫 표현은 <math>[0, 0, 0, 1, 0, 0, \dots]</math>이고, 그 임베딩 벡터는 다음과 같다.
<math display="block">\mathrm{Embed}(3) = [0, 0, 0, 1, 0, 0, \dots]M</math>
토큰 임베딩 벡터는 해당 위치 인코딩 벡터(아래 참조)에 추가되어 입력 벡터 시퀀스를 생성한다.

임베딩 벡터의 차원 수는 ''은닉 크기'' 또는 ''임베딩 크기''라고 불리며 <math>d_{\text{emb}}</math>로 표기된다.<ref name=":03"/> 이 크기는 원본 트랜스포머 논문에서 <math>d_{\text{model}}</math>로 표기된다.<ref name="2017_Attention_Is_All_You_Need" />

=== 언임베딩 ===
언임베딩 레이어는 임베딩 레이어의 거의 역이다. 임베딩 레이어가 토큰을 벡터로 변환하는 반면, 언임베딩 레이어는 벡터를 토큰에 대한 확률 분포로 변환한다.

언임베딩 레이어는 선형-[[소프트맥스 함수|소프트맥스]] 레이어이다.
<math display="block">\mathrm{UnEmbed}(x) = \mathrm{softmax}(xW + b)</math>
이 행렬의 형태는 <math>(d_{\text{emb}}, n_{\text{vocabulary}})</math>이다. 임베딩 행렬 <math>M</math>과 언임베딩 행렬 <math>W</math>는 때때로 서로의 전치 행렬이 되도록 요구되는데, 이를 가중치 연결이라고 한다.<ref>{{인용|last1=Press |first1=Ofir |title=Using the Output Embedding to Improve Language Models |date=2017-02-21 |arxiv=1608.05859 |last2=Wolf |first2=Lior}}</ref>

=== 위치 인코딩 ===
[[파일:Positional encoding.png|섬네일|매개변수 <math>N=10000, d=100</math>을 사용한 [[사인파|사인파형]] 위치 인코딩 다이어그램]]

위치 인코딩은 시퀀스 내 토큰의 상대적 위치를 고정된 크기의 벡터로 표현한 것이다. 이는 트랜스포머 모델에 입력 시퀀스에서 단어가 ''어디에'' 있는지에 대한 정보를 제공한다. 이는 입력 시퀀스 "[[man bites dog]]"가 "dog bites man"과 다르게 처리되도록 입력 시퀀스의 순서에 대한 [[귀납적 편향|편향]]을 유도한다.

위치 인코딩은 <math>f: \R \to \R^d; d \in \mathbb{Z}, d > 0</math> 유형의 함수로 정의되며, 여기서 <math>d</math>는 양의 짝수 [[정수]]이다. 원본 논문<ref name="2017_Attention_Is_All_You_Need" />에 정의된 전체 위치 인코딩은 다음과 같다.
<math display="block">(f(t)_{2k}, f(t)_{2k+1}) = (\sin(\theta), \cos(\theta)) \quad \forall k \in \{0, 1, \ldots, d/2 - 1\}</math>
여기서 <math>\theta = \frac{t}{r^k}, r = N^{2/d}</math>이다.

여기서 <math>N</math>은 위치 인코딩 함수에 입력될 수 있는 가장 큰 <math>k</math>보다 훨씬 커야 하는 자유 매개변수이다. 원본 논문은 <math>N=10000</math>을 사용한다.

이 함수는 <math>f: \R \to \mathbb C^{d/2}</math> 유형의 복소 함수로 작성될 때 더 간단한 형태를 가진다.
<math display="block">f(t) = \left(e^{it/r^k}\right)_{k=0, 1, \ldots, \frac d 2 - 1}</math>
여기서 <math>r = N^{2/d}</math>이다.

이 위치 인코딩 함수를 사용하는 주된 이유는 이를 사용하면 이동이 선형 변환이 되기 때문이다.
<math display="block">f(t + \Delta t) = \mathrm{diag}(f(\Delta t)) f(t)</math>
여기서 <math>\Delta t \in \R</math>는 이동하려는 거리이다. 이를 통해 트랜스포머는 인코딩된 모든 위치를 가져와 행렬 곱셈을 통해 n-단계 앞 또는 n-단계 뒤 위치의 인코딩을 찾을 수 있다.

선형 합을 취하면 모든 합성곱도 선형 변환으로 구현될 수 있다.
<math display="block">\sum_j c_j f(t + \Delta t_j) = \left(\sum_j c_j \,\mathrm{diag}(f(\Delta t_j))\right) f(t)</math>
어떤 상수 <math>c_j</math>에 대해서도 마찬가지이다. 이를 통해 트랜스포머는 인코딩된 모든 위치를 가져와 이웃의 인코딩된 위치의 선형 합을 찾을 수 있다. 인코딩된 위치의 이 합은 어텐션 메커니즘에 입력될 때, [[합성곱 신경망]] [[언어 모델]]에서 일어나는 것과 유사하게 이웃에 대한 어텐션 가중치를 생성한다. 저자의 말에 따르면, "이것은 모델이 상대적 위치에 따라 쉽게 어텐션하는 방법을 배울 수 있도록 할 것이라고 가정했다."

일반적인 구현에서는 모든 연산이 [[복소수]]가 아닌 실수에 대해 수행되지만, [[복소수#복소수의 행렬 표현|복소수 곱셈은 실수 2x2 행렬 곱셈으로 구현될 수 있기]] 때문에 이는 단순한 표기법 차이이다.

=== 인코더-디코더 (개요) ===
[[파일:Transformer,_one_encoder-decoder_block.png|섬네일|하나의 인코더-디코더 블록|220x220px]]
[[파일:Transformer,_stacked_layers_and_sublayers.png|섬네일|트랜스포머는 쌓인 인코더 레이어와 디코더 레이어로 구성된다.]]
이전 [[Seq2seq]] 모델과 마찬가지로, 원래 트랜스포머 모델은 '''인코더-디코더''' 아키텍처를 사용했다. 인코더는 모든 입력 토큰을 차례로 처리하는 인코딩 레이어로 구성되는 반면, 디코더는 인코더의 출력과 디코더의 지금까지의 출력 토큰을 반복적으로 처리하는 디코딩 레이어로 구성된다.

각 인코더 레이어의 목적은 토큰의 문맥화된 표현을 생성하는 것이다. 이 표현은 자체 어텐션 메커니즘을 통해 다른 입력 토큰의 정보를 "혼합"하는 토큰에 해당한다. 각 디코더 레이어는 두 개의 어텐션 서브레이어를 포함한다: (1) 인코더의 출력 (문맥화된 입력 토큰 표현)을 통합하기 위한 교차 어텐션, (2) 디코더의 입력 토큰 (즉, 추론 시간 동안 지금까지 생성된 토큰) 사이에서 정보를 "혼합"하기 위한 자체 어텐션.<ref>{{웹 인용|url=https://indico.io/blog/sequence-modeling-neural-networks-part2-attention-models/|title=Sequence Modeling with Neural Networks (Part 2): Attention Models|date=2016-04-18|website=Indico|access-date=2019-10-15|archive-date=2020-10-21|archive-url=https://web.archive.org/web/20201021203352/https://indico.io/blog/sequence-modeling-neural-networks-part2-attention-models/|url-status=live |last1=Lintz |first1=Nathan }}</ref><ref name=":1">{{웹 인용|last=Alammar |first=Jay |title=The Illustrated Transformer |url=http://jalammar.github.io/illustrated-transformer/ |url-status=live |archive-url=https://web.archive.org/web/20201018061610/https://jalammar.github.io/illustrated-transformer/ |archive-date=2020-10-18 |access-date=2019-10-15 |website=jalammar.github.io}}</ref>

인코더 및 디코더 레이어 모두 출력의 추가 처리를 위한 [[순방향 신경망]]을 가지며, 잔차 연결 및 레이어 정규화 단계를 포함한다.<ref name=":1" /> 이러한 순방향 레이어는 트랜스포머 모델의 매개변수 대부분을 포함한다.

=== 순방향 네트워크 ===
{{앵커|FFN|순방향 네트워크|순방향 모듈}}[[파일:Transformer architecture - FFN module.png|섬네일|순방향 네트워크 모듈. <math>d_{\text{emb}}</math> 차원 벡터를 <math>d_{\text{emb}}</math> 차원 벡터로 매핑하는 두 계층 네트워크이다.]]
트랜스포머의 순방향 네트워크 (FFN) 모듈은 2계층 [[다층 퍼셉트론]]이다.
<math display="block">\mathrm{FFN}(x) = \phi(xW^{(1)} + b^{(1)})W^{(2)} + b^{(2)}</math>
여기서 <math>W^{(1)}</math> 및 <math>W^{(2)}</math>는 가중치 행렬이고 <math>b^{(1)}</math> 및 <math>b^{(2)}</math>는 편향 벡터이며, <math>\phi</math>는 [[활성화 함수]]이다. 원래 트랜스포머는 [[ReLU]] 활성화를 사용했다.

중간 계층의 뉴런 수는 ''중간 크기'' (GPT),<ref>{{웹 인용|last=Team |first=Keras |title=Keras documentation: GPT2Backbone model |url=https://keras.io/api/keras_nlp/models/gpt2/gpt2_backbone/ |access-date=2024-08-08 |website=keras.io |language=en}}</ref> ''필터 크기'' (BERT),<ref name=":03" /> 또는 ''순방향 크기'' (BERT)라고 불린다.<ref name=":03" /> 일반적으로 임베딩 크기보다 크다. 예를 들어, GPT-2 시리즈와 BERT 시리즈 모두에서 모델의 중간 크기는 임베딩 크기의 4배이다. <math>d_{\text{ffn}} = 4 d_{\text{emb}}</math>.

=== 스케일드 점곱 어텐션 ===
{{본문|점곱 어텐션}}

==== 어텐션 헤드 ====
[[파일:Transformer,_attention_block_diagram.png|섬네일|스케일드 점곱 어텐션, 블록 다이어그램]]
[[파일:Transformer architecture - Attention Head module.png|섬네일|어텐션 헤드 모듈 내의 정확한 차원 수]]
트랜스포머 아키텍처에서 사용되는 어텐션 메커니즘은 스케일드 [[스칼라곱|점곱]] [[어텐션 (기계 학습)|어텐션]] 유닛이다. 각 유닛에 대해 트랜스포머 모델은 세 가지 가중치 행렬을 학습한다: 쿼리 가중치 <math>W^Q</math>, 키 가중치 <math>W^K</math>, 값 가중치 <math>W^V</math>.

이 모듈은 쿼리 시퀀스, 키 시퀀스, 값 시퀀스 세 가지 시퀀스를 입력으로 받는다. 쿼리 시퀀스는 길이 <math>\ell_{\text{seq, query}}</math>의 시퀀스이며, 각 항목은 차원 <math>d_{\text{emb, query}}</math>의 벡터이다. 키 및 값 시퀀스도 마찬가지이다.

쿼리 시퀀스의 각 벡터 <math>x_{i, \text{query}}</math>는 행렬 <math>W^Q</math>에 곱해져 쿼리 벡터 <math>q_i = x_{i, \text{query}} W^Q</math>를 생성한다. 모든 쿼리 벡터의 행렬은 쿼리 행렬이다.
<math display="block">Q = X_{\text{query}} W^Q</math>
마찬가지로 키 행렬 <math>K = X_{\text{key}} W^K</math>와 값 행렬 <math>V = X_{\text{value}} W^V</math>를 구성한다.

일반적으로 모든 <math>W^Q, W^K, W^V </math>는 정방 행렬이며, 이는 <math>d_{\text{emb, query}}= d_{\text{query}}</math> 등을 의미한다.

어텐션 가중치는 쿼리 및 키 벡터를 사용하여 계산된다. 토큰 <math>i</math>에서 토큰 <math>j</math>까지의 어텐션 가중치 <math>a_{ij}</math>는 <math>q_i</math>와 <math>k_j</math> 사이의 [[스칼라곱]]이다. 어텐션 가중치는 키 벡터의 차원인 <math>\sqrt{d_k}</math>의 제곱근으로 나뉘어 훈련 중 [[경사 하강법|기울기]]를 안정화하고, 가중치를 정규화하는 [[소프트맥스 함수|소프트맥스]]를 통해 전달된다. <math>W^Q</math>와 <math>W^K</math>가 다른 행렬이라는 사실은 어텐션이 비대칭일 수 있도록 한다. 토큰 <math>i</math>가 토큰 <math>j</math>에 어텐션한다면 (즉, <math>q_i\cdot k_j</math>가 크다면), 토큰 <math>j</math>가 토큰 <math>i</math>에 어텐션한다는 것을 반드시 의미하지는 않는다 (즉, <math>q_j\cdot k_i</math>는 작을 수 있다). 토큰 <math>i</math>에 대한 어텐션 단위의 출력은 모든 토큰의 값 벡터를 <math>a_{ij}</math> (토큰 <math>i</math>에서 각 토큰으로의 어텐션)로 가중 평균한 값이다.

모든 토큰에 대한 어텐션 계산은 [[소프트맥스 함수]]를 사용하여 하나의 큰 행렬 계산으로 표현할 수 있으며, 이는 행렬 연산 최적화를 통해 행렬 연산을 빠르게 계산할 수 있으므로 훈련에 유용하다. 행렬 <math>Q</math>, <math>K</math>, <math>V</math>는 각각 <math>q_i</math>, <math>k_i</math>, <math>v_i</math> 벡터를 행으로 하는 행렬로 정의된다. 그러면 어텐션을 다음과 같이 표현할 수 있다.
<math display="block">\begin{align}
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^\mathrm{T}}{\sqrt{d_k}}\right)V
\end{align}</math>

여기서 소프트맥스는 행렬의 각 행에 적용된다.

쿼리 벡터의 차원 수는 ''쿼리 크기'' <math>d_{\text{query}}</math>이고, 마찬가지로 ''키 크기'' <math>d_{\text{key}}</math> 및 ''값 크기'' <math>d_{\text{value}}</math>이다. 어텐션 헤드의 출력 차원은 ''헤드 차원'' <math>d_{\text{head}}</math>이다. 어텐션 메커니즘은 다음 세 가지 등식이 성립해야 한다.
<math display="block">\ell_{\text {seq, key}}=\ell_{\text {seq, value}}, \;d_{\text {query}}=d_{\text {key}}, \; d_{\text {value}}=d_{\text {head}}
</math>
그렇지 않으면 제약이 없다.

어텐션 헤드가 자체 어텐션 방식으로 사용되면 <math>X_{\text{query}} = X_{\text{key}} = X_{\text{value}} </math>이다. 어텐션 헤드가 교차 어텐션 방식으로 사용되면 일반적으로 <math>X_{\text{query}} \neq X_{\text{key}} = X_{\text{value}} </math>이다. 이론적으로는 세 가지 모두 다를 수 있지만, 실제로는 거의 그렇지 않다.

==== 멀티헤드 어텐션 ====
[[파일:Multiheaded_attention,_block_diagram.png|섬네일|멀티헤드 어텐션, 블록 다이어그램]]
[[파일:Transformer architecture - Multiheaded Attention module.png|섬네일|멀티헤드 어텐션 모듈 내의 정확한 차원 수]]
하나의 <math>\left( W^Q, W^K, W^V \right)</math> 행렬 세트를 ''어텐션 헤드''라고 하며, 트랜스포머 모델의 각 계층에는 여러 어텐션 헤드가 있다. 각 어텐션 헤드는 각 토큰과 관련된 토큰에 어텐션하는 반면, 여러 어텐션 헤드는 모델이 "관련성"에 대한 다른 정의에 대해 이를 수행할 수 있도록 한다. 특히, 어텐션 점수 계산에 관여하는 쿼리 및 키 투영 행렬인 <math>W^Q</math> 및 <math>W^K</math>는 "관련성"을 정의한다. 한편, 값 투영 행렬 <math>W^V</math>는 출력 투영 행렬 <math>W^O</math>의 부분과 결합하여 어텐션된 토큰이 후속 계층 및 궁극적으로 출력 로짓으로 전달되는 정보에 어떤 영향을 미치는지 결정한다. 또한, 어텐션의 범위, 즉 각 어텐션 헤드가 포착하는 토큰 관계의 범위는 토큰이 연속적인 계층을 통과함에 따라 확장될 수 있다. 이를 통해 모델은 더 깊은 계층에서 더 복잡하고 장거리 의존성을 포착할 수 있다. 많은 트랜스포머 어텐션 헤드는 인간에게 의미 있는 관련성 관계를 인코딩한다. 예를 들어, 일부 어텐션 헤드는 주로 다음 단어에 어텐션하는 반면, 다른 어텐션 헤드는 주로 동사에서 직접 목적어에 어텐션한다.<ref>{{서적 인용|last1=Clark|first1=Kevin |last2=Khandelwal|first2=Urvashi|last3=Levy|first3=Omer|last4=Manning|first4=Christopher D.|date=August 2019|title=What Does BERT Look at? An Analysis of BERT's Attention|url=https://www.aclweb.org/anthology/W19-4828|journal=Proceedings of the 2019 ACL Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP|location=Florence, Italy|publisher=Association for Computational Linguistics|pages=276–286|doi=10.18653/v1/W19-4828|doi-access=free|access-date=2020-05-20|archive-date=2020-10-21|archive-url=https://web.archive.org/web/20201021211357/https://www.aclweb.org/anthology/W19-4828/|url-status=live|arxiv=1906.04341}}</ref> 각 어텐션 헤드에 대한 계산은 [[병렬 컴퓨팅|병렬로]] 수행될 수 있어 빠른 처리가 가능하다. 어텐션 레이어의 출력은 [[순방향 신경망]] 레이어로 전달되기 위해 연결된다.

구체적으로, 여러 어텐션 헤드가 <math>i</math>로 인덱싱된다고 하자. 그러면 다음과 같다.
<math display="block">\text{MultiheadedAttention}(Q, K, V) = \text{Concat}_{i \in [n_{\text{heads}}]}(\text{Attention}(XW^Q_i, XW^K_i, XW^V_i)) W^O</math> 여기서 행렬 <math>X</math>는 단어 임베딩의 연결이고, 행렬 <math>W^Q_i, W^K_i, W^V_i</math>는 개별 어텐션 헤드 <math>i</math>가 소유하는 "투영 행렬"이며, <math>W^O</math>는 전체 멀티헤드 어텐션 헤드가 소유하는 최종 투영 행렬이다.

이론적으로 각 어텐션 헤드가 다른 헤드 차원 <math>d_{\text{head}}</math>를 가질 수 있지만, 실제로는 거의 그렇지 않다.

예를 들어, 가장 작은 GPT-2 모델에는 자체 어텐션 메커니즘만 있다. 이 모델은 다음과 같은 차원을 가진다.
<math display="block">d_{\text{emb}} = 768, n_{\text{head}} = 12, d_{\text{head}} = 64</math>
<math>12 \times 64 = 768</math>이므로, 출력 투영 행렬 <math>W^O \in \R^{(12 \times 64) \times 768}</math>는 정방 행렬이다.

==== 마스크드 어텐션 ====
트랜스포머 아키텍처는 출력 토큰을 반복적으로 계산하도록 구성된다. <math>t = 0</math>이 첫 번째 출력 토큰 <math>i = 0</math>의 계산을 나타낸다고 가정하면, 단계 <math>t > 0</math>에서 출력 토큰 <math>i = 0</math>은 상수로 유지되어야 한다. 이는 모델의 속성이 [[자기회귀모형|자기회귀 모델]]과 유사하도록 보장한다.<ref name="2017_Attention_Is_All_You_Need" /> 따라서 모든 시간 단계 <math>t</math>에서 모든 출력 <math>i</math>에 대한 계산은 <math>j >= i</math>인 위치 <math>j</math>의 토큰에 접근할 수 없어야 한다 (시간 단계 <math>t=i</math>의 경우 토큰 <math>j>t</math>는 아직 계산되지 않았으므로 당연하다). 이 동작은 소프트맥스 단계 전에 어텐션 링크를 끊어야 하는 항목에는 <math>-\infty</math>를, 다른 항목에는 <math>0</math>을 갖는 마스크 행렬 <math>M</math>을 추가하여 달성할 수 있다.
<math display="block">\begin{align}
\text{MaskedAttention}(Q, K, V) = \text{softmax}\left(M + \frac{QK^\mathrm{T}}{\sqrt{d_k}}\right)V
\end{align}</math> 다음 행렬은 디코더 자체 어텐션 모듈에서 일반적으로 사용되며 "인과적 마스킹"이라고 불린다.
<math display="block">M_{\text{causal}} = \begin{bmatrix}
0 & -\infty & -\infty & \dots  & -\infty \\
0 & 0 & -\infty & \dots  & -\infty \\
0 & 0 & 0 & \dots  & -\infty \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \dots  & 0
\end{bmatrix}
</math>

다시 말해, 각 토큰은 자신과 그 이전의 모든 토큰에 어텐션할 수 있지만, 그 이후의 토큰에는 어텐션할 수 없다. 마스크되지 않은 어텐션 모듈은 마스크의 모든 항목이 0인 마스크드 어텐션 모듈로 생각할 수 있다. 마스크 행렬의 흔치 않은 사용 예시로, [[XLNet]]은 <math>P M_{\text{causal}} P^{-1} </math> 형태의 모든 마스크를 고려하는데, 여기서 <math>P </math>는 무작위 [[치환행렬]]이다.<ref>{{서적 인용|last1=Yang |first1=Zhilin |last2=Dai |first2=Zihang |last3=Yang |first3=Yiming |last4=Carbonell |first4=Jaime |last5=Salakhutdinov |first5=Russ R |last6=Le |first6=Quoc V |date=2019 |title=XLNet: Generalized Autoregressive Pretraining for Language Understanding |url=https://proceedings.neurips.cc/paper/2019/hash/dc6a7e655d7e5840e66733e9ee67cc69-Abstract.html |journal=Advances in Neural Information Processing Systems |publisher=Curran Associates, Inc. |volume=32|arxiv=1906.08237 }}</ref>

=== 인코더 ===
[[파일:Transformer,_one_encoder_block.png|섬네일|하나의 인코더 레이어]]
인코더는 임베딩 레이어와 여러 인코더 레이어로 구성된다.

각 인코더 레이어는 자체 어텐션 메커니즘과 순방향 레이어의 두 가지 주요 구성 요소로 구성된다. 이 레이어는 입력 벡터 시퀀스를 입력으로 받아 자체 어텐션 메커니즘을 적용하여 중간 벡터 시퀀스를 생성한 다음, 각 벡터에 개별적으로 순방향 레이어를 적용한다. 개략적으로 다음과 같다.
<math>\begin{aligned}
\text{given input vectors } & h_0, h_1, \dots\\
\text{combine them into a matrix } H &= \begin{bmatrix} h_0 \\ h_1 \\ \vdots \end{bmatrix} \\
\text{EncoderLayer}(H) &= \begin{bmatrix} \text{FFN}(\text{MultiheadedAttention}(H, H, H)_0) \\ \text{FFN}(\text{MultiheadedAttention}(H, H, H)_1) \\ \vdots \end{bmatrix} \\

\end{aligned}</math>

여기서 <math>\text{FFN}</math>은 "순방향 네트워크"를 나타낸다. 이를 더 간결하게 다음과 같이 쓸 수 있다.
<math display="block">\text{EncoderLayer}(H) = \text{FFN}(\text{MultiheadedAttention}(H, H, H))
</math>
<math>\text{FFN}</math>은 행렬의 각 행에 개별적으로 적용된다는 암묵적인 관례가 있다.

인코더 레이어는 쌓여 있다. 첫 번째 인코더 레이어는 임베딩 레이어에서 입력 벡터 시퀀스를 받아 벡터 시퀀스를 생성한다. 이 벡터 시퀀스는 두 번째 인코더에 의해 처리되고, 이런 식으로 계속된다. 최종 인코더 레이어의 출력은 디코더에 의해 사용된다.

인코더가 전체 입력을 한 번에 처리하므로 모든 토큰은 다른 모든 토큰에 어텐션할 수 있으므로(모든 대 모든 어텐션) 인과적 마스킹이 필요 없다.

=== 디코더 ===
[[파일:Transformer,_one_decoder_block.png|섬네일|하나의 디코더 레이어]]
디코더는 임베딩 레이어, 여러 디코더 레이어, 그리고 언임베딩 레이어로 구성된다.

각 디코더는 세 가지 주요 구성 요소로 구성된다: 인과적으로 마스킹된 자체 어텐션 메커니즘, 교차 어텐션 메커니즘, 그리고 순방향 신경망이다. 디코더는 인코더와 유사하게 작동하지만, 인코더가 생성한 인코딩에서 관련 정보를 추출하는 추가적인 어텐션 메커니즘이 삽입된다. 이 메커니즘은 ''인코더-디코더 어텐션''이라고도 불린다.<ref name="2017_Attention_Is_All_You_Need" /><ref name=":1" />

첫 번째 인코더와 마찬가지로, 첫 번째 디코더는 인코딩 대신 출력 시퀀스의 위치 정보와 임베딩을 입력으로 받는다. 트랜스포머는 출력을 예측하기 위해 현재 또는 미래의 출력을 사용해서는 안 되므로, 이러한 역방향 정보 흐름을 방지하기 위해 출력 시퀀스를 부분적으로 마스킹해야 한다.<ref name="2017_Attention_Is_All_You_Need" /> 이를 통해 [[자기회귀모형|자기회귀]] 텍스트 생성이 가능하다. 디코딩의 경우, 토큰이 아직 생성되지 않았으므로 토큰이 아직 생성되지 않은 토큰에 어텐션할 수 없기 때문에 모든 대 모든 어텐션은 부적절하다. 따라서 디코더의 자체 어텐션 모듈은 인과적으로 마스킹된다.

대조적으로, 교차 어텐션 메커니즘은 디코더가 디코딩을 시작하기 전에 계산되는 인코더의 출력 벡터에 어텐션한다. 결과적으로 교차 어텐션 메커니즘에서는 마스킹이 필요 없다.

개략적으로 다음과 같다.
<math display="block">\begin{aligned}
H' &= \text{MaskedMultiheadedAttention}(H, H, H) \\
\text{DecoderLayer}(H) &=\text{FFN}(\text{MultiheadedAttention}(H', H^E, H^E))
\end{aligned}
</math>
여기서 <math>H^E</math>는 행이 인코더의 출력 벡터인 행렬이다.

마지막 디코더 뒤에는 최종 언임베딩 레이어가 이어져 어휘에 대한 출력 확률을 생성한다. 그런 다음 확률에 따라 토큰 중 하나가 샘플링되고, 디코더를 다시 실행하여 다음 토큰을 생성하는 방식으로 자기회귀적으로 출력 텍스트를 생성할 수 있다.

=== 수정된 아키텍처 ===

많은 [[대형 언어 모델]]은 입력 시퀀스로부터 완전히 새로운 시퀀스를 예측할 필요가 없으므로, 원래 트랜스포머 아키텍처의 인코더 또는 디코더만 사용한다. 초기 [[GPT (언어 모델)|GPT]] 모델은 시퀀스의 다음 토큰을 예측하도록 훈련된 디코더-온리 모델이다.<ref name="gpt1paper">{{웹 인용|url          = https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf
 |title        = Improving Language Understanding by Generative Pre-Training
 |last1        = Radford
 |first1       = Alec
 |last2        = Narasimhan
 |first2       = Karthik
 |last3        = Salimans
 |first3       = Tim
 |last4        = Sutskever
 |first4       = Ilya
 |page        = 12
 |publisher    = [[오픈AI]]
 |date         = 11 June 2018
 |access-date  = 23 January 2021
 |archive-date = 26 January 2021
 |archive-url  = https://web.archive.org/web/20210126024542/https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf
 |url-status   = live}}</ref> 다른 언어 모델인 [[BERT (언어 모델)|BERT]]는 인코더만 사용하며, 시퀀스에서 무작위로 마스킹된 토큰을 예측하도록 훈련된다.<ref name=":03"/>

== 전체 트랜스포머 아키텍처 ==

=== 서브레이어 ===
[[파일:Transformer,_stacked_multilayers.png|섬네일|(a) 하나의 인코더 레이어와 하나의 디코더 레이어. (b) 두 개의 인코더 레이어와 두 개의 디코더 레이어. 서브레이어도 레이블이 지정되어 있다.]]각 인코더 레이어는 자체 어텐션과 순방향 네트워크의 2개의 서브레이어를 포함한다. 각 디코더 레이어는 인과적으로 마스킹된 자체 어텐션, 교차 어텐션, 순방향 네트워크의 3개의 서브레이어를 포함한다.
[[파일:Transformer_encoder,_with_norm-first_and_norm-last.png|섬네일|노름 우선 및 노름 마지막이 있는 트랜스포머 인코더]]
[[파일:Transformer_decoder,_with_norm-first_and_norm-last.png|섬네일|노름 우선 및 노름 마지막이 있는 트랜스포머 디코더]]
[[파일:Transformer,_full_architecture.png|섬네일|전체 트랜스포머 아키텍처의 블록 다이어그램]][[파일:Transformer,_schematic_object_hierarchy,_for_implementation_in_object-oriented_programming.png|섬네일|[[객체 지향 프로그래밍]] 스타일로 구현하기 위한 전체 트랜스포머 아키텍처의 개략적인 [[객체 계층]] 구조]]마지막 세부 사항은 [[잔차 신경망|잔차 연결]]과 [[레이어 정규화]] (LayerNorm, 또는 LN)인데, 개념적으로는 불필요하지만 수치적 안정성과 수렴을 위해 필요하다.

소실 경사 문제를 피하고 훈련 과정을 안정화하기 위해 도입된 잔차 연결은 y = F(x) + x로 표현될 수 있다. 이 표현은 출력 y가 입력 x의 변환(F(x))과 입력 자체(x)의 합임을 나타낸다. 입력 x를 추가하면 입력 정보를 보존하고 F(x)의 경사가 거의 0에 가까울 때 발생하는 문제를 피할 수 있다.

순방향 네트워크 모듈이 각 벡터에 개별적으로 적용되는 것과 유사하게, 레이어 정규화(LayerNorm)도 각 벡터에 개별적으로 적용된다.

{{앵커|Pre-LN}}두 가지 일반적인 컨벤션이 사용된다: ''Post-LN''과 ''Pre-LN'' 컨벤션. Post-LN 컨벤션에서 각 서브레이어의 출력은 다음과 같다.
<math display="block">\mathrm{LayerNorm}(x + \mathrm{Sublayer}(x))</math>
여기서 <math>\mathrm{Sublayer}(x)</math>는 서브레이어 자체에서 구현된 함수이다.

Pre-LN 컨벤션에서 각 서브레이어의 출력은 다음과 같다.
<math display="block">x + \mathrm{Sublayer}(\mathrm{LayerNorm}(x))</math>
원래 2017년 트랜스포머는 Post-LN 컨벤션을 사용했다. 이는 훈련하기 어려웠고 신중한 [[하이퍼파라미터 (기계 학습)|하이퍼파라미터]] 튜닝과 학습률의 "웜업"이 필요했는데, 이는 학습률이 작게 시작하여 점진적으로 증가하는 방식이었다. 2018년에 여러 차례 제안된 Pre-LN 컨벤션은<ref>{{인용|last1=Wang |first1=Qiang |title=Learning Deep Transformer Models for Machine Translation |date=2019-06-04 |arxiv=1906.01787 |last2=Li |first2=Bei |last3=Xiao |first3=Tong |last4=Zhu |first4=Jingbo |last5=Li |first5=Changliang |last6=Wong |first6=Derek F. |last7=Chao |first7=Lidia S.}}</ref> 웜업이 필요 없이 훈련하기 더 쉽고 더 빠른 수렴을 이끌어낸다는 것이 밝혀졌다.<ref name="auto1" />

=== 의사 코드 ===
다음은 표준 Pre-LN 인코더-디코더 트랜스포머의 의사 코드이며<ref>{{인용|last1=Phuong |first1=Mary |title=Formal Algorithms for Transformers |date=2022-07-19 |arxiv=2207.09238 |last2=Hutter |first2=Marcus}}</ref>에서 발췌했다.
 '''입력:''' 인코더 입력 t_e
        디코더 입력 t_d
 '''출력:''' 확률 분포 배열 (디코더 어휘 크기 x 디코더 출력 시퀀스 길이)

 /* 인코더 */
 z_e ← encoder.tokenizer(t_e)

 '''각''' t '''에 대해''' 1:length(z_e) '''반복'''
     z_e[t] ← encoder.embedding(z_e[t]) + encoder.positional_embedding(t)

 '''각''' l '''에 대해''' 1:length(encoder.layers) '''반복'''
     layer ← encoder.layers[l]

     /* 첫 번째 서브레이어 */
     z_e_copy ← copy(z_e)
     '''각''' t '''에 대해''' 1:length(z_e) '''반복'''
         z_e[t] ← layer.layer_norm(z_e[t])
     z_e ← layer.multiheaded_attention(z_e, z_e, z_e)
     '''각''' t '''에 대해''' 1:length(z_e) '''반복'''
         z_e[t] ← z_e[t] + z_e_copy[t]

     /* 두 번째 서브레이어 */
     z_e_copy ← copy(z_e)
     '''각''' t '''에 대해''' 1:length(z_e) '''반복'''
         z_e[t] ← layer.layer_norm(z_e[t])
     z_e ← layer.feedforward(z_e)
     '''각''' t '''에 대해''' 1:length(z_e) '''반복'''
         z_e[t] ← z_e[t] + z_e_copy[t]

 '''각''' t '''에 대해''' 1:length(z_e) '''반복'''
     z_e[t] ← encoder.final_layer_norm(z_e[t])

 /* 디코더 */
 z_d ← decoder.tokenizer(t_d)

 '''각''' t '''에 대해''' 1:length(z_d) '''반복'''
     z_d[t] ← decoder.embedding(z_d[t]) + decoder.positional_embedding(t)

 '''각''' l '''에 대해''' 1:length(decoder.layers) '''반복'''
         layer ← decoder.layers[l]

         /* 첫 번째 서브레이어 */
         z_d_copy ← copy(z_d)
         '''각''' t '''에 대해''' 1:length(z_d) '''반복'''
             z_d[t] ← layer.layer_norm(z_d[t])
         z_d ← layer.masked_multiheaded_attention(z_d, z_d, z_d)
         '''각''' t '''에 대해''' 1:length(z_d) '''반복'''
             z_d[t] ← z_d[t] + z_d_copy[t]

         /* 두 번째 서브레이어 */
         z_d_copy ← copy(z_d)
         '''각''' t '''에 대해''' 1:length(z_d) '''반복'''
             z_d[t] ← layer.layer_norm(z_d[t])
         z_d ← layer.multiheaded_attention(z_d, z_e, z_e)
         '''각''' i '''에 대해''' 1:length(z_d) '''반복'''
             z_d[t] ← z_d[t] + z_d_copy[t]

         /* 세 번째 서브레이어 */
         z_d_copy ← copy(z_d)
         '''각''' t '''에 대해''' 1:length(z_d) '''반복'''
             z_d[t] ← layer.layer_norm(z_d[t])
         z_d ← layer.feedforward(z_d)
         '''각''' t '''에 대해''' 1:length(z_d) '''반복'''
             z_d[t] ← z_d[t] + z_d_copy[t]

 z_d ← decoder.final_layer_norm(z_d)

 output_distributions ← []
 '''각''' t '''에 대해''' 1:length(z_d) '''반복'''
     output_distributions.append(decoder.unembed(z_d[t]))

 '''return''' output_distributions

=== 용어 ===
트랜스포머 아키텍처는 모듈화되어 다양한 변형을 허용한다. 몇 가지 일반적인 변형이 여기에 설명되어 있다.<ref name=":3">{{서적 인용|last1=Raffel |first1=Colin |last2=Shazeer |first2=Noam |last3=Roberts |first3=Adam |last4=Lee |first4=Katherine |last5=Narang |first5=Sharan |last6=Matena |first6=Michael |last7=Zhou |first7=Yanqi |last8=Li |first8=Wei |last9=Liu |first9=Peter J. |date=2020 |title=Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer |url=http://jmlr.org/papers/v21/20-074.html |journal=Journal of Machine Learning Research |volume=21 |issue=140 |pages=1–67 |arxiv=1910.10683 |issn=1533-7928}}</ref>

{{앵커|encoder-only}}"인코더-온리" 트랜스포머는 인코더를 적용하여 입력 텍스트를 입력 텍스트를 나타내는 벡터 시퀀스로 매핑한다. 이는 일반적으로 텍스트 임베딩 및 후속 애플리케이션을 위한 [[특징 학습|표현 학습]]에 사용된다. [[BERT (언어 모델)|BERT]]는 인코더-온리이다. 인코더-디코더 트랜스포머를 훈련한 다음 인코더만 사용하는 것보다 훨씬 좋지 않다는 것이 밝혀졌으므로 현재는 덜 사용된다.<ref name=":4" />

{{앵커|decoder-only}}"디코더-온리" 트랜스포머는 문자 그대로 디코더-온리가 아니다. 인코더가 없으면 교차 어텐션 메커니즘은 어텐션할 대상이 없다. 따라서 디코더-온리 트랜스포머의 디코더 레이어는 인과적으로 마스킹된 자체 어텐션과 순방향 네트워크라는 두 개의 서브레이어로만 구성된다. 이는 일반적으로 [[자연어 생성|텍스트 생성]] 및 [[대형 언어 모델#명령 튜닝|명령 따르기]]에 사용된다. [[GPT (언어 모델)|GPT 시리즈]] 및 [[친칠라 (언어 모델)|친칠라 시리즈]]의 모델은 디코더-온리이다.

{{앵커|encoder-decoder}}"인코더-디코더" 트랜스포머는 일반적으로 원본 트랜스포머와 동일하며, 각 인코더 레이어당 2개의 서브레이어와 각 디코더 레이어당 3개의 서브레이어 등이 있다. [[#대체 활성화 함수|대체 활성화 함수]], [[#Pre-LN|정규화 위치 변경]] 등과 같은 사소한 아키텍처 개선 사항이 있을 수 있다. 이는 일반적으로 텍스트 생성 및 명령 따르기에도 사용된다. [[T5 (언어 모델)|T5 시리즈]]의 모델은 인코더-디코더이다.<ref name=":3" />

{{앵커|prefixLM}}"prefixLM" (접두사 언어 모델)은 디코더 전용 아키텍처이지만, 인과적 마스킹과 다른 접두사 마스킹을 사용한다.<ref name=":3" />{{참고 쪽|location=그림 3}}<math display="block">M_{\text{prefixLM}} = \begin{bmatrix}
\mathbf{0} &  -\infty \\
\mathbf{0} & M_{\text{causal}}
\end{bmatrix}
</math>
여기서 첫 번째 열은 "접두사"에 해당하고, 이어지는 열은 접두사를 기반으로 자기회귀적으로 생성된 텍스트에 해당한다. 이는 인코더-디코더 모델과 유사하지만 "희소성"이 적다. 이러한 모델은 이론적 가능성 및 벤치마크 비교로 인용되기는 하지만 거의 사용되지 않는다.<ref name=":4">{{인용|last1=Tay |first1=Yi |title=UL2: Unifying Language Learning Paradigms |date=2023-02-28 |arxiv=2205.05131 |last2=Dehghani |first2=Mostafa |last3=Tran |first3=Vinh Q. |last4=Garcia |first4=Xavier |last5=Wei |first5=Jason |last6=Wang |first6=Xuezhi |last7=Chung |first7=Hyung Won |last8=Shakeri |first8=Siamak |last9=Bahri |first9=Dara}}</ref>

혼합형 seq2seq 모델도 있다. 예를 들어, 2020년 구글 번역은 RNN-디코더가 자기회귀적으로 실행될 때 트랜스포머-디코더보다 훨씬 빠르게 실행된다는 주장에 따라 이전 RNN-인코더-RNN-디코더 모델을 트랜스포머-인코더-RNN-디코더 모델로 교체했다.<ref>{{웹 인용|date=June 8, 2020 |title=Recent Advances in Google Translate |url=http://research.google/blog/recent-advances-in-google-translate/ |url-status=live |archive-url=https://web.archive.org/web/20240704042433/https://research.google/blog/recent-advances-in-google-translate/ |archive-date=4 Jul 2024 |access-date=2024-08-07 |website=Google Research |language=en}}</ref>

== 후속 연구 ==
=== 대체 활성화 함수 ===
원래 트랜스포머는 [[ReLU]] [[활성화 함수]]를 사용한다. 다른 활성화 함수들이 개발되었다. [[LLaMA|라마 시리즈]]와 [[PaLM]]은 SwiGLU를 사용했고;<ref name=":14">{{ArXiv 인용|eprint=2002.05202 |class=cs.LG |first=Noam |last=Shazeer |title=GLU Variants Improve Transformer |date=2020-02-01}}</ref> GPT-1과 BERT<ref name=":03" /> 모두 GELU를 사용했다.<ref>{{ArXiv 인용|last1=Hendrycks |first1=Dan |last2=Gimpel |first2=Kevin |date=2016-06-27 |title=Gaussian Error Linear Units (GELUs) |class=cs.LG |eprint=1606.08415v5 |language=en}}</ref>

대체 활성화 함수는 순방향 모듈에서 [[게이트 선형 단위]]와 함께 사용되는 경우가 많다.<ref name=":14" />

=== 대체 정규화 ===
트랜스포머에 사용되는 정규화는 레이어 정규화(LayerNorm)와 다를 수 있다. 한 가지 예는 [[LLaMA|라마 시리즈]]에서 사용되는 [[RMSNorm]]이다.<ref>{{서적 인용|last1=Zhang |first1=Biao |last2=Sennrich |first2=Rico |date=2019 |title=Root Mean Square Layer Normalization |url=https://proceedings.neurips.cc/paper/2019/hash/1e8a19426224ca89e83cef47f1e7f53b-Abstract.html |journal=Advances in Neural Information Processing Systems |publisher=Curran Associates, Inc. |volume=32|arxiv=1910.07467 }}</ref> 다른 예로는 CapsuleNorm<ref>Tembine, Hamidou, Manzoor Ahmed Khan, and Issa Bamia. 2024. "Mean-Field-Type Transformers" Mathematics 12, no. 22: 3506. https://doi.org/10.3390/math12223506</ref> ScaleNorm,<ref name=":9">{{서적 인용|last1=Nguyen |first1=Toan Q. |last2=Salazar |first2=Julian |date=2019-11-02 |editor-last=Niehues |editor-first=Jan |editor2-last=Cattoni |editor2-first=Rolando |editor3-last=Stüker |editor3-first=Sebastian |editor4-last=Negri |editor4-first=Matteo |editor5-last=Turchi |editor5-first=Marco |editor6-last=Ha |editor6-first=Thanh-Le |editor7-last=Salesky |editor7-first=Elizabeth |editor8-last=Sanabria |editor8-first=Ramon |editor9-last=Barrault |editor9-first=Loic |title=Transformers without Tears: Improving the Normalization of Self-Attention |url=https://aclanthology.org/2019.iwslt-1.17 |journal=Proceedings of the 16th International Conference on Spoken Language Translation |location=Hong Kong |publisher=Association for Computational Linguistics|doi=10.5281/zenodo.3525484 |arxiv=1910.05895 }}</ref> 또는 FixNorm.<ref name=":9" />

=== 대체 위치 인코딩 ===
트랜스포머는 사인파형 외에 다른 위치 인코딩 방법을 사용할 수 있다.<ref>{{서적 인용|last1=Dufter |first1=Philipp |last2=Schmitt |first2=Martin |last3=Schütze |first3=Hinrich |date=2022-06-06 |title=Position Information in Transformers: An Overview |journal=Computational Linguistics |volume=48 |issue=3 |pages=733–763 |doi=10.1162/coli_a_00445 |issn=0891-2017 |s2cid=231986066 |doi-access=free|arxiv=2102.11090 }}</ref>

원래 트랜스포머 논문에서는 학습된 위치 인코딩을 사용했다고 보고했지만,<ref>{{서적 인용|last1=Gehring |first1=Jonas |last2=Auli |first2=Michael |last3=Grangier |first3=David |last4=Yarats |first4=Denis |last5=Dauphin |first5=Yann N. |date=2017-07-17 |title=Convolutional Sequence to Sequence Learning |url=https://proceedings.mlr.press/v70/gehring17a.html |journal=Proceedings of the 34th International Conference on Machine Learning |language=en |publisher=PMLR |pages=1243–1252}}</ref> 사인파형 인코딩보다 우수하지 않다는 것을 발견했다.<ref name="2017_Attention_Is_All_You_Need" /> 이후,<ref>{{인용|last1=Haviv |first1=Adi |title=Transformer Language Models without Positional Encodings Still Learn Positional Information |date=2022-12-05 |arxiv=2203.16634 |last2=Ram |first2=Ori |last3=Press |first3=Ofir |last4=Izsak |first4=Peter |last5=Levy |first5=Omer}}</ref>는 인과적 마스킹 자체가 트랜스포머 디코더에 충분한 신호를 제공하여 위치 인코딩 모듈 없이도 절대 위치 인코딩을 암시적으로 수행할 수 있음을 발견했다.

==== RoPE ====
{{앵커|Rotary positional embedding}}RoPE (회전 위치 임베딩)<ref>{{ArXiv 인용|last1=Su |first1=Jianlin |last2=Lu |first2=Yu |last3=Pan |first3=Shengfeng |last4=Murtadha |first4=Ahmed |last5=Wen |first5=Bo |last6=Liu |first6=Yunfeng |date=2021-04-01 |title=RoFormer: Enhanced Transformer with Rotary Position Embedding |class=cs.CL |eprint=2104.09864 }}</ref>는 2차원 벡터 목록 <math>[(x^{(1)}_1, x^{(2)}_1), (x^{(1)}_2, x^{(2)}_2), (x^{(1)}_3, x^{(2)}_3), ...]</math>를 고려하면 가장 잘 설명된다. 이제 어떤 각도 <math>\theta</math>를 선택한다. 그러면 RoPE 인코딩은 다음과 같다.
<math display="block">\text{RoPE}\big(x^{(1)}_m, x^{(2)}_m, m\big) =
\begin{pmatrix}    \cos m \theta & - \sin m \theta \\
\sin m \theta & \cos m \theta    \end{pmatrix}
\begin{pmatrix}    x^{(1)}_m \\    x^{(2)}_m \\    \end{pmatrix}  =    \begin{pmatrix}    x^{(1)}_m \cos m\theta - x^{(2)}_m \sin m \theta \\    x^{(2)}_m \cos m\theta + x^{(1)}_m \sin m \theta \\    \end{pmatrix}
</math>
동등하게, 2차원 벡터를 복소수 <math>z_m := x^{(1)}_m + i x^{(2)}_m</math>로 작성하면, RoPE 인코딩은 단순히 각도 곱셈이다.
<math display="block">\text{RoPE}\big(z_m, m\big) = e^{i m\theta} z_m
</math>
<math>2n</math>차원 벡터 목록의 경우, RoPE 인코더는 각도 시퀀스 <math>\theta^{(1)}, ..., \theta^{(n)}</math>에 의해 정의된다. 그러면 RoPE 인코딩은 각 좌표 쌍에 적용된다.

RoPE의 이점은 두 벡터 간의 점곱이 상대적 위치에만 의존한다는 것이다.
<math display="block">
\text{RoPE}\big(x, m\big)^T\text{RoPE}\big(y, n\big)
=
\text{RoPE}\big(x, m+k\big)^T\text{RoPE}\big(y, n+k\big)
</math>
어떤 정수 <math>k</math>에 대해서도 마찬가지이다.

==== ALiBi ====
ALiBi (Attention with Linear Biases)<ref>{{ArXiv 인용|last1=Press |first1=Ofir |last2=Smith |first2=Noah A. |last3=Lewis |first3=Mike |date=2021-08-01 |title=Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation |class=cs.CL |eprint=2108.12409 }}</ref>는 원래 트랜스포머의 위치 인코더를 ''대체하는'' 것이 아니다. 대신, 어텐션 메커니즘에 직접 연결되는 ''추가적인'' 위치 인코더이다. 구체적으로, ALiBi 어텐션 메커니즘은 다음과 같다.
<math display="block">\begin{align}
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^\mathrm{T}}{\sqrt{d_k}} + s B\right)V
\end{align}</math>
여기서 <math>s</math>는 실수("스칼라")이고, <math>B</math>는 다음과 같이 정의되는 ''선형 편향'' 행렬이다.
<math display="block">B = \begin{pmatrix}
0 & 1 & 2 & 3 & \cdots \\
-1 & 0 & 1 & 2 & \cdots \\
-2 & -1 & 0 & 1 & \cdots \\
-3 & -2 & -1 & 0 & \cdots \\
\vdots & \vdots & \vdots & \vdots & \ddots \\
\end{pmatrix}
</math>
다른 말로, <math>B_{i, j} = j - i</math>이다. 선형 편향 행렬은 부드러운 마스크라는 아이디어이다. <math>0</math>은 완전한 어텐션을 나타내고, <math>-\infty</math>는 어텐션을 나타내지 않는 것처럼, 선형 편향 행렬은 한 방향으로는 어텐션을 증가시키고 다른 방향으로는 어텐션을 감소시킨다.

ALiBi는 짧은 컨텍스트 창에서 사전 훈련한 다음, 더 긴 컨텍스트 창에서 미세 조정하는 것을 가능하게 한다. 어텐션 메커니즘에 직접 연결되기 때문에 전체 네트워크의 "바닥"에 연결되는 모든 위치 인코더 (원본 트랜스포머의 사인파 인코더, RoPE 및 기타 여러 가지)와 결합할 수 있다.

==== 상대 위치 인코딩 ====
상대 위치 인코딩<ref>{{ArXiv 인용|last1=Shaw |first1=Peter |last2=Uszkoreit |first2=Jakob |last3=Vaswani |first3=Ashish |date=2018 |title=Self-Attention with Relative Position Representations |class=cs.CL |eprint=1803.02155}}</ref>은 ALiBi와 유사하지만 더 일반적이다.
<math display="block">\begin{align}
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^\mathrm{T}}{\sqrt{d_k}} + B\right)V
\end{align}</math>
여기서 <math>B</math>는 [[퇴플리츠 행렬]]이며, 즉 <math>i-j = i'-j'</math>일 때마다 <math>B_{i, j} = B_{i', j'}</math>이다. 이는 "절대 위치 인코딩"인 원래의 사인파 위치 인코딩과 대조된다.<ref>{{인용|last1=Ke |first1=Guolin |title=Rethinking Positional Encoding in Language Pre-training |date=2021-03-15 |arxiv=2006.15595 |last2=He |first2=Di |last3=Liu |first3=Tie-Yan}}</ref>

=== 효율적인 구현 ===
트랜스포머 모델은 [[텐서플로]] 및 [[PyTorch]]와 같은 표준 [[프레임워크 (컴퓨터 과학)|딥 러닝 프레임워크]]에 구현되었다. ''트랜스포머''는 [[허깅 페이스]]가 개발한 라이브러리로, 트랜스포머 기반 아키텍처와 사전 훈련된 모델을 제공한다.<ref name="wolf2020" />

==== KV 캐싱 ====
자기회귀 트랜스포머가 텍스트 생성과 같은 추론에 사용될 때, 쿼리 벡터는 각 단계에서 다르지만, 이미 계산된 키 및 값 벡터는 항상 동일하다. '''KV 캐싱''' 방법은 각 어텐션 블록에서 계산된 키 및 값 벡터를 저장하여 각 새 토큰에서 다시 계산되지 않도록 한다. '''PagedAttention'''은 KV 캐싱에 [[페이징|메모리 페이징]]을 적용한다.<ref>{{서적 인용|last1=Kwon |first1=Woosuk |last2=Li |first2=Zhuohan |last3=Zhuang |first3=Siyuan |last4=Sheng |first4=Ying |last5=Zheng |first5=Lianmin |last6=Yu |first6=Cody Hao |last7=Gonzalez |first7=Joseph |last8=Zhang |first8=Hao |last9=Stoica |first9=Ion |date=2023-10-23 |publisher=Association for Computing Machinery |isbn=979-8-4007-0229-7 |series=SOSP '23 |location=New York, NY, USA |pages=611–626 |chapter=Efficient Memory Management for Large Language Model Serving with PagedAttention |doi=10.1145/3600006.3613165 |chapter-url=https://dl.acm.org/doi/10.1145/3600006.3613165 |arxiv=2309.06180}}</ref><ref>{{인용|title=vllm-project/vllm |date=2024-06-20 |url=https://github.com/vllm-project/vllm |access-date=2024-06-20 |publisher=vLLM}}</ref><ref>{{웹 인용|last=Contribution) |first=Woosuk Kwon*, Zhuohan Li*, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Yu, Joey Gonzalez, Hao Zhang, and Ion Stoica (* Equal |date=2023-06-20 |title=vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention |url=https://blog.vllm.ai/2023/06/20/vllm.html |access-date=2024-06-20 |website=vLLM Blog |language=en}}</ref>

["당신은 고객 지원 상담원입니다..."]와 같이 내장된 프롬프트와 함께 트랜스포머가 사용되는 경우, 프롬프트에 대한 키 및 값 벡터를 계산하고 디스크에 저장할 수 있다. 모델이 온라인 챗봇과 같이 많은 짧은 상호 작용에 사용될 때 계산 절약은 상당하다.

==== FlashAttention ====
FlashAttention<ref>{{서적 인용|last1=Dao |first1=Tri |last2=Fu |first2=Dan |last3=Ermon |first3=Stefano |last4=Rudra |first4=Atri |last5=Ré |first5=Christopher |date=2022-12-06 |title=FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness |url=https://proceedings.neurips.cc/paper_files/paper/2022/hash/67d57c32e20fd0a7a302cb81d36e40d5-Abstract-Conference.html |journal=Advances in Neural Information Processing Systems |volume=35 |pages=16344–16359|arxiv=2205.14135}}</ref>는 GPU에서 트랜스포머 어텐션 메커니즘을 효율적으로 구현하는 알고리즘이다. 이는 [[블록 행렬#블록 행렬 연산|블록 단위로 행렬 곱셈]]을 수행하여 각 블록이 GPU의 [[캐시]] 내에 맞도록 하고, 블록을 신중하게 관리하여 GPU 캐시 간의 데이터 복사를 최소화하는 (데이터 이동이 느리기 때문에) 통신 회피 알고리즘이다. 자세한 내용은 [[소프트맥스 함수#수치 알고리즘|소프트맥스]] 페이지를 참조한다.

개선된 버전인 FlashAttention-2<ref>{{웹 인용|title=Stanford CRFM |url=https://crfm.stanford.edu/2023/07/17/flash2.html |access-date=2023-07-18 |website=crfm.stanford.edu}}</ref><ref>{{웹 인용|date=2023-06-17 |title=FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning |url=https://princeton-nlp.github.io/flash-atttention-2/ |access-date=2023-07-18 |website=Princeton NLP }}</ref><ref>{{웹 인용|title=Introducing Together AI Chief Scientist Tri Dao, as he releases FlashAttention-2 to speed up model training and inference |url=https://together.ai/blog/tri-dao-flash-attention |access-date=2023-07-18 |website=TOGETHER }}</ref>는 더 긴 컨텍스트 길이를 처리할 수 있는 언어 모델에 대한 증가하는 수요를 충족시키기 위해 개발되었다. 작업 분할 및 병렬 처리 개선을 제공하여 [[Nvidia A100|A100]] GPU ([[FP16]]/[[BF16]])에서 최대 230 TFLOPs/s를 달성하여 원래 FlashAttention보다 2배 빠른 속도를 제공한다.

FlashAttention-2의 주요 발전 사항은 비-행렬 곱셈 FLOPS 감소, 시퀀스 길이 차원에 대한 병렬 처리 개선, GPU 워프 간의 더 나은 작업 분할, 그리고 최대 256의 헤드 차원과 멀티 쿼리 어텐션(MQA) 및 그룹 쿼리 어텐션(GQA)에 대한 추가 지원을 포함한다.<ref>{{ArXiv 인용|last1=Ainslie |first1=Joshua |title=GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints |date=2023-12-23 |eprint=2305.13245 |last2=Lee-Thorp |first2=James |last3=de Jong |first3=Michiel |last4=Zemlyanskiy |first4=Yury |last5=Lebrón |first5=Federico |last6=Sanghai |first6=Sumit|class=cs.CL }}</ref>

벤치마크 결과 FlashAttention-2는 FlashAttention보다 최대 2배 빠르고 PyTorch의 표준 어텐션 구현보다 최대 9배 빠르다. 향후 개발에는 [[Nvidia H100|H100]] GPU와 FP8과 같은 새로운 데이터 유형과 같은 새로운 하드웨어에 대한 최적화가 포함된다.

==== 멀티 쿼리 어텐션 ====
{{앵커|멀티 쿼리 어텐션|그룹 쿼리 어텐션}}
[[파일:DeepSeek KV cache comparison between MHA, GQA, MQA, MLA.svg|섬네일|몇 가지 다른 어텐션 메커니즘 형태와 각 형태에 필요한 KV 캐싱 양의 비교]]
멀티 쿼리 어텐션은 멀티헤드 어텐션 메커니즘을 변경한다.<ref>{{ArXiv 인용|last1=Chowdhery |first1=Aakanksha |last2=Narang |first2=Sharan |last3=Devlin |first3=Jacob |last4=Bosma |first4=Maarten |last5=Mishra |first5=Gaurav |last6=Roberts |first6=Adam |last7=Barham |first7=Paul |last8=Chung |first8=Hyung Won |last9=Sutton |first9=Charles |last10=Gehrmann |first10=Sebastian |last11=Schuh |first11=Parker |last12=Shi |first12=Kensen |last13=Tsvyashchenko |first13=Sasha |last14=Maynez |first14=Joshua |last15=Rao |first15=Abhishek |date=2022-04-01 |title=PaLM: Scaling Language Modeling with Pathways |class=cs.CL |eprint=2204.02311 }}</ref> 보통은 다음과 같지만,

<math display="block">\text{MultiheadedAttention}(Q, K, V) = \text{Concat}_{i \in [n_{\text{heads}}]}\left(\text{Attention}(XW^Q_i, XW^K_i, XW^V_i)\right) W^O</math>
멀티 쿼리 어텐션에서는 <math>W^K, W^V</math>가 하나만 있으므로 다음과 같다.

<math display="block">\text{MultiQueryAttention}(Q, K, V) = \text{Concat}_{i \in [n_{\text{heads}}]}\left(\text{Attention}(XW^Q_i, XW^K, XW^V)\right) W^O</math>

이는 모델 품질과 훈련 속도에 중립적인 영향을 미치지만, 추론 속도를 향상시킨다.

더 일반적으로, 그룹 쿼리 어텐션(GQA)은 어텐션 헤드를 그룹으로 나누며, 각 그룹은 키-값 쌍을 공유한다. MQA는 그룹이 하나인 GQA이고, 표준 멀티헤드 어텐션은 그룹 수가 최대인 GQA이다.<ref>{{인용|last1=Ainslie |first1=Joshua |title=GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints |date=2023-12-23 |arxiv=2305.13245 |last2=Lee-Thorp |first2=James |last3=de Jong |first3=Michiel |last4=Zemlyanskiy |first4=Yury |last5=Lebrón |first5=Federico |last6=Sanghai |first6=Sumit}}</ref>
[[파일:DeepSeek_MoE_and_MLA_(DeepSeek-V2).svg|섬네일|V2 아키텍처, MLA와 [[전문가 혼합]] 변형을 모두 보여준다.<ref name=":73">{{인용|author1=DeepSeek-AI |title=DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model |date=19 June 2024 |arxiv=2405.04434 |last2=Liu |first2=Aixin |last3=Feng |first3=Bei |last4=Wang |first4=Bin |last5=Wang |first5=Bingxuan |last6=Liu |first6=Bo |last7=Zhao |first7=Chenggang |last8=Dengr |first8=Chengqi |last9=Ruan |first9=Chong}}.</ref>{{참고 쪽|location=그림 2}}]]
{{앵커|MLA|멀티헤드 잠재 어텐션}}
멀티헤드 잠재 어텐션(MLA)은 표준 MHA의 [[저계수 근사]]이다. 구체적으로, 각 은닉 벡터는 어텐션 메커니즘에 들어가기 전에 먼저 두 개의 저차원 공간("잠재 공간")으로 투영되는데, 하나는 쿼리용이고 다른 하나는 키-값(KV 벡터)용이다. 이 설계는 KV 캐시를 최소화한다. 왜냐하면 저차원 KV 벡터만 캐시하면 되기 때문이다.<ref name=":73" />

==== 추론적 디코딩 ====
추론적 디코딩<ref name=":2">{{인용|last1=Leviathan |first1=Yaniv |title=Fast Inference from Transformers via Speculative Decoding |date=2023-05-18 |arxiv=2211.17192 |last2=Kalman |first2=Matan |last3=Matias |first3=Yossi}}</ref><ref>{{웹 인용|url=https://yaofu.notion.site/Towards-100x-Speedup-Full-Stack-Transformer-Inference-Optimization-43124c3688e14cffaf2f1d6cbdf26c6c|title=Towards 100x Speedup: Full Stack Transformer Inference Optimization|first=Yao|last=Fu|date=2023-12-13}}</ref>은 토큰 디코딩 속도를 높이는 방법이다. [[투기적 실행|CPU의 투기적 실행]]과 유사하게, 미래 토큰은 빠르게 계산된 다음 검증된다. 빠르게 계산된 토큰이 부정확하면 폐기되고 느리게 다시 계산된다.

추론적 디코딩의 핵심은 트랜스포머 디코더가 다음과 같은 의미에서 디코딩하는 것보다 더 빠르게 검증할 수 있다는 점이다.

GPT-3 및 GPT-3-small과 같이 컨텍스트 창 크기가 512인 두 개의 트랜스포머 모델이 있다고 가정하자. GPT-3로 전체 컨텍스트 창을 탐욕적 디코딩으로 자기회귀적으로 생성하려면, 각 토큰 <math>x_1, x_2, ..., x_{512}</math>를 생성할 때마다 512번 실행되어야 하며, 총 시간은 <math>512 T_{\text{GPT-3}}</math>가 걸린다. 그러나 이러한 토큰 값에 대해 교육받은 추측이 있다면, 모델을 한 번 실행하여 모든 토큰을 병렬로 검증할 수 있다. 각 <math>x_t</math>가 실제로 <math>t</math>번째 출력에서 가장 큰 로그 우도(log-likelihood)를 가진 토큰인지 확인하는 것이다.

추론적 디코딩에서는 더 작은 모델이나 다른 간단한 휴리스틱을 사용하여 몇 개의 추론적 토큰을 생성한 다음 더 큰 모델에 의해 검증된다. 예를 들어, GPT-3-small을 사용하여 네 개의 추론적 토큰 <math>\tilde{x}_1, \tilde{x}_2, \tilde{x}_3, \tilde{x}_4</math>를 생성한다고 가정하자. 이는 <math>4 T_{\text{GPT-3-small}}</math>만 소요된다. 이 토큰들은 더 큰 GPT-3를 통해 한 번에 실행된다. <math>\tilde{x}_1</math>과 <math>\tilde{x}_2</math>가 GPT-3에 의해 선택될 것이라고 확인되면 이들은 유지되지만, <math>\tilde{x}_3</math>은 그렇지 않으므로 <math>\tilde{x}_3, \tilde{x}_4</math>는 폐기되고, GPT-3는 이들에 대해 실행된다. 이 경우 <math>4 T_{\text{GPT-3-small}} + 3 T_{\text{GPT-3}}</math>가 소요되며, 이는 <math>4 T_{\text{GPT-3}}</math>보다 짧을 수 있다.

비탐욕적 디코딩의 경우, 유사한 아이디어가 적용되지만, 추론적 토큰은 확률적으로 수용되거나 거부되며, 이는 최종 출력 분포가 추론적 디코딩을 사용하지 않은 경우와 동일하도록 보장하는 방식으로 이루어진다.<ref name=":2" /><ref>{{인용|last1=Chen |first1=Charlie |title=Accelerating Large Language Model Decoding with Speculative Sampling |date=2023-02-02 |arxiv=2302.01318 |last2=Borgeaud |first2=Sebastian |last3=Irving |first3=Geoffrey |last4=Lespiau |first4=Jean-Baptiste |last5=Sifre |first5=Laurent |last6=Jumper |first6=John}}</ref>
[[파일:Multi-Token Prediction (DeepSeek) 01.svg|섬네일|멀티 토큰 예측]]
{{앵커|멀티 토큰 예측}}멀티 토큰 예측에서 단일 순방향 패스는 최종 임베딩 벡터를 생성하며, 이 벡터는 다시 토큰 확률로 언임베딩된다. 그러나 이 벡터는 다른 트랜스포머 블록에 의해 추가로 처리되어 다음 토큰을 예측할 수 있으며, 미래의 임의의 많은 단계에 대해 이러한 방식으로 계속될 수 있다. 이는 각 새 토큰이 전체 스택이 아닌 단 하나의 트랜스포머 블록만 비용을 지불하므로 정확도를 속도와 교환하는 것이다.<ref>{{ArXiv 인용|eprint=2404.19737 |last1=Gloeckle |first1=Fabian |author2=Badr Youbi Idrissi |last3=Rozière |first3=Baptiste |last4=Lopez-Paz |first4=David |last5=Synnaeve |first5=Gabriel |title=Better & Faster Large Language Models via Multi-token Prediction |date=2024 |class=cs.CL }}</ref><ref>{{ArXiv 인용|eprint=2412.19437 |author1=DeepSeek-AI |last2=Liu |first2=Aixin |last3=Feng |first3=Bei |last4=Xue |first4=Bing |last5=Wang |first5=Bingxuan |last6=Wu |first6=Bochao |last7=Lu |first7=Chengda |last8=Zhao |first8=Chenggang |last9=Deng |first9=Chengqi |last10=Zhang |first10=Chenyu |last11=Ruan |first11=Chong |last12=Dai |first12=Damai |last13=Guo |first13=Daya |last14=Yang |first14=Dejian |last15=Chen |first15=Deli |last16=Ji |first16=Dongjie |last17=Li |first17=Erhang |last18=Lin |first18=Fangyun |last19=Dai |first19=Fucong |last20=Luo |first20=Fuli |last21=Hao |first21=Guangbo |last22=Chen |first22=Guanting |last23=Li |first23=Guowei |last24=Zhang |first24=H. |last25=Bao |first25=Han |last26=Xu |first26=Hanwei |last27=Wang |first27=Haocheng |last28=Zhang |first28=Haowei |last29=Ding |first29=Honghui |last30=Xin |first30=Huajian |title=DeepSeek-V3 Technical Report |date=2024 |class=cs.CL |display-authors=1 }}</ref>

=== 이차 미만 트랜스포머 ===
트랜스포머 기반 아키텍처 훈련은 특히 긴 입력의 경우 비용이 많이 들 수 있다.<ref name="reformer">{{ArXiv 인용|eprint=2001.04451 |class=cs.LG |first1=Nikita |last1=Kitaev |first2=Łukasz |last2=Kaiser |title=Reformer: The Efficient Transformer |last3=Levskaya |first3=Anselm |year=2020}}</ref> 이 문제를 해결하기 위해 많은 방법이 개발되었다. 이미지 도메인에서 Swin Transformer는 이동 창 내에서 어텐션을 수행하는 효율적인 아키텍처이다.<ref>{{서적 인용|last1=Liu |first1=Ze |last2=Lin |first2=Yutong |last3=Cao |first3=Yue |last4=Hu |first4=Han |last5=Wei |first5=Yixuan |last6=Zhang |first6=Zheng |last7=Lin |first7=Stephen |last8=Guo |first8=Baining |chapter=Swin Transformer: Hierarchical Vision Transformer using Shifted Windows |year=2021 |title=2021 IEEE/CVF International Conference on Computer Vision (ICCV) |chapter-url=https://ieeexplore.ieee.org/document/9710580 |publisher=IEEE |pages=9992–10002 |doi=10.1109/ICCV48922.2021.00986 |isbn=978-1-6654-2812-5|arxiv=2103.14030 }}</ref> 오디오 도메인에서 SepTr은 시간 및 주파수 도메인에서 어텐션을 분리한다.<ref>{{서적 인용|last1=Ristea |first1=Nicolaea Catalin |last2=Ionescu |first2=Radu Tudor |last3=Khan |first3=Fahad Shahbaz |date=2022-09-18 |title=SepTr: Separable Transformer for Audio Spectrogram Processing |url=https://www.isca-archive.org/interspeech_2022/ristea22_interspeech.html |journal=Interspeech |language=en |publisher=ISCA |pages=4103–4107 |doi=10.21437/Interspeech.2022-249|arxiv=2203.09581 }}</ref> ''Long Range Arena'' (2020)<ref>{{ArXiv 인용|eprint=2011.04006 |class=cs.LG |first1=Yi |last1=Tay |first2=Mostafa |last2=Dehghani |title=Long Range Arena: A Benchmark for Efficient Transformers |date=2020-11-08 |last3=Abnar |first3=Samira |last4=Shen |first4=Yikang |last5=Bahri |first5=Dara |last6=Pham |first6=Philip |last7=Rao |first7=Jinfeng |last8=Yang |first8=Liu |last9=Ruder |first9=Sebastian |last10=Metzler |first10=Donald}}</ref>는 긴 입력에 대한 트랜스포머 아키텍처의 동작을 비교하는 표준 벤치마크이다.

==== 대체 어텐션 그래프 ====
표준 어텐션 그래프는 모든 대 모든 또는 인과적이며, 둘 다 <math>N</math>이 시퀀스의 토큰 수일 때 <math>O(N^2)</math>로 스케일링된다.

리포머 (2020)<ref name="reformer" /><ref>{{웹 인용|date=16 January 2020 |title=Reformer: The Efficient Transformer |url=http://ai.googleblog.com/2020/01/reformer-efficient-transformer.html |url-status=live |archive-url=https://web.archive.org/web/20201022210019/https://ai.googleblog.com/2020/01/reformer-efficient-transformer.html |archive-date=2020-10-22 |access-date=2020-10-22 |website=Google AI Blog}}</ref>는 [[지역 민감 해싱]]과 가역 계층을 사용하여 계산 부하를 <math>O(N^2)</math>에서 <math>O(N\ln N)</math>으로 줄인다.<ref>{{서적 인용|last1=Gomez |first1=Aidan N |last2=Ren |first2=Mengye |last3=Urtasun |first3=Raquel |last4=Grosse |first4=Roger B |date=2017 |title=The Reversible Residual Network: Backpropagation Without Storing Activations |url=https://proceedings.neurips.cc/paper/2017/hash/f9be311e65d81a9ad8150a60844bb94c-Abstract.html |journal=Advances in Neural Information Processing Systems |publisher=Curran Associates, Inc. |volume=30|arxiv=1707.04585 }}</ref>

희소 어텐션<ref>{{인용|last1=Child |first1=Rewon |title=Generating Long Sequences with Sparse Transformers |date=2019-04-23 |arxiv=1904.10509 |last2=Gray |first2=Scott |last3=Radford |first3=Alec |last4=Sutskever |first4=Ilya}}</ref>은 <math>O(N^2)</math>보다 느리게 증가하는 어텐션 그래프를 사용한다. 예를 들어, BigBird (2020)<ref>{{웹 인용|date=25 March 2021 |title=Constructing Transformers For Longer Sequences with Sparse Attention Methods |url=https://ai.googleblog.com/2021/03/constructing-transformers-for-longer.html |url-status=live |archive-url=https://web.archive.org/web/20210918150757/https://ai.googleblog.com/2021/03/constructing-transformers-for-longer.html |archive-date=2021-09-18 |access-date=2021-05-28 |website=Google AI Blog}}</ref>는 <math>O(N)</math>로 증가하는 무작위 [[작은 세상 네트워크]]를 사용한다.

일반 트랜스포머는 컨텍스트 창 크기에 대해 이차적인 메모리 크기를 필요로 한다. 어텐션이 없는 트랜스포머<ref>{{ArXiv 인용|eprint=2105.14103 |class=cs.LG |first1=Shuangfei |last1=Zhai |first2=Walter |last2=Talbott |title=An Attention Free Transformer |date=2021-09-21 |last3=Srivastava |first3=Nitish |last4=Huang |first4=Chen |last5=Goh |first5=Hanlin |last6=Zhang |first6=Ruixiang |last7=Susskind |first7=Josh}}</ref>는 키를 값에 연결하여 이를 선형 종속성으로 줄이면서도 트랜스포머의 장점을 유지한다.

==== 랜덤 특징 어텐션 ====
랜덤 특징 어텐션(Random Feature Attention) (2021)<ref>{{ArXiv 인용|last1=Peng |first1=Hao |last2=Pappas |first2=Nikolaos |last3=Yogatama |first3=Dani |last4=Schwartz |first4=Roy |last5=Smith |first5=Noah A. |last6=Kong |first6=Lingpeng |date=2021-03-19 |title=Random Feature Attention |class=cs.CL |eprint=2103.02143}}</ref>은 [[방사형 기저 함수 핵#푸리에 랜덤 특징|푸리에 랜덤 특징]]을 사용한다.
<math display="block">\varphi(x) = \frac{1}{\sqrt D}[\cos\langle w_1, x\rangle, \sin\langle w_1, x\rangle, \cdots \cos\langle w_D, x\rangle, \sin\langle w_D, x\rangle]^T</math>
여기서 <math>w_1, ..., w_D</math>는 정규 분포 <math>N(0, \sigma^2 I)</math>에서 독립적으로 샘플링된 것이다. 이러한 매개변수 선택은 <math>\mathbb E[\langle \varphi(x), \varphi(y)\rangle] = e^{-\frac{\|x-y\|^2}{2\sigma^2}}</math> 또는 다음과 같이 만족한다.
<math display="block">e^{\langle x, y\rangle/\sigma^2} = \mathbb E[\langle e^{\|x\|^2/2\sigma^2} \varphi(x), e^{\|y\|^2/2\sigma^2}\varphi(y)\rangle] \approx \langle e^{\|x\|^2/2\sigma^2} \varphi(x), e^{\|y\|^2/2\sigma^2}\varphi(y)\rangle </math>
결과적으로, 하나의 쿼리를 가진 단일 헤드 어텐션은 다음과 같이 쓸 수 있다.
<math display="block">
\text{Attention}(q, K, V) = \text{softmax}\left(\frac{qK^\mathrm{T}}{\sqrt{d_k}}\right)V

\approx \frac{\varphi(q)^T \sum_i e^{\|k_i\|^2/2\sigma^2}\varphi(k_i) v_i^T}{\varphi(q)^T \sum_i e^{\|k_i\|^2/2\sigma^2}\varphi(k_i)}</math>
여기서 <math>\sigma = d_K^{1/4}</math>이다. 여러 쿼리 및 멀티헤드 어텐션도 마찬가지이다.

이 근사치는 선형 시간으로 계산될 수 있는데, 이는 행렬 <math>\varphi(k_i) v_i^T</math>를 먼저 계산한 다음 쿼리와 곱할 수 있기 때문이다. 본질적으로 다음과 같은 더 정확한 버전을 얻을 수 있었다.
<math display="block">\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^\mathrm{T}}{\sqrt{d_k}}\right)V \approx Q(K^TV/\sqrt{d_k})
</math>
퍼포머(Performer) (2022)<ref>{{ArXiv 인용|last1=Choromanski |first1=Krzysztof |last2=Likhosherstov |first2=Valerii |last3=Dohan |first3=David |last4=Song |first4=Xingyou |last5=Gane |first5=Andreea |last6=Sarlos |first6=Tamas |last7=Hawkins |first7=Peter |last8=Davis |first8=Jared |last9=Belanger |first9=David |last10=Colwell |first10=Lucy |last11=Weller |first11=Adrian |date=2020-09-30 |title=Masked Language Modeling for Proteins via Linearly Scalable Long-Context Transformers |class=cs.LG |eprint=2006.03555}}</ref>는 동일한 랜덤 특징 어텐션을 사용하지만, <math>w_1, ..., w_D</math>는 먼저 정규 분포 <math>N(0, \sigma^2 I)</math>에서 독립적으로 샘플링된 다음, [[그람-슈미트 과정|그람-슈미트 처리]]된다.

=== 멀티모달리티 ===
트랜스포머는 텍스트를 넘어선 모달리티(입력 또는 출력)에도 사용/적용될 수 있으며, 일반적으로 모달리티를 "토큰화"하는 방법을 찾는 방식으로 이루어진다.

멀티모달 모델은 처음부터 훈련되거나 미세 조정을 통해 훈련될 수 있다. 2022년 연구에서는 자연어만으로 사전 훈련된 트랜스포머를 매개변수의 0.03%만으로 미세 조정하여 다양한 논리 및 시각 작업에서 LSTM과 경쟁할 수 있음을 발견하여 [[전이학습]]을 입증했다.<ref>{{서적 인용|last1=Lu |first1=Kevin |last2=Grover |first2=Aditya |last3=Abbeel |first3=Pieter |last4=Mordatch |first4=Igor |date=2022-06-28 |title=Frozen Pretrained Transformers as Universal Computation Engines |url=https://ojs.aaai.org/index.php/AAAI/article/view/20729 |journal=Proceedings of the AAAI Conference on Artificial Intelligence |language=en |volume=36 |issue=7 |pages=7628–7636 |doi=10.1609/aaai.v36i7.20729 |issn=2374-3468|doi-access=free }}</ref> LLaVA는 언어 모델(Vicuna-13B)<ref>{{웹 인용|title=Vicuna: An Open-Source Chatbot Impressing GPT-4 with 90%* ChatGPT Quality {{!}} LMSYS Org |url=https://lmsys.org/blog/2023-03-30-vicuna |access-date=2024-08-11 |website=lmsys.org |language=en}}</ref>과 비전 모델([[비전 트랜스포머|ViT]]-L/14)로 구성된 시각-언어 모델이며, 선형 계층으로 연결된다. 선형 계층만 미세 조정된다.<ref>{{서적 인용|last1=Liu |first1=Haotian |last2=Li |first2=Chunyuan |last3=Wu |first3=Qingyang |last4=Lee |first4=Yong Jae |date=2023-12-15 |title=Visual Instruction Tuning |url=https://proceedings.neurips.cc/paper_files/paper/2023/hash/6dcf277ea32ce3288914faf369fe6de0-Abstract-Conference.html |journal=Advances in Neural Information Processing Systems |language=en |volume=36 |pages=34892–34916}}</ref>

[[비전 트랜스포머]]<ref name="auto2" />는 입력 이미지를 일련의 패치로 분해하고, 이를 벡터로 변환하여 표준 트랜스포머의 토큰처럼 처리함으로써 트랜스포머를 컴퓨터 비전에 적용한다.

컨포머(Conformer)<ref name="Gulati2020">{{ArXiv 인용|eprint=2005.08100 |first1=Anmol |last1=Gulati |first2=James |last2=Qin |title=Conformer: Convolution-augmented Transformer for Speech Recognition |last3=Chiu |first3=Chung-Cheng |last4=Parmar |first4=Niki |last5=Zhang |first5=Yu |last6=Yu |last7=Han |first7=Wei |last8=Wang |first8=Shibo |last9=Zhang |first9=Zhengdong |last10=Wu |first10=Yonghui |last11=Pang |first11=Ruoming |year=2020 |page=|class=eess.AS }}</ref>와 이후의 [[휘스퍼 (음성 인식 시스템)|휘스퍼]]<ref name="Radford Kim Xu Brockman p.">{{ArXiv 인용|eprint=2212.04356 |first1=Alec |last1=Radford |first2=Jong Wook |last2=Kim |title=Robust Speech Recognition via Large-Scale Weak Supervision |last3=Xu |first3=Tao |last4=Brockman |first4=Greg |last5=McLeavey |first5=Christine |last6=Sutskever |first6=Ilya |year=2022 |page=|class=eess.AS }}</ref>는 [[음성 인식]]에 대해 동일한 패턴을 따르며, 먼저 음성 신호를 [[스펙트로그램]]으로 변환한 다음, 이를 이미지처럼 처리한다. 즉, 일련의 패치로 분해하고 벡터로 변환하여 표준 트랜스포머의 토큰처럼 처리한다.

[[퍼시버]]<ref name="perceiver2021">{{ArXiv 인용|eprint=2103.03206 |class=cs.CV |first1=Andrew |last1=Jaegle |first2=Felix |last2=Gimeno |title=Perceiver: General Perception with Iterative Attention |date=2021-06-22 |last3=Brock |first3=Andrew |last4=Zisserman |first4=Andrew |last5=Vinyals |first5=Oriol |last6=Carreira |first6=Joao}}</ref><ref name="jaegle2021b">{{ArXiv 인용|eprint=2107.14795 |class=cs.LG |first1=Andrew |last1=Jaegle |first2=Sebastian |last2=Borgeaud |title=Perceiver IO: A General Architecture for Structured Inputs & Outputs |date=2021-08-02 |last3=Alayrac |first3=Jean-Baptiste |last4=Doersch |first4=Carl |last5=Ionescu |first5=Catalin |last6=Ding |first6=David |last7=Koppula |first7=Skanda |last8=Zoran |first8=Daniel |last9=Brock |first9=Andrew |last10=Shelhamer |first10=Evan |last11=Hénaff |first11=Olivier}}</ref>는 멀티모달리티를 위해 설계된 트랜스포머의 변형이다.

이미지 생성을 위한 주목할 만한 아키텍처로는 [[DALL-E|DALL-E 1]] (2021), Parti (2022),<ref>{{웹 인용|title=Parti: Pathways Autoregressive Text-to-Image Model |url=https://sites.research.google/parti/ |access-date=2024-08-09 |website=sites.research.google}}</ref> Phenaki (2023),<ref name=":13">{{서적 인용|last1=Villegas |first1=Ruben |last2=Babaeizadeh |first2=Mohammad |last3=Kindermans |first3=Pieter-Jan |last4=Moraldo |first4=Hernan |last5=Zhang |first5=Han |last6=Saffar |first6=Mohammad Taghi |last7=Castro |first7=Santiago |last8=Kunze |first8=Julius |last9=Erhan |first9=Dumitru |date=2022-09-29 |title=Phenaki: Variable Length Video Generation from Open Domain Textual Descriptions |url=https://openreview.net/forum?id=vOEXS39nOF |language=en}}</ref> 및 Muse (2023)가 있다.<ref name=":12">{{ArXiv 인용|last1=Chang |first1=Huiwen |title=Muse: Text-To-Image Generation via Masked Generative Transformers |date=2023-01-02 |eprint=2301.00704 |last2=Zhang |first2=Han |last3=Barber |first3=Jarred |last4=Maschinot |first4=A. J. |last5=Lezama |first5=Jose |last6=Jiang |first6=Lu |last7=Yang |first7=Ming-Hsuan |last8=Murphy |first8=Kevin |last9=Freeman |first9=William T.|class=cs.CV }}</ref> 이후 모델과 달리 DALL-E는 확산 모델이 아니다. 대신, 자기회귀적으로 텍스트를 생성한 다음 이미지의 토큰 표현으로 변환하고, 이를 [[변분 오토인코더]]로 이미지로 변환하는 디코더-온리 트랜스포머를 사용한다.<ref>{{인용|last1=Ramesh |first1=Aditya |title=Zero-Shot Text-to-Image Generation |date=2021-02-26 |arxiv=2102.12092 |last2=Pavlov |first2=Mikhail |last3=Goh |first3=Gabriel |last4=Gray |first4=Scott |last5=Voss |first5=Chelsea |last6=Radford |first6=Alec |last7=Chen |first7=Mark |last8=Sutskever |first8=Ilya}}</ref> Parti는 인코더-디코더 트랜스포머로, 인코더는 텍스트 프롬프트를 처리하고 디코더는 이미지의 토큰 표현을 생성한다.<ref>{{인용|last1=Yu |first1=Jiahui |title=Scaling Autoregressive Models for Content-Rich Text-to-Image Generation |date=2022-06-21 |arxiv=2206.10789 |last2=Xu |first2=Yuanzhong |last3=Koh |first3=Jing Yu |last4=Luong |first4=Thang |last5=Baid |first5=Gunjan |last6=Wang |first6=Zirui |last7=Vasudevan |first7=Vijay |last8=Ku |first8=Alexander |last9=Yang |first9=Yinfei}}</ref> Muse는 마스킹되지 않은 이미지 토큰으로부터 마스킹된 이미지 토큰을 예측하도록 훈련된 인코더-온리 트랜스포머이다. 생성 중에 모든 입력 토큰은 마스킹되며, 가장 높은 신뢰도의 예측은 다음 반복에 포함되어 모든 토큰이 예측될 때까지 계속된다.<ref name=":12" /> Phenaki는 텍스트-비디오 모델이다. 이는 사전 계산된 텍스트 토큰을 조건으로 하는 양방향 마스크드 트랜스포머이다. 생성된 토큰은 비디오로 디코딩된다.<ref name=":13" />

== 응용 분야 ==
트랜스포머는 [[자연어 처리]] (NLP) 분야에서 큰 성공을 거두었다. [[GPT-2]], [[GPT-3]], [[GPT-4]], [[제미나이 (챗봇)|제미나이]], AlbertAGPT, [[앤트로픽#클로드|클로드]], [[BERT (언어 모델)|BERT]], [[Grok|그록]], [[XLNet]], [[BERT (언어 모델)#RoBERTa|RoBERTa]] 및 [[챗GPT]]와 같은 많은 [[대형 언어 모델]]은 다양한 NLP 관련 하위 작업 및 관련 실제 응용 프로그램에서 트랜스포머의 능력을 보여주었다. 다음을 포함한다.
* [[기계 번역]]
* [[시계열]] 예측
* [[자동 요약|문서 요약]]
* [[자연어 생성|문서 생성]]
* [[개체명 인식]] (NER)<ref>{{서적 인용|last1=Kariampuzha |first1=William |last2=Alyea |first2=Gioconda |last3=Qu |first3=Sue |last4=Sanjak |first4=Jaleal |last5=Mathé |first5=Ewy |last6=Sid |first6=Eric |last7=Chatelaine |first7=Haley |last8=Yadaw |first8=Arjun |last9=Xu |first9=Yanji |last10=Zhu |first10=Qian |date=2023 |title=Precision information extraction for rare disease epidemiology at scale |journal=Journal of Translational Medicine |volume=21 |issue=1 |page=157 |doi=10.1186/s12967-023-04011-y |pmc=9972634 |pmid=36855134 |doi-access=free}}</ref>
* 자연어로 표현된 요구 사항을 기반으로 [[컴퓨터 프로그래밍|컴퓨터 코드 작성]].
* [[음성 인식]]

전통적인 NLP 외에도 트랜스포머 아키텍처는 다음과 같은 다른 응용 분야에서 성공을 거두었다.
* [[서열 분석|생물학적 서열 분석]]
* [[컴퓨터 비전|비디오 이해]]
* [[단백질 구조 예측]] ([[알파폴드]] 등)
* 체스판 위치 [[평가 함수|평가]]. 정적 평가만 사용했을 때 (즉, [[최소극대화]] 탐색 없이) 트랜스포머는 [[엘로 평점 시스템|엘로]] 2895점을 달성하여 [[그랜드마스터 (체스)|그랜드마스터]] 수준에 도달했다.<ref name="grandmaster" />

== 같이 보기 ==
* {{주석 달린 링크|Seq2seq}}
* {{주석 달린 링크|퍼시버}}
* {{주석 달린 링크|비전 트랜스포머}}
* {{주석 달린 링크|대형 언어 모델}}
* {{주석 달린 링크|BERT (언어 모델)}}
* {{주석 달린 링크|GPT (언어 모델)}}
* {{주석 달린 링크|T5 (언어 모델)}}

== 참고 문헌 ==
{{참고 자료 시작}}
* Alexander Rush, [https://nlp.seas.harvard.edu/2018/04/03/attention.html The Annotated transformer] {{웹아카이브|url=https://web.archive.org/web/20210922093841/https://nlp.seas.harvard.edu/2018/04/03/attention.html |date=2021-09-22 }}, Harvard NLP group, 3 April 2018
* {{ArXiv 인용|last1=Phuong |first1=Mary |last2=Hutter |first2=Marcus |title=Formal Algorithms for Transformers |date=2022 |class=cs.LG |eprint=2207.09238 }}
* {{ArXiv 인용|last1=Ferrando |first1=Javier |title=A Primer on the Inner Workings of Transformer-based Language Models |date=2024-05-01 |eprint=2405.00208 |last2=Sarti |first2=Gabriele |last3=Bisazza |first3=Arianna |last4=Costa-jussà |first4=Marta R.|class=cs.CL }}
* {{웹 인용|title=Transformer++ |first=Gavin|last=Leech|url=https://www.gleech.org/tplus |date=2024-11-06|archive-url=https://web.archive.org/web/20250226110336/https://www.gleech.org/tplus|archive-date=2025-02-26|access-date=2025-05-08 |website=argmin gravitas}}
<!-- * Hubert Ramsauer ''et al.'' (2020), [https://arxiv.org/abs/2008.02217 "Hopfield Networks is All You Need"] {{웹아카이브|url=https://web.archive.org/web/20210918150812/https://arxiv.org/abs/2008.02217 |date=2021-09-18 }}, preprint submitted for [[International Conference on Learning Representations|ICLR]] 2021. {{arxiv|2008.02217}}; see also authors' [https://ml-jku.github.io/hopfield-layers/ blog] {{웹아카이브|url=https://web.archive.org/web/20210918150757/https://ml-jku.github.io/hopfield-layers/ |date=2021-09-18 }}
::– Discussion of the effect of a transformer layer as equivalent to a Hopfield update, bringing the input closer to one of the [[Fixed point (mathematics)|fixed points]] (representable patterns) of a continuous-valued [[Hopfield network]] -->
{{참고 자료 끝}}

== 각주 ==
;내용주
{{주하단}}

;참조주
{{각주}}

{{구글}}
{{위키데이터 속성 추적}}

[[분류:인공신경망]]
[[분류:구글의 소프트웨어]]
