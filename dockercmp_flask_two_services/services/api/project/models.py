"""database models"""
from project import db

class DataPoint(db.Model):
    """Schema for air quality data point."""

    __tablename__ = 'datapoint'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    pm = db.Column(
        db.Float,
        unique=False,
        nullable=False
    )
    time = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )

    def __repr__(self):
        return f'<DataPoint {self.time}, {self.pm}>'
