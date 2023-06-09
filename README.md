# streamlit_prac
# [1조] 카드 내역을 통한 소비 행태 분석

# 👩‍🦰 팀원 소개

- 김시아

- 민채영

- 박지현

# 💡 주제 선정 배경

경제학에서 배우는 개념 중에 80:20 법칙,  즉 ‘`파레토 법칙`’을 들어본 적이 있을 것이다. 한 카드회사의 1년치 카드 사용 데이터를 토대로 80:20의 법칙이 실제로 적용이 되는지 분석하고자 한다.   

<aside>
💡 **파레토 법칙이란?**

**파레토 법칙**( - 法則, [영어](https://ko.wikipedia.org/wiki/%EC%98%81%EC%96%B4): Pareto principle, law of the vital few, principle of factor sparsity)[[1]](https://ko.wikipedia.org/wiki/%ED%8C%8C%EB%A0%88%ED%86%A0_%EB%B2%95%EC%B9%99#cite_note-1)[[2]](https://ko.wikipedia.org/wiki/%ED%8C%8C%EB%A0%88%ED%86%A0_%EB%B2%95%EC%B9%99#cite_note-2) 또는 **80 대 20 법칙**([영어](https://ko.wikipedia.org/wiki/%EC%98%81%EC%96%B4): 80–20 rule)은 '전체 결과의 80%가 전체 원인의 20%에서 일어나는 현상을 가리킨다.[[3]](https://ko.wikipedia.org/wiki/%ED%8C%8C%EB%A0%88%ED%86%A0_%EB%B2%95%EC%B9%99#cite_note-NYT-3) 예를 들어, 20%의 고객이 백화점 전체 매출의 80%에 해당하는 만큼 쇼핑하는 현상을 설명할 때 이 용어를 사용한다. **2 대 8 법칙**라고도 한다.

</aside>

출처 | 위키백과 ‘파레토 법칙’

> 상위 20% 가 전체 수익 80%를 차지한다. 
20%의 우수한 사원이 회사 전체 매출이 80%를 이끈다. 
회사 핵심 제품 20%가 전체 매출 80%를 담당한다.
> 

→ 일상적인 일에서도 적용되는 법칙이다.

# 📃 데이터 개요

✔ Raw Data : 롯데카드 고객의 2021.01.01 ~ 2021.12.31 카드 사용 내역 데이터 

# 🔎 작업 과정

### (1) 전처리 : 3개의 Data Set에서 필요한 columns 추출 및 병합

1. 상품 구매 정보 : 
    
    **`cust`(고객번호)**, `rct_no`(영수증번호), `chnl_dv`(채널구분), `cop_c`(제휴사), `br_c`(점포코드), **`pd_c`(상품코드)**, **`de_dt`(구매일자), `de_hr`(구매시간)**, **`buy_am`(구매금액)**, `buy_ct`(구매수량)
    
2. 고객 정보 데이터 : ****
    
    **`cust` (고객번호)**, **`ma_fev_dv`(성별), `ages`(연령대)** ,`zon_hlv`(거주지 분류코드)
    
3. 상품 분류 정보 : ****
    
    **`pd_c` (상품코드)**, `pd_nm` (소분류명), **`clac_hlv_nm` (대분류명)**, `clac_mcls_nm` (중분류명)
    

![Untitled](%5B1%E1%84%8C%E1%85%A9%5D%20%E1%84%8F%E1%85%A1%E1%84%83%E1%85%B3%20%E1%84%82%E1%85%A2%E1%84%8B%E1%85%A7%E1%86%A8%E1%84%8B%E1%85%B3%E1%86%AF%20%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5%20%E1%84%92%E1%85%A2%E1%86%BC%E1%84%90%E1%85%A2%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20c229d3f30a45465c8534691e77d80906/Untitled.png)

### (2) EDA

1. **상품 품목 분석**
    - 상품 품목은 총 몇 개인가
        
        ```python
        df_cnt = collections.Counter(list(df.clac_hlv_nm))
        len(df_cnt)
        
        >>60
        ```
        
    - 가장 많이 구매한 품목은 무엇인가
        
        `('과자', 440223), ('채소', 423178), ('대용식', 311966), ('유제품', 284420), ('냉장식품', 266481), ('음료', 250179), ('과일', 231090), ('축산물', 190062), ('주류', 169834), ('테넌트/음식점', 166240)`
        
        ![newplot (4).png](%5B1%E1%84%8C%E1%85%A9%5D%20%E1%84%8F%E1%85%A1%E1%84%83%E1%85%B3%20%E1%84%82%E1%85%A2%E1%84%8B%E1%85%A7%E1%86%A8%E1%84%8B%E1%85%B3%E1%86%AF%20%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5%20%E1%84%92%E1%85%A2%E1%86%BC%E1%84%90%E1%85%A2%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20c229d3f30a45465c8534691e77d80906/newplot_(4).png)
        
    
    ![newplot (3).png](%5B1%E1%84%8C%E1%85%A9%5D%20%E1%84%8F%E1%85%A1%E1%84%83%E1%85%B3%20%E1%84%82%E1%85%A2%E1%84%8B%E1%85%A7%E1%86%A8%E1%84%8B%E1%85%B3%E1%86%AF%20%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5%20%E1%84%92%E1%85%A2%E1%86%BC%E1%84%90%E1%85%A2%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20c229d3f30a45465c8534691e77d80906/newplot_(3).png)
    
    - 30, 40대 여성이 주 고객층  👉 주고객층 타겟팅한 카드상품 출시 아이디어
    - 계층 별 구매 횟수가 높은 10가지 품목 👉 먹거리가 주된 소비로 차지하는 만큼, 편의점 또는 마트에서의 캐시백 혜택을 부여한 카드상품 출시로 경쟁력 강화
        
        ```
        20대 여성 [('과자', 17238), ('채소', 13535), ('음료', 12710), ('대용식', 11994), ('테넌트/음식점', 11091), ('냉장식품', 9048), ('유제품', 8955), ('주류', 7365), ('과일', 6412), ('조리식품', 5562)]
        
        30대 여성 [('과자', 81254), ('채소', 60240), ('대용식', 46789), ('유제품', 46699), ('냉장식품', 42304), ('음료', 38942), ('과일', 33613), ('테넌트/음식점', 32408), ('주류', 27388), ('축산물', 27368)]
        
        40대 여성 [('과자', 143484), ('채소', 123991), ('대용식', 99898), ('냉장식품', 87494), ('유제품', 84666), ('음료', 69911), ('과일', 66013), ('축산물', 59174), ('테넌트/음식점', 45772), ('주류', 44456)]
        
        50대 여성 [('채소', 80047), ('과자', 52049), ('대용식', 45744), ('유제품', 43526), ('과일', 41042), ('냉장식품', 37919), ('축산물', 33826), ('음료', 27886), ('조미료', 24014), ('테넌트/음식점', 23726)]
        
        60대 여성 [('채소', 29945), ('과일', 16115), ('유제품', 13680), ('과자', 13210), ('축산물', 11382), ('대용식', 10706), ('냉장식품', 9184), ('조미료', 8095), ('테넌트/음식점', 7438), ('음료', 5947)]
        
        70대 여성 [('채소', 9971), ('유제품', 5196), ('과일', 4773), ('축산물', 3468), ('과자', 3313), ('대용식', 3141), ('조미료', 2713), ('냉장식품', 2697), ('수산물', 2393), ('테넌트/음식점', 2087)]
        
        20대 남성 [('음료', 8211), ('과자', 6959), ('대용식', 5363), ('채소', 5074), ('냉장식품', 3916), ('주류', 3886), ('유제품', 3830), ('담배', 3370), ('테넌트/음식점', 3277), ('조리식품', 3053)]
        
        30대 남성 [('과자', 30841), ('음료', 25243), ('채소', 22349), ('대용식', 20736), ('유제품', 19361), ('냉장식품', 17733), ('주류', 16278), ('과일', 13039), ('테넌트/음식점', 12607), ('축산물', 10447)]
        
        40대 남성 [('과자', 61411), ('채소', 42094), ('대용식', 41260), ('음료', 39506), ('냉장식품', 35852), ('유제품', 35261), ('과일', 26143), ('주류', 24382), ('축산물', 20941), ('냉동식품', 17673)]
        
        50대 남성 [('채소', 23881), ('과자', 23555), ('대용식', 19635), ('냉장식품', 15980), ('유제품', 15671), ('음료', 15229), ('과일', 14562), ('주류', 13412), ('축산물', 11294), ('냉동식품', 7836)]
        
        60대 남성 [('채소', 8314), ('유제품', 4875), ('과자', 4763), ('대용식', 4719), ('과일', 4599), ('음료', 3384), ('축산물', 3287), ('냉장식품', 3108), ('주류', 3055), ('조미료', 2190)]
        
        70대 남성 [('채소', 3737), ('유제품', 2700), ('과일', 2421), ('과자', 2146), ('대용식', 1981), ('축산물', 1453), ('냉장식품', 1246), ('음료', 1218), ('조미료', 1192), ('주류', 906)]
        ```
        

**2. 가격 분석**

- pandas 프로파일링을 이용한 기본적인 파일 구조 파악
    - 최소값 : 1원 / 최대값 : 6,400만원
    - 중앙값 : 4,000원 / 평균값 : 23,212원
        - *평균값에 비해 중앙값이 낮아 구매금액이 낮은 쪽으로 치중되었다는 것을 알 수 있음*
    - 제1사분위수(25%) : 2,000원 / 제3사분위수(75%) : 9,280원
        - *자료를 4등분 하여 살펴봐도 구매가격이 낮은 쪽에 치중되어 있는 것을 알 수 있음*
    - 사분위범위(IQR) :  7,280원
        - *자료의 가운데 50%가 포함되는 구간의 길이로 이상치에 크게 영향을 받지 않음*

![Untitled](%5B1%E1%84%8C%E1%85%A9%5D%20%E1%84%8F%E1%85%A1%E1%84%83%E1%85%B3%20%E1%84%82%E1%85%A2%E1%84%8B%E1%85%A7%E1%86%A8%E1%84%8B%E1%85%B3%E1%86%AF%20%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5%20%E1%84%92%E1%85%A2%E1%86%BC%E1%84%90%E1%85%A2%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20c229d3f30a45465c8534691e77d80906/Untitled%201.png)

- 패션잡화의 소비가격이 다양한 것을 확인할 수 있음

![Untitled](%5B1%E1%84%8C%E1%85%A9%5D%20%E1%84%8F%E1%85%A1%E1%84%83%E1%85%B3%20%E1%84%82%E1%85%A2%E1%84%8B%E1%85%A7%E1%86%A8%E1%84%8B%E1%85%B3%E1%86%AF%20%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5%20%E1%84%92%E1%85%A2%E1%86%BC%E1%84%90%E1%85%A2%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20c229d3f30a45465c8534691e77d80906/Untitled%202.png)

- 패션잡화의 소비가격범위가 넓다는 것을 알 수 있음
    - *이상치 또한 대분류의 다른 카테고리에 비해 많음*

![newplot.png](%5B1%E1%84%8C%E1%85%A9%5D%20%E1%84%8F%E1%85%A1%E1%84%83%E1%85%B3%20%E1%84%82%E1%85%A2%E1%84%8B%E1%85%A7%E1%86%A8%E1%84%8B%E1%85%B3%E1%86%AF%20%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5%20%E1%84%92%E1%85%A2%E1%86%BC%E1%84%90%E1%85%A2%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20c229d3f30a45465c8534691e77d80906/newplot.png)

- 사분위수를 기준으로 한 이상치 제거 방법 이용
    - *데이터 표본을 4개의 동일한 부분으로 나눈 값*
    - *전체 데이터를 대상으로 제1사분위, 제3사분위를 제거하였음*
    
    ![Untitled](%5B1%E1%84%8C%E1%85%A9%5D%20%E1%84%8F%E1%85%A1%E1%84%83%E1%85%B3%20%E1%84%82%E1%85%A2%E1%84%8B%E1%85%A7%E1%86%A8%E1%84%8B%E1%85%B3%E1%86%AF%20%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5%20%E1%84%92%E1%85%A2%E1%86%BC%E1%84%90%E1%85%A2%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20c229d3f30a45465c8534691e77d80906/Untitled%203.png)
    
    - 출처 : 모두의 R 데이터 분석

- 4분위수를 이용한 이상치 제거 결과
    - *카테고리에 따라 차이는 있지만 일반적으로 20,000원 선 안에서 소비하는 것을 확인할 수 있음*
    - *이상치를 제거한 범위 내에 중앙값이 위치한 것을 확인할 수 있음*
    
    ![1newplot.png](%5B1%E1%84%8C%E1%85%A9%5D%20%E1%84%8F%E1%85%A1%E1%84%83%E1%85%B3%20%E1%84%82%E1%85%A2%E1%84%8B%E1%85%A7%E1%86%A8%E1%84%8B%E1%85%B3%E1%86%AF%20%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5%20%E1%84%92%E1%85%A2%E1%86%BC%E1%84%90%E1%85%A2%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20c229d3f30a45465c8534691e77d80906/1newplot.png)
    

### (3) 파레토 법칙

### ✔과정

(1) 총 고객 수와 `상위 20%`의 고객 수 구하기 

```python
cust_num = df['cust'].nunique() # 총 고객 수 : 26917
cust_num * 0.2  # 상위 20퍼의 고객 수 :5383
```

(2) `전체` 고객별 총 구매금액, `상위 20%` 고객별 총 구매금액 구하기 

```python
# 고객별 구매 총 금액 
df_buy= df.groupby('cust').sum('buy_am')

# 전체 고객별 구매 총 금액 (내림차순 정렬)
df_buy_sum= df_buy.sort_values('buy_am', ascending = False)
df_buy_sum

#상위 20퍼 고객별 구매 총 금액 (min 4139766, max 386581410)
df_buy_sum_20p = df_buy_sum.sort_values('buy_am', ascending = False)/n
									.head(round(cust_num*0.2))
df_buy_sum_20p
```

전체 고객 26,917 명에 대한 데이터

![Untitled](%5B1%E1%84%8C%E1%85%A9%5D%20%E1%84%8F%E1%85%A1%E1%84%83%E1%85%B3%20%E1%84%82%E1%85%A2%E1%84%8B%E1%85%A7%E1%86%A8%E1%84%8B%E1%85%B3%E1%86%AF%20%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5%20%E1%84%92%E1%85%A2%E1%86%BC%E1%84%90%E1%85%A2%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20c229d3f30a45465c8534691e77d80906/Untitled%204.png)

- Min 10
- Max 386,581,410(3억 8658만 1410원)

![Untitled](%5B1%E1%84%8C%E1%85%A9%5D%20%E1%84%8F%E1%85%A1%E1%84%83%E1%85%B3%20%E1%84%82%E1%85%A2%E1%84%8B%E1%85%A7%E1%86%A8%E1%84%8B%E1%85%B3%E1%86%AF%20%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5%20%E1%84%92%E1%85%A2%E1%86%BC%E1%84%90%E1%85%A2%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20c229d3f30a45465c8534691e77d80906/Untitled%205.png)

상위 20% 고객 5,383명에 대한 데이터 

- 상위 20%는 4백만원부터 4억 가까이 되는 금액으로 분포 범위가 매우 크다는 것을 알 수 있음.

(3) 그래프 구현

```python
import plotly.express as px
fig = px.histogram(df_buy_sum, x="buy_am" , 
                   labels=dict(buy_am="총구매금액"), 
                   range_x=[0, 20000000], 
                   height = 600, 
                   width = 600) 
fig.add_vline(x=5000000,
              line_width=3, 
              line_dash="dash",
              line_color="red")
fig.show()
```

- 전체 범위

![Untitled](%5B1%E1%84%8C%E1%85%A9%5D%20%E1%84%8F%E1%85%A1%E1%84%83%E1%85%B3%20%E1%84%82%E1%85%A2%E1%84%8B%E1%85%A7%E1%86%A8%E1%84%8B%E1%85%B3%E1%86%AF%20%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5%20%E1%84%92%E1%85%A2%E1%86%BC%E1%84%90%E1%85%A2%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20c229d3f30a45465c8534691e77d80906/Untitled%206.png)

- 0- 20M 범위 확대

![Untitled](%5B1%E1%84%8C%E1%85%A9%5D%20%E1%84%8F%E1%85%A1%E1%84%83%E1%85%B3%20%E1%84%82%E1%85%A2%E1%84%8B%E1%85%A7%E1%86%A8%E1%84%8B%E1%85%B3%E1%86%AF%20%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5%20%E1%84%92%E1%85%A2%E1%86%BC%E1%84%90%E1%85%A2%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20c229d3f30a45465c8534691e77d80906/Untitled%207.png)

전체 범위 중 유의미한 그래프 형태가 이루어지는 20M까지 범위를 설정하여 `롱테일 법칙`의 그래프와 유사한 형태가 그려진다는 결론을 도출하였다.  

### ✔결과

```python
# 전체 고객의 총 구매금액 
df['buy_am'].sum()
#>>>101711374397.0 (101,711,374,397원) #약 1000억원

# 전체 고객의 총 구매금액 의 80% 금액 (예측치)
df['buy_am'].sum() * 0.8
#>>>81369099517.6 (81,369,099,517.6원)

# 상위 20퍼 고객의 구매총금액의 합 (실제치)
df_buy_sum_20p['buy_am'].sum()
#>>>74531835126.0 (74,531,835,126원) 총 구매금액의 75%를 차지함 
```

### (4) 품목간 연관성 분석(Apriori알고리즘)

![Untitled](%5B1%E1%84%8C%E1%85%A9%5D%20%E1%84%8F%E1%85%A1%E1%84%83%E1%85%B3%20%E1%84%82%E1%85%A2%E1%84%8B%E1%85%A7%E1%86%A8%E1%84%8B%E1%85%B3%E1%86%AF%20%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5%20%E1%84%92%E1%85%A2%E1%86%BC%E1%84%90%E1%85%A2%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20c229d3f30a45465c8534691e77d80906/Untitled%208.png)

### ✔과정

1. [rct_no : 영수증 번호]를 기준으로 한번에 결제한 품목을 딕셔너리로 표현
    
    ![Untitled](%5B1%E1%84%8C%E1%85%A9%5D%20%E1%84%8F%E1%85%A1%E1%84%83%E1%85%B3%20%E1%84%82%E1%85%A2%E1%84%8B%E1%85%A7%E1%86%A8%E1%84%8B%E1%85%B3%E1%86%AF%20%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5%20%E1%84%92%E1%85%A2%E1%86%BC%E1%84%90%E1%85%A2%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20c229d3f30a45465c8534691e77d80906/Untitled%209.png)
    
2. 2개 이상 품목을 구매한 값 추출
    
    ![Untitled](%5B1%E1%84%8C%E1%85%A9%5D%20%E1%84%8F%E1%85%A1%E1%84%83%E1%85%B3%20%E1%84%82%E1%85%A2%E1%84%8B%E1%85%A7%E1%86%A8%E1%84%8B%E1%85%B3%E1%86%AF%20%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5%20%E1%84%92%E1%85%A2%E1%86%BC%E1%84%90%E1%85%A2%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20c229d3f30a45465c8534691e77d80906/Untitled%2010.png)
    
3. apriori알고리즘을 사용하여 품목 간 연관성이 높은 제품 파악

![Untitled](%5B1%E1%84%8C%E1%85%A9%5D%20%E1%84%8F%E1%85%A1%E1%84%83%E1%85%B3%20%E1%84%82%E1%85%A2%E1%84%8B%E1%85%A7%E1%86%A8%E1%84%8B%E1%85%B3%E1%86%AF%20%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%89%E1%85%A9%E1%84%87%E1%85%B5%20%E1%84%92%E1%85%A2%E1%86%BC%E1%84%90%E1%85%A2%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20c229d3f30a45465c8534691e77d80906/Untitled%2011.png)

→ 축산물을 구매할 때, 채소를 구매할 확률이 높음

→ 과일을 구매할 때 채소를 구매할 확률이 높음

# 📌 Trouble Shooting

**문제 1**

- [ ]  `**DtypeWarning**: Columns (4) have mixed types. Specify dtype option on import or set low_memory=False.`
    
    → 4번 column에 데이터 타입이 여러 종류
    
- **원인**
    
    컬럼에 NaN값이 섞여있었기 때문
    
- **해결**
    
    read_csv를 사용하여 불러 올 때 ‘low_memory=False’를 추가
    
    → 전체 열을 먼저 읽은 다음 적절한 유형을 결정한다는 뜻
    

**문제 2** 

- [ ]  대분류의 모든 카테고리가 한 그래프 안에 담기지 않음
- **원인**
    
    그래프에 기본으로 지정된 높이에 카테고리가 다 반영되지 못함
    
- **해결**
    
    height = 1000이상으로 지정
    
    ```python
    fig1 = px.box(price_df, # 데이터명(데이터프레임 형식)
                     x='buy_am', # x축에 들어갈 컬럼
                     y='clac_hlv_nm',
                     labels=dict(buy_am="구매금액(원)", clac_hlv_nm="대분류명"),
                     height=1200
                     )
    ```
    

**문제 3**

- [ ]  **`TypeError**: Object of type builtin_function_or_method is not JSON serializable`
    
    히스토그램의 x축의 범위를 조절하는 과정에서 `fig.update_xaxes(range=[min, max])` 방법은 오류가 발생 
    
    x축의 범위를 지정해서 확대해서 보고자 하는 과정에서 
    
- **원인**
    
    not JSON serializable 에러
    
- **해결**
    
    `fig= px.histogram` 함수 안에 `range_x=[0, 20000000]` 를 추가하는 방식으로 해결 
    

# ❗ 소감 및 피드백

**소감**

- 대용량 데이터를 다룸으로써 이론으로 배운 내용을 활용하며 실습하는데 큰 의미가 있었음
- 실제 구매 데이터를 통해서 경제학의 이론에 근접하게 증명하였을 때

**아쉬운 점** 

- 데이터에 거주지 분류코드가 있어서 지역적 특성도 파악하고 싶었으나 마스킹된 데이터이기 때문에 사용하기 어려웠음.
- 대용량 데이터를 다룸에도 불구하고 좀 더 다양하게 시각화 기법을 활용하지 못한 것에 대한 아쉬움이 있었음. 기법을 사용하는 것 자체보다도 유의미한 지표를 만들어내는 방법론을 생각해내는 것에 더 큰 어려움이 있었음
- 그래프 표현과 분석을 용이하게 하기 위해 상품 코드(1933개)가 아닌 대분류 코드(60개)를 사용한 점이 아쉬움.
    
    → 특히 연관성 분석에 있어서, 60개의 대분류 코드가 아닌 상품코드를 사용했다면 조금 더 구체적인 결과를 얻을 수 있었을 것
    
- 연관성 분석 시, 상대적으로 구매 확률이 높은 값들을 제거하고 분석을 했다면 더 흥미로운 인사이트를 발견할 수 있을 것
    - 전체 구매 데이터에서 채소와 과일의 구매량이 상대적으로 높음
        
        → 채소에 대한 확률이 높아서 다른 규칙들에 영향을 받을 수 있기 때문
        

# 👩‍🏫 연지샘 피드백

- 두괄식으로 분석 후 인사이트를 3-5 줄 정도 적어주는게 좋다
- 사람들의 시선이 좌측상단에서부터 우측하단으로 이동되기 때문에 좌측 상단에 중요 정보를 넣는 것이 좋다. 따라서 내림차순 형태로 정리하는 것이 더 좋을 것 (EDA 나이별 성별에 따른 그래프 참고)
- 대분류의 상위 10개의 상품코드를 가져와서 분석하거나
- 각 대분류별 상위 10개의 상품코드를 가져와서 분석하는 방법도 있음
