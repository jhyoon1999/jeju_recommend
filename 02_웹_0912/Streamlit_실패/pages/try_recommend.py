import streamlit as st
import pickle
import os
import pandas as pd
import random
import numpy as np
from lightfm.data import Dataset
from lightfm import LightFM

@st.cache_data
def get_user_features_name_meaning():
    data = pd.read_csv('data/user_features_name_meaning.csv')
    return data

user_features_name_meaning = get_user_features_name_meaning()

@st.cache_data
def get_spot_info() :
    data = pd.read_csv('data/spot_info.csv')
    return data

#spot_info = pd.read_csv(r'data\spot_info.csv')
spot_info = get_spot_info()
spot_info_list = spot_info['spot_id'].to_list()

@st.cache_data
def get_suggest():
    suggest_spot_list = random.sample(spot_info_list, 5)
    return suggest_spot_list

suggest_spot_list = get_suggest()


tab1, tab2 = st.tabs(['추천 요청서 작성', '추천 결과'])

with tab1 :
    with st.form(key = 'Request', clear_on_submit=False) :
        #### User Features ####
        #1. 성별
        gender_features_name = user_features_name_meaning[user_features_name_meaning['Category'] == '성별']
        gender_question_list = list(gender_features_name['meaning'])

        gender = st.selectbox('귀하의 성별을 선택해주세요.', gender_question_list)

        if gender :
            user_features_gender = list(gender_features_name[gender_features_name['meaning'] == gender]['user_features_name'])

        #2. 연령대
        age_features_name = user_features_name_meaning[user_features_name_meaning['Category'] == '연령대']
        age_question_list = list(age_features_name['meaning'])

        age = st.selectbox('귀하의 연령대를 선택해주세요', age_question_list)
        st.write(age)

        if age :
            user_features_age = list(age_features_name[age_features_name['meaning'] == age]['user_features_name'])

        #3. 여행동기
        motive_features_name = user_features_name_meaning[user_features_name_meaning['Category'] == '여행동기']
        motive_question_list = list(motive_features_name['meaning'])

        motive = st.multiselect('귀하의 여행동기를 선택해주세요.', motive_question_list)

        if motive :
            user_features_motive = list(motive_features_name[motive_features_name['meaning'].isin(motive)]['user_features_name'])

        #4. 동반현황
        accompany_features_name = user_features_name_meaning[user_features_name_meaning['Category'] == '동반현황']
        accompany_question_list = list(accompany_features_name['meaning'])

        accompany = st.selectbox('이번 여행의 동반현황을 선택해주세요.', accompany_question_list)

        if accompany :
            user_features_accompany = list(accompany_features_name[accompany_features_name['meaning'] == accompany]['user_features_name'])

        #5. 여행미션
        mission_features_name = user_features_name_meaning[user_features_name_meaning['Category'] == '여행미션']
        mission_question_list = list(mission_features_name['meaning'])

        mission = st.multiselect('이번 여행의 미션을 선택해주세요.', mission_question_list)

        if mission :
            user_features_mission = list(mission_features_name[mission_features_name['meaning'].isin(mission)]['user_features_name'])

        #6. 여행스타일_1
        style_1_features_name = user_features_name_meaning[user_features_name_meaning['Category'] == '여행스타일']
        style_1_features_name = style_1_features_name[style_1_features_name['user_features_name'].str.contains('TRAVEL_STYL_1')]
        style_1_question_list = list(style_1_features_name['meaning'])

        style_1 = st.selectbox('귀하의 여행스타일을 선택해주세요.', style_1_question_list)

        if style_1 :
            user_features_style_1 = list(style_1_features_name[style_1_features_name['meaning'] == style_1]['user_features_name'])

        #6. 여행스타일_2
        style_2_features_name = user_features_name_meaning[user_features_name_meaning['Category'] == '여행스타일']
        style_2_features_name = style_2_features_name[style_2_features_name['user_features_name'].str.contains('TRAVEL_STYL_2')]
        style_2_question_list = list(style_2_features_name['meaning'])

        style_2 = st.selectbox('귀하의 여행스타일을 선택해주세요.', style_2_question_list)

        if style_2 :
            user_features_style_2 = list(style_2_features_name[style_2_features_name['meaning'] == style_2]['user_features_name'])

        #6. 여행스타일_3
        style_3_features_name = user_features_name_meaning[user_features_name_meaning['Category'] == '여행스타일']
        style_3_features_name = style_3_features_name[style_3_features_name['user_features_name'].str.contains('TRAVEL_STYL_3')]
        style_3_question_list = list(style_3_features_name['meaning'])

        style_3 = st.selectbox('귀하의 여행스타일을 선택해주세요.', style_3_question_list)

        if style_3 :
            user_features_style_3 = list(style_3_features_name[style_3_features_name['meaning'] == style_3]['user_features_name'])

        #6. 여행스타일_4
        style_4_features_name = user_features_name_meaning[user_features_name_meaning['Category'] == '여행스타일']
        style_4_features_name = style_4_features_name[style_4_features_name['user_features_name'].str.contains('TRAVEL_STYL_4')]
        style_4_question_list = list(style_4_features_name['meaning'])

        style_4 = st.selectbox('귀하의 여행스타일을 선택해주세요.', style_4_question_list)

        if style_4 :
            user_features_style_4 = list(style_4_features_name[style_4_features_name['meaning'] == style_4]['user_features_name'])

        #6. 여행스타일_5
        style_5_features_name = user_features_name_meaning[user_features_name_meaning['Category'] == '여행스타일']
        style_5_features_name = style_5_features_name[style_5_features_name['user_features_name'].str.contains('TRAVEL_STYL_5')]
        style_5_question_list = list(style_5_features_name['meaning'])

        style_5 = st.selectbox('귀하의 여행스타일을 선택해주세요.', style_5_question_list)

        if style_5 :
            user_features_style_5 = list(style_5_features_name[style_5_features_name['meaning'] == style_5]['user_features_name'])

        #6. 여행스타일_6
        style_6_features_name = user_features_name_meaning[user_features_name_meaning['Category'] == '여행스타일']
        style_6_features_name = style_6_features_name[style_6_features_name['user_features_name'].str.contains('TRAVEL_STYL_6')]
        style_6_question_list = list(style_6_features_name['meaning'])

        style_6 = st.selectbox('귀하의 여행스타일을 선택해주세요.', style_6_question_list)

        if style_6 :
            user_features_style_6 = list(style_6_features_name[style_6_features_name['meaning'] == style_6]['user_features_name'])

        #6. 여행스타일_7
        style_7_features_name = user_features_name_meaning[user_features_name_meaning['Category'] == '여행스타일']
        style_7_features_name = style_7_features_name[style_7_features_name['user_features_name'].str.contains('TRAVEL_STYL_7')]
        style_7_question_list = list(style_7_features_name['meaning'])

        style_7 = st.selectbox('귀하의 여행스타일을 선택해주세요.', style_7_question_list)

        if style_7 :
            user_features_style_7 = list(style_7_features_name[style_7_features_name['meaning'] == style_7]['user_features_name'])

        #6. 여행스타일_8
        style_8_features_name = user_features_name_meaning[user_features_name_meaning['Category'] == '여행스타일']
        style_8_features_name = style_8_features_name[style_8_features_name['user_features_name'].str.contains('TRAVEL_STYL_8')]
        style_8_question_list = list(style_8_features_name['meaning'])

        style_8 = st.selectbox('귀하의 여행스타일을 선택해주세요.', style_8_question_list)

        if style_8 :
            user_features_style_8 = list(style_8_features_name[style_8_features_name['meaning'] == style_8]['user_features_name'])

        #### Ratings ####
        #1. 첫번째
        target_spot1 = suggest_spot_list[0]
        target_spot_dat1 = spot_info[spot_info['spot_id'] == target_spot1]

        st.subheader('첫번째 평가')
        st.write(target_spot_dat1)

        first_spot = st.select_slider('첫번째 관광지가 마음에 드시나요?', ['매우 불만족','불만족' , '보통' , '만족' ,  '매우 만족'])

        if first_spot == '매우 불만족' :
            first_spot_rate = 1
        elif first_spot == '불만족' :
            first_spot_rate = 2
        elif first_spot == '보통' :
            first_spot_rate = 3
        elif first_spot == '만족' :
            first_spot_rate = 4
        else :
            first_spot_rate = 5

        if first_spot_rate :
            ratings_first = {target_spot1: first_spot_rate}

        #2. 두번째
        target_spot2 = suggest_spot_list[1]
        target_spot_dat2 = spot_info[spot_info['spot_id'] == target_spot2]

        st.subheader('두번째 평가')
        st.write(target_spot_dat2)

        second_spot = st.select_slider('두번째 관광지가 정말 마음에 드시나요?', ['매우 불만족','불만족' , '보통' , '만족' ,  '매우 만족'])

        if second_spot == '매우 불만족' :
            second_spot_rate = 1
        elif second_spot == '불만족' :
            second_spot_rate = 2
        elif second_spot == '보통' :
            second_spot_rate = 3
        elif second_spot == '만족' :
            second_spot_rate = 4
        else :
            second_spot_rate = 5

        if second_spot_rate :
            ratings_second = {target_spot2 : second_spot_rate}

        #3. 세번째
        target_spot3 = suggest_spot_list[2]
        target_spot_dat3 = spot_info[spot_info['spot_id'] == target_spot3]

        st.subheader('세번째 평가')
        st.write(target_spot_dat3)

        third_spot = st.select_slider('세번째 관광지가 정말 마음에 드시나요?', ['매우 불만족','불만족' , '보통' , '만족' ,  '매우 만족'])

        if third_spot == '매우 불만족' :
            third_spot_rate = 1
        elif third_spot == '불만족' :
            third_spot_rate = 2
        elif third_spot == '보통' :
            third_spot_rate = 3
        elif third_spot == '만족' :
            third_spot_rate = 4
        else :
            third_spot_rate = 5

        if third_spot_rate :
            ratings_third = {target_spot3 : third_spot_rate}

        #4. 네번째
        target_spot4 = suggest_spot_list[3]
        target_spot_dat4 = spot_info[spot_info['spot_id'] == target_spot4]

        st.subheader('네번째 평가')
        st.write(target_spot_dat4)

        fourth_spot = st.select_slider('네번째 관광지가 정말 마음에 드시나요?', ['매우 불만족','불만족' , '보통' , '만족' ,  '매우 만족'])

        if fourth_spot == '매우 불만족' :
            fourth_spot_rate = 1
        elif fourth_spot == '불만족' :
            fourth_spot_rate = 2
        elif fourth_spot == '보통' :
            fourth_spot_rate = 3
        elif fourth_spot == '만족' :
            fourth_spot_rate = 4
        else :
            fourth_spot_rate = 5

        if fourth_spot_rate :
            ratings_fourth = {target_spot4 : fourth_spot_rate}

        #5. 다섯번째
        target_spot5 = suggest_spot_list[4]
        target_spot_dat5 = spot_info[spot_info['spot_id'] == target_spot5]

        st.subheader('다섯째 평가')
        st.write(target_spot_dat5)

        fifth_spot = st.select_slider('다섯번째 관광지가 정말 마음에 드시나요?', ['매우 불만족','불만족' , '보통' , '만족' ,  '매우 만족'])

        if fifth_spot == '매우 불만족' :
            fifth_spot_rate = 1
        elif fifth_spot == '불만족' :
            fifth_spot_rate = 2
        elif fifth_spot == '보통' :
            fifth_spot_rate = 3
        elif fifth_spot == '만족' :
            fifth_spot_rate = 4
        else :
            fifth_spot_rate = 5

        if fifth_spot_rate :
            ratings_fifth = {target_spot5 : fifth_spot_rate}
        
        submitted = st.form_submit_button('추천요청')
        if submitted :
            new_user_features = user_features_gender + user_features_age + user_features_accompany + user_features_motive + user_features_mission + user_features_style_1 + user_features_style_2 + user_features_style_3 + user_features_style_4 + user_features_style_5 + user_features_style_6 + user_features_style_7 + user_features_style_8
            new_user_ratings = {**ratings_first, **ratings_second, **ratings_third, **ratings_fourth, **ratings_fifth}

### 두번째 페이지
#1. ratings_data
ratings_data = pd.read_csv('data/ratings.csv')

#2. user_features
with open('data/user_features.pkl', 'rb') as f:
    user_features = pickle.load(f)

with open('data/user_features_name.pkl', 'rb') as f:
    user_features_name = pickle.load(f)

#3. item_features
with open('data/item_features.pkl', 'rb') as f:
    item_features = pickle.load(f)

with open('data/item_features_name.pkl', 'rb') as f:
    item_features_name = pickle.load(f)

#4. 파라미터 정보
with open('data/parameter_info.pkl', 'rb') as f:
    parameter_info = pickle.load(f)

with tab2 :
    if new_user_features :
        new_user_id = "new_user_id"
        user_features.append((new_user_id, new_user_features))
        new_user_ratings_list = list(new_user_ratings.items())
        new_user_ratings_dat = pd.DataFrame(new_user_ratings_list, columns = ['spot_id', 'rating'])
        new_user_ratings_dat['TRAVEL_ID'] = new_user_id
        new_user_ratings_dat = new_user_ratings_dat[new_user_ratings_dat['rating'] > 3]
        ratings_data_new = pd.concat([ratings_data, new_user_ratings_dat])
        
        dataset = Dataset()
        
        #1. fit
        dataset.fit(users = ratings_data_new['TRAVEL_ID'],
                    items = ratings_data_new['spot_id'],
                    user_features = user_features_name,
                    item_features = item_features_name)
        #2. interactions
        interactions, weights = dataset.build_interactions((x[1], x[0]) for x in ratings_data_new.values)

        #3. item_features
        item_features_input = dataset.build_item_features(item_features)

        #4. user_features
        user_features_input = dataset.build_user_features(user_features)
        
        #모델링
        model = LightFM(no_components=parameter_info['no_component'],
                            learning_rate=parameter_info['learning_rate'],
                            loss=parameter_info['loss'],
                            item_alpha=parameter_info['item_alpha'],
                            user_alpha=parameter_info['user_alpha'],
                            learning_schedule=parameter_info['learning_schedule'])
        model.fit(interactions = interactions,
                user_features = user_features_input,
                item_features = item_features_input,
                epochs = 10,
                num_threads = 4)
        #예측
        new_user_internal_id = dataset.mapping()[0]["new_user_id"]
        def top_k_recommendations(model, user_id, nitem = len(dataset.mapping()[2]) ,k = 5) :
            user_id_input = np.full(nitem, user_id)
            scores = model.predict(user_id_input, np.arange(nitem))
            top_items = np.argsort(-scores)[:k]
            return list(top_items)
        
        recommend_spot_list = top_k_recommendations(model, new_user_internal_id)
        st.write(recommend_spot_list)








