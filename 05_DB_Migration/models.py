from sqlalchemy import Column,  String, ForeignKey, Float, Integer
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

#1. item_features
class ItemFeatures(Base):
    __tablename__ = "item_features"
    
    index = Column(Integer, primary_key=True, index=True)
    new_spot_id	= Column(String(256),  index=True)
    spot_id = Column(String(256), nullable=True)
    VISIT_AREA_NM= Column(String(256), nullable=True)
    rename= Column(String(256), nullable=True)
    address_name= Column(String(256), nullable=True)
    category_name= Column(String(256), nullable=True)
    place_name= Column(String(256), nullable=True)
    place_url= Column(String(256), nullable=True)
    x= Column(String(256), nullable=True)
    y= Column(String(256), nullable=True)
    category_name_1= Column(String(256), nullable=True)
    category_name_2= Column(String(256), nullable=True)
    category_name_3= Column(String(256), nullable=True)
    category_name_4= Column(String(256), nullable=True)
    category_name_5= Column(String(256), nullable=True)
    RESIDENCE_TIME_MIN= Column(Float, nullable=True)
    VISIT_CHC_REASON_가기_편해서_교통이_좋아서= Column(Integer, nullable=True)
    VISIT_CHC_REASON_가성비가_좋아서= Column(Integer, nullable=True)
    VISIT_CHC_REASON_과거_경험이_좋아서= Column(Integer, nullable=True)
    VISIT_CHC_REASON_교육성이_좋아서= Column(Integer, nullable=True)
    VISIT_CHC_REASON_기타= Column(Integer, nullable=True)
    VISIT_CHC_REASON_미디어_TV_정보_프로그램_등_평가가_좋아서= Column(Integer, nullable=True)
    VISIT_CHC_REASON_온라인_SNS_블로그_등_평가가_좋아서= Column(Integer, nullable=True)	
    VISIT_CHC_REASON_지나가다_우연히= Column(Integer, nullable=True)
    VISIT_CHC_REASON_지명도_명소_핫플레이스= Column(Integer, nullable=True)
    VISIT_CHC_REASON_지인의_추천이_있어서= Column(Integer, nullable=True)
    VISIT_CHC_REASON_편의시설_서비스가_좋아서= Column(Integer, nullable=True)
    DGSTFN= Column(Float, nullable=True)	
    REVISIT_INTENTION= Column(Float, nullable=True)
    RCMDTN_INTENTION= Column(Float, nullable=True)
    VISIT_AREA_TYPE_CD_레저_스포츠_관련_시설_스키_카트_수상레저= Column(Integer, nullable=True)
    VISIT_AREA_TYPE_CD_문화_시설_공연장_영화관_전시관_등= Column(Integer, nullable=True)
    VISIT_AREA_TYPE_CD_산책로_둘레길_등= Column(Integer, nullable=True)
    VISIT_AREA_TYPE_CD_상업지구_거리_시장_쇼핑시설= Column(Integer, nullable=True)
    VISIT_AREA_TYPE_CD_역사_유적_종교_시설_문화재_박물관_촬영지_절_등= Column(Integer, nullable=True)
    VISIT_AREA_TYPE_CD_자연관광지= Column(Integer, nullable=True)
    VISIT_AREA_TYPE_CD_지역_축제_행사= Column(Integer, nullable=True)
    VISIT_AREA_TYPE_CD_체험_활동_관광지= Column(Integer, nullable=True)
    VISIT_AREA_TYPE_CD_테마시설_놀이공원_워터파크= Column(Integer, nullable=True)

#2. ratings
class Ratings(Base):
    __tablename__ = "ratings"
    
    index = Column(Integer, primary_key=True, index=True)
    TRAVEL_ID = Column(String(256),  index=True)	
    new_spot_id	= Column(String(256), ForeignKey("item_features.new_spot_id"))
    item_features = relationship("ItemFeatures", backref="ratings")
    rating= Column(Float, nullable=False)
