from sqlalchemy import Column,  String
from database import Base


#1. Item_info
class ItemInfo(Base):
    __tablename__ = 'item_info'
    
    item = Column(String(100), primary_key=True, nullable=False, index = True)
    name = Column(String(100), nullable=False)
    place_name	= Column(String(100), nullable=False)
    address_name = Column(String(100), nullable=False)
    category_name = Column(String(100), nullable=False)
    place_url = Column(String(100), nullable=False)
    x = Column(String(256), nullable=False)
    y = Column(String(256), nullable=False)	
    RESIDENCE_TIME_MIN= Column(String(256), nullable=False)	
    VISIT_AREA_TYPE_CD_1 = Column(String(256), nullable=False)	
    VISIT_AREA_TYPE_CD_2 = Column(String(256), nullable=False)		
    VISIT_AREA_TYPE_CD_3 = Column(String(256), nullable=False)		
    VISIT_AREA_TYPE_CD_4 = Column(String(256), nullable=False)	
    VISIT_AREA_TYPE_CD_5 = Column(String(256), nullable=False)	
    VISIT_AREA_TYPE_CD_6 = Column(String(256), nullable=False)		
    VISIT_AREA_TYPE_CD_7 = Column(String(256), nullable=False)		
    VISIT_AREA_TYPE_CD_8 = Column(String(256), nullable=False)	
    REVISIT_INTENTION= Column(String(256), nullable=False)	
    RCMDTN_INTENTION= Column(String(256), nullable=False)	
