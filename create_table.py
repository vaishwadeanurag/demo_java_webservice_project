"""
Connects to a mysql database and creates few tables
expects a db with name flight_reservation_db
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine,
                        Column,
                        Integer,
                        String,
                        DateTime,
                        ForeignKey,
                        Float,
                        func,
                        Boolean)
import datetime

engine = create_engine('mysql://root:@localhost/flight_reservation_db', echo=True)

Base = declarative_base()


class User(Base):

    """
    Stores user details for flight reservation system
    """
    __tablename__ = 'user'

    user_idn = Column(Integer, primary_key=True, nullable=False)
    user_name = Column(String(200))
    user_email = Column(String(300))
    user_password = Column(String(300))
    user_phone = Column(String(30))
    active = Column(Boolean, default=True)
    update_date = Column(DateTime, onupdate=datetime.datetime.now)
    create_date = Column(DateTime, default=func.now())

class LocationDetail(Base):

    """
    Strore Location information
    """
    __tablename__ = 'location'

    location_idn = Column(Integer, primary_key=True, nullable=False)
    location_name = Column(String(200))
    created_by = Column(Integer, ForeignKey("user.user_idn"), nullable=False)
    updated_by = Column(Integer, ForeignKey("user.user_idn"), nullable=False)
    active = Column(Boolean, default=True)
    update_date = Column(DateTime, onupdate=datetime.datetime.now)
    create_date = Column(DateTime, default=func.now())


class FlightDetail(Base):

    """
    This class represents the flight_detail table which will hold
    the flight information
    """
    __tablename__ = 'flight_detail'

    flight_idn = Column(Integer, primary_key=True, nullable=False)
    flight_name = Column(String(200))
    flight_from = Column(Integer, ForeignKey("location.location_idn"), nullable=False)
    flight_to = Column(Integer, ForeignKey("location.location_idn"), nullable=False)
    journey_start_time = Column(DateTime)
    journey_end_time = Column(DateTime)
    total_no_of_seats = Column(Integer)
    base_fare = Column(Float)
    created_by = Column(Integer, ForeignKey("user.user_idn"), nullable=False)
    updated_by = Column(Integer, ForeignKey("user.user_idn"), nullable=False)
    active = Column(Boolean, default=True)
    update_date = Column(DateTime, onupdate=datetime.datetime.now)
    create_date = Column(DateTime, default=func.now())


class ReservationDetails(Base):

    """
    Stores reservation details for flight and locations
    """
    __tablename__ = 'reservation_details'
    reservation_idn = Column(Integer, primary_key=True)
    flight_no = Column(Integer, ForeignKey("flight_detail.flight_idn"), nullable=False)
    total_fare = Column(Float)
    reserved_by = Column(Integer, ForeignKey("user.user_idn"), nullable=False)
    active = Column(Boolean, default=True)
    update_date = Column(DateTime, onupdate=datetime.datetime.now)
    create_date = Column(DateTime, default=func.now())


class PassengerDetails(Base):
    """
    Stores information for passenges travelling in one flight ticket
    """
    __tablename__ = 'passenger_details'
    passenger_idn = Column(Integer, primary_key=True)
    reservation_idn = Column(Integer, ForeignKey("reservation_details.reservation_idn"), nullable=False)
    passenger_name = Column(String(200))
    passenger_age = Column(Integer)


Base.metadata.create_all(engine)
