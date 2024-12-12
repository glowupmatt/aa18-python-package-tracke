from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Package(db.Model):
    __tablename__ = 'packages'
    
    id = db.Column(db.Integer, primary_key=True)
    sender_name = db.Column(db.String(20), index=True, nullable=False)
    recipient_name = db.Column(db.String(20), index=True, nullable=False)
    origin = db.Column(db.String(20), index=True, nullable=False)
    destination = db.Column(db.String(20), index=True, nullable=False)
    express_shipping = db.Column(db.String(20), index=True, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'sender_name': self.sender_name,
            'recipient_name': self.recipient_name,
            'origin': self.origin,
            'destination': self.destination,
            'express_shipping': self.express_shipping
        }