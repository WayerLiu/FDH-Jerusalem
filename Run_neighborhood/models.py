#encoding:utf-8

from exts import db


# 定义微博模型
class Neighbor(db.Model):
    __tablename__ = 'neighbor_total_list'
    index = db.Column(db.Integer, primary_key=True)
    Neighborhood = db.Column(db.String(50), nullable=False)
    Original_year_info = db.Column(db.String(20), nullable=False)
    Year_founded = db.Column(db.Integer, nullable=False)
    Inhabitants = db.Column(db.String(50), nullable=False)
    Initiative = db.Column(db.String(50), nullable=False)
    Remarks = db.Column(db.String(20), nullable=False)
    Type = db.Column(db.String(20), nullable=False)
    # Notes = db.Column(db.String(20), nullable=False)
    source_book = db.Column(db.Boolean)
    links = db.Column(db.String(200), nullable=False)
    source_NoJ = db.Column(db.Boolean)
    source_LoP = db.Column(db.Boolean)
    coord_urls = db.Column(db.String(200), nullable=False)
    latitudes = db.Column(db.String(20), nullable=False)
    longitudes = db.Column(db.String(20), nullable=False)
    latitudes_g = db.Column(db.Float, nullable=False)
    longitudes_g = db.Column(db.Float, nullable=False)
    Other_name = db.Column(db.String(50), nullable=False)
    is_othername = db.Column(db.Boolean)


