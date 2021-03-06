# coding=utf-8
from flask_login import UserMixin

from main import db


VolunteerRole = db.Table('volunteer_role_mapping', db.Model.metadata,
    db.Column('volunteer_id', db.Integer, db.ForeignKey('volunteer.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('volunteer_role.id'), primary_key=True))


class Volunteer(db.Model, UserMixin):
    __table_name__ = 'volunteer'

    __versioned__ = {}

    id = db.Column(db.Integer, primary_key=True)
    planned_arrival = db.Column(db.DateTime)
    planned_departure = db.Column(db.DateTime)
    nickname = db.Column(db.String)
    missing_shifts_opt_in = db.Column(db.Boolean, nullable=False, default=False)
    banned = db.Column(db.Boolean, nullable=False, default=False)
    volunteer_phone = db.Column(db.String, nullable=False)
    volunteer_email = db.Column(db.String)
    age = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref='volunteer')

    roles = db.relationship('Role', backref='users', secondary=VolunteerRole, lazy='dynamic')

    @classmethod
    def get_for_user(cls, user):
        return cls.query.filter_by(user_id=user.id).first()


"""
class Messages(db.Model):
    from_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    to_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    sent = db.Column(db.DateTime)
    text = db.Column(db.String)
    is_read = db.Column(db.Boolean, nullable=False, default=False)
    shift_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
"""

