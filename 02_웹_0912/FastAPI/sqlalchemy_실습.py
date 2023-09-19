from models import ItemInfo
from database import SessionLocal
import pandas as pd


db = SessionLocal()

#특정 아이디 조회하기
item = db.query(ItemInfo).filter(ItemInfo.item == "spot_1").first()

# Convert SQLAlchemy results to a list of dictionaries
data = item.__dict__

# Filter out the internal attribute _sa_instance_state that SQLAlchemy adds to its objects
data = [{k: v for k, v in data.items() if k != "_sa_instance_state"}]
data

# Convert to DataFrame
df = pd.DataFrame(data)

df






[{"TRAVEL_MISSION_1" : "호캉스 여행",
    "TRAVEL_MISSION_2" : "친환경 여행(플로깅 여행)",
    "TRAVEL_MISSION_3" : "missing",
    "TRAVEL_MISSION_4" : "missing",
    "TRAVEL_MISSION_5" : "missing",
    "TRAVEL_MISSION_6" : "missing",
    "TRAVEL_MISSION_7" : "missing",
    "TRAVEL_MISSION_8" : "missing",
    "TRAVEL_MISSION_9" : "missing",
    "TRAVEL_MISSION_10" : "missing",
    "TRAVEL_MISSION_11" : "missing",
    "TRAVEL_MISSION_12" : "missing",
    "TRAVEL_MISSION_13" : "missing",
    "TRAVEL_MISSION_14" : "missing",
    "TRAVEL_MISSION_15" : "missing",
    "TRAVEL_MISSION_16" : "missing",
    "TRAVEL_MISSION_17" : "missing",
    "TRAVEL_MISSION_18" : "missing",
    "TRAVEL_MISSION_19" : "missing",
    "TRAVEL_MISSION_20" : "missing",
    "TRAVEL_MISSION_21" : "missing",
    "GENDER" : "남",
    "AGE_GRP" : "20대",
    "TRAVEL_STATUS_ACCOMPANY" : "나홀로 여행",
    "TRAVEL_MOTIVE_1" : "새로운 경험 추구",
    "TRAVEL_MOTIVE_2" : "missing",
    "TRAVEL_MOTIVE_3" : "missing",
    "TRAVEL_STYL_1" : "자연중간선호",
    "TRAVEL_STYL_3" : "새로운지역매우선호",
    "TRAVEL_STYL_6" : "잘알려지지않은방문지약간선호",
    "ratings" : {"spot_5" : 1,  "spot_10" : 0, "spot_20" : 1}
}]



    new_user = recommendation_crud.make_new_user_data(db, new_user_info)
    rec_result = recommendation_crud.make_recommend(new_user)
    rec_data = recommendation_crud.return_recommendation(db, rec_result)